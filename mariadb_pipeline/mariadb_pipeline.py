import dlt

from mariadb import mariadb_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="mariadb_pipeline",
        destination='duckdb',
        dataset_name="mariadb_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = mariadb_source()
    info = pipeline.run(source)
    print(info)
