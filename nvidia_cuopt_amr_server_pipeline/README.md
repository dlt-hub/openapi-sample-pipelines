# nvidia_cuopt_amr_server pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/nvidia_cuopt_amr_server.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /cuopt/health_ 
  *resource*: health  
  *description*: To ping if server is running
* _GET /v2/health/live_ 
  *resource*: live  
  *description*: To check liveness of the server
* _GET /v2/health/ready_ 
  *resource*: ready  
  *description*: To check readiness of the server
* _GET /cuopt/routes/{id}_ 
  *resource*: response_routes_result_cuopt_routes_id_get  
  *description*: Note: This is for self hosted. Query a previously submitted request which timed out. The 'id' is the uuid returned when the original request timed out.
