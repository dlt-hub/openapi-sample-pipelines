import dlt

from visible_thread import visible_thread_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="visible_thread_pipeline",
        destination='duckdb',
        dataset_name="visible_thread_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = visible_thread_source()
    info = pipeline.run(source)
    print(info)
