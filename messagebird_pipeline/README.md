# messagebird pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/messagebird.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /api/v1/datasets_ 
  *resource*: intent_list_datasets  
  *description*: Lists datasets containing intents and corresponding phrases. You can choose to list only your own datasets, as well as template datasets, or both. Template datasets are used as examples and can be found under the `Templates` tab in the [dataset overview of the dashboard](https://dashboard.messagebird.com/knowledge-base/list). You can clone such datasets to kickstart the creation of a dataset that is tailored to your use-case.   Note that the results are paginated and so you might need to iteratively call this endpoint to obtain all your datasets.
* _GET /api/v1/datasets/{datasetId}_ 
  *resource*: intent_get_dataset  
  *description*: Retrieves the dataset for the given dataset ID. It only displays the metadata corresponding to the dataset. If you want to view the individual intent phrases that you have added, you can use the [dataset section of the dashboard](https://dashboard.messagebird.com/knowledge-base/list).
* _GET /api/v1/supported-languages_ 
  *resource*: intent_list_supported_languages  
  *description*: Lists the languages supported by the Intent API.
