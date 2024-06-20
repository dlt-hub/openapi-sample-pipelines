import dlt

from osi_api import osi_api_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="osi_api_pipeline",
        destination='duckdb',
        dataset_name="osi_api_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = osi_api_source()
    info = pipeline.run(source)
    print(info)
