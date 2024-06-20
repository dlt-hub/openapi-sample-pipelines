# postmark_app pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/postmark_app.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /bounces_ 
  *resource*: get_bounces  
* _GET /bounces/{bounceid}_ 
  *resource*: get_single_bounce  
* _GET /stats/outbound/bounces_ 
  *resource*: get_bounce_counts  
* _GET /stats/outbound/clicks/browserfamilies_ 
  *resource*: get_outbound_click_counts_by_browser_family  
* _GET /messages/outbound/clicks_ 
  *resource*: search_clicks_for_outbound_messages  
* _GET /messages/outbound/clicks/{messageid}_ 
  *resource*: get_clicks_for_single_outbound_message  
* _GET /stats/outbound/clicks_ 
  *resource*: get_outbound_click_counts  
* _GET /deliverystats_ 
  *resource*: get_delivery_stats  
* _GET /messages/inbound/{messageid}/details_ 
  *resource*: get_inbound_message_details  
* _GET /messages/outbound/{messageid}/details_ 
  *resource*: get_outbound_message_details  
* _GET /bounces/{bounceid}/dump_ 
  *resource*: get_bouncesbounceiddump  
* _GET /messages/outbound/{messageid}/dump_ 
  *resource*: get_outbound_message_dump  
* _GET /stats/outbound/opens/emailclients_ 
  *resource*: get_outbound_open_counts_by_email_client  
* _GET /messages/inbound_ 
  *resource*: search_inbound_messages  
* _GET /triggers/inboundrules_ 
  *resource*: list_inbound_rules  
* _GET /stats/outbound/clicks/location_ 
  *resource*: get_outbound_click_counts_by_location  
* _GET /messages/outbound/opens_ 
  *resource*: search_opens_for_outbound_messages  
* _GET /messages/outbound/opens/{messageid}_ 
  *resource*: get_opens_for_single_outbound_message  
* _GET /stats/outbound/opens_ 
  *resource*: get_outbound_open_counts  
* _GET /messages/outbound_ 
  *resource*: search_outbound_messages  
* _GET /stats/outbound_ 
  *resource*: get_outbound_overview_statistics  
* _GET /stats/outbound/clicks/platforms_ 
  *resource*: get_outbound_click_counts_by_platform  
* _GET /stats/outbound/opens/platforms_ 
  *resource*: get_outbound_open_counts_by_platform  
* _GET /stats/outbound/sends_ 
  *resource*: get_sent_counts  
* _GET /server_ 
  *resource*: get_current_server_configuration  
* _GET /stats/outbound/spam_ 
  *resource*: get_spam_complaints  
* _GET /templates_ 
  *resource*: list_templates  
* _GET /templates/{templateIdOrAlias}_ 
  *resource*: get_single_template  
* _GET /stats/outbound/tracked_ 
  *resource*: get_tracked_email_counts  
