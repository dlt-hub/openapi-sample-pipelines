from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_adsense_host_source", max_table_nesting=2)
def google_adsense_host_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # List hosted accounts associated with this AdSense account by ad client id.
            {
                "name": "adsensehost_accounts_list",
                "table_name": "account",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/accounts",
                    "params": {
                        "filterAdClientId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about the selected associated AdSense account.
            {
                "name": "adsensehost_accounts_get",
                "table_name": "account",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/accounts/{accountId}",
                    "params": {
                        "accountId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List all hosted ad clients in the specified hosted account.
            {
                "name": "adsensehost_accounts_adclients_list",
                "table_name": "ad_client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/accounts/{accountId}/adclients",
                    "params": {
                        "accountId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about one of the ad clients in the specified publisher's AdSense account.
            {
                "name": "adsensehost_accounts_adclients_get",
                "table_name": "ad_client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/accounts/{accountId}/adclients/{adClientId}",
                    "params": {
                        "adClientId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_adclients_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List all host ad clients in this AdSense account.
            {
                "name": "adsensehost_adclients_list",
                "table_name": "ad_client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/adclients",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about one of the ad clients in the Host AdSense account.
            {
                "name": "adsensehost_adclients_get",
                "table_name": "ad_client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/adclients/{adClientId}",
                    "params": {
                        "adClientId": {
                            "type": "resolve",
                            "resource": "adsensehost_adclients_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get ad code for the specified ad unit, attaching the specified host custom channels.
            {
                "name": "adsensehost_accounts_adunits_get_ad_code",
                "table_name": "ad_code",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}/adcode",
                    "params": {
                        "adUnitId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_adunits_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "adClientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "hostCustomChannelId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List all ad units in the specified publisher's AdSense account.
            {
                "name": "adsensehost_accounts_adunits_list",
                "table_name": "ad_unit",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/accounts/{accountId}/adclients/{adClientId}/adunits",
                    "params": {
                        "adClientId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_adclients_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "includeInactive": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the specified host ad unit in this AdSense account.
            {
                "name": "adsensehost_accounts_adunits_get",
                "table_name": "ad_unit",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}",
                    "params": {
                        "adUnitId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_adunits_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "adClientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List all host custom channels in this AdSense account.
            {
                "name": "adsensehost_customchannels_list",
                "table_name": "custom_channel",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/adclients/{adClientId}/customchannels",
                    "params": {
                        "adClientId": {
                            "type": "resolve",
                            "resource": "adsensehost_adclients_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a specific custom channel from the host AdSense account.
            {
                "name": "adsensehost_customchannels_get",
                "table_name": "custom_channel",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/adclients/{adClientId}/customchannels/{customChannelId}",
                    "params": {
                        "customChannelId": {
                            "type": "resolve",
                            "resource": "adsensehost_customchannels_list",
                            "field": "id",
                        },
                        "adClientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.
            {
                "name": "adsensehost_accounts_reports_generate",
                "table_name": "report",
                "endpoint": {
                    "data_selector": "averages",
                    "path": "/accounts/{accountId}/reports",
                    "params": {
                        "accountId": {
                            "type": "resolve",
                            "resource": "adsensehost_accounts_list",
                            "field": "id",
                        },
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "dimension": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "locale": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "metric": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "startIndex": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.
            {
                "name": "adsensehost_reports_generate",
                "table_name": "report",
                "endpoint": {
                    "data_selector": "averages",
                    "path": "/reports",
                    "params": {
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "dimension": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "locale": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "metric": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "startIndex": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Create an association session for initiating an association with an AdSense user.
            {
                "name": "adsensehost_associationsessions_start",
                "table_name": "start",
                "endpoint": {
                    "data_selector": "productCodes",
                    "path": "/associationsessions/start",
                    "params": {
                        "productCode": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "websiteUrl": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "callbackUrl": "OPTIONAL_CONFIG",
                        # "userLocale": "OPTIONAL_CONFIG",
                        # "websiteLocale": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List all host URL channels in the host AdSense account.
            {
                "name": "adsensehost_urlchannels_list",
                "table_name": "url_channel",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/adclients/{adClientId}/urlchannels",
                    "params": {
                        "adClientId": {
                            "type": "resolve",
                            "resource": "adsensehost_adclients_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Verify an association session after the association callback returns from AdSense signup.
            {
                "name": "adsensehost_associationsessions_verify",
                "table_name": "verify",
                "endpoint": {
                    "data_selector": "productCodes",
                    "path": "/associationsessions/verify",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
