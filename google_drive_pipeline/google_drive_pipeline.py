import dlt

from google_drive import google_drive_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_drive_pipeline",
        destination='duckdb',
        dataset_name="google_drive_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_drive_source()
    info = pipeline.run(source)
    print(info)
