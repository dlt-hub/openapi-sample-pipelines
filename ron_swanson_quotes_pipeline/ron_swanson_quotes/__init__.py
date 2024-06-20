from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="ron_swanson_quotes_source", max_table_nesting=2)
def ron_swanson_quotes_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Returns a single Ron Swanson quote wrapped in an array
            {
                "name": "get_quotes",
                "table_name": "quote",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/quotes",
                    "paginator": "auto",
                },
            },
            # Returns {count} quotes in an array
            {
                "name": "get_quotescount",
                "table_name": "quote",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/quotes/{count}",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns an array of quotes matching {term} without case sensitivity
            {
                "name": "get_quotessearchterm",
                "table_name": "search",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/quotes/search/{term}",
                    "params": {
                        "term": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
