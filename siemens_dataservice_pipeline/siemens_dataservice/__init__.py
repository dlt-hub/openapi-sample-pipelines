from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="siemens_dataservice_source", max_table_nesting=2)
def siemens_dataservice_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Get a list of all available Adapters.
            {
                "name": "get_data_service_adapters",
                "table_name": "adapter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "adapters",
                    "path": "/DataService/Adapters",
                    "paginator": "auto",
                },
            },
            # Read a specific adapter with the id from path.
            {
                "name": "get_data_service_adaptersid",
                "table_name": "adapter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Adapters/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_adapters",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the specified aggregation.
            {
                "name": "get_data_service_aggregationsid",
                "table_name": "aggregation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Aggregations/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_aggregations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of aggregations, aggregations can be filtered by variable ids
            {
                "name": "get_data_service_aggregations",
                "table_name": "aggregation_object",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Aggregations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "variableIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of Aspects. Aspects can be filtered by aspectId or assetId. If no filter is specified, all aspects will be returned. It is not supported to specify more than one filter parameter.
            {
                "name": "get_data_service_aspects",
                "table_name": "aspect",
                "primary_key": "aspectId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "aspects",
                    "path": "/DataService/Aspects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "aspectIds": "OPTIONAL_CONFIG",
                        # "assetIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Read a specific aspect with the id from path.
            {
                "name": "get_data_service_aspectsid",
                "table_name": "aspect",
                "primary_key": "aspectId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Aspects/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_aspects",
                            "field": "aspectId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of aspect types. It can be configured to also return the according aspect type variables.
            {
                "name": "get_data_service_aspect_types",
                "table_name": "aspect_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/AspectTypes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "includeVariables": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Read a specific aspect type. It can be configured to also return the according aspect type variables.
            {
                "name": "get_data_service_aspect_typesid",
                "table_name": "aspect_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/AspectTypes/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_aspect_types",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "includeVariables": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of assets. Assets can be filtered by assetId. Breadcrumb and children can be added to the response if specific assets are requested.
            {
                "name": "get_asset_service_assets",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "assets",
                    "path": "/AssetService/Assets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "assetIds": "OPTIONAL_CONFIG",
                        # "includeChildren": "false",
                        # "includeBreadcrumb": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Read an specific asset. Breadcrumb and children can be added to the response.
            {
                "name": "get_asset_service_assetsid",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/AssetService/Assets/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_asset_service_assets",
                            "field": "assetId",
                        },
                        # the parameters below can optionally be configured
                        # "includeChildren": "false",
                        # "includeBreadcrumb": "false",
                    },
                    "paginator": "auto",
                },
            },
            # The root asset is created automatically. It can not be deleted. Returns root asset if defined its children and breadcrumb.
            {
                "name": "get_asset_service_assets_root",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "children",
                    "path": "/AssetService/Assets/Root",
                    "params": {
                        # the parameters below can optionally be configured
                        # "includeChildren": "false",
                        # "includeBreadcrumb": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Read all child assets of a specified asset.
            {
                "name": "get_asset_service_assetsidchildren",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "assets",
                    "path": "/AssetService/Assets/{id}/children",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_asset_service_assets",
                            "field": "assetId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Read all descendent assets of a specified asset.
            {
                "name": "get_asset_service_assetsiddecendants",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "assets",
                    "path": "/AssetService/Assets/{id}/decendants",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_asset_service_assets",
                            "field": "assetId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Read all breadcrumb assets of a specified asset.
            {
                "name": "get_asset_service_assetsidbreadcrumb",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "assets",
                    "path": "/AssetService/Assets/{id}/breadcrumb",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_asset_service_assets",
                            "field": "assetId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get all assets, build together as a tree.
            {
                "name": "get_asset_service_assets_tree",
                "table_name": "asset",
                "primary_key": "assetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "children",
                    "path": "/AssetService/Assets/Tree",
                    "paginator": "auto",
                },
            },
            # Browse an active adapter that supports browsing. All available tags will be returned.
            {
                "name": "get_data_service_adaptersidbrowse",
                "table_name": "browse",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/DataService/Adapters/{id}/browse",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_adapters",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_data_service_calculate_job_collectionsid",
                "table_name": "calculate_job_collection_result",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/CalculateJobCollections/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fetchMode": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Download the whole configuration backup. This includes Adapters, Aspects, AspectTypes, Assets, Aggregations, DataRetentions and Variables. This is configured as an automatic file download
            {
                "name": "get_data_service_backup_config",
                "table_name": "config",
                "endpoint": {
                    "path": "/DataService/Backup/Config",
                    "paginator": "auto",
                },
            },
            # Count data for a selected variable within a time range.
            {
                "name": "get_data_service_dataid_count",
                "table_name": "count",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Data/{id}/Count",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Create a user, as dataservice c++ does not support body content in get request, only a default user will be returned. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_serviceuserscreate",
                "table_name": "create",
                "endpoint": {
                    "data_selector": "roles",
                    "path": "/TokenManagerService/users/create",
                    "paginator": "auto",
                },
            },
            # Get time series data of multiple variables.
            {
                "name": "get_data_service_data",
                "table_name": "data",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/DataService/Data",
                    "params": {
                        "variableIds": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get time series data of a single variable.
            {
                "name": "get_data_service_dataid",
                "table_name": "data_response_array",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Data/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the data retention setting of the specified asset, aspect or variable. If there is no data retention configured at the object, the data retention settings inherited from an parent object will be returned if there is some.
            {
                "name": "get_data_service_data_retentions",
                "table_name": "data_retention",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/DataRetentions",
                    "params": {
                        "sourceId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "sourceTypeId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all existing datasources from an asset.
            {
                "name": "get_data_service_data_sources",
                "table_name": "data_source",
                "endpoint": {
                    "data_selector": "path",
                    "path": "/DataService/DataSources",
                    "params": {
                        "assetId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all existing datasources from an asset. Same route than GET /DataService/DataSources.  This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_kpi_service_data_sources",
                "table_name": "data_source",
                "endpoint": {
                    "path": "/KPIService/DataSources",
                    "params": {
                        "assetId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Download the whole data backup. This includes all content from all variables and aggregation variables. This is configured as an automatic file download
            {
                "name": "get_data_service_backup_data",
                "table_name": "datum",
                "endpoint": {
                    "path": "/DataService/Backup/Data",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_data_service_calculate_job_collections_ids",
                "table_name": "id",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/CalculateJobCollections/Ids",
                    "paginator": "auto",
                },
            },
            # Can be called to check if dataservice is available.
            {
                "name": "get_data_service_service_is_running",
                "table_name": "is_running",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Service/IsRunning",
                    "paginator": "auto",
                },
            },
            # Can be called to check if dataservice is available. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_service_service_is_running",
                "table_name": "is_running",
                "endpoint": {
                    "path": "/TokenManagerService/Service/IsRunning",
                    "paginator": "auto",
                },
            },
            # Get own user. The returned user is only a predefined user. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_serviceusersme",
                "table_name": "me",
                "endpoint": {
                    "data_selector": "roles",
                    "path": "/TokenManagerService/users/me",
                    "paginator": "auto",
                },
            },
            # Get raw meta data from an active adapter that supports browsing. The meta data is dependent on the used adapter.
            {
                "name": "get_data_service_adaptersid_raw_meta_data",
                "table_name": "raw_meta_datum",
                "endpoint": {
                    "path": "/DataService/Adapters/{id}/RawMetaData",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_adapters",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Delete all generated data of the specified aggregation.
            {
                "name": "get_data_service_aggregationsid_reset",
                "table_name": "reset",
                "endpoint": {
                    "path": "/DataService/Aggregations/{id}/Reset",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_aggregations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the size of the internal database.
            {
                "name": "get_data_service_data_size",
                "table_name": "size",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Data/Size",
                    "paginator": "auto",
                },
            },
            # Return the size of one variable in the internal database.
            {
                "name": "get_data_service_dataid_size",
                "table_name": "size",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Data/{id}/Size",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get list of predefined identity users. The list cannot be extented. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_serviceidentitymanagementv_3_users",
                "table_name": "token_identity_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "resources",
                    "path": "/TokenManagerService/identitymanagement/v3/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a predefined identity users. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_serviceidentitymanagementv_3_usersid",
                "table_name": "token_identity_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/TokenManagerService/identitymanagement/v3/users/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_token_manager_serviceidentitymanagementv_3_users",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Provide a cookie and get a session token. The session token is a constant.
            {
                "name": "get_token_manager_serviceoauth_token",
                "table_name": "token_information",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/TokenManagerService/oauth_token",
                    "paginator": "auto",
                },
            },
            # Get public key to sign a token. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_servicetoken_keys",
                "table_name": "token_key",
                "endpoint": {
                    "path": "/TokenManagerService/token_keys",
                    "paginator": "auto",
                },
            },
            # Get list of predefined users. The list cannot be extented. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_serviceusers",
                "table_name": "token_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/TokenManagerService/users",
                    "paginator": "auto",
                },
            },
            # Get a user. The returned user is only a predefined user. This route is deprecated and will be supported until 2023-09-07.
            {
                "name": "get_token_manager_serviceusersid",
                "table_name": "token_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/TokenManagerService/users/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_token_manager_serviceusers",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of Variables. Variables can be filtered by assetsIds, aspectIds, adapterIds or variableIds. If no filter is specified, all variables will be returned. It is not supported to specify more than one filter parameter.
            {
                "name": "get_data_service_variables",
                "table_name": "variable",
                "primary_key": "variableId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "variables",
                    "path": "/DataService/Variables",
                    "params": {
                        # the parameters below can optionally be configured
                        # "assetIds": "OPTIONAL_CONFIG",
                        # "aspectIds": "OPTIONAL_CONFIG",
                        # "adapterIds": "OPTIONAL_CONFIG",
                        # "variable": "OPTIONAL_CONFIG",
                        # "cloudSync": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Read a specific variable with the id from path.
            {
                "name": "get_data_service_variablesid",
                "table_name": "variable",
                "primary_key": "variableId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Variables/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_data_service_variables",
                            "field": "variableId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a variable configuration. If not found a default configuration will be send.
            {
                "name": "get_data_service_variable_configurationsid",
                "table_name": "variable_configuration",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/VariableConfigurations/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get the current version of dataservice.
            {
                "name": "get_data_service_service_version",
                "table_name": "version",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/DataService/Service/Version",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
