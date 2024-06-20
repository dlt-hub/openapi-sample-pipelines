from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="imgur_source", max_table_nesting=2)
def imgur_source(
    api_key: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "api_key",
                "api_key": api_key,
                "name": "Authorization",
                "location": "header",
            },
        },
        "resources": [
            {
                "name": "get_account",
                "table_name": "account_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/3/account/{userName}",
                    "params": {
                        "userName": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_account_images_count",
                "table_name": "basic_int_32_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/3/account/{userName}/images/count",
                    "params": {
                        "userName": {
                            "type": "resolve",
                            "resource": "get_account_images",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_account_images",
                "table_name": "image",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/3/account/{userName}/images",
                    "params": {
                        "userName": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_account_image",
                "table_name": "image_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/3/account/{userName}/images/{imageHash}",
                    "params": {
                        "imageHash": {
                            "type": "resolve",
                            "resource": "get_account_images",
                            "field": "id",
                        },
                        "userName": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_image",
                "table_name": "image_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/3/image/{imageHash}",
                    "params": {
                        "imageHash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
