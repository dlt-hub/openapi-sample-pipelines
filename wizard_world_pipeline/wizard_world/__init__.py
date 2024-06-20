from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="wizard_world_source", max_table_nesting=2)
def wizard_world_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "get_elixirs",
                "table_name": "elixir_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Elixirs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "Name": "OPTIONAL_CONFIG",
                        # "Difficulty": "OPTIONAL_CONFIG",
                        # "Ingredient": "OPTIONAL_CONFIG",
                        # "InventorFullName": "OPTIONAL_CONFIG",
                        # "Manufacturer": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_elixirsid",
                "table_name": "elixir_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Elixirs/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_elixirs",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_houses",
                "table_name": "house_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Houses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_housesid",
                "table_name": "house_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Houses/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_houses",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_ingredients",
                "table_name": "ingredient_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Ingredients",
                    "params": {
                        # the parameters below can optionally be configured
                        # "Name": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_ingredientsid",
                "table_name": "ingredient_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Ingredients/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_ingredients",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_spells",
                "table_name": "spell_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Spells",
                    "params": {
                        # the parameters below can optionally be configured
                        # "Name": "OPTIONAL_CONFIG",
                        # "Type": "OPTIONAL_CONFIG",
                        # "Incantation": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_spellsid",
                "table_name": "spell_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Spells/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_spells",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_wizards",
                "table_name": "wizard_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Wizards",
                    "params": {
                        # the parameters below can optionally be configured
                        # "FirstName": "OPTIONAL_CONFIG",
                        # "LastName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_wizardsid",
                "table_name": "wizard_dto",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/Wizards/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_wizards",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
