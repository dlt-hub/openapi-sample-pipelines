# mailchimp pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/mailchimp.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /_ 
  *resource*: get_root  
  *description*: Get links to all other resources available in the API.
* _GET /lists/{list_id}/abuse-reports_ 
  *resource*: get_lists_id_abuse_reports  
  *description*: Get all abuse reports for a specific list.
* _GET /lists/{list_id}/abuse-reports/{report_id}_ 
  *resource*: get_lists_id_abuse_reports_id  
  *description*: Get details about a specific abuse report.
* _GET /reports/{campaign_id}/abuse-reports_ 
  *resource*: get_reports_id_abuse_reports_id  
  *description*: Get a list of abuse complaints for a specific campaign.
* _GET /reports/{campaign_id}/abuse-reports/{report_id}_ 
  *resource*: get_reports_id_abuse_reports_id_id  
  *description*: Get information about a specific abuse report for a campaign.
* _GET /account-exports_ 
  *resource*: get_account_exports  
  *description*: Get a list of account exports for a given account.
* _GET /account-exports/{export_id}_ 
  *resource*: get_account_export_id  
  *description*: Get information about a specific account export.
* _GET /lists/{list_id}/activity_ 
  *resource*: get_lists_id_activity  
  *description*: Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.
* _GET /lists/{list_id}/members/{subscriber_hash}/activity_ 
  *resource*: get_lists_id_members_id_activity  
  *description*: Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.
* _GET /lists/{list_id}/members/{subscriber_hash}/activity-feed_ 
  *resource*: get_lists_id_members_id_activity_feed  
  *description*: Get a member's activity on a specific list, including opens, clicks, and unsubscribes.
* _GET /reports/{campaign_id}/advice_ 
  *resource*: get_reports_id_advice  
  *description*: Get feedback based on a campaign's statistics. Advice feedback is based on campaign stats like opens, clicks, unsubscribes, bounces, and more.
* _GET /reporting/surveys/{survey_id}/questions/{question_id}/answers_ 
  *resource*: get_reporting_surveys_id_questions_id_answers  
  *description*: Get answers for a survey question.
* _GET /authorized-apps_ 
  *resource*: get_authorized_apps  
  *description*: Get a list of an account's registered, connected applications.
* _GET /authorized-apps/{app_id}_ 
  *resource*: get_authorized_apps_id  
  *description*: Get information about a specific authorized application.
* _GET /automations_ 
  *resource*: get_automations  
  *description*: Get a summary of an account's classic automations.
* _GET /automations/{workflow_id}_ 
  *resource*: get_automations_id  
  *description*: Get a summary of an individual classic automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.
* _GET /batches_ 
  *resource*: get_batches  
  *description*: Get a summary of batch requests that have been made.
* _GET /batches/{batch_id}_ 
  *resource*: get_batches_id  
  *description*: Get the status of a batch request.
* _GET /batch-webhooks_ 
  *resource*: get_batch_webhooks  
  *description*: Get all webhooks that have been configured for batches.
* _GET /batch-webhooks/{batch_webhook_id}_ 
  *resource*: get_batch_webhook  
  *description*: Get information about a specific batch webhook.
* _GET /campaigns_ 
  *resource*: get_campaigns  
  *description*: Get all campaigns in an account.
* _GET /campaigns/{campaign_id}_ 
  *resource*: get_campaigns_id  
  *description*: Get information about a specific campaign.
* _GET /campaign-folders_ 
  *resource*: get_campaign_folders  
  *description*: Get all folders used to organize campaigns.
* _GET /campaign-folders/{folder_id}_ 
  *resource*: get_campaign_folders_id  
  *description*: Get information about a specific folder used to organize campaigns.
* _GET /ecommerce/stores/{store_id}/carts_ 
  *resource*: get_ecommerce_stores_id_carts  
  *description*: Get information about a store's carts.
* _GET /ecommerce/stores/{store_id}/carts/{cart_id}_ 
  *resource*: get_ecommerce_stores_id_carts_id  
  *description*: Get information about a specific cart.
* _GET /activity-feed/chimp-chatter_ 
  *resource*: get_activity_feed_chimp_chatter  
  *description*: Return the Chimp Chatter for this account ordered by most recent.
* _GET /reports/{campaign_id}/click-details_ 
  *resource*: get_reports_id_click_details  
  *description*: Get information about clicks on specific links in your Mailchimp campaigns.
* _GET /reports/{campaign_id}/click-details/{link_id}_ 
  *resource*: get_reports_id_click_details_id  
  *description*: Get click details for a specific link in a campaign.
* _GET /lists/{list_id}/clients_ 
  *resource*: get_lists_id_clients  
  *description*: Get a list of the top email clients based on user-agent strings.
* _GET /connected-sites_ 
  *resource*: get_connected_sites  
  *description*: Get all connected sites in an account.
* _GET /connected-sites/{connected_site_id}_ 
  *resource*: get_connected_sites_id  
  *description*: Get information about a specific connected site.
* _GET /campaigns/{campaign_id}/content_ 
  *resource*: get_campaigns_id_content  
  *description*: Get the the HTML and plain-text content for a campaign.
* _GET /landing-pages/{page_id}/content_ 
  *resource*: get_landing_page_id_content  
  *description*: Get the the HTML for your landing page.
* _GET /conversations_ 
  *resource*: get_conversations  
  *description*: Get a list of conversations for the account. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
* _GET /conversations/{conversation_id}_ 
  *resource*: get_conversations_id  
  *description*: Get details about an individual conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
* _GET /ecommerce/stores/{store_id}/customers_ 
  *resource*: get_ecommerce_stores_id_customers  
  *description*: Get information about a store's customers.
* _GET /ecommerce/stores/{store_id}/customers/{customer_id}_ 
  *resource*: get_ecommerce_stores_id_customers_id  
  *description*: Get information about a specific customer.
* _GET /templates/{template_id}/default-content_ 
  *resource*: get_templates_id_default_content  
  *description*: Get the sections that you can edit in a template, including each section's default content.
* _GET /reports/{campaign_id}/domain-performance_ 
  *resource*: get_reports_id_domain_performance  
  *description*: Get statistics for the top-performing email domains in a campaign.
* _GET /reports/{campaign_id}/ecommerce-product-activity_ 
  *resource*: get_reports_id_ecommerce_product_activity  
  *description*: Get breakdown of product activity for a campaign
* _GET /reporting/facebook-ads/{outreach_id}/ecommerce-product-activity_ 
  *resource*: get_reporting_facebook_ads_id_ecommerce_product_activity  
  *description*: Get breakdown of product activity for an outreach.
* _GET /reports/{campaign_id}/eepurl_ 
  *resource*: get_reports_id_eepurl  
  *description*: Get a summary of social activity for the campaign, tracked by EepURL.
* _GET /automations/{workflow_id}/emails_ 
  *resource*: get_automations_id_emails  
  *description*: Get a summary of the emails in a classic automation workflow.
* _GET /automations/{workflow_id}/emails/{workflow_email_id}_ 
  *resource*: get_automations_id_emails_id  
  *description*: Get information about an individual classic automation workflow email.
* _GET /reports/{campaign_id}/email-activity_ 
  *resource*: get_reports_id_email_activity  
  *description*: Get a list of member's subscriber activity in a specific campaign.
* _GET /reports/{campaign_id}/email-activity/{subscriber_hash}_ 
  *resource*: get_reports_id_email_activity_id  
  *description*: Get a specific list member's activity in a campaign including opens, clicks, and bounces.
* _GET /lists/{list_id}/members/{subscriber_hash}/events_ 
  *resource*: get_lists_id_members_id_events  
  *description*: Get events for a contact.
* _GET /facebook-ads_ 
  *resource*: get_all_facebook_ads  
  *description*: Get list of Facebook ads.
* _GET /facebook-ads/{outreach_id}_ 
  *resource*: get_facebook_ads_id  
  *description*: Get details of a Facebook ad.
* _GET /reporting/facebook-ads_ 
  *resource*: get_reporting_facebook_ads  
  *description*: Get reports of Facebook ads.
* _GET /reporting/facebook-ads/{outreach_id}_ 
  *resource*: get_reporting_facebook_ads_id  
  *description*: Get report of a Facebook ad.
* _GET /campaigns/{campaign_id}/feedback_ 
  *resource*: get_campaigns_id_feedback  
  *description*: Get team feedback while you're working together on a Mailchimp campaign.
* _GET /campaigns/{campaign_id}/feedback/{feedback_id}_ 
  *resource*: get_campaigns_id_feedback_id  
  *description*: Get a specific feedback message from a campaign.
* _GET /file-manager/files_ 
  *resource*: get_file_manager_files  
  *description*: Get a list of available images and files stored in the File Manager for the account.
* _GET /file-manager/files/{file_id}_ 
  *resource*: get_file_manager_files_id  
  *description*: Get information about a specific file in the File Manager.
* _GET /file-manager/folders/{folder_id}/files_ 
  *resource*: get_file_manager_folders_files  
  *description*: Get a list of available images and files stored in this folder.
* _GET /file-manager/folders_ 
  *resource*: get_file_manager_folders  
  *description*: Get a list of all folders in the File Manager.
* _GET /file-manager/folders/{folder_id}_ 
  *resource*: get_file_manager_folders_id  
  *description*: Get information about a specific folder in the File Manager.
* _GET /lists/{list_id}/members/{subscriber_hash}/goals_ 
  *resource*: get_lists_id_members_id_goals  
  *description*: Get the last 50 Goal events for a member on a specific list.
* _GET /lists/{list_id}/growth-history_ 
  *resource*: get_lists_id_growth_history  
  *description*: Get a month-by-month summary of a specific list's growth activity.
* _GET /lists/{list_id}/growth-history/{month}_ 
  *resource*: get_lists_id_growth_history_id  
  *description*: Get a summary of a specific list's growth activity for a specific month and year.
* _GET /ecommerce/stores/{store_id}/products/{product_id}/images_ 
  *resource*: get_ecommerce_stores_id_products_id_images  
  *description*: Get information about a product's images.
* _GET /ecommerce/stores/{store_id}/products/{product_id}/images/{image_id}_ 
  *resource*: get_ecommerce_stores_id_products_id_images_id  
  *description*: Get information about a specific product image.
* _GET /lists/{list_id}/interest-categories/{interest_category_id}/interests_ 
  *resource*: get_lists_id_interest_categories_id_interests  
  *description*: Get a list of this category's interests.
* _GET /lists/{list_id}/interest-categories/{interest_category_id}/interests/{interest_id}_ 
  *resource*: get_lists_id_interest_categories_id_interests_id  
  *description*: Get interests or 'group names' for a specific category.
* _GET /lists/{list_id}/interest-categories_ 
  *resource*: get_lists_id_interest_categories  
  *description*: Get information about a list's interest categories.
* _GET /lists/{list_id}/interest-categories/{interest_category_id}_ 
  *resource*: get_lists_id_interest_categories_id  
  *description*: Get information about a specific interest category.
* _GET /landing-pages_ 
  *resource*: get_all_landing_pages  
  *description*: Get all landing pages.
* _GET /landing-pages/{page_id}_ 
  *resource*: get_landing_page_id  
  *description*: Get information about a specific page.
* _GET /reporting/landing-pages/{outreach_id}_ 
  *resource*: get_reporting_landing_pages_id  
  *description*: Get report of a landing page.
* _GET /reporting/landing-pages_ 
  *resource*: get_reporting_landing_pages  
  *description*: Get reports of landing pages.
* _GET /ecommerce/stores/{store_id}/carts/{cart_id}/lines_ 
  *resource*: get_ecommerce_stores_id_carts_id_lines  
  *description*: Get information about a cart's line items.
* _GET /ecommerce/stores/{store_id}/carts/{cart_id}/lines/{line_id}_ 
  *resource*: get_ecommerce_stores_id_carts_id_lines_id  
  *description*: Get information about a specific cart line item.
* _GET /ecommerce/stores/{store_id}/orders/{order_id}/lines_ 
  *resource*: get_ecommerce_stores_id_orders_id_lines  
  *description*: Get information about an order's line items.
* _GET /ecommerce/stores/{store_id}/orders/{order_id}/lines/{line_id}_ 
  *resource*: get_ecommerce_stores_id_orders_id_lines_id  
  *description*: Get information about a specific order line item.
* _GET /lists_ 
  *resource*: get_lists  
  *description*: Get information about all lists in the account.
* _GET /lists/{list_id}_ 
  *resource*: get_lists_id  
  *description*: Get information about a specific list in your Mailchimp account. Results include list members who have signed up but haven't confirmed their subscription yet and unsubscribed or cleaned.
* _GET /lists/{list_id}/locations_ 
  *resource*: get_lists_id_locations  
  *description*: Get the locations (countries) that the list's subscribers have been tagged to based on geocoding their IP address.
* _GET /reports/{campaign_id}/locations_ 
  *resource*: get_reports_id_locations  
  *description*: Get top open locations for a specific campaign.
* _GET /lists/{list_id}/segments/{segment_id}/members_ 
  *resource*: get_lists_id_segments_id_members  
  *description*: Get information about members in a saved segment.
* _GET /lists/{list_id}/members_ 
  *resource*: get_lists_id_members  
  *description*: Get information about members in a specific Mailchimp list.
* _GET /lists/{list_id}/members/{subscriber_hash}_ 
  *resource*: get_lists_id_members_id  
  *description*: Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.
* _GET /reports/{campaign_id}/click-details/{link_id}/members_ 
  *resource*: get_reports_id_click_details_id_members  
  *description*: Get information about list members who clicked on a specific link in a campaign.
* _GET /reports/{campaign_id}/click-details/{link_id}/members/{subscriber_hash}_ 
  *resource*: get_reports_id_click_details_id_members_id  
  *description*: Get information about a specific subscriber who clicked a link in a specific campaign.
* _GET /lists/{list_id}/merge-fields_ 
  *resource*: get_lists_id_merge_fields  
  *description*: Get a list of all merge fields for an audience.
* _GET /lists/{list_id}/merge-fields/{merge_id}_ 
  *resource*: get_lists_id_merge_fields_id  
  *description*: Get information about a specific merge field.
* _GET /conversations/{conversation_id}/messages_ 
  *resource*: get_conversations_id_messages  
  *description*: Get messages from a specific conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
* _GET /conversations/{conversation_id}/messages/{message_id}_ 
  *resource*: get_conversations_id_messages_id  
  *description*: Get an individual message in a conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
* _GET /lists/{list_id}/members/{subscriber_hash}/notes_ 
  *resource*: get_lists_id_members_id_notes  
  *description*: Get recent notes for a specific list member.
* _GET /lists/{list_id}/members/{subscriber_hash}/notes/{note_id}_ 
  *resource*: get_lists_id_members_id_notes_id  
  *description*: Get a specific note for a specific list member.
* _GET /reports/{campaign_id}/open-details_ 
  *resource*: get_reports_id_open_details  
  *description*: Get detailed information about any campaign emails that were opened by a list member.
* _GET /reports/{campaign_id}/open-details/{subscriber_hash}_ 
  *resource*: get_reports_id_open_details_id_members_id  
  *description*: Get information about a specific subscriber who opened a campaign.
* _GET /ecommerce/orders_ 
  *resource*: get_ecommerce_orders  
  *description*: Get information about an account's orders.
* _GET /ecommerce/stores/{store_id}/orders_ 
  *resource*: get_ecommerce_stores_id_orders  
  *description*: Get information about a store's orders.
* _GET /ecommerce/stores/{store_id}/orders/{order_id}_ 
  *resource*: get_ecommerce_stores_id_orders_id  
  *description*: Get information about a specific order.
* _GET /ping_ 
  *resource*: get_ping  
  *description*: A health check for the API that won't return any account-specific information.
* _GET /ecommerce/stores/{store_id}/products_ 
  *resource*: get_ecommerce_stores_id_products  
  *description*: Get information about a store's products.
* _GET /ecommerce/stores/{store_id}/products/{product_id}_ 
  *resource*: get_ecommerce_stores_id_products_id  
  *description*: Get information about a specific product.
* _GET /ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes_ 
  *resource*: get_ecommerce_stores_id_promocodes  
  *description*: Get information about a store's promo codes.
* _GET /ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes/{promo_code_id}_ 
  *resource*: get_ecommerce_stores_id_promocodes_id  
  *description*: Get information about a specific promo code.
* _GET /ecommerce/stores/{store_id}/promo-rules_ 
  *resource*: get_ecommerce_stores_id_promorules  
  *description*: Get information about a store's promo rules.
* _GET /ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}_ 
  *resource*: get_ecommerce_stores_id_promorules_id  
  *description*: Get information about a specific promo rule.
* _GET /reporting/surveys/{survey_id}/questions_ 
  *resource*: get_reporting_surveys_id_questions  
  *description*: Get reports for survey questions.
* _GET /reporting/surveys/{survey_id}/questions/{question_id}_ 
  *resource*: get_reporting_surveys_id_questions_id  
  *description*: Get report for a survey question.
* _GET /automations/{workflow_id}/emails/{workflow_email_id}/queue_ 
  *resource*: get_automations_id_emails_id_queue  
  *description*: Get information about a classic automation email queue.
* _GET /automations/{workflow_id}/emails/{workflow_email_id}/queue/{subscriber_hash}_ 
  *resource*: get_automations_id_emails_id_queue_id  
  *description*: Get information about a specific subscriber in a classic automation email queue.
* _GET /automations/{workflow_id}/removed-subscribers_ 
  *resource*: get_automations_id_removed_subscribers  
  *description*: Get information about subscribers who were removed from a classic automation workflow.
* _GET /automations/{workflow_id}/removed-subscribers/{subscriber_hash}_ 
  *resource*: get_automations_id_removed_subscribers_id  
  *description*: Get information about a specific subscriber who was removed from a classic automation workflow.
* _GET /reports_ 
  *resource*: get_reports  
  *description*: Get campaign reports.
* _GET /reports/{campaign_id}_ 
  *resource*: get_reports_id  
  *description*: Get report details for a specific sent campaign.
* _GET /reporting/surveys/{survey_id}/responses_ 
  *resource*: get_reporting_surveys_id_responses  
  *description*: Get responses to a survey.
* _GET /reporting/surveys/{survey_id}/responses/{response_id}_ 
  *resource*: get_reporting_surveys_id_responses_id  
  *description*: Get a single survey response.
* _GET /search-campaigns_ 
  *resource*: get_search_campaigns  
  *description*: Search all campaigns for the specified query terms.
* _GET /search-members_ 
  *resource*: get_search_members  
  *description*: Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.
* _GET /lists/{list_id}/segments_ 
  *resource*: preview_a_segment  
  *description*: Get information about all available segments for a specific list.
* _GET /lists/{list_id}/segments/{segment_id}_ 
  *resource*: get_lists_id_segments_id  
  *description*: Get information about a specific segment.
* _GET /campaigns/{campaign_id}/send-checklist_ 
  *resource*: get_campaigns_id_send_checklist  
  *description*: Review the send checklist for a campaign, and resolve any issues before sending.
* _GET /reports/{campaign_id}/sent-to_ 
  *resource*: get_reports_id_sent_to  
  *description*: Get information about campaign recipients.
* _GET /reports/{campaign_id}/sent-to/{subscriber_hash}_ 
  *resource*: get_reports_id_sent_to_id  
  *description*: Get information about a specific campaign recipient.
* _GET /lists/{list_id}/signup-forms_ 
  *resource*: get_lists_id_signup_forms  
  *description*: Get signup forms for a specific list.
* _GET /ecommerce/stores_ 
  *resource*: get_ecommerce_stores  
  *description*: Get information about all stores in the account.
* _GET /ecommerce/stores/{store_id}_ 
  *resource*: get_ecommerce_stores_id  
  *description*: Get information about a specific store.
* _GET /reports/{campaign_id}/sub-reports_ 
  *resource*: get_reports_id_sub_reports_id  
  *description*: Get a list of reports with child campaigns for a specific parent campaign.
* _GET /lists/{list_id}/surveys_ 
  *resource*: get_lists_id_surveys  
  *description*: Get information about all available surveys for a specific list.
* _GET /lists/{list_id}/surveys/{survey_id}_ 
  *resource*: get_lists_id_surveys_id  
  *description*: Get details about a specific survey.
* _GET /reporting/surveys_ 
  *resource*: get_reporting_surveys  
  *description*: Get reports for surveys.
* _GET /reporting/surveys/{survey_id}_ 
  *resource*: get_reporting_surveys_id  
  *description*: Get report for a survey.
* _GET /lists/{list_id}/members/{subscriber_hash}/tags_ 
  *resource*: get_list_member_tags  
  *description*: Get the tags on a list member.
* _GET /lists/{list_id}/tag-search_ 
  *resource*: search_tags_by_name  
  *description*: Search for tags on a list by name. If no name is provided, will return all tags on the list.
* _GET /templates_ 
  *resource*: get_templates  
  *description*: Get a list of an account's available templates.
* _GET /templates/{template_id}_ 
  *resource*: get_templates_id  
  *description*: Get information about a specific template.
* _GET /template-folders_ 
  *resource*: get_template_folders  
  *description*: Get all folders used to organize templates.
* _GET /template-folders/{folder_id}_ 
  *resource*: get_template_folders_id  
  *description*: Get information about a specific folder used to organize templates.
* _GET /reports/{campaign_id}/unsubscribed_ 
  *resource*: get_reports_id_unsubscribed  
  *description*: Get information about members who have unsubscribed from a specific campaign.
* _GET /reports/{campaign_id}/unsubscribed/{subscriber_hash}_ 
  *resource*: get_reports_id_unsubscribed_id  
  *description*: Get information about a specific list member who unsubscribed from a campaign.
* _GET /ecommerce/stores/{store_id}/products/{product_id}/variants_ 
  *resource*: get_ecommerce_stores_id_products_id_variants  
  *description*: Get information about a product's variants.
* _GET /ecommerce/stores/{store_id}/products/{product_id}/variants/{variant_id}_ 
  *resource*: get_ecommerce_stores_id_products_id_variants_id  
  *description*: Get information about a specific product variant.
* _GET /verified-domains/{domain_name}_ 
  *resource*: get_verified_domain  
  *description*: Get the details for a single domain on the account.
* _GET /verified-domains_ 
  *resource*: get_verified_domains  
  *description*: Get all of the sending domains on the account.
* _GET /lists/{list_id}/webhooks_ 
  *resource*: get_lists_id_webhooks  
  *description*: Get information about all webhooks for a specific list.
* _GET /lists/{list_id}/webhooks/{webhook_id}_ 
  *resource*: get_lists_id_webhooks_id  
  *description*: Get information about a specific webhook.
