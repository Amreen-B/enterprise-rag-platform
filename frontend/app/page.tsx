"use client";

import { useState } from "react";

export default function Home() {

  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function askQuestion() {

    setLoading(true);

    try {

      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          question:question
        })
      });

      const data = await response.json();

      setAnswer(data.answer);

    } catch (error) {

      setAnswer("Error connecting to backend.");

    }

    setLoading(false);
  }

  return (
    <main className="min-h-screen bg-black text-white flex flex-col items-center p-10">

      <h1 className="text-5xl font-bold mb-10">
        Enterprise AI Assistant
      </h1>

      <div className="w-full max-w-4xl">

        <textarea
          className="w-full h-40 p-4 rounded-2xl bg-zinc-900 border border-zinc-700 outline-none"
          placeholder="Ask questions about your documents..."
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button
          onClick={askQuestion}
          className="mt-4 bg-white text-black px-6 py-3 rounded-2xl font-bold"
        >
          {loading ? "Thinking..." : "Ask AI"}
        </button>

        <div className="mt-10 p-6 bg-zinc-900 rounded-2xl border border-zinc-700 whitespace-pre-wrap min-h-[200px]">
          {answer}
        </div>

      </div>

    </main>
  );
}