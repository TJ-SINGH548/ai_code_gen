import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

# Load environment variables
load_dotenv()

llm_config = {
    "model": "llama-3.1-8b-instant",
    "api_key": os.getenv("GROQ_API_KEY"),
    "base_url": "https://api.groq.com/openai/v1"
}


assistant = AssistantAgent(
    name="CodeGen",
    llm_config=llm_config,
    system_message="""
    You are a code generation assistant.

    RULES:
    - Respond ONLY ONCE
    - Generate code ONLY for the requested language
    - Do NOT provide alternatives
    - Do NOT suggest other languages
    - Do NOT continue the conversation
    - Stop after providing the code
    """
)


user_proxy = UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    code_execution_config=False
)
