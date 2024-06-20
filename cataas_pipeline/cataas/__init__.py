from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="cataas_source", max_table_nesting=2)
def cataas_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
        },
        "resources": [
            # Browse cats
            {
                "name": "admincatsbrowse",
                "table_name": "cat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/cats",
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "skip",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # Get a random cat
            {
                "name": "catrandom",
                "table_name": "cat",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/cat",
                    "params": {
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "fit": "OPTIONAL_CONFIG",
                        # "position": "center",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                        # "blur": "OPTIONAL_CONFIG",
                        # "r": "OPTIONAL_CONFIG",
                        # "g": "OPTIONAL_CONFIG",
                        # "b": "OPTIONAL_CONFIG",
                        # "brightness": "OPTIONAL_CONFIG",
                        # "saturation": "OPTIONAL_CONFIG",
                        # "hue": "OPTIONAL_CONFIG",
                        # "lightness": "OPTIONAL_CONFIG",
                        # "html": "OPTIONAL_CONFIG",
                        # "json": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get cat by id
            {
                "name": "catget",
                "table_name": "cat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cat/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "fit": "OPTIONAL_CONFIG",
                        # "position": "center",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                        # "blur": "OPTIONAL_CONFIG",
                        # "r": "OPTIONAL_CONFIG",
                        # "g": "OPTIONAL_CONFIG",
                        # "b": "OPTIONAL_CONFIG",
                        # "brightness": "OPTIONAL_CONFIG",
                        # "saturation": "OPTIONAL_CONFIG",
                        # "hue": "OPTIONAL_CONFIG",
                        # "lightness": "OPTIONAL_CONFIG",
                        # "html": "OPTIONAL_CONFIG",
                        # "json": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get random cat by tag
            {
                "name": "catrandomtag",
                "table_name": "cat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cat/{tag}",
                    "params": {
                        "tag": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "fit": "OPTIONAL_CONFIG",
                        # "position": "center",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                        # "blur": "OPTIONAL_CONFIG",
                        # "r": "OPTIONAL_CONFIG",
                        # "g": "OPTIONAL_CONFIG",
                        # "b": "OPTIONAL_CONFIG",
                        # "brightness": "OPTIONAL_CONFIG",
                        # "saturation": "OPTIONAL_CONFIG",
                        # "hue": "OPTIONAL_CONFIG",
                        # "lightness": "OPTIONAL_CONFIG",
                        # "html": "OPTIONAL_CONFIG",
                        # "json": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Will return all cats
            {
                "name": "apicats",
                "table_name": "cat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/cats",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tags": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 10,
                        "offset_param": "skip",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # Count how many cat
            {
                "name": "apicount",
                "table_name": "count",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/count",
                    "paginator": "auto",
                },
            },
            # Get random cat saying text
            {
                "name": "catrandomtext",
                "table_name": "say",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cat/says/{text}",
                    "params": {
                        "text": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "font": "Impact",
                        # "fontSize": "30",
                        # "fontColor": "#000",
                        # "fontBackground": "none",
                        # "type": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "fit": "OPTIONAL_CONFIG",
                        # "position": "center",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                        # "blur": "OPTIONAL_CONFIG",
                        # "r": "OPTIONAL_CONFIG",
                        # "g": "OPTIONAL_CONFIG",
                        # "b": "OPTIONAL_CONFIG",
                        # "brightness": "OPTIONAL_CONFIG",
                        # "saturation": "OPTIONAL_CONFIG",
                        # "hue": "OPTIONAL_CONFIG",
                        # "lightness": "OPTIONAL_CONFIG",
                        # "html": "OPTIONAL_CONFIG",
                        # "json": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get cat by id saying text
            {
                "name": "catgettext",
                "table_name": "say",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cat/{id}/says/{text}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "text": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "font": "Impact",
                        # "fontSize": "30",
                        # "fontColor": "#000",
                        # "fontBackground": "none",
                        # "type": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "fit": "OPTIONAL_CONFIG",
                        # "position": "center",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                        # "blur": "OPTIONAL_CONFIG",
                        # "r": "OPTIONAL_CONFIG",
                        # "g": "OPTIONAL_CONFIG",
                        # "b": "OPTIONAL_CONFIG",
                        # "brightness": "OPTIONAL_CONFIG",
                        # "saturation": "OPTIONAL_CONFIG",
                        # "hue": "OPTIONAL_CONFIG",
                        # "lightness": "OPTIONAL_CONFIG",
                        # "html": "OPTIONAL_CONFIG",
                        # "json": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get random cat by tag saying text
            {
                "name": "catrandomtagtext",
                "table_name": "say",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/cat/{tag}/says/{text}",
                    "params": {
                        "tag": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "text": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "font": "Impact",
                        # "fontSize": "30",
                        # "fontColor": "#000",
                        # "fontBackground": "none",
                        # "type": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "fit": "OPTIONAL_CONFIG",
                        # "position": "center",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                        # "blur": "OPTIONAL_CONFIG",
                        # "r": "OPTIONAL_CONFIG",
                        # "g": "OPTIONAL_CONFIG",
                        # "b": "OPTIONAL_CONFIG",
                        # "brightness": "OPTIONAL_CONFIG",
                        # "saturation": "OPTIONAL_CONFIG",
                        # "hue": "OPTIONAL_CONFIG",
                        # "lightness": "OPTIONAL_CONFIG",
                        # "html": "OPTIONAL_CONFIG",
                        # "json": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Will return all tags
            {
                "name": "apitags",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/tags",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
