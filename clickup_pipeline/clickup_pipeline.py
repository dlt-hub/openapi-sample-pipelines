import dlt

from clickup import clickup_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="clickup_pipeline",
        destination='duckdb',
        dataset_name="clickup_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = clickup_source()
    info = pipeline.run(source)
    print(info)
