import dlt

from art_institute_chicago_api import art_institute_chicago_api_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="art_institute_chicago_api_pipeline",
        destination='duckdb',
        dataset_name="art_institute_chicago_api_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = art_institute_chicago_api_source()
    info = pipeline.run(source)
    print(info)
