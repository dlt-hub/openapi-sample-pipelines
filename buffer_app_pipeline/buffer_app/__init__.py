from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="buffer_app_source", max_table_nesting=2)
def buffer_app_source(
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
            # Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.
            {
                "name": "configurationmedia_type_extension",
                "table_name": "configurationmedia_type_extension",
                "endpoint": {
                    "path": "/info/configuration{mediaTypeExtension}",
                },
            },
            # Returns the detailed information on individual interactions with the social media update such as favorites, retweets and likes.
            {
                "name": "interactionsmedia_type_extension",
                "table_name": "interactionsmedia_type_extension",
                "endpoint": {
                    "path": "/updates/{id}/interactions{mediaTypeExtension}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "event": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                    },
                },
            },
            # "Returns an array of updates that are currently in the buffer for an individual social media profile.
            {
                "name": "pendingmedia_type_extension",
                "table_name": "pendingmedia_type_extension",
                "endpoint": {
                    "path": "/profiles/{id}/updates/pending{mediaTypeExtension}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "utc": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns details of the single specified social media profile.
            {
                "name": "profile",
                "table_name": "profile",
                "endpoint": {
                    "path": "/profiles/{id}{mediaTypeExtension}",
                    "params": {
                        "id}{mediaTypeExtension": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns an array of social media profiles connected to a users account.
            {
                "name": "profilesmedia_type_extension",
                "table_name": "profilesmedia_type_extension",
                "endpoint": {
                    "path": "/profiles{mediaTypeExtension}",
                },
            },
            # Returns details of the posting schedules associated with a social media profile.
            {
                "name": "schedulesmedia_type_extension",
                "table_name": "schedulesmedia_type_extension",
                "endpoint": {
                    "path": "/profiles/{id}/schedules{mediaTypeExtension}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns an array of updates that have been sent from the buffer for an individual social media profile.
            {
                "name": "sentmedia_type_extension",
                "table_name": "sentmedia_type_extension",
                "endpoint": {
                    "path": "/profiles/{id}/updates/sent{mediaTypeExtension}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "utc": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns an object with a the numbers of shares a link has had using Buffer.
            {
                "name": "sharesmedia_type_extension",
                "table_name": "sharesmedia_type_extension",
                "endpoint": {
                    "path": "/links/shares{mediaTypeExtension}",
                    "params": {
                        "url": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Returns a single social media update.
            {
                "name": "update",
                "table_name": "update",
                "endpoint": {
                    "path": "/updates/{id}{mediaTypeExtension}",
                    "params": {
                        "id}{mediaTypeExtension": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a single user.
            {
                "name": "usermedia_type_extension",
                "table_name": "usermedia_type_extension",
                "endpoint": {
                    "path": "/user{mediaTypeExtension}",
                },
            },
        ],
    }

    return rest_api_source(source_config)
