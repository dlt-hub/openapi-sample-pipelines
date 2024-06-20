from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="visible_thread_source", max_table_nesting=2)
def visible_thread_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Get your list of dictionaries
            {
                "name": "get_dictionaries",
                "table_name": "dictionary",
                "endpoint": {
                    "path": "/dictionaries",
                    "paginator": "auto",
                },
            },
            # Get your list of documents
            {
                "name": "get_documents",
                "table_name": "document",
                "endpoint": {
                    "path": "/documents",
                    "paginator": "auto",
                },
            },
            # Get data from a previously submitted document identified by ***docId***
            {
                "name": "get_doc_by_id",
                "table_name": "document",
                "endpoint": {
                    "path": "/documents/{docId}",
                    "params": {
                        "docId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get your list of searches
            {
                "name": "get_searches",
                "table_name": "search",
                "endpoint": {
                    "path": "/searches",
                    "paginator": "auto",
                },
            },
            # Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** & **urlId**
            {
                "name": "get_search_results",
                "table_name": "search",
                "endpoint": {
                    "path": "/searches/{docId}/{dictionaryId}",
                    "params": {
                        "docId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "dictionaryId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "matchingOnly": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** & **urlId**
            {
                "name": "get_scan_url_by_id",
                "table_name": "web_url",
                "endpoint": {
                    "path": "/webscans/{scanId}/webUrls/{urlId}",
                    "params": {
                        "scanId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "urlId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get your list of scans
            {
                "name": "get_webscans",
                "table_name": "webscan",
                "endpoint": {
                    "path": "/webscans",
                    "paginator": "auto",
                },
            },
            # Get data from a previously run scan, identified by **scanId**
            {
                "name": "get_scan_by_id",
                "table_name": "webscan",
                "endpoint": {
                    "path": "/webscans/{scanId}",
                    "params": {
                        "scanId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
