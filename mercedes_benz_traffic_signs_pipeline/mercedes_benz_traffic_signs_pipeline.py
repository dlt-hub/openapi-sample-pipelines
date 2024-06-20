import dlt

from mercedes_benz_traffic_signs import mercedes_benz_traffic_signs_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="mercedes_benz_traffic_signs_pipeline",
        destination='duckdb',
        dataset_name="mercedes_benz_traffic_signs_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = mercedes_benz_traffic_signs_source()
    info = pipeline.run(source)
    print(info)
