# SYNAPSE: The Agentic Knowledge Workspace

An AI-powered knowledge management and analysis platform that transforms your documents into an intelligent knowledge base with semantic search, AI-powered analysis, and agentic workflows.

## 🚀 Features

- **AI-Powered Search**: Find exactly what you need with semantic search across all your documents.
- **Document Analysis**: Extract key insights and summaries from your documents automatically.
- **Agentic Workflows**: Let AI agents process and analyze your content automatically.
- **Multi-Format Support**: Upload PDF and TXT documents for processing.
- **Modern UI**: Clean, responsive interface built with Next.js and Tailwind CSS.

## 🛠️ Tech Stack

- **Frontend**: Next.js 14/15, TypeScript, Tailwind CSS
- **Backend**: Next.js API Routes
- **Vector Database**: Pinecone
- **AI/ML**: LangGraph.js, Groq Llama-3.1/3.3, OpenAI GPT-4/4o
- **File Processing**: pdf-parse, PyPDFLoader

## 🚀 Getting Started

### Prerequisites

- Node.js 18+ and npm
- Pinecone account and API key
- Groq API key
- OpenAI API key (optional, for fallback)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/synapse.git
   cd synapse
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   - Copy `.env.example` to `.env.local`
   - Fill in your API keys and configuration

4. Run the development server:
   ```bash
   npm run dev
   ```

5. Open [http://localhost:3000](http://localhost:3000) in your browser.

## 📂 Project Structure

```
synapse/
├── app/                    # Next.js app directory
│   ├── api/                # API routes
│   ├── globals.css         # Global styles
│   ├── layout.tsx          # Root layout
│   └── page.tsx            # Home page
├── components/             # Reusable components
│   └── ui/                 # Shadcn UI components
├── lib/                    # Utility functions and configurations
│   ├── rag/                # RAG pipeline components
│   └── langgraph/          # LangGraph agent components
├── public/                 # Static files
├── types/                  # TypeScript type definitions
└── utils/                  # Utility functions
```

## 🌐 Deployment

### Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fyourusername%2Fsynapse)

1. Fork this repository
2. Connect your Vercel account to your GitHub repository
3. Add your environment variables in the Vercel dashboard
4. Deploy!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/synapse](https://github.com/yourusername/synapse)
