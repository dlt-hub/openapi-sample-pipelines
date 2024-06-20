# hootsuite pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/hootsuite.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /oauth2/auth_ 
  *resource*: oauth_2_authorize  
  *description*: [OAuth2 Authorize](https://tools.ietf.org/html/rfc6749#section-3.1) endpoint.
* _GET /v1/comments/{commentId}_ 
  *resource*: retrieve_comment  
  *description*: Retrieves a comment if it's been through the approvals workflow. 
* _GET /scim/v2/Groups_ 
  *resource*: get_scim_groups  
  *description*: Retrieves Hootsuite teams using the SCIM 2.0 protocol. Support equals filtering on displayName.
* _GET /scim/v2/Groups/{groupId}_ 
  *resource*: get_scim_group  
  *description*: Retrieves a Hootsuite team using the SCIM 2.0 protocol.
* _GET /v1/messages/{messageId}/history_ 
  *resource*: get_message_history  
  *description*: Gets a message's prescreening review history.
* _GET /v1/interactions/{socialNetworkType}_ 
  *resource*: get  
  *description*: Retrieves the interactions between two users of a particular social network type such as direct messages, comments, and posts.  This API is only available to Enterprise users. 
* _GET /v1/me_ 
  *resource*: retrieve_me  
  *description*: Retrieves authenticated member.
* _GET /v1/media/{mediaId}_ 
  *resource*: get_media  
  *description*: Retrieves the status of a media upload to Hootsuite.
* _GET /v1/members/{memberId}_ 
  *resource*: retrieve_member  
  *description*: Retrieves a member
* _GET /v1/organizations/{organizationId}/teams/{teamId}/members_ 
  *resource*: get_team_members  
  *description*: Retrieves the members in a team.
* _GET /v1/organizations/{organizationId}/members_ 
  *resource*: retrieve_organization_members  
  *description*: Retrieves the members in an organization
* _GET /v1/messages_ 
  *resource*: retrieve_messages  
  *description*: Outbound messages are messages that are scheduled or were previously sent. This endpoint returns outbound messages sorted by increasing scheduled send time. Messages pending approval, including those created by and/or actionable by the given user, will also be returned via this API.  Messages returned can be filtered by social profile or the current state of the message. If more than 50 results are returned a cursor will be automatically created to paginate the results.  Query Parameters must be [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding). For example:  ``` ?startTime=2020-01-01T00%3A00%3A00Z &endTime=2020-01-15T17%3A55%3A01Z &socialProfileIds=1234 &state=SCHEDULED &limit=5 ```  To specify multiple social profiles, use the following [syntax](http://stackoverflow.com/questions/6243051/how-to-pass-an-array-within-a-query-string):  ``` ?socialProfileIds=1234&socialProfileIds=5678 ``` 
* _GET /v1/messages/{messageId}_ 
  *resource*: retrieve_message  
  *description*: Retrieves a message. A message is always associated with a single social profile. Messages might be unavailable for a brief time during upload to social networks. 
* _GET /v1/me/organizations_ 
  *resource*: retrieve_me_organizations  
  *description*: Retrieves the organizations that the authenticated member is in.
* _GET /v1/members/{memberId}/organizations_ 
  *resource*: retrieve_member_organizations_by_id  
  *description*: Retrieves the organizations that the member is in.
* _GET /v1/organizations/{organizationId}/members/{memberId}/permissions_ 
  *resource*: retrieve_organization_member_organization_permissions  
  *description*: Retrieves an organization member’s permissions for the organization.
* _GET /v1/organizations/{organizationId}/teams/{teamId}/members/{memberId}/permissions_ 
  *resource*: retrieve_organization_members_team_permissions  
  *description*: Retrieves team member's team permissions.
* _GET /v1/organizations/{organizationId}/members/{memberId}/socialProfiles/{socialProfileId}/permissions_ 
  *resource*: retrieve_organization_social_profile_permissions  
  *description*: Retrieves an organization member’s permissions for a social profile.
* _GET /scim/v2/ResourceTypes_ 
  *resource*: get_scim_resource_types  
  *description*: Retrieves the configuration for all supported SCIM resource types
* _GET /v1/socialProfiles_ 
  *resource*: get_social_profiles  
  *description*: Retrieves the social profiles that the authenticated user has access to.
* _GET /v1/socialProfiles/{socialProfileId}_ 
  *resource*: get_social_profile  
  *description*: Retrieve a social profile. Requires BASIC_USAGE permission on the social profile.
* _GET /v1/me/socialProfiles_ 
  *resource*: get_my_social_profiles  
  *description*: Retrieves the social media profiles that the authenticated user has BASIC_USAGE permissions on.
* _GET /v1/organizations/{organizationId}/teams/{teamId}/socialProfiles_ 
  *resource*: retrieve_organization_teams_social_profiles  
  *description*: Retrieves the organization's social profiles that an organization team can access.
* _GET /v1/organizations/{organizationId}/members/{memberId}/socialProfiles_ 
  *resource*: retrieve_organization_members_social_profiles  
  *description*: Retrieves the organization's social profiles that an organization member can access.
* _GET /v1/socialProfiles/{socialProfileId}/teams_ 
  *resource*: get_social_profile_teams  
  *description*: Retrieves a list of team IDs with access to a social profile. Requires BASIC_USAGE permission on the social profile or ORG_MANAGE_SOCIAL_PROFILE permission on the organization that owns the social profile.
* _GET /v1/organizations/{organizationId}/teams_ 
  *resource*: get_organization_teams  
  *description*: Retrieves a list of teams for a given organization.
* _GET /v1/organizations/{organizationId}/members/{memberId}/teams_ 
  *resource*: retrieve_organization_members_teams  
  *description*: Retrieves the teams an organization member is in.
* _GET /v1/teams/{teamId}_ 
  *resource*: get_team  
  *description*: Retrieves a team with a given team ID.
* _GET /scim/v2/Users_ 
  *resource*: get_scim_users  
  *description*: Retrieves Hootsuite users using the SCIM 2.0 protocol. Support equals filtering on username.
* _GET /scim/v2/Users/{memberId}_ 
  *resource*: get_scim_user  
  *description*: Retrieves a Hootsuite user using the SCIM 2.0 protocol.
