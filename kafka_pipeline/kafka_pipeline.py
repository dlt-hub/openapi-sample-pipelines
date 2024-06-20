import dlt

from kafka import kafka_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="kafka_pipeline",
        destination='duckdb',
        dataset_name="kafka_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = kafka_source()
    info = pipeline.run(source)
    print(info)
