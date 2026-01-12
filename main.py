import typer
from pathlib import Path
 
app = typer.Typer(help="File Utility CLI")
 
@app.command()
def read(file: Path = typer.Argument(..., exists=True)):
    typer.echo(file.read_text())
 
@app.command()
def stats(file: Path = typer.Argument(..., exists=True)):
    text = file.read_text()
    typer.echo(f"Lines      : {len(text.splitlines())}")
    typer.echo(f"Words      : {len(text.split())}")
    typer.echo(f"Characters : {len(text)}")
 
@app.command()
def write(file: Path, content: str):
    file.write_text(content)
    typer.echo(f"Written to {file}")
 
@app.command()
def connect(api_key: str = typer.Option(..., envvar="API_KEY")):
    typer.echo("Connected successfully!")
 
@app.command()
def divide(a: int, b: int):
    if b == 0:
        typer.echo("Error: Cannot divide by zero", err=True)
        raise typer.Exit(code=1)
    typer.echo(a / b)
 
if __name__ == "__main__":
    app()
 