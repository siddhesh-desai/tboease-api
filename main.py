import uvicorn
from fastapi import FastAPI
from api.requirementExtractingAgent import RequirementExtractingAgent
from pydantic import BaseModel


class Prompt(BaseModel):
    prompt: str


app = FastAPI()
req_agent = RequirementExtractingAgent()


@app.post("/extract-requirements/")
async def extract_requirements(prompt: Prompt):
    return req_agent.extract_requirements(prompt)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
