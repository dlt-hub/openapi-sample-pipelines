import dlt

from google_analytics import google_analytics_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_analytics_pipeline",
        destination='duckdb',
        dataset_name="google_analytics_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_analytics_source()
    info = pipeline.run(source)
    print(info)
