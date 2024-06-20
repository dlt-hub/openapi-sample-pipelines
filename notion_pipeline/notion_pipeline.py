import dlt

from notion import notion_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="notion_pipeline",
        destination='duckdb',
        dataset_name="notion_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = notion_source()
    info = pipeline.run(source)
    print(info)
