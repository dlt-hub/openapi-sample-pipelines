from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="vimeo_source", max_table_nesting=2)
def vimeo_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # This method returns a full specification for the Vimeo API.
            {
                "name": "get_endpoints",
                "table_name": "",
                "endpoint": {
                    "data_selector": "methods",
                    "path": "/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "openapi": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the videos in the authenticated user's feed.
            {
                "name": "get_feed_alt1",
                "table_name": "activity_3_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/feed",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "per_page",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # This method returns all the videos in the authenticated user's feed.
            {
                "name": "get_feed",
                "table_name": "activity_3_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/feed",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "per_page",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # This method gets all the albums from the specified user's account.
            {
                "name": "get_albums_alt1",
                "table_name": "album",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/albums",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single album.
            {
                "name": "get_album_alt1",
                "table_name": "album",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/albums/{album_id}",
                    "params": {
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the albums from the specified user's account.
            {
                "name": "get_albums",
                "table_name": "album",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single album.
            {
                "name": "get_album",
                "table_name": "album",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_available_video_albums",
                "table_name": "album",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/available_albums",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all existing categories.
            {
                "name": "get_categories",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/categories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single category.
            {
                "name": "get_category",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/categories/{category}",
                    "params": {
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the categories in the specified channel.
            {
                "name": "get_channel_categories",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/categories",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the categories to which a particular user has subscribed.
            {
                "name": "get_category_subscriptions_alt1",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/categories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a particular user is subscribed to the specified category.
            {
                "name": "check_if_user_subscribed_to_category_alt1",
                "table_name": "category",
                "endpoint": {
                    "path": "/me/categories/{category}",
                    "params": {
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the categories to which a particular user has subscribed.
            {
                "name": "get_category_subscriptions",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/categories",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a particular user is subscribed to the specified category.
            {
                "name": "check_if_user_subscribed_to_category",
                "table_name": "category",
                "endpoint": {
                    "path": "/users/{user_id}/categories/{category}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the categories that contain a particular video.
            {
                "name": "get_video_categories",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/categories",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the channels that belong to a category.
            {
                "name": "get_category_channels",
                "table_name": "channel",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/categories/{category}/channels",
                    "params": {
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all existing channels.
            {
                "name": "get_channels",
                "table_name": "channel",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single channel.
            {
                "name": "get_channel",
                "table_name": "channel",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the channels to which the specified user subscribes.
            {
                "name": "get_channel_subscriptions_alt1",
                "table_name": "channel",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/channels",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a specific user is a follower of the channel in question.
            {
                "name": "check_if_user_subscribed_to_channel_alt1",
                "table_name": "channel",
                "endpoint": {
                    "path": "/me/channels/{channel_id}",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the channels to which the specified user subscribes.
            {
                "name": "get_channel_subscriptions",
                "table_name": "channel",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/channels",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a specific user is a follower of the channel in question.
            {
                "name": "check_if_user_subscribed_to_channel",
                "table_name": "channel",
                "endpoint": {
                    "path": "/users/{user_id}/channels/{channel_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_available_video_channels",
                "table_name": "channel",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/available_channels",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the comments on the specified video.
            {
                "name": "get_comments_alt1",
                "table_name": "comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}/comments",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the comments on the specified video.
            {
                "name": "get_comments",
                "table_name": "comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/comments",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns the specified comment on a video.
            {
                "name": "get_comment",
                "table_name": "comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/comments/{comment_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the replies to the specified video comment.
            {
                "name": "get_comment_replies",
                "table_name": "comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/comments/{comment_id}/replies",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all available content ratings.
            {
                "name": "get_content_ratings",
                "table_name": "content_rating",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/contentratings",
                },
            },
            # This method returns all available Creative Commons licenses.
            {
                "name": "get_cc_licenses",
                "table_name": "creative_commons",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/creativecommons",
                },
            },
            # This method returns all the credited users in a video.
            {
                "name": "get_video_credits_alt1",
                "table_name": "credit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}/credits",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the credited users in a video.
            {
                "name": "get_video_credits",
                "table_name": "credit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/credits",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single credited user in a video.
            {
                "name": "get_video_credit",
                "table_name": "credit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/credits/{credit_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "credit_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the domains on the specified video's whitelist.
            {
                "name": "get_video_privacy_domains",
                "table_name": "domain",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/privacy/domains",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether the authenticated user is a follower of the user in question.
            {
                "name": "check_if_user_is_following_alt1",
                "table_name": "following",
                "endpoint": {
                    "path": "/me/following/{follow_user_id}",
                    "params": {
                        "follow_user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method determines whether the authenticated user is a follower of the user in question.
            {
                "name": "check_if_user_is_following",
                "table_name": "following",
                "endpoint": {
                    "path": "/users/{user_id}/following/{follow_user_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "follow_user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the groups that belong to a category.
            {
                "name": "get_category_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/categories/{category}/groups",
                    "params": {
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all groups.
            {
                "name": "get_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a specific group.
            {
                "name": "get_group",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{group_id}",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the groups to which a particular user belongs.
            {
                "name": "get_user_groups_alt1",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/groups",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a particular user belongs to the specified group.
            {
                "name": "check_if_user_joined_group_alt1",
                "table_name": "group",
                "endpoint": {
                    "path": "/me/groups/{group_id}",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the groups to which a particular user belongs.
            {
                "name": "get_user_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/groups",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a particular user belongs to the specified group.
            {
                "name": "check_if_user_joined_group",
                "table_name": "group",
                "endpoint": {
                    "path": "/users/{user_id}/groups/{group_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the video languages that Vimeo supports.
            {
                "name": "get_languages",
                "table_name": "language",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/languages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method checks if the specified user has liked a particular video.
            {
                "name": "check_if_user_liked_video_alt1",
                "table_name": "like",
                "endpoint": {
                    "path": "/me/likes/{video_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method checks if the specified user has liked a particular video.
            {
                "name": "check_if_user_liked_video",
                "table_name": "like",
                "endpoint": {
                    "path": "/users/{user_id}/likes/{video_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns the representation of the authenticated user.
            {
                "name": "get_user_alt1",
                "table_name": "me",
                "endpoint": {
                    "data_selector": "content_filter",
                    "path": "/me",
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_genres",
                "table_name": "on_demand_genre",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/genres",
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_genre",
                "table_name": "on_demand_genre",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/genres/{genre_id}",
                    "params": {
                        "genre_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_genres_by_ondemand_id",
                "table_name": "on_demand_genre",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/genres",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_genre_by_ondemand_id",
                "table_name": "on_demand_genre",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/genres/{genre_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "genre_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_user_vods_alt1",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/ondemand/pages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_purchases",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/ondemand/purchases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "check_if_vod_was_purchased_alt1",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/ondemand/purchases/{ondemand_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the On Demand pages that are in a specific genre.
            {
                "name": "get_genre_vods",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/genres/{genre_id}/pages",
                    "params": {
                        "genre_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Check whether a genre contains an On Demand page.
            {
                "name": "get_genre_vod",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/genres/{genre_id}/pages/{ondemand_id}",
                    "params": {
                        "genre_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_user_vods",
                "table_name": "on_demand_page",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/ondemand/pages",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_promotion",
                "table_name": "on_demand_promotion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/promotions/{promotion_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promotion_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the codes of a promotion on an On Demand page.
            {
                "name": "get_vod_promotion_codes",
                "table_name": "on_demand_promotion_code",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promotion_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_regions",
                "table_name": "on_demand_region",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/regions",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Checks whether an On Demand page belongs to a region.
            {
                "name": "get_vod_region",
                "table_name": "on_demand_region",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/regions/{country}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "country": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_regions",
                "table_name": "on_demand_region",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/regions",
                },
            },
            # Information about this method appears below.
            {
                "name": "get_region",
                "table_name": "on_demand_region",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/regions/{country}",
                    "params": {
                        "country": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_seasons",
                "table_name": "on_demand_season",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/seasons",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_season",
                "table_name": "on_demand_season",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/seasons/{season_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "season_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the thumbnail images of the specified video.
            {
                "name": "get_video_thumbnails_alt1",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}/pictures",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the custom logos that belong to the specified user.
            {
                "name": "get_custom_logos_alt1",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/customlogos",
                },
            },
            # This method returns a single custom logo belonging to the specified user.
            {
                "name": "get_custom_logo_alt1",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/customlogos/{logo_id}",
                    "params": {
                        "logo_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the portrait images belonging to the authenticated user.
            {
                "name": "get_pictures_alt1",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/pictures",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single portrait image belonging to the authenticated user.
            {
                "name": "get_picture_alt1",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/pictures/{portraitset_id}",
                    "params": {
                        "portraitset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_backgrounds",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/backgrounds",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_background",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/backgrounds/{background_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "background_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_posters",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/pictures",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_poster",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/pictures/{poster_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "poster_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the custom uploaded thumbnails from the specified album.
            {
                "name": "get_album_custom_thumbs",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}/custom_thumbnails",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the videos associated with the specified tag.
            {
                "name": "get_album_custom_thumbnail",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "thumbnail_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the custom logos from the specified album.
            {
                "name": "get_album_logos",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}/logos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single custom logo from the specified album.
            {
                "name": "get_album_logo",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}/logos/{logo_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "logo_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the custom logos that belong to the specified user.
            {
                "name": "get_custom_logos",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/customlogos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns a single custom logo belonging to the specified user.
            {
                "name": "get_custom_logo",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/customlogos/{logo_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "logo_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the portrait images belonging to the authenticated user.
            {
                "name": "get_pictures",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/pictures",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single portrait image belonging to the authenticated user.
            {
                "name": "get_picture",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/pictures/{portraitset_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "portraitset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the thumbnail images of the specified video.
            {
                "name": "get_video_thumbnails",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/pictures",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single thumbnail image from the specified video.
            {
                "name": "get_video_thumbnail",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/pictures/{picture_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "picture_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns a single timeline event thumbnail that belongs to the specified video.
            {
                "name": "get_video_custom_logo",
                "table_name": "picture",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/timelinethumbnails/{thumbnail_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "thumbnail_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the specified user's portfolios.
            {
                "name": "get_portfolios_alt1",
                "table_name": "portfolio",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/portfolios",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single portfolio from the specified user.
            {
                "name": "get_portfolio_alt1",
                "table_name": "portfolio",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/portfolios/{portfolio_id}",
                    "params": {
                        "portfolio_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the specified user's portfolios.
            {
                "name": "get_portfolios",
                "table_name": "portfolio",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/portfolios",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single portfolio from the specified user.
            {
                "name": "get_portfolio",
                "table_name": "portfolio",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/portfolios/{portfolio_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "portfolio_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method determines whether the specified video uses a particular embed preset.
            {
                "name": "get_video_embed_preset",
                "table_name": "preset",
                "endpoint": {
                    "path": "/videos/{video_id}/presets/{preset_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "preset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the embed presets that belong to the specified user.
            {
                "name": "get_embed_presets_alt1",
                "table_name": "presets",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/presets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single embed preset that belongs to the specified user.
            {
                "name": "get_embed_preset_alt1",
                "table_name": "presets",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/presets/{preset_id}",
                    "params": {
                        "preset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the embed presets that belong to the specified user.
            {
                "name": "get_embed_presets",
                "table_name": "presets",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/presets",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single embed preset that belongs to the specified user.
            {
                "name": "get_embed_preset",
                "table_name": "presets",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/presets/{preset_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "preset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the projects that belong to the specified user.
            {
                "name": "get_projects_alt1",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/projects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single project that belongs to the specified user.
            {
                "name": "get_project_alt1",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/projects/{project_id}",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the projects that belong to the specified user.
            {
                "name": "get_projects",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/projects",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single project that belongs to the specified user.
            {
                "name": "get_project",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/projects/{project_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_promotions",
                "table_name": "promotion",
                "endpoint": {
                    "data_selector": "metadata.connections.codes.options",
                    "path": "/ondemand/pages/{ondemand_id}/promotions",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "check_if_vod_was_purchased",
                "table_name": "purchase",
                "endpoint": {
                    "data_selector": "content_rating",
                    "path": "/users/{user_id}/ondemand/purchases",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the tags that have been added to the specified channel.
            {
                "name": "get_channel_tags",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/tags",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method determines whether a specific tag has been added to the channel in question.
            {
                "name": "check_if_channel_has_tag",
                "table_name": "tag",
                "endpoint": {
                    "path": "/channels/{channel_id}/tags/{word}",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "word": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets a specific tag from all available tags.
            {
                "name": "get_tag",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/tags/{word}",
                    "params": {
                        "word": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the tags associated with a video.
            {
                "name": "get_video_tags",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/tags",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method determines whether a particular tag has been added to a video.
            {
                "name": "check_video_for_tag",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/tags/{word}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "word": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the text tracks of the specified video.
            {
                "name": "get_text_tracks_alt1",
                "table_name": "text_track",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}/texttracks",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the text tracks of the specified video.
            {
                "name": "get_text_tracks",
                "table_name": "text_track",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/texttracks",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns a single text track from the specified video.
            {
                "name": "get_text_track",
                "table_name": "text_track",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/texttracks/{texttrack_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "texttrack_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method, in conjunction with our [Getting Started](https://developer.vimeo.com/api/guides/start) guide, can help you learn how to use the Vimeo API.
            {
                "name": "developer_tutorial",
                "table_name": "tutorial",
                "endpoint": {
                    "path": "/tutorial",
                },
            },
            # This method returns all the embed presets that belong to the specified user.
            {
                "name": "get_upload_attempt",
                "table_name": "upload_attempt",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/uploads/{upload_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "upload_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the moderators of the specified channel.
            {
                "name": "get_channel_moderators",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/moderators",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single moderator of the specified channel.
            {
                "name": "get_channel_moderator",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/moderators/{user_id}",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the users who have access to the specified private channel.
            {
                "name": "get_channel_privacy_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/privacy/users",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the followers of a specific channel.
            {
                "name": "get_channel_subscribers",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/users",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the users who have liked a particular video.
            {
                "name": "get_video_likes_alt1",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}/likes",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the users who have access to the specified private video.
            {
                "name": "get_video_privacy_users_alt1",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}/privacy/users",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the users that belong to the specified group.
            {
                "name": "get_group_members",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{group_id}/users",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the followers of the authenticated user.
            {
                "name": "get_followers_alt1",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/followers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all users that the authenticated user is following.
            {
                "name": "get_user_following_alt1",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/following",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the users who have liked a particular video on an On Demand page.
            {
                "name": "get_vod_likes",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/likes",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "search_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns the representation of the authenticated user.
            {
                "name": "get_user",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the followers of the authenticated user.
            {
                "name": "get_followers",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/followers",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all users that the authenticated user is following.
            {
                "name": "get_user_following",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/following",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the users who have liked a particular video.
            {
                "name": "get_video_likes",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/likes",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the users who have access to the specified private video.
            {
                "name": "get_video_privacy_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/privacy/users",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method verifies that an OAuth 2 token exists.
            {
                "name": "verify_token",
                "table_name": "verify",
                "endpoint": {
                    "data_selector": "user.content_filter",
                    "path": "/oauth/verify",
                },
            },
            # This method gets all the videos that belong to a category.
            {
                "name": "get_category_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/categories/{category}/videos",
                    "params": {
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single video from a category. Use it to determine whether the video belongs to the category.
            {
                "name": "check_category_for_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/categories/{category}/videos/{video_id}",
                    "params": {
                        "category": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the videos in a specific channel.
            {
                "name": "get_channel_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a specific video in a channel. You can use it to determine whether the video is in the channel.
            {
                "name": "get_channel_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/channels/{channel_id}/videos/{video_id}",
                    "params": {
                        "channel_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method removes a single video from the specified group.
            {
                "name": "get_group_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{group_id}/videos",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single video from a group. You can use this method to determine whether the video belongs to the group.
            {
                "name": "get_group_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{group_id}/videos/{video_id}",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the videos from the specified album.
            {
                "name": "get_album_videos_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/albums/{album_id}/videos",
                    "params": {
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "password": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "weak_search": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.
            {
                "name": "get_album_video_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/albums/{album_id}/videos/{video_id}",
                    "params": {
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "password": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the videos in which the authenticated user has a credited appearance.
            {
                "name": "get_appearances_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/appearances",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos that the specified user has liked.
            {
                "name": "get_likes_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/likes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos from the specified portfolio.
            {
                "name": "get_portfolio_videos_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/portfolios/{portfolio_id}/videos",
                    "params": {
                        "portfolio_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single video from the specified portfolio.
            {
                "name": "get_portfolio_video_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/portfolios/{portfolio_id}/videos/{video_id}",
                    "params": {
                        "portfolio_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the videos that make use of the specified embed preset.
            {
                "name": "get_embed_preset_videos_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/presets/{preset_id}/videos",
                    "params": {
                        "preset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos that belong to the specified project.
            {
                "name": "get_project_videos_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/projects/{project_id}/videos",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the videos that the authenticated user has uploaded.
            {
                "name": "get_videos_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/videos",
                    "params": {
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "filter_playable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a particular user is the owner of the specified video.
            {
                "name": "check_if_user_owns_video_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/videos/{video_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.  **NOTE:** This endpoint is deprecated. Any request to it returns empty data with HTTP status code 200.
            {
                "name": "get_watch_history",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/watched/videos",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos from the specified user's Watch Later queue.
            {
                "name": "get_watch_later_queue_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/watchlater",
                    "params": {
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method checks the specified user's Watch Later queue for a particular video.
            {
                "name": "check_watch_later_queue_alt1",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/me/watchlater/{video_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_season_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/seasons/{season_id}/videos",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "season_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/videos",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Information about this method appears below.
            {
                "name": "get_vod_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/ondemand/pages/{ondemand_id}/videos/{video_id}",
                    "params": {
                        "ondemand_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the videos associated with the specified tag.
            {
                "name": "get_videos_with_tag",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/tags/{word}/videos",
                    "params": {
                        "word": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos from the specified album.
            {
                "name": "get_album_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}/videos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "password": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "weak_search": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.
            {
                "name": "get_album_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/albums/{album_id}/videos/{video_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "album_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "password": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the videos in which the authenticated user has a credited appearance.
            {
                "name": "get_appearances",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/appearances",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos that the specified user has liked.
            {
                "name": "get_likes",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/likes",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos from the specified portfolio.
            {
                "name": "get_portfolio_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/portfolios/{portfolio_id}/videos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "portfolio_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets a single video from the specified portfolio.
            {
                "name": "get_portfolio_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "portfolio_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the videos that make use of the specified embed preset.
            {
                "name": "get_embed_preset_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/presets/{preset_id}/videos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "preset_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method gets all the videos that belong to the specified project.
            {
                "name": "get_project_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/projects/{project_id}/videos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns all the videos that the authenticated user has uploaded.
            {
                "name": "get_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/videos",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "containing_uri": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "filter_playable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method determines whether a particular user is the owner of the specified video.
            {
                "name": "check_if_user_owns_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/videos/{video_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method gets all the videos from the specified user's Watch Later queue.
            {
                "name": "get_watch_later_queue",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/watchlater",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "filter_embeddable": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method checks the specified user's Watch Later queue for a particular video.
            {
                "name": "check_watch_later_queue",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}/watchlater/{video_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the videos that match custom search criteria.
            {
                "name": "search_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "direction": "OPTIONAL_CONFIG",
                        # "filter": "OPTIONAL_CONFIG",
                        # "links": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "uris": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This method returns a single video.
            {
                "name": "get_video",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns all the related videos of a particular video.
            {
                "name": "get_related_videos",
                "table_name": "video",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/videos/{video_id}/videos",
                    "params": {
                        "video_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
