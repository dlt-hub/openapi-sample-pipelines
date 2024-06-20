# explore_education_statistics pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/explore_education_statistics.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /api/v1/data-sets/{dataSetId}/versions/{dataSetVersion}/changes_ 
  *resource*: get_data_set_version_changes  
  *description*: Get a data set version's list of changes.
* _GET /api/v1/data-sets/{dataSetId}/versions_ 
  *resource*: list_data_set_versions  
  *description*: List a data set's versions. Only provides summary information of each version.
* _GET /api/v1/data-sets/{dataSetId}/versions/{dataSetVersion}_ 
  *resource*: get_data_set_version  
  *description*: Get a data set version, including a full list of its changes.
* _GET /api/v1/publications/{publicationId}/data-sets_ 
  *resource*: list_publication_data_sets  
  *description*: Lists summary details of all the data sets related to a publication.
* _GET /api/v1/data-sets/{dataSetId}_ 
  *resource*: get_data_set  
  *description*: Gets a specific data set's summary details.
* _GET /api/v1/data-sets/{dataSetId}/file_ 
  *resource*: get_data_set_file  
  *description*: Get the entire data set in a specified file format.
* _GET /api/v1/data-sets/{dataSetId}/meta_ 
  *resource*: get_data_set_meta  
  *description*: Get the metadata about a data set. Use this to create data set queries.
* _GET /api/v1/data-sets/{dataSetId}/meta/filters_ 
  *resource*: get_data_set_meta_filters  
  *description*: Get the filter metadata about a data set. Use this to create data set queries.
* _GET /api/v1/data-sets/{dataSetId}/query_ 
  *resource*: query_data_set_get  
  *description*: Query a data set using a `GET` request, returning the filtered results.  Note that there is a `POST` variant of this endpoint which provides a more complete set of querying functionality. The `GET` variant is only recommended for initial exploratory  testing or simple queries that do not need advanced functionality.  Unlike the `POST` variant, this endpoint does not allow condition clauses (`and`, `or`, `not`) and consequently cannot express more complex queries.
* _GET /api/v1/data-sets/{dataSetId}/meta/geographic_ 
  *resource*: get_data_set_meta_geographic  
  *description*: Get the geographic metadata about a data set. Use this to create data set queries.
* _GET /api/v1/data-sets/{dataSetId}/meta/indicators_ 
  *resource*: get_data_set_meta_indicators  
  *description*: Get the indicator metadata about a data set. Use this to create data set queries.
* _GET /api/v1/publications_ 
  *resource*: list_publications  
  *description*: Lists details about publications with data available for querying.
* _GET /api/v1/publications/{publicationId}_ 
  *resource*: get_publication  
  *description*: Gets a specific publication's details.
* _GET /api/v1/data-sets/{dataSetId}/meta/time-periods_ 
  *resource*: get_data_set_meta_time_periods  
  *description*: Get the time period metadata about a data set. Use this to create data set queries.
