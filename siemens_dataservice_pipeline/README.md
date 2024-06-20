# siemens_dataservice pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/siemens_dataservice.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /DataService/Adapters_ 
  *resource*: get_data_service_adapters  
  *description*: Get a list of all available Adapters.
* _GET /DataService/Adapters/{id}_ 
  *resource*: get_data_service_adaptersid  
  *description*: Read a specific adapter with the id from path.
* _GET /DataService/Aggregations/{id}_ 
  *resource*: get_data_service_aggregationsid  
  *description*: Return the specified aggregation.
* _GET /DataService/Aggregations_ 
  *resource*: get_data_service_aggregations  
  *description*: Get a list of aggregations, aggregations can be filtered by variable ids
* _GET /DataService/Aspects_ 
  *resource*: get_data_service_aspects  
  *description*: Get a list of Aspects. Aspects can be filtered by aspectId or assetId. If no filter is specified, all aspects will be returned. It is not supported to specify more than one filter parameter.
* _GET /DataService/Aspects/{id}_ 
  *resource*: get_data_service_aspectsid  
  *description*: Read a specific aspect with the id from path.
* _GET /DataService/AspectTypes_ 
  *resource*: get_data_service_aspect_types  
  *description*: Get a list of aspect types. It can be configured to also return the according aspect type variables.
* _GET /DataService/AspectTypes/{id}_ 
  *resource*: get_data_service_aspect_typesid  
  *description*: Read a specific aspect type. It can be configured to also return the according aspect type variables.
* _GET /AssetService/Assets_ 
  *resource*: get_asset_service_assets  
  *description*: Get a list of assets. Assets can be filtered by assetId. Breadcrumb and children can be added to the response if specific assets are requested.
* _GET /AssetService/Assets/{id}_ 
  *resource*: get_asset_service_assetsid  
  *description*: Read an specific asset. Breadcrumb and children can be added to the response.
* _GET /AssetService/Assets/Root_ 
  *resource*: get_asset_service_assets_root  
  *description*: The root asset is created automatically. It can not be deleted. Returns root asset if defined its children and breadcrumb.
* _GET /AssetService/Assets/{id}/children_ 
  *resource*: get_asset_service_assetsidchildren  
  *description*: Read all child assets of a specified asset.
* _GET /AssetService/Assets/{id}/decendants_ 
  *resource*: get_asset_service_assetsiddecendants  
  *description*: Read all descendent assets of a specified asset.
* _GET /AssetService/Assets/{id}/breadcrumb_ 
  *resource*: get_asset_service_assetsidbreadcrumb  
  *description*: Read all breadcrumb assets of a specified asset.
* _GET /AssetService/Assets/Tree_ 
  *resource*: get_asset_service_assets_tree  
  *description*: Get all assets, build together as a tree.
* _GET /DataService/Adapters/{id}/browse_ 
  *resource*: get_data_service_adaptersidbrowse  
  *description*: Browse an active adapter that supports browsing. All available tags will be returned.
* _GET /DataService/CalculateJobCollections/{id}_ 
  *resource*: get_data_service_calculate_job_collectionsid  
* _GET /DataService/Backup/Config_ 
  *resource*: get_data_service_backup_config  
  *description*: Download the whole configuration backup. This includes Adapters, Aspects, AspectTypes, Assets, Aggregations, DataRetentions and Variables. This is configured as an automatic file download
* _GET /DataService/Data/{id}/Count_ 
  *resource*: get_data_service_dataid_count  
  *description*: Count data for a selected variable within a time range.
* _GET /TokenManagerService/users/create_ 
  *resource*: get_token_manager_serviceuserscreate  
  *description*: Create a user, as dataservice c++ does not support body content in get request, only a default user will be returned. This route is deprecated and will be supported until 2023-09-07.
* _GET /DataService/Data_ 
  *resource*: get_data_service_data  
  *description*: Get time series data of multiple variables.
* _GET /DataService/Data/{id}_ 
  *resource*: get_data_service_dataid  
  *description*: Get time series data of a single variable.
* _GET /DataService/DataRetentions_ 
  *resource*: get_data_service_data_retentions  
  *description*: Get the data retention setting of the specified asset, aspect or variable. If there is no data retention configured at the object, the data retention settings inherited from an parent object will be returned if there is some.
* _GET /DataService/DataSources_ 
  *resource*: get_data_service_data_sources  
  *description*: Get all existing datasources from an asset.
* _GET /KPIService/DataSources_ 
  *resource*: get_kpi_service_data_sources  
  *description*: Get all existing datasources from an asset. Same route than GET /DataService/DataSources.  This route is deprecated and will be supported until 2023-09-07.
* _GET /DataService/Backup/Data_ 
  *resource*: get_data_service_backup_data  
  *description*: Download the whole data backup. This includes all content from all variables and aggregation variables. This is configured as an automatic file download
* _GET /DataService/CalculateJobCollections/Ids_ 
  *resource*: get_data_service_calculate_job_collections_ids  
* _GET /DataService/Service/IsRunning_ 
  *resource*: get_data_service_service_is_running  
  *description*: Can be called to check if dataservice is available.
* _GET /TokenManagerService/Service/IsRunning_ 
  *resource*: get_token_manager_service_service_is_running  
  *description*: Can be called to check if dataservice is available. This route is deprecated and will be supported until 2023-09-07.
* _GET /TokenManagerService/users/me_ 
  *resource*: get_token_manager_serviceusersme  
  *description*: Get own user. The returned user is only a predefined user. This route is deprecated and will be supported until 2023-09-07.
* _GET /DataService/Adapters/{id}/RawMetaData_ 
  *resource*: get_data_service_adaptersid_raw_meta_data  
  *description*: Get raw meta data from an active adapter that supports browsing. The meta data is dependent on the used adapter.
* _GET /DataService/Aggregations/{id}/Reset_ 
  *resource*: get_data_service_aggregationsid_reset  
  *description*: Delete all generated data of the specified aggregation.
* _GET /DataService/Data/Size_ 
  *resource*: get_data_service_data_size  
  *description*: Return the size of the internal database.
* _GET /DataService/Data/{id}/Size_ 
  *resource*: get_data_service_dataid_size  
  *description*: Return the size of one variable in the internal database.
* _GET /TokenManagerService/identitymanagement/v3/users_ 
  *resource*: get_token_manager_serviceidentitymanagementv_3_users  
  *description*: Get list of predefined identity users. The list cannot be extented. This route is deprecated and will be supported until 2023-09-07.
* _GET /TokenManagerService/identitymanagement/v3/users/{id}_ 
  *resource*: get_token_manager_serviceidentitymanagementv_3_usersid  
  *description*: Get a predefined identity users. This route is deprecated and will be supported until 2023-09-07.
* _GET /TokenManagerService/oauth_token_ 
  *resource*: get_token_manager_serviceoauth_token  
  *description*: Provide a cookie and get a session token. The session token is a constant.
* _GET /TokenManagerService/token_keys_ 
  *resource*: get_token_manager_servicetoken_keys  
  *description*: Get public key to sign a token. This route is deprecated and will be supported until 2023-09-07.
* _GET /TokenManagerService/users_ 
  *resource*: get_token_manager_serviceusers  
  *description*: Get list of predefined users. The list cannot be extented. This route is deprecated and will be supported until 2023-09-07.
* _GET /TokenManagerService/users/{id}_ 
  *resource*: get_token_manager_serviceusersid  
  *description*: Get a user. The returned user is only a predefined user. This route is deprecated and will be supported until 2023-09-07.
* _GET /DataService/Variables_ 
  *resource*: get_data_service_variables  
  *description*: Get a list of Variables. Variables can be filtered by assetsIds, aspectIds, adapterIds or variableIds. If no filter is specified, all variables will be returned. It is not supported to specify more than one filter parameter.
* _GET /DataService/Variables/{id}_ 
  *resource*: get_data_service_variablesid  
  *description*: Read a specific variable with the id from path.
* _GET /DataService/VariableConfigurations/{id}_ 
  *resource*: get_data_service_variable_configurationsid  
  *description*: Get a variable configuration. If not found a default configuration will be send.
* _GET /DataService/Service/Version_ 
  *resource*: get_data_service_service_version  
  *description*: Get the current version of dataservice.
