import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const { question } = await req.json();

  const response = await fetch(`http://localhost:8000/query?question=${encodeURIComponent(question)}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
  });

  return new NextResponse(response.body, {
    headers: {
      'Content-Type': 'text/event-stream',
    },
  });
}
