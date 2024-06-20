import dlt

from runscope import runscope_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="runscope_pipeline",
        destination='duckdb',
        dataset_name="runscope_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = runscope_source()
    info = pipeline.run(source)
    print(info)
