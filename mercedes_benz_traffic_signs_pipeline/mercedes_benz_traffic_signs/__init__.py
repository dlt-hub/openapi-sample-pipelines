from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="mercedes_benz_traffic_signs_source", max_table_nesting=2)
def mercedes_benz_traffic_signs_source(
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
            # This endpoint returns the uuid of the GeoJSON object and the GeoJSON object itself that is predefined for the user. The object is used to restrict the area of data retrieval. The response does not incorporate any geolocation filters.
            {
                "name": "geojson",
                "table_name": "geojson",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/geojson",
                },
            },
            # This endpoint returns a set of traffic signs restricted to the predefined area of the user. The traffic signs data is returned in a paged response. If there are no traffic signs in the defined area, an empty list is returned. Note that missing fields in individual traffic sign data are returned as `null` values. To additionally limit the returned data, a bounding box can be defined as geolocation filter. The bounding box is defined by two points, each represented by a longitude and a latitude coordinate. The first point is defined by the longitudePoint1 and latitudePoint1 query parameters. The second point is defined by the longitudePoint2 and latitudePoint2 query parameters. All four query parameters are optional, but if one of them is provided, all four must be provided to define a bounding box as geolocation filter.
            {
                "name": "trafficsign",
                "table_name": "trafficsign",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/trafficsigns",
                    "params": {
                        # the parameters below can optionally be configured
                        # "size": "OPTIONAL_CONFIG",
                        # "longitudePoint1": "OPTIONAL_CONFIG",
                        # "latitudePoint1": "OPTIONAL_CONFIG",
                        # "longitudePoint2": "OPTIONAL_CONFIG",
                        # "latitudePoint2": "OPTIONAL_CONFIG",
                        # "lonelySign": "OPTIONAL_CONFIG",
                        # "minConfidence": "OPTIONAL_CONFIG",
                        # "permanency": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
