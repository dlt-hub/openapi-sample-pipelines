from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="messagebird_source", max_table_nesting=2)
def messagebird_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Lists datasets containing intents and corresponding phrases. You can choose to list only your own datasets, as well as template datasets, or both. Template datasets are used as examples and can be found under the `Templates` tab in the [dataset overview of the dashboard](https://dashboard.messagebird.com/knowledge-base/list). You can clone such datasets to kickstart the creation of a dataset that is tailored to your use-case.   Note that the results are paginated and so you might need to iteratively call this endpoint to obtain all your datasets.
            {
                "name": "intent_list_datasets",
                "table_name": "dataset",
                "endpoint": {
                    "path": "/api/v1/datasets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "listMode": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the dataset for the given dataset ID. It only displays the metadata corresponding to the dataset. If you want to view the individual intent phrases that you have added, you can use the [dataset section of the dashboard](https://dashboard.messagebird.com/knowledge-base/list).
            {
                "name": "intent_get_dataset",
                "table_name": "dataset",
                "endpoint": {
                    "path": "/api/v1/datasets/{datasetId}",
                    "params": {
                        "datasetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists the languages supported by the Intent API.
            {
                "name": "intent_list_supported_languages",
                "table_name": "supported_language",
                "endpoint": {
                    "path": "/api/v1/supported-languages",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
