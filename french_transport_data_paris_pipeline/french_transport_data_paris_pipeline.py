import dlt

from french_transport_data_paris import french_transport_data_paris_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="french_transport_data_paris_pipeline",
        destination='duckdb',
        dataset_name="french_transport_data_paris_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = french_transport_data_paris_source()
    info = pipeline.run(source)
    print(info)
