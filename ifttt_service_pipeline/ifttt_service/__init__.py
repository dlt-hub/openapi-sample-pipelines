from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="ifttt_service_source", max_table_nesting=2)
def ifttt_service_source(
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
                "name": "IFTTT-Service-Key",
                "location": "header",
            },
        },
        "resources": [
            {
                "name": "statu",
                "table_name": "statu",
                "endpoint": {
                    "path": "/ifttt/v1/status",
                    "paginator": "auto",
                },
            },
            {
                "name": "user_info",
                "table_name": "user_info",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/ifttt/v1/user/info",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
