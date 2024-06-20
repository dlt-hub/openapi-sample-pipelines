from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_bigquery_source", max_table_nesting=2)
def google_bigquery_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Lists all datasets in the specified project to which the user has been granted the READER dataset role.
            {
                "name": "bigquery_datasets_list",
                "table_name": "dataset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "datasets",
                    "path": "/projects/{projectId}/datasets",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "bigquery_projects_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "all": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the dataset specified by datasetID.
            {
                "name": "bigquery_datasets_get",
                "table_name": "dataset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/datasets/{datasetId}",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "bigquery_datasets_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "datasetView": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # RPC to get the results of a query job.
            {
                "name": "bigquery_jobs_get_query_results",
                "table_name": "get_query_results_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/queries/{jobId}",
                    "params": {
                        "jobId": {
                            "type": "resolve",
                            "resource": "bigquery_projects_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "formatOptions.useInt64Timestamp": "OPTIONAL_CONFIG",
                        # "location": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "startIndex": "OPTIONAL_CONFIG",
                        # "timeoutMs": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # RPC to get the service account for a project used for interactions with Google Cloud KMS
            {
                "name": "bigquery_projects_get_service_account",
                "table_name": "get_service_account_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/serviceAccount",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "bigquery_projects_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all jobs that you started in the specified project. Job information is available for a six month period after creation. The job list is sorted in reverse chronological order, by job creation time. Requires the Can View project role, or the Is Owner project role if you set the allUsers property.
            {
                "name": "bigquery_jobs_list",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "jobs",
                    "path": "/projects/{projectId}/jobs",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "bigquery_projects_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "allUsers": "OPTIONAL_CONFIG",
                        # "maxCreationTime": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "minCreationTime": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "parentJobId": "OPTIONAL_CONFIG",
                        # "projection": "OPTIONAL_CONFIG",
                        # "stateFilter": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns information about a specific job. Job information is available for a six month period after creation. Requires that you're the person who ran the job, or have the Is Owner project role.
            {
                "name": "bigquery_jobs_get",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/jobs/{jobId}",
                    "params": {
                        "jobId": {
                            "type": "resolve",
                            "resource": "bigquery_jobs_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "location": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all models in the specified dataset. Requires the READER dataset role. After retrieving the list of models, you can get information about a particular model by calling the models.get method.
            {
                "name": "bigquery_models_list",
                "table_name": "model",
                "endpoint": {
                    "data_selector": "models",
                    "path": "/projects/{projectId}/datasets/{datasetId}/models",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "bigquery_datasets_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the specified model resource by model ID.
            {
                "name": "bigquery_models_get",
                "table_name": "model",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/datasets/{datasetId}/models/{modelId}",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "datasetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # RPC to list projects to which the user has been granted any project role. Users of this method are encouraged to consider the [Resource Manager](https://cloud.google.com/resource-manager/docs/) API, which provides the underlying data for this method and has more capabilities.
            {
                "name": "bigquery_projects_list",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "projects",
                    "path": "/projects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all routines in the specified dataset. Requires the READER dataset role.
            {
                "name": "bigquery_routines_list",
                "table_name": "routine",
                "endpoint": {
                    "data_selector": "routines",
                    "path": "/projects/{projectId}/datasets/{datasetId}/routines",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "bigquery_datasets_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "readMask": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the specified routine resource by routine ID.
            {
                "name": "bigquery_routines_get",
                "table_name": "routine",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/datasets/{datasetId}/routines/{routineId}",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "datasetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "routineId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "readMask": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all row access policies on the specified table.
            {
                "name": "bigquery_row_access_policies_list",
                "table_name": "row_access_policy",
                "endpoint": {
                    "data_selector": "rowAccessPolicies",
                    "path": "/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/rowAccessPolicies",
                    "params": {
                        "tableId": {
                            "type": "resolve",
                            "resource": "bigquery_tables_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "datasetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all tables in the specified dataset. Requires the READER dataset role.
            {
                "name": "bigquery_tables_list",
                "table_name": "table",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tables",
                    "path": "/projects/{projectId}/datasets/{datasetId}/tables",
                    "params": {
                        "datasetId": {
                            "type": "resolve",
                            "resource": "bigquery_datasets_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the specified table resource by table ID. This method does not return the data in the table, it only returns the table resource, which describes the structure of this table.
            {
                "name": "bigquery_tables_get",
                "table_name": "table",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/datasets/{datasetId}/tables/{tableId}",
                    "params": {
                        "tableId": {
                            "type": "resolve",
                            "resource": "bigquery_tables_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "datasetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "selectedFields": "OPTIONAL_CONFIG",
                        # "view": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the content of a table in rows.
            {
                "name": "bigquery_tabledata_list",
                "table_name": "table_row",
                "endpoint": {
                    "data_selector": "rows",
                    "path": "/projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data",
                    "params": {
                        "tableId": {
                            "type": "resolve",
                            "resource": "bigquery_tables_list",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "datasetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "formatOptions.useInt64Timestamp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "selectedFields": "OPTIONAL_CONFIG",
                        # "startIndex": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
