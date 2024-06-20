from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="french_transport_data_paris_source", max_table_nesting=2)
def french_transport_data_paris_source(
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
                "name": "apikey",
                "location": "query",
            },
            "paginator": {
                "type": "offset",
                "limit": 100,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            # Returns a list of all available attachments for a dataset.
            {
                "name": "get_dataset_attachments",
                "table_name": "attachment",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/attachments",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Export a catalog in CSV (Comma Separated Values). Specific parameters are described here
            {
                "name": "export_catalog_csv",
                "table_name": "csv",
                "endpoint": {
                    "path": "/catalog/exports/csv",
                    "params": {
                        # the parameters below can optionally be configured
                        # "delimiter": ";",
                        # "list_separator": ",",
                        # "quote_all": "OPTIONAL_CONFIG",
                        # "with_bom": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Export a dataset in CSV (Comma Separated Values). Specific parameters are described here
            {
                "name": "export_records_csv",
                "table_name": "csv",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/exports/csv",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "delimiter": ";",
                        # "list_separator": ",",
                        # "quote_all": "OPTIONAL_CONFIG",
                        # "with_bom": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve available datasets.
            {
                "name": "get_datasets",
                "table_name": "dataset",
                "endpoint": {
                    "path": "/catalog/datasets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "select": "OPTIONAL_CONFIG",
                        # "where": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                        # "refine": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                },
            },
            # Returns a list of available endpoints for the specified dataset, with metadata and endpoints.  The response includes the following links: * the attachments endpoint * the files endpoint * the records endpoint * the catalog endpoint.
            {
                "name": "get_dataset",
                "table_name": "dataset_v2_0",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/catalog/datasets/{dataset_id}",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "select": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                },
            },
            # List available export formats
            {
                "name": "list_export_formats",
                "table_name": "export",
                "endpoint": {
                    "path": "/catalog/exports",
                },
            },
            # Export a catalog in the desired format.
            {
                "name": "export_datasets",
                "table_name": "export",
                "endpoint": {
                    "path": "/catalog/exports/{format}",
                    "params": {
                        "format": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "where": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                        # "refine": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": -1,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # List available export formats
            {
                "name": "list_dataset_export_formats",
                "table_name": "export",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/exports",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Export a dataset in the desired format. **Note:** The `group_by` parameter is only available on exports starting with the v2.1
            {
                "name": "export_records",
                "table_name": "export",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/exports/{format}",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "format": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "select": "OPTIONAL_CONFIG",
                        # "where": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                        # "limit": "-1",
                        # "refine": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                        # "use_labels": "OPTIONAL_CONFIG",
                        # "epsg": "4326",
                    },
                },
            },
            # Enumerate facet values for datasets and returns a list of values for each facet. Can be used to implement guided navigation in large result sets.
            {
                "name": "get_datasets_facets",
                "table_name": "facet",
                "endpoint": {
                    "path": "/catalog/facets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "facet": "OPTIONAL_CONFIG",
                        # "refine": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "where": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                },
            },
            # Enumerates facet values for records and returns a list of values for each facet. Can be used to implement guided navigation in large result sets.
            {
                "name": "get_records_facets",
                "table_name": "facet",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/facets",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "where": "OPTIONAL_CONFIG",
                        # "refine": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "facet": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                },
            },
            # Export a dataset in GPX. Specific parameters are described here
            {
                "name": "export_records_gpx",
                "table_name": "gpx",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/exports/gpx",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "name_field": "OPTIONAL_CONFIG",
                        # "description_field_list": "OPTIONAL_CONFIG",
                        # "use_extension": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Perform a query on dataset records.
            {
                "name": "get_records",
                "table_name": "record",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/records",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "select": "OPTIONAL_CONFIG",
                        # "where": "OPTIONAL_CONFIG",
                        # "group_by": "OPTIONAL_CONFIG",
                        # "order_by": "OPTIONAL_CONFIG",
                        # "refine": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                },
            },
            # Reads a single dataset record based on its identifier.
            {
                "name": "get_record",
                "table_name": "record",
                "endpoint": {
                    "path": "/catalog/datasets/{dataset_id}/records/{record_id}",
                    "params": {
                        "dataset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "record_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "select": "OPTIONAL_CONFIG",
                        # "lang": "OPTIONAL_CONFIG",
                        # "timezone": "UTC",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
