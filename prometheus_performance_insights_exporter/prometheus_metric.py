class PrometheusMetric:
    def __init__(self, metric_name: str, labels: dict, value: float) -> None:
        self.metric_name = metric_name
        self.labels = labels
        self.value = value

    def __str__(self):
        # metric_name{label="value", another_label="value"} actual_metric_value
        labels_str = ",".join(f'{k}="{v}"' for k, v in self.labels.items())
        return f"{self.metric_name}{{{labels_str}}} {self.value}"
