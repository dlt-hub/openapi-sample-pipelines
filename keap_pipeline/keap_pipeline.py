import dlt

from keap import keap_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="keap_pipeline",
        destination='duckdb',
        dataset_name="keap_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = keap_source()
    info = pipeline.run(source)
    print(info)
