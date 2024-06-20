from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="qualtrics_source", max_table_nesting=2)
def qualtrics_source(
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
                "name": "X-API-TOKEN",
                "location": "header",
            },
        },
        "resources": [
            # Gets all distributions for a given survey
            {
                "name": "distribution",
                "table_name": "distribution",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result.elements",
                    "path": "/distributions",
                    "params": {
                        "surveyId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get event subscriptions
            {
                "name": "event_subscriptions_response",
                "table_name": "event_subscriptions_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/eventsubscriptions/{SubscriptionId}",
                    "params": {
                        "SubscriptionId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves all the individual links for a given distribution
            {
                "name": "link",
                "table_name": "link",
                "endpoint": {
                    "data_selector": "result.elements",
                    "path": "/distributions/{DistributionId}/links",
                    "params": {
                        "DistributionId": {
                            "type": "resolve",
                            "resource": "distribution",
                            "field": "id",
                        },
                        "surveyId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Gets a single Qualtrics survey speficied by its ID
            {
                "name": "survey_response",
                "table_name": "survey_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/survey-definitions/{SurveyId}",
                    "params": {
                        "SurveyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
