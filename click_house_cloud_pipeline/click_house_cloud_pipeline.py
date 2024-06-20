import dlt

from click_house_cloud import click_house_cloud_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="click_house_cloud_pipeline",
        destination='duckdb',
        dataset_name="click_house_cloud_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = click_house_cloud_source()
    info = pipeline.run(source)
    print(info)
