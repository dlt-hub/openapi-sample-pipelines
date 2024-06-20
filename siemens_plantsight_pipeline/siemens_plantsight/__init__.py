from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="siemens_plantsight_source", max_table_nesting=2)
def siemens_plantsight_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
        },
        "resources": [
            {
                "name": "imports_get_by_id_async",
                "table_name": "import",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/imports/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "jobs_get_all",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/jobs",
                    "paginator": "auto",
                },
            },
            {
                "name": "jobs_get",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/jobs/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "jobs_get_all",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "projects_get_all",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects",
                    "paginator": "auto",
                },
            },
            {
                "name": "projects_get_by_id",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "projects_get_all",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "scenarios_get_all",
                "table_name": "scenario",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/scenarios",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "projects_get_all",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "scenarios_get_scenario_by_id_async",
                "table_name": "scenario",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/scenarios/{scenarioId}",
                    "params": {
                        "scenarioId": {
                            "type": "resolve",
                            "resource": "scenarios_get_all",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "user_groups_get_all",
                "table_name": "user_group",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/usergroups",
                    "paginator": "auto",
                },
            },
            {
                "name": "users_get_all",
                "table_name": "user_info",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "loginname": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "users_get_by_id",
                "table_name": "user_info",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "users_get_all",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "users_get_user_info",
                "table_name": "user_info",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/me",
                    "paginator": "auto",
                },
            },
            {
                "name": "viewpoints_get_all",
                "table_name": "viewpoint",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/viewpoints",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "projects_get_all",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
