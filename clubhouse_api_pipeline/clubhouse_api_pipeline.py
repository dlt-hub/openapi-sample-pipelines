import dlt

from clubhouse_api import clubhouse_api_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="clubhouse_api_pipeline",
        destination='duckdb',
        dataset_name="clubhouse_api_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = clubhouse_api_source()
    info = pipeline.run(source)
    print(info)
