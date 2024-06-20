from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="game_of_thrones_source", max_table_nesting=2)
def game_of_thrones_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # GET api/characters
            {
                "name": "get_apiv_2_characters",
                "table_name": "character_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v2/Characters",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_apiv_2_charactersid",
                "table_name": "character_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v2/Characters/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_apiv_2_characters",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # GET: api/Continents
            {
                "name": "get_apiv_2_continents",
                "table_name": "continent_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v2/Continents",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_apiv_2_continentsid",
                "table_name": "continent_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v2/Continents/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_apiv_2_continents",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
