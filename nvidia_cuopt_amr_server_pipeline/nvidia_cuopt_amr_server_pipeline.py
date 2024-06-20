import dlt

from nvidia_cuopt_amr_server import nvidia_cuopt_amr_server_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="nvidia_cuopt_amr_server_pipeline",
        destination='duckdb',
        dataset_name="nvidia_cuopt_amr_server_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = nvidia_cuopt_amr_server_source()
    info = pipeline.run(source)
    print(info)
