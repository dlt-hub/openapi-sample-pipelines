# klaviyo pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/klaviyo.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /api/accounts/_ 
  *resource*: get_accounts  
  *description*: Retrieve the account(s) associated with a given private API key. This will return 1 account object within the array.  You can use this to retrieve account-specific data (contact information, timezone, currency, Public API key, etc.) or test if a Private API Key belongs to the correct account prior to performing subsequent actions with the API.<br><br>*Rate limits*:<br>Burst: `1/s`<br>Steady: `15/m`  **Scopes:** `accounts:read`
* _GET /api/accounts/{id}/_ 
  *resource*: get_account  
  *description*: Retrieve a single account object by its account ID. You can only request the account by which the private API key was generated.<br><br>*Rate limits*:<br>Burst: `1/s`<br>Steady: `15/m`  **Scopes:** `accounts:read`
* _GET /api/campaign-messages/{id}/relationships/campaign/_ 
  *resource*: get_campaign_message_relationships_campaign  
  *description*: Returns the ID of the related campaign<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaign-messages/{id}/campaign/_ 
  *resource*: get_campaign_message_campaign  
  *description*: Return the related campaign<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/tags/{id}/relationships/campaigns/_ 
  *resource*: get_tag_relationships_campaigns  
  *description*: Returns the IDs of all campaigns associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `campaigns:read` `tags:read`
* _GET /api/campaigns/{id}/relationships/campaign-messages/_ 
  *resource*: get_campaign_relationships_campaign_messages  
  *description*: Returns the IDs of all messages associated with the given campaign.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaigns/{id}/campaign-messages/_ 
  *resource*: get_campaign_campaign_messages  
  *description*: Return all messages that belong to the given campaign.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaign-recipient-estimation-jobs/{id}/_ 
  *resource*: get_campaign_recipient_estimation_job  
  *description*: Retrieve the status of a recipient estimation job triggered with the `Create Campaign Recipient Estimation Job` endpoint.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaign-recipient-estimations/{id}/_ 
  *resource*: get_campaign_recipient_estimation  
  *description*: Get the estimated recipient count for a campaign with the provided campaign ID. You can refresh this count by using the `Create Campaign Recipient Estimation Job` endpoint.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaigns/_ 
  *resource*: get_campaigns  
  *description*: Returns some or all campaigns based on filters.  A channel filter is required to list campaigns. Please provide either: `?filter=equals(messages.channel,'email')` to list email campaigns, or `?filter=equals(messages.channel,'sms')` to list SMS campaigns.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaign-send-jobs/{id}/_ 
  *resource*: get_campaign_send_job  
  *description*: Get a campaign send job<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/catalog-category-bulk-create-jobs/_ 
  *resource*: get_create_categories_jobs  
  *description*: Get all catalog category bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-category-bulk-delete-jobs/_ 
  *resource*: get_delete_categories_jobs  
  *description*: Get all catalog category bulk delete jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-category-bulk-delete-jobs/{job_id}/_ 
  *resource*: get_delete_categories_job  
  *description*: Get a catalog category bulk delete job with the given job ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-categories/_ 
  *resource*: get_catalog_categories  
  *description*: Get all catalog categories in an account.  Catalog categories can be sorted by the following fields, in ascending and descending order: `created`  Currently, the only supported integration type is `$custom`, and the only supported catalog type is `$default`.  Returns a maximum of 100 categories per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-categories/{id}/_ 
  *resource*: get_catalog_category  
  *description*: Get a catalog category with the given category ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-items/{id}/categories/_ 
  *resource*: get_catalog_item_categories  
  *description*: Get all catalog categories that an item with the given item ID is in.  Catalog categories can be sorted by the following fields, in ascending and descending order: `created`  Returns a maximum of 100 categories per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-category-bulk-update-jobs/_ 
  *resource*: get_update_categories_jobs  
  *description*: Get all catalog category bulk update jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-item-bulk-create-jobs/_ 
  *resource*: get_create_items_jobs  
  *description*: Get all catalog item bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-item-bulk-delete-jobs/_ 
  *resource*: get_delete_items_jobs  
  *description*: Get all catalog item bulk delete jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-item-bulk-delete-jobs/{job_id}/_ 
  *resource*: get_delete_items_job  
  *description*: Get a catalog item bulk delete job with the given job ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-items/_ 
  *resource*: get_catalog_items  
  *description*: Get all catalog items in an account.  Catalog items can be sorted by the following fields, in ascending and descending order: `created`  Currently, the only supported integration type is `$custom`, and the only supported catalog type is `$default`.  Returns a maximum of 100 items per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-categories/{id}/items/_ 
  *resource*: get_catalog_category_items  
  *description*: Get all items in a category with the given category ID.  Items can be sorted by the following fields, in ascending and descending order: `created`  Returns a maximum of 100 items per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-item-bulk-update-jobs/_ 
  *resource*: get_update_items_jobs  
  *description*: Get all catalog item bulk update jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variant-bulk-create-jobs/_ 
  *resource*: get_create_variants_jobs  
  *description*: Get all catalog variant bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variant-bulk-delete-jobs/_ 
  *resource*: get_delete_variants_jobs  
  *description*: Get all catalog variant bulk delete jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variant-bulk-delete-jobs/{job_id}/_ 
  *resource*: get_delete_variants_job  
  *description*: Get a catalog variant bulk delete job with the given job ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variants/_ 
  *resource*: get_catalog_variants  
  *description*: Get all variants in an account.  Variants can be sorted by the following fields, in ascending and descending order: `created`  Currently, the only supported integration type is `$custom`, and the only supported catalog type is `$default`.  Returns a maximum of 100 variants per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variants/{id}/_ 
  *resource*: get_catalog_variant  
  *description*: Get a catalog item variant with the given variant ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-items/{id}/variants/_ 
  *resource*: get_catalog_item_variants  
  *description*: Get all variants related to the given item ID.  Variants can be sorted by the following fields, in ascending and descending order: `created`  Returns a maximum of 100 variants per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variant-bulk-update-jobs/_ 
  *resource*: get_update_variants_jobs  
  *description*: Get all catalog variant bulk update jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-items/{id}/relationships/categories/_ 
  *resource*: get_catalog_item_relationships_categories  
  *description*: Get all catalog categories that a particular item is in.  Returns a maximum of 100 categories per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/coupon-codes/{id}/relationships/coupon/_ 
  *resource*: get_coupon_relationships_coupon_codes  
  *description*: Gets the coupon relationship associated with the given coupon code id<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
* _GET /api/coupons/{id}/relationships/coupon-codes/_ 
  *resource*: get_coupon_code_relationships_coupon  
  *description*: Gets a list of coupon code relationships associated with the given coupon id<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
* _GET /api/coupon-code-bulk-create-jobs/_ 
  *resource*: get_coupon_code_bulk_create_jobs  
  *description*: Get all coupon code bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
* _GET /api/coupon-codes/_ 
  *resource*: get_coupon_codes  
  *description*: Gets a list of coupon codes associated with a coupon/coupons or a profile/profiles.  A coupon/coupons or a profile/profiles must be provided as required filter params.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `coupon-codes:read`
* _GET /api/coupons/{id}/coupon-codes/_ 
  *resource*: get_coupon_codes_for_coupon  
  *description*: Gets a list of coupon codes associated with the given coupon id<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
* _GET /api/coupons/_ 
  *resource*: get_coupons  
  *description*: Get all coupons in an account.  To learn more, see our [Coupons API guide](https://developers.klaviyo.com/en/docs/use_klaviyos_coupons_api).<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
* _GET /api/coupons/{id}/_ 
  *resource*: get_coupon  
  *description*: Get a specific coupon with the given coupon ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
* _GET /api/coupon-codes/{id}/coupon/_ 
  *resource*: get_coupon_for_coupon_code  
  *description*: Get the coupon associated with a given coupon code ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
* _GET /api/events/_ 
  *resource*: get_events  
  *description*: Get all events in an account  Requests can be sorted by the following fields: `datetime`, `timestamp`  Returns a maximum of 200 events per page.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read`
* _GET /api/flow-actions/{id}/relationships/flow/_ 
  *resource*: get_flow_action_relationships_flow  
  *description*: Get the flow associated with the given action ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/tags/{id}/relationships/flows/_ 
  *resource*: get_tag_relationships_flows  
  *description*: Returns the IDs of all flows associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read` `tags:read`
* _GET /api/flows/{id}/relationships/flow-actions/_ 
  *resource*: get_flow_relationships_flow_actions  
  *description*: Get all [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for flow actions associated with the given flow ID.  Flow action relationships can be sorted by the following fields, in ascending and descending order: `id`,  `status`, `created`, `updated`  Use filters to narrow your results.  Returns a maximum of 50 flow action relationships per request, which can be paginated with offset pagination. Offset pagination uses the following parameters: `page[size]` and `page[number]`.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flow-messages/{id}/flow-action/_ 
  *resource*: get_flow_message_action  
  *description*: Get the flow action for a flow message with the given message ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flow-messages/{id}/relationships/flow-action/_ 
  *resource*: get_flow_message_relationships_action  
  *description*: Get the [relationship](https://developers.klaviyo.com/en/reference/api_overview#relationships) for a flow message's flow action, given the flow ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flows/{id}/flow-actions/_ 
  *resource*: get_flow_flow_actions  
  *description*: Get all flow actions associated with the given flow ID.  Returns a maximum of 50 flows per request, which can be paginated with cursor-based pagination.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flow-actions/{id}/relationships/flow-messages/_ 
  *resource*: get_flow_action_relationships_messages  
  *description*: Get all relationships for flow messages associated with the given flow action ID.  Returns a maximum of 50 flow message relationships per request, which can be paginated with cursor-based pagination.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flow-actions/{id}/flow-messages/_ 
  *resource*: get_flow_action_messages  
  *description*: Get all flow messages associated with the given action ID.  Flow messages can be sorted by the following fields, in ascending and descending order:  ascending: `id`,  `name`, `created`, `updated` descending: `-id`,  `-name`, `-created`, `-updated`  Returns a maximum of 50 flows per request, which can be paginated with offset pagination. Offset pagination uses the following parameters: `page[size]` and `page[number]`<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flows/_ 
  *resource*: get_flows  
  *description*: Get all flows in an account.  Returns a maximum of 50 flows per request, which can be paginated with cursor-based pagination.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flow-actions/{id}/flow/_ 
  *resource*: get_flow_action_flow  
  *description*: Get the flow associated with the given action ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/campaign-messages/{id}/_ 
  *resource*: get_campaign_message  
  *description*: Returns a specific message based on a required id.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/campaigns/{id}/_ 
  *resource*: get_campaign  
  *description*: Returns a specific campaign based on a required id.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
* _GET /api/catalog-category-bulk-create-jobs/{job_id}/_ 
  *resource*: get_create_categories_job  
  *description*: Get a catalog category bulk create job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `categories`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-category-bulk-update-jobs/{job_id}/_ 
  *resource*: get_update_categories_job  
  *description*: Get a catalog category bulk update job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `categories`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-item-bulk-create-jobs/{job_id}/_ 
  *resource*: get_create_items_job  
  *description*: Get a catalog item bulk create job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `items`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-items/{id}/_ 
  *resource*: get_catalog_item  
  *description*: Get a specific catalog item with the given item ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-item-bulk-update-jobs/{job_id}/_ 
  *resource*: get_update_items_job  
  *description*: Get a catalog item bulk update job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `items`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variant-bulk-create-jobs/{job_id}/_ 
  *resource*: get_create_variants_job  
  *description*: Get a catalog variant bulk create job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `variants`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/catalog-variant-bulk-update-jobs/{job_id}/_ 
  *resource*: get_update_variants_job  
  *description*: Get a catalog variate bulk update job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `variants`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/coupon-code-bulk-create-jobs/{job_id}/_ 
  *resource*: get_coupon_code_bulk_create_job  
  *description*: Get a coupon code bulk create job with the given job ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
* _GET /api/coupon-codes/{id}/_ 
  *resource*: get_coupon_code  
  *description*: Returns a Coupon Code specified by the given identifier.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `coupon-codes:read`
* _GET /api/events/{id}/_ 
  *resource*: get_event  
  *description*: Get an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `events:read`
* _GET /api/flow-actions/{id}/_ 
  *resource*: get_flow_action  
  *description*: Get a flow action from a flow with the given flow action ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flow-messages/{id}/_ 
  *resource*: get_flow_message  
  *description*: Get the flow message of a flow with the given message ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/flows/{id}/_ 
  *resource*: get_flow  
  *description*: Get a flow with the given flow ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
* _GET /api/lists/{id}/_ 
  *resource*: get_list  
  *description*: Get a list with the given list ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[list]=profile_count` parameter in your API request:<br>Burst: `1/s`<br>Steady: `15/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `lists:read`
* _GET /api/profile-bulk-import-jobs/{job_id}/_ 
  *resource*: get_bulk_profile_import_job  
  *description*: Get a bulk profile import job with the given job ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read` `profiles:read`
* _GET /api/profiles/{id}/_ 
  *resource*: get_profile  
  *description*: Get the profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `profiles:read`
* _GET /api/segments/{id}/_ 
  *resource*: get_segment  
  *description*: Get a segment with the given segment ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[segment]=profile_count` parameter in your API request:<br>Burst: `1/s`<br>Steady: `15/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `segments:read`
* _GET /api/tags/{id}/_ 
  *resource*: get_tag  
  *description*: Retrieve the tag with the given tag ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/images/_ 
  *resource*: get_images  
  *description*: Get all images in an account.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `images:read`
* _GET /api/images/{id}/_ 
  *resource*: get_image  
  *description*: Get the image with the given image ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `images:read`
* _GET /api/profile-bulk-import-jobs/{id}/import-errors/_ 
  *resource*: get_bulk_profile_import_job_import_errors  
  *description*: Get import errors for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `profiles:read`
* _GET /api/catalog-categories/{id}/relationships/items/_ 
  *resource*: get_catalog_category_relationships_items  
  *description*: Get all items in the given category ID.  Returns a maximum of 100 items per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
* _GET /api/profiles/{id}/relationships/lists/_ 
  *resource*: get_profile_relationships_lists  
  *description*: Get list memberships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `profiles:read`
* _GET /api/profile-bulk-import-jobs/{id}/relationships/lists/_ 
  *resource*: get_bulk_profile_import_job_relationships_lists  
  *description*: Get list relationship for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read`
* _GET /api/tags/{id}/relationships/lists/_ 
  *resource*: get_tag_relationships_lists  
  *description*: Returns the IDs of all lists associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `tags:read`
* _GET /api/lists/_ 
  *resource*: get_lists  
  *description*: Get all lists in an account.  Filter to request a subset of all lists. Lists can be filtered by `id`, `name`, `created`, and `updated` fields.  Returns a maximum of 10 results per page.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `lists:read`
* _GET /api/lists/{id}/profiles/_ 
  *resource*: get_list_profiles  
  *description*: Get all profiles within a list with the given list ID.  Filter to request a subset of all profiles. Profiles can be filtered by `email`, `phone_number`, `push_token`, and `joined_group_at` fields. Profiles can be sorted by the following fields, in ascending and descending order: `joined_group_at`<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[profile]=predictive_analytics` parameter in your API request:<br>Burst: `10/s`<br>Steady: `150/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `lists:read` `profiles:read`
* _GET /api/profiles/{id}/lists/_ 
  *resource*: get_profile_lists  
  *description*: Get list memberships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `profiles:read`
* _GET /api/profile-bulk-import-jobs/{id}/lists/_ 
  *resource*: get_bulk_profile_import_job_lists  
  *description*: Get list for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read`
* _GET /api/events/{id}/relationships/metric/_ 
  *resource*: get_event_relationships_metric  
  *description*: Get a list of related Metrics for an Event<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `metrics:read`
* _GET /api/events/{id}/metric/_ 
  *resource*: get_event_metric  
  *description*: Get the metric for an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `metrics:read`
* _GET /api/metrics/_ 
  *resource*: get_metrics  
  *description*: Get all metrics in an account.  Requests can be filtered by the following fields: integration `name`, integration `category`  Returns a maximum of 200 results per page.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `metrics:read`
* _GET /api/metrics/{id}/_ 
  *resource*: get_metric  
  *description*: Get a metric with the given metric ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `metrics:read`
* _GET /api/events/{id}/relationships/profile/_ 
  *resource*: get_event_relationships_profile  
  *description*: Get profile [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `profiles:read`
* _GET /api/lists/{id}/relationships/profiles/_ 
  *resource*: get_list_relationships_profiles  
  *description*: Get profile membership [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for a list with the given list ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `lists:read` `profiles:read`
* _GET /api/profile-bulk-import-jobs/{id}/relationships/profiles/_ 
  *resource*: get_bulk_profile_import_job_relationships_profiles  
  *description*: Get profile relationships for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `profiles:read`
* _GET /api/segments/{id}/relationships/profiles/_ 
  *resource*: get_segment_relationships_profiles  
  *description*: Get all profile membership [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for the given segment ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `profiles:read` `segments:read`
* _GET /api/profile-bulk-import-jobs/_ 
  *resource*: get_bulk_profile_import_jobs  
  *description*: Get all bulk profile import jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read` `profiles:read`
* _GET /api/events/{id}/profile/_ 
  *resource*: get_event_profile  
  *description*: Get the profile associated with an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `profiles:read`
* _GET /api/profiles/_ 
  *resource*: get_profiles  
  *description*: Get all profiles in an account.  Profiles can be sorted by the following fields in ascending and descending order: `id`, `created`, `updated`, `email`, `subscriptions.email.marketing.suppression.timestamp`, `subscriptions.email.marketing.list_suppressions.timestamp`<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[profile]=predictive_analytics` parameter in your API request:<br>Burst: `10/s`<br>Steady: `150/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `profiles:read`
* _GET /api/profile-bulk-import-jobs/{id}/profiles/_ 
  *resource*: get_bulk_profile_import_job_profiles  
  *description*: Get profiles for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `profiles:read`
* _GET /api/profiles/{id}/relationships/segments/_ 
  *resource*: get_profile_relationships_segments  
  *description*: Get segment membership relationships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `profiles:read` `segments:read`
* _GET /api/tags/{id}/relationships/segments/_ 
  *resource*: get_tag_relationships_segments  
  *description*: Returns the IDs of all segments associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `segments:read` `tags:read`
* _GET /api/segments/_ 
  *resource*: get_segments  
  *description*: Get all segments in an account.  Filter to request a subset of all segments. Segments can be filtered by `name`, `created`, and `updated` fields.  Returns a maximum of 10 results per page.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `segments:read`
* _GET /api/segments/{id}/profiles/_ 
  *resource*: get_segment_profiles  
  *description*: Get all profiles within a segment with the given segment ID.  Filter to request a subset of all profiles. Profiles can be filtered by `email`, `phone_number`, `push_token`, and `joined_group_at` fields. Profiles can be sorted by the following fields, in ascending and descending order: `joined_group_at`<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `profiles:read` `segments:read`
* _GET /api/profiles/{id}/segments/_ 
  *resource*: get_profile_segments  
  *description*: Get segment memberships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `profiles:read` `segments:read`
* _GET /api/campaigns/{id}/relationships/tags/_ 
  *resource*: get_campaign_relationships_tags  
  *description*: Returns the IDs of all tags associated with the given campaign.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `campaigns:read` `tags:read`
* _GET /api/flows/{id}/relationships/tags/_ 
  *resource*: get_flow_relationships_tags  
  *description*: Return the tag IDs of all tags associated with the given flow.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read` `tags:read`
* _GET /api/lists/{id}/relationships/tags/_ 
  *resource*: get_list_relationships_tags  
  *description*: Returns the tag IDs of all tags associated with the given list.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `tags:read`
* _GET /api/segments/{id}/relationships/tags/_ 
  *resource*: get_segment_relationships_tags  
  *description*: If `related_resource` is `tags`, returns the tag IDs of all tags associated with the given segment ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `segments:read` `tags:read`
* _GET /api/tag-groups/{id}/relationships/tags/_ 
  *resource*: get_tag_group_relationships_tags  
  *description*: Returns the tag IDs of all tags inside the given tag group.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/tags/{id}/relationships/tag-group/_ 
  *resource*: get_tag_relationships_tag_group  
  *description*: Returns the id of the tag group related to the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/tag-groups/_ 
  *resource*: get_tag_groups  
  *description*: List all tag groups in an account. Every account has one default tag group.  Tag groups can be filtered by `name`, `exclusive`, and `default`, and sorted by `name` or `id` in ascending or descending order.  Returns a maximum of 25 tag groups per request, which can be paginated with [cursor-based pagination](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#pagination).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/tag-groups/{id}/_ 
  *resource*: get_tag_group  
  *description*: Retrieve the tag group with the given tag group ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/tags/{id}/tag-group/_ 
  *resource*: get_tag_tag_group  
  *description*: Returns the tag group resource for a given tag ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/campaigns/{id}/tags/_ 
  *resource*: get_campaign_tags  
  *description*: Return all tags that belong to the given campaign.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `campaigns:read` `tags:read`
* _GET /api/flows/{id}/tags/_ 
  *resource*: get_flow_tags  
  *description*: Return all tags associated with the given flow ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read` `tags:read`
* _GET /api/lists/{id}/tags/_ 
  *resource*: get_list_tags  
  *description*: Return all tags associated with the given list ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `tags:read`
* _GET /api/segments/{id}/tags/_ 
  *resource*: get_segment_tags  
  *description*: Return all tags associated with the given segment ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `segments:read` `tags:read`
* _GET /api/tags/_ 
  *resource*: get_tags  
  *description*: List all tags in an account.  Tags can be filtered by `name`, and sorted by `name` or `id` in ascending or descending order.  Returns a maximum of 50 tags per request, which can be paginated with [cursor-based pagination](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#pagination).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/tag-groups/{id}/tags/_ 
  *resource*: get_tag_group_tags  
  *description*: Return the tags for a given tag group ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
* _GET /api/campaign-messages/{id}/relationships/template/_ 
  *resource*: get_campaign_message_relationships_template  
  *description*: Returns the ID of the related template<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read` `templates:read`
* _GET /api/flow-messages/{id}/relationships/template/_ 
  *resource*: get_flow_message_relationships_template  
  *description*: Returns the ID of the related template<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `templates:read`
* _GET /api/campaign-messages/{id}/template/_ 
  *resource*: get_campaign_message_template  
  *description*: Return the related template<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read` `templates:read`
* _GET /api/flow-messages/{id}/template/_ 
  *resource*: get_flow_message_template  
  *description*: Return the related template<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `templates:read`
* _GET /api/templates/_ 
  *resource*: get_templates  
  *description*: Get all templates in an account.  Filter to request a subset of all templates. Templates can be sorted by the following fields, in ascending and descending order: `id`, `name`, `created`, `updated`  Returns a maximum of 10 results per page.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `templates:read`
* _GET /api/templates/{id}/_ 
  *resource*: get_template  
  *description*: Get a template with the given template ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `templates:read`
