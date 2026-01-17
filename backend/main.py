from fastapi import FastAPI
from schemas import UserQuery
from agents import assistant, user_proxy
from utils import build_prompt
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def is_ambiguous(prompt: str) -> bool:
    vague_phrases = [
        "write a code",
        "write me a code",
        "make it recursive",
        "modify this",
        "improve it",
        "optimize it"
    ]
    return any(phrase in prompt.lower() for phrase in vague_phrases)

last_task = None

def is_refinement_only(prompt: str) -> bool:
    refinement_phrases = [
        "make it recursive",
        "optimize it",
        "improve it",
        "make it iterative",
        "add comments",
        "make it faster"
    ]
    return any(p in prompt.lower() for p in refinement_phrases)


MAX_MESSAGES = 4  # keep last 2 user + 2 assistant messages
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.post("/generate")
def generate_code(query: UserQuery):
    prompt_text = query.prompt.strip().lower()
    base_prompt = query.prompt


# 1️⃣ Too short
    if len(prompt_text) < 10:
        return {
            "code": "",
            "explanation": "❗ Your prompt is too short. Please describe the task in more detail."
        }
# 2️⃣ Ambiguous phrases detection
    generic_phrases = [
    "write me a code",
    "write a code",
    "write code",
    "write me code",
    "make a code",
    "create a code",
    "do it",
    "program",
    "code it"
]

# keywords that indicate a real task
    task_indicators = [
    "reverse", "sort", "calculate", "check", "find",
    "convert", "generate", "implement", "validate",
    "palindrome", "factorial", "prime", "array", "string"
]

    if any(phrase in prompt_text for phrase in generic_phrases) and not any(
    keyword in prompt_text for keyword in task_indicators
):
        return {
        "code": "",
        "explanation": (
            "❗ Your request is ambiguous. Please specify what the code should do.\n\n"
            "Examples:\n"
            "- Write a Python function to reverse a string\n"
            "- Write Java code to check if a number is prime"
        )
    }

    if not query.prompt:
        return {"error": "Please enter a prompt"}

    if query.language not in ["Python", "JavaScript", "Java"]:
        return {"error": "Unsupported language"}

        global last_task

    # 🔹 Handle refinement using previous context
    if is_refinement_only(prompt_text):
        if last_task is None:
            return {
                "code": "",
                "explanation": (
                    "❗ This request depends on previous context.\n"
                    "Please first describe what code you want to generate."
                )
            }
        else:
            base_prompt = (
                f"Previous task:\n{last_task}\n\n"
                f"User refinement:\n{query.prompt}\n\n"
                f"Modify the previous code accordingly."
            )
    else:
        # Store only meaningful, non-ambiguous tasks
        last_task = query.prompt

    prompt = build_prompt(base_prompt, query.language)



    # TRIM OLD HISTORY (instead of reset)
    for agent in (user_proxy, assistant):
        if len(agent.chat_messages) > MAX_MESSAGES:
            for sender in list(agent.chat_messages.keys()):
                agent.chat_messages[sender] = agent.chat_messages[sender][-MAX_MESSAGES:]

    chat_result = user_proxy.initiate_chat(
        assistant,
        message=prompt,
        max_turns=1
    )
    

    generated_code = ""

    for msg in chat_result.chat_history:
        # AI responses come from CodeGenerator
        if msg.get("name") == "CodeGen":
            content = msg.get("content", "")
            if "```" in content:
                generated_code = content
                break

    return {
        "code": generated_code,
        "explanation": "Code generated successfully"
    }
