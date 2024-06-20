import dlt

from trello import trello_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="trello_pipeline",
        destination='duckdb',
        dataset_name="trello_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = trello_source()
    info = pipeline.run(source)
    print(info)
