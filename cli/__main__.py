import typer
from typing_extensions import Annotated
from loguru import logger
from prometheus_performance_insights_exporter.pi_client import PiClient
from prometheus_performance_insights_exporter.rds_helper import RdsHelper

app = typer.Typer()


@app.command()
def get_rds_metrics(
    instance_id: Annotated[str, typer.Option(help="RDS database instance id. It is NOT DBInstanceIdentifier, it is the DB ResourceId")]
):
    logger.debug(f'Getting \'DbiResourceId\' from instance id {instance_id}.')
    db_resource_id = RdsHelper.get_db_resource_id(instance_id)
    logger.info(f'DbiResourceId for instance id {instance_id} is {db_resource_id}')

    pi_client = PiClient(db_resource_id)
    return pi_client.get_rds_metrics()


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()
