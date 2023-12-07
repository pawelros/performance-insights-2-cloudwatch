from loguru import logger
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import time

from prometheus_performance_insights_exporter.pi_client import PiClient
from prometheus_performance_insights_exporter.rds_helper import RdsHelper
from prometheus_performance_insights_exporter.metrics_converter import MetricsConverter

app = FastAPI()


@app.get("/{instance_id}", response_class=PlainTextResponse)
async def root(instance_id):
    logger.debug(f"Getting 'DbiResourceId' from instance id {instance_id}.")
    db_resource_id = RdsHelper.get_db_resource_id(instance_id)
    logger.info(f"DbiResourceId for instance id {instance_id} is {db_resource_id}")
    #
    pi_client = PiClient(db_resource_id)
    response = pi_client.get_rds_metrics(
        [{"Metric": "db.load.avg", "GroupBy": {"Group": "db"}}],
        start_time=time.time() - (5 * 60),
        end_time=time.time(),
    )

    prometheus_metrics = MetricsConverter.pi_to_prometheus(
        response, extra_labels={"instance_id": instance_id}, labels_to_ignore=["db_id"]
    )

    response_str = "\n".join(str(m) for m in prometheus_metrics)

    logger.info(response_str)
    return response_str
