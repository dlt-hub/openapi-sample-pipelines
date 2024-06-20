import dlt

from wizard_world import wizard_world_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="wizard_world_pipeline",
        destination='duckdb',
        dataset_name="wizard_world_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = wizard_world_source()
    info = pipeline.run(source)
    print(info)
