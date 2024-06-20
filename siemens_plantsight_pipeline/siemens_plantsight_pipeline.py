import dlt

from siemens_plantsight import siemens_plantsight_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="siemens_plantsight_pipeline",
        destination='duckdb',
        dataset_name="siemens_plantsight_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = siemens_plantsight_source()
    info = pipeline.run(source)
    print(info)
