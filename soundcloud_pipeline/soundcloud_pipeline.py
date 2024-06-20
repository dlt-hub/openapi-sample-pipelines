import dlt

from soundcloud import soundcloud_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="soundcloud_pipeline",
        destination='duckdb',
        dataset_name="soundcloud_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = soundcloud_source()
    info = pipeline.run(source)
    print(info)
