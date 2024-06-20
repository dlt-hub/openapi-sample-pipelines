import dlt

from star_treck import star_treck_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="star_treck_pipeline",
        destination='duckdb',
        dataset_name="star_treck_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = star_treck_source()
    info = pipeline.run(source)
    print(info)
