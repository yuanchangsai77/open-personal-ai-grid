import re

from fastapi import FastAPI
from pydantic import BaseModel

from tools.registry import call_tool

app = FastAPI()

class Task(BaseModel):
    text: str


def extract_amount(text: str) -> int | None:
    match = re.search(r"(\d+)", text)
    if match is None:
        return None
    return int(match.group(1))


@app.post("/task")
def run_task(task: Task):

    text = task.text

    if "米线" in text:
        amount = extract_amount(text)
        if amount is None:
            return {"result": "amount not found"}

        result = call_tool(
            "ledger.add_expense",
            {"item": "米线", "amount": amount}
        )
        return {"result": result}

    return {"result": "unknown task"}
