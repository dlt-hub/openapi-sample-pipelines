from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="shipstation_source", max_table_nesting=2)
def shipstation_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "question",
                "table_name": "question",
                "endpoint": {
                    "path": "/questions",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
