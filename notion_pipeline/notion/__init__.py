from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="notion_source", max_table_nesting=2)
def notion_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Retrieve a block
            {
                "name": "block",
                "table_name": "block",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/blocks/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve block children
            {
                "name": "child",
                "table_name": "child",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/v1/blocks/{id}/children",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a user object using the ID specified in the request path.
            {
                "name": "comment",
                "table_name": "comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/v1/comments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "block_id": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a database object using the ID specified in the request path.
            {
                "name": "databasis",
                "table_name": "databasis",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/databases/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a Page object using the ID in the request path. This endpoint exposes page properties, not page content.
            {
                "name": "page",
                "table_name": "page",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/pages/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a Page Property Item
            {
                "name": "property",
                "table_name": "property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/pages/{page_id}/properties/{property_id}",
                    "params": {
                        "page_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "property_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a user object using the ID specified in the request path.
            {
                "name": "user",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
