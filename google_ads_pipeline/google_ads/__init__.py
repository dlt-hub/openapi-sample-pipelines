from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_ads_source", max_table_nesting=2)
def google_ads_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Lists all accounts available to this user.
            {
                "name": "v2_accounts",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "accounts",
                    "path": "/v2/accounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all accounts directly managed by the given AdSense account.
            {
                "name": "v_2_parentlist_child_accounts",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "accounts",
                    "path": "/v2/{parent}:listChildAccounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the ad blocking recovery tag of an account.
            {
                "name": "v_2_ad_blocking_recovery_tag",
                "table_name": "ad_blocking_recovery_tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/{name}/adBlockingRecoveryTag",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the ad clients available in an account.
            {
                "name": "v2_adclients",
                "table_name": "ad_client",
                "endpoint": {
                    "data_selector": "adClients",
                    "path": "/v2/{parent}/adclients",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all ad units under a specified account and ad client.
            {
                "name": "v2_adunits",
                "table_name": "ad_unit",
                "endpoint": {
                    "data_selector": "adUnits",
                    "path": "/v2/{parent}/adunits",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the ad units available for a custom channel.
            {
                "name": "v_2_parentlist_linked_ad_units",
                "table_name": "ad_unit",
                "endpoint": {
                    "data_selector": "adUnits",
                    "path": "/v2/{parent}:listLinkedAdUnits",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the ad unit code for a given ad unit. For more information, see [About the AdSense code](https://support.google.com/adsense/answer/9274634) and [Where to place the ad code in your HTML](https://support.google.com/adsense/answer/9190028).
            {
                "name": "v2_adcode",
                "table_name": "ad_unit_ad_code",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/{name}/adcode",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the alerts available in an account.
            {
                "name": "v2_alerts",
                "table_name": "alert",
                "endpoint": {
                    "data_selector": "alerts",
                    "path": "/v2/{parent}/alerts",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "languageCode": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the custom channels available in an ad client.
            {
                "name": "v2_customchannels",
                "table_name": "custom_channel",
                "endpoint": {
                    "data_selector": "customChannels",
                    "path": "/v2/{parent}/customchannels",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the custom channels available for an ad unit.
            {
                "name": "v_2_parentlist_linked_custom_channels",
                "table_name": "custom_channel",
                "endpoint": {
                    "data_selector": "customChannels",
                    "path": "/v2/{parent}:listLinkedCustomChannels",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generates an ad hoc report.
            {
                "name": "v2_reportsgenerate",
                "table_name": "header",
                "endpoint": {
                    "data_selector": "headers",
                    "path": "/v2/{account}/reports:generate",
                    "params": {
                        "account": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "currencyCode": "OPTIONAL_CONFIG",
                        # "dateRange": "OPTIONAL_CONFIG",
                        # "dimensions": "OPTIONAL_CONFIG",
                        # "endDate.day": "OPTIONAL_CONFIG",
                        # "endDate.month": "OPTIONAL_CONFIG",
                        # "endDate.year": "OPTIONAL_CONFIG",
                        # "filters": "OPTIONAL_CONFIG",
                        # "languageCode": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "metrics": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "reportingTimeZone": "OPTIONAL_CONFIG",
                        # "startDate.day": "OPTIONAL_CONFIG",
                        # "startDate.month": "OPTIONAL_CONFIG",
                        # "startDate.year": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generates a saved report.
            {
                "name": "v2_savedgenerate",
                "table_name": "header",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "headers",
                    "path": "/v2/{name}/saved:generate",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "currencyCode": "OPTIONAL_CONFIG",
                        # "dateRange": "OPTIONAL_CONFIG",
                        # "endDate.day": "OPTIONAL_CONFIG",
                        # "endDate.month": "OPTIONAL_CONFIG",
                        # "endDate.year": "OPTIONAL_CONFIG",
                        # "languageCode": "OPTIONAL_CONFIG",
                        # "reportingTimeZone": "OPTIONAL_CONFIG",
                        # "startDate.day": "OPTIONAL_CONFIG",
                        # "startDate.month": "OPTIONAL_CONFIG",
                        # "startDate.year": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the payments available for an account.
            {
                "name": "v2_payments",
                "table_name": "payment",
                "endpoint": {
                    "data_selector": "payments",
                    "path": "/v2/{parent}/payments",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generates a csv formatted ad hoc report.
            {
                "name": "v_2_reportsgenerate_csv",
                "table_name": "reportsgenerate_csv",
                "endpoint": {
                    "data_selector": "extensions",
                    "path": "/v2/{account}/reports:generateCsv",
                    "params": {
                        "account": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "currencyCode": "OPTIONAL_CONFIG",
                        # "dateRange": "OPTIONAL_CONFIG",
                        # "dimensions": "OPTIONAL_CONFIG",
                        # "endDate.day": "OPTIONAL_CONFIG",
                        # "endDate.month": "OPTIONAL_CONFIG",
                        # "endDate.year": "OPTIONAL_CONFIG",
                        # "filters": "OPTIONAL_CONFIG",
                        # "languageCode": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "metrics": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "reportingTimeZone": "OPTIONAL_CONFIG",
                        # "startDate.day": "OPTIONAL_CONFIG",
                        # "startDate.month": "OPTIONAL_CONFIG",
                        # "startDate.year": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the saved report from the given resource name.
            {
                "name": "v2_saved",
                "table_name": "saved_report",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/{name}/saved",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists saved reports.
            {
                "name": "v2_reports_saved",
                "table_name": "saved_report",
                "endpoint": {
                    "data_selector": "savedReports",
                    "path": "/v2/{parent}/reports/saved",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generates a csv formatted saved report.
            {
                "name": "v_2_savedgenerate_csv",
                "table_name": "savedgenerate_csv",
                "endpoint": {
                    "data_selector": "extensions",
                    "path": "/v2/{name}/saved:generateCsv",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "currencyCode": "OPTIONAL_CONFIG",
                        # "dateRange": "OPTIONAL_CONFIG",
                        # "endDate.day": "OPTIONAL_CONFIG",
                        # "endDate.month": "OPTIONAL_CONFIG",
                        # "endDate.year": "OPTIONAL_CONFIG",
                        # "languageCode": "OPTIONAL_CONFIG",
                        # "reportingTimeZone": "OPTIONAL_CONFIG",
                        # "startDate.day": "OPTIONAL_CONFIG",
                        # "startDate.month": "OPTIONAL_CONFIG",
                        # "startDate.year": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets information about the selected site.
            {
                "name": "v2",
                "table_name": "site",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all the sites available in an account.
            {
                "name": "v2_sites",
                "table_name": "site",
                "endpoint": {
                    "data_selector": "sites",
                    "path": "/v2/{parent}/sites",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists active url channels.
            {
                "name": "v2_urlchannels",
                "table_name": "url_channel",
                "endpoint": {
                    "data_selector": "urlChannels",
                    "path": "/v2/{parent}/urlchannels",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
