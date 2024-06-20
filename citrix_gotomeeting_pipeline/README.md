# citrix_gotomeeting pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/citrix_gotomeeting.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /groups/{groupKey}/attendees_ 
  *resource*: get_groupsgroup_keyattendees  
  *description*: Returns all attendees for all meetings within specified date range held by organizers within the specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.
* _GET /meetings/{meetingId}/attendees_ 
  *resource*: get_meetingsmeeting_idattendees  
  *description*: List all attendees for specified meetingId of historical meeting. The historical meetings can be fetched using 'Get historical meetings', 'Get historical meetings by organizer', and 'Get historical meetings by group'. For users with the admin role this call returns attendees for any meeting. For any other user the call will return attendees for meetings on which the user is a valid organizer.
* _GET /organizers/{organizerKey}/attendees_ 
  *resource*: get_organizersorganizer_keyattendees  
  *description*: Lists all attendees for all meetings within a specified date range for a specified organizer. This API call is only available to users with the admin role.
* _GET /groups_ 
  *resource*: get_groups  
  *description*: List all groups for an account. This API call is only available to users with the admin role.
* _GET /groups/{groupKey}/historicalMeetings_ 
  *resource*: get_groupsgroup_keyhistorical_meetings  
  *description*: Get historical meetings for the specified group that started within the specified date/time range. This API call is only available to users with the admin role. This API call is restricted to groups with a maximum of 50 organizers. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.
* _GET /historicalMeetings_ 
  *resource*: get_historical_meetings  
  *description*: Get historical meetings for the currently authenticated organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.
* _GET /organizers/{organizerKey}/historicalMeetings_ 
  *resource*: get_organizersorganizer_keyhistorical_meetings  
  *description*: Get historical meetings for the specified organizer that started within the specified date/time range. Remark: Meetings which are still ongoing at the time of the request are NOT contained in the result array.
* _GET /groups/{groupKey}/meetings_ 
  *resource*: get_groupsgroup_keymeetings  
  *description*: DEPRECATED: Please use the new API calls 'Get historical meetings by group' and 'Get upcoming meetings by group'. Get meetings for a specified group. Additional filters can be used to view only meetings within a specified date range. This API call is only available to users with the admin role.
* _GET /meetings_ 
  *resource*: get_meetings  
  *description*: DEPRECATED: Please use the new API calls 'Get historical meetings' and 'Get upcoming meetings'.  Gets historical meetings for the current authenticated organizer. Requires date range for filtering results to only meetings within specified dates. History searches will contain the parameter 'meetingInstanceKey' which is used in conjunction with the call 'Get Attendees by Meeting' to get attendee information for a past meeting.
* _GET /meetings/{meetingId}_ 
  *resource*: get_meetingsmeeting_id  
  *description*: Returns the meeting details for the specified meeting.
* _GET /organizers/{organizerKey}/meetings_ 
  *resource*: get_organizersorganizer_keymeetings  
  *description*: DEPRECATED: Please use the new API calls 'Get historical meetings by organizer' and 'Get upcoming meetings by organizer'. Gets future (scheduled) or past (history) meetings for a specified organizer. Include 'history=true' and the past start and end dates in the URL to retrieve past meetings. Enter 'scheduled=true' (without dates) to get scheduled meetings.
* _GET /groups/{groupKey}/organizers_ 
  *resource*: get_groupsgroup_keyorganizers  
  *description*: Returns all the organizers within a specific group. This API call is only available to users with the admin role.
* _GET /organizers_ 
  *resource*: get_organizers  
  *description*: Gets the individual organizer specified by the organizer's email address. If an email address is not specified, all organizers are returned. This API call is only available to users with the admin role.
* _GET /organizers/{organizerKey}_ 
  *resource*: get_organizersorganizer_key  
  *description*: Returns the individual organizer specified by the key. This API call is only available to users with the admin role. Non-admin users can only make this call for their own organizerKey.
* _GET /meetings/{meetingId}/start_ 
  *resource*: get_meetingsmeeting_idstart  
  *description*: Returns a host URL that can be used to start a meeting. When this URL is opened in a web browser, the GoToMeeting client will be downloaded and launched and the meeting will start. The end user is not required to login to a client.
* _GET /groups/{groupKey}/upcomingMeetings_ 
  *resource*: get_groupsgroup_keyupcoming_meetings  
  *description*: Get upcoming meetings for a specified group. This API call is only available to users with the admin role. This API call can be used only for groups with maximum 50 organizers.
* _GET /organizers/{organizerKey}/upcomingMeetings_ 
  *resource*: get_organizersorganizer_keyupcoming_meetings  
  *description*: Get upcoming meetings for a specified organizer. This API call is only available to users with the admin role.
* _GET /upcomingMeetings_ 
  *resource*: get_upcoming_meetings  
  *description*: Gets upcoming meetings for the current authenticated organizer.
