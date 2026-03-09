from fastapi import FastAPI
from pydantic import BaseModel

from tools.registry import call_tool

app = FastAPI()

class Task(BaseModel):
    text: str


@app.post("/task")
def run_task(task: Task):

    text = task.text

    if "米线" in text:
        result = call_tool(
            "ledger.add_expense",
            {"item": "米线", "amount": 14}
        )
        return {"result": result}

    return {"result": "unknown task"}