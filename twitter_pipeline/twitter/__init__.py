from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="twitter_source", max_table_nesting=2)
def twitter_source(
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
        },
        "resources": [
            # Returns recent Compliance Jobs for a given job type and optional job status
            {
                "name": "list_batch_compliance_jobs",
                "table_name": "compliance_job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/compliance/jobs",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                        # "compliance_job.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns DM Events for a DM Conversation
            {
                "name": "get_dm_conversations_with_participant_id_dm_events",
                "table_name": "dm_event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/dm_conversations/with/{participant_id}/dm_events",
                    "params": {
                        "participant_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "event_types": "['MessageCreate', 'ParticipantsLeave', 'ParticipantsJoin']",
                        # "dm_event.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns DM Events for a DM Conversation
            {
                "name": "get_dm_conversations_id_dm_events",
                "table_name": "dm_event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/dm_conversations/{id}/dm_events",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "event_types": "['MessageCreate', 'ParticipantsLeave', 'ParticipantsJoin']",
                        # "dm_event.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns recent DM Events across DM conversations
            {
                "name": "get_dm_events",
                "table_name": "dm_event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/dm_events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "event_types": "['MessageCreate', 'ParticipantsLeave', 'ParticipantsJoin']",
                        # "dm_event.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single Compliance Job by ID
            {
                "name": "get_batch_compliance_job",
                "table_name": "get_2_compliance_jobs_id_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/compliance/jobs/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "list_batch_compliance_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "compliance_job.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a List.
            {
                "name": "list_id_get",
                "table_name": "get_2_lists_id_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/lists/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "list.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a variety of information about the Space specified by the requested ID
            {
                "name": "find_space_by_id",
                "table_name": "get_2_spaces_id_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/spaces/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_spaces_by_ids",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "space.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "topic.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a variety of information about the Tweet specified by the requested ID.
            {
                "name": "find_tweet_by_id",
                "table_name": "get_2_tweets_id_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/tweets/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_tweets_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint returns information about a User. Specify User by username.
            {
                "name": "find_user_by_username",
                "table_name": "get_2_users_by_username_username_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/users/by/username/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "find_users_by_username",
                            "field": "username",
                        },
                        # the parameters below can optionally be configured
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint returns information about a User. Specify User by ID.
            {
                "name": "find_user_by_id",
                "table_name": "get_2_users_id_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/users/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a User's followed Lists.
            {
                "name": "user_followed_lists",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/followed_lists",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "list.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a User's List Memberships.
            {
                "name": "get_user_list_memberships",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/list_memberships",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "list.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a User's Owned Lists.
            {
                "name": "list_user_owned_lists",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/owned_lists",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "list.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a User's Pinned Lists.
            {
                "name": "list_user_pinned_lists",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/pinned_lists",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "list.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
            {
                "name": "get_open_api_spec",
                "table_name": "openapus",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2/openapi.json",
                    "paginator": "auto",
                },
            },
            # Streams 100% of compliance data for Tweets
            {
                "name": "get_tweets_compliance_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/tweets/compliance/stream",
                    "params": {
                        "partition": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Streams 100% of public Tweets.
            {
                "name": "get_tweets_firehose_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/tweets/firehose/stream",
                    "params": {
                        "partition": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Streams 100% of labeling events applied to Tweets
            {
                "name": "get_tweets_label_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/tweets/label/stream",
                    "params": {
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Streams a deterministic 1% of public Tweets.
            {
                "name": "sample_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/tweets/sample/stream",
                    "params": {
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Streams a deterministic 10% of public Tweets.
            {
                "name": "get_tweets_sample_10_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/tweets/sample10/stream",
                    "params": {
                        "partition": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Streams Tweets matching the stream's active rule set.
            {
                "name": "search_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/tweets/search/stream",
                    "params": {
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Streams 100% of compliance data for Users
            {
                "name": "get_users_compliance_stream",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/users/compliance/stream",
                    "params": {
                        "partition": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "backfill_minutes": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint returns information about the requesting User.
            {
                "name": "find_my_user",
                "table_name": "problem",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/2/users/me",
                    "params": {
                        # the parameters below can optionally be configured
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns rules from a User's active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.
            {
                "name": "get_rules",
                "table_name": "rule",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/search/stream/rules",
                    "params": {
                        # the parameters below can optionally be configured
                        # "ids": "OPTIONAL_CONFIG",
                        # "max_results": "1000",
                        # "pagination_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweet Counts that match a search query.
            {
                "name": "tweet_counts_full_archive_search",
                "table_name": "search_count",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/counts/all",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "next_token": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "granularity": "hour",
                        # "search_count.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweet Counts from the last 7 days that match a search query.
            {
                "name": "tweet_counts_recent_search",
                "table_name": "search_count",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/counts/recent",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "next_token": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "granularity": "hour",
                        # "search_count.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a variety of information about the Spaces specified by the requested IDs
            {
                "name": "find_spaces_by_ids",
                "table_name": "space",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/spaces",
                    "params": {
                        "ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "space.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "topic.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a variety of information about the Spaces created by the provided User IDs
            {
                "name": "find_spaces_by_creator_ids",
                "table_name": "space",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/spaces/by/creator_ids",
                    "params": {
                        "user_ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "space.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "topic.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Spaces that match the provided query.
            {
                "name": "search_spaces",
                "table_name": "space",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/spaces/search",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "state": "all",
                        # "max_results": "100",
                        # "space.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "topic.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Tweets associated with the provided List ID.
            {
                "name": "lists_id_tweets",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/lists/{id}/tweets",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves Tweets shared in the specified Space.
            {
                "name": "space_tweets",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/spaces/{id}/tweets",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_spaces_by_ids",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a variety of information about the Tweet specified by the requested ID.
            {
                "name": "find_tweets_by_id",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets",
                    "params": {
                        "ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweets that match a search query.
            {
                "name": "tweets_fullarchive_search",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/search/all",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "max_results": "10",
                        # "next_token": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweets from the last 7 days that match a search query.
            {
                "name": "tweets_recent_search",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/search/recent",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "max_results": "10",
                        # "next_token": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a variety of information about each Tweet that quotes the Tweet specified by the requested ID.
            {
                "name": "find_tweets_that_quote_a_tweet",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/{id}/quote_tweets",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_tweets_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "10",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweet objects that have been bookmarked by the requesting User
            {
                "name": "get_users_id_bookmarks",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/bookmarks",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Tweets liked by the provided User ID
            {
                "name": "users_id_liked_tweets",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/liked_tweets",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweet objects that mention username associated to the provided User ID
            {
                "name": "users_id_mentions",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/mentions",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns Tweet objects that appears in the provided User ID's home timeline
            {
                "name": "users_id_timeline",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/timelines/reverse_chronological",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Tweets authored by the provided User ID
            {
                "name": "users_id_tweets",
                "table_name": "tweet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/tweets",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "since_id": "OPTIONAL_CONFIG",
                        # "until_id": "OPTIONAL_CONFIG",
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "start_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "media.fields": "OPTIONAL_CONFIG",
                        # "poll.fields": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "place.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that follow a List by the provided List ID
            {
                "name": "list_get_followers",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/lists/{id}/followers",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that are members of a List by the provided List ID.
            {
                "name": "list_get_members",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/lists/{id}/members",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the list of Users who purchased a ticket to the given space
            {
                "name": "space_buyers",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/spaces/{id}/buyers",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_spaces_by_ids",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "max_results": "100",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that have liked the provided Tweet ID
            {
                "name": "tweets_id_liking_users",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/{id}/liking_users",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_tweets_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that have retweeted the provided Tweet ID
            {
                "name": "tweets_id_retweeting_users",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/tweets/{id}/retweeted_by",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_tweets_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint returns information about Users. Specify Users by their ID.
            {
                "name": "find_users_by_id",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users",
                    "params": {
                        "ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint returns information about Users. Specify Users by their username.
            {
                "name": "find_users_by_username",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/by",
                    "params": {
                        "usernames": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that are blocked by the provided User ID
            {
                "name": "users_id_blocking",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/blocking",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users who are followers of the specified User ID.
            {
                "name": "users_id_followers",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/followers",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that are being followed by the provided User ID
            {
                "name": "users_id_following",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/following",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "OPTIONAL_CONFIG",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of Users that are muted by the provided User ID
            {
                "name": "users_id_muting",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/2/users/{id}/muting",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_users_by_id",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "max_results": "100",
                        # "pagination_token": "OPTIONAL_CONFIG",
                        # "user.fields": "OPTIONAL_CONFIG",
                        # "expansions": "OPTIONAL_CONFIG",
                        # "tweet.fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
