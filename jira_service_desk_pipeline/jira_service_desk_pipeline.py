import dlt

from jira_service_desk import jira_service_desk_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="jira_service_desk_pipeline",
        destination='duckdb',
        dataset_name="jira_service_desk_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = jira_service_desk_source()
    info = pipeline.run(source)
    print(info)
