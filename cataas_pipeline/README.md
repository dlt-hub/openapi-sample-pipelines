# cataas pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/cataas.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /admin/cats_ 
  *resource*: admincatsbrowse  
  *description*: Browse cats
* _GET /cat_ 
  *resource*: catrandom  
  *description*: Get a random cat
* _GET /cat/{id}_ 
  *resource*: catget  
  *description*: Get cat by id
* _GET /cat/{tag}_ 
  *resource*: catrandomtag  
  *description*: Get random cat by tag
* _GET /api/cats_ 
  *resource*: apicats  
  *description*: Will return all cats
* _GET /api/count_ 
  *resource*: apicount  
  *description*: Count how many cat
* _GET /cat/says/{text}_ 
  *resource*: catrandomtext  
  *description*: Get random cat saying text
* _GET /cat/{id}/says/{text}_ 
  *resource*: catgettext  
  *description*: Get cat by id saying text
* _GET /cat/{tag}/says/{text}_ 
  *resource*: catrandomtagtext  
  *description*: Get random cat by tag saying text
* _GET /api/tags_ 
  *resource*: apitags  
  *description*: Will return all tags
