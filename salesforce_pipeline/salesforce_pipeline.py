import dlt

from salesforce import salesforce_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="salesforce_pipeline",
        destination='duckdb',
        dataset_name="salesforce_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = salesforce_source()
    info = pipeline.run(source)
    print(info)
