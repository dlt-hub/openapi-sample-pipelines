from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="strapi_source", max_table_nesting=2)
def strapi_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Return comments on a post with postId={id}.
            {
                "name": "comment",
                "table_name": "comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/comments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "postId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a post with postId equals to id.
            {
                "name": "entry",
                "table_name": "entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/:pluralposts/{pluralApiId}",
                    "params": {
                        "pluralApiId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
