import dlt

from bitbucket import bitbucket_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="bitbucket_pipeline",
        destination='duckdb',
        dataset_name="bitbucket_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = bitbucket_source()
    info = pipeline.run(source)
    print(info)
