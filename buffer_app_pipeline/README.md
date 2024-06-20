# buffer_app pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/buffer_app.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /info/configuration{mediaTypeExtension}_ 
  *resource*: configurationmedia_type_extension  
  *description*: Returns an object with the current configuration that Buffer is using, including supported services, their icons and the varying limits of character and schedules.
* _GET /updates/{id}/interactions{mediaTypeExtension}_ 
  *resource*: interactionsmedia_type_extension  
  *description*: Returns the detailed information on individual interactions with the social media update such as favorites, retweets and likes. 
* _GET /profiles/{id}/updates/pending{mediaTypeExtension}_ 
  *resource*: pendingmedia_type_extension  
  *description*: "Returns an array of updates that are currently in the buffer for an individual social media profile. 
* _GET /profiles/{id}{mediaTypeExtension}_ 
  *resource*: profile  
  *description*: Returns details of the single specified social media profile.
* _GET /profiles{mediaTypeExtension}_ 
  *resource*: profilesmedia_type_extension  
  *description*: Returns an array of social media profiles connected to a users account.
* _GET /profiles/{id}/schedules{mediaTypeExtension}_ 
  *resource*: schedulesmedia_type_extension  
  *description*: Returns details of the posting schedules associated with a social media profile.
* _GET /profiles/{id}/updates/sent{mediaTypeExtension}_ 
  *resource*: sentmedia_type_extension  
  *description*: Returns an array of updates that have been sent from the buffer for an individual social media profile. 
* _GET /links/shares{mediaTypeExtension}_ 
  *resource*: sharesmedia_type_extension  
  *description*: Returns an object with a the numbers of shares a link has had using Buffer.
* _GET /updates/{id}{mediaTypeExtension}_ 
  *resource*: update  
  *description*: Returns a single social media update.
* _GET /user{mediaTypeExtension}_ 
  *resource*: usermedia_type_extension  
  *description*: Returns a single user.
