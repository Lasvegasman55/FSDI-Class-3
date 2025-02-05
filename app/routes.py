from flask import (
    Flask,
    request
)
from app.database import task

app= Flask(__name__)


@app.get("/")
@app.get("/tasks")
def get_all_tasks():
    out = {
        "tasks": task.scan(),
        "ok": True
    }
    return out

@app.get("/tasks/<int:pk>")
def get_single_task(pk):
    out = {
        "task": task.select_by_id(pk),
    "ok": True
    }
    return out