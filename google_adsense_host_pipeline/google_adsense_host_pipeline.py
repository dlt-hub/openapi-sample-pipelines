import dlt

from google_adsense_host import google_adsense_host_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="google_adsense_host_pipeline",
        destination='duckdb',
        dataset_name="google_adsense_host_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = google_adsense_host_source()
    info = pipeline.run(source)
    print(info)
