from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="docugenerate_source", max_table_nesting=2)
def docugenerate_source(
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
                "name": "Authorization",
                "location": "header",
            },
        },
        "resources": [
            # Get all the documents generated from template `template_id`.<br><br> The `template_id` needs to be passed as a query parameter.<br><br> Results are ordered by the `created` time in descending order.
            {
                "name": "query_documents",
                "table_name": "document",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/document",
                    "params": {
                        "template_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get a document by `id`.
            {
                "name": "get_document",
                "table_name": "document",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/document/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "query_documents",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get all the templates ordered by the `created` time in descending order.
            {
                "name": "query_templates",
                "table_name": "template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/template",
                    "paginator": "auto",
                },
            },
            # Get a template by `id`.
            {
                "name": "get_template",
                "table_name": "template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/template/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "query_templates",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
