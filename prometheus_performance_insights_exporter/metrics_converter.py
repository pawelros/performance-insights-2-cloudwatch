from prometheus_performance_insights_exporter.prometheus_metric import PrometheusMetric


class MetricsConverter:
    def pi_to_prometheus(pi_client_response):
        result = {}

        for m in pi_client_response["MetricList"]:
            if "Dimensions" not in m["Key"].keys():
                continue

            db_user = m["Key"]["Dimensions"]["db.name"]

            result[db_user] = m["DataPoints"][0]["Value"]

        prom_metrics = []
        for k, v in result.items():
            prom_metrics.append(str(PrometheusMetric("db_load_avg", {"db_name": k}, v)))

        return prom_metrics
