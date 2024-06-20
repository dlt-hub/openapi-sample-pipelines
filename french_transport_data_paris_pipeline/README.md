# french_transport_data_paris pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/french_transport_data_paris.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /catalog/datasets/{dataset_id}/attachments_ 
  *resource*: get_dataset_attachments  
  *description*: Returns a list of all available attachments for a dataset. 
* _GET /catalog/exports/csv_ 
  *resource*: export_catalog_csv  
  *description*: Export a catalog in CSV (Comma Separated Values). Specific parameters are described here
* _GET /catalog/datasets/{dataset_id}/exports/csv_ 
  *resource*: export_records_csv  
  *description*: Export a dataset in CSV (Comma Separated Values). Specific parameters are described here
* _GET /catalog/datasets_ 
  *resource*: get_datasets  
  *description*: Retrieve available datasets.
* _GET /catalog/datasets/{dataset_id}_ 
  *resource*: get_dataset  
  *description*: Returns a list of available endpoints for the specified dataset, with metadata and endpoints.  The response includes the following links: * the attachments endpoint * the files endpoint * the records endpoint * the catalog endpoint.
* _GET /catalog/exports_ 
  *resource*: list_export_formats  
  *description*: List available export formats
* _GET /catalog/exports/{format}_ 
  *resource*: export_datasets  
  *description*: Export a catalog in the desired format.
* _GET /catalog/datasets/{dataset_id}/exports_ 
  *resource*: list_dataset_export_formats  
  *description*: List available export formats
* _GET /catalog/datasets/{dataset_id}/exports/{format}_ 
  *resource*: export_records  
  *description*: Export a dataset in the desired format. **Note:** The `group_by` parameter is only available on exports starting with the v2.1
* _GET /catalog/facets_ 
  *resource*: get_datasets_facets  
  *description*: Enumerate facet values for datasets and returns a list of values for each facet. Can be used to implement guided navigation in large result sets.
* _GET /catalog/datasets/{dataset_id}/facets_ 
  *resource*: get_records_facets  
  *description*: Enumerates facet values for records and returns a list of values for each facet. Can be used to implement guided navigation in large result sets. 
* _GET /catalog/datasets/{dataset_id}/exports/gpx_ 
  *resource*: export_records_gpx  
  *description*: Export a dataset in GPX. Specific parameters are described here
* _GET /catalog/datasets/{dataset_id}/records_ 
  *resource*: get_records  
  *description*: Perform a query on dataset records.
* _GET /catalog/datasets/{dataset_id}/records/{record_id}_ 
  *resource*: get_record  
  *description*: Reads a single dataset record based on its identifier. 
