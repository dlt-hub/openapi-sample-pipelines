from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_analytics_source", max_table_nesting=2)
def google_analytics_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Lists all accounts to which the user has access.
            {
                "name": "analytics_management_accounts_list",
                "table_name": "account",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists account summaries (lightweight tree comprised of accounts/properties/profiles) to which the user has access.
            {
                "name": "analytics_management_account_summaries_list",
                "table_name": "account_summary",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accountSummaries",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all columns for a report type
            {
                "name": "analytics_metadata_columns_list",
                "table_name": "column",
                "endpoint": {
                    "data_selector": "attributeNames",
                    "path": "/metadata/{reportType}/columns",
                    "params": {
                        "reportType": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # List custom data sources to which the user has access.
            {
                "name": "analytics_management_custom_data_sources_list",
                "table_name": "custom_data_source",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists custom dimensions to which the user has access.
            {
                "name": "analytics_management_custom_dimensions_list",
                "table_name": "custom_dimension",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a custom dimension to which the user has access.
            {
                "name": "analytics_management_custom_dimensions_get",
                "table_name": "custom_dimension",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}",
                    "params": {
                        "customDimensionId": {
                            "type": "resolve",
                            "resource": "analytics_management_custom_dimensions_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists custom metrics to which the user has access.
            {
                "name": "analytics_management_custom_metrics_list",
                "table_name": "custom_metric",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a custom metric to which the user has access.
            {
                "name": "analytics_management_custom_metrics_get",
                "table_name": "custom_metric",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}",
                    "params": {
                        "customMetricId": {
                            "type": "resolve",
                            "resource": "analytics_management_custom_metrics_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists webProperty-Google Ads links for a given web property.
            {
                "name": "analytics_management_web_property_ad_words_links_list",
                "table_name": "entity_ad_words_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a web property-Google Ads link to which the user has access.
            {
                "name": "analytics_management_web_property_ad_words_links_get",
                "table_name": "entity_ad_words_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}",
                    "params": {
                        "webPropertyAdWordsLinkId": {
                            "type": "resolve",
                            "resource": "analytics_management_web_property_ad_words_links_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists account-user links for a given account.
            {
                "name": "analytics_management_account_user_links_list",
                "table_name": "entity_user_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/entityUserLinks",
                    "params": {
                        "accountId": {
                            "type": "resolve",
                            "resource": "analytics_management_accounts_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists webProperty-user links for a given web property.
            {
                "name": "analytics_management_webproperty_user_links_list",
                "table_name": "entity_user_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/entityUserLinks",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists profile-user links for a given view (profile).
            {
                "name": "analytics_management_profile_user_links_list",
                "table_name": "entity_user_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks",
                    "params": {
                        "profileId": {
                            "type": "resolve",
                            "resource": "analytics_management_profiles_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists experiments to which the user has access.
            {
                "name": "analytics_management_experiments_list",
                "table_name": "experiment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments",
                    "params": {
                        "profileId": {
                            "type": "resolve",
                            "resource": "analytics_management_profiles_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns an experiment to which the user has access.
            {
                "name": "analytics_management_experiments_get",
                "table_name": "experiment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}",
                    "params": {
                        "experimentId": {
                            "type": "resolve",
                            "resource": "analytics_management_experiments_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "profileId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists all filters for an account
            {
                "name": "analytics_management_filters_list",
                "table_name": "filter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/filters",
                    "params": {
                        "accountId": {
                            "type": "resolve",
                            "resource": "analytics_management_accounts_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns filters to which the user has access.
            {
                "name": "analytics_management_filters_get",
                "table_name": "filter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/filters/{filterId}",
                    "params": {
                        "filterId": {
                            "type": "resolve",
                            "resource": "analytics_management_filters_list",
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
            # Returns Analytics data for a view (profile).
            {
                "name": "analytics_data_ga_get",
                "table_name": "ga",
                "endpoint": {
                    "data_selector": "columnHeaders",
                    "path": "/data/ga",
                    "params": {
                        "ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start-date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end-date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "metrics": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "dimensions": "OPTIONAL_CONFIG",
                        # "filters": "OPTIONAL_CONFIG",
                        # "include-empty-rows": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "output": "OPTIONAL_CONFIG",
                        # "samplingLevel": "OPTIONAL_CONFIG",
                        # "segment": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists goals to which the user has access.
            {
                "name": "analytics_management_goals_list",
                "table_name": "goal",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals",
                    "params": {
                        "profileId": {
                            "type": "resolve",
                            "resource": "analytics_management_profiles_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a goal to which the user has access.
            {
                "name": "analytics_management_goals_get",
                "table_name": "goal",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}",
                    "params": {
                        "goalId": {
                            "type": "resolve",
                            "resource": "analytics_management_goals_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "profileId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Returns Analytics Multi-Channel Funnels data for a view (profile).
            {
                "name": "analytics_data_mcf_get",
                "table_name": "mcf",
                "endpoint": {
                    "data_selector": "columnHeaders",
                    "path": "/data/mcf",
                    "params": {
                        "ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start-date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end-date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "metrics": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "dimensions": "OPTIONAL_CONFIG",
                        # "filters": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "samplingLevel": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists views (profiles) to which the user has access.
            {
                "name": "analytics_management_profiles_list",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a view (profile) to which the user has access.
            {
                "name": "analytics_management_profiles_get",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}",
                    "params": {
                        "profileId": {
                            "type": "resolve",
                            "resource": "analytics_management_profiles_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists all profile filter links for a profile.
            {
                "name": "analytics_management_profile_filter_links_list",
                "table_name": "profile_filter_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks",
                    "params": {
                        "profileId": {
                            "type": "resolve",
                            "resource": "analytics_management_profiles_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single profile filter link.
            {
                "name": "analytics_management_profile_filter_links_get",
                "table_name": "profile_filter_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}",
                    "params": {
                        "linkId": {
                            "type": "resolve",
                            "resource": "analytics_management_profile_filter_links_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "profileId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Returns real time data for a view (profile).
            {
                "name": "analytics_data_realtime_get",
                "table_name": "realtime",
                "endpoint": {
                    "data_selector": "columnHeaders",
                    "path": "/data/realtime",
                    "params": {
                        "ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "metrics": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "dimensions": "OPTIONAL_CONFIG",
                        # "filters": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists remarketing audiences to which the user has access.
            {
                "name": "analytics_management_remarketing_audience_list",
                "table_name": "remarketing_audience",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a remarketing audience to which the user has access.
            {
                "name": "analytics_management_remarketing_audience_get",
                "table_name": "remarketing_audience",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}",
                    "params": {
                        "remarketingAudienceId": {
                            "type": "resolve",
                            "resource": "analytics_management_remarketing_audience_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists segments to which the user has access.
            {
                "name": "analytics_management_segments_list",
                "table_name": "segment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/segments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists unsampled reports to which the user has access.
            {
                "name": "analytics_management_unsampled_reports_list",
                "table_name": "unsampled_report",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports",
                    "params": {
                        "profileId": {
                            "type": "resolve",
                            "resource": "analytics_management_profiles_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single unsampled report.
            {
                "name": "analytics_management_unsampled_reports_get",
                "table_name": "unsampled_report",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports/{unsampledReportId}",
                    "params": {
                        "unsampledReportId": {
                            "type": "resolve",
                            "resource": "analytics_management_unsampled_reports_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "profileId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # List uploads to which the user has access.
            {
                "name": "analytics_management_uploads_list",
                "table_name": "upload",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads",
                    "params": {
                        "customDataSourceId": {
                            "type": "resolve",
                            "resource": "analytics_management_custom_data_sources_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List uploads to which the user has access.
            {
                "name": "analytics_management_uploads_get",
                "table_name": "upload",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads/{uploadId}",
                    "params": {
                        "uploadId": {
                            "type": "resolve",
                            "resource": "analytics_management_uploads_list",
                            "field": "id",
                        },
                        "accountId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webPropertyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "customDataSourceId": "FILL_ME_IN",  # TODO: fill in required path parameter
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
            # Lists web properties to which the user has access.
            {
                "name": "analytics_management_webproperties_list",
                "table_name": "webproperty",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/management/accounts/{accountId}/webproperties",
                    "params": {
                        "accountId": {
                            "type": "resolve",
                            "resource": "analytics_management_accounts_list",
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
                        # "max-results": "OPTIONAL_CONFIG",
                        # "start-index": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a web property to which the user has access.
            {
                "name": "analytics_management_webproperties_get",
                "table_name": "webproperty",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/management/accounts/{accountId}/webproperties/{webPropertyId}",
                    "params": {
                        "webPropertyId": {
                            "type": "resolve",
                            "resource": "analytics_management_webproperties_list",
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
        ],
    }

    return rest_api_source(source_config)
