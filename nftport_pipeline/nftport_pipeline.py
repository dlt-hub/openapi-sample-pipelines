import dlt

from nftport import nftport_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="nftport_pipeline",
        destination='duckdb',
        dataset_name="nftport_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = nftport_source()
    info = pipeline.run(source)
    print(info)
