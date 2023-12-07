from typing import List


class PrometheusMetric:
    def __init__(self, metric_name: str, labels: dict, value: float) -> None:
        # metric_name{label="value"} actual_metric_value
        self.metric_name = metric_name
        self.labels = labels
        self.value = value

    def __str__(self):
        labels_str = ",".join(f'{k}="{v}"' for k, v in self.labels.items())
        return f"{self.metric_name}={{{labels_str}}} {self.value}"
