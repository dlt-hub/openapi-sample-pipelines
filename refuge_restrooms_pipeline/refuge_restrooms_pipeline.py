import dlt

from refuge_restrooms import refuge_restrooms_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="refuge_restrooms_pipeline",
        destination='duckdb',
        dataset_name="refuge_restrooms_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = refuge_restrooms_source()
    info = pipeline.run(source)
    print(info)
