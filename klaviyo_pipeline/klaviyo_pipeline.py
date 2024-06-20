import dlt

from klaviyo import klaviyo_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="klaviyo_pipeline",
        destination='duckdb',
        dataset_name="klaviyo_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = klaviyo_source()
    info = pipeline.run(source)
    print(info)
