import dlt

from looker import looker_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="looker_pipeline",
        destination='duckdb',
        dataset_name="looker_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = looker_source()
    info = pipeline.run(source)
    print(info)
