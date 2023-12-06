import typer
import boto3
import time
from typing_extensions import Annotated
from loguru import logger

app = typer.Typer()


@app.command()
def get_rds_metrics(
    instance_id: Annotated[str, typer.Option(help="RDS database instance id. It is NOT DBInstanceIdentifier, it is the DB ResourceId")]
):
    logger.info(f"Hello {instance_id}")
    pi_client = boto3.client("pi")
    response = pi_client.get_resource_metrics(
        ServiceType='RDS',
        Identifier=instance_id,
        StartTime=time.time() - 300,
        EndTime=time.time(),
        PeriodInSeconds=60,
        MetricQueries=[{'Metric': 'os.general.numVCPUs.avg'}]
    )

    logger.debug("response={}", response)
    return response


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


def get_db_resource_id(instance_id: str):


if __name__ == "__main__":
    app()
