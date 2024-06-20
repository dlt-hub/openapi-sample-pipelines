import dlt

from box_platform import box_platform_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="box_platform_pipeline",
        destination='duckdb',
        dataset_name="box_platform_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = box_platform_source()
    info = pipeline.run(source)
    print(info)
