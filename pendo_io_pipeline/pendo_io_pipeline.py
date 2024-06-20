import dlt

from pendo_io import pendo_io_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="pendo_io_pipeline",
        destination='duckdb',
        dataset_name="pendo_io_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = pendo_io_source()
    info = pipeline.run(source)
    print(info)
