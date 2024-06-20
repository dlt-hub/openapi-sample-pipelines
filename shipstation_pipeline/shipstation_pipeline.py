import dlt

from shipstation import shipstation_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="shipstation_pipeline",
        destination='duckdb',
        dataset_name="shipstation_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = shipstation_source()
    info = pipeline.run(source)
    print(info)
