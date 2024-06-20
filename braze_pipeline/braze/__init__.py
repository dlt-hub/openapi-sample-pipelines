from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="braze_source", max_table_nesting=2)
def braze_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # This endpoint allows you to retrieve a daily series of various stats for a campaign over time. Data returned includes how many messages were sent, opened, clicked, converted, etc., broken down by message channel.   ### Components Used -[Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Responses  #### Multi-Channel Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) date as ISO 8601 date,             "messages" : {                 "ios_push" : [                     {                       "variation_name": "iOS_Push",                       "sent" : (int),                       "direct_opens" : (int),                       "total_opens" : (int),                       "bounces" : (int),                       "body_clicks" : (int)                       "revenue": 0,                       "unique_recipients": 1,                       "conversions": 0,                       "conversions_by_send_time": 0,                       "conversions1": 0,                       "conversions1_by_send_time": 0,                       "conversions2": 0,                       "conversions2_by_send_time": 0,                       "conversions3": 0,                       "conversions3_by_send_time": 0,                       "carousel_slide_[NUM]_[TITLE]_click": (optional, int),                       "notif_button_[NUM]_[TITLE]_click": (optional, int)                     }                 ],                 "android_push" : [                     {                       "sent" : (int),                       "direct_opens" : (int),                       "total_opens" : (int),                       "bounces" : (int),                       "body_clicks" : (int)                     }                 ],                 "webhook": [                     {                       "sent": (int),                       "errors": (int)                     }                 ],                 "email" : [                     {                       "sent": (int),                       "opens": (int),                       "unique_opens": (int),                       "clicks": (int),                       "unique_clicks": (int),                       "unsubscribes": (int),                       "bounces": (int),                       "delivered": (int),                       "reported_spam": (int)                     }                 ],                 "sms" : [                   {                     "sent": (int),                     "delivered": (int),                     "undelivered": (int),                     "delivery_failed": (int)                   }                 ]               },            "conversions_by_send_time": (optional, int),            "conversions1_by_send_time": (optional, int),            "conversions2_by_send_time": (optional, int),            "conversions3_by_send_time": (optional, int),            "conversions": (int),            "conversions1": (optional, int),            "conversions2": (optional, int),            "conversions3": (optional, int),            "unique_recipients": (int),            "revenue": (optional, float)         },         ...     ],     ... } ```  #### Multivariate Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "data" : [         {             "time" : (string) date as ISO 8601 date,             "conversions" : (int),             "revenue": (float),             "conversions_by_send_time": (int),             "messages" : {                "trigger_in_app_message": [{       				"variation_name": (optional, string),       				"impressions": (int),       				"clicks": (int),       				"first_button_clicks": (int),       				"second_button_clicks": (int),       				"revenue": (optional, float),,       				"unique_recipients": (int),       				"conversions": (optional, int),       				"conversions_by_send_time": (optional, int),       				"conversions1": (optional, int),       				"conversions1_by_send_time": (optional, int),       				"conversions2": (optional, int),       				"conversions2_by_send_time": (optional, int),       				"conversions3": (optional, int),       				"conversions3_by_send_time": (optional, int)       			}, {       				"variation_name": (optional, string),       				"impressions": (int),       				"clicks": (int),       				"first_button_clicks": (int),       				"second_button_clicks": (int),       				"revenue": (optional, float),,       				"unique_recipients": (int),       				"conversions": (optional, int),       				"conversions_by_send_time": (optional, int),       				"conversions1": (optional, int),       				"conversions1_by_send_time": (optional, int),       				"conversions2": (optional, int),       				"conversions2_by_send_time": (optional, int),       				"conversions3": (optional, int).       				"conversions3_by_send_time": (optional, int)       			}, {       				"variation_name": (optional, string),       				"revenue": (optional, float),,       				"unique_recipients": (int),       				"conversions": (optional, int),       				"conversions_by_send_time": (optional, int),       				"conversions1": (optional, int),       				"conversions1_by_send_time": (optional, int),       				"conversions2": (optional, int),       				"conversions2_by_send_time": (optional, int),       				"conversions3": (optional, int),       				"conversions3_by_send_time": (optional, int),       				"enrolled": (optional, int)       			}]       		},       		"conversions_by_send_time": (optional, int),       		"conversions1_by_send_time": (optional, int),       		"conversions2_by_send_time": (optional, int),       		"conversions3_by_send_time": (optional, int),       		"conversions": (optional, int,       		"conversions1": (optional, int),       		"conversions2": (optional, int),       		"conversions3": (optional, int),       		"unique_recipients": (int),       		"revenue": (optional, float)          }],          ... } ```  Possible message types are `email`, `in_app_message`, `webhook`, `android_push`, `apple_push`, `kindle_push`, `web_push`, `windows_phone8_push`, and `windows_universal_push`. All push message types will have the same statistics shown for `android_push` above.
            {
                "name": "campaigns_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/campaigns/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "campaign_id": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to export time series data for a Canvas.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   "data": {     "name": (string) Canvas name,     "stats": [       {         "time": (string) date as ISO 8601 date,         "total_stats": {           "revenue": (float),           "conversions": (int),           "conversions_by_entry_time": (int),           "entries": (int)         },         "variant_stats": (optional) {           "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {             "name": (string) name of variant,             "revenue": (int),             "conversions": (int),             "conversions_by_entry_time": (int),             "entries": (int)           },           ... (more variants)         },         "step_stats": (optional) {           "00000000-0000-0000-0000-0000000000000": (API identifier for step) {             "name": (string) name of step,             "revenue": (float),             "conversions": (int),             "conversions_by_entry_time": (int),             "messages": {               "email": [                 {                   "sent": (int),                   "opens": (int),                   "unique_opens": (int),                   "clicks": (int),                   ... (more stats)                 }               ],               ... (more channels)             }           },           ... (more steps)         }       },       ... (more stats by time)     ]   },   "message": (required, string) the status of the export, returns 'success' when completed without errors } ```
            {
                "name": "canvas_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/canvas/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "canvas_id": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "starting_at": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "include_variant_breakdown": "OPTIONAL_CONFIG",
                        # "include_step_breakdown": "OPTIONAL_CONFIG",
                        # "include_deleted_step_data": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",             "count" : (int)         },         ...     ] } ```  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
            {
                "name": "events_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/events/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "event": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "unit": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "app_id": "OPTIONAL_CONFIG",
                        # "segment_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of engagement stats for a card over time.  ### Components Used - [Card ID](https://www.braze.com/docs/api/identifier_types/) - [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",             "clicks" : (int) ,             "impressions" : (int),             "unique_clicks" : (int),             "unique_impressions" : (int)         },         ...     ] } ```
            {
                "name": "feed_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/feed/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "card_id": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "unit": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) date as ISO 8601 date,             "dau" : (int)         },         ...     ] } ```
            {
                "name": "kpi_dau_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/kpi/dau/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "app_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) date as ISO 8601 date,             "mau" : (int)         },         ...     ] } ```
            {
                "name": "kpi_mau_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/kpi/mau/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "app_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of the total number of new users on each date.   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) date as ISO 8601 date,             "new_users" : (int)         },         ...     ] } ```
            {
                "name": "kpi_new_users_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/kpi/new_users/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "app_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) date as ISO 8601 date,             "uninstalls" : (int)         },         ...     ] } ```
            {
                "name": "kpi_uninstalls_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/kpi/uninstalls/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "app_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) date as ISO 8601 date,             "size" : (int) size of the segment on that date         },         ...     ] } ```
            {
                "name": "segments_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/segments/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "segment_id": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a daily series of various stats for a tracked `send_id`. Braze stores send analytics for 14 days after the send.  Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.  > The `send_id` is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the `send_id` is included in response for the `messages/send`, `messages/schedule`, `campaign/trigger/send` and `campaign/trigger/schedule` endpoints.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)  ### Send Analytics Endpoint API Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {             "variation_name": (string) variation name,             "sent": (int) the number of sends,             "delivered": (int) the number of messages successfully delivered,             "undelivered": (int) the number of undelivered,             "delivery_failed": (int) the number of rejected,             "direct_opens": (int) the number of direct opens,             "total_opens": (int) the number of total opens,             "bounces": (int) the number of bounces,             "body_clicks": (int) the number of body clicks,             "revenue": (float) the number of dollars of revenue (USD),             "unique_recipients": (int) the number of unique recipients,             "conversions": (int) the number of conversions,             "conversions_by_send_time": (int) the number of conversions,             "conversions1": (int, optional) the number of conversions for the second conversion event,             "conversions1_by_send_time": (int, optional) the number of conversions for the second conversion event by send time,             "conversions2": (int, optional) the number of conversions for the third conversion event,             "conversions2_by_send_time": (int, optional) the number of conversions for the third conversion event by send time,             "conversions3": (int, optional) the number of conversions for the fourth conversion event,             "conversions3_by_send_time": (int, optional) the number of conversions for the fourth conversion event by send time           }         ]       },       "conversions_by_send_time": 0,       "conversions1_by_send_time": 0,       "conversions2_by_send_time": 0,       "conversions3_by_send_time": 0,       "conversions": 0,       "conversions1": 0,       "conversions2": 0,       "conversions3": 0,       "unique_recipients": 1,       "revenue": 0     }   ],   "message": "success" } ```
            {
                "name": "sends_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/sends/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "campaign_id": "OPTIONAL_CONFIG",
                        # "send_id": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.  ### Components Used - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "data" : [         {             "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",             "sessions" : (int)         },         ...     ] } ```
            {
                "name": "sessions_data_series",
                "table_name": "data_series",
                "endpoint": {
                    "path": "/sessions/data_series",
                    "params": {
                        # the parameters below can optionally be configured
                        # "length": "OPTIONAL_CONFIG",
                        # "unit": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "app_id": "OPTIONAL_CONFIG",
                        # "segment_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas' results.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   "data": {     "name": (string) Canvas name,     "total_stats": {       "revenue": (float),       "conversions": (int),       "conversions_by_entry_time": (int),       "entries": (int)     },     "variant_stats": (optional) {       "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {         "name": (string) name of variant,         "revenue": (float),         "conversions": (int),         "entries": (int)       },       ... (more variants)     },     "step_stats": (optional) {       "00000000-0000-0000-0000-0000000000000": (API identifier for step) {         "name": (string) name of step,         "revenue": (float),         "conversions": (int),         "conversions_by_entry_time": (int),         "messages": {           "android_push": (name of channel) [             {               "sent": (int),               "opens": (int),               "influenced_opens": (int),               "bounces": (int)               ... (more stats for channel)             }           ],           ... (more channels)         }       },       ... (more steps)     }   },   "message": (required, string) the status of the export, returns 'success' when completed without errors } ```
            {
                "name": "canvas_data_summary",
                "table_name": "data_summary",
                "endpoint": {
                    "path": "/canvas/data_summary",
                    "params": {
                        # the parameters below can optionally be configured
                        # "canvas_id": "OPTIONAL_CONFIG",
                        # "ending_at": "OPTIONAL_CONFIG",
                        # "starting_at": "OPTIONAL_CONFIG",
                        # "length": "OPTIONAL_CONFIG",
                        # "include_variant_breakdown": "OPTIONAL_CONFIG",
                        # "include_step_breakdown": "OPTIONAL_CONFIG",
                        # "include_deleted_step_data": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the `campaign_id`.   > The campaign_id for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard or you can use the Campaign List Endpoint.  ### Components Used - [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)   ### Campaign Details Endpoint API Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "created_at" : (string) date created as ISO 8601 date,     "updated_at" : (string) date last updated as ISO 8601 date,     "archived": (boolean) whether this Campaign is archived,     "draft": (boolean) whether this Campaign is a draft,     "name" : (string) campaign name,     "description" : (string) campaign description,     "schedule_type" : (string) type of scheduling action,     "channels" : (array) list of channels to send via,     "first_sent" : (string) date and hour of first sent as ISO 8601 date,     "last_sent" : (string) date and hour of last sent as ISO 8601 date,     "tags" : (array) tag names associated with the campaign,     "messages": {         "message_variation_id": (string) { // <=This is the actual id             "channel": (string) channel type of the message (as in, "email", "ios_push", "webhook", "content_card", "in-app_message", "sms"),             "name": (string) name of the message in the Dashboard (eg., "Variation 1")             ... channel-specific fields for this message, see below ...         }     },     "conversion_behaviors": (array) conversion event behaviors assigned to the campaign (see below) } ```  #### Messages  The `messages` response will contain information about each message. Example message responses for channels are below:  ##### Push Channels  ```json {     "channel": (string) description of the channel, such as "ios_push" or "android_push"     "alert": (string) alert body text,     "extras": (hash) any key value pairs provided } ```  ##### Email Channel  ```json {     "channel": "email",     "subject": (string) subject,     "body": (string) HTML body,     "from": (string) from address and display name,     "reply_to": (string) reply-to for message, if different than "from" address,     "title": (string) name of the email,     "extras": (hash) any key value pairs provided } ```  ##### Content Card Channel  ```json {     "channel": "content_cards",     "name": (string) name of variant,     "extras": (hash) any key value pairs provided; only present if at least one key-value pair has been set } ```  ##### Webhook Channel  ```json {     "channel": "webhook",     "url": (string) url for webhook,     "body": (string) payload body,     "type": (string) body content type,     "headers": (hash) specified request headers,     "method": (string) HTTP method (e.g., "POST" or "GET"), } ```  ##### SMS Channel  ```json {   "channel": "sms",   "body": (string) payload body,   "from": (string) list of numbers associated with the subscription group,   "subscription_group_id": (string) API id of the subscription group targeted in the SMS message } ```  ##### Control Messages  ```json {     "channel": (string) description of the channel that the control is for,     "type": "control" } ```  #### Conversion Behaviors  The `conversion_behaviors` array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. Example conversion event behavior responses for are below:  ##### Clicks Email  ```json {     "type": "Clicks Email",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } ```  ##### Opens Email  ```json {     "type": "Opens Email",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } ```  ##### Makes Purchase (any purchase)  ```json {     "type": "Makes Any Purchase",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours } ```  ##### Makes Purchase (specific product)  ```json {     "type": "Makes Specific Purchase",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     "product": (string) name of the product, i.e. - "Feline Body Armor" } ```  ##### Performs Custom Event  ```json {     "type": "Performs Custom Event",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     "custom_event_name": (string) name of the event, i.e. - "Used Feline Body Armor" } ```  ##### Upgrades App  ```json {     "type": "Upgrades App",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     "app_ids": (array|null) array of app ids, i.e. - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI } ```  ##### Uses App  ```json {     "type": "Starts Session",     "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,     "app_ids": (array|null) array of app ids, i.e. - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI } ```
            {
                "name": "campaigns_details",
                "table_name": "detail",
                "endpoint": {
                    "path": "/campaigns/details",
                    "params": {
                        # the parameters below can optionally be configured
                        # "campaign_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to export metadata about a Canvas, such as its name, when it was created, its current status, and more.  ### Components Used - [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   "created_at": (string) date created as ISO 8601 date,   "updated_at": (string) date updated as ISO 8601 date,   "name": (string) Canvas name,   "description": (string) Canvas description,   "archived": (boolean) whether this Canvas is archived,   "draft": (boolean) whether this Canvas is a draft,   "schedule_type": (string) type of scheduling action,   "first_entry": (string) date of first entry as ISO 8601 date,   "last_entry": (string) date of last entry as ISO 8601 date,   "channels": (array of strings) step channels used with Canvas,   "variants": [     {       "name": (string) name of variant,       "id": (string) API identifier of the variant,       "first_step_ids": (array of strings) API identifiers for first steps in variant,       "first_step_id": (string) API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)     },     ... (more variations)   ],   "tags": (array of strings) tag names associated with the Canvas,   "steps": [     {       "name": (string) name of step,       "id": (string) API identifier of the step,       "next_step_ids": (array of strings) API identifiers of steps following step,       "channels": (array of strings) channels used in step,       "messages": {           "message_variation_id": (string) {  // <=This is the actual id               "channel": (string) channel type of the message (eg., "email"),               ... channel-specific fields for this message, see Campaign Details Endpoint API Response for example message responses ...           }       }     },     ... (more steps)   ],   "message": (required, string) the status of the export, returns 'success' when completed without errors } ```
            {
                "name": "canvas_details",
                "table_name": "detail",
                "endpoint": {
                    "path": "/canvas/details",
                    "params": {
                        # the parameters below can optionally be configured
                        # "canvas_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve relevant information on the card, which can be identified by the `card_id`.  ### Components Used - [Card ID](https://www.braze.com/docs/api/identifier_types/) - [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) The status of the export, returns 'success' when completed without errors,     "created_at" : (string) Date created as ISO 8601 date,     "updated_at" : (string) Date last updated as ISO 8601 date,     "name" : (string) Card name,     "publish_at" : (string) Date card was published as ISO 8601 date,     "end_at" : (string) Date card will stop displaying for users as ISO 8601 date,     "tags" : (array) Tag names associated with the card,     "title" : (string) Title of the card,     "image_url" : (string) Image URL used by this card,     "extras" : (dictionary) Dictionary containing key-value pair data attached to this card,     "description" : (string) Description text used by this card,     "archived": (boolean) whether this Card is archived,     "draft": (boolean) whether this Card is a draft, } ```
            {
                "name": "feed_details",
                "table_name": "detail",
                "endpoint": {
                    "path": "/feed/details",
                    "params": {
                        # the parameters below can optionally be configured
                        # "card_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve relevant information on the segment, which can be identified by the `segment_id`.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {       "message": (required, string) the status of the export, returns 'success' when completed without errors,       "created_at" : (string) date created as ISO 8601 date,       "updated_at" : (string) date last updated as ISO 8601 date,       "name" : (string) segment name,       "description" : (string) human-readable description of filters,       "text_description" : (string) segment description,        "tags" : (array) tag names associated with the segment } ```
            {
                "name": "segments_details",
                "table_name": "detail",
                "endpoint": {
                    "path": "/segments/details",
                    "params": {
                        # the parameters below can optionally be configured
                        # "segment_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Use the endpoint below to get the subscription state of a user in a subscription group. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.  > *Either `external_id` or `email` are required.  ## Response  All successful responses will return `subscribed`, `unsubscribed`, or `unknown` depending on status and user history with the subscription group.  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   "status": {     "1": "Unsubscribed",     "2": "Subscribed"   },   "message": "success" } ```
            {
                "name": "subscription_status_get",
                "table_name": "get",
                "endpoint": {
                    "path": "/subscription/status/get",
                    "params": {
                        # the parameters below can optionally be configured
                        # "subscription_group_id": "OPTIONAL_CONFIG",
                        # "external_id": "OPTIONAL_CONFIG",
                        # "phone": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.  > You must provide an `end_date`, as well as either an `email` or a `start_date`.<br><br>If your date range has more than `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.  ## Response  Entries are listed in descending order.  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   "emails": [     {       "email": "example1@braze.com",       "hard_bounced_at": "2016-08-25 15:24:32 +0000"     },     {       "email": "example2@braze.com",       "hard_bounced_at": "2016-08-24 17:41:58 +0000"     },     {       "email": "example3@braze.com",       "hard_bounced_at": "2016-08-24 12:01:13 +0000"     }   ],   "message": "success" } ```
            {
                "name": "email_hard_bounces",
                "table_name": "hard_bounce",
                "endpoint": {
                    "path": "/email/hard_bounces",
                    "params": {
                        # the parameters below can optionally be configured
                        # "start_date": "OPTIONAL_CONFIG",
                        # "end_date": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # This endpoint will call information for an existing Content Block.  ### Successful Response Properties ```json Content-Type: application/json Authorization: Bearer YOUR_REST_API_KEY {   "content_block_id": "string",   "name": "string",   "content": "string",   "description": "string",   "content_type": "html or text",   "tags":  "array of strings",   "created_at": "time-in-iso",   "last_edited": "time-in-iso",   "inclusion_count" : "integer",   "message": "success" } ```  ### Possible Errors - `Content Block ID cannot be blank.` - A Content Block has not been listed or is not encapsulated in quotes.  - `Content Block ID is invalid for this App Group.` - This Content Block does not exist or is in a different company account or app group.  - `Content Block has been deleted - content not available.` - This Content Block, though it may have existed earlier, has been deleted.  - `Include Inclusion Data - error` - One of true or false is not provided.
            {
                "name": "content_blocks_info",
                "table_name": "info",
                "endpoint": {
                    "path": "/content_blocks/info",
                    "params": {
                        # the parameters below can optionally be configured
                        # "content_block_id": "OPTIONAL_CONFIG",
                        # "include_inclusion_data": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Use to get information on your email templates.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.  ### Request Components - [Template Identifier](https://www.braze.com/docs/api/identifier_types/)
            {
                "name": "templates_email_info",
                "table_name": "info",
                "endpoint": {
                    "path": "/templates/email/info",
                    "params": {
                        # the parameters below can optionally be configured
                        # "email_template_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to export a list of campaigns, each of which will include its name, Campaign API Identifier, whether it is an API Campaign, and Tags associated with the campaign. The campaigns are returned in groups of 100 sorted by time of creation (oldest to newest by default).  ## Campaign List Endpoint API Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "campaigns" : [         {             "id" : (string) Campaign API Identifier,             "last_edited": (ISO 8601 string) the last edited time for the message              "name" : (string) campaign name,             "is_api_campaign" : (boolean) whether the campaign is an API Campaign,             "tags" : (array) tag names associated with the campaign         },         ...     ] } ```
            {
                "name": "campaigns_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/campaigns/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "include_archived": "OPTIONAL_CONFIG",
                        # "sort_direction": "OPTIONAL_CONFIG",
                        # "last_edit.time[gt]": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # This endpoint allows you to export a list of Canvases, including the name, Canvas API Identifier and associated Tags. The Canvases are returned in groups of 100 sorted by time of creation (oldest to newest by default).  > Archived Canvases will not be included in the API response unless the `include_archived` field is specified. Canvases that are stopped but not archived, however, will be returned by default.   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {   "canvases" : [   	{   		"id" : (string) Canvas API Identifier,   		"last_edited": (ISO 8601 string) the last edited time for the message,   		"name" : (string) Canvas name,   		"tags" : (array) tag names associated with the Canvas,   	},     ... (more Canvases)   ],   "message": (required, string) the status of the export, returns 'success' when completed without errors } ```
            {
                "name": "canvas_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/canvas/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "include_archived": "OPTIONAL_CONFIG",
                        # "sort_direction": "OPTIONAL_CONFIG",
                        # "last_edit.time[gt]": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # This endpoint will list existing Content Block information.  ### Successful Response Properties ```json Content-Type: application/json Authorization: Bearer YOUR_REST_API_KEY {   "count": "integer",   "content_blocks": [     {       "content_block_id": "string",       "name": "string",       "content_type": "html or text",       "liquid_tag": "string",       "inclusion_count" : "integer",       "created_at": "time-in-iso",       "last_edited": "time-in-iso",       "tags" : "array of strings"     }   ] } ```  ### Possible Errors - `Modified after time is invalid.` The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).  - `Modified before time is invalid.` The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).  - `Modified after time must be earlier than or the same as modified before time.`  - `Content Block number limit is invalid.` The `limit` parameter must be an integer (positive number) greater than 0.  - `Content Block number limit must be greater than 0.` The `limit` parameter must be an integer (positive number) greater than 0.  - `Content Block number limit exceeds maximum of 1000.` The `limit` parameter must be an integer (positive number) greater than 0.  - `Offset is invalid.` The `offset` parameter must be an integer (positive number) greater than 0.  - `Offset must be greater than 0.` The `offset` parameter must be an integer (positive number) greater than 0.
            {
                "name": "content_blocks_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/content_blocks/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "modified_after": "OPTIONAL_CONFIG",
                        # "modified_before": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "events" : [         "Event A",         "Event B",         "Event C",         ...     ] } ```  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |
            {
                "name": "events_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/events/list",
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "cards" : [         {             "id" : (string) Card API Identifier,             "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner or DevPick (cross-promotional cards),             "title" : (string) title of the card,             "tags" : (array) tag names associated with the card         },         ...     ] } ```
            {
                "name": "feed_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/feed/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "include_archived": "OPTIONAL_CONFIG",
                        # "sort_direction": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "message": (required, string) the status of the export, returns 'success' when completed without errors,     "segments" : [         {             "id" : (string) Segment API Identifier,             "name" : (string) segment name,             "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,             "tags" : (array) tag names associated with the segment         },         ...     ] } ```
            {
                "name": "segments_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/segments/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "sort_direction": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # Use this endpoint to get a list of available templates in your Braze account.  Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.  ### Successful Response Properties ```json {   "count": number of templates returned   "templates": [template with the following properties]:     "email_template_id": (string) your email template's API Identifier,     "template_name": (string) the name of your email template,     "created_at": (string, in ISO 8601),     "updated_at": (string, in ISO 8601),     "tags": (array of strings) tags appended to the template }   ```
            {
                "name": "templates_email_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/templates/email/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "modified_after": "OPTIONAL_CONFIG",
                        # "modified_before": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # You can view a JSON list of upcoming and scheduled Campaigns and Canvases using the following information and parameters. The endpoint will return information about scheduled Campaigns and entry Canvases between now and the designated end_time (ISO 8601 format) specified in the request. Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint are only for Campaigns and Canvases created and scheduled in Braze.  ## Response  ```json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     "scheduled_broadcasts": [       # Example Canvas       {         "name" => String,         "id" => String,         "type" => "Canvas",         "tags" => [String tag names],         "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)         "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone       },       # Example Campaign       {         "name" => String,         "id" => String,         "type" => "Campaign",         "tags" => [String tag names],         "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)         "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone       },     ] } ```
            {
                "name": "messages_scheduled_broadcasts",
                "table_name": "scheduled_broadcast",
                "endpoint": {
                    "path": "/messages/scheduled_broadcasts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "end_time": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Use the endpoint below to list and get the subscription groups of a certain user.  > If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).
            {
                "name": "subscription_user_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/subscription/user/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "external_id": "OPTIONAL_CONFIG",
                        # "phone": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # Use the /email/unsubscribes endpoint to return emails that have unsubscribed during the time period from `start_date` to `end_date`. You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.  > You must provide either an email or a start_date and an end_date. <br><br>If your date range has more than `limit` number of unsubscribes, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.
            {
                "name": "email_unsubscribes",
                "table_name": "unsubscribe",
                "endpoint": {
                    "path": "/email/unsubscribes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "start_date": "OPTIONAL_CONFIG",
                        # "end_date": "OPTIONAL_CONFIG",
                        # "sort_direction": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 20,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
