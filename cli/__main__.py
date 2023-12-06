import typer
from typing_extensions import Annotated
from loguru import logger

app = typer.Typer()


@app.command()
def get_resource_metrics(instance_id: Annotated[str, typer.Option(help="RDS database instance id")]):
    logger.info(f"Hello {instance_id}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
