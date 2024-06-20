import dlt

from qualtrics import qualtrics_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="qualtrics_pipeline",
        destination='duckdb',
        dataset_name="qualtrics_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = qualtrics_source()
    info = pipeline.run(source)
    print(info)
