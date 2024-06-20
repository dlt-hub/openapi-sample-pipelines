from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="nvidia_cuopt_amr_server_source", max_table_nesting=2)
def nvidia_cuopt_amr_server_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # To ping if server is running
            {
                "name": "health",
                "table_name": "health",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cuopt/health",
                    "paginator": "auto",
                },
            },
            # To check liveness of the server
            {
                "name": "live",
                "table_name": "live",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/health/live",
                    "paginator": "auto",
                },
            },
            # To check readiness of the server
            {
                "name": "ready",
                "table_name": "ready",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/health/ready",
                    "paginator": "auto",
                },
            },
            # Note: This is for self hosted. Query a previously submitted request which timed out. The 'id' is the uuid returned when the original request timed out.
            {
                "name": "response_routes_result_cuopt_routes_id_get",
                "table_name": "response_routes_result_cuopt_routes_id_get",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cuopt/routes/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
