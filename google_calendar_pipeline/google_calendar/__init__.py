from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_calendar_source", max_table_nesting=2)
def google_calendar_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Returns the rules in the access control list for the calendar.
            {
                "name": "calendar_acl_list",
                "table_name": "acl_rule",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/calendars/{calendarId}/acl",
                    "params": {
                        "calendarId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "showDeleted": "OPTIONAL_CONFIG",
                        # "syncToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns an access control rule.
            {
                "name": "calendar_acl_get",
                "table_name": "acl_rule",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/calendars/{calendarId}/acl/{ruleId}",
                    "params": {
                        "ruleId": {
                            "type": "resolve",
                            "resource": "calendar_acl_list",
                            "field": "id",
                        },
                        "calendarId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns metadata for a calendar.
            {
                "name": "calendar_calendars_get",
                "table_name": "calendar",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/calendars/{calendarId}",
                    "params": {
                        "calendarId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the calendars on the user's calendar list.
            {
                "name": "calendar_calendar_list_list",
                "table_name": "calendar_list_entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/users/me/calendarList",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "minAccessRole": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "showDeleted": "OPTIONAL_CONFIG",
                        # "showHidden": "OPTIONAL_CONFIG",
                        # "syncToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a calendar from the user's calendar list.
            {
                "name": "calendar_calendar_list_get",
                "table_name": "calendar_list_entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/me/calendarList/{calendarId}",
                    "params": {
                        "calendarId": {
                            "type": "resolve",
                            "resource": "calendar_calendar_list_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the color definitions for calendars and events.
            {
                "name": "calendar_colors_get",
                "table_name": "colors",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/colors",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the events.list method using the iCalUID parameter.
            {
                "name": "calendar_events_get",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/calendars/{calendarId}/events/{eventId}",
                    "params": {
                        "calendarId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "eventId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "alwaysIncludeEmail": "OPTIONAL_CONFIG",
                        # "maxAttendees": "OPTIONAL_CONFIG",
                        # "timeZone": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns events on the specified calendar.
            {
                "name": "calendar_events_list",
                "table_name": "event_reminder",
                "endpoint": {
                    "data_selector": "defaultReminders",
                    "path": "/calendars/{calendarId}/events",
                    "params": {
                        "calendarId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "alwaysIncludeEmail": "OPTIONAL_CONFIG",
                        # "eventTypes": "OPTIONAL_CONFIG",
                        # "iCalUID": "OPTIONAL_CONFIG",
                        # "maxAttendees": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "privateExtendedProperty": "OPTIONAL_CONFIG",
                        # "q": "OPTIONAL_CONFIG",
                        # "sharedExtendedProperty": "OPTIONAL_CONFIG",
                        # "showDeleted": "OPTIONAL_CONFIG",
                        # "showHiddenInvitations": "OPTIONAL_CONFIG",
                        # "singleEvents": "OPTIONAL_CONFIG",
                        # "syncToken": "OPTIONAL_CONFIG",
                        # "timeMax": "OPTIONAL_CONFIG",
                        # "timeMin": "OPTIONAL_CONFIG",
                        # "timeZone": "OPTIONAL_CONFIG",
                        # "updatedMin": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns instances of the specified recurring event.
            {
                "name": "calendar_events_instances",
                "table_name": "event_reminder",
                "endpoint": {
                    "data_selector": "defaultReminders",
                    "path": "/calendars/{calendarId}/events/{eventId}/instances",
                    "params": {
                        "calendarId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "eventId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "alwaysIncludeEmail": "OPTIONAL_CONFIG",
                        # "maxAttendees": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "originalStart": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "showDeleted": "OPTIONAL_CONFIG",
                        # "timeMax": "OPTIONAL_CONFIG",
                        # "timeMin": "OPTIONAL_CONFIG",
                        # "timeZone": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all user settings for the authenticated user.
            {
                "name": "calendar_settings_list",
                "table_name": "setting",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/users/me/settings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "syncToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single user setting.
            {
                "name": "calendar_settings_get",
                "table_name": "setting",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/me/settings/{setting}",
                    "params": {
                        "setting": {
                            "type": "resolve",
                            "resource": "calendar_settings_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "alt": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "userIp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
