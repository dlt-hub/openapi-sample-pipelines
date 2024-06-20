import dlt

from square_connect import square_connect_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="square_connect_pipeline",
        destination='duckdb',
        dataset_name="square_connect_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = square_connect_source()
    info = pipeline.run(source)
    print(info)
