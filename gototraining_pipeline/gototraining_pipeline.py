import dlt

from gototraining import gototraining_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="gototraining_pipeline",
        destination='duckdb',
        dataset_name="gototraining_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = gototraining_source()
    info = pipeline.run(source)
    print(info)
