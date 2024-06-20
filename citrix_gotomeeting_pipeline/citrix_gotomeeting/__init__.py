from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="citrix_gotomeeting_source", max_table_nesting=2)
def citrix_gotomeeting_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Returns all attendees for all meetings within specified date range held by organizers within the specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.
            {
                "name": "get_groupsgroup_keyattendees",
                "table_name": "attendee",
                "endpoint": {
                    "path": "/groups/{groupKey}/attendees",
                    "params": {
                        "groupKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List all attendees for specified meetingId of historical meeting. The historical meetings can be fetched using 'Get historical meetings', 'Get historical meetings by organizer', and 'Get historical meetings by group'. For users with the admin role this call returns attendees for any meeting. For any other user the call will return attendees for meetings on which the user is a valid organizer.
            {
                "name": "get_meetingsmeeting_idattendees",
                "table_name": "attendee",
                "endpoint": {
                    "path": "/meetings/{meetingId}/attendees",
                    "params": {
                        "meetingId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists all attendees for all meetings within a specified date range for a specified organizer. This API call is only available to users with the admin role.
            {
                "name": "get_organizersorganizer_keyattendees",
                "table_name": "attendee",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/attendees",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all groups for an account. This API call is only available to users with the admin role.
            {
                "name": "get_groups",
                "table_name": "group",
                "endpoint": {
                    "path": "/groups",
                    "paginator": "auto",
                },
            },
            # Get historical meetings for the specified group that started within the specified date/time range. This API call is only available to users with the admin role. This API call is restricted to groups with a maximum of 50 organizers. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.
            {
                "name": "get_groupsgroup_keyhistorical_meetings",
                "table_name": "historical_meeting",
                "endpoint": {
                    "path": "/groups/{groupKey}/historicalMeetings",
                    "params": {
                        "groupKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get historical meetings for the currently authenticated organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.
            {
                "name": "get_historical_meetings",
                "table_name": "historical_meeting",
                "endpoint": {
                    "path": "/historicalMeetings",
                    "params": {
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get historical meetings for the specified organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.
            {
                "name": "get_organizersorganizer_keyhistorical_meetings",
                "table_name": "historical_meeting",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/historicalMeetings",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # DEPRECATED: Please use the new API calls 'Get historical meetings by group' and 'Get upcoming meetings by group'. Get meetings for a specified group. Additional filters can be used to view only meetings within a specified date range. This API call is only available to users with the admin role.
            {
                "name": "get_groupsgroup_keymeetings",
                "table_name": "meeting",
                "endpoint": {
                    "path": "/groups/{groupKey}/meetings",
                    "params": {
                        "groupKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "history": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # DEPRECATED: Please use the new API calls 'Get historical meetings' and 'Get upcoming meetings'.  Gets historical meetings for the current authenticated organizer. Requires date range for filtering results to only meetings within specified dates. History searches will contain the parameter 'meetingInstanceKey' which is used in conjunction with the call 'Get Attendees by Meeting' to get attendee information for a past meeting.
            {
                "name": "get_meetings",
                "table_name": "meeting",
                "endpoint": {
                    "path": "/meetings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "history": "OPTIONAL_CONFIG",
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the meeting details for the specified meeting.
            {
                "name": "get_meetingsmeeting_id",
                "table_name": "meeting",
                "endpoint": {
                    "path": "/meetings/{meetingId}",
                    "params": {
                        "meetingId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # DEPRECATED: Please use the new API calls 'Get historical meetings by organizer' and 'Get upcoming meetings by organizer'. Gets future (scheduled) or past (history) meetings for a specified organizer. Include 'history=true' and the past start and end dates in the URL to retrieve past meetings. Enter 'scheduled=true' (without dates) to get scheduled meetings.
            {
                "name": "get_organizersorganizer_keymeetings",
                "table_name": "meeting",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/meetings",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "scheduled": "OPTIONAL_CONFIG",
                        # "history": "OPTIONAL_CONFIG",
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all the organizers within a specific group. This API call is only available to users with the admin role.
            {
                "name": "get_groupsgroup_keyorganizers",
                "table_name": "organizer",
                "endpoint": {
                    "path": "/groups/{groupKey}/organizers",
                    "params": {
                        "groupKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Gets the individual organizer specified by the organizer's email address. If an email address is not specified, all organizers are returned. This API call is only available to users with the admin role.
            {
                "name": "get_organizers",
                "table_name": "organizer",
                "endpoint": {
                    "path": "/organizers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "email": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the individual organizer specified by the key. This API call is only available to users with the admin role. Non-admin users can only make this call for their own organizerKey.
            {
                "name": "get_organizersorganizer_key",
                "table_name": "organizer",
                "endpoint": {
                    "path": "/organizers/{organizerKey}",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a host URL that can be used to start a meeting. When this URL is opened in a web browser, the GoToMeeting client will be downloaded and launched and the meeting will start. The end user is not required to login to a client.
            {
                "name": "get_meetingsmeeting_idstart",
                "table_name": "start",
                "endpoint": {
                    "path": "/meetings/{meetingId}/start",
                    "params": {
                        "meetingId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get upcoming meetings for a specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.
            {
                "name": "get_groupsgroup_keyupcoming_meetings",
                "table_name": "upcoming_meeting",
                "endpoint": {
                    "path": "/groups/{groupKey}/upcomingMeetings",
                    "params": {
                        "groupKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get upcoming meetings for a specified organizer. This API call is only available to users with the admin role.
            {
                "name": "get_organizersorganizer_keyupcoming_meetings",
                "table_name": "upcoming_meeting",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/upcomingMeetings",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Gets upcoming meetings for the current authenticated organizer.
            {
                "name": "get_upcoming_meetings",
                "table_name": "upcoming_meeting",
                "endpoint": {
                    "path": "/upcomingMeetings",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
