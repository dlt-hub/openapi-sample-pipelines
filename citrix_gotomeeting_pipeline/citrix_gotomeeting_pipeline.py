import dlt

from citrix_gotomeeting import citrix_gotomeeting_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="citrix_gotomeeting_pipeline",
        destination='duckdb',
        dataset_name="citrix_gotomeeting_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = citrix_gotomeeting_source()
    info = pipeline.run(source)
    print(info)
