from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="zuora_source", max_table_nesting=2)
def zuora_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves detailed information about all the entities that a user has permission to access.  ## User Access Permission You can make the call as any entity user.
            {
                "name": "get_entities_user_accessible",
                "table_name": "accessible_entity",
                "endpoint": {
                    "path": "/v1/users/{username}/accessible-entities",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves basic information about a customer account.  This operation is a quick retrieval that doesn't include the account's subscriptions, invoices, payments, or usage details. Use Get account summary to get more detailed information about an account.
            {
                "name": "get_account",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/accounts/{account-key}",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the information about one specific account.
            {
                "name": "object_get_account",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/object/account/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This REST API reference describes how to retrieve all credit card information for the specified customer account.   ## Notes The response includes details of credit or debit cards for the specified customer account. Card numbers are masked, e.g., "************1234". Cards are returned in reverse chronological order of last update.  Though you can also send requests for bank transfer, ACH, or other supported payment methods, the response will not include effective details of these payment methods.
            {
                "name": "get_payment_methods_credit_card",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/payment-methods/credit-cards/accounts/{account-key}",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # Retrieves all subscriptions associated with the specified account. Zuora only returns the latest version of the subscriptions.  Subscription data is returned in reverse chronological order based on `updatedDate`.
            {
                "name": "get_subscriptions_by_account",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/subscriptions/accounts/{account-key}",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "charge-detail": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves invoices for a specified account.  Invoices are returned in reverse chronological order by **updatedDate**.  For a use case of this operation, see [View invoices](https://www.zuora.com/developer/api-guides/#View-invoices).
            {
                "name": "get_transaction_invoice",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/transactions/invoices/accounts/{account-key}",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # Retrieves payments for a specified account. Payments are returned in reverse chronological order by **updatedDate**.
            {
                "name": "get_transaction_payment",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/transactions/payments/accounts/{account-key}",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # This REST API reference describes how to retrieve usage details for an account. Usage data is returned in reverse chronological order.
            {
                "name": "get_usage",
                "table_name": "account",
                "endpoint": {
                    "path": "/v1/usage/accounts/{account-key}",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # This reference describes how to query all accounting codes in your chart of accounts through the REST API.
            {
                "name": "get_all_accounting_codes",
                "table_name": "accounting_code",
                "endpoint": {
                    "path": "/v1/accounting-codes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "300",
                    },
                },
            },
            # This reference describes how to query an accounting code through the REST API.
            {
                "name": "get_accounting_code",
                "table_name": "accounting_code",
                "endpoint": {
                    "path": "/v1/accounting-codes/{ac-id}",
                    "params": {
                        "ac-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all accounting periods on your tenant.
            {
                "name": "get_all_accounting_periods",
                "table_name": "accounting_period",
                "endpoint": {
                    "path": "/v1/accounting-periods",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "300",
                    },
                },
            },
            # Retrieves an accounting period. Prerequisites -------------  You must have Zuora Finance enabled on your tenant.
            {
                "name": "get_accounting_period",
                "table_name": "accounting_period",
                "endpoint": {
                    "path": "/v1/accounting-periods/{ap-id}",
                    "params": {
                        "ap-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves detailed information about the specified subscription amendment.
            {
                "name": "get_amendments_by_key",
                "table_name": "amendment",
                "endpoint": {
                    "path": "/v1/amendments/{amendment-key}",
                    "params": {
                        "amendment-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_amendment",
                "table_name": "amendment",
                "endpoint": {
                    "path": "/v1/object/amendment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves information about the payments or credit memos that are applied to a specified debit memo.
            {
                "name": "get_debit_memo_application_parts",
                "table_name": "application_part",
                "endpoint": {
                    "path": "/v1/debitmemos/{debitMemoId}/application-parts",
                    "params": {
                        "debitMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about the payments or credit memos that are applied to a specified invoice.
            {
                "name": "get_invoice_application_parts",
                "table_name": "application_part",
                "endpoint": {
                    "path": "/v1/invoices/{invoiceId}/application-parts",
                    "params": {
                        "invoiceId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. Orders is now generally available as of Zuora Billing Release 284 (August 2020). If you are an existing Zuora Subscribe and Amend customer and want to adopt Orders, see [What is Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization#What_is_Orders_Harmonization.3F) and join the [Orders Harmonization community group](https://community.zuora.com/t5/Orders-Harmonization/gp-p/Orders-Harmonization) for more information. If you want to enable Orders, submit a request at [Zuora Global Support](https://support.zuora.com/).  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Get the status and response of an asynchronous job. Currently, an asynchronous job created by "Create an order asynchronously" or "Preview an order asynchronously" is supported.
            {
                "name": "get_job_status_and_response",
                "table_name": "async_job",
                "endpoint": {
                    "path": "/v1/async-jobs/{jobId}",
                    "params": {
                        "jobId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Use the View Attachment REST request to retrieve information about an attachment document.
            {
                "name": "get_attachments",
                "table_name": "attachment",
                "endpoint": {
                    "path": "/v1/attachments/{attachment-id}",
                    "params": {
                        "attachment-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Use the View Attachment REST request to get a list of attachments on an account, an invoice, a subscription, a credit memo, or a debit memo.  **Note**: The Credit and Debit Memos feature is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.
            {
                "name": "get_attachments_list",
                "table_name": "attachment",
                "endpoint": {
                    "path": "/v1/attachments/{object-type}/{object-key}",
                    "params": {
                        "object-type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "object-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # Retrieves information about a bill run.    Business operations depending on the completion of the bill run will not be available while the bill run query returns `PostInProgress`. Upon completion of the bill run, a query will return `Posted`.
            {
                "name": "object_get_bill_run",
                "table_name": "bill_run",
                "endpoint": {
                    "path": "/v1/object/bill-run/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the information about all billing documents associated with a specified account. The billing documents contain invoices, credit memos, and debit memos.   To retrieve information about credit memos and debit memos, you must have the Invoice Settlement feature enabled.   You can use query parameters to restrict the data returned in the response.  Examples: - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1&sort=+documentDate - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1&status=Posted
            {
                "name": "get_billing_documents",
                "table_name": "billing_document",
                "endpoint": {
                    "path": "/v1/billing-documents",
                    "params": {
                        "accountId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "documentDate": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a preview of future invoice items for multiple customer accounts through a billing preview run. If you have the Invoice Settlement feature enabled,  you can also retrieve a preview of future credit memo items. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   A billing preview run asynchronously generates a downloadable CSV file containing a preview of invoice item data and credit memo item data for a batch of customer accounts.
            {
                "name": "get_billing_preview_run",
                "table_name": "billing_preview_run",
                "endpoint": {
                    "path": "/v1/billing-preview-runs/{billingPreviewRunId}",
                    "params": {
                        "billingPreviewRunId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Describes how to get information about the result of a mass action through the REST API.
            {
                "name": "get_mass_updater",
                "table_name": "bulk",
                "endpoint": {
                    "path": "/v1/bulk/{bulk-key}",
                    "params": {
                        "bulk-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Describes how to get a notification history for callouts.
            {
                "name": "get_callout_history",
                "table_name": "callout",
                "endpoint": {
                    "path": "/v1/notification-history/callout",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "endTime": "OPTIONAL_CONFIG",
                        # "startTime": "OPTIONAL_CONFIG",
                        # "objectId": "OPTIONAL_CONFIG",
                        # "failedOnly": "OPTIONAL_CONFIG",
                        # "eventCategory": "OPTIONAL_CONFIG",
                        # "includeResponseContent": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves key charge metrics about rate plan charges that have changes in a specified time range.  The purpose of `fromTimestamp` and `toTimestamp` is to synchronize charge metrics data incrementally.
            {
                "name": "get_charge_metrics",
                "table_name": "charge_metric",
                "endpoint": {
                    "path": "/charge-metrics/data/charge-metrics",
                    "params": {
                        "fromTimestamp": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "toTimestamp": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Retrieves discount allocation details about rate plan charges that have changes in a specified time range.  The purpose of `fromTimestamp` and `toTimestamp` is to synchronize discount allocation details incrementally.
            {
                "name": "get_charge_metrics_discount_allocation_details",
                "table_name": "charge_metrics_discount_allocation_detail",
                "endpoint": {
                    "path": "/charge-metrics/data/charge-metrics-discount-allocation-detail",
                    "params": {
                        "fromTimestamp": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "toTimestamp": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Retrieves the details of a charge revenue summary by specifying the charge revenue summary number. The response includes all revenue items associated with the charge revenue summary.
            {
                "name": "get_crs_by_crs_number",
                "table_name": "charge_revenue_summary",
                "endpoint": {
                    "path": "/v1/charge-revenue-summaries/{crs-number}",
                    "params": {
                        "crs-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This REST API reference describes how to get the details for each revenue item in a charge revenue summary by specifying the charge revenue summary number. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_items_by_charge_revenue_summary_number",
                "table_name": "charge_revenue_summary",
                "endpoint": {
                    "path": "/v1/revenue-items/charge-revenue-summaries/{crs-number}",
                    "params": {
                        "crs-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "300",
                    },
                },
            },
            {
                "name": "object_get_communication_profile",
                "table_name": "communication_profile",
                "endpoint": {
                    "path": "/v1/object/communication-profile/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves detailed information about a specific contact.
            {
                "name": "object_get_contact",
                "table_name": "contact",
                "endpoint": {
                    "path": "/v1/object/contact/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_credit_balance_adjustment",
                "table_name": "credit_balance_adjustment",
                "endpoint": {
                    "path": "/v1/object/credit-balance-adjustment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the details about a revenue schedule by specifying a valid credit memo item ID.
            {
                "name": "get_r_sby_credit_memo_item",
                "table_name": "credit_memo_item",
                "endpoint": {
                    "path": "/v1/revenue-schedules/credit-memo-items/{cmi-id}",
                    "params": {
                        "cmi-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all credit memos.   For a use case of this operation, see [Get credit memo](https://www.zuora.com/developer/api-guides/#Get-credit-memo).   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.     Examples:  - /v1/creditmemos?status=Posted  - /v1/creditmemos?referredInvoiceId=null&status=Draft  - /v1/creditmemos?status=Posted&type=External&sort=+number
            {
                "name": "get_credit_memos",
                "table_name": "creditmemo",
                "endpoint": {
                    "path": "/v1/creditmemos",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "amount": "OPTIONAL_CONFIG",
                        # "appliedAmount": "OPTIONAL_CONFIG",
                        # "autoApplyUponPosting": "OPTIONAL_CONFIG",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "creditMemoDate": "OPTIONAL_CONFIG",
                        # "currency": "OPTIONAL_CONFIG",
                        # "excludeFromAutoApplyRules": "OPTIONAL_CONFIG",
                        # "number": "OPTIONAL_CONFIG",
                        # "referredInvoiceId": "OPTIONAL_CONFIG",
                        # "refundAmount": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "targetDate": "OPTIONAL_CONFIG",
                        # "taxAmount": "OPTIONAL_CONFIG",
                        # "totalTaxExemptAmount": "OPTIONAL_CONFIG",
                        # "transferredToAccounting": "OPTIONAL_CONFIG",
                        # "unappliedAmount": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific credit memo.  For a use case of this operation, see [Get credit memo](https://www.zuora.com/developer/api-guides/#Get-credit-memo).
            {
                "name": "get_credit_memo",
                "table_name": "creditmemo",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   This reference describes how to query custom foreign exchange rates from Zuora. You can use this API method to query exchange rates only if you use a custom exchange rate provider and upload rates with the Import Foreign Exchange Rates mass action.
            {
                "name": "get_custom_exchange_rates",
                "table_name": "custom_exchange_rate",
                "endpoint": {
                    "path": "/v1/custom-exchange-rates/{currency}",
                    "params": {
                        "currency": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the details about a revenue schedule by specifying a valid debit memo item ID.
            {
                "name": "get_r_sby_debit_memo_item",
                "table_name": "debit_memo_item",
                "endpoint": {
                    "path": "/v1/revenue-schedules/debit-memo-items/{dmi-id}",
                    "params": {
                        "dmi-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about all debit memos associated with all customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos?status=Posted  - /v1/debitmemos?referredInvoiceId=null&status=Draft  - /v1/debitmemos?status=Posted&type=External&sort=+number
            {
                "name": "get_debit_memos",
                "table_name": "debitmemo",
                "endpoint": {
                    "path": "/v1/debitmemos",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "amount": "OPTIONAL_CONFIG",
                        # "balance": "OPTIONAL_CONFIG",
                        # "beAppliedAmount": "OPTIONAL_CONFIG",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "currency": "OPTIONAL_CONFIG",
                        # "debitMemoDate": "OPTIONAL_CONFIG",
                        # "dueDate": "OPTIONAL_CONFIG",
                        # "number": "OPTIONAL_CONFIG",
                        # "referredInvoiceId": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "targetDate": "OPTIONAL_CONFIG",
                        # "taxAmount": "OPTIONAL_CONFIG",
                        # "totalTaxExemptAmount": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific debit memo.
            {
                "name": "get_debit_memo",
                "table_name": "debitmemo",
                "endpoint": {
                    "path": "/v1/debitmemos/{debitMemoId}",
                    "params": {
                        "debitMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get all custom objects definitions for a given tenant. If you want to copy all the existing custom objects from an old tenant to a new tenant, you can call this operation in your old tenant and then use its response directly as the request of the [Create custom object definitions](https://www.zuora.com/developer/api-reference/#operation/POST_CustomObjectDefinitions) call in the new tenant to import all the custom objects from the old tenant.
            {
                "name": "get_all_custom_object_definitions_in_namespace",
                "table_name": "default",
                "endpoint": {
                    "path": "/objects/definitions/default",
                    "params": {
                        # the parameters below can optionally be configured
                        # "select": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the custom object definition by type for the given tenant.
            {
                "name": "get_custom_object_definition_by_type",
                "table_name": "default",
                "endpoint": {
                    "path": "/objects/definitions/default/{object}",
                    "params": {
                        "object": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all object records of the given type. You can also use the `q` query parameter to filter the output records.  ## Limitations   This call has the following limitations: * When a record is created, there will be a delay before it is available for search. For example, if you create 5 records and perform a query that these 5 records satisfy the query conditions, there will be a delay between when the 5 records are created, and when all the 5 records can be returned in the query result.
            {
                "name": "get_all_records_for_custom_object_type",
                "table_name": "default",
                "endpoint": {
                    "path": "/objects/records/default/{object}",
                    "params": {
                        "object": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "ids": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a record of a given type by ID.
            {
                "name": "get_custom_object_record_by_id",
                "table_name": "default",
                "endpoint": {
                    "path": "/objects/records/default/{object}/{id}",
                    "params": {
                        "object": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves information about an asynchronous job of permanently deleting all billing document PDF files for specific accounts.  **Note**: This operation can be used only if you have the Billing user permission "Hard Delete Billing Document Files" enabled.
            {
                "name": "get_billing_document_files_deletion_job",
                "table_name": "deletion_job",
                "endpoint": {
                    "path": "/v1/accounts/billing-documents/files/deletion-jobs/{jobId}",
                    "params": {
                        "jobId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Provides a reference listing of each object that is available in your Zuora tenant.  The information returned by this call is useful if you are using [CRUD: Create Export](https://www.zuora.com/developer/api-reference/#operation/Object_POSTExport) or the [AQuA API](https://knowledgecenter.zuora.com/DC_Developers/T_Aggregate_Query_API) to create a data source export. See [Export ZOQL](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL) for more information.  ## Response The response contains an XML document that lists the fields of the specified object. Each of the object's fields is represented by a `<field>` element in the XML document.      Each `<field>` element contains the following elements:  | Element      | Description                                                                                                                                                                                                                                                                                  | |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `<name>`     | API name of the field.                                                                                                                                                                                                                                                                       | | `<label>`    | Name of the field in the Zuora user interface.                                                                                                                                                                                                                                               | | `<type>`     | Data type of the field. The possible data types are: `boolean`, `date`, `datetime`, `decimal`, `integer`, `picklist`, `text`, `timestamp`, and `ZOQL`. If the data type is `picklist`, the `<field>` element contains an `<options>` element that lists the possible values of the field.    | | `<contexts>` | Specifies the availability of the field. If the `<contexts>` element lists the `export` context, the field is available for use in data source exports.                                                                                                                                                |  The `<field>` element contains other elements that provide legacy information about the field. This information is not directly related to the REST API.  Response sample: ```xml <?xml version="1.0" encoding="UTF-8"?> <object>   <name>ProductRatePlanCharge</name>   <label>Product Rate Plan Charge</label>   <fields>     ...     <field>       <name>TaxMode</name>       <label>Tax Mode</label>       <type>picklist</type>       <options>         <option>TaxExclusive</option>         <option>TaxInclusive</option>       </options>       <contexts>         <context>export</context>       </contexts>       ...     </field>     ...   </fields> </object> ```  It is strongly recommended that your integration checks `<contexts>` elements in the response. If your integration does not check `<contexts>` elements, your integration may process fields that are not available for use in data source exports. See [Changes to the Describe API](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL/Changes_to_the_Describe_API) for more information.
            {
                "name": "get_describe",
                "table_name": "describe",
                "endpoint": {
                    "path": "/v1/describe/{object}",
                    "params": {
                        "object": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This feature is available only if you have the Billing Document Properties Setup feature enabled. The Billing Document Properties Setup feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieve information about document properties of a billing document. Billing documents include invoices, credit memos, and debit memos.    **Note:** You can retrieve information about document properties of credit and debit memos only if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.
            {
                "name": "get_document_properies",
                "table_name": "document_property",
                "endpoint": {
                    "path": "/v1/document-properties/{documentType}/{documentId}",
                    "params": {
                        "documentType": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "documentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Describes how to get a notification history for notification emails.   ## Notes Request parameters and their values may be appended with a "?" following the HTTPS GET request.  Additional request parameter are separated by "&".   For example:  `GET https://rest.zuora.com/v1/notification-history/email?startTime=2015-01-12T00:00:00&endTime=2015-01-15T00:00:00&failedOnly=false&eventCategory=1000&pageSize=1`
            {
                "name": "get_email_history",
                "table_name": "email",
                "endpoint": {
                    "path": "/v1/notification-history/email",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "endTime": "OPTIONAL_CONFIG",
                        # "startTime": "OPTIONAL_CONFIG",
                        # "objectId": "OPTIONAL_CONFIG",
                        # "failedOnly": "OPTIONAL_CONFIG",
                        # "eventCategory": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Queries email templates.  **Note**: This operation is only applicable to email templates for custom events.
            {
                "name": "get_query_email_templates",
                "table_name": "email_template",
                "endpoint": {
                    "path": "/notifications/email-templates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "eventTypeName": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 100,
                        "offset_param": "start",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # Queries the email template of the specified ID.  **Note**: This operation is only applicable to email templates for custom events.
            {
                "name": "get_get_email_template",
                "table_name": "email_template",
                "endpoint": {
                    "path": "/notifications/email-templates/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    Retrieves detailed information of certain entities in a multi-entity hierarchy.   You can retrieve:   - Provisioned entities     - Unprovisioned entities     - Both provisioned and unprovisioned entities  ## User Access Permission  You can make the call as any entity user.
            {
                "name": "get_entities",
                "table_name": "entity",
                "endpoint": {
                    "path": "/v1/entities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provisioned": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves detailed information about a specified entity.  ## User Access Permission You can make the call as any entity user.
            {
                "name": "get_entity_by_id",
                "table_name": "entity",
                "endpoint": {
                    "path": "/v1/entities/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about certain connections for a specified entity. You can specify the entity to retrieve in the `Zuora-Entity-Ids` request header.  You can retrieve:  - Inbound connections  - Outbound connections  - Both inbound and outbound connections  ## User Access Permission You can make the call as any entity user.
            {
                "name": "get_entity_connections",
                "table_name": "entity_connection",
                "endpoint": {
                    "path": "/v1/entity-connections",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "30",
                        # "type": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists all errors for a custom object bulk job.
            {
                "name": "get_custom_object_bulk_job_errors",
                "table_name": "error",
                "endpoint": {
                    "path": "/objects/jobs/{id}/errors",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_event_triggers",
                "table_name": "event_trigger",
                "endpoint": {
                    "path": "/events/event-triggers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "baseObject": "OPTIONAL_CONFIG",
                        # "eventTypeName": "OPTIONAL_CONFIG",
                        # "active": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 10,
                        "offset_param": "start",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            {
                "name": "get_event_trigger",
                "table_name": "event_trigger",
                "endpoint": {
                    "path": "/events/event-triggers/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** As of Zuora Billing Release 306, Zuora has upgraded the methodologies for calculating metrics in [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders). The new methodologies are reflected in the following Order Delta Metrics objects.  * [Order Delta Mrr](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Mrr) * [Order Delta Tcv](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcv) * [Order Delta Tcb](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcb)  It is recommended that all customers use the new [Order Delta Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/AA_Overview_of_Order_Delta_Metrics). If you are an existing [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders) customer and want to migrate to Order Delta Metrics, submit a request at [Zuora Global Support](https://support.zuora.com/).  Whereas new customers, and existing customers not currently on [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders), will no longer have access to Order Metrics, existing customers currently using Order Metrics will continue to be supported.  **Note:** As of Zuora Billing Release 306, any new customers who onboard on [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) or [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) will no longer get this operation.   Retrieves the metrics of an evergreen subscription in a specified order.
            {
                "name": "get_order_metricsfor_evergreen_subscription",
                "table_name": "evergreen_metric",
                "endpoint": {
                    "path": "/v1/orders/{orderNumber}/evergreenMetrics/{subscriptionNumber}",
                    "params": {
                        "orderNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "subscriptionNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Use this operation to check the status of a data source export and access the exported data.  When you export data from Zuora, each exported file is available for download for 7 days. Data source exports (Export objects) older than 90 days are automatically deleted.
            {
                "name": "object_get_export",
                "table_name": "export",
                "endpoint": {
                    "path": "/v1/object/export/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Export a Workflow in a JSON document. This document can be used to create a copy of this workflow.
            {
                "name": "get_workflow_export",
                "table_name": "export",
                "endpoint": {
                    "path": "/workflows/{workflow_id}/export",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_feature",
                "table_name": "feature",
                "endpoint": {
                    "path": "/v1/object/feature/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve files such as export results, invoices, and accounting period reports.  The response content type depends on the type of file that you retrieve. For example, if you retrieve an invoice PDF, the value of the `Content-Type` header in the response is `application/pdf;charset=UTF-8`.  Other content types include:  - `text/csv` for CSV files - `application/msword` for Microsoft Word files - `application/vnd.ms-excel` and `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`   for Microsoft Excel files (*.xls* and *.xlsx* respectively) - `application/zip` and `application/x-gzip` for ZIP and Gzip files respectively - `text/html` for HTML files - `text/plain` for text files  The response always contains character encoding information in the `Content-Type` header. For example, `Content-Type: application/zip;charset=UTF-8`.  **Note:** The maximum file size is 2,047 MB. If you have a data request that exceeds this limit, Zuora returns the following 403 response: `<security:max-object-size>2047MB</security:max-object-size>`. Submit a request at <a href="http://support.zuora.com/" target="_blank">Zuora Global Support</a> to determine if large file optimization is an option for you.
            {
                "name": "get_files",
                "table_name": "file",
                "endpoint": {
                    "path": "/v1/files/{file-id}",
                    "params": {
                        "file-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the information about all PDF files of a specified invoice.   Invoice PDF files are returned in reverse chronological order by the value of the `versionNumber` field.  **Note**: This API only retrieves the PDF files that have been generated. If the latest PDF file is being generated, it will not be included in the response.  You can use the [Query](https://www.zuora.com/developer/api-reference/#operation/Action_POSTquery) action to get the latest PDF file, for example: `"select Body from Invoice where Id = '2c93808457d787030157e0324aea5158'"`.  See [Query an Invoice Body](https://knowledgecenter.zuora.com/Central_Platform/API/G_SOAP_API/E1_SOAP_API_Object_Reference/Invoice/Query_an_Invoice_Body_Field) for more information.
            {
                "name": "get_invoice_files",
                "table_name": "file",
                "endpoint": {
                    "path": "/v1/invoices/{invoiceId}/files",
                    "params": {
                        "invoiceId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # Retrieves payment run data and the processing result with details, if the `data` field was specified in the Create payment run operation.
            {
                "name": "get_payment_run_data",
                "table_name": "get_payment_run_data_element_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/v1/payment-runs/{paymentRunId}/data",
                    "params": {
                        "paymentRunId": {
                            "type": "resolve",
                            "resource": "get_payment_runs",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrives the summary of a payment run.
            {
                "name": "get_payment_run_summary",
                "table_name": "get_payment_run_summary_total_values",
                "endpoint": {
                    "data_selector": "totalValues",
                    "path": "/v1/payment-runs/{paymentRunId}/summary",
                    "params": {
                        "paymentRunId": {
                            "type": "resolve",
                            "resource": "get_payment_runs",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves the information about all payment runs. You can define filterable fields to restrict the data returned in the response.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/payment-runs?status=Processed  - /v1/payment-runs?targetDate=2017-10-10&status=Pending  - /v1/payment-runs?status=Completed&sort=+updatedDate
            {
                "name": "get_payment_runs",
                "table_name": "get_payment_run_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "paymentRuns",
                    "path": "/v1/payment-runs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "targetDate": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrives the information about a specific payment run.
            {
                "name": "get_payment_run",
                "table_name": "get_payment_run_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/payment-runs/{paymentRunId}",
                    "params": {
                        "paymentRunId": {
                            "type": "resolve",
                            "resource": "get_payment_runs",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the Payment Pages configuration metadata, specifically, page ID, page version, payment method type.  The following are the version-specific and general REST requests for Payment Pages:  * The request for Payment Pages 1.0 configuration information: `GET <BaseURL>/hostedpages?version=1` * The request for Payment Pages 2.0 configuration information: `GET <BaseURL>/hostedpages?version=2` * The request for all versions of Payment Pages configuration information: `GET <BaseURL>/hostedpages`  ## Notes If you do not have the corresponding tenant setting enabled, e.g., the request `version` parameter set to 2 with the Payment Pages 2.0 setting disabled, you will receive an error.
            {
                "name": "get_hosted_pages",
                "table_name": "hostedpage",
                "endpoint": {
                    "path": "/v1/hostedpages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "versionNumber": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_import",
                "table_name": "import",
                "endpoint": {
                    "path": "/v1/object/import/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_invoice",
                "table_name": "invoice",
                "endpoint": {
                    "path": "/v1/object/invoice/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_invoice_adjustment",
                "table_name": "invoice_adjustment",
                "endpoint": {
                    "path": "/v1/object/invoice-adjustment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_invoice_item",
                "table_name": "invoice_item",
                "endpoint": {
                    "path": "/v1/object/invoice-item/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the details of a revenue schedule by specifying the invoice item ID.
            {
                "name": "get_r_sby_invoice_item",
                "table_name": "invoice_item",
                "endpoint": {
                    "path": "/v1/revenue-schedules/invoice-items/{invoice-item-id}",
                    "params": {
                        "invoice-item-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_invoice_item_adjustment",
                "table_name": "invoice_item_adjustment",
                "endpoint": {
                    "path": "/v1/object/invoice-item-adjustment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the details of a revenue schedule by specifying a valid invoice item adjustment identifier. Request and response field descriptions and sample code are provided.
            {
                "name": "get_r_sby_invoice_item_adjustment",
                "table_name": "invoice_item_adjustment",
                "endpoint": {
                    "path": "/v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}",
                    "params": {
                        "invoice-item-adj-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about all orders for a specified invoice owner.
            {
                "name": "get_orders_by_invoice_owner",
                "table_name": "invoice_owner",
                "endpoint": {
                    "path": "/v1/orders/invoiceOwner/{accountNumber}",
                    "params": {
                        "accountNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "dateFilterOption": "OPTIONAL_CONFIG",
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_invoice_payment",
                "table_name": "invoice_payment",
                "endpoint": {
                    "path": "/v1/object/invoice-payment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_invoice_split",
                "table_name": "invoice_split",
                "endpoint": {
                    "path": "/v1/object/invoice-split/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_invoice_split_item",
                "table_name": "invoice_split_item",
                "endpoint": {
                    "path": "/v1/object/invoice-split-item/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a credit memo. A credit memo item is a single line item in a credit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:        - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100      - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate
            {
                "name": "get_credit_memo_items",
                "table_name": "item",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/items",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "amount": "OPTIONAL_CONFIG",
                        # "appliedAmount": "OPTIONAL_CONFIG",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "id": "OPTIONAL_CONFIG",
                        # "refundAmount": "OPTIONAL_CONFIG",
                        # "serviceEndDate": "OPTIONAL_CONFIG",
                        # "serviceStartDate": "OPTIONAL_CONFIG",
                        # "sku": "OPTIONAL_CONFIG",
                        # "skuName": "OPTIONAL_CONFIG",
                        # "sourceItemId": "OPTIONAL_CONFIG",
                        # "subscriptionId": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about a specific item of a credit memo. A credit memo item is a single line item in a credit memo.
            {
                "name": "get_credit_memo_item",
                "table_name": "item",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/items/{cmitemid}",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cmitemid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a debit memo. A debit memo item is a single line item in a debit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate
            {
                "name": "get_debit_memo_items",
                "table_name": "item",
                "endpoint": {
                    "path": "/v1/debitmemos/{debitMemoId}/items",
                    "params": {
                        "debitMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "amount": "OPTIONAL_CONFIG",
                        # "beAppliedAmount": "OPTIONAL_CONFIG",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "id": "OPTIONAL_CONFIG",
                        # "serviceEndDate": "OPTIONAL_CONFIG",
                        # "serviceStartDate": "OPTIONAL_CONFIG",
                        # "sku": "OPTIONAL_CONFIG",
                        # "skuName": "OPTIONAL_CONFIG",
                        # "sourceItemId": "OPTIONAL_CONFIG",
                        # "subscriptionId": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about a specific item of a debit memo. A debit memo item is a single line item in a debit memo.
            {
                "name": "get_debit_memo_item",
                "table_name": "item",
                "endpoint": {
                    "path": "/v1/debitmemos/{debitMemoId}/items/{dmitemid}",
                    "params": {
                        "debitMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "dmitemid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the information about all items of a specified invoice.
            {
                "name": "get_invoice_items",
                "table_name": "item",
                "endpoint": {
                    "path": "/v1/invoices/{invoiceId}/items",
                    "params": {
                        "invoiceId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a credit memo part. A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items.
            {
                "name": "get_credit_memo_item_parts",
                "table_name": "itempart",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "partid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about a specific credit memo part item.  A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items.
            {
                "name": "get_credit_memo_item_part",
                "table_name": "itempart",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts/{itempartid}",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "partid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itempartid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a payment part. A payment part item is a single line item in a payment part. A payment part can consist of several different types of items.
            {
                "name": "get_payment_item_parts",
                "table_name": "itempart",
                "endpoint": {
                    "path": "/v1/payments/{paymentId}/parts/{partid}/itemparts",
                    "params": {
                        "paymentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "partid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about a specific payment part item. A payment part item is a single line item in a payment part. A payment part can consist of several different types of items.
            {
                "name": "get_payment_item_part",
                "table_name": "itempart",
                "endpoint": {
                    "path": "/v1/payments/{paymentId}/parts/{partid}/itemparts/{itempartid}",
                    "params": {
                        "paymentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "partid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itempartid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about all items of a refund part. A refund part item is a single line item in a refund part. A refund part can consist of several different types of items.
            {
                "name": "get_refund_item_parts",
                "table_name": "itempart",
                "endpoint": {
                    "path": "/v1/refunds/{refundId}/parts/{refundpartid}/itemparts",
                    "params": {
                        "refundId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "refundpartid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.    Retrieves the information about a specific refund part item. A refund part item is a single line item in a refund part. A refund part can consist of several different types of items.
            {
                "name": "get_refund_item_part",
                "table_name": "itempart",
                "endpoint": {
                    "path": "/v1/refunds/{refundId}/parts/{refundpartid}/itemparts/{itempartid}",
                    "params": {
                        "refundId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "refundpartid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itempartid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all custom object bulk jobs submitted by your tenant.
            {
                "name": "get_all_custom_object_bulk_jobs",
                "table_name": "job",
                "endpoint": {
                    "path": "/objects/jobs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the custom object bulk job details by job ID.  Only the users that have the "View Custom Objects" permission can retrieve custom object bulk jobs. See [Platform Permissions](https://knowledgecenter.zuora.com/Billing/Tenant_Management/A_Administrator_Settings/User_Roles/h_Platform_Roles#Platform_Permissions) for more information.
            {
                "name": "get_custom_object_bulk_job",
                "table_name": "job",
                "endpoint": {
                    "path": "/objects/jobs/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of [data query](https://knowledgecenter.zuora.com/DC_Developers/BA_Data_Query) jobs that have been created in your Zuora tenant. You can filter the list by status.  If you are an administrator, you can retrieve all the query jobs in your tenant. Otherwise, you can only retrieve your own query jobs.
            {
                "name": "get_data_query_jobs",
                "table_name": "job",
                "endpoint": {
                    "path": "/query/jobs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "queryStatus": "OPTIONAL_CONFIG",
                        # "pageSize": "20",
                    },
                },
            },
            # Retrieves a [data query](https://knowledgecenter.zuora.com/DC_Developers/BA_Data_Query) job. You can use this operation to track the status of the query job and obtain the URL of the query results.  If you are an administrator, you can retrieve every query job in your tenant.   If you are a non-admin user and try to retrieve a query job that you are not the owner of, you will get a 403 response indicating that you are forbidden from viewing this job. As a non-admin user, you can only retrieve your own query job.
            {
                "name": "get_data_query_job",
                "table_name": "job",
                "endpoint": {
                    "path": "/query/jobs/{job-id}",
                    "params": {
                        "job-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This REST API reference describes how to get information about a summary journal entry by its journal entry number.
            {
                "name": "get_summary_journal_entry",
                "table_name": "journal_entry",
                "endpoint": {
                    "path": "/v1/journal-entries/{je-number}",
                    "params": {
                        "je-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            #  This REST API reference describes how to retrieve information about all summary journal entries in a journal run.
            {
                "name": "get_all_summary_journal_entries",
                "table_name": "journal_run",
                "endpoint": {
                    "path": "/v1/journal-entries/journal-runs/{jr-number}",
                    "params": {
                        "jr-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "8",
                    },
                },
            },
            # This REST API reference describes how to get information about a journal run. Request and response field descriptions and sample code are provided.
            {
                "name": "get_journal_run",
                "table_name": "journal_run",
                "endpoint": {
                    "path": "/v1/journal-runs/{jr-number}",
                    "params": {
                        "jr-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets workflow task usage sorted by day within a specified time frame.
            {
                "name": "get_workflows_usages",
                "table_name": "metric",
                "endpoint": {
                    "path": "/workflows/metrics.json",
                    "params": {
                        "startDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "endDate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "metrics": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Queries notification definitions with the specified filters.  **Note**: This operation is only applicable to notifications for custom events.
            {
                "name": "get_query_notification_definitions",
                "table_name": "notification_definition",
                "endpoint": {
                    "path": "/notifications/notification-definitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "profileId": "OPTIONAL_CONFIG",
                        # "eventTypeName": "OPTIONAL_CONFIG",
                        # "emailTemplateId": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 100,
                        "offset_param": "start",
                        "limit_param": "limit",
                        "total_path": "",
                        "maximum_offset": 20,
                    },
                },
            },
            # Queries the notification definition of the given ID.  **Note**: This operation is only applicable to notifications for custom events.
            {
                "name": "get_get_notification_definition",
                "table_name": "notification_definition",
                "endpoint": {
                    "path": "/notifications/notification-definitions/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).   Retrieves information about all orders in your tenant. By default, it returns the first page of the orders.
            {
                "name": "get_all_orders",
                "table_name": "order",
                "endpoint": {
                    "path": "/v1/orders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "dateFilterOption": "OPTIONAL_CONFIG",
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).          Retrieves the detailed information about a specified order.
            {
                "name": "get_order",
                "table_name": "order",
                "endpoint": {
                    "path": "/v1/orders/{orderNumber}",
                    "params": {
                        "orderNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  **Note:** You also need to enable the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature to access the Order Line Items feature. Orders is now generally available as of Zuora Billing Release 284 (August 2020). If you are an existing Zuora Subscribe and Amend customer and want to adopt Orders, see [What is Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization#What_is_Orders_Harmonization.3F) and join the [Orders Harmonization community group](https://community.zuora.com/t5/Orders-Harmonization/gp-p/Orders-Harmonization) for more information. If you want to enable Orders, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about a specified order line item.
            {
                "name": "get_order_line_item",
                "table_name": "order_line_item",
                "endpoint": {
                    "path": "/v1/order-line-items/{itemId}",
                    "params": {
                        "itemId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all parts of a credit memo. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a credit memo.
            {
                "name": "get_credit_memo_parts",
                "table_name": "part",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/parts",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific credit memo part. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos.
            {
                "name": "get_credit_memo_part",
                "table_name": "part",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/parts/{partid}",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "partid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all parts of a payment. A payment can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a payment.
            {
                "name": "get_payment_parts",
                "table_name": "part",
                "endpoint": {
                    "path": "/v1/payments/{paymentId}/parts",
                    "params": {
                        "paymentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific payment part. A payment can consist of an unapplied part, and several parts applied to invoices and debit memos.
            {
                "name": "get_payment_part",
                "table_name": "part",
                "endpoint": {
                    "path": "/v1/payments/{paymentId}/parts/{partid}",
                    "params": {
                        "paymentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "partid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all parts of a refund.
            {
                "name": "get_refund_parts",
                "table_name": "part",
                "endpoint": {
                    "path": "/v1/refunds/{refundId}/parts",
                    "params": {
                        "refundId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific refund part.
            {
                "name": "get_refund_part",
                "table_name": "part",
                "endpoint": {
                    "path": "/v1/refunds/{refundId}/parts/{refundpartid}",
                    "params": {
                        "refundId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "refundpartid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the information about one specific payment.
            {
                "name": "object_get_payment",
                "table_name": "payment",
                "endpoint": {
                    "path": "/v1/object/payment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all payments from all your customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.  Examples:  - /v1/payments?status=Processed  - /v1/payments?currency=USD&status=Processed  - /v1/payments?status=Processed&type=External&sort=+number
            {
                "name": "get_retrieve_all_payments",
                "table_name": "payment",
                "endpoint": {
                    "path": "/v1/payments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "amount": "OPTIONAL_CONFIG",
                        # "appliedAmount": "OPTIONAL_CONFIG",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "creditBalanceAmount": "OPTIONAL_CONFIG",
                        # "currency": "OPTIONAL_CONFIG",
                        # "effectiveDate": "OPTIONAL_CONFIG",
                        # "number": "OPTIONAL_CONFIG",
                        # "refundAmount": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "unappliedAmount": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about one specific payment.
            {
                "name": "get_payment",
                "table_name": "payment",
                "endpoint": {
                    "path": "/v1/payments/{paymentId}",
                    "params": {
                        "paymentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_payment_method",
                "table_name": "payment_method",
                "endpoint": {
                    "path": "/v1/object/payment-method/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This operation allows you to get the detailed information about a payment method.
            {
                "name": "get_payment_method",
                "table_name": "payment_method",
                "endpoint": {
                    "path": "/v1/payment-methods/{payment-method-id}",
                    "params": {
                        "payment-method-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This REST API reference describes how to retrieve a Payment Method Snapshot.  A Payment Method Snapshot is a copy of the particular Payment Method used in a transaction. If the Payment Method is deleted, the Payment Method Snapshot continues to retain the data used in each of the past transactions.  ## Notes The following Payment Method fields are not available in Payment Method Snapshots:  * `Active` * `AchAddress1` * `AchAddress2` * `CreatedById` * `CreatedDate` * `UpdatedById` * `UpdatedDate`  The Payment Method Snapshot field `PaymentMethodId` is not available in Payment Methods.
            {
                "name": "object_get_payment_method_snapshot",
                "table_name": "payment_method_snapshot",
                "endpoint": {
                    "path": "/v1/object/payment-method-snapshot/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_payment_method_transaction_log",
                "table_name": "payment_method_transaction_log",
                "endpoint": {
                    "path": "/v1/object/payment-method-transaction-log/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about a specific payment transaction log.
            {
                "name": "object_get_payment_transaction_log",
                "table_name": "payment_transaction_log",
                "endpoint": {
                    "path": "/v1/object/payment-transaction-log/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the basic information about all the payment gateways.
            {
                "name": "get_paymentgateways",
                "table_name": "paymentgateway",
                "endpoint": {
                    "path": "/v1/paymentgateways",
                },
            },
            # Retrieves detailed information about a specific product, including information about its product rate plans and charges.
            {
                "name": "get_product",
                "table_name": "product",
                "endpoint": {
                    "path": "/v1/catalog/product/{product-id}",
                    "params": {
                        "product-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the entire product catalog, including all products, features, and their corresponding product rate plans, charges. Products are returned in reverse chronological order on the `UpdatedDate` field.   With product rate plans and rate plan charges, the REST API has a maximum array size.   For a use case of this operation, see [Retrieve the product catalog](https://www.zuora.com/developer/api-guides/#Retrieve-the-product-catalog).
            {
                "name": "get_catalog",
                "table_name": "product",
                "endpoint": {
                    "path": "/v1/catalog/products",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "10",
                    },
                },
            },
            {
                "name": "object_get_product",
                "table_name": "product",
                "endpoint": {
                    "path": "/v1/object/product/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the revenue recognition rule associated with a production rate plan charge by specifying the charge ID.
            {
                "name": "get_revenue_rec_ruleby_product_rate_plan_charge",
                "table_name": "product_charge",
                "endpoint": {
                    "path": "/v1/revenue-recognition-rules/product-charges/{charge-key}",
                    "params": {
                        "charge-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the details about all revenue schedules of a product rate plan charge by specifying the charge ID and billing account ID.
            {
                "name": "get_r_sby_product_charge_and_billing_account",
                "table_name": "product_charge",
                "endpoint": {
                    "path": "/v1/revenue-schedules/product-charges/{charge-key}/{account-key}",
                    "params": {
                        "charge-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "8",
                    },
                },
            },
            {
                "name": "object_get_product_feature",
                "table_name": "product_feature",
                "endpoint": {
                    "path": "/v1/object/product-feature/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_product_rate_plan",
                "table_name": "product_rate_plan",
                "endpoint": {
                    "path": "/v1/object/product-rate-plan/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about all product rate plans of a specific product.  For a use case of this operation, see [Retrieve the product catalog](https://www.zuora.com/developer/api-guides/#Retrieve-the-product-catalog).
            {
                "name": "get_product_rate_plans",
                "table_name": "product_rate_plan",
                "endpoint": {
                    "path": "/v1/rateplan/{product_id}/productRatePlan",
                    "params": {
                        "product_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            {
                "name": "object_get_product_rate_plan_charge",
                "table_name": "product_rate_plan_charge",
                "endpoint": {
                    "path": "/v1/object/product-rate-plan-charge/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_product_rate_plan_charge_tier",
                "table_name": "product_rate_plan_charge_tier",
                "endpoint": {
                    "path": "/v1/object/product-rate-plan-charge-tier/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the stored credential profiles within a payment method.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available.
            {
                "name": "get_stored_credential_profiles",
                "table_name": "profile",
                "endpoint": {
                    "path": "/v1/payment-methods/{payment-method-id}/profiles",
                    "params": {
                        "payment-method-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "includeAll": "false",
                    },
                },
            },
            # **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves the latest definition of a specified ramp.
            {
                "name": "get_ramp_by_ramp_number",
                "table_name": "ramp",
                "endpoint": {
                    "path": "/v1/ramps/{rampNumber}",
                    "params": {
                        "rampNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.   Retrieves the definition of the ramp associated with a specified subscription.
            {
                "name": "get_ramps_by_subscription_key",
                "table_name": "ramp",
                "endpoint": {
                    "path": "/v1/subscriptions/{subscriptionKey}/ramps",
                    "params": {
                        "subscriptionKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves key ramp metrics about a specified order, including the following metrics:  * TCB, TCV in the Ramp level * TCB, TCV in the Interval level * TCB, TCV, Quantity, and MRR in Interval Metrics * Delta TCB, Delta TCV, Delta Quantity, and Delta MRR in Interval Delta Metrics  See [Key metrics for Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/F_Key_metrics_for_Ramps) for more information.
            {
                "name": "get_ramp_metrics_by_order_number",
                "table_name": "ramp_metric",
                "endpoint": {
                    "path": "/v1/orders/{orderNumber}/ramp-metrics",
                    "params": {
                        "orderNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves key metrics about a specified ramp, including the following metrics:  * TCB, TCV in the Ramp level * TCB, TCV in the Interval level * TCB, TCV, Quantity, and MRR in Interval Metrics * Delta TCB, Delta TCV, Delta Quantity, and Delta MRR in Interval Delta Metrics  See [Key metrics for Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/F_Key_metrics_for_Ramps) for more information.
            {
                "name": "get_ramp_metrics_by_ramp_number",
                "table_name": "ramp_metric",
                "endpoint": {
                    "path": "/v1/ramps/{rampNumber}/ramp-metrics",
                    "params": {
                        "rampNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves key ramp metrics about a specified subscription, including the following metrics:  * TCB, TCV in the Ramp level * TCB, TCV in the Interval level * TCB, TCV, Quantity, and MRR in Interval Metrics * Delta TCB, Delta TCV, Delta Quantity, and Delta MRR in Interval Delta Metrics  See [Key metrics for Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/F_Key_metrics_for_Ramps) for more information.
            {
                "name": "get_ramp_metrics_by_subscription_key",
                "table_name": "ramp_metric",
                "endpoint": {
                    "path": "/v1/subscriptions/{subscriptionKey}/ramp-metrics",
                    "params": {
                        "subscriptionKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_rate_plan",
                "table_name": "rate_plan",
                "endpoint": {
                    "path": "/v1/object/rate-plan/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_rate_plan_charge",
                "table_name": "rate_plan_charge",
                "endpoint": {
                    "path": "/v1/object/rate-plan-charge/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_rate_plan_charge_tier",
                "table_name": "rate_plan_charge_tier",
                "endpoint": {
                    "path": "/v1/object/rate-plan-charge-tier/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_refund",
                "table_name": "refund",
                "endpoint": {
                    "path": "/v1/object/refund/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all refunds. Two types of refunds are available, electronic refunds and external refunds.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.  Examples:  - /v1/refunds?status=Processed  - /v1/refunds?amount=4&status=Processed  - /v1/refunds?status=Processed&type=External&sort=+number
            {
                "name": "get_refunds",
                "table_name": "refund",
                "endpoint": {
                    "path": "/v1/refunds",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "amount": "OPTIONAL_CONFIG",
                        # "createdById": "OPTIONAL_CONFIG",
                        # "createdDate": "OPTIONAL_CONFIG",
                        # "methodType": "OPTIONAL_CONFIG",
                        # "number": "OPTIONAL_CONFIG",
                        # "paymentId": "OPTIONAL_CONFIG",
                        # "refundDate": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "updatedById": "OPTIONAL_CONFIG",
                        # "updatedDate": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific refund.
            {
                "name": "get_refund",
                "table_name": "refund",
                "endpoint": {
                    "path": "/v1/refunds/{refundId}",
                    "params": {
                        "refundId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_refund_invoice_payment",
                "table_name": "refund_invoice_payment",
                "endpoint": {
                    "path": "/v1/object/refund-invoice-payment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_refund_transaction_log",
                "table_name": "refund_transaction_log",
                "endpoint": {
                    "path": "/v1/object/refund-transaction-log/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Describes how to get the revenue automation start date. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_automation_start_date",
                "table_name": "revenue_automation_start_date",
                "endpoint": {
                    "path": "/v1/settings/finance/revenue-automation-start-date",
                },
            },
            # This REST API reference describes how to get revenue event details by specifying the revenue event number. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_event_details",
                "table_name": "revenue_event",
                "endpoint": {
                    "path": "/v1/revenue-events/{event-number}",
                    "params": {
                        "event-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This REST API reference describes how to get the details of each revenue item in a revenue event by specifying the revenue event number. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_items_by_charge_revenue_event_number",
                "table_name": "revenue_event",
                "endpoint": {
                    "path": "/v1/revenue-items/revenue-events/{event-number}",
                    "params": {
                        "event-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "300",
                    },
                },
            },
            #  This REST API reference describes how to get all revenue events in a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_event_for_revenue_schedule",
                "table_name": "revenue_schedule",
                "endpoint": {
                    "path": "/v1/revenue-events/revenue-schedules/{rs-number}",
                    "params": {
                        "rs-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "8",
                    },
                },
            },
            # This REST API reference describes how to get the details for each revenue items in a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_items_by_revenue_schedule",
                "table_name": "revenue_schedule",
                "endpoint": {
                    "path": "/v1/revenue-items/revenue-schedules/{rs-number}",
                    "params": {
                        "rs-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "300",
                    },
                },
            },
            # Retrieves the details of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided.
            {
                "name": "get_rs",
                "table_name": "revenue_schedule",
                "endpoint": {
                    "path": "/v1/revenue-schedules/{rs-number}",
                    "params": {
                        "rs-number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves information about all sequence sets configured for billing documents, payments, and refunds. Billing documents include invoices, credit memos, and debit memos.  You can use query parameters to restrict the data returned in the response.  **Note**: The Credit and Debit Memos feature is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.
            {
                "name": "get_sequence_sets",
                "table_name": "sequence_set",
                "endpoint": {
                    "path": "/v1/sequence-sets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about a specific sequence set configured for billing documents, payments, and refunds. Billing documents include invoices, credit memos, and debit memos  **Note**: The Credit and Debit Memos feature is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.
            {
                "name": "get_sequence_set",
                "table_name": "sequence_set",
                "endpoint": {
                    "path": "/v1/sequence-sets/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get a list of all available settings in your tenant.   The response message is by default in JSON format. If you want to receive all the availabe settings in csv format, include `Accept` in the header parameters and set it to `application/csv`.              See a [200 response sample in JSON format](https://assets.zuora.com/zuora-documentation/ListAllSettingsResponseSample.json).  See a [200 response sample in CSV format](https://assets.zuora.com/zuora-documentation/ListAllSettingsResponseSample.csv).  You can find a specific operate of an available setting item in your tenant from the 200 response body of this call. See the following tutorials of Settings API for how to operate on a specifc setting item.   * Billing Rules:    * [Get a specific setting - Billing Rules](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/AA_Get_a_specific_setting_-_Billing_Rules)    * [Update a specific setting - Billing Rules](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/AB_Update_a_specific_setting_-_Billing_Rules)  * Age Buckets:    * [Get Age Buckets](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_Age_Buckets)    * [Update Age Buckets](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Update_Age_Buckets)  * Invoice Templates:    * [Get a specific Invoice Template](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_a_specific_Invoice_Template)    * [Get all Invoice Templates](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_all_Invoice_Templates)    * [Create a new Invoice Template](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Create_a_new_Invoice_Template)  * Communications Profiles:    * [Get all Communication Profiles](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_all_Communication_Profiles)    * [Create a new Communication Profile](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Create_a_new_Communication_Profile)    * [Modify a Communication Profile](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Modify_a_Communication_Profile)    * [Get all Notifications under a particular Communication Profile](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_all_Notifications_under_a_particular_Communication_Profile)  * Chart of Accounts:    * [Get Chart of Accounts](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_Chart_of_Accounts)    * [Add a new Chart of Account](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Add_a_new_Chart_of_Account)  * Quote Templates:    * [Get all Quote Templates](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Get_all_Quote_Templates)    * [Get a specific Quote Template](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Get_a_specific_Quote_Template)    * [Create a new Quote Template](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Create_a_new_Quote_Template)  * Custom Fields:    * [View all custom fields](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/View_all_custom_fields)    * [View custom fields of a specific object](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/View_custom_fields_of_a_specific_object)    * [Update custom fields of a specific object](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Update_custom_fields_of_a_specific_object)
            {
                "name": "get_list_all_settings",
                "table_name": "setting_item_with_operations_information",
                "endpoint": {
                    "data_selector": "settings",
                    "path": "/settings/listing",
                },
            },
            # Retrieves detailed information about the amendment with the specified subscription.
            {
                "name": "get_amendments_by_subscription_id",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v1/amendments/subscriptions/{subscription-id}",
                    "params": {
                        "subscription-id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "object_get_subscription",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v1/object/subscription/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about all orders for a specified subscription. Any orders containing the changes on the specified subscription are returned.
            {
                "name": "get_orders_by_subscription_number",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v1/orders/subscription/{subscriptionNumber}",
                    "params": {
                        "subscriptionNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "dateFilterOption": "OPTIONAL_CONFIG",
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This REST API reference describes how to retrieve detailed information about a specified subscription in the latest version.
            {
                "name": "get_subscriptions_by_key",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v1/subscriptions/{subscription-key}",
                    "params": {
                        "subscription-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "charge-detail": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the details of a charge revenue summary by specifying the subscription charge ID. This response retrieves all revenue items associated with a charge revenue summary.
            {
                "name": "get_crs_by_charge_id",
                "table_name": "subscription_charge",
                "endpoint": {
                    "path": "/v1/charge-revenue-summaries/subscription-charges/{charge-key}",
                    "params": {
                        "charge-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the revenue recognition rule associated with a subscription charge by specifying the charge ID. Request and response field descriptions and sample code are provided.
            {
                "name": "get_revenue_rec_rules",
                "table_name": "subscription_charge",
                "endpoint": {
                    "path": "/v1/revenue-recognition-rules/subscription-charges/{charge-key}",
                    "params": {
                        "charge-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the revenue schedule details by specifying subscription charge ID. Request and response field descriptions and sample code are provided
            {
                "name": "get_r_sfor_subsc_charge",
                "table_name": "subscription_charge",
                "endpoint": {
                    "path": "/v1/revenue-schedules/subscription-charges/{charge-key}",
                    "params": {
                        "charge-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "8",
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about all orders for a specified subscription owner. Any orders containing the changes on the subscriptions owned by this account are returned.
            {
                "name": "get_orders_by_subscription_owner",
                "table_name": "subscription_owner",
                "endpoint": {
                    "path": "/v1/orders/subscriptionOwner/{accountNumber}",
                    "params": {
                        "accountNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                        # "dateFilterOption": "OPTIONAL_CONFIG",
                        # "startDate": "OPTIONAL_CONFIG",
                        # "endDate": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_subscription_product_feature",
                "table_name": "subscription_product_feature",
                "endpoint": {
                    "path": "/v1/object/subscription-product-feature/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves detailed information about the specified customer account.  The response includes the account information and a summary of the account’s subscriptions, invoices, payments, and usages for the last six recently updated subscriptions.  ## Notes  Returns only the six most recent subscriptions based on the subscription updatedDate. Within those subscriptions, there may be many rate plans and many rate plan charges. These items are subject to the maximum limit on the array size.
            {
                "name": "get_account_summary",
                "table_name": "summary",
                "endpoint": {
                    "path": "/v1/accounts/{account-key}/summary",
                    "params": {
                        "account-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get the notification history deletion task by ID.  **Note**: This operation is only available if you have the Notification and the Configurable Event features enabled.
            {
                "name": "get_get_notification_history_deletion_task",
                "table_name": "task",
                "endpoint": {
                    "path": "/notifications/history/tasks/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves a list of workflow tasks available in your Zuora tenant.
            {
                "name": "get_workflows_tasks",
                "table_name": "task",
                "endpoint": {
                    "path": "/workflows/tasks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "id": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                        # "instance": "OPTIONAL_CONFIG",
                        # "action_type": "OPTIONAL_CONFIG",
                        # "object": "OPTIONAL_CONFIG",
                        # "object_id": "OPTIONAL_CONFIG",
                        # "call_type": "OPTIONAL_CONFIG",
                        # "workflow_id": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "page_length": "20",
                    },
                },
            },
            # Retrieves a specific workflow task by its ID.
            {
                "name": "get_workflows_task",
                "table_name": "task",
                "endpoint": {
                    "path": "/workflows/tasks/{task_id}",
                    "params": {
                        "task_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about the taxation items of a specific credit memo item.
            {
                "name": "get_taxation_items_of_credit_memo_item",
                "table_name": "taxation_item",
                "endpoint": {
                    "path": "/v1/creditmemos/{creditMemoId}/items/{cmitemid}/taxation-items",
                    "params": {
                        "creditMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cmitemid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about the taxation items of a specific debit memo item.
            {
                "name": "get_taxation_items_of_debit_memo_item",
                "table_name": "taxation_item",
                "endpoint": {
                    "path": "/v1/debitmemos/{debitMemoId}/items/{dmitemid}/taxation-items",
                    "params": {
                        "debitMemoId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "dmitemid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            # Retrieves information about the taxation items of a specific invoice item.
            {
                "name": "get_taxation_items_of_invoice_item",
                "table_name": "taxation_item",
                "endpoint": {
                    "path": "/v1/invoices/{invoiceId}/items/{itemId}/taxation-items",
                    "params": {
                        "invoiceId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itemId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pageSize": "20",
                    },
                },
            },
            {
                "name": "object_get_taxation_item",
                "table_name": "taxation_item",
                "endpoint": {
                    "path": "/v1/object/taxation-item/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the information about a specific taxation item by ID.
            {
                "name": "get_taxation_item",
                "table_name": "taxationitem",
                "endpoint": {
                    "path": "/v1/taxationitems/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  Retrieves the terms of the specified subscription.
            {
                "name": "get_subscription_term_info",
                "table_name": "term",
                "endpoint": {
                    "path": "/v1/orders/term/{subscriptionNumber}",
                    "params": {
                        "subscriptionNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                        # "pageSize": "20",
                    },
                },
            },
            {
                "name": "object_get_unit_of_measure",
                "table_name": "unit_of_measure",
                "endpoint": {
                    "path": "/v1/object/unit-of-measure/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "object_get_usage",
                "table_name": "usage",
                "endpoint": {
                    "path": "/v1/object/usage/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This REST API reference describes how to retrieve detailed information about a specified subscription in a specified version. When you create a subscription amendment, you create a new version of the subscription. You can use this method to retrieve information about a subscription in any version.
            {
                "name": "get_subscriptions_by_key_and_version",
                "table_name": "version",
                "endpoint": {
                    "path": "/v1/subscriptions/{subscription-key}/versions/{version}",
                    "params": {
                        "subscription-key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "version": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "charge-detail": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of workflows available in your Zuora tenant.
            {
                "name": "get_workflows",
                "table_name": "workflow",
                "endpoint": {
                    "path": "/workflows",
                    "params": {
                        # the parameters below can optionally be configured
                        # "callout_trigger": "OPTIONAL_CONFIG",
                        # "interval": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                        # "ondemand_trigger": "OPTIONAL_CONFIG",
                        # "scheduled_trigger": "OPTIONAL_CONFIG",
                        # "page_length": "20",
                    },
                },
            },
            # Retrieves information about a specific workflow by its ID.
            {
                "name": "get_workflow",
                "table_name": "workflow",
                "endpoint": {
                    "path": "/workflows/{workflow_id}",
                    "params": {
                        "workflow_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
