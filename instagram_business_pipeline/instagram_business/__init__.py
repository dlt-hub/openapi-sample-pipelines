from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="instagram_business_source", max_table_nesting=2)
def instagram_business_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Get a list of recent comments on a media object.
            {
                "name": "media_comments",
                "table_name": "comment",
                "endpoint": {
                    "path": "/media/{media-id}/comments",
                    "params": {
                        "media-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # See the authenticated user's feed.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015
            {
                "name": "users_self_feed",
                "table_name": "feed",
                "endpoint": {
                    "path": "/users/self/feed",
                    "params": {
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "min_id": "OPTIONAL_CONFIG",
                        # "max_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the list of users this user follows. To get follows of the owner of the access token, you can use **self** instead of the `user-id`.
            {
                "name": "users_follows",
                "table_name": "follow",
                "endpoint": {
                    "path": "/users/{user-id}/follows",
                    "params": {
                        "user-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get the list of users this user is followed by. To get users followed by the owner of the access token, you can use **self** instead of the `user-id`.
            {
                "name": "users_followed_by",
                "table_name": "followed_by",
                "endpoint": {
                    "path": "/users/{user-id}/followed-by",
                    "params": {
                        "user-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of users who have liked this media.
            {
                "name": "media_likes",
                "table_name": "like",
                "endpoint": {
                    "path": "/media/{media-id}/likes",
                    "params": {
                        "media-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # See the list of media liked by the authenticated user. Private media is returned as long as the authenticated user has permission to view that media. Liked media lists are only available for the currently authenticated user.
            {
                "name": "users_self_media_liked",
                "table_name": "liked",
                "endpoint": {
                    "path": "/users/self/media/liked",
                    "params": {
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "max_like_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a location.
            {
                "name": "locations",
                "table_name": "location",
                "endpoint": {
                    "path": "/locations/{location-id}",
                    "params": {
                        "location-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a media object. The returned type key will allow you to differentiate between image and video media.  **Note:** if you authenticate with an OAuth Token, you will receive the user_has_liked key which quickly tells you whether the current user has liked this media item.
            {
                "name": "media",
                "table_name": "medium",
                "endpoint": {
                    "path": "/media/{media-id}",
                    "params": {
                        "media-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of what media is most popular at the moment. Can return mix of `image` and `video` types.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015
            {
                "name": "media_popular",
                "table_name": "popular",
                "endpoint": {
                    "path": "/media/popular",
                    "paginator": "auto",
                },
            },
            # Get recent media from a geography subscription that you created.  **Note:** You can only access Geographies that were explicitly created by your OAuth client. Check the Geography Subscriptions section of the [real-time updates page](https://instagram.com/developer/realtime/). When you create a subscription to some geography that you define, you will be returned a unique `geo-id` that can be used in this query. To backfill photos from the location covered by this geography, use the [media search endpoint](https://instagram.com/developer/endpoints/media/).  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015
            {
                "name": "geographies_media_recent",
                "table_name": "recent",
                "endpoint": {
                    "path": "/geographies/{geo-id}/media/recent",
                    "params": {
                        "geo-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "min_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of recent media objects from a given location.
            {
                "name": "locations_media_recent",
                "table_name": "recent",
                "endpoint": {
                    "path": "/locations/{location-id}/media/recent",
                    "params": {
                        "location-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "min_timestamp": "OPTIONAL_CONFIG",
                        # "max_timestamp": "OPTIONAL_CONFIG",
                        # "min_id": "OPTIONAL_CONFIG",
                        # "max_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of recently tagged media. Use the `max_tag_id` and `min_tag_id` parameters in the pagination response to paginate through these objects.
            {
                "name": "tags_media_recent",
                "table_name": "recent",
                "endpoint": {
                    "path": "/tags/{tag-name}/media/recent",
                    "params": {
                        "tag-name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "min_tag_id": "OPTIONAL_CONFIG",
                        # "max_tag_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the most recent media published by a user. To get the most recent media published by the owner of the access token, you can use **self** instead of the `user-id`.  Security scope `public_content` is required to read information about other users.
            {
                "name": "users_media_recent",
                "table_name": "recent",
                "endpoint": {
                    "path": "/users/{user-id}/media/recent",
                    "params": {
                        "user-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "max_timestamp": "OPTIONAL_CONFIG",
                        # "min_timestamp": "OPTIONAL_CONFIG",
                        # "min_id": "OPTIONAL_CONFIG",
                        # "max_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a relationship to another user.
            {
                "name": "users_relationship",
                "table_name": "relationship",
                "endpoint": {
                    "path": "/users/{user-id}/relationship",
                    "params": {
                        "user-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the users who have requested this user's permission to follow.
            {
                "name": "users_self_requested_by",
                "table_name": "requested_by",
                "endpoint": {
                    "path": "/users/self/requested-by",
                    "paginator": "auto",
                },
            },
            # Search for a location by geographic coordinate.
            {
                "name": "locations_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/locations/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "distance": "OPTIONAL_CONFIG",
                        # "facebook_places_id": "OPTIONAL_CONFIG",
                        # "foursquare_id": "OPTIONAL_CONFIG",
                        # "lat": "OPTIONAL_CONFIG",
                        # "lng": "OPTIONAL_CONFIG",
                        # "foursquare_v2_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for media in a given area. The default time span is set to 5 days. The time span must not exceed 7 days. Defaults time stamps cover the last 5 days. Can return mix of `image` and `video` types.
            {
                "name": "media_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/media/search",
                    "params": {
                        "lat": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "lng": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "min_timestamp": "OPTIONAL_CONFIG",
                        # "max_timestamp": "OPTIONAL_CONFIG",
                        # "distance": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for tags by name.
            {
                "name": "tags_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/tags/search",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search for a user by name.
            {
                "name": "users_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/users/search",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint returns the same response as `GET /media/{media-id}`.  A media object's shortcode can be found in its shortlink URL. An example shortlink is `http://instagram.com/p/D/`, its corresponding shortcode is `D`.
            {
                "name": "media_shortcode",
                "table_name": "shortcode",
                "endpoint": {
                    "path": "/media/shortcode/{shortcode}",
                    "params": {
                        "shortcode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a tag object.
            {
                "name": "tags",
                "table_name": "tag",
                "endpoint": {
                    "path": "/tags/{tag-name}",
                    "params": {
                        "tag-name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get basic information about a user. To get information about the owner of the access token, you can use **self** instead of the `user-id`.  Security scope `public_content` is required to read information about other users.
            {
                "name": "users",
                "table_name": "user",
                "endpoint": {
                    "path": "/users/{user-id}",
                    "params": {
                        "user-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
