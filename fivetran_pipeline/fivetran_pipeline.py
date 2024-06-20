import dlt

from fivetran import fivetran_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="fivetran_pipeline",
        destination='duckdb',
        dataset_name="fivetran_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = fivetran_source()
    info = pipeline.run(source)
    print(info)
