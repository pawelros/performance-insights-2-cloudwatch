import boto3
from typing import List
import time
from loguru import logger


class PiClient:
    def __init__(self, db_resource_id: str):
        self.db_resource_id = db_resource_id
        self.boto_client = boto3.client("pi")

    def get_rds_metrics(self, metrics: List[dict], start_time: time.time, end_time: time.time):
        if not start_time:
            start_time = time.time() - 300
        if not end_time:
            end_time = time.time()
        response = self.boto_client.get_resource_metrics(
            ServiceType="RDS",
            Identifier=self.db_resource_id,
            StartTime=start_time,
            EndTime=end_time,
            PeriodInSeconds=300,
            MetricQueries=metrics,
        )

        logger.debug("response={}", response)
        return response
