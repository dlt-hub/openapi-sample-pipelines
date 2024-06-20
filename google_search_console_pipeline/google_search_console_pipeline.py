import dlt

from google_search_console import google_search_console_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_search_console_pipeline",
        destination='duckdb',
        dataset_name="google_search_console_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_search_console_source()
    info = pipeline.run(source)
    print(info)
