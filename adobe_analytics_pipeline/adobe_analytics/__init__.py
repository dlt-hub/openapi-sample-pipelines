from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="adobe_analytics_source", max_table_nesting=2)
def adobe_analytics_source(
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
            # A calculated metric response will always include these default items: *id, name, description, rsid, owner, polarity, precision, type*  Other attributes can be optionally requested through the 'expansion' field:  * *modified*: Date that the metric was last modified (ISO 8601) * *definition*: Calculated metric definition as JSON object * *compatibility*: Products that the metric is compatible with * *reportSuiteName*: Also return the friendly Report Suite name for the RSID * *tags*: Gives all existing tags associated with the calculated metric  For more information about calculated metrics go [here](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/calculatedmetrics.md)
            {
                "name": "find_calculated_metrics",
                "table_name": "analytics_calculated_metric",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/calculatedmetrics",
                    "params": {
                        # the parameters below can optionally be configured
                        # "rsids": "OPTIONAL_CONFIG",
                        # "ownerId": "OPTIONAL_CONFIG",
                        # "calculatedMetricFilter": "OPTIONAL_CONFIG",
                        # "locale": "en_US",
                        # "name": "OPTIONAL_CONFIG",
                        # "tagNames": "OPTIONAL_CONFIG",
                        # "limit": "10",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # A calculated metric response will always include these default items: *id, name, description, rsid, owner, polarity, precision, type*  Other attributes can be optionally requested through the 'expansion' field:  * *modified*: Date that the metric was last modified (ISO 8601) * *definition*: Calculated metric definition as JSON object * *compatibility*: Products that the metric is compatible with * *reportSuiteName*: Also return the friendly Report Suite name for the RSID * *tags*: Gives all existing tags associated with the calculated metric  For more information about calculated metrics go [here](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/calculatedmetrics.md)
            {
                "name": "find_one_calculated_metric",
                "table_name": "analytics_calculated_metric",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/calculatedmetrics/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_calculated_metrics",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_date_range",
                "table_name": "analytics_date_range",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/dateranges/{dateRangeId}",
                    "params": {
                        "dateRangeId": {
                            "type": "resolve",
                            "resource": "get_date_ranges",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "dimensions_get_dimensions",
                "table_name": "analytics_dimension",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/dimensions",
                    "params": {
                        "rsid": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "segmentable": "OPTIONAL_CONFIG",
                        # "reportable": "OPTIONAL_CONFIG",
                        # "classifiable": "false",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "dimensions_get_dimension",
                "table_name": "analytics_dimension",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/dimensions/{dimensionId}",
                    "params": {
                        "dimensionId": {
                            "type": "resolve",
                            "resource": "dimensions_get_dimensions",
                            "field": "id",
                        },
                        "rsid": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_metric",
                "table_name": "analytics_metric",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/metrics/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "rsid": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "segments_get_segment",
                "table_name": "analytics_segment_response_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/segments/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "segments_get_segments",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all users for the company designated by the auth token.
            {
                "name": "find_all_users",
                "table_name": "analytics_user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "10",
                    },
                },
            },
            {
                "name": "get_current_user",
                "table_name": "analytics_user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/me",
                },
            },
            # This returns the metrics list primarily for the Analytics product. The platform identity API Returns a list of all possible metrics for the supported systems.
            {
                "name": "get_metrics",
                "table_name": "metric",
                "endpoint": {
                    "data_selector": "support",
                    "path": "/metrics",
                    "params": {
                        "rsid": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "segmentable": "false",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns all report suite types in a single collection.
            {
                "name": "get_collections",
                "table_name": "suite_collection_item",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/collections/suites",
                    "params": {
                        # the parameters below can optionally be configured
                        # "rsids": "OPTIONAL_CONFIG",
                        # "rsidContains": "OPTIONAL_CONFIG",
                        # "limit": "10",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns all report suite types in a single collection.
            {
                "name": "find_one",
                "table_name": "suite_collection_item",
                "primary_key": "rsid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/collections/suites/{rsid}",
                    "params": {
                        "rsid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This API allows users to store commonly used date ranges so that they can be reused throughout the product.
            {
                "name": "get_date_ranges",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/dateranges",
                    "params": {
                        # the parameters below can optionally be configured
                        # "locale": "en_US",
                        # "filterByIds": "OPTIONAL_CONFIG",
                        # "limit": "10",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "segments_get_segments",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/segments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "includeType": "OPTIONAL_CONFIG",
                        # "rsids": "OPTIONAL_CONFIG",
                        # "segmentFilter": "OPTIONAL_CONFIG",
                        # "locale": "en_US",
                        # "name": "OPTIONAL_CONFIG",
                        # "tagNames": "OPTIONAL_CONFIG",
                        # "limit": "10",
                        # "expansion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This API returns the usage and access logs for a given date range within a 3 month period. This API authenticates with an IMS user token.
            {
                "name": "get_usage_logs",
                "table_name": "usage_logs",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/auditlogs/usage",
                    "params": {
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "login": "OPTIONAL_CONFIG",
                        # "ip": "OPTIONAL_CONFIG",
                        # "rsid": "OPTIONAL_CONFIG",
                        # "eventType": "OPTIONAL_CONFIG",
                        # "event": "OPTIONAL_CONFIG",
                        # "limit": "10",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "[*].totalPages",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
