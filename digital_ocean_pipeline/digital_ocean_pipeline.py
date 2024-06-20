import dlt

from digital_ocean import digital_ocean_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="digital_ocean_pipeline",
        destination='duckdb',
        dataset_name="digital_ocean_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = digital_ocean_source()
    info = pipeline.run(source)
    print(info)
