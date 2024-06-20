import dlt

from swagger import swagger_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="swagger_pipeline",
        destination='duckdb',
        dataset_name="swagger_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = swagger_source()
    info = pipeline.run(source)
    print(info)
