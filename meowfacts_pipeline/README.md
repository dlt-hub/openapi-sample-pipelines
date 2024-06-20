# meowfacts pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/meowfacts.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /_ 
  *resource*: fact  
  *description*: By passing in the appropriate options, you can recieve a specific or more than one fact. 
* _GET /health_ 
  *resource*: healthcheck_data  
  *description*: The health check endpoint will return a status of 200 if the api is up and ready to recieve connections. It will tell the uptime, and total requests served since last restart. It also has a field for version which corresponds to the versioned release from the github repo.   
* _GET /options_ 
  *resource*: options_object  
  *description*: This endpoint will list all languages available to the root endpoint.    
