import dlt

from postmark_app import postmark_app_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="postmark_app_pipeline",
        destination='duckdb',
        dataset_name="postmark_app_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = postmark_app_source()
    info = pipeline.run(source)
    print(info)
