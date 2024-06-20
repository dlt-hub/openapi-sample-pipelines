from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="meowfacts_source", max_table_nesting=2)
def meowfacts_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # By passing in the appropriate options, you can recieve a specific or more than one fact.
            {
                "name": "fact",
                "table_name": "fact",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "factID": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # The health check endpoint will return a status of 200 if the api is up and ready to recieve connections. It will tell the uptime, and total requests served since last restart. It also has a field for version which corresponds to the versioned release from the github repo.
            {
                "name": "healthcheck_data",
                "table_name": "healthcheck_data",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/health",
                    "paginator": "auto",
                },
            },
            # This endpoint will list all languages available to the root endpoint.
            {
                "name": "options_object",
                "table_name": "options_object",
                "endpoint": {
                    "data_selector": "lang",
                    "path": "/options",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
