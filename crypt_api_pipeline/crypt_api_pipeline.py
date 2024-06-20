import dlt

from crypt_api import crypt_api_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="crypt_api_pipeline",
        destination='duckdb',
        dataset_name="crypt_api_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = crypt_api_source()
    info = pipeline.run(source)
    print(info)
