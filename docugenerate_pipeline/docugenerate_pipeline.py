import dlt

from docugenerate import docugenerate_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="docugenerate_pipeline",
        destination='duckdb',
        dataset_name="docugenerate_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = docugenerate_source()
    info = pipeline.run(source)
    print(info)
