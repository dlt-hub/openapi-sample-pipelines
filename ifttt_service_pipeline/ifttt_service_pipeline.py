import dlt

from ifttt_service import ifttt_service_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="ifttt_service_pipeline",
        destination='duckdb',
        dataset_name="ifttt_service_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = ifttt_service_source()
    info = pipeline.run(source)
    print(info)
