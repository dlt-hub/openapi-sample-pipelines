import dlt

from aviation_api import aviation_api_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="aviation_api_pipeline",
        destination='duckdb',
        dataset_name="aviation_api_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = aviation_api_source()
    info = pipeline.run(source)
    print(info)
