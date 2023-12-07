from typing import List
from prometheus_performance_insights_exporter.prometheus_metric import PrometheusMetric


class MetricsConverter:
    def pi_to_prometheus(
        pi_client_response,
        extra_labels: dict = None,
        labels_to_ignore: List[str] = None,
    ):
        if not labels_to_ignore:
            labels_to_ignore = []

        prom_metrics = []

        for m in pi_client_response["MetricList"]:
            metric_name = m["Key"]["Metric"].replace(".", "_")

            if "Dimensions" not in m["Key"].keys():
                continue

            labels = extra_labels.copy() or {}

            for k, v in m["Key"]["Dimensions"].items():
                key = k.replace(".", "_")
                if key not in labels_to_ignore:
                    labels[key] = v

            prom_metrics.append(
                PrometheusMetric(metric_name, labels, m["DataPoints"][0]["Value"])
            )

        return prom_metrics
