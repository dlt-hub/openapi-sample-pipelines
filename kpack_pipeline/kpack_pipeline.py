import dlt

from kpack import kpack_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="kpack_pipeline",
        destination='duckdb',
        dataset_name="kpack_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = kpack_source()
    info = pipeline.run(source)
    print(info)
