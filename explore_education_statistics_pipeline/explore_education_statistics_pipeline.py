import dlt

from explore_education_statistics import explore_education_statistics_source


if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="explore_education_statistics_pipeline",
        destination='duckdb',
        dataset_name="explore_education_statistics_data",
        progress="log",
        export_schema_path="schemas/export"
    )
    source = explore_education_statistics_source()
    info = pipeline.run(source)
    print(info)
