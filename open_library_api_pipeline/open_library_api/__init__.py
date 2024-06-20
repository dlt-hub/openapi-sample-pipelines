from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="open_library_api_source", max_table_nesting=2)
def open_library_api_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            {
                "name": "authors",
                "table_name": "author",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/authors/{olid}.json",
                    "params": {
                        "olid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "search_authors",
                "table_name": "author",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/search/authors.json",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "api_books",
                "table_name": "book",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/books",
                    "params": {
                        "bibkeys": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "format": "json",
                        # "callback": "OPTIONAL_CONFIG",
                        # "jscmd": "viewapi",
                    },
                },
            },
            {
                "name": "books",
                "table_name": "book",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/books/{olid}",
                    "params": {
                        "olid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "api_volumes_brief",
                "table_name": "brief",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/volumes/brief/{key_type}/{value}.json",
                    "params": {
                        "key_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "value": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "callback": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "covers",
                "table_name": "cover",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/covers/{key_type}/{value}-{size}.jpg",
                    "params": {
                        "key_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "value}-{size": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "isbn",
                "table_name": "isbn",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/isbn/{isbn}",
                    "params": {
                        "isbn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "search",
                "table_name": "search",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/search.json",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "subjects",
                "table_name": "subject",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/subjects/{subject}.json",
                    "params": {
                        "subject": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "details": "false",
                    },
                },
            },
            {
                "name": "authors_works",
                "table_name": "work",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/authors/{olid}/works.json",
                    "params": {
                        "olid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "works",
                "table_name": "work",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/works/{olid}",
                    "params": {
                        "olid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
