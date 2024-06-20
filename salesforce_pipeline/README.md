# salesforce pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/salesforce.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /v2/apiusage_ 
  *resource*: get_api_usage_plans_v2  
  *description*: Returns prediction usage on a monthly basis for the current calendar month and future months. Each apiusage object in the response corresponds to a calendar month in your plan.
* _GET /v2/language/datasets_ 
  *resource*: list_datasets  
  *description*: Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.
* _GET /v2/language/datasets/{datasetId}_ 
  *resource*: get_dataset  
  *description*: Returns a single dataset.
* _GET /v2/vision/datasets_ 
  *resource*: list_datasets_1  
  *description*: Returns a list of datasets and their labels that were created by the current user. The response is sorted by dataset ID.
* _GET /v2/vision/datasets/{datasetId}_ 
  *resource*: get_dataset_1  
  *description*: Returns a single dataset.
* _GET /v2/language/deletion/{id}_ 
  *resource*: get  
  *description*: Returns the status of a language dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.
* _GET /v2/vision/deletion/{id}_ 
  *resource*: get_1  
  *description*: Returns the status of an image dataset or model deletion. When you delete a dataset or model, the deletion may not occur immediately. Use this call to find out when the deletion is complete.
* _GET /v2/language/datasets/{datasetId}/examples_ 
  *resource*: get_examples  
  *description*: Returns all the examples for the specified dataset,
* _GET /v2/language/examples_ 
  *resource*: get_examples_by_label  
  *description*: Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.
* _GET /v2/vision/datasets/{datasetId}/examples_ 
  *resource*: get_examples_1  
  *description*: Returns all the examples for the specified dataset. By default, returns examples created by uploading them from a .zip file.
* _GET /v2/vision/examples_ 
  *resource*: get_examples_by_label_1  
  *description*: Returns all the examples for the specified label. Returns both uploaded examples and feedback examples.
* _GET /v2/language/models/{modelId}/lc_ 
  *resource*: get_trained_model_learning_curve  
  *description*: Returns the metrics for each epoch in a model.
* _GET /v2/vision/models/{modelId}/lc_ 
  *resource*: get_trained_model_learning_curve_1  
  *description*: Returns the metrics for each epoch in a model.
* _GET /v2/language/models/{modelId}_ 
  *resource*: get_trained_model_metrics  
  *description*: Returns the metrics for a model
* _GET /v2/vision/models/{modelId}_ 
  *resource*: get_trained_model_metrics_1  
  *description*: Returns the metrics for a model
* _GET /v2/language/datasets/{datasetId}/models_ 
  *resource*: get_trained_models  
  *description*: Returns all models for the specified dataset.
* _GET /v2/vision/datasets/{datasetId}/models_ 
  *resource*: get_trained_models_1  
  *description*: Returns all models for the specified dataset.
* _GET /v2/language/train/{modelId}_ 
  *resource*: get_train_status_and_progress  
  *description*: Returns the status of a model's training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.
* _GET /v2/vision/train/{modelId}_ 
  *resource*: get_train_status_and_progress_1  
  *description*: Returns the status of a model's training process. Use the progress field to determine how far the training has progressed. When training completes successfully, the status is SUCCEEDED and the progress is 1.
