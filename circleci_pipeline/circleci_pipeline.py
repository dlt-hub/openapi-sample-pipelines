import dlt

from circleci import circleci_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="circleci_pipeline",
        destination='duckdb',
        dataset_name="circleci_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = circleci_source()
    info = pipeline.run(source)
    print(info)
