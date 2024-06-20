import dlt

from twilio import twilio_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="twilio_pipeline",
        destination='duckdb',
        dataset_name="twilio_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = twilio_source()
    info = pipeline.run(source)
    print(info)
