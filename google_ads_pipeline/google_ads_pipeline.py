import dlt

from google_ads import google_ads_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_ads_pipeline",
        destination='duckdb',
        dataset_name="google_ads_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_ads_source()
    info = pipeline.run(source)
    print(info)
