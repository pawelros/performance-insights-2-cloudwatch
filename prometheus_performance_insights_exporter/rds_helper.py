import boto3


class RdsHelper:
    def get_db_resource_id(db_instance_id: str):
        client = boto3.client("rds")
        return client.describe_db_instances(
            DBInstanceIdentifier="string",
            Filters=[
                {"Name": "db-instance-id", "Values": [db_instance_id]},
            ],
            MaxRecords=20,
            Marker="string",
        )['DBInstances'][0]['DbiResourceId']
