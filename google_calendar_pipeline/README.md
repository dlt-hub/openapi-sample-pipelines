# google_calendar pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/google_calendar.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /calendars/{calendarId}/acl_ 
  *resource*: calendar_acl_list  
  *description*: Returns the rules in the access control list for the calendar.
* _GET /calendars/{calendarId}/acl/{ruleId}_ 
  *resource*: calendar_acl_get  
  *description*: Returns an access control rule.
* _GET /calendars/{calendarId}_ 
  *resource*: calendar_calendars_get  
  *description*: Returns metadata for a calendar.
* _GET /users/me/calendarList_ 
  *resource*: calendar_calendar_list_list  
  *description*: Returns the calendars on the user's calendar list.
* _GET /users/me/calendarList/{calendarId}_ 
  *resource*: calendar_calendar_list_get  
  *description*: Returns a calendar from the user's calendar list.
* _GET /colors_ 
  *resource*: calendar_colors_get  
  *description*: Returns the color definitions for calendars and events.
* _GET /calendars/{calendarId}/events/{eventId}_ 
  *resource*: calendar_events_get  
  *description*: Returns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the events.list method using the iCalUID parameter.
* _GET /calendars/{calendarId}/events_ 
  *resource*: calendar_events_list  
  *description*: Returns events on the specified calendar.
* _GET /calendars/{calendarId}/events/{eventId}/instances_ 
  *resource*: calendar_events_instances  
  *description*: Returns instances of the specified recurring event.
* _GET /users/me/settings_ 
  *resource*: calendar_settings_list  
  *description*: Returns all user settings for the authenticated user.
* _GET /users/me/settings/{setting}_ 
  *resource*: calendar_settings_get  
  *description*: Returns a single user setting.
