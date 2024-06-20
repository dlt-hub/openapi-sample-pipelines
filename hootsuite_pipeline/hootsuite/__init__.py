from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="hootsuite_source", max_table_nesting=2)
def hootsuite_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # [OAuth2 Authorize](https://tools.ietf.org/html/rfc6749#section-3.1) endpoint.
            {
                "name": "oauth_2_authorize",
                "table_name": "auth",
                "endpoint": {
                    "path": "/oauth2/auth",
                    "params": {
                        "response_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "client_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "scope": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "redirect_uri": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a comment if it's been through the approvals workflow.
            {
                "name": "retrieve_comment",
                "table_name": "comment",
                "endpoint": {
                    "path": "/v1/comments/{commentId}",
                    "params": {
                        "commentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves Hootsuite teams using the SCIM 2.0 protocol. Support equals filtering on displayName.
            {
                "name": "get_scim_groups",
                "table_name": "group",
                "endpoint": {
                    "path": "/scim/v2/Groups",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "startIndex": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a Hootsuite team using the SCIM 2.0 protocol.
            {
                "name": "get_scim_group",
                "table_name": "group",
                "endpoint": {
                    "path": "/scim/v2/Groups/{groupId}",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Gets a message's prescreening review history.
            {
                "name": "get_message_history",
                "table_name": "history",
                "endpoint": {
                    "path": "/v1/messages/{messageId}/history",
                    "params": {
                        "messageId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the interactions between two users of a particular social network type such as direct messages, comments, and posts.  This API is only available to Enterprise users.
            {
                "name": "get",
                "table_name": "interaction",
                "endpoint": {
                    "path": "/v1/interactions/{socialNetworkType}",
                    "params": {
                        "socialNetworkType": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "socialNetworkId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "targetSocialNetworkId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves authenticated member.
            {
                "name": "retrieve_me",
                "table_name": "me",
                "endpoint": {
                    "path": "/v1/me",
                    "paginator": "auto",
                },
            },
            # Retrieves the status of a media upload to Hootsuite.
            {
                "name": "get_media",
                "table_name": "medium",
                "endpoint": {
                    "path": "/v1/media/{mediaId}",
                    "params": {
                        "mediaId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a member
            {
                "name": "retrieve_member",
                "table_name": "member",
                "endpoint": {
                    "path": "/v1/members/{memberId}",
                    "params": {
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the members in a team.
            {
                "name": "get_team_members",
                "table_name": "member",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/teams/{teamId}/members",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the members in an organization
            {
                "name": "retrieve_organization_members",
                "table_name": "member",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/members",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Outbound messages are messages that are scheduled or were previously sent. This endpoint returns outbound messages sorted by increasing scheduled send time. Messages pending approval, including those created by and/or actionable by the given user, will also be returned via this API.  Messages returned can be filtered by social profile or the current state of the message. If more than 50 results are returned a cursor will be automatically created to paginate the results.  Query Parameters must be [URL encoded](https://en.wikipedia.org/wiki/Percent-encoding). For example:  ``` ?startTime=2020-01-01T00%3A00%3A00Z &endTime=2020-01-15T17%3A55%3A01Z &socialProfileIds=1234 &state=SCHEDULED &limit=5 ```  To specify multiple social profiles, use the following [syntax](http://stackoverflow.com/questions/6243051/how-to-pass-an-array-within-a-query-string):  ``` ?socialProfileIds=1234&socialProfileIds=5678 ```
            {
                "name": "retrieve_messages",
                "table_name": "message",
                "endpoint": {
                    "path": "/v1/messages",
                    "params": {
                        "startTime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endTime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "socialProfileIds": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "includeUnscheduledReviewMsgs": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a message. A message is always associated with a single social profile. Messages might be unavailable for a brief time during upload to social networks.
            {
                "name": "retrieve_message",
                "table_name": "message",
                "endpoint": {
                    "path": "/v1/messages/{messageId}",
                    "params": {
                        "messageId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the organizations that the authenticated member is in.
            {
                "name": "retrieve_me_organizations",
                "table_name": "organization",
                "endpoint": {
                    "path": "/v1/me/organizations",
                    "paginator": "auto",
                },
            },
            # Retrieves the organizations that the member is in.
            {
                "name": "retrieve_member_organizations_by_id",
                "table_name": "organization",
                "endpoint": {
                    "path": "/v1/members/{memberId}/organizations",
                    "params": {
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves an organization member’s permissions for the organization.
            {
                "name": "retrieve_organization_member_organization_permissions",
                "table_name": "permission",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/members/{memberId}/permissions",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves team member's team permissions.
            {
                "name": "retrieve_organization_members_team_permissions",
                "table_name": "permission",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/teams/{teamId}/members/{memberId}/permissions",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves an organization member’s permissions for a social profile.
            {
                "name": "retrieve_organization_social_profile_permissions",
                "table_name": "permission",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/members/{memberId}/socialProfiles/{socialProfileId}/permissions",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "socialProfileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the configuration for all supported SCIM resource types
            {
                "name": "get_scim_resource_types",
                "table_name": "resource_type",
                "endpoint": {
                    "path": "/scim/v2/ResourceTypes",
                    "paginator": "auto",
                },
            },
            # Retrieves the social profiles that the authenticated user has access to.
            {
                "name": "get_social_profiles",
                "table_name": "social_profile",
                "endpoint": {
                    "path": "/v1/socialProfiles",
                    "paginator": "auto",
                },
            },
            # Retrieve a social profile. Requires BASIC_USAGE permission on the social profile.
            {
                "name": "get_social_profile",
                "table_name": "social_profile",
                "endpoint": {
                    "path": "/v1/socialProfiles/{socialProfileId}",
                    "params": {
                        "socialProfileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the social media profiles that the authenticated user has BASIC_USAGE permissions on.
            {
                "name": "get_my_social_profiles",
                "table_name": "social_profile",
                "endpoint": {
                    "path": "/v1/me/socialProfiles",
                    "paginator": "auto",
                },
            },
            # Retrieves the organization's social profiles that an organization team can access.
            {
                "name": "retrieve_organization_teams_social_profiles",
                "table_name": "social_profile",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/teams/{teamId}/socialProfiles",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the organization's social profiles that an organization member can access.
            {
                "name": "retrieve_organization_members_social_profiles",
                "table_name": "social_profile",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/members/{memberId}/socialProfiles",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of team IDs with access to a social profile. Requires BASIC_USAGE permission on the social profile or ORG_MANAGE_SOCIAL_PROFILE permission on the organization that owns the social profile.
            {
                "name": "get_social_profile_teams",
                "table_name": "team",
                "endpoint": {
                    "path": "/v1/socialProfiles/{socialProfileId}/teams",
                    "params": {
                        "socialProfileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of teams for a given organization.
            {
                "name": "get_organization_teams",
                "table_name": "team",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/teams",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the teams an organization member is in.
            {
                "name": "retrieve_organization_members_teams",
                "table_name": "team",
                "endpoint": {
                    "path": "/v1/organizations/{organizationId}/members/{memberId}/teams",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a team with a given team ID.
            {
                "name": "get_team",
                "table_name": "team",
                "endpoint": {
                    "path": "/v1/teams/{teamId}",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves Hootsuite users using the SCIM 2.0 protocol. Support equals filtering on username.
            {
                "name": "get_scim_users",
                "table_name": "user",
                "endpoint": {
                    "path": "/scim/v2/Users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "startIndex": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a Hootsuite user using the SCIM 2.0 protocol.
            {
                "name": "get_scim_user",
                "table_name": "user",
                "endpoint": {
                    "path": "/scim/v2/Users/{memberId}",
                    "params": {
                        "memberId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
