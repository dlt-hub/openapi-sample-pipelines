import dlt

from messagebird import messagebird_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="messagebird_pipeline",
        destination='duckdb',
        dataset_name="messagebird_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = messagebird_source()
    info = pipeline.run(source)
    print(info)
