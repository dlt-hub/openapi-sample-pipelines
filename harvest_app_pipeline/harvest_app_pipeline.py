import dlt

from harvest_app import harvest_app_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="harvest_app_pipeline",
        destination='duckdb',
        dataset_name="harvest_app_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = harvest_app_source()
    info = pipeline.run(source)
    print(info)
