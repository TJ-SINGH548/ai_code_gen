from pydantic import BaseModel

class UserQuery(BaseModel):
    prompt: str
    language: str 

class AgentResponse(BaseModel):
    code: str
    explanation: str