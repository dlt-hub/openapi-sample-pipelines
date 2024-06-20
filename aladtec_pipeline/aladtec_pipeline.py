import dlt

from aladtec import aladtec_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="aladtec_pipeline",
        destination='duckdb',
        dataset_name="aladtec_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = aladtec_source()
    info = pipeline.run(source)
    print(info)
