# zuora pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/zuora.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /v1/users/{username}/accessible-entities_ 
  *resource*: get_entities_user_accessible  
  *description*: **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves detailed information about all the entities that a user has permission to access.  ## User Access Permission You can make the call as any entity user. 
* _GET /v1/accounts/{account-key}_ 
  *resource*: get_account  
  *description*: Retrieves basic information about a customer account.  This operation is a quick retrieval that doesn't include the account's subscriptions, invoices, payments, or usage details. Use Get account summary to get more detailed information about an account. 
* _GET /v1/object/account/{id}_ 
  *resource*: object_get_account  
  *description*: Retrieves the information about one specific account. 
* _GET /v1/payment-methods/credit-cards/accounts/{account-key}_ 
  *resource*: get_payment_methods_credit_card  
  *description*: This REST API reference describes how to retrieve all credit card information for the specified customer account.   ## Notes The response includes details of credit or debit cards for the specified customer account. Card numbers are masked, e.g., "************1234". Cards are returned in reverse chronological order of last update.  Though you can also send requests for bank transfer, ACH, or other supported payment methods, the response will not include effective details of these payment methods. 
* _GET /v1/subscriptions/accounts/{account-key}_ 
  *resource*: get_subscriptions_by_account  
  *description*: Retrieves all subscriptions associated with the specified account. Zuora only returns the latest version of the subscriptions.  Subscription data is returned in reverse chronological order based on `updatedDate`. 
* _GET /v1/transactions/invoices/accounts/{account-key}_ 
  *resource*: get_transaction_invoice  
  *description*: Retrieves invoices for a specified account.  Invoices are returned in reverse chronological order by **updatedDate**.  For a use case of this operation, see [View invoices](https://www.zuora.com/developer/api-guides/#View-invoices). 
* _GET /v1/transactions/payments/accounts/{account-key}_ 
  *resource*: get_transaction_payment  
  *description*: Retrieves payments for a specified account. Payments are returned in reverse chronological order by **updatedDate**. 
* _GET /v1/usage/accounts/{account-key}_ 
  *resource*: get_usage  
  *description*: This REST API reference describes how to retrieve usage details for an account. Usage data is returned in reverse chronological order. 
* _GET /v1/accounting-codes_ 
  *resource*: get_all_accounting_codes  
  *description*: This reference describes how to query all accounting codes in your chart of accounts through the REST API.
* _GET /v1/accounting-codes/{ac-id}_ 
  *resource*: get_accounting_code  
  *description*: This reference describes how to query an accounting code through the REST API.
* _GET /v1/accounting-periods_ 
  *resource*: get_all_accounting_periods  
  *description*: Retrieves all accounting periods on your tenant.
* _GET /v1/accounting-periods/{ap-id}_ 
  *resource*: get_accounting_period  
  *description*: Retrieves an accounting period. Prerequisites -------------  You must have Zuora Finance enabled on your tenant. 
* _GET /v1/amendments/{amendment-key}_ 
  *resource*: get_amendments_by_key  
  *description*: Retrieves detailed information about the specified subscription amendment.
* _GET /v1/object/amendment/{id}_ 
  *resource*: object_get_amendment  
* _GET /v1/debitmemos/{debitMemoId}/application-parts_ 
  *resource*: get_debit_memo_application_parts  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves information about the payments or credit memos that are applied to a specified debit memo. 
* _GET /v1/invoices/{invoiceId}/application-parts_ 
  *resource*: get_invoice_application_parts  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about the payments or credit memos that are applied to a specified invoice. 
* _GET /v1/async-jobs/{jobId}_ 
  *resource*: get_job_status_and_response  
  *description*: **Note:** This operation is only available if you have the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature enabled. Orders is now generally available as of Zuora Billing Release 284 (August 2020). If you are an existing Zuora Subscribe and Amend customer and want to adopt Orders, see [What is Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization#What_is_Orders_Harmonization.3F) and join the [Orders Harmonization community group](https://community.zuora.com/t5/Orders-Harmonization/gp-p/Orders-Harmonization) for more information. If you want to enable Orders, submit a request at [Zuora Global Support](https://support.zuora.com/).  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Get the status and response of an asynchronous job. Currently, an asynchronous job created by "Create an order asynchronously" or "Preview an order asynchronously" is supported. 
* _GET /v1/attachments/{attachment-id}_ 
  *resource*: get_attachments  
  *description*: Use the View Attachment REST request to retrieve information about an attachment document. 
* _GET /v1/attachments/{object-type}/{object-key}_ 
  *resource*: get_attachments_list  
  *description*: Use the View Attachment REST request to get a list of attachments on an account, an invoice, a subscription, a credit memo, or a debit memo.  **Note**: The Credit and Debit Memos feature is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  
* _GET /v1/object/bill-run/{id}_ 
  *resource*: object_get_bill_run  
  *description*: Retrieves information about a bill run.    Business operations depending on the completion of the bill run will not be available while the bill run query returns `PostInProgress`. Upon completion of the bill run, a query will return `Posted`. 
* _GET /v1/billing-documents_ 
  *resource*: get_billing_documents  
  *description*: Retrieves the information about all billing documents associated with a specified account. The billing documents contain invoices, credit memos, and debit memos.   To retrieve information about credit memos and debit memos, you must have the Invoice Settlement feature enabled.   You can use query parameters to restrict the data returned in the response.  Examples: - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1&sort=+documentDate - /billing-documents?accountId=4028905f5e4feb38015e50af9aa002d1&status=Posted 
* _GET /v1/billing-preview-runs/{billingPreviewRunId}_ 
  *resource*: get_billing_preview_run  
  *description*: Retrieves a preview of future invoice items for multiple customer accounts through a billing preview run. If you have the Invoice Settlement feature enabled,  you can also retrieve a preview of future credit memo items. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   A billing preview run asynchronously generates a downloadable CSV file containing a preview of invoice item data and credit memo item data for a batch of customer accounts. 
* _GET /v1/bulk/{bulk-key}_ 
  *resource*: get_mass_updater  
  *description*: Describes how to get information about the result of a mass action through the REST API.  
* _GET /v1/notification-history/callout_ 
  *resource*: get_callout_history  
  *description*: Describes how to get a notification history for callouts. 
* _GET /charge-metrics/data/charge-metrics_ 
  *resource*: get_charge_metrics  
  *description*: Retrieves key charge metrics about rate plan charges that have changes in a specified time range.  The purpose of `fromTimestamp` and `toTimestamp` is to synchronize charge metrics data incrementally.  
* _GET /charge-metrics/data/charge-metrics-discount-allocation-detail_ 
  *resource*: get_charge_metrics_discount_allocation_details  
  *description*: Retrieves discount allocation details about rate plan charges that have changes in a specified time range.  The purpose of `fromTimestamp` and `toTimestamp` is to synchronize discount allocation details incrementally.  
* _GET /v1/charge-revenue-summaries/{crs-number}_ 
  *resource*: get_crs_by_crs_number  
  *description*: Retrieves the details of a charge revenue summary by specifying the charge revenue summary number. The response includes all revenue items associated with the charge revenue summary. 
* _GET /v1/revenue-items/charge-revenue-summaries/{crs-number}_ 
  *resource*: get_revenue_items_by_charge_revenue_summary_number  
  *description*: This REST API reference describes how to get the details for each revenue item in a charge revenue summary by specifying the charge revenue summary number. Request and response field descriptions and sample code are provided. 
* _GET /v1/object/communication-profile/{id}_ 
  *resource*: object_get_communication_profile  
* _GET /v1/object/contact/{id}_ 
  *resource*: object_get_contact  
  *description*: Retrieves detailed information about a specific contact. 
* _GET /v1/object/credit-balance-adjustment/{id}_ 
  *resource*: object_get_credit_balance_adjustment  
* _GET /v1/revenue-schedules/credit-memo-items/{cmi-id}_ 
  *resource*: get_r_sby_credit_memo_item  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the details about a revenue schedule by specifying a valid credit memo item ID. 
* _GET /v1/creditmemos_ 
  *resource*: get_credit_memos  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all credit memos.   For a use case of this operation, see [Get credit memo](https://www.zuora.com/developer/api-guides/#Get-credit-memo).   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.     Examples:  - /v1/creditmemos?status=Posted  - /v1/creditmemos?referredInvoiceId=null&status=Draft  - /v1/creditmemos?status=Posted&type=External&sort=+number 
* _GET /v1/creditmemos/{creditMemoId}_ 
  *resource*: get_credit_memo  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific credit memo.  For a use case of this operation, see [Get credit memo](https://www.zuora.com/developer/api-guides/#Get-credit-memo). 
* _GET /v1/custom-exchange-rates/{currency}_ 
  *resource*: get_custom_exchange_rates  
  *description*: This feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   This reference describes how to query custom foreign exchange rates from Zuora. You can use this API method to query exchange rates only if you use a custom exchange rate provider and upload rates with the Import Foreign Exchange Rates mass action.  
* _GET /v1/revenue-schedules/debit-memo-items/{dmi-id}_ 
  *resource*: get_r_sby_debit_memo_item  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the details about a revenue schedule by specifying a valid debit memo item ID. 
* _GET /v1/debitmemos_ 
  *resource*: get_debit_memos  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about all debit memos associated with all customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos?status=Posted  - /v1/debitmemos?referredInvoiceId=null&status=Draft  - /v1/debitmemos?status=Posted&type=External&sort=+number 
* _GET /v1/debitmemos/{debitMemoId}_ 
  *resource*: get_debit_memo  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific debit memo. 
* _GET /objects/definitions/default_ 
  *resource*: get_all_custom_object_definitions_in_namespace  
  *description*: Get all custom objects definitions for a given tenant. If you want to copy all the existing custom objects from an old tenant to a new tenant, you can call this operation in your old tenant and then use its response directly as the request of the [Create custom object definitions](https://www.zuora.com/developer/api-reference/#operation/POST_CustomObjectDefinitions) call in the new tenant to import all the custom objects from the old tenant. 
* _GET /objects/definitions/default/{object}_ 
  *resource*: get_custom_object_definition_by_type  
  *description*: Retrieves the custom object definition by type for the given tenant. 
* _GET /objects/records/default/{object}_ 
  *resource*: get_all_records_for_custom_object_type  
  *description*: Lists all object records of the given type. You can also use the `q` query parameter to filter the output records.  ## Limitations   This call has the following limitations: * When a record is created, there will be a delay before it is available for search. For example, if you create 5 records and perform a query that these 5 records satisfy the query conditions, there will be a delay between when the 5 records are created, and when all the 5 records can be returned in the query result. 
* _GET /objects/records/default/{object}/{id}_ 
  *resource*: get_custom_object_record_by_id  
  *description*: Retrieves a record of a given type by ID. 
* _GET /v1/accounts/billing-documents/files/deletion-jobs/{jobId}_ 
  *resource*: get_billing_document_files_deletion_job  
  *description*: Retrieves information about an asynchronous job of permanently deleting all billing document PDF files for specific accounts.  **Note**: This operation can be used only if you have the Billing user permission "Hard Delete Billing Document Files" enabled.  
* _GET /v1/describe/{object}_ 
  *resource*: get_describe  
  *description*: Provides a reference listing of each object that is available in your Zuora tenant.  The information returned by this call is useful if you are using [CRUD: Create Export](https://www.zuora.com/developer/api-reference/#operation/Object_POSTExport) or the [AQuA API](https://knowledgecenter.zuora.com/DC_Developers/T_Aggregate_Query_API) to create a data source export. See [Export ZOQL](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL) for more information.  ## Response The response contains an XML document that lists the fields of the specified object. Each of the object's fields is represented by a `<field>` element in the XML document.      Each `<field>` element contains the following elements:  | Element      | Description                                                                                                                                                                                                                                                                                  | |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| | `<name>`     | API name of the field.                                                                                                                                                                                                                                                                       | | `<label>`    | Name of the field in the Zuora user interface.                                                                                                                                                                                                                                               | | `<type>`     | Data type of the field. The possible data types are: `boolean`, `date`, `datetime`, `decimal`, `integer`, `picklist`, `text`, `timestamp`, and `ZOQL`. If the data type is `picklist`, the `<field>` element contains an `<options>` element that lists the possible values of the field.    | | `<contexts>` | Specifies the availability of the field. If the `<contexts>` element lists the `export` context, the field is available for use in data source exports.                                                                                                                                                |  The `<field>` element contains other elements that provide legacy information about the field. This information is not directly related to the REST API.  Response sample: ```xml <?xml version="1.0" encoding="UTF-8"?> <object>   <name>ProductRatePlanCharge</name>   <label>Product Rate Plan Charge</label>   <fields>     ...     <field>       <name>TaxMode</name>       <label>Tax Mode</label>       <type>picklist</type>       <options>         <option>TaxExclusive</option>         <option>TaxInclusive</option>       </options>       <contexts>         <context>export</context>       </contexts>       ...     </field>     ...   </fields> </object> ```  It is strongly recommended that your integration checks `<contexts>` elements in the response. If your integration does not check `<contexts>` elements, your integration may process fields that are not available for use in data source exports. See [Changes to the Describe API](https://knowledgecenter.zuora.com/DC_Developers/M_Export_ZOQL/Changes_to_the_Describe_API) for more information. 
* _GET /v1/document-properties/{documentType}/{documentId}_ 
  *resource*: get_document_properies  
  *description*: **Note:** This feature is available only if you have the Billing Document Properties Setup feature enabled. The Billing Document Properties Setup feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieve information about document properties of a billing document. Billing documents include invoices, credit memos, and debit memos.    **Note:** You can retrieve information about document properties of credit and debit memos only if you have the Invoice Settlement feature enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information. 
* _GET /v1/notification-history/email_ 
  *resource*: get_email_history  
  *description*: Describes how to get a notification history for notification emails.   ## Notes Request parameters and their values may be appended with a "?" following the HTTPS GET request.  Additional request parameter are separated by "&".   For example:  `GET https://rest.zuora.com/v1/notification-history/email?startTime=2015-01-12T00:00:00&endTime=2015-01-15T00:00:00&failedOnly=false&eventCategory=1000&pageSize=1` 
* _GET /notifications/email-templates_ 
  *resource*: get_query_email_templates  
  *description*: Queries email templates.  **Note**: This operation is only applicable to email templates for custom events. 
* _GET /notifications/email-templates/{id}_ 
  *resource*: get_get_email_template  
  *description*: Queries the email template of the specified ID.  **Note**: This operation is only applicable to email templates for custom events. 
* _GET /v1/entities_ 
  *resource*: get_entities  
  *description*: **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).    Retrieves detailed information of certain entities in a multi-entity hierarchy.   You can retrieve:   - Provisioned entities     - Unprovisioned entities     - Both provisioned and unprovisioned entities  ## User Access Permission  You can make the call as any entity user. 
* _GET /v1/entities/{id}_ 
  *resource*: get_entity_by_id  
  *description*: **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).   Retrieves detailed information about a specified entity.  ## User Access Permission You can make the call as any entity user.      
* _GET /v1/entity-connections_ 
  *resource*: get_entity_connections  
  *description*: **Note:** The Multi-entity feature is in **Limited Availability**. If you wish to have access to the feature, submit a request at [Zuora Global Support](http://support.zuora.com/).  Retrieves information about certain connections for a specified entity. You can specify the entity to retrieve in the `Zuora-Entity-Ids` request header.  You can retrieve:  - Inbound connections  - Outbound connections  - Both inbound and outbound connections  ## User Access Permission You can make the call as any entity user.  
* _GET /objects/jobs/{id}/errors_ 
  *resource*: get_custom_object_bulk_job_errors  
  *description*: Lists all errors for a custom object bulk job. 
* _GET /events/event-triggers_ 
  *resource*: get_event_triggers  
* _GET /events/event-triggers/{id}_ 
  *resource*: get_event_trigger  
* _GET /v1/orders/{orderNumber}/evergreenMetrics/{subscriptionNumber}_ 
  *resource*: get_order_metricsfor_evergreen_subscription  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** As of Zuora Billing Release 306, Zuora has upgraded the methodologies for calculating metrics in [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders). The new methodologies are reflected in the following Order Delta Metrics objects.  * [Order Delta Mrr](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Mrr) * [Order Delta Tcv](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcv) * [Order Delta Tcb](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/Order_Delta_Tcb)  It is recommended that all customers use the new [Order Delta Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Delta_Metrics/AA_Overview_of_Order_Delta_Metrics). If you are an existing [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders) customer and want to migrate to Order Delta Metrics, submit a request at [Zuora Global Support](https://support.zuora.com/).  Whereas new customers, and existing customers not currently on [Order Metrics](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders/Key_Metrics_for_Orders), will no longer have access to Order Metrics, existing customers currently using Order Metrics will continue to be supported.  **Note:** As of Zuora Billing Release 306, any new customers who onboard on [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) or [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization) will no longer get this operation.   Retrieves the metrics of an evergreen subscription in a specified order. 
* _GET /v1/object/export/{id}_ 
  *resource*: object_get_export  
  *description*: Use this operation to check the status of a data source export and access the exported data.  When you export data from Zuora, each exported file is available for download for 7 days. Data source exports (Export objects) older than 90 days are automatically deleted. 
* _GET /workflows/{workflow_id}/export_ 
  *resource*: get_workflow_export  
  *description*: Export a Workflow in a JSON document. This document can be used to create a copy of this workflow.
* _GET /v1/object/feature/{id}_ 
  *resource*: object_get_feature  
* _GET /v1/files/{file-id}_ 
  *resource*: get_files  
  *description*: Retrieve files such as export results, invoices, and accounting period reports.  The response content type depends on the type of file that you retrieve. For example, if you retrieve an invoice PDF, the value of the `Content-Type` header in the response is `application/pdf;charset=UTF-8`.  Other content types include:  - `text/csv` for CSV files - `application/msword` for Microsoft Word files - `application/vnd.ms-excel` and `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`   for Microsoft Excel files (*.xls* and *.xlsx* respectively) - `application/zip` and `application/x-gzip` for ZIP and Gzip files respectively - `text/html` for HTML files - `text/plain` for text files  The response always contains character encoding information in the `Content-Type` header. For example, `Content-Type: application/zip;charset=UTF-8`.  **Note:** The maximum file size is 2,047 MB. If you have a data request that exceeds this limit, Zuora returns the following 403 response: `<security:max-object-size>2047MB</security:max-object-size>`. Submit a request at <a href="http://support.zuora.com/" target="_blank">Zuora Global Support</a> to determine if large file optimization is an option for you. 
* _GET /v1/invoices/{invoiceId}/files_ 
  *resource*: get_invoice_files  
  *description*: Retrieves the information about all PDF files of a specified invoice.   Invoice PDF files are returned in reverse chronological order by the value of the `versionNumber` field.  **Note**: This API only retrieves the PDF files that have been generated. If the latest PDF file is being generated, it will not be included in the response.  You can use the [Query](https://www.zuora.com/developer/api-reference/#operation/Action_POSTquery) action to get the latest PDF file, for example: `"select Body from Invoice where Id = '2c93808457d787030157e0324aea5158'"`.  See [Query an Invoice Body](https://knowledgecenter.zuora.com/Central_Platform/API/G_SOAP_API/E1_SOAP_API_Object_Reference/Invoice/Query_an_Invoice_Body_Field) for more information. 
* _GET /v1/payment-runs/{paymentRunId}/data_ 
  *resource*: get_payment_run_data  
  *description*: Retrieves payment run data and the processing result with details, if the `data` field was specified in the Create payment run operation.     
* _GET /v1/payment-runs/{paymentRunId}/summary_ 
  *resource*: get_payment_run_summary  
  *description*: Retrives the summary of a payment run. 
* _GET /v1/payment-runs_ 
  *resource*: get_payment_runs  
  *description*: Retrieves the information about all payment runs. You can define filterable fields to restrict the data returned in the response.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/payment-runs?status=Processed  - /v1/payment-runs?targetDate=2017-10-10&status=Pending  - /v1/payment-runs?status=Completed&sort=+updatedDate 
* _GET /v1/payment-runs/{paymentRunId}_ 
  *resource*: get_payment_run  
  *description*: Retrives the information about a specific payment run. 
* _GET /v1/hostedpages_ 
  *resource*: get_hosted_pages  
  *description*: Returns the Payment Pages configuration metadata, specifically, page ID, page version, payment method type.  The following are the version-specific and general REST requests for Payment Pages:  * The request for Payment Pages 1.0 configuration information: `GET <BaseURL>/hostedpages?version=1` * The request for Payment Pages 2.0 configuration information: `GET <BaseURL>/hostedpages?version=2` * The request for all versions of Payment Pages configuration information: `GET <BaseURL>/hostedpages`  ## Notes If you do not have the corresponding tenant setting enabled, e.g., the request `version` parameter set to 2 with the Payment Pages 2.0 setting disabled, you will receive an error. 
* _GET /v1/object/import/{id}_ 
  *resource*: object_get_import  
* _GET /v1/object/invoice/{id}_ 
  *resource*: object_get_invoice  
* _GET /v1/object/invoice-adjustment/{id}_ 
  *resource*: object_get_invoice_adjustment  
* _GET /v1/object/invoice-item/{id}_ 
  *resource*: object_get_invoice_item  
* _GET /v1/revenue-schedules/invoice-items/{invoice-item-id}_ 
  *resource*: get_r_sby_invoice_item  
  *description*: Retrieves the details of a revenue schedule by specifying the invoice item ID. 
* _GET /v1/object/invoice-item-adjustment/{id}_ 
  *resource*: object_get_invoice_item_adjustment  
* _GET /v1/revenue-schedules/invoice-item-adjustments/{invoice-item-adj-key}_ 
  *resource*: get_r_sby_invoice_item_adjustment  
  *description*: Retrieves the details of a revenue schedule by specifying a valid invoice item adjustment identifier. Request and response field descriptions and sample code are provided. 
* _GET /v1/orders/invoiceOwner/{accountNumber}_ 
  *resource*: get_orders_by_invoice_owner  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about all orders for a specified invoice owner. 
* _GET /v1/object/invoice-payment/{id}_ 
  *resource*: object_get_invoice_payment  
* _GET /v1/object/invoice-split/{id}_ 
  *resource*: object_get_invoice_split  
* _GET /v1/object/invoice-split-item/{id}_ 
  *resource*: object_get_invoice_split_item  
* _GET /v1/creditmemos/{creditMemoId}/items_ 
  *resource*: get_credit_memo_items  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a credit memo. A credit memo item is a single line item in a credit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:        - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100      - /v1/creditmemos/402890245c7ca371015c7cb40ac30015/items?amount=100&sort=createdDate      
* _GET /v1/creditmemos/{creditMemoId}/items/{cmitemid}_ 
  *resource*: get_credit_memo_item  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about a specific item of a credit memo. A credit memo item is a single line item in a credit memo. 
* _GET /v1/debitmemos/{debitMemoId}/items_ 
  *resource*: get_debit_memo_items  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a debit memo. A debit memo item is a single line item in a debit memo.   ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.   Examples:  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100  - /v1/debitmemos/402890245c7ca371015c7cb40b28001f/items?amount=100&sort=createdDate 
* _GET /v1/debitmemos/{debitMemoId}/items/{dmitemid}_ 
  *resource*: get_debit_memo_item  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about a specific item of a debit memo. A debit memo item is a single line item in a debit memo. 
* _GET /v1/invoices/{invoiceId}/items_ 
  *resource*: get_invoice_items  
  *description*: Retrieves the information about all items of a specified invoice.  
* _GET /v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts_ 
  *resource*: get_credit_memo_item_parts  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a credit memo part. A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items. 
* _GET /v1/creditmemos/{creditMemoId}/parts/{partid}/itemparts/{itempartid}_ 
  *resource*: get_credit_memo_item_part  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about a specific credit memo part item.  A credit memo part item is a single line item in a credit memo part. A credit memo part can consist of several different types of items. 
* _GET /v1/payments/{paymentId}/parts/{partid}/itemparts_ 
  *resource*: get_payment_item_parts  
  *description*: **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all items of a payment part. A payment part item is a single line item in a payment part. A payment part can consist of several different types of items. 
* _GET /v1/payments/{paymentId}/parts/{partid}/itemparts/{itempartid}_ 
  *resource*: get_payment_item_part  
  *description*: **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about a specific payment part item. A payment part item is a single line item in a payment part. A payment part can consist of several different types of items. 
* _GET /v1/refunds/{refundId}/parts/{refundpartid}/itemparts_ 
  *resource*: get_refund_item_parts  
  *description*: **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the information about all items of a refund part. A refund part item is a single line item in a refund part. A refund part can consist of several different types of items. 
* _GET /v1/refunds/{refundId}/parts/{refundpartid}/itemparts/{itempartid}_ 
  *resource*: get_refund_item_part  
  *description*: **Note:** This operation is only available if you have the [Invoice Item Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/C_Invoice_Item_Settlement) feature enabled. Invoice Item Settlement must be used together with other Invoice Settlement features (Unapplied Payments, and Credit and Debit memos).  If you wish to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.    Retrieves the information about a specific refund part item. A refund part item is a single line item in a refund part. A refund part can consist of several different types of items. 
* _GET /objects/jobs_ 
  *resource*: get_all_custom_object_bulk_jobs  
  *description*: Lists all custom object bulk jobs submitted by your tenant. 
* _GET /objects/jobs/{id}_ 
  *resource*: get_custom_object_bulk_job  
  *description*: Retrieves the custom object bulk job details by job ID.  Only the users that have the "View Custom Objects" permission can retrieve custom object bulk jobs. See [Platform Permissions](https://knowledgecenter.zuora.com/Billing/Tenant_Management/A_Administrator_Settings/User_Roles/h_Platform_Roles#Platform_Permissions) for more information. 
* _GET /query/jobs_ 
  *resource*: get_data_query_jobs  
  *description*: Returns a list of [data query](https://knowledgecenter.zuora.com/DC_Developers/BA_Data_Query) jobs that have been created in your Zuora tenant. You can filter the list by status.  If you are an administrator, you can retrieve all the query jobs in your tenant. Otherwise, you can only retrieve your own query jobs. 
* _GET /query/jobs/{job-id}_ 
  *resource*: get_data_query_job  
  *description*: Retrieves a [data query](https://knowledgecenter.zuora.com/DC_Developers/BA_Data_Query) job. You can use this operation to track the status of the query job and obtain the URL of the query results.  If you are an administrator, you can retrieve every query job in your tenant.   If you are a non-admin user and try to retrieve a query job that you are not the owner of, you will get a 403 response indicating that you are forbidden from viewing this job. As a non-admin user, you can only retrieve your own query job. 
* _GET /v1/journal-entries/{je-number}_ 
  *resource*: get_summary_journal_entry  
  *description*: This REST API reference describes how to get information about a summary journal entry by its journal entry number. 
* _GET /v1/journal-entries/journal-runs/{jr-number}_ 
  *resource*: get_all_summary_journal_entries  
  *description*:  This REST API reference describes how to retrieve information about all summary journal entries in a journal run. 
* _GET /v1/journal-runs/{jr-number}_ 
  *resource*: get_journal_run  
  *description*: This REST API reference describes how to get information about a journal run. Request and response field descriptions and sample code are provided. 
* _GET /workflows/metrics.json_ 
  *resource*: get_workflows_usages  
  *description*: Gets workflow task usage sorted by day within a specified time frame. 
* _GET /notifications/notification-definitions_ 
  *resource*: get_query_notification_definitions  
  *description*: Queries notification definitions with the specified filters.  **Note**: This operation is only applicable to notifications for custom events. 
* _GET /notifications/notification-definitions/{id}_ 
  *resource*: get_get_notification_definition  
  *description*: Queries the notification definition of the given ID.  **Note**: This operation is only applicable to notifications for custom events. 
* _GET /v1/orders_ 
  *resource*: get_all_orders  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).   Retrieves information about all orders in your tenant. By default, it returns the first page of the orders.  
* _GET /v1/orders/{orderNumber}_ 
  *resource*: get_order  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).          Retrieves the detailed information about a specified order. 
* _GET /v1/order-line-items/{itemId}_ 
  *resource*: get_order_line_item  
  *description*: **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  **Note:** You also need to enable the [Orders](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Orders) feature to access the Order Line Items feature. Orders is now generally available as of Zuora Billing Release 284 (August 2020). If you are an existing Zuora Subscribe and Amend customer and want to adopt Orders, see [What is Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization#What_is_Orders_Harmonization.3F) and join the [Orders Harmonization community group](https://community.zuora.com/t5/Orders-Harmonization/gp-p/Orders-Harmonization) for more information. If you want to enable Orders, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about a specified order line item. 
* _GET /v1/creditmemos/{creditMemoId}/parts_ 
  *resource*: get_credit_memo_parts  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all parts of a credit memo. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a credit memo. 
* _GET /v1/creditmemos/{creditMemoId}/parts/{partid}_ 
  *resource*: get_credit_memo_part  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific credit memo part. A credit memo can consist of an unapplied part, and several parts applied to invoices and debit memos. 
* _GET /v1/payments/{paymentId}/parts_ 
  *resource*: get_payment_parts  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all parts of a payment. A payment can consist of an unapplied part, and several parts applied to invoices and debit memos. You can use this operation to get all the applied and unapplied portions of a payment. 
* _GET /v1/payments/{paymentId}/parts/{partid}_ 
  *resource*: get_payment_part  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific payment part. A payment can consist of an unapplied part, and several parts applied to invoices and debit memos. 
* _GET /v1/refunds/{refundId}/parts_ 
  *resource*: get_refund_parts  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all parts of a refund. 
* _GET /v1/refunds/{refundId}/parts/{refundpartid}_ 
  *resource*: get_refund_part  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific refund part. 
* _GET /v1/object/payment/{id}_ 
  *resource*: object_get_payment  
  *description*: Retrieves the information about one specific payment.  
* _GET /v1/payments_ 
  *resource*: get_retrieve_all_payments  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all payments from all your customer accounts.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.  Examples:  - /v1/payments?status=Processed  - /v1/payments?currency=USD&status=Processed  - /v1/payments?status=Processed&type=External&sort=+number 
* _GET /v1/payments/{paymentId}_ 
  *resource*: get_payment  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about one specific payment. 
* _GET /v1/object/payment-method/{id}_ 
  *resource*: object_get_payment_method  
* _GET /v1/payment-methods/{payment-method-id}_ 
  *resource*: get_payment_method  
  *description*: This operation allows you to get the detailed information about a payment method. 
* _GET /v1/object/payment-method-snapshot/{id}_ 
  *resource*: object_get_payment_method_snapshot  
  *description*: This REST API reference describes how to retrieve a Payment Method Snapshot.  A Payment Method Snapshot is a copy of the particular Payment Method used in a transaction. If the Payment Method is deleted, the Payment Method Snapshot continues to retain the data used in each of the past transactions.  ## Notes The following Payment Method fields are not available in Payment Method Snapshots:  * `Active` * `AchAddress1` * `AchAddress2` * `CreatedById` * `CreatedDate` * `UpdatedById` * `UpdatedDate`  The Payment Method Snapshot field `PaymentMethodId` is not available in Payment Methods. 
* _GET /v1/object/payment-method-transaction-log/{id}_ 
  *resource*: object_get_payment_method_transaction_log  
* _GET /v1/object/payment-transaction-log/{id}_ 
  *resource*: object_get_payment_transaction_log  
  *description*: Retrieves information about a specific payment transaction log. 
* _GET /v1/paymentgateways_ 
  *resource*: get_paymentgateways  
  *description*: Retrieves the basic information about all the payment gateways. 
* _GET /v1/catalog/product/{product-id}_ 
  *resource*: get_product  
  *description*: Retrieves detailed information about a specific product, including information about its product rate plans and charges.  
* _GET /v1/catalog/products_ 
  *resource*: get_catalog  
  *description*: Retrieves the entire product catalog, including all products, features, and their corresponding product rate plans, charges. Products are returned in reverse chronological order on the `UpdatedDate` field.   With product rate plans and rate plan charges, the REST API has a maximum array size.   For a use case of this operation, see [Retrieve the product catalog](https://www.zuora.com/developer/api-guides/#Retrieve-the-product-catalog). 
* _GET /v1/object/product/{id}_ 
  *resource*: object_get_product  
* _GET /v1/revenue-recognition-rules/product-charges/{charge-key}_ 
  *resource*: get_revenue_rec_ruleby_product_rate_plan_charge  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the revenue recognition rule associated with a production rate plan charge by specifying the charge ID. 
* _GET /v1/revenue-schedules/product-charges/{charge-key}/{account-key}_ 
  *resource*: get_r_sby_product_charge_and_billing_account  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves the details about all revenue schedules of a product rate plan charge by specifying the charge ID and billing account ID. 
* _GET /v1/object/product-feature/{id}_ 
  *resource*: object_get_product_feature  
* _GET /v1/object/product-rate-plan/{id}_ 
  *resource*: object_get_product_rate_plan  
* _GET /v1/rateplan/{product_id}/productRatePlan_ 
  *resource*: get_product_rate_plans  
  *description*: Retrieves information about all product rate plans of a specific product.  For a use case of this operation, see [Retrieve the product catalog](https://www.zuora.com/developer/api-guides/#Retrieve-the-product-catalog). 
* _GET /v1/object/product-rate-plan-charge/{id}_ 
  *resource*: object_get_product_rate_plan_charge  
* _GET /v1/object/product-rate-plan-charge-tier/{id}_ 
  *resource*: object_get_product_rate_plan_charge_tier  
* _GET /v1/payment-methods/{payment-method-id}/profiles_ 
  *resource*: get_stored_credential_profiles  
  *description*: Retrieves the stored credential profiles within a payment method.  **Note:** This feature is in the **Early Adopters** phase. We are actively soliciting feedback from a small set of early adopters before releasing as generally available. 
* _GET /v1/ramps/{rampNumber}_ 
  *resource*: get_ramp_by_ramp_number  
  *description*: **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves the latest definition of a specified ramp. 
* _GET /v1/subscriptions/{subscriptionKey}/ramps_ 
  *resource*: get_ramps_by_subscription_key  
  *description*: **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.   Retrieves the definition of the ramp associated with a specified subscription. 
* _GET /v1/orders/{orderNumber}/ramp-metrics_ 
  *resource*: get_ramp_metrics_by_order_number  
  *description*: **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves key ramp metrics about a specified order, including the following metrics:  * TCB, TCV in the Ramp level * TCB, TCV in the Interval level * TCB, TCV, Quantity, and MRR in Interval Metrics * Delta TCB, Delta TCV, Delta Quantity, and Delta MRR in Interval Delta Metrics  See [Key metrics for Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/F_Key_metrics_for_Ramps) for more information. 
* _GET /v1/ramps/{rampNumber}/ramp-metrics_ 
  *resource*: get_ramp_metrics_by_ramp_number  
  *description*: **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves key metrics about a specified ramp, including the following metrics:  * TCB, TCV in the Ramp level * TCB, TCV in the Interval level * TCB, TCV, Quantity, and MRR in Interval Metrics * Delta TCB, Delta TCV, Delta Quantity, and Delta MRR in Interval Delta Metrics  See [Key metrics for Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/F_Key_metrics_for_Ramps) for more information. 
* _GET /v1/subscriptions/{subscriptionKey}/ramp-metrics_ 
  *resource*: get_ramp_metrics_by_subscription_key  
  *description*: **Note**: This operation is only available if you have the Ramps feature enabled. The [Orders](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/AA_Overview_of_Orders) feature must be enabled before you can access the [Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/A_Overview_of_Ramps_and_Ramp_Metrics) feature. The Ramps feature is available for customers with Enterprise and Nine editions by default. If you are a Growth customer, see [Zuora Editions](https://knowledgecenter.zuora.com/BB_Introducing_Z_Business/C_Zuora_Editions) for pricing information coming October 2020.  Retrieves key ramp metrics about a specified subscription, including the following metrics:  * TCB, TCV in the Ramp level * TCB, TCV in the Interval level * TCB, TCV, Quantity, and MRR in Interval Metrics * Delta TCB, Delta TCV, Delta Quantity, and Delta MRR in Interval Delta Metrics  See [Key metrics for Ramps](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Ramps_and_Ramp_Metrics/F_Key_metrics_for_Ramps) for more information. 
* _GET /v1/object/rate-plan/{id}_ 
  *resource*: object_get_rate_plan  
* _GET /v1/object/rate-plan-charge/{id}_ 
  *resource*: object_get_rate_plan_charge  
* _GET /v1/object/rate-plan-charge-tier/{id}_ 
  *resource*: object_get_rate_plan_charge_tier  
* _GET /v1/object/refund/{id}_ 
  *resource*: object_get_refund  
* _GET /v1/refunds_ 
  *resource*: get_refunds  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about all refunds. Two types of refunds are available, electronic refunds and external refunds.  ### Filtering  You can use query parameters to restrict the data returned in the response. Each query parameter corresponds to one field in the response body.  If the value of a filterable field is string, you can set the corresponding query parameter to `null` when filtering. Then, you can get the response data with this field value being `null`.  Examples:  - /v1/refunds?status=Processed  - /v1/refunds?amount=4&status=Processed  - /v1/refunds?status=Processed&type=External&sort=+number 
* _GET /v1/refunds/{refundId}_ 
  *resource*: get_refund  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.   Retrieves the information about a specific refund. 
* _GET /v1/object/refund-invoice-payment/{id}_ 
  *resource*: object_get_refund_invoice_payment  
* _GET /v1/object/refund-transaction-log/{id}_ 
  *resource*: object_get_refund_transaction_log  
* _GET /v1/settings/finance/revenue-automation-start-date_ 
  *resource*: get_revenue_automation_start_date  
  *description*: Describes how to get the revenue automation start date. Request and response field descriptions and sample code are provided. 
* _GET /v1/revenue-events/{event-number}_ 
  *resource*: get_revenue_event_details  
  *description*: This REST API reference describes how to get revenue event details by specifying the revenue event number. Request and response field descriptions and sample code are provided. 
* _GET /v1/revenue-items/revenue-events/{event-number}_ 
  *resource*: get_revenue_items_by_charge_revenue_event_number  
  *description*: This REST API reference describes how to get the details of each revenue item in a revenue event by specifying the revenue event number. Request and response field descriptions and sample code are provided. 
* _GET /v1/revenue-events/revenue-schedules/{rs-number}_ 
  *resource*: get_revenue_event_for_revenue_schedule  
  *description*:  This REST API reference describes how to get all revenue events in a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 
* _GET /v1/revenue-items/revenue-schedules/{rs-number}_ 
  *resource*: get_revenue_items_by_revenue_schedule  
  *description*: This REST API reference describes how to get the details for each revenue items in a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 
* _GET /v1/revenue-schedules/{rs-number}_ 
  *resource*: get_rs  
  *description*: Retrieves the details of a revenue schedule by specifying the revenue schedule number. Request and response field descriptions and sample code are provided. 
* _GET /v1/sequence-sets_ 
  *resource*: get_sequence_sets  
  *description*: Retrieves information about all sequence sets configured for billing documents, payments, and refunds. Billing documents include invoices, credit memos, and debit memos.  You can use query parameters to restrict the data returned in the response.  **Note**: The Credit and Debit Memos feature is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  
* _GET /v1/sequence-sets/{id}_ 
  *resource*: get_sequence_set  
  *description*: Retrieves information about a specific sequence set configured for billing documents, payments, and refunds. Billing documents include invoices, credit memos, and debit memos  **Note**: The Credit and Debit Memos feature is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  
* _GET /settings/listing_ 
  *resource*: get_list_all_settings  
  *description*: Get a list of all available settings in your tenant.   The response message is by default in JSON format. If you want to receive all the availabe settings in csv format, include `Accept` in the header parameters and set it to `application/csv`.              See a [200 response sample in JSON format](https://assets.zuora.com/zuora-documentation/ListAllSettingsResponseSample.json).  See a [200 response sample in CSV format](https://assets.zuora.com/zuora-documentation/ListAllSettingsResponseSample.csv).  You can find a specific operate of an available setting item in your tenant from the 200 response body of this call. See the following tutorials of Settings API for how to operate on a specifc setting item.   * Billing Rules:    * [Get a specific setting - Billing Rules](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/AA_Get_a_specific_setting_-_Billing_Rules)    * [Update a specific setting - Billing Rules](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/AB_Update_a_specific_setting_-_Billing_Rules)  * Age Buckets:    * [Get Age Buckets](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_Age_Buckets)    * [Update Age Buckets](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Update_Age_Buckets)  * Invoice Templates:    * [Get a specific Invoice Template](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_a_specific_Invoice_Template)    * [Get all Invoice Templates](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_all_Invoice_Templates)    * [Create a new Invoice Template](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Create_a_new_Invoice_Template)  * Communications Profiles:    * [Get all Communication Profiles](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_all_Communication_Profiles)    * [Create a new Communication Profile](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Create_a_new_Communication_Profile)    * [Modify a Communication Profile](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Modify_a_Communication_Profile)    * [Get all Notifications under a particular Communication Profile](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_all_Notifications_under_a_particular_Communication_Profile)  * Chart of Accounts:    * [Get Chart of Accounts](https://knowledgecenter.zuora.com/DC_Developers/BB_C_Settings_API/Settings_API_tutorials/Get_Chart_of_Accounts)    * [Add a new Chart of Account](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Add_a_new_Chart_of_Account)  * Quote Templates:    * [Get all Quote Templates](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Get_all_Quote_Templates)    * [Get a specific Quote Template](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Get_a_specific_Quote_Template)    * [Create a new Quote Template](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Create_a_new_Quote_Template)  * Custom Fields:    * [View all custom fields](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/View_all_custom_fields)    * [View custom fields of a specific object](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/View_custom_fields_of_a_specific_object)    * [Update custom fields of a specific object](https://knowledgecenter.zuora.com/Central_Platform/API/BB_C_Settings_API/Settings_API_tutorials/Update_custom_fields_of_a_specific_object) 
* _GET /v1/amendments/subscriptions/{subscription-id}_ 
  *resource*: get_amendments_by_subscription_id  
  *description*: Retrieves detailed information about the amendment with the specified subscription.
* _GET /v1/object/subscription/{id}_ 
  *resource*: object_get_subscription  
* _GET /v1/orders/subscription/{subscriptionNumber}_ 
  *resource*: get_orders_by_subscription_number  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about all orders for a specified subscription. Any orders containing the changes on the specified subscription are returned. 
* _GET /v1/subscriptions/{subscription-key}_ 
  *resource*: get_subscriptions_by_key  
  *description*: This REST API reference describes how to retrieve detailed information about a specified subscription in the latest version. 
* _GET /v1/charge-revenue-summaries/subscription-charges/{charge-key}_ 
  *resource*: get_crs_by_charge_id  
  *description*: Retrieves the details of a charge revenue summary by specifying the subscription charge ID. This response retrieves all revenue items associated with a charge revenue summary. 
* _GET /v1/revenue-recognition-rules/subscription-charges/{charge-key}_ 
  *resource*: get_revenue_rec_rules  
  *description*: Retrieves the revenue recognition rule associated with a subscription charge by specifying the charge ID. Request and response field descriptions and sample code are provided. 
* _GET /v1/revenue-schedules/subscription-charges/{charge-key}_ 
  *resource*: get_r_sfor_subsc_charge  
  *description*: Retrieves the revenue schedule details by specifying subscription charge ID. Request and response field descriptions and sample code are provided 
* _GET /v1/orders/subscriptionOwner/{accountNumber}_ 
  *resource*: get_orders_by_subscription_owner  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  **Note:** The [Order Line Items](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Order_Line_Items/AA_Overview_of_Order_Line_Items) feature is in the **Early Adopter** phase. We are actively soliciting feedback from a small set of early adopters before releasing it as generally available. If you want to join this early adopter program, submit a request at [Zuora Global Support](https://support.zuora.com/).  Retrieves the detailed information about all orders for a specified subscription owner. Any orders containing the changes on the subscriptions owned by this account are returned. 
* _GET /v1/object/subscription-product-feature/{id}_ 
  *resource*: object_get_subscription_product_feature  
* _GET /v1/accounts/{account-key}/summary_ 
  *resource*: get_account_summary  
  *description*: Retrieves detailed information about the specified customer account.  The response includes the account information and a summary of the account’s subscriptions, invoices, payments, and usages for the last six recently updated subscriptions.  ## Notes  Returns only the six most recent subscriptions based on the subscription updatedDate. Within those subscriptions, there may be many rate plans and many rate plan charges. These items are subject to the maximum limit on the array size.  
* _GET /notifications/history/tasks/{id}_ 
  *resource*: get_get_notification_history_deletion_task  
  *description*: Get the notification history deletion task by ID.  **Note**: This operation is only available if you have the Notification and the Configurable Event features enabled. 
* _GET /workflows/tasks_ 
  *resource*: get_workflows_tasks  
  *description*: Retrieves a list of workflow tasks available in your Zuora tenant. 
* _GET /workflows/tasks/{task_id}_ 
  *resource*: get_workflows_task  
  *description*: Retrieves a specific workflow task by its ID. 
* _GET /v1/creditmemos/{creditMemoId}/items/{cmitemid}/taxation-items_ 
  *resource*: get_taxation_items_of_credit_memo_item  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about the taxation items of a specific credit memo item.  
* _GET /v1/debitmemos/{debitMemoId}/items/{dmitemid}/taxation-items_ 
  *resource*: get_taxation_items_of_debit_memo_item  
  *description*: **Note:** This operation is only available if you have [Invoice Settlement](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement) enabled. The Invoice Settlement feature is generally available as of Zuora Billing Release 296 (March 2021). This feature includes Unapplied Payments, Credit and Debit Memo, and Invoice Item Settlement. If you want to enable Invoice Settlement, see [Invoice Settlement Enablement and Checklist Guide](https://knowledgecenter.zuora.com/Billing/Billing_and_Payments/Invoice_Settlement/Invoice_Settlement_Migration_Checklist_and_Guide) for more information.  Retrieves information about the taxation items of a specific debit memo item. 
* _GET /v1/invoices/{invoiceId}/items/{itemId}/taxation-items_ 
  *resource*: get_taxation_items_of_invoice_item  
  *description*: Retrieves information about the taxation items of a specific invoice item.  
* _GET /v1/object/taxation-item/{id}_ 
  *resource*: object_get_taxation_item  
* _GET /v1/taxationitems/{id}_ 
  *resource*: get_taxation_item  
  *description*: Retrieves the information about a specific taxation item by ID. 
* _GET /v1/orders/term/{subscriptionNumber}_ 
  *resource*: get_subscription_term_info  
  *description*: **Note:** This feature is only available if you have the [Order Metrics](https://knowledgecenter.zuora.com/BC_Subscription_Management/Orders/AA_Overview_of_Orders#Order_Metrics) feature enabled. As of Zuora Billing Release 284, Orders is generally available and the Order Metrics feature is no longer available as a standalone feature. If you are an existing Subscribe and Amend customer and want Order Metrics only, you must turn on [Orders Harmonization](https://knowledgecenter.zuora.com/Billing/Subscriptions/Orders/Orders_Harmonization/Orders_Harmonization). You can still keep the existing Subscribe and Amend API integrations to create and manage subscriptions.  Retrieves the terms of the specified subscription. 
* _GET /v1/object/unit-of-measure/{id}_ 
  *resource*: object_get_unit_of_measure  
* _GET /v1/object/usage/{id}_ 
  *resource*: object_get_usage  
* _GET /v1/subscriptions/{subscription-key}/versions/{version}_ 
  *resource*: get_subscriptions_by_key_and_version  
  *description*: This REST API reference describes how to retrieve detailed information about a specified subscription in a specified version. When you create a subscription amendment, you create a new version of the subscription. You can use this method to retrieve information about a subscription in any version. 
* _GET /workflows_ 
  *resource*: get_workflows  
  *description*: Retrieves a list of workflows available in your Zuora tenant.       
* _GET /workflows/{workflow_id}_ 
  *resource*: get_workflow  
  *description*: Retrieves information about a specific workflow by its ID. 
