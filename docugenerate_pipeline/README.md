# docugenerate pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/docugenerate.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /v1/document_ 
  *resource*: query_documents  
  *description*: Get all the documents generated from template `template_id`.<br><br> The `template_id` needs to be passed as a query parameter.<br><br> Results are ordered by the `created` time in descending order.
* _GET /v1/document/{id}_ 
  *resource*: get_document  
  *description*: Get a document by `id`.
* _GET /v1/template_ 
  *resource*: query_templates  
  *description*: Get all the templates ordered by the `created` time in descending order.
* _GET /v1/template/{id}_ 
  *resource*: get_template  
  *description*: Get a template by `id`.
