from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="keap_source", max_table_nesting=2)
def keap_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "offset",
                "limit": 20,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "count",
            },
        },
        "resources": [
            # Retrieves a list of all affiliates
            {
                "name": "list_affiliates_using_get",
                "table_name": "affiliate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "affiliates",
                    "path": "/v1/affiliates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "code": "OPTIONAL_CONFIG",
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                        # "parent_id": "OPTIONAL_CONFIG",
                        # "program_id": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a single affiliate
            {
                "name": "get_affiliate_using_get",
                "table_name": "affiliate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/affiliates/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "list_affiliates_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieve a list of Commissions based on Affiliate or Date Range
            {
                "name": "list_commissions_using_get",
                "table_name": "affiliate_commission",
                "endpoint": {
                    "data_selector": "commissions",
                    "path": "/v1/affiliates/commissions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "affiliateId": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of Commission Programs
            {
                "name": "list_programs_using_get",
                "table_name": "affiliate_program",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "programs",
                    "path": "/v1/affiliates/programs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "affiliate_id": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all affiliate redirects
            {
                "name": "list_affiliate_redirect_links_using_get",
                "table_name": "affiliate_redirect",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "redirects",
                    "path": "/v1/affiliates/redirectlinks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "affiliate_id": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of affiliate summaries
            {
                "name": "list_summaries_using_get",
                "table_name": "affiliate_summary",
                "endpoint": {
                    "data_selector": "summaries",
                    "path": "/v1/affiliates/summaries",
                    "params": {
                        # the parameters below can optionally be configured
                        # "affiliate_ids": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves all appointments for the authenticated user
            {
                "name": "list_appointments_using_get",
                "table_name": "appointment",
                "endpoint": {
                    "data_selector": "appointments",
                    "path": "/v1/appointments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a specific appointment with respect to user permissions. The authenticated user will need the "can view all records" permission for Task/Appt/Notes
            {
                "name": "get_appointment_using_get",
                "table_name": "appointment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/appointments/{appointmentId}",
                    "params": {
                        "appointmentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all campaigns for the authenticated user
            {
                "name": "list_campaigns_using_get",
                "table_name": "campaign",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "campaigns",
                    "path": "/v1/campaigns",
                    "params": {
                        # the parameters below can optionally be configured
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                        # "search_text": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single campaign
            {
                "name": "get_campaign_using_get",
                "table_name": "campaign_with_stats",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/campaigns/{campaignId}",
                    "params": {
                        "campaignId": {
                            "type": "resolve",
                            "resource": "list_campaigns_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "optional_properties": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all companies
            {
                "name": "list_companies_using_get",
                "table_name": "company",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "companies",
                    "path": "/v1/companies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "company_name": "OPTIONAL_CONFIG",
                        # "optional_properties": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single company
            {
                "name": "get_company_using_get",
                "table_name": "company",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/companies/{companyId}",
                    "params": {
                        "companyId": {
                            "type": "resolve",
                            "resource": "list_companies_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "optional_properties": "OPTIONAL_CONFIG",
                    },
                },
            },
            # List all Credit Cards on a contact
            {
                "name": "list_credit_cards_using_get",
                "table_name": "contact_credit_card",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/contacts/{contactId}/creditCards",
                    "params": {
                        "contactId": {
                            "type": "resolve",
                            "resource": "list_contacts_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of tags applied to a given contact
            {
                "name": "list_applied_tags_using_get",
                "table_name": "contact_tag",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/v1/contacts/{contactId}/tags",
                    "params": {
                        "contactId": {
                            "type": "resolve",
                            "resource": "list_contacts_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            {
                "name": "list_countries_using_get",
                "table_name": "country",
                "endpoint": {
                    "data_selector": "countries",
                    "path": "/v1/locales/countries",
                },
            },
            # Get the custom fields for the Affiliate object
            {
                "name": "retrieve_affiliate_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/affiliates/model",
                },
            },
            # Get the custom fields for the Appointment object
            {
                "name": "retrieve_appointment_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/appointments/model",
                },
            },
            # Get the custom fields and optional properties for the Company object
            {
                "name": "retrieve_company_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/companies/model",
                },
            },
            # Get the custom fields and optional properties for the Contact object
            {
                "name": "retrieve_contact_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/contacts/model",
                },
            },
            # Get the custom fields for the Note object
            {
                "name": "retrieve_note_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/notes/model",
                },
            },
            # Get the custom fields for the Opportunity object
            {
                "name": "retrieve_opportunity_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/opportunities/model",
                },
            },
            # Get the custom fields for the Order object
            {
                "name": "retrieve_order_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/orders/model",
                },
            },
            # Get the custom fields for the Subscription object
            {
                "name": "retrieve_subscription_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/subscriptions/model",
                },
            },
            # Get the custom fields for the Task object
            {
                "name": "retrieve_task_model_using_get",
                "table_name": "custom_field_meta_data",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_fields",
                    "path": "/v1/tasks/model",
                },
            },
            {
                "name": "default_options_using_get",
                "table_name": "default_option",
                "endpoint": {
                    "data_selector": "contact_types",
                    "path": "/v1/locales/defaultOptions",
                },
            },
            # Retrieves a list of all orders using the specified search criteria. Each order may or may not have items.  Potential values for order status:`DRAFT`, `SENT`, `VIEWED`, `PAID`
            {
                "name": "list_orders_using_get",
                "table_name": "ecommerce_reporting_order",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "orders",
                    "path": "/v1/orders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "paid": "OPTIONAL_CONFIG",
                        # "product_id": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single order. The order may or may not have items.  Potential values for order status:`DRAFT`, `SENT`, `VIEWED`, `PAID`
            {
                "name": "get_order_using_get",
                "table_name": "ecommerce_reporting_order",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/orders/{orderId}",
                    "params": {
                        "orderId": {
                            "type": "resolve",
                            "resource": "list_orders_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of all transactions on a given order using the specified search criteria
            {
                "name": "list_transactions_for_order_using_get",
                "table_name": "ecommerce_reporting_transaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "transactions",
                    "path": "/v1/orders/{orderId}/transactions",
                    "params": {
                        "orderId": {
                            "type": "resolve",
                            "resource": "list_orders_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list transactions for a given contact
            {
                "name": "list_transactions_using_get",
                "table_name": "ecommerce_reporting_transaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "transactions",
                    "path": "/v1/transactions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single transaction
            {
                "name": "get_transaction_using_get",
                "table_name": "ecommerce_reporting_transaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/transactions/{transactionId}",
                    "params": {
                        "transactionId": {
                            "type": "resolve",
                            "resource": "list_transactions_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # List Emails that have been sent to a Contact
            {
                "name": "list_emails_for_contact_using_get",
                "table_name": "email_sent_query_result",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "emails",
                    "path": "/v1/contacts/{contactId}/emails",
                    "params": {
                        "contactId": {
                            "type": "resolve",
                            "resource": "list_contacts_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "email": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of emails that have been sent  Keap is currently investigating an issue with degraded performance of this endpoint with very large (millions of records) record sets
            {
                "name": "list_emails_using_get",
                "table_name": "email_sent_query_result",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "emails",
                    "path": "/v1/emails",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                        # "ordered": "true",
                        # "since_sent_date": "OPTIONAL_CONFIG",
                        # "until_sent_date": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single email that has been sent
            {
                "name": "get_email_using_get",
                "table_name": "email_sent_query_result_with_content",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/emails/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "list_emails_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # List the available types of Events that can be listened to
            {
                "name": "list_hook_event_types",
                "table_name": "event_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/hooks/event_keys",
                },
            },
            # Retrieves a list of all files
            {
                "name": "list_files_using_get",
                "table_name": "file_descriptor",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "files",
                    "path": "/v1/files",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                        # "permission": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "viewable": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves metadata about a specific file. Optionally returns the base64 encoded file data.
            {
                "name": "get_file_using_get",
                "table_name": "file_information",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/files/{fileId}",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "list_files_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "optional_properties": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single contact
            {
                "name": "get_contact_using_get",
                "table_name": "full_contact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/contacts/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "list_contacts_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "optional_properties": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of payments made against a given order, including historical or external payments of cash or credit card.
            {
                "name": "list_order_payments_using_get",
                "table_name": "invoice_payment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/orders/{orderId}/payments",
                    "params": {
                        "orderId": {
                            "type": "resolve",
                            "resource": "list_orders_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of all merchant accounts
            {
                "name": "get_merchant_accounts_using_get",
                "table_name": "merchant",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "merchant_accounts",
                    "path": "/v1/merchants",
                },
            },
            # Retrieves a list of all notes
            {
                "name": "list_notes_using_get",
                "table_name": "note",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "notes",
                    "path": "/v1/notes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "user_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single note
            {
                "name": "get_note_using_get",
                "table_name": "note",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/notes/{noteId}",
                    "params": {
                        "noteId": {
                            "type": "resolve",
                            "resource": "list_notes_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of all opportunities.  Please note: the sample response erroneously shows properties, such as _stage reasons_, that are unavailable through the list endpoint. Such properties are only available through the retrieve operation. Future versions of the Opportunity resource will correct the oversight.
            {
                "name": "list_opportunities_using_get",
                "table_name": "opportunity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "opportunities",
                    "path": "/v1/opportunities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "order": "OPTIONAL_CONFIG",
                        # "search_term": "OPTIONAL_CONFIG",
                        # "stage_id": "OPTIONAL_CONFIG",
                        # "user_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrives a single opportunity
            {
                "name": "get_opportunity_using_get",
                "table_name": "opportunity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/opportunities/{opportunityId}",
                    "params": {
                        "opportunityId": {
                            "type": "resolve",
                            "resource": "list_opportunities_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "optional_properties": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all products
            {
                "name": "list_products_using_get",
                "table_name": "product",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "products",
                    "path": "/v1/products",
                    "params": {
                        # the parameters below can optionally be configured
                        # "active": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "retrieve_product_using_get",
                "table_name": "product",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/products/{productId}",
                    "params": {
                        "productId": {
                            "type": "resolve",
                            "resource": "list_products_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # The Sync endpoint returns a set of products that have been updated or created since the last result set was retrieved, minus any products that have been deleted.
            {
                "name": "list_products_from_sync_token_using_get",
                "table_name": "product_status",
                "endpoint": {
                    "data_selector": "product_statuses",
                    "path": "/v1/products/sync",
                    "params": {
                        # the parameters below can optionally be configured
                        # "sync_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "retrieve_product_subscription_using_get",
                "table_name": "product_subscription",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/products/{productId}/subscriptions/{subscriptionId}",
                    "params": {
                        "subscriptionId": {
                            "type": "resolve",
                            "resource": "list_products_using_get",
                            "field": "id",
                        },
                        "productId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves profile/company info for an account.
            {
                "name": "get_account_profile_using_get",
                "table_name": "profile",
                "endpoint": {
                    "data_selector": "business_goals",
                    "path": "/v1/account/profile",
                },
            },
            {
                "name": "list_countries_using_get_1",
                "table_name": "province",
                "endpoint": {
                    "data_selector": "provinces",
                    "path": "/v1/locales/countries/{countryCode}/provinces",
                    "params": {
                        "countryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves a list of all affiliate clawbacks
            {
                "name": "list_affiliate_clawbacks_using_get",
                "table_name": "rest_affiliate_clawback",
                "endpoint": {
                    "data_selector": "clawbacks",
                    "path": "/v1/affiliates/{affiliateId}/clawbacks",
                    "params": {
                        "affiliateId": {
                            "type": "resolve",
                            "resource": "list_affiliates_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all affiliate payments
            {
                "name": "list_payments_using_get",
                "table_name": "rest_affiliate_payment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "payments",
                    "path": "/v1/affiliates/{affiliateId}/payments",
                    "params": {
                        "affiliateId": {
                            "type": "resolve",
                            "resource": "list_affiliates_using_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the properties for the current application's configuration
            {
                "name": "get_configuration_using_get",
                "table_name": "rest_application_configuration",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/setting/application/configuration",
                },
            },
            # Lists your hook subscriptions.
            {
                "name": "list_stored_hook_subscriptions",
                "table_name": "rest_hook",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/hooks",
                },
            },
            # Retrieves an existing hook subscription and its status.  If your hook subscription becomes inactive, you may request an activation attempt via [Verify a Hook Subscription](#!/REST_Hooks/verify_a_hook_subscription).
            {
                "name": "retrieve_a_hook_subscription",
                "table_name": "rest_hook",
                "primary_key": "key",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/hooks/{key}",
                    "params": {
                        "key": {
                            "type": "resolve",
                            "resource": "list_stored_hook_subscriptions",
                            "field": "key",
                        },
                    },
                },
            },
            # Retrieves a list of all contacts
            {
                "name": "list_contacts_using_get",
                "table_name": "rest_partial_contact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "contacts",
                    "path": "/v1/contacts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "email": "OPTIONAL_CONFIG",
                        # "family_name": "OPTIONAL_CONFIG",
                        # "given_name": "OPTIONAL_CONFIG",
                        # "optional_properties": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "order_direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all users
            {
                "name": "list_users_using_get",
                "table_name": "rest_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "users",
                    "path": "/v1/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "include_inactive": "OPTIONAL_CONFIG",
                        # "include_partners": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of all opportunity stages with pipeline details
            {
                "name": "list_opportunity_stage_pipelines_using_get",
                "table_name": "sales_pipeline",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/opportunity/stage_pipeline",
                },
            },
            # Retrieves whether the application is enabled
            {
                "name": "get_application_enabled_using_get",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/setting/application/enabled",
                },
            },
            # Lists the Contact types in a comma-separated list.   *Note:* This is now provided by GET /setting/application/configuration
            {
                "name": "get_contact_option_types_using_get",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/setting/contact/optionTypes",
                },
            },
            # Retrieves a HTML snippet that contains the user's email signature.
            {
                "name": "get_user_signature_using_get",
                "table_name": "signature",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{userId}/signature",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "list_users_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of all subcriptions using the specified search criteria.
            {
                "name": "list_subscriptions_using_get",
                "table_name": "subscription",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "subscriptions",
                    "path": "/v1/subscriptions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "contact_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of tags defined in the application
            {
                "name": "list_tags_using_get",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/v1/tags",
                    "params": {
                        # the parameters below can optionally be configured
                        # "category": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single tag
            {
                "name": "get_tag_using_get",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/tags/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "list_tags_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of companies that have the given tag applied
            {
                "name": "list_companies_for_tag_id_using_get",
                "table_name": "tagged_company",
                "endpoint": {
                    "data_selector": "companies",
                    "path": "/v1/tags/{tagId}/companies",
                    "params": {
                        "tagId": {
                            "type": "resolve",
                            "resource": "list_tags_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of contacts that have the given tag applied
            {
                "name": "list_contacts_for_tag_id_using_get",
                "table_name": "tagged_contact",
                "endpoint": {
                    "data_selector": "contacts",
                    "path": "/v1/tags/{tagId}/contacts",
                    "params": {
                        "tagId": {
                            "type": "resolve",
                            "resource": "list_tags_using_get",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of all tasks using the specified search criteria
            {
                "name": "list_tasks_using_get",
                "table_name": "task",
                "endpoint": {
                    "data_selector": "tasks",
                    "path": "/v1/tasks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "completed": "OPTIONAL_CONFIG",
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "has_due_date": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                        # "user_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves Tasks belonging to the authenticated user using the specified search criteria
            {
                "name": "list_tasks_for_current_user_using_get",
                "table_name": "task",
                "endpoint": {
                    "data_selector": "tasks",
                    "path": "/v1/tasks/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "completed": "OPTIONAL_CONFIG",
                        # "contact_id": "OPTIONAL_CONFIG",
                        # "has_due_date": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                        # "user_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single task
            {
                "name": "get_task_using_get",
                "table_name": "task",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/tasks/{taskId}",
                    "params": {
                        "taskId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves information for the current authenticated end-user, as outlined by the [OpenID Connect specification](http://openid.net/specs/openid-connect-core-1_0.html#UserInfo).
            {
                "name": "get_user_info_using_get",
                "table_name": "user_info_dto",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/oauth/connect/userinfo",
                },
            },
        ],
    }

    return rest_api_source(source_config)
