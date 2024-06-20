# keap pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/keap.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /v1/affiliates_ 
  *resource*: list_affiliates_using_get  
  *description*: Retrieves a list of all affiliates
* _GET /v1/affiliates/{id}_ 
  *resource*: get_affiliate_using_get  
  *description*: Retrieve a single affiliate
* _GET /v1/affiliates/commissions_ 
  *resource*: list_commissions_using_get  
  *description*: Retrieve a list of Commissions based on Affiliate or Date Range
* _GET /v1/affiliates/programs_ 
  *resource*: list_programs_using_get  
  *description*: Retrieve a list of Commission Programs
* _GET /v1/affiliates/redirectlinks_ 
  *resource*: list_affiliate_redirect_links_using_get  
  *description*: Retrieves a list of all affiliate redirects
* _GET /v1/affiliates/summaries_ 
  *resource*: list_summaries_using_get  
  *description*: Retrieve a list of affiliate summaries
* _GET /v1/appointments_ 
  *resource*: list_appointments_using_get  
  *description*: Retrieves all appointments for the authenticated user
* _GET /v1/appointments/{appointmentId}_ 
  *resource*: get_appointment_using_get  
  *description*: Retrieves a specific appointment with respect to user permissions. The authenticated user will need the "can view all records" permission for Task/Appt/Notes
* _GET /v1/campaigns_ 
  *resource*: list_campaigns_using_get  
  *description*: Retrieves all campaigns for the authenticated user
* _GET /v1/campaigns/{campaignId}_ 
  *resource*: get_campaign_using_get  
  *description*: Retrieves a single campaign
* _GET /v1/companies_ 
  *resource*: list_companies_using_get  
  *description*: Retrieves a list of all companies
* _GET /v1/companies/{companyId}_ 
  *resource*: get_company_using_get  
  *description*: Retrieves a single company
* _GET /v1/contacts/{contactId}/creditCards_ 
  *resource*: list_credit_cards_using_get  
  *description*: List all Credit Cards on a contact
* _GET /v1/contacts/{contactId}/tags_ 
  *resource*: list_applied_tags_using_get  
  *description*: Retrieves a list of tags applied to a given contact
* _GET /v1/locales/countries_ 
  *resource*: list_countries_using_get  
* _GET /v1/affiliates/model_ 
  *resource*: retrieve_affiliate_model_using_get  
  *description*: Get the custom fields for the Affiliate object
* _GET /v1/appointments/model_ 
  *resource*: retrieve_appointment_model_using_get  
  *description*: Get the custom fields for the Appointment object
* _GET /v1/companies/model_ 
  *resource*: retrieve_company_model_using_get  
  *description*: Get the custom fields and optional properties for the Company object
* _GET /v1/contacts/model_ 
  *resource*: retrieve_contact_model_using_get  
  *description*: Get the custom fields and optional properties for the Contact object
* _GET /v1/notes/model_ 
  *resource*: retrieve_note_model_using_get  
  *description*: Get the custom fields for the Note object
* _GET /v1/opportunities/model_ 
  *resource*: retrieve_opportunity_model_using_get  
  *description*: Get the custom fields for the Opportunity object
* _GET /v1/orders/model_ 
  *resource*: retrieve_order_model_using_get  
  *description*: Get the custom fields for the Order object
* _GET /v1/subscriptions/model_ 
  *resource*: retrieve_subscription_model_using_get  
  *description*: Get the custom fields for the Subscription object
* _GET /v1/tasks/model_ 
  *resource*: retrieve_task_model_using_get  
  *description*: Get the custom fields for the Task object
* _GET /v1/locales/defaultOptions_ 
  *resource*: default_options_using_get  
* _GET /v1/orders_ 
  *resource*: list_orders_using_get  
  *description*: Retrieves a list of all orders using the specified search criteria. Each order may or may not have items.  Potential values for order status:`DRAFT`, `SENT`, `VIEWED`, `PAID`
* _GET /v1/orders/{orderId}_ 
  *resource*: get_order_using_get  
  *description*: Retrieves a single order. The order may or may not have items.  Potential values for order status:`DRAFT`, `SENT`, `VIEWED`, `PAID`
* _GET /v1/orders/{orderId}/transactions_ 
  *resource*: list_transactions_for_order_using_get  
  *description*: Retrieves a list of all transactions on a given order using the specified search criteria
* _GET /v1/transactions_ 
  *resource*: list_transactions_using_get  
  *description*: Retrieves a list transactions for a given contact
* _GET /v1/transactions/{transactionId}_ 
  *resource*: get_transaction_using_get  
  *description*: Retrieves a single transaction
* _GET /v1/contacts/{contactId}/emails_ 
  *resource*: list_emails_for_contact_using_get  
  *description*: List Emails that have been sent to a Contact
* _GET /v1/emails_ 
  *resource*: list_emails_using_get  
  *description*: Retrieve a list of emails that have been sent  Keap is currently investigating an issue with degraded performance of this endpoint with very large (millions of records) record sets
* _GET /v1/emails/{id}_ 
  *resource*: get_email_using_get  
  *description*: Retrieves a single email that has been sent
* _GET /v1/hooks/event_keys_ 
  *resource*: list_hook_event_types  
  *description*: List the available types of Events that can be listened to
* _GET /v1/files_ 
  *resource*: list_files_using_get  
  *description*: Retrieves a list of all files
* _GET /v1/files/{fileId}_ 
  *resource*: get_file_using_get  
  *description*: Retrieves metadata about a specific file. Optionally returns the base64 encoded file data.
* _GET /v1/contacts/{id}_ 
  *resource*: get_contact_using_get  
  *description*: Retrieves a single contact
* _GET /v1/orders/{orderId}/payments_ 
  *resource*: list_order_payments_using_get  
  *description*: Retrieves a list of payments made against a given order, including historical or external payments of cash or credit card.
* _GET /v1/merchants_ 
  *resource*: get_merchant_accounts_using_get  
  *description*: Retrieves a list of all merchant accounts
* _GET /v1/notes_ 
  *resource*: list_notes_using_get  
  *description*: Retrieves a list of all notes
* _GET /v1/notes/{noteId}_ 
  *resource*: get_note_using_get  
  *description*: Retrieves a single note
* _GET /v1/opportunities_ 
  *resource*: list_opportunities_using_get  
  *description*: Retrieves a list of all opportunities.  Please note: the sample response erroneously shows properties, such as _stage reasons_, that are unavailable through the list endpoint. Such properties are only available through the retrieve operation. Future versions of the Opportunity resource will correct the oversight.
* _GET /v1/opportunities/{opportunityId}_ 
  *resource*: get_opportunity_using_get  
  *description*: Retrives a single opportunity
* _GET /v1/products_ 
  *resource*: list_products_using_get  
  *description*: Retrieves a list of all products
* _GET /v1/products/{productId}_ 
  *resource*: retrieve_product_using_get  
* _GET /v1/products/sync_ 
  *resource*: list_products_from_sync_token_using_get  
  *description*: The Sync endpoint returns a set of products that have been updated or created since the last result set was retrieved, minus any products that have been deleted.
* _GET /v1/products/{productId}/subscriptions/{subscriptionId}_ 
  *resource*: retrieve_product_subscription_using_get  
* _GET /v1/account/profile_ 
  *resource*: get_account_profile_using_get  
  *description*: Retrieves profile/company info for an account.
* _GET /v1/locales/countries/{countryCode}/provinces_ 
  *resource*: list_countries_using_get_1  
* _GET /v1/affiliates/{affiliateId}/clawbacks_ 
  *resource*: list_affiliate_clawbacks_using_get  
  *description*: Retrieves a list of all affiliate clawbacks
* _GET /v1/affiliates/{affiliateId}/payments_ 
  *resource*: list_payments_using_get  
  *description*: Retrieves a list of all affiliate payments
* _GET /v1/setting/application/configuration_ 
  *resource*: get_configuration_using_get  
  *description*: Get the properties for the current application's configuration
* _GET /v1/hooks_ 
  *resource*: list_stored_hook_subscriptions  
  *description*: Lists your hook subscriptions.
* _GET /v1/hooks/{key}_ 
  *resource*: retrieve_a_hook_subscription  
  *description*: Retrieves an existing hook subscription and its status.  If your hook subscription becomes inactive, you may request an activation attempt via [Verify a Hook Subscription](#!/REST_Hooks/verify_a_hook_subscription).
* _GET /v1/contacts_ 
  *resource*: list_contacts_using_get  
  *description*: Retrieves a list of all contacts
* _GET /v1/users_ 
  *resource*: list_users_using_get  
  *description*: Retrieves a list of all users
* _GET /v1/opportunity/stage_pipeline_ 
  *resource*: list_opportunity_stage_pipelines_using_get  
  *description*: Retrieves a list of all opportunity stages with pipeline details
* _GET /v1/setting/application/enabled_ 
  *resource*: get_application_enabled_using_get  
  *description*: Retrieves whether the application is enabled
* _GET /v1/setting/contact/optionTypes_ 
  *resource*: get_contact_option_types_using_get  
  *description*: Lists the Contact types in a comma-separated list.   *Note:* This is now provided by GET /setting/application/configuration
* _GET /v1/users/{userId}/signature_ 
  *resource*: get_user_signature_using_get  
  *description*: Retrieves a HTML snippet that contains the user's email signature.
* _GET /v1/subscriptions_ 
  *resource*: list_subscriptions_using_get  
  *description*: Retrieves a list of all subcriptions using the specified search criteria.
* _GET /v1/tags_ 
  *resource*: list_tags_using_get  
  *description*: Retrieve a list of tags defined in the application
* _GET /v1/tags/{id}_ 
  *resource*: get_tag_using_get  
  *description*: Retrieves a single tag
* _GET /v1/tags/{tagId}/companies_ 
  *resource*: list_companies_for_tag_id_using_get  
  *description*: Retrieves a list of companies that have the given tag applied
* _GET /v1/tags/{tagId}/contacts_ 
  *resource*: list_contacts_for_tag_id_using_get  
  *description*: Retrieves a list of contacts that have the given tag applied
* _GET /v1/tasks_ 
  *resource*: list_tasks_using_get  
  *description*: Retrieves a list of all tasks using the specified search criteria
* _GET /v1/tasks/search_ 
  *resource*: list_tasks_for_current_user_using_get  
  *description*: Retrieves Tasks belonging to the authenticated user using the specified search criteria
* _GET /v1/tasks/{taskId}_ 
  *resource*: get_task_using_get  
  *description*: Retrieves a single task
* _GET /v1/oauth/connect/userinfo_ 
  *resource*: get_user_info_using_get  
  *description*: Retrieves information for the current authenticated end-user, as outlined by the [OpenID Connect specification](http://openid.net/specs/openid-connect-core-1_0.html#UserInfo).
