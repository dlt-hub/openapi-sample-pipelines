import dlt

from google_sheets import google_sheets_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_sheets_pipeline",
        destination='duckdb',
        dataset_name="google_sheets_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_sheets_source()
    info = pipeline.run(source)
    print(info)
