# google_bigquery pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/google_bigquery.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /projects/{projectId}/datasets_ 
  *resource*: bigquery_datasets_list  
  *description*: Lists all datasets in the specified project to which the user has been granted the READER dataset role.
* _GET /projects/{projectId}/datasets/{datasetId}_ 
  *resource*: bigquery_datasets_get  
  *description*: Returns the dataset specified by datasetID.
* _GET /projects/{projectId}/queries/{jobId}_ 
  *resource*: bigquery_jobs_get_query_results  
  *description*: RPC to get the results of a query job.
* _GET /projects/{projectId}/serviceAccount_ 
  *resource*: bigquery_projects_get_service_account  
  *description*: RPC to get the service account for a project used for interactions with Google Cloud KMS
* _GET /projects/{projectId}/jobs_ 
  *resource*: bigquery_jobs_list  
  *description*: Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property.
* _GET /projects/{projectId}/jobs/{jobId}_ 
  *resource*: bigquery_jobs_get  
  *description*: Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role.
* _GET /projects/{projectId}/datasets/{datasetId}/models_ 
  *resource*: bigquery_models_list  
  *description*: Lists all models in the specified dataset. Requires the READER dataset role. After retrieving the list of models, you can get information about a particular model by calling the models.get method.
* _GET /projects/{projectId}/datasets/{datasetId}/models/{modelId}_ 
  *resource*: bigquery_models_get  
  *description*: Gets the specified model resource by model ID.
* _GET /projects_ 
  *resource*: bigquery_projects_list  
  *description*: RPC to list projects to which the user has been granted any project role. Users of this method are encouraged to consider the [Resource Manager](https://cloud.google.com/resource-manager/docs/) API, which provides the underlying data for this method and has more capabilities.
* _GET /projects/{projectId}/datasets/{datasetId}/routines_ 
  *resource*: bigquery_routines_list  
  *description*: Lists all routines in the specified dataset. Requires the READER dataset role.
* _GET /projects/{projectId}/datasets/{datasetId}/routines/{routineId}_ 
  *resource*: bigquery_routines_get  
  *description*: Gets the specified routine resource by routine ID.
* _GET /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies_ 
  *resource*: bigquery_row_access_policies_list  
  *description*: Lists all row access policies on the specified table.
* _GET /projects/{projectId}/datasets/{datasetId}/tables_ 
  *resource*: bigquery_tables_list  
  *description*: Lists all tables in the specified dataset. Requires the READER dataset role.
* _GET /projects/{projectId}/datasets/{datasetId}/tables/{tableId}_ 
  *resource*: bigquery_tables_get  
  *description*: Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table.
* _GET /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data_ 
  *resource*: bigquery_tabledata_list  
  *description*: List the content of a table in rows.
