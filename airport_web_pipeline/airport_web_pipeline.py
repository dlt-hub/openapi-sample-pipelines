import dlt

from airport_web import airport_web_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="airport_web_pipeline",
        destination='duckdb',
        dataset_name="airport_web_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = airport_web_source()
    info = pipeline.run(source)
    print(info)
