import dlt

from buffer_app import buffer_app_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="buffer_app_pipeline",
        destination='duckdb',
        dataset_name="buffer_app_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = buffer_app_source()
    info = pipeline.run(source)
    print(info)
