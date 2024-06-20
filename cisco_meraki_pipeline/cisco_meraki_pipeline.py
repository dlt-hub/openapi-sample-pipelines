import dlt

from cisco_meraki import cisco_meraki_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="cisco_meraki_pipeline",
        destination='duckdb',
        dataset_name="cisco_meraki_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = cisco_meraki_source()
    info = pipeline.run(source)
    print(info)
