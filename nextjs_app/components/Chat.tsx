"use client";

import { useState } from 'react';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

export default function Chat() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');

  const handleSend = async () => {
    if (!input) return;

    const newMessages = [...messages, { role: 'user', content: input }];
    setMessages(newMessages);
    setInput('');

    const response = await fetch(`http://localhost:8000/query?question=${encodeURIComponent(input)}`);
    if (!response.body) return;

    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let fullResponse = '';

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      fullResponse += decoder.decode(value, { stream: true });
      setMessages([...newMessages, { role: 'assistant', content: fullResponse }]);
    }
  };

  return (
    <div className="w-full p-4 mt-10 border rounded-lg">
      <h2 className="text-2xl font-bold mb-4">Chat</h2>
      <div className="flex flex-col space-y-4 h-96 overflow-y-auto">
        {messages.map((msg, index) => (
          <div key={index} className={`p-2 rounded-lg ${msg.role === 'user' ? 'bg-blue-200 self-end' : 'bg-gray-200 self-start'}`}>
            {msg.content}
          </div>
        ))}
      </div>
      <div className="flex items-center mt-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
          className="flex-grow p-2 border rounded-lg"
          placeholder="Ask a question..."
        />
        <button onClick={handleSend} className="px-4 py-2 ml-4 bg-blue-500 text-white rounded-lg">
          Send
        </button>
      </div>
    </div>
  );
}
