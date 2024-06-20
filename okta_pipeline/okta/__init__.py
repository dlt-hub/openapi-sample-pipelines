from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="okta_source", max_table_nesting=2)
def okta_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Get Assigned App Links
            {
                "name": "get_assigned_app_links",
                "table_name": "app_link",
                "endpoint": {
                    "path": "/api/v1/users/{userId}/appLinks",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get Groups for User
            {
                "name": "get_groups_for_user",
                "table_name": "group",
                "endpoint": {
                    "path": "/api/v1/users/{userId}/groups",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get Current User
            {
                "name": "get_current_user",
                "table_name": "me",
                "endpoint": {
                    "path": "/api/v1/users/me",
                    "paginator": "auto",
                },
            },
            # Find User
            {
                "name": "find_user",
                "table_name": "user",
                "endpoint": {
                    "path": "/api/v1/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get User
            {
                "name": "get_user",
                "table_name": "user",
                "endpoint": {
                    "path": "/api/v1/users/{userId}",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
