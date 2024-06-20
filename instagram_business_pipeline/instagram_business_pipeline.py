import dlt

from instagram_business import instagram_business_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="instagram_business_pipeline",
        destination='duckdb',
        dataset_name="instagram_business_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = instagram_business_source()
    info = pipeline.run(source)
    print(info)
