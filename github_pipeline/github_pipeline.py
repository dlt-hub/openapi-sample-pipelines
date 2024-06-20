import dlt

from github import github_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="github_pipeline",
        destination='duckdb',
        dataset_name="github_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = github_source()
    info = pipeline.run(source)
    print(info)
