import dlt

from stripe import stripe_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="stripe_pipeline",
        destination='duckdb',
        dataset_name="stripe_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = stripe_source()
    info = pipeline.run(source)
    print(info)
