# instagram_business pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/instagram_business.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /media/{media-id}/comments_ 
  *resource*: media_comments  
  *description*: Get a list of recent comments on a media object.
* _GET /users/self/feed_ 
  *resource*: users_self_feed  
  *description*: See the authenticated user's feed.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 
* _GET /users/{user-id}/follows_ 
  *resource*: users_follows  
  *description*: Get the list of users this user follows. To get follows of the owner of the access token, you can use **self** instead of the `user-id`. 
* _GET /users/{user-id}/followed-by_ 
  *resource*: users_followed_by  
  *description*: Get the list of users this user is followed by. To get users followed by the owner of the access token, you can use **self** instead of the `user-id`. 
* _GET /media/{media-id}/likes_ 
  *resource*: media_likes  
  *description*: Get a list of users who have liked this media.
* _GET /users/self/media/liked_ 
  *resource*: users_self_media_liked  
  *description*: See the list of media liked by the authenticated user. Private media is returned as long as the authenticated user has permission to view that media. Liked media lists are only available for the currently authenticated user. 
* _GET /locations/{location-id}_ 
  *resource*: locations  
  *description*: Get information about a location.
* _GET /media/{media-id}_ 
  *resource*: media  
  *description*: Get information about a media object. The returned type key will allow you to differentiate between image and video media.  **Note:** if you authenticate with an OAuth Token, you will receive the user_has_liked key which quickly tells you whether the current user has liked this media item. 
* _GET /media/popular_ 
  *resource*: media_popular  
  *description*: Get a list of what media is most popular at the moment. Can return mix of `image` and `video` types.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 
* _GET /geographies/{geo-id}/media/recent_ 
  *resource*: geographies_media_recent  
  *description*: Get recent media from a geography subscription that you created.  **Note:** You can only access Geographies that were explicitly created by your OAuth client. Check the Geography Subscriptions section of the [real-time updates page](https://instagram.com/developer/realtime/). When you create a subscription to some geography that you define, you will be returned a unique `geo-id` that can be used in this query. To backfill photos from the location covered by this geography, use the [media search endpoint](https://instagram.com/developer/endpoints/media/).  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 
* _GET /locations/{location-id}/media/recent_ 
  *resource*: locations_media_recent  
  *description*: Get a list of recent media objects from a given location.
* _GET /tags/{tag-name}/media/recent_ 
  *resource*: tags_media_recent  
  *description*: Get a list of recently tagged media. Use the `max_tag_id` and `min_tag_id` parameters in the pagination response to paginate through these objects. 
* _GET /users/{user-id}/media/recent_ 
  *resource*: users_media_recent  
  *description*: Get the most recent media published by a user. To get the most recent media published by the owner of the access token, you can use **self** instead of the `user-id`.  Security scope `public_content` is required to read information about other users. 
* _GET /users/{user-id}/relationship_ 
  *resource*: users_relationship  
  *description*: Get information about a relationship to another user.
* _GET /users/self/requested-by_ 
  *resource*: users_self_requested_by  
  *description*: List the users who have requested this user's permission to follow.
* _GET /locations/search_ 
  *resource*: locations_search  
  *description*: Search for a location by geographic coordinate.
* _GET /media/search_ 
  *resource*: media_search  
  *description*: Search for media in a given area. The default time span is set to 5 days. The time span must not exceed 7 days. Defaults time stamps cover the last 5 days. Can return mix of `image` and `video` types. 
* _GET /tags/search_ 
  *resource*: tags_search  
  *description*: Search for tags by name.
* _GET /users/search_ 
  *resource*: users_search  
  *description*: Search for a user by name.
* _GET /media/shortcode/{shortcode}_ 
  *resource*: media_shortcode  
  *description*: This endpoint returns the same response as `GET /media/{media-id}`.  A media object's shortcode can be found in its shortlink URL. An example shortlink is `http://instagram.com/p/D/`, its corresponding shortcode is `D`. 
* _GET /tags/{tag-name}_ 
  *resource*: tags  
  *description*: Get information about a tag object.
* _GET /users/{user-id}_ 
  *resource*: users  
  *description*: Get basic information about a user. To get information about the owner of the access token, you can use **self** instead of the `user-id`.  Security scope `public_content` is required to read information about other users. 
