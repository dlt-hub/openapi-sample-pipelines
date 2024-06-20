import dlt

from roster_api import roster_api_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="roster_api_pipeline",
        destination='duckdb',
        dataset_name="roster_api_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = roster_api_source()
    info = pipeline.run(source)
    print(info)
