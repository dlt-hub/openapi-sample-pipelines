import dlt

from bigcommerce import bigcommerce_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="bigcommerce_pipeline",
        destination='duckdb',
        dataset_name="bigcommerce_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = bigcommerce_source()
    info = pipeline.run(source)
    print(info)
