import React, { useState } from "react";
import "./App.css";

function App() {
  const [prompt, setPrompt] = useState("");
  const [language, setLanguage] = useState("Python");
  const [code, setCode] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");


  const generateCode = async () => {
  if (!prompt.trim()) {
    setError("Please enter a prompt.");
    setCode("");
    return;
  }

  setLoading(true);
  setError("");
  setSuccess("");
  setCode("");

  try {
    const response = await fetch("http://127.0.0.1:8000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, language }),
    });

    const data = await response.json();

    if (data.code) {
      setCode(data.code);
      setSuccess("Code generated successfully.");
    } else {
      setError(data.explanation || "Something went wrong.");
    }
  } catch {
    setError("Error connecting to backend.");
  }

  setLoading(false);
};

const copyToClipboard = () => {
  navigator.clipboard.writeText(code);
  setSuccess("Code copied to clipboard!");
};


  return (
    <div className="app-container">
      <div className="card">
        <h1 className="title">Conversational Code Generator</h1>

        <label className="label">Prompt</label>
        <textarea
          rows="5"
          placeholder="e.g. Write a Python function to reverse a string"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <label className="label">Language</label>
        <select
          value={language}
          onChange={(e) => setLanguage(e.target.value)}
        >
          <option>Python</option>
          <option>JavaScript</option>
          <option>Java</option>
        </select>

        <br />

        <button onClick={generateCode} disabled={loading}>
          {loading ? "Generating..." : "Generate Code"}
        </button>

        <div className="output-container">
          <label className="label">Generated Code</label>

          {error && <div className="error-box">{error}</div>}
          {success && <div className="success-box">{success}</div>}

          {code ? (
          <>
        <div className="code-header">
          <span className="badge">{language}</span>
          <button className="copy-btn" onClick={copyToClipboard}>
             Copy
          </button>
      </div>
      <pre>{code}</pre>
    </>
  ) : (
    <div className="placeholder">
      Generated code will appear here...
    </div>
  )}
</div>

      </div>
    </div>
  );
}

export default App;
