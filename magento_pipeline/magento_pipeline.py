import dlt

from magento import magento_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="magento_pipeline",
        destination='duckdb',
        dataset_name="magento_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = magento_source()
    info = pipeline.run(source)
    print(info)
