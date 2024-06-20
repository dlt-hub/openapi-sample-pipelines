# twitter pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/twitter.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /2/compliance/jobs_ 
  *resource*: list_batch_compliance_jobs  
  *description*: Returns recent Compliance Jobs for a given job type and optional job status
* _GET /2/dm_conversations/with/{participant_id}/dm_events_ 
  *resource*: get_dm_conversations_with_participant_id_dm_events  
  *description*: Returns DM Events for a DM Conversation
* _GET /2/dm_conversations/{id}/dm_events_ 
  *resource*: get_dm_conversations_id_dm_events  
  *description*: Returns DM Events for a DM Conversation
* _GET /2/dm_events_ 
  *resource*: get_dm_events  
  *description*: Returns recent DM Events across DM conversations
* _GET /2/compliance/jobs/{id}_ 
  *resource*: get_batch_compliance_job  
  *description*: Returns a single Compliance Job by ID
* _GET /2/lists/{id}_ 
  *resource*: list_id_get  
  *description*: Returns a List.
* _GET /2/spaces/{id}_ 
  *resource*: find_space_by_id  
  *description*: Returns a variety of information about the Space specified by the requested ID
* _GET /2/tweets/{id}_ 
  *resource*: find_tweet_by_id  
  *description*: Returns a variety of information about the Tweet specified by the requested ID.
* _GET /2/users/by/username/{username}_ 
  *resource*: find_user_by_username  
  *description*: This endpoint returns information about a User. Specify User by username.
* _GET /2/users/{id}_ 
  *resource*: find_user_by_id  
  *description*: This endpoint returns information about a User. Specify User by ID.
* _GET /2/users/{id}/followed_lists_ 
  *resource*: user_followed_lists  
  *description*: Returns a User's followed Lists.
* _GET /2/users/{id}/list_memberships_ 
  *resource*: get_user_list_memberships  
  *description*: Get a User's List Memberships.
* _GET /2/users/{id}/owned_lists_ 
  *resource*: list_user_owned_lists  
  *description*: Get a User's Owned Lists.
* _GET /2/users/{id}/pinned_lists_ 
  *resource*: list_user_pinned_lists  
  *description*: Get a User's Pinned Lists.
* _GET /2/openapi.json_ 
  *resource*: get_open_api_spec  
  *description*: Full OpenAPI Specification in JSON format. (See https://github.com/OAI/OpenAPI-Specification/blob/master/README.md)
* _GET /2/tweets/compliance/stream_ 
  *resource*: get_tweets_compliance_stream  
  *description*: Streams 100% of compliance data for Tweets
* _GET /2/tweets/firehose/stream_ 
  *resource*: get_tweets_firehose_stream  
  *description*: Streams 100% of public Tweets.
* _GET /2/tweets/label/stream_ 
  *resource*: get_tweets_label_stream  
  *description*: Streams 100% of labeling events applied to Tweets
* _GET /2/tweets/sample/stream_ 
  *resource*: sample_stream  
  *description*: Streams a deterministic 1% of public Tweets.
* _GET /2/tweets/sample10/stream_ 
  *resource*: get_tweets_sample_10_stream  
  *description*: Streams a deterministic 10% of public Tweets.
* _GET /2/tweets/search/stream_ 
  *resource*: search_stream  
  *description*: Streams Tweets matching the stream's active rule set.
* _GET /2/users/compliance/stream_ 
  *resource*: get_users_compliance_stream  
  *description*: Streams 100% of compliance data for Users
* _GET /2/users/me_ 
  *resource*: find_my_user  
  *description*: This endpoint returns information about the requesting User.
* _GET /2/tweets/search/stream/rules_ 
  *resource*: get_rules  
  *description*: Returns rules from a User's active rule set. Users can fetch all of their rules or a subset, specified by the provided rule ids.
* _GET /2/tweets/counts/all_ 
  *resource*: tweet_counts_full_archive_search  
  *description*: Returns Tweet Counts that match a search query.
* _GET /2/tweets/counts/recent_ 
  *resource*: tweet_counts_recent_search  
  *description*: Returns Tweet Counts from the last 7 days that match a search query.
* _GET /2/spaces_ 
  *resource*: find_spaces_by_ids  
  *description*: Returns a variety of information about the Spaces specified by the requested IDs
* _GET /2/spaces/by/creator_ids_ 
  *resource*: find_spaces_by_creator_ids  
  *description*: Returns a variety of information about the Spaces created by the provided User IDs
* _GET /2/spaces/search_ 
  *resource*: search_spaces  
  *description*: Returns Spaces that match the provided query.
* _GET /2/lists/{id}/tweets_ 
  *resource*: lists_id_tweets  
  *description*: Returns a list of Tweets associated with the provided List ID.
* _GET /2/spaces/{id}/tweets_ 
  *resource*: space_tweets  
  *description*: Retrieves Tweets shared in the specified Space.
* _GET /2/tweets_ 
  *resource*: find_tweets_by_id  
  *description*: Returns a variety of information about the Tweet specified by the requested ID.
* _GET /2/tweets/search/all_ 
  *resource*: tweets_fullarchive_search  
  *description*: Returns Tweets that match a search query.
* _GET /2/tweets/search/recent_ 
  *resource*: tweets_recent_search  
  *description*: Returns Tweets from the last 7 days that match a search query.
* _GET /2/tweets/{id}/quote_tweets_ 
  *resource*: find_tweets_that_quote_a_tweet  
  *description*: Returns a variety of information about each Tweet that quotes the Tweet specified by the requested ID.
* _GET /2/users/{id}/bookmarks_ 
  *resource*: get_users_id_bookmarks  
  *description*: Returns Tweet objects that have been bookmarked by the requesting User
* _GET /2/users/{id}/liked_tweets_ 
  *resource*: users_id_liked_tweets  
  *description*: Returns a list of Tweets liked by the provided User ID
* _GET /2/users/{id}/mentions_ 
  *resource*: users_id_mentions  
  *description*: Returns Tweet objects that mention username associated to the provided User ID
* _GET /2/users/{id}/timelines/reverse_chronological_ 
  *resource*: users_id_timeline  
  *description*: Returns Tweet objects that appears in the provided User ID's home timeline
* _GET /2/users/{id}/tweets_ 
  *resource*: users_id_tweets  
  *description*: Returns a list of Tweets authored by the provided User ID
* _GET /2/lists/{id}/followers_ 
  *resource*: list_get_followers  
  *description*: Returns a list of Users that follow a List by the provided List ID
* _GET /2/lists/{id}/members_ 
  *resource*: list_get_members  
  *description*: Returns a list of Users that are members of a List by the provided List ID.
* _GET /2/spaces/{id}/buyers_ 
  *resource*: space_buyers  
  *description*: Retrieves the list of Users who purchased a ticket to the given space
* _GET /2/tweets/{id}/liking_users_ 
  *resource*: tweets_id_liking_users  
  *description*: Returns a list of Users that have liked the provided Tweet ID
* _GET /2/tweets/{id}/retweeted_by_ 
  *resource*: tweets_id_retweeting_users  
  *description*: Returns a list of Users that have retweeted the provided Tweet ID
* _GET /2/users_ 
  *resource*: find_users_by_id  
  *description*: This endpoint returns information about Users. Specify Users by their ID.
* _GET /2/users/by_ 
  *resource*: find_users_by_username  
  *description*: This endpoint returns information about Users. Specify Users by their username.
* _GET /2/users/{id}/blocking_ 
  *resource*: users_id_blocking  
  *description*: Returns a list of Users that are blocked by the provided User ID
* _GET /2/users/{id}/followers_ 
  *resource*: users_id_followers  
  *description*: Returns a list of Users who are followers of the specified User ID.
* _GET /2/users/{id}/following_ 
  *resource*: users_id_following  
  *description*: Returns a list of Users that are being followed by the provided User ID
* _GET /2/users/{id}/muting_ 
  *resource*: users_id_muting  
  *description*: Returns a list of Users that are muted by the provided User ID
