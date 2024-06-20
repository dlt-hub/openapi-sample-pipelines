import dlt

from google_calendar import google_calendar_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_calendar_pipeline",
        destination='duckdb',
        dataset_name="google_calendar_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_calendar_source()
    info = pipeline.run(source)
    print(info)
