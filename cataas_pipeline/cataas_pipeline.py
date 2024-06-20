import dlt

from cataas import cataas_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="cataas_pipeline",
        destination='duckdb',
        dataset_name="cataas_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = cataas_source()
    info = pipeline.run(source)
    print(info)
