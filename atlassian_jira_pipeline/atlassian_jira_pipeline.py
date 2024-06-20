import dlt

from atlassian_jira import atlassian_jira_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="atlassian_jira_pipeline",
        destination='duckdb',
        dataset_name="atlassian_jira_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = atlassian_jira_source()
    info = pipeline.run(source)
    print(info)
