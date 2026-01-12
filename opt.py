from typing import Annotated

import typer

app = typer.Typer()


@app.command()
def email(
    name: str,
    email: Annotated[str, typer.Option(prompt=True, confirmation_prompt=True)],
):
    print(f"Hello {name}, your email is {email}")

@app.command()
def password(
    name: str,
    password: Annotated[
        str, typer.Option(prompt=True, confirmation_prompt=True, hide_input=True)
    ],
):
    print(f"Hello {name}. Doing something very secure with password.")
    print(f"...just kidding, here it is, very insecure: {password}")

if __name__ == "__main__":
    app()