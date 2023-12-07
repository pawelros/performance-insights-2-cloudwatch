import boto3
import time
from loguru import logger


class PiClient:
    def __init__(self, db_resource_id: str):
        self.db_resource_id = db_resource_id
        self.boto_client = boto3.client("pi")

    def get_rds_metrics(self):
        response = self.boto_client.get_resource_metrics(
            ServiceType='RDS',
            Identifier=self.db_resource_id,
            StartTime=time.time() - 300,
            EndTime=time.time(),
            PeriodInSeconds=60,
            MetricQueries=[{'Metric': 'os.general.numVCPUs.avg'}]
        )

        logger.debug("response={}", response)
        return response
