from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_search_console_source", max_table_nesting=2)
def google_search_console_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            #  Lists the user's Search Console sites.
            {
                "name": "webmasters_sites_list",
                "table_name": "wmx_site",
                "endpoint": {
                    "data_selector": "siteEntry",
                    "path": "/webmasters/v3/sites",
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
                    },
                    "paginator": "auto",
                },
            },
            #  Retrieves information about specific site.
            {
                "name": "webmasters_sites_get",
                "table_name": "wmx_site",
                "primary_key": "siteUrl",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/webmasters/v3/sites/{siteUrl}",
                    "params": {
                        "siteUrl": {
                            "type": "resolve",
                            "resource": "webmasters_sites_list",
                            "field": "siteUrl",
                        },
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
            #  Lists the [sitemaps-entries](/webmaster-tools/v3/sitemaps) submitted for this site, or included in the sitemap index file (if `sitemapIndex` is specified in the request).
            {
                "name": "webmasters_sitemaps_list",
                "table_name": "wmx_sitemap",
                "endpoint": {
                    "data_selector": "sitemap",
                    "path": "/webmasters/v3/sites/{siteUrl}/sitemaps",
                    "params": {
                        "siteUrl": {
                            "type": "resolve",
                            "resource": "webmasters_sites_list",
                            "field": "siteUrl",
                        },
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
                        # "sitemapIndex": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves information about a specific sitemap.
            {
                "name": "webmasters_sitemaps_get",
                "table_name": "wmx_sitemap",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/webmasters/v3/sites/{siteUrl}/sitemaps/{feedpath}",
                    "params": {
                        "siteUrl": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "feedpath": "FILL_ME_IN",  # TODO: fill in required path parameter
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
        ],
    }

    return rest_api_source(source_config)
