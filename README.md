🧠 Conversational Code Generator

A full-stack AI-powered conversational code generation system that generates clean, well-documented code based on user prompts. The system validates ambiguous inputs, maintains limited conversational context for refinements, handles errors gracefully, includes automated tests, and is fully deployed.


</n>
</n>
</n>

🚀 Features

🧑‍💻 Generate code in Python, JavaScript, and Java

🔍 Detects ambiguous or insufficient prompts

🧠 Supports context-aware refinements (e.g., “make it recursive”)

⚠️ User-friendly error handling and feedback

🧪 Automated backend tests using Pytest

🌐 Frontend–Backend integration

☁️ Deployed using Render (backend) and Vercel (frontend)

🛠️ Tech Stack
Frontend

React

CSS

Fetch API

Backend

FastAPI

AutoGen (LLM agent framework)

Python

Uvicorn

Testing

Pytest

FastAPI TestClient

Deployment

Backend: Render

Frontend: Vercel

Version Control: Git & GitHub

📂 Project Structure
ai_codegen/
│
├── backend/
│   ├── main.py
│   ├── agents.py
│   ├── schemas.py
│   ├── utils.py
│   ├── requirements.txt
│   └── tests/
│       └── test_generate.py
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   └── App.css
│   └── package.json
│
└── README.md

⚙️ How It Works

User enters a prompt and selects a programming language

Frontend sends the request to the FastAPI backend

Backend:

Validates prompt length

Detects ambiguity

Maintains limited chat history

Generates code using an AI agent

Generated code is returned and displayed with:

Syntax formatting

Copy-to-clipboard support

Errors and feedback are shown clearly to the user

🧠 Prompt Validation Examples
❌ Ambiguous Prompt
write me a code


Response:

❗ Your request is ambiguous. Please specify what the code should do.

✅ Valid Prompt
Write a Python function to reverse a string

🔁 Refinement Prompt
make it recursive


The system modifies the previously generated code accordingly.

🧪 Running Tests

Navigate to the project root and run:

pytest

✅ Expected Output
4 passed, 1 warning


All core backend behaviors are validated through automated tests.

🌐 Deployment
Backend (Render)

FastAPI app deployed with Uvicorn

Environment variables used for API keys

Public endpoint exposed

Frontend (Vercel)

React app deployed

Backend URL configured using environment variables

🔐 Security

API keys are stored securely using environment variables

.env files are excluded from version control

GitHub push protection enabled

📸 Screenshots (For Evaluation)

Backend live on Render

Frontend generating code

Error handling example

Context-based refinement example

Test cases passing

GitHub repository structure

📌 Future Improvements

Syntax highlighting for generated code

Support for additional programming languages

Persistent chat history using a database

Authentication and user sessions

👨‍💻 Author

Taranjot Singh Dhingra
Intern Project – AI Code Generation System
