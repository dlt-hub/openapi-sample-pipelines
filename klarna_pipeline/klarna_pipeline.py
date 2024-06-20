import dlt

from klarna import klarna_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="klarna_pipeline",
        destination='duckdb',
        dataset_name="klarna_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = klarna_source()
    info = pipeline.run(source)
    print(info)
