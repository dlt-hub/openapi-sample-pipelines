import dlt

from strapi import strapi_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="strapi_pipeline",
        destination='duckdb',
        dataset_name="strapi_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = strapi_source()
    info = pipeline.run(source)
    print(info)
