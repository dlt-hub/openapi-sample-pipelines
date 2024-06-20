import dlt

from imgur import imgur_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="imgur_pipeline",
        destination='duckdb',
        dataset_name="imgur_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = imgur_source()
    info = pipeline.run(source)
    print(info)
