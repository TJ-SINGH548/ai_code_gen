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
<img width="907" height="854" alt="backend_render_live" src="https://github.com/user-attachments/assets/ae6d0729-24c7-4b92-859d-a7254b977d67" />

Frontend generating code
<img width="906" height="850" alt="frontend_generation" src="https://github.com/user-attachments/assets/247a48a9-72d0-4ecc-84ed-3527bd2f3b24" />

Error handling example
<img width="902" height="531" alt="error_handling" src="https://github.com/user-attachments/assets/5ef91529-dc66-481d-9b06-0e7fe52a2dc3" />

Context-based refinement example
<img width="904" height="909" alt="refinement_generation" src="https://github.com/user-attachments/assets/6248c542-bafa-4600-8dc3-68ef8fb0e7bb" />

Test cases passing
<img width="1101" height="364" alt="tests_passed" src="https://github.com/user-attachments/assets/b0cb810c-4f39-4b48-9dc4-7fe5f0ad6981" />

GitHub repository structure
<img width="306" height="582" alt="github_repo" src="https://github.com/user-attachments/assets/d00e6dce-d06f-42d1-8bf6-5bf10c6dcf73" />

📌 Future Improvements

Syntax highlighting for generated code

Support for additional programming languages

Persistent chat history using a database

Authentication and user sessions

👨‍💻 Author

Taranjot Singh Dhingra
Intern Project – AI Code Generation System
