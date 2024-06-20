import dlt

from capsule_crm import capsule_crm_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="capsule_crm_pipeline",
        destination='duckdb',
        dataset_name="capsule_crm_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = capsule_crm_source()
    info = pipeline.run(source)
    print(info)
