from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="salesforce_source", max_table_nesting=2)
def salesforce_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
        },
        "resources": [
            # Returns prediction usage on a monthly basis for the current calendar month and future months. Each apiusage object in the response corresponds to a calendar month in your plan.
            {
                "name": "get_api_usage_plans_v2",
                "table_name": "api_usage",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/apiusage",
                    "paginator": "auto",
                },
            },
            # Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.
            {
                "name": "list_datasets",
                "table_name": "dataset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/language/datasets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "25",
                        # "global": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single dataset.
            {
                "name": "get_dataset",
                "table_name": "dataset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/language/datasets/{datasetId}",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "list_datasets",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.
            {
                "name": "list_datasets_1",
                "table_name": "dataset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/vision/datasets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "25",
                        # "global": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single dataset.
            {
                "name": "get_dataset_1",
                "table_name": "dataset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/vision/datasets/{datasetId}",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "list_datasets_1",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the status of a language dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.
            {
                "name": "get",
                "table_name": "deletion_response",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/language/deletion/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the status of an image dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.
            {
                "name": "get_1",
                "table_name": "deletion_response",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/vision/deletion/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all the examples for the specified dataset,
            {
                "name": "get_examples",
                "table_name": "example",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/language/datasets/{datasetId}/examples",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "list_datasets",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "100",
                        # "source": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.
            {
                "name": "get_examples_by_label",
                "table_name": "example",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/language/examples",
                    "params": {
                        # the parameters below can optionally be configured
                        # "labelId": "OPTIONAL_CONFIG",
                        # "offset": "0",
                        # "count": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all the examples for the specified dataset. By default, returns examples created by uploading them from a .zip file.
            {
                "name": "get_examples_1",
                "table_name": "example",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/vision/datasets/{datasetId}/examples",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "list_datasets_1",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "100",
                        # "source": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.
            {
                "name": "get_examples_by_label_1",
                "table_name": "example",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/vision/examples",
                    "params": {
                        # the parameters below can optionally be configured
                        # "labelId": "OPTIONAL_CONFIG",
                        # "offset": "0",
                        # "count": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metrics for each epoch in a model.
            {
                "name": "get_trained_model_learning_curve",
                "table_name": "learning_curve",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/language/models/{modelId}/lc",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "25",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metrics for each epoch in a model.
            {
                "name": "get_trained_model_learning_curve_1",
                "table_name": "learning_curve",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/vision/models/{modelId}/lc",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "25",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metrics for a model
            {
                "name": "get_trained_model_metrics",
                "table_name": "metrics",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/language/models/{modelId}",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metrics for a model
            {
                "name": "get_trained_model_metrics_1",
                "table_name": "metrics",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/vision/models/{modelId}",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all models for the specified dataset.
            {
                "name": "get_trained_models",
                "table_name": "model",
                "primary_key": "datasetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/language/datasets/{datasetId}/models",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "list_datasets",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all models for the specified dataset.
            {
                "name": "get_trained_models_1",
                "table_name": "model",
                "primary_key": "datasetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v2/vision/datasets/{datasetId}/models",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "list_datasets_1",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "offset": "0",
                        # "count": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the status of a model's training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.
            {
                "name": "get_train_status_and_progress",
                "table_name": "train_response",
                "primary_key": "modelId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/language/train/{modelId}",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the status of a model's training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.
            {
                "name": "get_train_status_and_progress_1",
                "table_name": "train_response",
                "primary_key": "modelId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/vision/train/{modelId}",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
