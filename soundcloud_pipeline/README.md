# soundcloud pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/soundcloud.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /me/activities_ 
  *resource*: get_meactivities  
* _GET /tracks/{track_id}/comments_ 
  *resource*: get_trackstrack_idcomments  
* _GET /users/{user_id}/comments_ 
  *resource*: get_usersuser_idcomments  
* _GET /connect_ 
  *resource*: get_connect  
  *description*: <h3>Security Advice</h3> * Using the [implicit OAuth authorization flow](https://tools.ietf.org/html/draft-ietf-oauth-security-topics-16#section-2.1.2) (`response_type=token`)  is **not recommended**. It can suffer from access token leakage and access token replay attacks. Use `response_type=code` instead. * Use the `state` parameter for [CSRF protection](https://tools.ietf.org/html/draft-ietf-oauth-security-topics-16#section-4.7). Pass a sufficient  random nonce here and verify this nonce again after retrieving the token. 
* _GET /me/connections_ 
  *resource*: get_meconnections  
* _GET /me/connections/{connection_id}_ 
  *resource*: get_meconnectionsconnection_id  
* _GET /users/{user_id}/favorites_ 
  *resource*: get_usersuser_idfavorites  
* _GET /tracks/{track_id}/favoriters_ 
  *resource*: get_trackstrack_idfavoriters  
* _GET /me/followers_ 
  *resource*: get_mefollowers  
* _GET /me/followers/{follower_id}_ 
  *resource*: get_mefollowersfollower_id  
* _GET /users/{user_id}/followers_ 
  *resource*: get_usersuser_idfollowers  
  *description*: Returns a list of users that follows (user_id).
* _GET /me/followings_ 
  *resource*: get_mefollowings  
* _GET /me/followings/{user_id}_ 
  *resource*: get_mefollowingsuser_id  
* _GET /users/{user_id}/followings_ 
  *resource*: get_usersuser_idfollowings  
  *description*: Returns list of users that (user_id) follows.
* _GET /users/{user_id}/followings/{following_id}_ 
  *resource*: get_usersuser_idfollowingsfollowing_id  
  *description*: Returns (following_id) that is followed by (user_id).
* _GET /me/favorites/ids_ 
  *resource*: get_mefavoritesids  
* _GET /me_ 
  *resource*: get_me  
* _GET /me/activities/all/own_ 
  *resource*: get_meactivitiesallown  
* _GET /me/playlists_ 
  *resource*: get_meplaylists  
  *description*: Returns playlist info, playlist tracks and tracks owner info.
* _GET /me/playlists/{playlist_id}_ 
  *resource*: get_meplaylistsplaylist_id  
* _GET /playlists_ 
  *resource*: get_playlists  
* _GET /playlists/{playlist_id}_ 
  *resource*: get_playlistsplaylist_id  
* _GET /users/{user_id}/playlists_ 
  *resource*: get_usersuser_idplaylists  
* _GET /tracks/{track_id}/related_ 
  *resource*: get_trackstrack_idrelated  
* _GET /playlists/{playlist_id}/reposters_ 
  *resource*: get_playlistsplaylist_idreposters  
* _GET /tracks/{track_id}/reposters_ 
  *resource*: get_trackstrack_idreposters  
* _GET /resolve_ 
  *resource*: get_resolve  
* _GET /tracks/{track_id}/streams_ 
  *resource*: get_trackstrack_idstreams  
* _GET /me/activities/tracks_ 
  *resource*: get_meactivitiestracks  
* _GET /me/followings/tracks_ 
  *resource*: get_mefollowingstracks  
* _GET /me/likes/tracks_ 
  *resource*: get_melikestracks  
* _GET /me/tracks_ 
  *resource*: get_metracks  
* _GET /me/tracks/{track_id}_ 
  *resource*: get_metrackstrack_id  
* _GET /playlists/{playlist_id}/tracks_ 
  *resource*: get_playlistsplaylist_idtracks  
* _GET /tracks_ 
  *resource*: get_tracks  
* _GET /tracks/{track_id}_ 
  *resource*: get_trackstrack_id  
* _GET /users/{user_id}/likes/tracks_ 
  *resource*: get_usersuser_idlikestracks  
* _GET /users/{user_id}/tracks_ 
  *resource*: get_usersuser_idtracks  
* _GET /users_ 
  *resource*: get_users  
* _GET /users/{user_id}_ 
  *resource*: get_usersuser_id  
* _GET /users/{user_id}/web-profiles_ 
  *resource*: get_usersuser_idweb_profiles  
