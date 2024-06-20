from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="soundcloud_source", max_table_nesting=2)
def soundcloud_source(
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
                "name": "Authorization",
                "location": "header",
            },
            "paginator": {
                "type": "offset",
                "limit": 200,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            {
                "name": "get_meactivities",
                "table_name": "activity",
                "endpoint": {
                    "path": "/me/activities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_trackstrack_idcomments",
                "table_name": "comment",
                "endpoint": {
                    "path": "/tracks/{track_id}/comments",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_usersuser_idcomments",
                "table_name": "comment",
                "endpoint": {
                    "path": "/users/{user_id}/comments",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # <h3>Security Advice</h3> * Using the [implicit OAuth authorization flow](https://tools.ietf.org/html/draft-ietf-oauth-security-topics-16#section-2.1.2) (`response_type=token`)  is **not recommended**. It can suffer from access token leakage and access token replay attacks. Use `response_type=code` instead. * Use the `state` parameter for [CSRF protection](https://tools.ietf.org/html/draft-ietf-oauth-security-topics-16#section-4.7). Pass a sufficient  random nonce here and verify this nonce again after retrieving the token.
            {
                "name": "get_connect",
                "table_name": "connect",
                "endpoint": {
                    "path": "/connect",
                    "params": {
                        "client_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "redirect_uri": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "response_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "scope": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_meconnections",
                "table_name": "connection",
                "endpoint": {
                    "path": "/me/connections",
                },
            },
            {
                "name": "get_meconnectionsconnection_id",
                "table_name": "connection",
                "endpoint": {
                    "path": "/me/connections/{connection_id}",
                    "params": {
                        "connection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_usersuser_idfavorites",
                "table_name": "favorite",
                "endpoint": {
                    "path": "/users/{user_id}/favorites",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "50",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_trackstrack_idfavoriters",
                "table_name": "favoriter",
                "endpoint": {
                    "path": "/tracks/{track_id}/favoriters",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_mefollowers",
                "table_name": "follower",
                "endpoint": {
                    "path": "/me/followers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_mefollowersfollower_id",
                "table_name": "follower",
                "endpoint": {
                    "path": "/me/followers/{follower_id}",
                    "params": {
                        "follower_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of users that follows (user_id).
            {
                "name": "get_usersuser_idfollowers",
                "table_name": "follower",
                "endpoint": {
                    "path": "/users/{user_id}/followers",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_mefollowings",
                "table_name": "following",
                "endpoint": {
                    "path": "/me/followings",
                },
            },
            {
                "name": "get_mefollowingsuser_id",
                "table_name": "following",
                "endpoint": {
                    "path": "/me/followings/{user_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns list of users that (user_id) follows.
            {
                "name": "get_usersuser_idfollowings",
                "table_name": "following",
                "endpoint": {
                    "path": "/users/{user_id}/followings",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            # Returns (following_id) that is followed by (user_id).
            {
                "name": "get_usersuser_idfollowingsfollowing_id",
                "table_name": "following",
                "endpoint": {
                    "path": "/users/{user_id}/followings/{following_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "following_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_mefavoritesids",
                "table_name": "id",
                "endpoint": {
                    "path": "/me/favorites/ids",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_me",
                "table_name": "me",
                "endpoint": {
                    "path": "/me",
                },
            },
            {
                "name": "get_meactivitiesallown",
                "table_name": "own",
                "endpoint": {
                    "path": "/me/activities/all/own",
                    "params": {
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "limit": "50",
                    },
                },
            },
            # Returns playlist info, playlist tracks and tracks owner info.
            {
                "name": "get_meplaylists",
                "table_name": "playlist",
                "endpoint": {
                    "path": "/me/playlists",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_meplaylistsplaylist_id",
                "table_name": "playlist",
                "endpoint": {
                    "path": "/me/playlists/{playlist_id}",
                    "params": {
                        "playlist_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_playlists",
                "table_name": "playlist",
                "endpoint": {
                    "path": "/playlists",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_playlistsplaylist_id",
                "table_name": "playlist",
                "endpoint": {
                    "path": "/playlists/{playlist_id}",
                    "params": {
                        "playlist_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "secret_token": "OPTIONAL_CONFIG",
                        # "access": "playable,preview",
                    },
                },
            },
            {
                "name": "get_usersuser_idplaylists",
                "table_name": "playlist",
                "endpoint": {
                    "path": "/users/{user_id}/playlists",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "limit": "50",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_trackstrack_idrelated",
                "table_name": "related",
                "endpoint": {
                    "path": "/tracks/{track_id}/related",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_playlistsplaylist_idreposters",
                "table_name": "reposter",
                "endpoint": {
                    "path": "/playlists/{playlist_id}/reposters",
                    "params": {
                        "playlist_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_trackstrack_idreposters",
                "table_name": "reposter",
                "endpoint": {
                    "path": "/tracks/{track_id}/reposters",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_resolve",
                "table_name": "resolve",
                "endpoint": {
                    "path": "/resolve",
                    "params": {
                        "url": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_trackstrack_idstreams",
                "table_name": "stream",
                "endpoint": {
                    "path": "/tracks/{track_id}/streams",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "secret_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_meactivitiestracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/me/activities/tracks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_mefollowingstracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/me/followings/tracks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                    },
                },
            },
            {
                "name": "get_melikestracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/me/likes/tracks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "50",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_metracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/me/tracks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "50",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_metrackstrack_id",
                "table_name": "track",
                "endpoint": {
                    "path": "/me/tracks/{track_id}",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_playlistsplaylist_idtracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/playlists/{playlist_id}/tracks",
                    "params": {
                        "playlist_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "secret_token": "OPTIONAL_CONFIG",
                        # "access": "playable,preview",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_tracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/tracks",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "ids": "OPTIONAL_CONFIG",
                        # "genres": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "bpm": "OPTIONAL_CONFIG",
                        # "duration": "OPTIONAL_CONFIG",
                        # "created_at": "OPTIONAL_CONFIG",
                        # "access": "playable,preview",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_trackstrack_id",
                "table_name": "track",
                "endpoint": {
                    "path": "/tracks/{track_id}",
                    "params": {
                        "track_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "secret_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_usersuser_idlikestracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/users/{user_id}/likes/tracks",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "limit": "50",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_usersuser_idtracks",
                "table_name": "track",
                "endpoint": {
                    "path": "/users/{user_id}/tracks",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "access": "playable,preview",
                        # "limit": "50",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_users",
                "table_name": "user",
                "endpoint": {
                    "path": "/users",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "ids": "OPTIONAL_CONFIG",
                        # "linked_partitioning": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_usersuser_id",
                "table_name": "user",
                "endpoint": {
                    "path": "/users/{user_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_usersuser_idweb_profiles",
                "table_name": "web_profile",
                "endpoint": {
                    "path": "/users/{user_id}/web-profiles",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "50",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
