import dlt

from twitter import twitter_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="twitter_pipeline",
        destination='duckdb',
        dataset_name="twitter_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = twitter_source()
    info = pipeline.run(source)
    print(info)
