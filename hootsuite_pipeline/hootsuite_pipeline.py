import dlt

from hootsuite import hootsuite_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="hootsuite_pipeline",
        destination='duckdb',
        dataset_name="hootsuite_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = hootsuite_source()
    info = pipeline.run(source)
    print(info)
