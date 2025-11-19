from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import uvicorn
import os
import tempfile
from ..rag.loader import load_documents
from ..rag.splitter import split_documents
from ..rag.vectorstore import add_documents
from ..agent.graph import app as agent_app
from ..config import API_HOST, API_PORT

app = FastAPI(
    title="Synapse - The Agentic Knowledge Workspace",
    description="A full RAG + Agent system with Streamlit and Next.js frontends.",
    version="1.0.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(file.filename)[1]) as tmp_file:
            content = await file.read()
            tmp_file.write(content)
            tmp_file_path = tmp_file.name
        
        # Load, split, and add documents to the vector store
        docs = load_documents(tmp_file_path)
        split_docs = split_documents(docs)
        add_documents(split_docs)
        
        os.remove(tmp_file_path)
        return {"message": f"Successfully uploaded and processed {file.filename}"}
    except Exception as e:
        return {"error": str(e)}

@app.post("/query")
async def query(question: str):
    async def stream_response():
        async for event in agent_app.astream_events(
            {"question": question},
            version="v1"
        ):
            kind = event["event"]
            if kind == "on_chat_model_stream":
                content = event["data"]["chunk"].content
                if content:
                    yield content

    return StreamingResponse(stream_response(), media_type="text/event-stream")


def run():
    uvicorn.run(app, host=API_HOST, port=API_PORT)

if __name__ == "__main__":
    run()
