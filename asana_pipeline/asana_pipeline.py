import dlt

from asana import asana_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="asana_pipeline",
        destination='duckdb',
        dataset_name="asana_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = asana_source()
    info = pipeline.run(source)
    print(info)
