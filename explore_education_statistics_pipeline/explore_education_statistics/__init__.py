from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="explore_education_statistics_source", max_table_nesting=2)
def explore_education_statistics_source(
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
            # Get a data set version's list of changes.
            {
                "name": "get_data_set_version_changes",
                "table_name": "change_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "changes",
                    "path": "/api/v1/data-sets/{dataSetId}/versions/{dataSetVersion}/changes",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "dataSetVersion": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List a data set's versions. Only provides summary information of each version.
            {
                "name": "list_data_set_versions",
                "table_name": "data_set_version_view_model",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/data-sets/{dataSetId}/versions",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "10",
                    },
                },
            },
            # Get a data set version, including a full list of its changes.
            {
                "name": "get_data_set_version",
                "table_name": "data_set_version_view_model",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/data-sets/{dataSetId}/versions/{dataSetVersion}",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "dataSetVersion": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists summary details of all the data sets related to a publication.
            {
                "name": "list_publication_data_sets",
                "table_name": "data_set_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/publications/{publicationId}/data-sets",
                    "params": {
                        "publicationId": {
                            "type": "resolve",
                            "resource": "list_publications",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "pageSize": "10",
                    },
                },
            },
            # Gets a specific data set's summary details.
            {
                "name": "get_data_set",
                "table_name": "data_set_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/data-sets/{dataSetId}",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get the entire data set in a specified file format.
            {
                "name": "get_data_set_file",
                "table_name": "file",
                "endpoint": {
                    "path": "/api/v1/data-sets/{dataSetId}/file",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the metadata about a data set. Use this to create data set queries.
            {
                "name": "get_data_set_meta",
                "table_name": "filter_meta_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "filters",
                    "path": "/api/v1/data-sets/{dataSetId}/meta",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the filter metadata about a data set. Use this to create data set queries.
            {
                "name": "get_data_set_meta_filters",
                "table_name": "filter_meta_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "filters",
                    "path": "/api/v1/data-sets/{dataSetId}/meta/filters",
                    "params": {
                        "dataSetId": {
                            "type": "resolve",
                            "resource": "get_data_set_meta",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Query a data set using a `GET` request, returning the filtered results.  Note that there is a `POST` variant of this endpoint which provides a more complete set of querying functionality. The `GET` variant is only recommended for initial exploratory  testing or simple queries that do not need advanced functionality.  Unlike the `POST` variant, this endpoint does not allow condition clauses (`and`, `or`, `not`) and consequently cannot express more complex queries.
            {
                "name": "query_data_set_get",
                "table_name": "footnote_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "footnotes",
                    "path": "/api/v1/data-sets/{dataSetId}/query",
                    "params": {
                        "dataSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "indicators": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                        # "filters": "OPTIONAL_CONFIG",
                        # "geographicLevels": "OPTIONAL_CONFIG",
                        # "locations": "OPTIONAL_CONFIG",
                        # "timePeriods": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "debug": "false",
                        # "pageSize": "1000",
                    },
                },
            },
            # Get the geographic metadata about a data set. Use this to create data set queries.
            {
                "name": "get_data_set_meta_geographic",
                "table_name": "geographic_level",
                "endpoint": {
                    "data_selector": "geographicLevels",
                    "path": "/api/v1/data-sets/{dataSetId}/meta/geographic",
                    "params": {
                        "dataSetId": {
                            "type": "resolve",
                            "resource": "get_data_set_meta",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the indicator metadata about a data set. Use this to create data set queries.
            {
                "name": "get_data_set_meta_indicators",
                "table_name": "indicator_meta_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "indicators",
                    "path": "/api/v1/data-sets/{dataSetId}/meta/indicators",
                    "params": {
                        "dataSetId": {
                            "type": "resolve",
                            "resource": "get_data_set_meta",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists details about publications with data available for querying.
            {
                "name": "list_publications",
                "table_name": "publication_summary_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/publications",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "search": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a specific publication's details.
            {
                "name": "get_publication",
                "table_name": "publication_summary_view_model",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/publications/{publicationId}",
                    "params": {
                        "publicationId": {
                            "type": "resolve",
                            "resource": "list_publications",
                            "field": "id",
                        },
                    },
                },
            },
            # Get the time period metadata about a data set. Use this to create data set queries.
            {
                "name": "get_data_set_meta_time_periods",
                "table_name": "time_period_meta_view_model",
                "endpoint": {
                    "data_selector": "timePeriods",
                    "path": "/api/v1/data-sets/{dataSetId}/meta/time-periods",
                    "params": {
                        "dataSetId": {
                            "type": "resolve",
                            "resource": "get_data_set_meta",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "dataSetVersion": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
