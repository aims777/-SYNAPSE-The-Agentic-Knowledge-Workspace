import Chat from "../components/Chat";
import FileUpload from "../components/FileUpload";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div className="z-10 w-full max-w-5xl items-center justify-between font-mono text-sm lg:flex">
        <h1 className="text-4xl font-bold">⭐ SYNAPSE – The Agentic Knowledge Workspace</h1>
      </div>

      <div className="w-full max-w-5xl mt-10">
        <FileUpload />
        <Chat />
      </div>
    </main>
  );
}
