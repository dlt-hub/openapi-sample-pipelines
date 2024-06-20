from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="refuge_restrooms_source", max_table_nesting=2)
def refuge_restrooms_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "offset",
                "limit": 20,
                "offset_param": "offset",
                "limit_param": "per_page",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            # Search for restroom records updated or created on or after a given date
            {
                "name": "by_date",
                "table_name": "by_date",
                "endpoint": {
                    "path": "/v1/restrooms/by_date",
                    "params": {
                        "day": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "month": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "year": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "page": "OPTIONAL_CONFIG",
                        # "ada": "OPTIONAL_CONFIG",
                        # "unisex": "OPTIONAL_CONFIG",
                        # "updated": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Search by location.
            {
                "name": "by_location",
                "table_name": "by_location",
                "endpoint": {
                    "path": "/v1/restrooms/by_location",
                    "params": {
                        "lat": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "lng": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "page": "OPTIONAL_CONFIG",
                        # "ada": "OPTIONAL_CONFIG",
                        # "unisex": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all restroom records ordered by date descending.
            {
                "name": "restroom",
                "table_name": "restroom",
                "endpoint": {
                    "path": "/v1/restrooms",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page": "OPTIONAL_CONFIG",
                        # "ada": "OPTIONAL_CONFIG",
                        # "unisex": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Perform full-text search of restroom records.
            {
                "name": "search",
                "table_name": "search",
                "endpoint": {
                    "path": "/v1/restrooms/search",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "page": "OPTIONAL_CONFIG",
                        # "ada": "OPTIONAL_CONFIG",
                        # "unisex": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
