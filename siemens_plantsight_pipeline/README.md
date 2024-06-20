# siemens_plantsight pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/siemens_plantsight.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /imports/{id}_ 
  *resource*: imports_get_by_id_async  
* _GET /jobs_ 
  *resource*: jobs_get_all  
* _GET /jobs/{id}_ 
  *resource*: jobs_get  
* _GET /projects_ 
  *resource*: projects_get_all  
* _GET /projects/{id}_ 
  *resource*: projects_get_by_id  
* _GET /projects/{projectId}/scenarios_ 
  *resource*: scenarios_get_all  
* _GET /projects/{projectId}/scenarios/{scenarioId}_ 
  *resource*: scenarios_get_scenario_by_id_async  
* _GET /usergroups_ 
  *resource*: user_groups_get_all  
* _GET /users_ 
  *resource*: users_get_all  
* _GET /users/{id}_ 
  *resource*: users_get_by_id  
* _GET /users/me_ 
  *resource*: users_get_user_info  
* _GET /projects/{projectId}/viewpoints_ 
  *resource*: viewpoints_get_all  
