# vimeo pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/vimeo.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /_ 
  *resource*: get_endpoints  
  *description*: This method returns a full specification for the Vimeo API.
* _GET /me/feed_ 
  *resource*: get_feed_alt1  
  *description*: This method returns all the videos in the authenticated user's feed.
* _GET /users/{user_id}/feed_ 
  *resource*: get_feed  
  *description*: This method returns all the videos in the authenticated user's feed.
* _GET /me/albums_ 
  *resource*: get_albums_alt1  
  *description*: This method gets all the albums from the specified user's account.
* _GET /me/albums/{album_id}_ 
  *resource*: get_album_alt1  
  *description*: This method gets a single album.
* _GET /users/{user_id}/albums_ 
  *resource*: get_albums  
  *description*: This method gets all the albums from the specified user's account.
* _GET /users/{user_id}/albums/{album_id}_ 
  *resource*: get_album  
  *description*: This method gets a single album.
* _GET /videos/{video_id}/available_albums_ 
  *resource*: get_available_video_albums  
* _GET /categories_ 
  *resource*: get_categories  
  *description*: This method gets all existing categories.
* _GET /categories/{category}_ 
  *resource*: get_category  
  *description*: This method gets a single category.
* _GET /channels/{channel_id}/categories_ 
  *resource*: get_channel_categories  
  *description*: This method gets all the categories in the specified channel.
* _GET /me/categories_ 
  *resource*: get_category_subscriptions_alt1  
  *description*: This method gets all the categories to which a particular user has subscribed.
* _GET /me/categories/{category}_ 
  *resource*: check_if_user_subscribed_to_category_alt1  
  *description*: This method determines whether a particular user is subscribed to the specified category.
* _GET /users/{user_id}/categories_ 
  *resource*: get_category_subscriptions  
  *description*: This method gets all the categories to which a particular user has subscribed.
* _GET /users/{user_id}/categories/{category}_ 
  *resource*: check_if_user_subscribed_to_category  
  *description*: This method determines whether a particular user is subscribed to the specified category.
* _GET /videos/{video_id}/categories_ 
  *resource*: get_video_categories  
  *description*: This method gets all the categories that contain a particular video.
* _GET /categories/{category}/channels_ 
  *resource*: get_category_channels  
  *description*: This method gets all the channels that belong to a category.
* _GET /channels_ 
  *resource*: get_channels  
  *description*: This method gets all existing channels.
* _GET /channels/{channel_id}_ 
  *resource*: get_channel  
  *description*: This method gets a single channel.
* _GET /me/channels_ 
  *resource*: get_channel_subscriptions_alt1  
  *description*: This method gets all the channels to which the specified user subscribes.
* _GET /me/channels/{channel_id}_ 
  *resource*: check_if_user_subscribed_to_channel_alt1  
  *description*: This method determines whether a specific user is a follower of the channel in question.
* _GET /users/{user_id}/channels_ 
  *resource*: get_channel_subscriptions  
  *description*: This method gets all the channels to which the specified user subscribes.
* _GET /users/{user_id}/channels/{channel_id}_ 
  *resource*: check_if_user_subscribed_to_channel  
  *description*: This method determines whether a specific user is a follower of the channel in question.
* _GET /videos/{video_id}/available_channels_ 
  *resource*: get_available_video_channels  
  *description*: Information about this method appears below.
* _GET /channels/{channel_id}/videos/{video_id}/comments_ 
  *resource*: get_comments_alt1  
  *description*: This method returns all the comments on the specified video.
* _GET /videos/{video_id}/comments_ 
  *resource*: get_comments  
  *description*: This method returns all the comments on the specified video.
* _GET /videos/{video_id}/comments/{comment_id}_ 
  *resource*: get_comment  
  *description*: This method returns the specified comment on a video.
* _GET /videos/{video_id}/comments/{comment_id}/replies_ 
  *resource*: get_comment_replies  
  *description*: This method returns all the replies to the specified video comment.
* _GET /contentratings_ 
  *resource*: get_content_ratings  
  *description*: This method returns all available content ratings.
* _GET /creativecommons_ 
  *resource*: get_cc_licenses  
  *description*: This method returns all available Creative Commons licenses.
* _GET /channels/{channel_id}/videos/{video_id}/credits_ 
  *resource*: get_video_credits_alt1  
  *description*: This method returns all the credited users in a video.
* _GET /videos/{video_id}/credits_ 
  *resource*: get_video_credits  
  *description*: This method returns all the credited users in a video.
* _GET /videos/{video_id}/credits/{credit_id}_ 
  *resource*: get_video_credit  
  *description*: This method returns a single credited user in a video.
* _GET /videos/{video_id}/privacy/domains_ 
  *resource*: get_video_privacy_domains  
  *description*: This method returns all the domains on the specified video's whitelist.
* _GET /me/following/{follow_user_id}_ 
  *resource*: check_if_user_is_following_alt1  
  *description*: This method determines whether the authenticated user is a follower of the user in question.
* _GET /users/{user_id}/following/{follow_user_id}_ 
  *resource*: check_if_user_is_following  
  *description*: This method determines whether the authenticated user is a follower of the user in question.
* _GET /categories/{category}/groups_ 
  *resource*: get_category_groups  
  *description*: This method gets all the groups that belong to a category.
* _GET /groups_ 
  *resource*: get_groups  
  *description*: This method returns all groups.
* _GET /groups/{group_id}_ 
  *resource*: get_group  
  *description*: This method returns a specific group.
* _GET /me/groups_ 
  *resource*: get_user_groups_alt1  
  *description*: This method returns all the groups to which a particular user belongs.
* _GET /me/groups/{group_id}_ 
  *resource*: check_if_user_joined_group_alt1  
  *description*: This method determines whether a particular user belongs to the specified group.
* _GET /users/{user_id}/groups_ 
  *resource*: get_user_groups  
  *description*: This method returns all the groups to which a particular user belongs.
* _GET /users/{user_id}/groups/{group_id}_ 
  *resource*: check_if_user_joined_group  
  *description*: This method determines whether a particular user belongs to the specified group.
* _GET /languages_ 
  *resource*: get_languages  
  *description*: This method returns all the video languages that Vimeo supports.
* _GET /me/likes/{video_id}_ 
  *resource*: check_if_user_liked_video_alt1  
  *description*: This method checks if the specified user has liked a particular video.
* _GET /users/{user_id}/likes/{video_id}_ 
  *resource*: check_if_user_liked_video  
  *description*: This method checks if the specified user has liked a particular video.
* _GET /me_ 
  *resource*: get_user_alt1  
  *description*: This method returns the representation of the authenticated user.
* _GET /ondemand/genres_ 
  *resource*: get_vod_genres  
  *description*: Information about this method appears below.
* _GET /ondemand/genres/{genre_id}_ 
  *resource*: get_vod_genre  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/genres_ 
  *resource*: get_vod_genres_by_ondemand_id  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/genres/{genre_id}_ 
  *resource*: get_vod_genre_by_ondemand_id  
  *description*: Information about this method appears below.
* _GET /me/ondemand/pages_ 
  *resource*: get_user_vods_alt1  
  *description*: Information about this method appears below.
* _GET /me/ondemand/purchases_ 
  *resource*: get_vod_purchases  
  *description*: Information about this method appears below.
* _GET /me/ondemand/purchases/{ondemand_id}_ 
  *resource*: check_if_vod_was_purchased_alt1  
  *description*: Information about this method appears below.
* _GET /ondemand/genres/{genre_id}/pages_ 
  *resource*: get_genre_vods  
  *description*: This method returns all the On Demand pages that are in a specific genre.
* _GET /ondemand/genres/{genre_id}/pages/{ondemand_id}_ 
  *resource*: get_genre_vod  
  *description*: Check whether a genre contains an On Demand page.
* _GET /ondemand/pages/{ondemand_id}_ 
  *resource*: get_vod  
  *description*: Information about this method appears below.
* _GET /users/{user_id}/ondemand/pages_ 
  *resource*: get_user_vods  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/promotions/{promotion_id}_ 
  *resource*: get_vod_promotion  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/promotions/{promotion_id}/codes_ 
  *resource*: get_vod_promotion_codes  
  *description*: This method returns all the codes of a promotion on an On Demand page.
* _GET /ondemand/pages/{ondemand_id}/regions_ 
  *resource*: get_vod_regions  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/regions/{country}_ 
  *resource*: get_vod_region  
  *description*: Checks whether an On Demand page belongs to a region.
* _GET /ondemand/regions_ 
  *resource*: get_regions  
  *description*: Information about this method appears below.
* _GET /ondemand/regions/{country}_ 
  *resource*: get_region  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/seasons_ 
  *resource*: get_vod_seasons  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/seasons/{season_id}_ 
  *resource*: get_vod_season  
  *description*: Information about this method appears below.
* _GET /channels/{channel_id}/videos/{video_id}/pictures_ 
  *resource*: get_video_thumbnails_alt1  
  *description*: This method returns all the thumbnail images of the specified video.
* _GET /me/customlogos_ 
  *resource*: get_custom_logos_alt1  
  *description*: This method returns all the custom logos that belong to the specified user.
* _GET /me/customlogos/{logo_id}_ 
  *resource*: get_custom_logo_alt1  
  *description*: This method returns a single custom logo belonging to the specified user.
* _GET /me/pictures_ 
  *resource*: get_pictures_alt1  
  *description*: This method returns all the portrait images belonging to the authenticated user.
* _GET /me/pictures/{portraitset_id}_ 
  *resource*: get_picture_alt1  
  *description*: This method returns a single portrait image belonging to the authenticated user.
* _GET /ondemand/pages/{ondemand_id}/backgrounds_ 
  *resource*: get_vod_backgrounds  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/backgrounds/{background_id}_ 
  *resource*: get_vod_background  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/pictures_ 
  *resource*: get_vod_posters  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/pictures/{poster_id}_ 
  *resource*: get_vod_poster  
  *description*: Information about this method appears below.
* _GET /users/{user_id}/albums/{album_id}/custom_thumbnails_ 
  *resource*: get_album_custom_thumbs  
  *description*: This method gets all the custom uploaded thumbnails from the specified album.
* _GET /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id}_ 
  *resource*: get_album_custom_thumbnail  
  *description*: This method returns all the videos associated with the specified tag.
* _GET /users/{user_id}/albums/{album_id}/logos_ 
  *resource*: get_album_logos  
  *description*: This method gets all the custom logos from the specified album.
* _GET /users/{user_id}/albums/{album_id}/logos/{logo_id}_ 
  *resource*: get_album_logo  
  *description*: This method gets a single custom logo from the specified album.
* _GET /users/{user_id}/customlogos_ 
  *resource*: get_custom_logos  
  *description*: This method returns all the custom logos that belong to the specified user.
* _GET /users/{user_id}/customlogos/{logo_id}_ 
  *resource*: get_custom_logo  
  *description*: This method returns a single custom logo belonging to the specified user.
* _GET /users/{user_id}/pictures_ 
  *resource*: get_pictures  
  *description*: This method returns all the portrait images belonging to the authenticated user.
* _GET /users/{user_id}/pictures/{portraitset_id}_ 
  *resource*: get_picture  
  *description*: This method returns a single portrait image belonging to the authenticated user.
* _GET /videos/{video_id}/pictures_ 
  *resource*: get_video_thumbnails  
  *description*: This method returns all the thumbnail images of the specified video.
* _GET /videos/{video_id}/pictures/{picture_id}_ 
  *resource*: get_video_thumbnail  
  *description*: This method returns a single thumbnail image from the specified video.
* _GET /videos/{video_id}/timelinethumbnails/{thumbnail_id}_ 
  *resource*: get_video_custom_logo  
  *description*: This method returns a single timeline event thumbnail that belongs to the specified video.
* _GET /me/portfolios_ 
  *resource*: get_portfolios_alt1  
  *description*: This method gets all the specified user's portfolios.
* _GET /me/portfolios/{portfolio_id}_ 
  *resource*: get_portfolio_alt1  
  *description*: This method gets a single portfolio from the specified user.
* _GET /users/{user_id}/portfolios_ 
  *resource*: get_portfolios  
  *description*: This method gets all the specified user's portfolios.
* _GET /users/{user_id}/portfolios/{portfolio_id}_ 
  *resource*: get_portfolio  
  *description*: This method gets a single portfolio from the specified user.
* _GET /videos/{video_id}/presets/{preset_id}_ 
  *resource*: get_video_embed_preset  
  *description*: This method determines whether the specified video uses a particular embed preset.
* _GET /me/presets_ 
  *resource*: get_embed_presets_alt1  
  *description*: This method returns all the embed presets that belong to the specified user.
* _GET /me/presets/{preset_id}_ 
  *resource*: get_embed_preset_alt1  
  *description*: This method returns a single embed preset that belongs to the specified user.
* _GET /users/{user_id}/presets_ 
  *resource*: get_embed_presets  
  *description*: This method returns all the embed presets that belong to the specified user.
* _GET /users/{user_id}/presets/{preset_id}_ 
  *resource*: get_embed_preset  
  *description*: This method returns a single embed preset that belongs to the specified user.
* _GET /me/projects_ 
  *resource*: get_projects_alt1  
  *description*: This method gets all the projects that belong to the specified user.
* _GET /me/projects/{project_id}_ 
  *resource*: get_project_alt1  
  *description*: This method gets a single project that belongs to the specified user.
* _GET /users/{user_id}/projects_ 
  *resource*: get_projects  
  *description*: This method gets all the projects that belong to the specified user.
* _GET /users/{user_id}/projects/{project_id}_ 
  *resource*: get_project  
  *description*: This method gets a single project that belongs to the specified user.
* _GET /ondemand/pages/{ondemand_id}/promotions_ 
  *resource*: get_vod_promotions  
  *description*: Information about this method appears below.
* _GET /users/{user_id}/ondemand/purchases_ 
  *resource*: check_if_vod_was_purchased  
  *description*: Information about this method appears below.
* _GET /channels/{channel_id}/tags_ 
  *resource*: get_channel_tags  
  *description*: This method gets all the tags that have been added to the specified channel.
* _GET /channels/{channel_id}/tags/{word}_ 
  *resource*: check_if_channel_has_tag  
  *description*: This method determines whether a specific tag has been added to the channel in question.
* _GET /tags/{word}_ 
  *resource*: get_tag  
  *description*: This method gets a specific tag from all available tags.
* _GET /videos/{video_id}/tags_ 
  *resource*: get_video_tags  
  *description*: This method returns all the tags associated with a video.
* _GET /videos/{video_id}/tags/{word}_ 
  *resource*: check_video_for_tag  
  *description*: This method determines whether a particular tag has been added to a video.
* _GET /channels/{channel_id}/videos/{video_id}/texttracks_ 
  *resource*: get_text_tracks_alt1  
  *description*: This method returns all the text tracks of the specified video.
* _GET /videos/{video_id}/texttracks_ 
  *resource*: get_text_tracks  
  *description*: This method returns all the text tracks of the specified video.
* _GET /videos/{video_id}/texttracks/{texttrack_id}_ 
  *resource*: get_text_track  
  *description*: This method returns a single text track from the specified video.
* _GET /tutorial_ 
  *resource*: developer_tutorial  
  *description*: This method, in conjunction with our [Getting Started](https://developer.vimeo.com/api/guides/start) guide, can help you learn how to use the Vimeo API.
* _GET /users/{user_id}/uploads/{upload_id}_ 
  *resource*: get_upload_attempt  
  *description*: This method returns all the embed presets that belong to the specified user.
* _GET /channels/{channel_id}/moderators_ 
  *resource*: get_channel_moderators  
  *description*: This method gets all the moderators of the specified channel.
* _GET /channels/{channel_id}/moderators/{user_id}_ 
  *resource*: get_channel_moderator  
  *description*: This method gets a single moderator of the specified channel.
* _GET /channels/{channel_id}/privacy/users_ 
  *resource*: get_channel_privacy_users  
  *description*: This method gets all the users who have access to the specified private channel.
* _GET /channels/{channel_id}/users_ 
  *resource*: get_channel_subscribers  
  *description*: This method gets all the followers of a specific channel.
* _GET /channels/{channel_id}/videos/{video_id}/likes_ 
  *resource*: get_video_likes_alt1  
  *description*: This method gets all the users who have liked a particular video.
* _GET /channels/{channel_id}/videos/{video_id}/privacy/users_ 
  *resource*: get_video_privacy_users_alt1  
  *description*: This method returns all the users who have access to the specified private video.
* _GET /groups/{group_id}/users_ 
  *resource*: get_group_members  
  *description*: This method returns all the users that belong to the specified group.
* _GET /me/followers_ 
  *resource*: get_followers_alt1  
  *description*: This method returns all the followers of the authenticated user.
* _GET /me/following_ 
  *resource*: get_user_following_alt1  
  *description*: This method returns all users that the authenticated user is following.
* _GET /ondemand/pages/{ondemand_id}/likes_ 
  *resource*: get_vod_likes  
  *description*: This method gets all the users who have liked a particular video on an On Demand page.
* _GET /users_ 
  *resource*: search_users  
  *description*: Information about this method appears below.
* _GET /users/{user_id}_ 
  *resource*: get_user  
  *description*: This method returns the representation of the authenticated user.
* _GET /users/{user_id}/followers_ 
  *resource*: get_followers  
  *description*: This method returns all the followers of the authenticated user.
* _GET /users/{user_id}/following_ 
  *resource*: get_user_following  
  *description*: This method returns all users that the authenticated user is following.
* _GET /videos/{video_id}/likes_ 
  *resource*: get_video_likes  
  *description*: This method gets all the users who have liked a particular video.
* _GET /videos/{video_id}/privacy/users_ 
  *resource*: get_video_privacy_users  
  *description*: This method returns all the users who have access to the specified private video.
* _GET /oauth/verify_ 
  *resource*: verify_token  
  *description*: This method verifies that an OAuth 2 token exists.
* _GET /categories/{category}/videos_ 
  *resource*: get_category_videos  
  *description*: This method gets all the videos that belong to a category.
* _GET /categories/{category}/videos/{video_id}_ 
  *resource*: check_category_for_video  
  *description*: This method gets a single video from a category. Use it to determine whether the video belongs to the category.
* _GET /channels/{channel_id}/videos_ 
  *resource*: get_channel_videos  
  *description*: This method gets all the videos in a specific channel.
* _GET /channels/{channel_id}/videos/{video_id}_ 
  *resource*: get_channel_video  
  *description*: This method returns a specific video in a channel. You can use it to determine whether the video is in the channel.
* _GET /groups/{group_id}/videos_ 
  *resource*: get_group_videos  
  *description*: This method removes a single video from the specified group.
* _GET /groups/{group_id}/videos/{video_id}_ 
  *resource*: get_group_video  
  *description*: This method returns a single video from a group. You can use this method to determine whether the video belongs to the group.
* _GET /me/albums/{album_id}/videos_ 
  *resource*: get_album_videos_alt1  
  *description*: This method gets all the videos from the specified album.
* _GET /me/albums/{album_id}/videos/{video_id}_ 
  *resource*: get_album_video_alt1  
  *description*: This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.
* _GET /me/appearances_ 
  *resource*: get_appearances_alt1  
  *description*: This method returns all the videos in which the authenticated user has a credited appearance.
* _GET /me/likes_ 
  *resource*: get_likes_alt1  
  *description*: This method gets all the videos that the specified user has liked.
* _GET /me/portfolios/{portfolio_id}/videos_ 
  *resource*: get_portfolio_videos_alt1  
  *description*: This method gets all the videos from the specified portfolio.
* _GET /me/portfolios/{portfolio_id}/videos/{video_id}_ 
  *resource*: get_portfolio_video_alt1  
  *description*: This method gets a single video from the specified portfolio.
* _GET /me/presets/{preset_id}/videos_ 
  *resource*: get_embed_preset_videos_alt1  
  *description*: This method returns all the videos that make use of the specified embed preset.
* _GET /me/projects/{project_id}/videos_ 
  *resource*: get_project_videos_alt1  
  *description*: This method gets all the videos that belong to the specified project.
* _GET /me/videos_ 
  *resource*: get_videos_alt1  
  *description*: This method returns all the videos that the authenticated user has uploaded.
* _GET /me/videos/{video_id}_ 
  *resource*: check_if_user_owns_video_alt1  
  *description*: This method determines whether a particular user is the owner of the specified video.
* _GET /me/watched/videos_ 
  *resource*: get_watch_history  
  *description*: Information about this method appears below.  **NOTE:** This endpoint is deprecated. Any request to it returns empty data with HTTP status code 200.
* _GET /me/watchlater_ 
  *resource*: get_watch_later_queue_alt1  
  *description*: This method gets all the videos from the specified user's Watch Later queue.
* _GET /me/watchlater/{video_id}_ 
  *resource*: check_watch_later_queue_alt1  
  *description*: This method checks the specified user's Watch Later queue for a particular video.
* _GET /ondemand/pages/{ondemand_id}/seasons/{season_id}/videos_ 
  *resource*: get_vod_season_videos  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/videos_ 
  *resource*: get_vod_videos  
  *description*: Information about this method appears below.
* _GET /ondemand/pages/{ondemand_id}/videos/{video_id}_ 
  *resource*: get_vod_video  
  *description*: Information about this method appears below.
* _GET /tags/{word}/videos_ 
  *resource*: get_videos_with_tag  
  *description*: This method returns all the videos associated with the specified tag.
* _GET /users/{user_id}/albums/{album_id}/videos_ 
  *resource*: get_album_videos  
  *description*: This method gets all the videos from the specified album.
* _GET /users/{user_id}/albums/{album_id}/videos/{video_id}_ 
  *resource*: get_album_video  
  *description*: This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.
* _GET /users/{user_id}/appearances_ 
  *resource*: get_appearances  
  *description*: This method returns all the videos in which the authenticated user has a credited appearance.
* _GET /users/{user_id}/likes_ 
  *resource*: get_likes  
  *description*: This method gets all the videos that the specified user has liked.
* _GET /users/{user_id}/portfolios/{portfolio_id}/videos_ 
  *resource*: get_portfolio_videos  
  *description*: This method gets all the videos from the specified portfolio.
* _GET /users/{user_id}/portfolios/{portfolio_id}/videos/{video_id}_ 
  *resource*: get_portfolio_video  
  *description*: This method gets a single video from the specified portfolio.
* _GET /users/{user_id}/presets/{preset_id}/videos_ 
  *resource*: get_embed_preset_videos  
  *description*: This method returns all the videos that make use of the specified embed preset.
* _GET /users/{user_id}/projects/{project_id}/videos_ 
  *resource*: get_project_videos  
  *description*: This method gets all the videos that belong to the specified project.
* _GET /users/{user_id}/videos_ 
  *resource*: get_videos  
  *description*: This method returns all the videos that the authenticated user has uploaded.
* _GET /users/{user_id}/videos/{video_id}_ 
  *resource*: check_if_user_owns_video  
  *description*: This method determines whether a particular user is the owner of the specified video.
* _GET /users/{user_id}/watchlater_ 
  *resource*: get_watch_later_queue  
  *description*: This method gets all the videos from the specified user's Watch Later queue.
* _GET /users/{user_id}/watchlater/{video_id}_ 
  *resource*: check_watch_later_queue  
  *description*: This method checks the specified user's Watch Later queue for a particular video.
* _GET /videos_ 
  *resource*: search_videos  
  *description*: This method returns all the videos that match custom search criteria.
* _GET /videos/{video_id}_ 
  *resource*: get_video  
  *description*: This method returns a single video.
* _GET /videos/{video_id}/videos_ 
  *resource*: get_related_videos  
  *description*: This method returns all the related videos of a particular video.
