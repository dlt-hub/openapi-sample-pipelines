from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="mailchimp_source", max_table_nesting=2)
def mailchimp_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Get links to all other resources available in the API.
            {
                "name": "get_root",
                "table_name": "",
                "endpoint": {
                    "path": "/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all abuse reports for a specific list.
            {
                "name": "get_lists_id_abuse_reports",
                "table_name": "abuse_report",
                "endpoint": {
                    "path": "/lists/{list_id}/abuse-reports",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get details about a specific abuse report.
            {
                "name": "get_lists_id_abuse_reports_id",
                "table_name": "abuse_report",
                "endpoint": {
                    "path": "/lists/{list_id}/abuse-reports/{report_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "report_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of abuse complaints for a specific campaign.
            {
                "name": "get_reports_id_abuse_reports_id",
                "table_name": "abuse_report",
                "endpoint": {
                    "path": "/reports/{campaign_id}/abuse-reports",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific abuse report for a campaign.
            {
                "name": "get_reports_id_abuse_reports_id_id",
                "table_name": "abuse_report",
                "endpoint": {
                    "path": "/reports/{campaign_id}/abuse-reports/{report_id}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "report_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of account exports for a given account.
            {
                "name": "get_account_exports",
                "table_name": "account_export",
                "endpoint": {
                    "path": "/account-exports",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific account export.
            {
                "name": "get_account_export_id",
                "table_name": "account_export",
                "endpoint": {
                    "path": "/account-exports/{export_id}",
                    "params": {
                        "export_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get up to the previous 180 days of daily detailed aggregated activity stats for a list, not including Automation activity.
            {
                "name": "get_lists_id_activity",
                "table_name": "activity",
                "endpoint": {
                    "path": "/lists/{list_id}/activity",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the last 50 events of a member's activity on a specific list, including opens, clicks, and unsubscribes.
            {
                "name": "get_lists_id_members_id_activity",
                "table_name": "activity",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/activity",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "action": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a member's activity on a specific list, including opens, clicks, and unsubscribes.
            {
                "name": "get_lists_id_members_id_activity_feed",
                "table_name": "activity_feed",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/activity-feed",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "activity_filters": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get feedback based on a campaign's statistics. Advice feedback is based on campaign stats like opens, clicks, unsubscribes, bounces, and more.
            {
                "name": "get_reports_id_advice",
                "table_name": "advice",
                "endpoint": {
                    "path": "/reports/{campaign_id}/advice",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get answers for a survey question.
            {
                "name": "get_reporting_surveys_id_questions_id_answers",
                "table_name": "answer",
                "endpoint": {
                    "path": "/reporting/surveys/{survey_id}/questions/{question_id}/answers",
                    "params": {
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "question_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "respondent_familiarity_is": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of an account's registered, connected applications.
            {
                "name": "get_authorized_apps",
                "table_name": "authorized_app",
                "endpoint": {
                    "path": "/authorized-apps",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific authorized application.
            {
                "name": "get_authorized_apps_id",
                "table_name": "authorized_app",
                "endpoint": {
                    "path": "/authorized-apps/{app_id}",
                    "params": {
                        "app_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a summary of an account's classic automations.
            {
                "name": "get_automations",
                "table_name": "automation",
                "endpoint": {
                    "path": "/automations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "before_create_time": "OPTIONAL_CONFIG",
                        # "since_create_time": "OPTIONAL_CONFIG",
                        # "before_start_time": "OPTIONAL_CONFIG",
                        # "since_start_time": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a summary of an individual classic automation workflow's settings and content. The `trigger_settings` object returns information for the first email in the workflow.
            {
                "name": "get_automations_id",
                "table_name": "automation",
                "endpoint": {
                    "path": "/automations/{workflow_id}",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a summary of batch requests that have been made.
            {
                "name": "get_batches",
                "table_name": "batch",
                "endpoint": {
                    "path": "/batches",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the status of a batch request.
            {
                "name": "get_batches_id",
                "table_name": "batch",
                "endpoint": {
                    "path": "/batches/{batch_id}",
                    "params": {
                        "batch_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all webhooks that have been configured for batches.
            {
                "name": "get_batch_webhooks",
                "table_name": "batch_webhook",
                "endpoint": {
                    "path": "/batch-webhooks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific batch webhook.
            {
                "name": "get_batch_webhook",
                "table_name": "batch_webhook",
                "endpoint": {
                    "path": "/batch-webhooks/{batch_webhook_id}",
                    "params": {
                        "batch_webhook_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all campaigns in an account.
            {
                "name": "get_campaigns",
                "table_name": "campaign",
                "endpoint": {
                    "path": "/campaigns",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "before_send_time": "OPTIONAL_CONFIG",
                        # "since_send_time": "OPTIONAL_CONFIG",
                        # "before_create_time": "OPTIONAL_CONFIG",
                        # "since_create_time": "OPTIONAL_CONFIG",
                        # "list_id": "OPTIONAL_CONFIG",
                        # "folder_id": "OPTIONAL_CONFIG",
                        # "member_id": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                        # "include_resend_shortcut_eligibility": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific campaign.
            {
                "name": "get_campaigns_id",
                "table_name": "campaign",
                "endpoint": {
                    "path": "/campaigns/{campaign_id}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "include_resend_shortcut_eligibility": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all folders used to organize campaigns.
            {
                "name": "get_campaign_folders",
                "table_name": "campaign_folder",
                "endpoint": {
                    "path": "/campaign-folders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific folder used to organize campaigns.
            {
                "name": "get_campaign_folders_id",
                "table_name": "campaign_folder",
                "endpoint": {
                    "path": "/campaign-folders/{folder_id}",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a store's carts.
            {
                "name": "get_ecommerce_stores_id_carts",
                "table_name": "cart",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/carts",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific cart.
            {
                "name": "get_ecommerce_stores_id_carts_id",
                "table_name": "cart",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/carts/{cart_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cart_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the Chimp Chatter for this account ordered by most recent.
            {
                "name": "get_activity_feed_chimp_chatter",
                "table_name": "chimp_chatter",
                "endpoint": {
                    "path": "/activity-feed/chimp-chatter",
                    "params": {
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about clicks on specific links in your Mailchimp campaigns.
            {
                "name": "get_reports_id_click_details",
                "table_name": "click_detail",
                "endpoint": {
                    "path": "/reports/{campaign_id}/click-details",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get click details for a specific link in a campaign.
            {
                "name": "get_reports_id_click_details_id",
                "table_name": "click_detail",
                "endpoint": {
                    "path": "/reports/{campaign_id}/click-details/{link_id}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of the top email clients based on user-agent strings.
            {
                "name": "get_lists_id_clients",
                "table_name": "client",
                "endpoint": {
                    "path": "/lists/{list_id}/clients",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all connected sites in an account.
            {
                "name": "get_connected_sites",
                "table_name": "connected_site",
                "endpoint": {
                    "path": "/connected-sites",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific connected site.
            {
                "name": "get_connected_sites_id",
                "table_name": "connected_site",
                "endpoint": {
                    "path": "/connected-sites/{connected_site_id}",
                    "params": {
                        "connected_site_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the the HTML and plain-text content for a campaign.
            {
                "name": "get_campaigns_id_content",
                "table_name": "content",
                "endpoint": {
                    "path": "/campaigns/{campaign_id}/content",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the the HTML for your landing page.
            {
                "name": "get_landing_page_id_content",
                "table_name": "content",
                "endpoint": {
                    "path": "/landing-pages/{page_id}/content",
                    "params": {
                        "page_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of conversations for the account. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
            {
                "name": "get_conversations",
                "table_name": "conversation",
                "endpoint": {
                    "path": "/conversations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "has_unread_messages": "OPTIONAL_CONFIG",
                        # "list_id": "OPTIONAL_CONFIG",
                        # "campaign_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get details about an individual conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
            {
                "name": "get_conversations_id",
                "table_name": "conversation",
                "endpoint": {
                    "path": "/conversations/{conversation_id}",
                    "params": {
                        "conversation_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a store's customers.
            {
                "name": "get_ecommerce_stores_id_customers",
                "table_name": "customer",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/customers",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "email_address": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific customer.
            {
                "name": "get_ecommerce_stores_id_customers_id",
                "table_name": "customer",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/customers/{customer_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "customer_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the sections that you can edit in a template, including each section's default content.
            {
                "name": "get_templates_id_default_content",
                "table_name": "default_content",
                "endpoint": {
                    "path": "/templates/{template_id}/default-content",
                    "params": {
                        "template_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get statistics for the top-performing email domains in a campaign.
            {
                "name": "get_reports_id_domain_performance",
                "table_name": "domain_performance",
                "endpoint": {
                    "path": "/reports/{campaign_id}/domain-performance",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get breakdown of product activity for a campaign
            {
                "name": "get_reports_id_ecommerce_product_activity",
                "table_name": "ecommerce_product_activity",
                "endpoint": {
                    "path": "/reports/{campaign_id}/ecommerce-product-activity",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get breakdown of product activity for an outreach.
            {
                "name": "get_reporting_facebook_ads_id_ecommerce_product_activity",
                "table_name": "ecommerce_product_activity",
                "endpoint": {
                    "path": "/reporting/facebook-ads/{outreach_id}/ecommerce-product-activity",
                    "params": {
                        "outreach_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a summary of social activity for the campaign, tracked by EepURL.
            {
                "name": "get_reports_id_eepurl",
                "table_name": "eepurl",
                "endpoint": {
                    "path": "/reports/{campaign_id}/eepurl",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a summary of the emails in a classic automation workflow.
            {
                "name": "get_automations_id_emails",
                "table_name": "email",
                "endpoint": {
                    "path": "/automations/{workflow_id}/emails",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about an individual classic automation workflow email.
            {
                "name": "get_automations_id_emails_id",
                "table_name": "email",
                "endpoint": {
                    "path": "/automations/{workflow_id}/emails/{workflow_email_id}",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "workflow_email_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of member's subscriber activity in a specific campaign.
            {
                "name": "get_reports_id_email_activity",
                "table_name": "email_activity",
                "endpoint": {
                    "path": "/reports/{campaign_id}/email-activity",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a specific list member's activity in a campaign including opens, clicks, and bounces.
            {
                "name": "get_reports_id_email_activity_id",
                "table_name": "email_activity",
                "endpoint": {
                    "path": "/reports/{campaign_id}/email-activity/{subscriber_hash}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get events for a contact.
            {
                "name": "get_lists_id_members_id_events",
                "table_name": "event",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/events",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get list of Facebook ads.
            {
                "name": "get_all_facebook_ads",
                "table_name": "facebook_ad",
                "endpoint": {
                    "path": "/facebook-ads",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get details of a Facebook ad.
            {
                "name": "get_facebook_ads_id",
                "table_name": "facebook_ad",
                "endpoint": {
                    "path": "/facebook-ads/{outreach_id}",
                    "params": {
                        "outreach_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get reports of Facebook ads.
            {
                "name": "get_reporting_facebook_ads",
                "table_name": "facebook_ad",
                "endpoint": {
                    "path": "/reporting/facebook-ads",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get report of a Facebook ad.
            {
                "name": "get_reporting_facebook_ads_id",
                "table_name": "facebook_ad",
                "endpoint": {
                    "path": "/reporting/facebook-ads/{outreach_id}",
                    "params": {
                        "outreach_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get team feedback while you're working together on a Mailchimp campaign.
            {
                "name": "get_campaigns_id_feedback",
                "table_name": "feedback",
                "endpoint": {
                    "path": "/campaigns/{campaign_id}/feedback",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a specific feedback message from a campaign.
            {
                "name": "get_campaigns_id_feedback_id",
                "table_name": "feedback",
                "endpoint": {
                    "path": "/campaigns/{campaign_id}/feedback/{feedback_id}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "feedback_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of available images and files stored in the File Manager for the account.
            {
                "name": "get_file_manager_files",
                "table_name": "file",
                "endpoint": {
                    "path": "/file-manager/files",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "created_by": "OPTIONAL_CONFIG",
                        # "before_created_at": "OPTIONAL_CONFIG",
                        # "since_created_at": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific file in the File Manager.
            {
                "name": "get_file_manager_files_id",
                "table_name": "file",
                "endpoint": {
                    "path": "/file-manager/files/{file_id}",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of available images and files stored in this folder.
            {
                "name": "get_file_manager_folders_files",
                "table_name": "file",
                "endpoint": {
                    "path": "/file-manager/folders/{folder_id}/files",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "created_by": "OPTIONAL_CONFIG",
                        # "before_created_at": "OPTIONAL_CONFIG",
                        # "since_created_at": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of all folders in the File Manager.
            {
                "name": "get_file_manager_folders",
                "table_name": "folder",
                "endpoint": {
                    "path": "/file-manager/folders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "created_by": "OPTIONAL_CONFIG",
                        # "before_created_at": "OPTIONAL_CONFIG",
                        # "since_created_at": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific folder in the File Manager.
            {
                "name": "get_file_manager_folders_id",
                "table_name": "folder",
                "endpoint": {
                    "path": "/file-manager/folders/{folder_id}",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the last 50 Goal events for a member on a specific list.
            {
                "name": "get_lists_id_members_id_goals",
                "table_name": "goal",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/goals",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a month-by-month summary of a specific list's growth activity.
            {
                "name": "get_lists_id_growth_history",
                "table_name": "growth_history",
                "endpoint": {
                    "path": "/lists/{list_id}/growth-history",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a summary of a specific list's growth activity for a specific month and year.
            {
                "name": "get_lists_id_growth_history_id",
                "table_name": "growth_history",
                "endpoint": {
                    "path": "/lists/{list_id}/growth-history/{month}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "month": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a product's images.
            {
                "name": "get_ecommerce_stores_id_products_id_images",
                "table_name": "image",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/products/{product_id}/images",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "product_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific product image.
            {
                "name": "get_ecommerce_stores_id_products_id_images_id",
                "table_name": "image",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/products/{product_id}/images/{image_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "product_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "image_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of this category's interests.
            {
                "name": "get_lists_id_interest_categories_id_interests",
                "table_name": "interest",
                "endpoint": {
                    "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "interest_category_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get interests or 'group names' for a specific category.
            {
                "name": "get_lists_id_interest_categories_id_interests_id",
                "table_name": "interest",
                "endpoint": {
                    "path": "/lists/{list_id}/interest-categories/{interest_category_id}/interests/{interest_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "interest_category_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "interest_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a list's interest categories.
            {
                "name": "get_lists_id_interest_categories",
                "table_name": "interest_category",
                "endpoint": {
                    "path": "/lists/{list_id}/interest-categories",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific interest category.
            {
                "name": "get_lists_id_interest_categories_id",
                "table_name": "interest_category",
                "endpoint": {
                    "path": "/lists/{list_id}/interest-categories/{interest_category_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "interest_category_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all landing pages.
            {
                "name": "get_all_landing_pages",
                "table_name": "landing_page",
                "endpoint": {
                    "path": "/landing-pages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "sort_dir": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific page.
            {
                "name": "get_landing_page_id",
                "table_name": "landing_page",
                "endpoint": {
                    "path": "/landing-pages/{page_id}",
                    "params": {
                        "page_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get report of a landing page.
            {
                "name": "get_reporting_landing_pages_id",
                "table_name": "landing_page",
                "endpoint": {
                    "path": "/reporting/landing-pages/{outreach_id}",
                    "params": {
                        "outreach_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get reports of landing pages.
            {
                "name": "get_reporting_landing_pages",
                "table_name": "landing_page",
                "endpoint": {
                    "path": "/reporting/landing-pages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a cart's line items.
            {
                "name": "get_ecommerce_stores_id_carts_id_lines",
                "table_name": "line",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cart_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific cart line item.
            {
                "name": "get_ecommerce_stores_id_carts_id_lines_id",
                "table_name": "line",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/carts/{cart_id}/lines/{line_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cart_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "line_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about an order's line items.
            {
                "name": "get_ecommerce_stores_id_orders_id_lines",
                "table_name": "line",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific order line item.
            {
                "name": "get_ecommerce_stores_id_orders_id_lines_id",
                "table_name": "line",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/orders/{order_id}/lines/{line_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "line_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about all lists in the account.
            {
                "name": "get_lists",
                "table_name": "list",
                "endpoint": {
                    "path": "/lists",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "before_date_created": "OPTIONAL_CONFIG",
                        # "since_date_created": "OPTIONAL_CONFIG",
                        # "before_campaign_last_sent": "OPTIONAL_CONFIG",
                        # "since_campaign_last_sent": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                        # "has_ecommerce_store": "OPTIONAL_CONFIG",
                        # "include_total_contacts": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific list in your Mailchimp account. Results include list members who have signed up but haven't confirmed their subscription yet and unsubscribed or cleaned.
            {
                "name": "get_lists_id",
                "table_name": "list",
                "endpoint": {
                    "path": "/lists/{list_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "include_total_contacts": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the locations (countries) that the list's subscribers have been tagged to based on geocoding their IP address.
            {
                "name": "get_lists_id_locations",
                "table_name": "location",
                "endpoint": {
                    "path": "/lists/{list_id}/locations",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get top open locations for a specific campaign.
            {
                "name": "get_reports_id_locations",
                "table_name": "location",
                "endpoint": {
                    "path": "/reports/{campaign_id}/locations",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about members in a saved segment.
            {
                "name": "get_lists_id_segments_id_members",
                "table_name": "member",
                "endpoint": {
                    "path": "/lists/{list_id}/segments/{segment_id}/members",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "segment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "include_cleaned": "OPTIONAL_CONFIG",
                        # "include_transactional": "OPTIONAL_CONFIG",
                        # "include_unsubscribed": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about members in a specific Mailchimp list.
            {
                "name": "get_lists_id_members",
                "table_name": "member",
                "endpoint": {
                    "path": "/lists/{list_id}/members",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "email_type": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "since_timestamp_opt": "OPTIONAL_CONFIG",
                        # "before_timestamp_opt": "OPTIONAL_CONFIG",
                        # "since_last_changed": "OPTIONAL_CONFIG",
                        # "before_last_changed": "OPTIONAL_CONFIG",
                        # "unique_email_id": "OPTIONAL_CONFIG",
                        # "vip_only": "OPTIONAL_CONFIG",
                        # "interest_category_id": "OPTIONAL_CONFIG",
                        # "interest_ids": "OPTIONAL_CONFIG",
                        # "interest_match": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                        # "since_last_campaign": "OPTIONAL_CONFIG",
                        # "unsubscribed_since": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific list member, including a currently subscribed, unsubscribed, or bounced member.
            {
                "name": "get_lists_id_members_id",
                "table_name": "member",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about list members who clicked on a specific link in a campaign.
            {
                "name": "get_reports_id_click_details_id_members",
                "table_name": "member",
                "endpoint": {
                    "path": "/reports/{campaign_id}/click-details/{link_id}/members",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific subscriber who clicked a link in a specific campaign.
            {
                "name": "get_reports_id_click_details_id_members_id",
                "table_name": "member",
                "endpoint": {
                    "path": "/reports/{campaign_id}/click-details/{link_id}/members/{subscriber_hash}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of all merge fields for an audience.
            {
                "name": "get_lists_id_merge_fields",
                "table_name": "merge_field",
                "endpoint": {
                    "path": "/lists/{list_id}/merge-fields",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "required": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific merge field.
            {
                "name": "get_lists_id_merge_fields_id",
                "table_name": "merge_field",
                "endpoint": {
                    "path": "/lists/{list_id}/merge-fields/{merge_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "merge_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get messages from a specific conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
            {
                "name": "get_conversations_id_messages",
                "table_name": "message",
                "endpoint": {
                    "path": "/conversations/{conversation_id}/messages",
                    "params": {
                        "conversation_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "is_read": "OPTIONAL_CONFIG",
                        # "before_timestamp": "OPTIONAL_CONFIG",
                        # "since_timestamp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get an individual message in a conversation. Conversations has been deprecated in favor of Inbox and these endpoints don't include Inbox data. Past Conversations are still available via this endpoint, but new campaign replies and other Inbox messages aren’t available using this endpoint.
            {
                "name": "get_conversations_id_messages_id",
                "table_name": "message",
                "endpoint": {
                    "path": "/conversations/{conversation_id}/messages/{message_id}",
                    "params": {
                        "conversation_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "message_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get recent notes for a specific list member.
            {
                "name": "get_lists_id_members_id_notes",
                "table_name": "note",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/notes",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a specific note for a specific list member.
            {
                "name": "get_lists_id_members_id_notes_id",
                "table_name": "note",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/notes/{note_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "note_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get detailed information about any campaign emails that were opened by a list member.
            {
                "name": "get_reports_id_open_details",
                "table_name": "open_detail",
                "endpoint": {
                    "path": "/reports/{campaign_id}/open-details",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific subscriber who opened a campaign.
            {
                "name": "get_reports_id_open_details_id_members_id",
                "table_name": "open_detail",
                "endpoint": {
                    "path": "/reports/{campaign_id}/open-details/{subscriber_hash}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about an account's orders.
            {
                "name": "get_ecommerce_orders",
                "table_name": "order",
                "endpoint": {
                    "path": "/ecommerce/orders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "campaign_id": "OPTIONAL_CONFIG",
                        # "outreach_id": "OPTIONAL_CONFIG",
                        # "customer_id": "OPTIONAL_CONFIG",
                        # "has_outreach": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a store's orders.
            {
                "name": "get_ecommerce_stores_id_orders",
                "table_name": "order",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/orders",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "customer_id": "OPTIONAL_CONFIG",
                        # "has_outreach": "OPTIONAL_CONFIG",
                        # "campaign_id": "OPTIONAL_CONFIG",
                        # "outreach_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific order.
            {
                "name": "get_ecommerce_stores_id_orders_id",
                "table_name": "order",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/orders/{order_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # A health check for the API that won't return any account-specific information.
            {
                "name": "get_ping",
                "table_name": "ping",
                "endpoint": {
                    "path": "/ping",
                    "paginator": "auto",
                },
            },
            # Get information about a store's products.
            {
                "name": "get_ecommerce_stores_id_products",
                "table_name": "product",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/products",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific product.
            {
                "name": "get_ecommerce_stores_id_products_id",
                "table_name": "product",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/products/{product_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "product_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a store's promo codes.
            {
                "name": "get_ecommerce_stores_id_promocodes",
                "table_name": "promo_code",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promo_rule_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific promo code.
            {
                "name": "get_ecommerce_stores_id_promocodes_id",
                "table_name": "promo_code",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}/promo-codes/{promo_code_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promo_rule_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promo_code_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a store's promo rules.
            {
                "name": "get_ecommerce_stores_id_promorules",
                "table_name": "promo_rule",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/promo-rules",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific promo rule.
            {
                "name": "get_ecommerce_stores_id_promorules_id",
                "table_name": "promo_rule",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/promo-rules/{promo_rule_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promo_rule_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get reports for survey questions.
            {
                "name": "get_reporting_surveys_id_questions",
                "table_name": "question",
                "endpoint": {
                    "path": "/reporting/surveys/{survey_id}/questions",
                    "params": {
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get report for a survey question.
            {
                "name": "get_reporting_surveys_id_questions_id",
                "table_name": "question",
                "endpoint": {
                    "path": "/reporting/surveys/{survey_id}/questions/{question_id}",
                    "params": {
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "question_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a classic automation email queue.
            {
                "name": "get_automations_id_emails_id_queue",
                "table_name": "queue",
                "endpoint": {
                    "path": "/automations/{workflow_id}/emails/{workflow_email_id}/queue",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "workflow_email_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific subscriber in a classic automation email queue.
            {
                "name": "get_automations_id_emails_id_queue_id",
                "table_name": "queue",
                "endpoint": {
                    "path": "/automations/{workflow_id}/emails/{workflow_email_id}/queue/{subscriber_hash}",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "workflow_email_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about subscribers who were removed from a classic automation workflow.
            {
                "name": "get_automations_id_removed_subscribers",
                "table_name": "removed_subscriber",
                "endpoint": {
                    "path": "/automations/{workflow_id}/removed-subscribers",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific subscriber who was removed from a classic automation workflow.
            {
                "name": "get_automations_id_removed_subscribers_id",
                "table_name": "removed_subscriber",
                "endpoint": {
                    "path": "/automations/{workflow_id}/removed-subscribers/{subscriber_hash}",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get campaign reports.
            {
                "name": "get_reports",
                "table_name": "report",
                "endpoint": {
                    "path": "/reports",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "before_send_time": "OPTIONAL_CONFIG",
                        # "since_send_time": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get report details for a specific sent campaign.
            {
                "name": "get_reports_id",
                "table_name": "report",
                "endpoint": {
                    "path": "/reports/{campaign_id}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get responses to a survey.
            {
                "name": "get_reporting_surveys_id_responses",
                "table_name": "response",
                "endpoint": {
                    "path": "/reporting/surveys/{survey_id}/responses",
                    "params": {
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "answered_question": "OPTIONAL_CONFIG",
                        # "chose_answer": "OPTIONAL_CONFIG",
                        # "respondent_familiarity_is": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a single survey response.
            {
                "name": "get_reporting_surveys_id_responses_id",
                "table_name": "response",
                "endpoint": {
                    "path": "/reporting/surveys/{survey_id}/responses/{response_id}",
                    "params": {
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "response_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search all campaigns for the specified query terms.
            {
                "name": "get_search_campaigns",
                "table_name": "search_campaign",
                "endpoint": {
                    "path": "/search-campaigns",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for list members. This search can be restricted to a specific list, or can be used to search across all lists in an account.
            {
                "name": "get_search_members",
                "table_name": "search_member",
                "endpoint": {
                    "path": "/search-members",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "list_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about all available segments for a specific list.
            {
                "name": "preview_a_segment",
                "table_name": "segment",
                "endpoint": {
                    "path": "/lists/{list_id}/segments",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "since_created_at": "OPTIONAL_CONFIG",
                        # "before_created_at": "OPTIONAL_CONFIG",
                        # "include_cleaned": "OPTIONAL_CONFIG",
                        # "include_transactional": "OPTIONAL_CONFIG",
                        # "include_unsubscribed": "OPTIONAL_CONFIG",
                        # "since_updated_at": "OPTIONAL_CONFIG",
                        # "before_updated_at": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific segment.
            {
                "name": "get_lists_id_segments_id",
                "table_name": "segment",
                "endpoint": {
                    "path": "/lists/{list_id}/segments/{segment_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "segment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "include_cleaned": "OPTIONAL_CONFIG",
                        # "include_transactional": "OPTIONAL_CONFIG",
                        # "include_unsubscribed": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Review the send checklist for a campaign, and resolve any issues before sending.
            {
                "name": "get_campaigns_id_send_checklist",
                "table_name": "send_checklist",
                "endpoint": {
                    "path": "/campaigns/{campaign_id}/send-checklist",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about campaign recipients.
            {
                "name": "get_reports_id_sent_to",
                "table_name": "sent_to",
                "endpoint": {
                    "path": "/reports/{campaign_id}/sent-to",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific campaign recipient.
            {
                "name": "get_reports_id_sent_to_id",
                "table_name": "sent_to",
                "endpoint": {
                    "path": "/reports/{campaign_id}/sent-to/{subscriber_hash}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get signup forms for a specific list.
            {
                "name": "get_lists_id_signup_forms",
                "table_name": "signup_form",
                "endpoint": {
                    "path": "/lists/{list_id}/signup-forms",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about all stores in the account.
            {
                "name": "get_ecommerce_stores",
                "table_name": "store",
                "endpoint": {
                    "path": "/ecommerce/stores",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific store.
            {
                "name": "get_ecommerce_stores_id",
                "table_name": "store",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of reports with child campaigns for a specific parent campaign.
            {
                "name": "get_reports_id_sub_reports_id",
                "table_name": "sub_report",
                "endpoint": {
                    "path": "/reports/{campaign_id}/sub-reports",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about all available surveys for a specific list.
            {
                "name": "get_lists_id_surveys",
                "table_name": "survey",
                "endpoint": {
                    "path": "/lists/{list_id}/surveys",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get details about a specific survey.
            {
                "name": "get_lists_id_surveys_id",
                "table_name": "survey",
                "endpoint": {
                    "path": "/lists/{list_id}/surveys/{survey_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get reports for surveys.
            {
                "name": "get_reporting_surveys",
                "table_name": "survey",
                "endpoint": {
                    "path": "/reporting/surveys",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get report for a survey.
            {
                "name": "get_reporting_surveys_id",
                "table_name": "survey",
                "endpoint": {
                    "path": "/reporting/surveys/{survey_id}",
                    "params": {
                        "survey_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the tags on a list member.
            {
                "name": "get_list_member_tags",
                "table_name": "tag",
                "endpoint": {
                    "path": "/lists/{list_id}/members/{subscriber_hash}/tags",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Search for tags on a list by name. If no name is provided, will return all tags on the list.
            {
                "name": "search_tags_by_name",
                "table_name": "tag_search",
                "endpoint": {
                    "path": "/lists/{list_id}/tag-search",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "name": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of an account's available templates.
            {
                "name": "get_templates",
                "table_name": "template",
                "endpoint": {
                    "path": "/templates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                        # "created_by": "OPTIONAL_CONFIG",
                        # "since_date_created": "OPTIONAL_CONFIG",
                        # "before_date_created": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "category": "OPTIONAL_CONFIG",
                        # "folder_id": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "content_type": "OPTIONAL_CONFIG",
                        # "sort_dir": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific template.
            {
                "name": "get_templates_id",
                "table_name": "template",
                "endpoint": {
                    "path": "/templates/{template_id}",
                    "params": {
                        "template_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all folders used to organize templates.
            {
                "name": "get_template_folders",
                "table_name": "template_folder",
                "endpoint": {
                    "path": "/template-folders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific folder used to organize templates.
            {
                "name": "get_template_folders_id",
                "table_name": "template_folder",
                "endpoint": {
                    "path": "/template-folders/{folder_id}",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about members who have unsubscribed from a specific campaign.
            {
                "name": "get_reports_id_unsubscribed",
                "table_name": "unsubscribed",
                "endpoint": {
                    "path": "/reports/{campaign_id}/unsubscribed",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific list member who unsubscribed from a campaign.
            {
                "name": "get_reports_id_unsubscribed_id",
                "table_name": "unsubscribed",
                "endpoint": {
                    "path": "/reports/{campaign_id}/unsubscribed/{subscriber_hash}",
                    "params": {
                        "campaign_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriber_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a product's variants.
            {
                "name": "get_ecommerce_stores_id_products_id_variants",
                "table_name": "variant",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "product_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific product variant.
            {
                "name": "get_ecommerce_stores_id_products_id_variants_id",
                "table_name": "variant",
                "endpoint": {
                    "path": "/ecommerce/stores/{store_id}/products/{product_id}/variants/{variant_id}",
                    "params": {
                        "store_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "product_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "variant_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "exclude_fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the details for a single domain on the account.
            {
                "name": "get_verified_domain",
                "table_name": "verified_domain",
                "endpoint": {
                    "path": "/verified-domains/{domain_name}",
                    "params": {
                        "domain_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all of the sending domains on the account.
            {
                "name": "get_verified_domains",
                "table_name": "verified_domain",
                "endpoint": {
                    "path": "/verified-domains",
                    "paginator": "auto",
                },
            },
            # Get information about all webhooks for a specific list.
            {
                "name": "get_lists_id_webhooks",
                "table_name": "webhook",
                "endpoint": {
                    "path": "/lists/{list_id}/webhooks",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get information about a specific webhook.
            {
                "name": "get_lists_id_webhooks_id",
                "table_name": "webhook",
                "endpoint": {
                    "path": "/lists/{list_id}/webhooks/{webhook_id}",
                    "params": {
                        "list_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webhook_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
