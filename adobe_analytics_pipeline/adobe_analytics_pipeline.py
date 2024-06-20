import dlt

from adobe_analytics import adobe_analytics_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="adobe_analytics_pipeline",
        destination='duckdb',
        dataset_name="adobe_analytics_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = adobe_analytics_source()
    info = pipeline.run(source)
    print(info)
