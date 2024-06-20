import dlt

from gitlab import gitlab_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="gitlab_pipeline",
        destination='duckdb',
        dataset_name="gitlab_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = gitlab_source()
    info = pipeline.run(source)
    print(info)
