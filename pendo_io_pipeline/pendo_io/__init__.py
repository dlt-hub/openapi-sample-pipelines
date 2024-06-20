from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="pendo_io_source", max_table_nesting=2)
def pendo_io_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "offset",
                "limit": 20,
                "offset_param": "start",
                "limit_param": "limit",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            {
                "name": "get_accounts",
                "table_name": "account",
                "endpoint": {
                    "path": "/accounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "order_dir": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_accountsid",
                "table_name": "account",
                "endpoint": {
                    "path": "/accounts/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # get a list of Comment records
            {
                "name": "get_comments",
                "table_name": "comment",
                "endpoint": {
                    "path": "/comments",
                    "params": {
                        "case_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_features",
                "table_name": "feature",
                "endpoint": {
                    "path": "/features",
                    "params": {
                        # the parameters below can optionally be configured
                        # "order_dir": "OPTIONAL_CONFIG",
                        # "is_private": "OPTIONAL_CONFIG",
                        # "wanted_by": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "products": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_featuresid",
                "table_name": "feature",
                "endpoint": {
                    "path": "/features/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Provides a response for automatic checks that the API and load balancers are healthy
            {
                "name": "get_health_checkping",
                "table_name": "ping",
                "endpoint": {
                    "path": "/health-check/ping",
                },
            },
            {
                "name": "get_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/search",
                    "params": {
                        "scope": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "products": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_userssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/users/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "external_id": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                        # "role": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_accountsidtags",
                "table_name": "tag",
                "endpoint": {
                    "path": "/accounts/{id}/tags",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_featuresidtags",
                "table_name": "tag",
                "endpoint": {
                    "path": "/features/{id}/tags",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_usersidtags",
                "table_name": "tag",
                "endpoint": {
                    "path": "/users/{id}/tags",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # get a list of User records
            {
                "name": "get_users",
                "table_name": "user",
                "endpoint": {
                    "path": "/users",
                    "params": {
                        "role": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "account": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                        # "order_dir": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_usersid",
                "table_name": "user",
                "endpoint": {
                    "path": "/users/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_votes",
                "table_name": "vote",
                "endpoint": {
                    "path": "/votes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "user_id": "OPTIONAL_CONFIG",
                        # "feature_id": "OPTIONAL_CONFIG",
                        # "positive": "OPTIONAL_CONFIG",
                        # "negative": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
