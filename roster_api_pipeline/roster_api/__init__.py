from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="roster_api_source", max_table_nesting=2)
def roster_api_source(
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
            "location": "header"

            },
        },
        "resources": 
        [
        # Gets a contact's information by contactId, email or phone.
              
 <b>Header requires</b>: "Authorization Bearer {accessToken}"
        {
            "name": "contact",
            "table_name": "legacy_api_contact_response_app_response",
            "endpoint": {
                "data_selector": "$",
                "path": "/contact",
                "params": {
                    # the parameters below can optionally be configured
                    # "ContactId": "OPTIONAL_CONFIG",
                    # "Email": "OPTIONAL_CONFIG",
                    # "Phone": "OPTIONAL_CONFIG",

                },
                "paginator": "auto",
            }
        },
        # Gets the delayed processing results of a previous request that exceeded the wait limit.
 When a request in the API exceeds the wait limit, a RequestId will be provided in the API response.
 This RequestId can be used here to retrieve the json response of the associated endpoint that was called previously where processing exceeded the wait limit.
 This endpoint is typically only needed when using this API for real-time social data collection when a new contact is added to the system.
 
 <b>Header requires</b>: "Authorization Bearer {accessToken}"
 
 <b>Response Statuses</b>:
 
 - <b>COMPLETED</b>: request completed successfully<br />
 - <b>NEW</b>: request created<br />
 - <b>IN_PROGRESS</b>: request is being processed. Try again in a few seconds.<br />
 - <b>PROCESSING_LIMIT_EXCEEDED</b>: processing took too long and was terminated.<br />
 - <b>ERROR</b>: error occurred during processing<br />
        {
            "name": "get_request",
            "table_name": "legacy_api_contact_response_app_response",
            "endpoint": {
                "data_selector": "$",
                "path": "/get-request",
                "params": {
                    # the parameters below can optionally be configured
                    # "requestId": "OPTIONAL_CONFIG",

                },
                "paginator": "auto",
            }
        },
        # Returns a list of active programs.
             
 <b>Header requires</b>: "Authorization Bearer {accessToken}"
        {
            "name": "program",
            "table_name": "legacy_client_api_user_program",
            "primary_key": "id",
            "write_disposition": "merge",
            "endpoint": {
                "data_selector": "result",
                "path": "/program",
                "paginator": "auto",
            }
        },
        ]
    }

    return rest_api_source(source_config)
