from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="aviation_api_source", max_table_nesting=2)
def aviation_api_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Search for AFD by ICAO or FAA identifier
            {
                "name": "afd",
                "table_name": "afd",
                "endpoint": {
                    "path": "/charts/afd",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search for an airport by its ICAO or FAA identifier
            {
                "name": "airport",
                "table_name": "airport",
                "endpoint": {
                    "path": "/airports",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search for charts by ICAO or FAA identifier or chart name
            {
                "name": "change",
                "table_name": "change",
                "endpoint": {
                    "path": "/charts/changes",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "chart_name": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for charts by ICAO or FAA identifier with optional grouping
            {
                "name": "chart",
                "table_name": "chart",
                "endpoint": {
                    "path": "/charts",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "group": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for all the at a specified facility on VATSIM
            {
                "name": "controller",
                "table_name": "controller",
                "endpoint": {
                    "path": "/vatsim/controllers",
                    "params": {
                        "fac": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search for an airport's METAR
            {
                "name": "metar",
                "table_name": "metar",
                "endpoint": {
                    "path": "/weather/metar",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search for all the arrivals and/or departures into an airport on VATSIM
            {
                "name": "pilot",
                "table_name": "pilot",
                "endpoint": {
                    "path": "/vatsim/pilots",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "dep": "OPTIONAL_CONFIG",
                        # "arr": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all of the preferred routes with no search parameters
            {
                "name": "preferred_route",
                "table_name": "preferred_route",
                "endpoint": {
                    "path": "/preferred-routes",
                    "paginator": "auto",
                },
            },
            # Search for preferred routes by various parameters. At least one search criteria is required, although a combination of any can be used
            {
                "name": "search",
                "table_name": "search",
                "endpoint": {
                    "path": "/preferred-routes/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "origin": "OPTIONAL_CONFIG",
                        # "dest": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "lower_alt": "OPTIONAL_CONFIG",
                        # "upper_alt": "OPTIONAL_CONFIG",
                        # "aircraft": "OPTIONAL_CONFIG",
                        # "d_artcc": "OPTIONAL_CONFIG",
                        # "a_artcc": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for an airport's TAF
            {
                "name": "taf",
                "table_name": "taf",
                "endpoint": {
                    "path": "/weather/taf",
                    "params": {
                        "apt": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
