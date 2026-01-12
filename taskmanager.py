import typer
import json
from pathlib import Path
 
app = typer.Typer(help="🗂️ Simple Task Manager CLI")
 
DATA_FILE = Path("tasks.json")
 
 
# ------------------ Helpers ------------------
 
def load_tasks():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []
 
 
def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))
 
 
# ------------------ Commands ------------------
 
@app.command()
def add(
    title: str = typer.Argument(..., help="Task title"),
    priority: int = typer.Option(
        1, min=1, max=5, help="Priority from 1 (low) to 5 (high)"
    ),
):
    """Add a new task"""
    tasks = load_tasks()
 
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False,
    }
 
    tasks.append(task)
    save_tasks(tasks)
 
    typer.echo(f"✅ Task added: {title}")
 
 
@app.command()
def list():
    """List all tasks"""
    tasks = load_tasks()
 
    if not tasks:
        typer.echo("📭 No tasks found")
        return
 
    for task in tasks:
        status = "✔️" if task["done"] else "❌"
        typer.echo(
            f'{task["id"]}. {task["title"]} | '
            f'Priority: {task["priority"]} | {status}'
        )
 
 
@app.command()
def done(
    task_id: int = typer.Argument(..., help="Task ID to mark as done")
):
    """Mark a task as done"""
    tasks = load_tasks()
 
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            typer.echo(f"🎉 Task {task_id} marked as done")
            return
 
    typer.echo("❌ Task not found")
 
 
@app.command()
def delete(
    task_id: int = typer.Argument(..., help="Task ID to delete"),
    yes: bool = typer.Option(
        False, "--yes", "-y", help="Delete without confirmation"
    ),
):
    """Delete a task"""
    tasks = load_tasks()
 
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        typer.echo("❌ Task not found")
        return
 
    if not yes:
        confirm = typer.confirm(
            f"Are you sure you want to delete '{task['title']}'?"
        )
        if not confirm:
            typer.echo("❎ Cancelled")
            return
 
    tasks.remove(task)
    save_tasks(tasks)
    typer.echo("🗑️ Task deleted")
 
 
# ------------------ Entry Point ------------------
 
if __name__ == "__main__":
    app()
 