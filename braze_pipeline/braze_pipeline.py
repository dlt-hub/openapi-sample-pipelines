import dlt

from braze import braze_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="braze_pipeline",
        destination='duckdb',
        dataset_name="braze_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = braze_source()
    info = pipeline.run(source)
    print(info)
