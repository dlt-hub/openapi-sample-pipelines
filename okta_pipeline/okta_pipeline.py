import dlt

from okta import okta_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="okta_pipeline",
        destination='duckdb',
        dataset_name="okta_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = okta_source()
    info = pipeline.run(source)
    print(info)
