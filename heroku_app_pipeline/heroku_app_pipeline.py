import dlt

from heroku_app import heroku_app_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="heroku_app_pipeline",
        destination='duckdb',
        dataset_name="heroku_app_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = heroku_app_source()
    info = pipeline.run(source)
    print(info)
