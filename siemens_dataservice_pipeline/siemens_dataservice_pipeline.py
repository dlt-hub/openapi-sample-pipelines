import dlt

from siemens_dataservice import siemens_dataservice_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="siemens_dataservice_pipeline",
        destination='duckdb',
        dataset_name="siemens_dataservice_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = siemens_dataservice_source()
    info = pipeline.run(source)
    print(info)
