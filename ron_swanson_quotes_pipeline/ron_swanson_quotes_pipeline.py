import dlt

from ron_swanson_quotes import ron_swanson_quotes_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="ron_swanson_quotes_pipeline",
        destination='duckdb',
        dataset_name="ron_swanson_quotes_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = ron_swanson_quotes_source()
    info = pipeline.run(source)
    print(info)
