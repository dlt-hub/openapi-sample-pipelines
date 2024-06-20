from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="heroku_app_source", max_table_nesting=2)
def heroku_app_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "check",
                "table_name": "check",
                "endpoint": {
                    "path": "/check",
                    "paginator": "auto",
                },
            },
            {
                "name": "stats_id",
                "table_name": "id",
                "endpoint": {
                    "path": "/stats/id/{plateform}/{id}",
                    "params": {
                        "plateform": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "pve_info",
                "table_name": "info",
                "endpoint": {
                    "path": "/pve/info",
                    "paginator": "auto",
                },
            },
            {
                "name": "news",
                "table_name": "news",
                "endpoint": {
                    "path": "/news",
                    "paginator": "auto",
                },
            },
            {
                "name": "stats",
                "table_name": "stat",
                "endpoint": {
                    "path": "/stats/{plateform}/{username}",
                    "params": {
                        "plateform": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "store",
                "table_name": "store",
                "endpoint": {
                    "path": "/store",
                    "paginator": "auto",
                },
            },
            {
                "name": "pve_user",
                "table_name": "user",
                "endpoint": {
                    "path": "/pve/user/{username}",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "user",
                "table_name": "user",
                "endpoint": {
                    "path": "/user/{plateform}/{username}",
                    "params": {
                        "plateform": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
