import dlt

from kubernetes import kubernetes_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="kubernetes_pipeline",
        destination='duckdb',
        dataset_name="kubernetes_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = kubernetes_source()
    info = pipeline.run(source)
    print(info)
