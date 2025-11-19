import Link from 'next/link';
import { Button } from '@/components/ui/button';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-b from-background to-muted/20 p-4">
      <div className="max-w-4xl mx-auto text-center space-y-8">
        <h1 className="text-5xl font-bold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-primary to-primary/80">
          SYNAPSE
        </h1>
        <p className="text-xl text-muted-foreground max-w-2xl mx-auto">
          The Agentic Knowledge Workspace
        </p>
        
        <div className="space-y-4 pt-8">
          <p className="text-lg text-muted-foreground">
            Transform your documents into an intelligent knowledge base with AI-powered search, analysis, and insights.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
            <Button size="lg" asChild>
              <Link href="/workspace">
                Start Workspace
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="20"
                  height="20"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  className="ml-2"
                >
                  <path d="M5 12h14"></path>
                  <path d="m12 5 7 7-7 7"></path>
                </svg>
              </Link>
            </Button>
            
            <Button variant="outline" size="lg" asChild>
              <a href="#features">Learn More</a>
            </Button>
          </div>
        </div>
      </div>
      
      <div id="features" className="w-full max-w-6xl mx-auto mt-24 px-4">
        <h2 className="text-3xl font-bold text-center mb-12">Powerful Features</h2>
        
        <div className="grid md:grid-cols-3 gap-8">
          {[
            {
              title: 'AI-Powered Search',
              description: 'Find exactly what you need with semantic search across all your documents.',
              icon: '🔍',
            },
            {
              title: 'Document Analysis',
              description: 'Extract key insights and summaries from your documents automatically.',
              icon: '📊',
            },
            {
              title: 'Agentic Workflows',
              description: 'Let AI agents process and analyze your content automatically.',
              icon: '🤖',
            },
          ].map((feature, index) => (
            <div key={index} className="bg-card p-6 rounded-lg border border-border">
              <div className="text-4xl mb-4">{feature.icon}</div>
              <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
              <p className="text-muted-foreground">{feature.description}</p>
            </div>
          ))}
        </div>
      </div>
      
      <footer className="w-full border-t border-border mt-24 py-8">
        <div className="container mx-auto px-4 text-center text-sm text-muted-foreground">
          <p>© {new Date().getFullYear()} SYNAPSE. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}
