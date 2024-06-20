import dlt

from mailchimp import mailchimp_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="mailchimp_pipeline",
        destination='duckdb',
        dataset_name="mailchimp_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = mailchimp_source()
    info = pipeline.run(source)
    print(info)
