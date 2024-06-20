import dlt

from zuora import zuora_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="zuora_pipeline",
        destination='duckdb',
        dataset_name="zuora_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = zuora_source()
    info = pipeline.run(source)
    print(info)
