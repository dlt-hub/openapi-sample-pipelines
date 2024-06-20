# square_connect pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/square_connect.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /v2/loyalty/accounts/{account_id}_ 
  *resource*: retrieve_loyalty_account  
  *description*: Retrieves a loyalty account.
* _GET /v2/terminals/actions/{action_id}_ 
  *resource*: get_terminal_action  
  *description*: Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.
* _GET /v2/gift-cards/activities_ 
  *resource*: list_gift_card_activities  
  *description*: Lists gift card activities. By default, you get gift card activities for all gift cards in the seller's account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift card activities for a gift card, for all gift cards in a specific region, or for activities within a time window.
* _GET /v2/inventory/adjustment/{adjustment_id}_ 
  *resource*: deprecated_retrieve_inventory_adjustment  
  *description*: Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2024-04-17/inventory-api/retrieve-inventory-adjustment) after the endpoint URL is updated to conform to the standard convention.
* _GET /v2/inventory/adjustments/{adjustment_id}_ 
  *resource*: retrieve_inventory_adjustment  
  *description*: Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2024-04-17/objects/InventoryAdjustment) object with the provided `adjustment_id`.
* _GET /v2/bank-accounts_ 
  *resource*: list_bank_accounts  
  *description*: Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2024-04-17/objects/BankAccount) objects linked to a Square account.
* _GET /v2/bank-accounts/{bank_account_id}_ 
  *resource*: get_bank_account  
  *description*: Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2024-04-17/objects/BankAccount) linked to a Square account.
* _GET /v2/bookings_ 
  *resource*: list_bookings  
  *description*: Retrieve a collection of bookings.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
* _GET /v2/bookings/{booking_id}_ 
  *resource*: retrieve_booking  
  *description*: Retrieves a booking.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
* _GET /v2/labor/break-types_ 
  *resource*: list_break_types  
  *description*: Returns a paginated list of `BreakType` instances for a business.
* _GET /v2/labor/break-types/{id}_ 
  *resource*: get_break_type  
  *description*: Returns a single `BreakType` specified by `id`.
* _GET /v2/bookings/business-booking-profile_ 
  *resource*: retrieve_business_booking_profile  
  *description*: Retrieves a seller's booking profile.
* _GET /v2/bank-accounts/by-v1-id/{v1_bank_account_id}_ 
  *resource*: get_bank_account_by_v1_id  
  *description*: Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2024-04-17/objects/BankAccount) identified by V1 bank account ID.
* _GET /v2/cards_ 
  *resource*: list_cards  
  *description*: Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.
* _GET /v2/cards/{card_id}_ 
  *resource*: retrieve_card  
  *description*: Retrieves details for a specific Card.
* _GET /v2/inventory/{catalog_object_id}/changes_ 
  *resource*: retrieve_inventory_changes  
  *description*: Returns a set of physical counts and inventory adjustments for the provided [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject) at the requested [Location](https://developer.squareup.com/reference/square_2024-04-17/objects/Location)s.  You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2024-04-17/inventory-api/batch-retrieve-inventory-changes) and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.  Results are paginated and sorted in descending order according to their `occurred_at` timestamp (newest first).  There are no limits on how far back the caller can page. This endpoint can be used to display recent changes for a specific item. For more sophisticated queries, use a batch endpoint.
* _GET /v2/terminals/checkouts/{checkout_id}_ 
  *resource*: get_terminal_checkout  
  *description*: Retrieves a Terminal checkout request by `checkout_id`. Terminal checkout requests are available for 30 days.
* _GET /v2/devices/codes_ 
  *resource*: list_device_codes  
  *description*: Lists all DeviceCodes associated with the merchant.
* _GET /v2/devices/codes/{id}_ 
  *resource*: get_device_code  
  *description*: Retrieves DeviceCode with the associated ID.
* _GET /v2/bookings/{booking_id}/custom-attributes_ 
  *resource*: list_booking_custom_attributes  
  *description*: Lists a booking's custom attributes.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
* _GET /v2/bookings/{booking_id}/custom-attributes/{key}_ 
  *resource*: retrieve_booking_custom_attribute  
  *description*: Retrieves a bookings custom attribute.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
* _GET /v2/customers/{customer_id}/custom-attributes_ 
  *resource*: list_customer_custom_attributes  
  *description*: Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a customer profile.  You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call.  When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/customers/{customer_id}/custom-attributes/{key}_ 
  *resource*: retrieve_customer_custom_attribute  
  *description*: Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a customer profile.  You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call.  To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/locations/{location_id}/custom-attributes_ 
  *resource*: list_location_custom_attributes  
  *description*: Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a location. You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call. When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/locations/{location_id}/custom-attributes/{key}_ 
  *resource*: retrieve_location_custom_attribute  
  *description*: Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a location. You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call. To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/merchants/{merchant_id}/custom-attributes_ 
  *resource*: list_merchant_custom_attributes  
  *description*: Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a merchant. You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call. When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/merchants/{merchant_id}/custom-attributes/{key}_ 
  *resource*: retrieve_merchant_custom_attribute  
  *description*: Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a merchant. You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call. To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/orders/{order_id}/custom-attributes_ 
  *resource*: list_order_custom_attributes  
  *description*: Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with an order.  You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call.  When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}_ 
  *resource*: retrieve_order_custom_attribute  
  *description*: Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with an order.  You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call.  To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/bookings/custom-attribute-definitions_ 
  *resource*: list_booking_custom_attribute_definitions  
  *description*: Get all bookings custom attribute definitions.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
* _GET /v2/bookings/custom-attribute-definitions/{key}_ 
  *resource*: retrieve_booking_custom_attribute_definition  
  *description*: Retrieves a bookings custom attribute definition.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
* _GET /v2/customers/custom-attribute-definitions_ 
  *resource*: list_customer_custom_attribute_definitions  
  *description*: Lists the customer-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account.  When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/customers/custom-attribute-definitions/{key}_ 
  *resource*: retrieve_customer_custom_attribute_definition  
  *description*: Retrieves a customer-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account.  To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/locations/custom-attribute-definitions_ 
  *resource*: list_location_custom_attribute_definitions  
  *description*: Lists the location-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account. When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/locations/custom-attribute-definitions/{key}_ 
  *resource*: retrieve_location_custom_attribute_definition  
  *description*: Retrieves a location-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account. To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/merchants/custom-attribute-definitions_ 
  *resource*: list_merchant_custom_attribute_definitions  
  *description*: Lists the merchant-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account. When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/merchants/custom-attribute-definitions/{key}_ 
  *resource*: retrieve_merchant_custom_attribute_definition  
  *description*: Retrieves a merchant-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account. To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/orders/custom-attribute-definitions_ 
  *resource*: list_order_custom_attribute_definitions  
  *description*: Lists the order-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account.  When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/orders/custom-attribute-definitions/{key}_ 
  *resource*: retrieve_order_custom_attribute_definition  
  *description*: Retrieves an order-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account.  To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
* _GET /v2/customers_ 
  *resource*: list_customers  
  *description*: Lists customer profiles associated with a Square account.  Under normal operating conditions, newly created or updated customer profiles become available for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to one minute or longer, especially during network incidents and outages.
* _GET /v2/customers/{customer_id}_ 
  *resource*: retrieve_customer  
  *description*: Returns details for a single customer.
* _GET /v2/devices_ 
  *resource*: list_devices  
  *description*: List devices associated with the merchant. Currently, only Terminal API devices are supported.
* _GET /v2/devices/{device_id}_ 
  *resource*: get_device  
  *description*: Retrieves Device with the associated `device_id`.
* _GET /v2/disputes_ 
  *resource*: list_disputes  
  *description*: Returns a list of disputes associated with a particular account.
* _GET /v2/disputes/{dispute_id}_ 
  *resource*: retrieve_dispute  
  *description*: Returns details about a specific dispute.
* _GET /v2/employees_ 
  *resource*: list_employees  
* _GET /v2/employees/{id}_ 
  *resource*: retrieve_employee  
* _GET /v2/labor/employee-wages_ 
  *resource*: list_employee_wages  
  *description*: Returns a paginated list of `EmployeeWage` instances for a business.
* _GET /v2/labor/employee-wages/{id}_ 
  *resource*: get_employee_wage  
  *description*: Returns a single `EmployeeWage` specified by `id`.
* _GET /v2/cash-drawers/shifts/{shift_id}/events_ 
  *resource*: list_cash_drawer_shift_events  
  *description*: Provides a paginated list of events for a single cash drawer shift.
* _GET /v2/subscriptions/{subscription_id}/events_ 
  *resource*: list_subscription_events  
  *description*: Lists all [events](https://developer.squareup.com/docs/subscriptions-api/actions-events) for a specific subscription.
* _GET /v2/webhooks/event-types_ 
  *resource*: list_webhook_event_types  
  *description*: Lists all webhook event types that can be subscribed to.
* _GET /v2/disputes/{dispute_id}/evidence_ 
  *resource*: list_dispute_evidence  
  *description*: Returns a list of evidence associated with a dispute.
* _GET /v2/disputes/{dispute_id}/evidence/{evidence_id}_ 
  *resource*: retrieve_dispute_evidence  
  *description*: Returns the metadata for the evidence specified in the request URL path.  You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be downloaded after you upload it.
* _GET /v2/gift-cards_ 
  *resource*: list_gift_cards  
  *description*: Lists all gift cards. You can specify optional filters to retrieve  a subset of the gift cards. Results are sorted by `created_at` in ascending order.
* _GET /v2/gift-cards/{id}_ 
  *resource*: retrieve_gift_card  
  *description*: Retrieves a gift card using the gift card ID.
* _GET /v2/customers/groups_ 
  *resource*: list_customer_groups  
  *description*: Retrieves the list of customer groups of a business.
* _GET /v2/customers/groups/{group_id}_ 
  *resource*: retrieve_customer_group  
  *description*: Retrieves a specific customer group as identified by the `group_id` value.
* _GET /v2/catalog/info_ 
  *resource*: catalog_info  
  *description*: Retrieves information about the Square Catalog API, such as batch size limits that can be used by the `BatchUpsertCatalogObjects` endpoint.
* _GET /v2/inventory/{catalog_object_id}_ 
  *resource*: retrieve_inventory_count  
  *description*: Retrieves the current calculated stock count for a given [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject) at a given set of [Location](https://developer.squareup.com/reference/square_2024-04-17/objects/Location)s. Responses are paginated and unsorted. For more sophisticated queries, use a batch endpoint.
* _GET /v2/invoices_ 
  *resource*: list_invoices  
  *description*: Returns a list of invoices for a given location. The response  is paginated. If truncated, the response includes a `cursor` that you     use in a subsequent request to retrieve the next set of invoices.
* _GET /v2/invoices/{invoice_id}_ 
  *resource*: get_invoice  
  *description*: Retrieves an invoice by invoice ID.
* _GET /v2/catalog/list_ 
  *resource*: list_catalog  
  *description*: Returns a list of all [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject)s of the specified types in the catalog.   The `types` parameter is specified as a comma-separated list of the [CatalogObjectType](https://developer.squareup.com/reference/square_2024-04-17/enums/CatalogObjectType) values,  for example, "`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`".  __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2024-04-17/catalog-api/search-catalog-objects) and set the `include_deleted_objects` attribute value to `true`.
* _GET /v2/locations_ 
  *resource*: list_locations  
  *description*: Provides details about all of the seller's [locations](https://developer.squareup.com/docs/locations-api), including those with an inactive status. Locations are listed alphabetically by `name`.
* _GET /v2/locations/{location_id}_ 
  *resource*: retrieve_location  
  *description*: Retrieves details of a single location. Specify "main" as the location ID to retrieve details of the [main location](https://developer.squareup.com/docs/locations-api#about-the-main-location).
* _GET /v2/bookings/location-booking-profiles_ 
  *resource*: list_location_booking_profiles  
  *description*: Lists location booking profiles of a seller.
* _GET /v2/bookings/location-booking-profiles/{location_id}_ 
  *resource*: retrieve_location_booking_profile  
  *description*: Retrieves a seller's location booking profile.
* _GET /v2/online-checkout/location-settings/{location_id}_ 
  *resource*: retrieve_location_settings  
  *description*: Retrieves the location-level settings for a Square-hosted checkout page.
* _GET /v2/merchants_ 
  *resource*: list_merchants  
  *description*: Provides details about the merchant associated with a given access token.  The access token used to connect your application to a Square seller is associated with a single merchant. That means that `ListMerchants` returns a list with a single `Merchant` object. You can specify your personal access token to get your own merchant information or specify an OAuth token to get the information for the merchant that granted your application access.  If you know the merchant ID, you can also use the [RetrieveMerchant](https://developer.squareup.com/reference/square_2024-04-17/merchants-api/retrieve-merchant) endpoint to retrieve the merchant information.
* _GET /v2/merchants/{merchant_id}_ 
  *resource*: retrieve_merchant  
  *description*: Retrieves the `Merchant` object for the given `merchant_id`.
* _GET /v2/online-checkout/merchant-settings_ 
  *resource*: retrieve_merchant_settings  
  *description*: Retrieves the merchant-level settings for a Square-hosted checkout page.
* _GET /v2/catalog/object/{object_id}_ 
  *resource*: retrieve_catalog_object  
  *description*: Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogItem) as a [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject) based on the provided ID. The returned object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogItem) information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogItemVariation) children, references to its [CatalogModifierList](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogModifierList) objects, and the ids of any [CatalogTax](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogTax) objects that apply to it.
* _GET /v1/{location_id}/orders_ 
  *resource*: v1_list_orders  
  *description*: Provides summary information for a merchant's online store orders.
* _GET /v1/{location_id}/orders/{order_id}_ 
  *resource*: v1_retrieve_order  
  *description*: Provides comprehensive information for a single online store order, including the order's history.
* _GET /v2/orders/{order_id}_ 
  *resource*: retrieve_order  
  *description*: Retrieves an [Order](https://developer.squareup.com/reference/square_2024-04-17/objects/Order) by ID.
* _GET /v2/payments_ 
  *resource*: list_payments  
  *description*: Retrieves a list of payments taken by the account making the request.  Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.  The maximum results per page is 100.
* _GET /v2/payments/{payment_id}_ 
  *resource*: get_payment  
  *description*: Retrieves details for a specific payment.
* _GET /v2/online-checkout/payment-links_ 
  *resource*: list_payment_links  
  *description*: Lists all payment links.
* _GET /v2/online-checkout/payment-links/{id}_ 
  *resource*: retrieve_payment_link  
  *description*: Retrieves a payment link.
* _GET /v2/payouts_ 
  *resource*: list_payouts  
  *description*: Retrieves a list of all payouts for the default location. You can filter payouts by location ID, status, time range, and order them in ascending or descending order. To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
* _GET /v2/payouts/{payout_id}_ 
  *resource*: get_payout  
  *description*: Retrieves details of a specific payout identified by a payout ID. To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
* _GET /v2/payouts/{payout_id}/payout-entries_ 
  *resource*: list_payout_entries  
  *description*: Retrieves a list of all payout entries for a specific payout. To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
* _GET /v2/inventory/physical-count/{physical_count_id}_ 
  *resource*: deprecated_retrieve_inventory_physical_count  
  *description*: Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2024-04-17/inventory-api/retrieve-inventory-physical-count) after the endpoint URL is updated to conform to the standard convention.
* _GET /v2/inventory/physical-counts/{physical_count_id}_ 
  *resource*: retrieve_inventory_physical_count  
  *description*: Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2024-04-17/objects/InventoryPhysicalCount) object with the provided `physical_count_id`.
* _GET /v2/loyalty/programs_ 
  *resource*: list_loyalty_programs  
  *description*: Returns a list of loyalty programs in the seller's account. Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).   Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2024-04-17/loyalty-api/retrieve-loyalty-program) when used with the keyword `main`.
* _GET /v2/loyalty/programs/{program_id}_ 
  *resource*: retrieve_loyalty_program  
  *description*: Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.  Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).
* _GET /v2/loyalty/programs/{program_id}/promotions_ 
  *resource*: list_loyalty_promotions  
  *description*: Lists the loyalty promotions associated with a [loyalty program](https://developer.squareup.com/reference/square_2024-04-17/objects/LoyaltyProgram). Results are sorted by the `created_at` date in descending order (newest to oldest).
* _GET /v2/loyalty/programs/{program_id}/promotions/{promotion_id}_ 
  *resource*: retrieve_loyalty_promotion  
  *description*: Retrieves a loyalty promotion.
* _GET /v2/refunds_ 
  *resource*: list_payment_refunds  
  *description*: Retrieves a list of refunds for the account making the request.  Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.  The maximum results per page is 100.
* _GET /v2/refunds/{refund_id}_ 
  *resource*: get_payment_refund  
  *description*: Retrieves a specific refund using the `refund_id`.
* _GET /v2/terminals/refunds/{terminal_refund_id}_ 
  *resource*: get_terminal_refund  
  *description*: Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.
* _GET /v2/loyalty/rewards/{reward_id}_ 
  *resource*: retrieve_loyalty_reward  
  *description*: Retrieves a loyalty reward.
* _GET /v2/customers/segments_ 
  *resource*: list_customer_segments  
  *description*: Retrieves the list of customer segments of a business.
* _GET /v2/customers/segments/{segment_id}_ 
  *resource*: retrieve_customer_segment  
  *description*: Retrieves a specific customer segment as identified by the `segment_id` value.
* _GET /v2/cash-drawers/shifts_ 
  *resource*: list_cash_drawer_shifts  
  *description*: Provides the details for all of the cash drawer shifts for a location in a date range.
* _GET /v2/cash-drawers/shifts/{shift_id}_ 
  *resource*: retrieve_cash_drawer_shift  
  *description*: Provides the summary details for a single cash drawer shift. See [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2024-04-17/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.
* _GET /v2/labor/shifts/{id}_ 
  *resource*: get_shift  
  *description*: Returns a single `Shift` specified by `id`.
* _GET /v2/sites_ 
  *resource*: list_sites  
  *description*: Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the `created_at` date.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
* _GET /v2/sites/{site_id}/snippet_ 
  *resource*: retrieve_snippet  
  *description*: Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.  You can call [ListSites](https://developer.squareup.com/reference/square_2024-04-17/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
* _GET /v2/subscriptions/{subscription_id}_ 
  *resource*: retrieve_subscription  
  *description*: Retrieves a specific subscription.
* _GET /v2/webhooks/subscriptions_ 
  *resource*: list_webhook_subscriptions  
  *description*: Lists all webhook subscriptions owned by your application.
* _GET /v2/webhooks/subscriptions/{subscription_id}_ 
  *resource*: retrieve_webhook_subscription  
  *description*: Retrieves a webhook subscription identified by its ID.
* _GET /v2/team-members/{team_member_id}_ 
  *resource*: retrieve_team_member  
  *description*: Retrieves a `TeamMember` object for the given `TeamMember.id`. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).
* _GET /v2/bookings/team-member-booking-profiles_ 
  *resource*: list_team_member_booking_profiles  
  *description*: Lists booking profiles for team members.
* _GET /v2/bookings/team-member-booking-profiles/{team_member_id}_ 
  *resource*: retrieve_team_member_booking_profile  
  *description*: Retrieves a team member's booking profile.
* _GET /v2/labor/team-member-wages_ 
  *resource*: list_team_member_wages  
  *description*: Returns a paginated list of `TeamMemberWage` instances for a business.
* _GET /v2/labor/team-member-wages/{id}_ 
  *resource*: get_team_member_wage  
  *description*: Returns a single `TeamMemberWage` specified by `id`.
* _GET /v2/locations/{location_id}/transactions_ 
  *resource*: list_transactions  
  *description*: Lists transactions for a particular location.  Transactions include payment information from sales and exchanges and refund information from returns and exchanges.  Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50
* _GET /v2/locations/{location_id}/transactions/{transaction_id}_ 
  *resource*: retrieve_transaction  
  *description*: Retrieves details for a single transaction.
* _GET /v2/inventory/transfers/{transfer_id}_ 
  *resource*: retrieve_inventory_transfer  
  *description*: Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2024-04-17/objects/InventoryTransfer) object with the provided `transfer_id`.
* _GET /v2/vendors/{vendor_id}_ 
  *resource*: retrieve_vendor  
  *description*: Retrieves the vendor of a specified [Vendor](https://developer.squareup.com/reference/square_2024-04-17/objects/Vendor) ID.
* _GET /v2/team-members/{team_member_id}/wage-setting_ 
  *resource*: retrieve_wage_setting  
  *description*: Retrieves a `WageSetting` object for a team member specified by `TeamMember.id`. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).
* _GET /v2/labor/workweek-configs_ 
  *resource*: list_workweek_configs  
  *description*: Returns a list of `WorkweekConfig` instances for a business.
