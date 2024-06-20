from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="square_connect_source", max_table_nesting=2)
def square_connect_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Retrieves a loyalty account.
            {
                "name": "retrieve_loyalty_account",
                "table_name": "account",
                "endpoint": {
                    "path": "/v2/loyalty/accounts/{account_id}",
                    "params": {
                        "account_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.
            {
                "name": "get_terminal_action",
                "table_name": "action",
                "endpoint": {
                    "path": "/v2/terminals/actions/{action_id}",
                    "params": {
                        "action_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists gift card activities. By default, you get gift card activities for all gift cards in the seller's account. You can optionally specify query parameters to filter the list. For example, you can get a list of gift card activities for a gift card, for all gift cards in a specific region, or for activities within a time window.
            {
                "name": "list_gift_card_activities",
                "table_name": "activity",
                "endpoint": {
                    "path": "/v2/gift-cards/activities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "gift_card_id": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                        # "begin_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2024-04-17/inventory-api/retrieve-inventory-adjustment) after the endpoint URL is updated to conform to the standard convention.
            {
                "name": "deprecated_retrieve_inventory_adjustment",
                "table_name": "adjustment",
                "endpoint": {
                    "path": "/v2/inventory/adjustment/{adjustment_id}",
                    "params": {
                        "adjustment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2024-04-17/objects/InventoryAdjustment) object with the provided `adjustment_id`.
            {
                "name": "retrieve_inventory_adjustment",
                "table_name": "adjustment",
                "endpoint": {
                    "path": "/v2/inventory/adjustments/{adjustment_id}",
                    "params": {
                        "adjustment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of [BankAccount](https://developer.squareup.com/reference/square_2024-04-17/objects/BankAccount) objects linked to a Square account.
            {
                "name": "list_bank_accounts",
                "table_name": "bank_account",
                "endpoint": {
                    "path": "/v2/bank-accounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2024-04-17/objects/BankAccount) linked to a Square account.
            {
                "name": "get_bank_account",
                "table_name": "bank_account",
                "endpoint": {
                    "path": "/v2/bank-accounts/{bank_account_id}",
                    "params": {
                        "bank_account_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a collection of bookings.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
            {
                "name": "list_bookings",
                "table_name": "booking",
                "endpoint": {
                    "path": "/v2/bookings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "customer_id": "OPTIONAL_CONFIG",
                        # "team_member_id": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                        # "start_at_min": "OPTIONAL_CONFIG",
                        # "start_at_max": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a booking.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
            {
                "name": "retrieve_booking",
                "table_name": "booking",
                "endpoint": {
                    "path": "/v2/bookings/{booking_id}",
                    "params": {
                        "booking_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a paginated list of `BreakType` instances for a business.
            {
                "name": "list_break_types",
                "table_name": "break_type",
                "endpoint": {
                    "path": "/v2/labor/break-types",
                    "params": {
                        # the parameters below can optionally be configured
                        # "location_id": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single `BreakType` specified by `id`.
            {
                "name": "get_break_type",
                "table_name": "break_type",
                "endpoint": {
                    "path": "/v2/labor/break-types/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a seller's booking profile.
            {
                "name": "retrieve_business_booking_profile",
                "table_name": "business_booking_profile",
                "endpoint": {
                    "path": "/v2/bookings/business-booking-profile",
                    "paginator": "auto",
                },
            },
            # Returns details of a [BankAccount](https://developer.squareup.com/reference/square_2024-04-17/objects/BankAccount) identified by V1 bank account ID.
            {
                "name": "get_bank_account_by_v1_id",
                "table_name": "by_v1_id",
                "endpoint": {
                    "path": "/v2/bank-accounts/by-v1-id/{v1_bank_account_id}",
                    "params": {
                        "v1_bank_account_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.
            {
                "name": "list_cards",
                "table_name": "card",
                "endpoint": {
                    "path": "/v2/cards",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "customer_id": "OPTIONAL_CONFIG",
                        # "include_disabled": "OPTIONAL_CONFIG",
                        # "reference_id": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details for a specific Card.
            {
                "name": "retrieve_card",
                "table_name": "card",
                "endpoint": {
                    "path": "/v2/cards/{card_id}",
                    "params": {
                        "card_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a set of physical counts and inventory adjustments for the provided [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject) at the requested [Location](https://developer.squareup.com/reference/square_2024-04-17/objects/Location)s.  You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2024-04-17/inventory-api/batch-retrieve-inventory-changes) and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.  Results are paginated and sorted in descending order according to their `occurred_at` timestamp (newest first).  There are no limits on how far back the caller can page. This endpoint can be used to display recent changes for a specific item. For more sophisticated queries, use a batch endpoint.
            {
                "name": "retrieve_inventory_changes",
                "table_name": "change",
                "endpoint": {
                    "path": "/v2/inventory/{catalog_object_id}/changes",
                    "params": {
                        "catalog_object_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "location_ids": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a Terminal checkout request by `checkout_id`. Terminal checkout requests are available for 30 days.
            {
                "name": "get_terminal_checkout",
                "table_name": "checkout",
                "endpoint": {
                    "path": "/v2/terminals/checkouts/{checkout_id}",
                    "params": {
                        "checkout_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists all DeviceCodes associated with the merchant.
            {
                "name": "list_device_codes",
                "table_name": "code",
                "endpoint": {
                    "path": "/v2/devices/codes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                        # "product_type": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves DeviceCode with the associated ID.
            {
                "name": "get_device_code",
                "table_name": "code",
                "endpoint": {
                    "path": "/v2/devices/codes/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists a booking's custom attributes.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
            {
                "name": "list_booking_custom_attributes",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/bookings/{booking_id}/custom-attributes",
                    "params": {
                        "booking_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "with_definitions": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a bookings custom attribute.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
            {
                "name": "retrieve_booking_custom_attribute",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/bookings/{booking_id}/custom-attributes/{key}",
                    "params": {
                        "booking_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "with_definition": "OPTIONAL_CONFIG",
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a customer profile.  You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call.  When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_customer_custom_attributes",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/customers/{customer_id}/custom-attributes",
                    "params": {
                        "customer_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "with_definitions": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a customer profile.  You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call.  To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_customer_custom_attribute",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/customers/{customer_id}/custom-attributes/{key}",
                    "params": {
                        "customer_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "with_definition": "OPTIONAL_CONFIG",
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a location. You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call. When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_location_custom_attributes",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/locations/{location_id}/custom-attributes",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "visibility_filter": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "with_definitions": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a location. You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call. To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_location_custom_attribute",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/locations/{location_id}/custom-attributes/{key}",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "with_definition": "OPTIONAL_CONFIG",
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a merchant. You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call. When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_merchant_custom_attributes",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/merchants/{merchant_id}/custom-attributes",
                    "params": {
                        "merchant_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "visibility_filter": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "with_definitions": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with a merchant. You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call. To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_merchant_custom_attribute",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/merchants/{merchant_id}/custom-attributes/{key}",
                    "params": {
                        "merchant_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "with_definition": "OPTIONAL_CONFIG",
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the [custom attributes](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with an order.  You can use the `with_definitions` query parameter to also retrieve custom attribute definitions in the same call.  When all response pages are retrieved, the results include all custom attributes that are visible to the requesting application, including those that are owned by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_order_custom_attributes",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/orders/{order_id}/custom-attributes",
                    "params": {
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "visibility_filter": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "with_definitions": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a [custom attribute](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttribute) associated with an order.  You can use the `with_definition` query parameter to also retrieve the custom attribute definition in the same call.  To retrieve a custom attribute owned by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_order_custom_attribute",
                "table_name": "custom_attribute",
                "endpoint": {
                    "path": "/v2/orders/{order_id}/custom-attributes/{custom_attribute_key}",
                    "params": {
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "custom_attribute_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                        # "with_definition": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all bookings custom attribute definitions.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
            {
                "name": "list_booking_custom_attribute_definitions",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/bookings/custom-attribute-definitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a bookings custom attribute definition.  To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope. To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.
            {
                "name": "retrieve_booking_custom_attribute_definition",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/bookings/custom-attribute-definitions/{key}",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the customer-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account.  When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_customer_custom_attribute_definitions",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/customers/custom-attribute-definitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a customer-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account.  To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_customer_custom_attribute_definition",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/customers/custom-attribute-definitions/{key}",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the location-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account. When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_location_custom_attribute_definitions",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/locations/custom-attribute-definitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "visibility_filter": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a location-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account. To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_location_custom_attribute_definition",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/locations/custom-attribute-definitions/{key}",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the merchant-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account. When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_merchant_custom_attribute_definitions",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/merchants/custom-attribute-definitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "visibility_filter": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a merchant-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account. To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_merchant_custom_attribute_definition",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/merchants/custom-attribute-definitions/{key}",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the order-related [custom attribute definitions](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) that belong to a Square seller account.  When all response pages are retrieved, the results include all custom attribute definitions that are visible to the requesting application, including those that are created by other applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "list_order_custom_attribute_definitions",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/orders/custom-attribute-definitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "visibility_filter": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves an order-related [custom attribute definition](https://developer.squareup.com/reference/square_2024-04-17/objects/CustomAttributeDefinition) from a Square seller account.  To retrieve a custom attribute definition created by another application, the `visibility` setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.
            {
                "name": "retrieve_order_custom_attribute_definition",
                "table_name": "custom_attribute_definition",
                "endpoint": {
                    "path": "/v2/orders/custom-attribute-definitions/{key}",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists customer profiles associated with a Square account.  Under normal operating conditions, newly created or updated customer profiles become available for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to one minute or longer, especially during network incidents and outages.
            {
                "name": "list_customers",
                "table_name": "customer",
                "endpoint": {
                    "path": "/v2/customers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "sort_field": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns details for a single customer.
            {
                "name": "retrieve_customer",
                "table_name": "customer",
                "endpoint": {
                    "path": "/v2/customers/{customer_id}",
                    "params": {
                        "customer_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List devices associated with the merchant. Currently, only Terminal API devices are supported.
            {
                "name": "list_devices",
                "table_name": "device",
                "endpoint": {
                    "path": "/v2/devices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves Device with the associated `device_id`.
            {
                "name": "get_device",
                "table_name": "device",
                "endpoint": {
                    "path": "/v2/devices/{device_id}",
                    "params": {
                        "device_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of disputes associated with a particular account.
            {
                "name": "list_disputes",
                "table_name": "dispute",
                "endpoint": {
                    "path": "/v2/disputes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "states": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns details about a specific dispute.
            {
                "name": "retrieve_dispute",
                "table_name": "dispute",
                "endpoint": {
                    "path": "/v2/disputes/{dispute_id}",
                    "params": {
                        "dispute_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "list_employees",
                "table_name": "employee",
                "endpoint": {
                    "path": "/v2/employees",
                    "params": {
                        # the parameters below can optionally be configured
                        # "location_id": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "retrieve_employee",
                "table_name": "employee",
                "endpoint": {
                    "path": "/v2/employees/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a paginated list of `EmployeeWage` instances for a business.
            {
                "name": "list_employee_wages",
                "table_name": "employee_wage",
                "endpoint": {
                    "path": "/v2/labor/employee-wages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "employee_id": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single `EmployeeWage` specified by `id`.
            {
                "name": "get_employee_wage",
                "table_name": "employee_wage",
                "endpoint": {
                    "path": "/v2/labor/employee-wages/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Provides a paginated list of events for a single cash drawer shift.
            {
                "name": "list_cash_drawer_shift_events",
                "table_name": "event",
                "endpoint": {
                    "path": "/v2/cash-drawers/shifts/{shift_id}/events",
                    "params": {
                        "shift_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "location_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all [events](https://developer.squareup.com/docs/subscriptions-api/actions-events) for a specific subscription.
            {
                "name": "list_subscription_events",
                "table_name": "event",
                "endpoint": {
                    "path": "/v2/subscriptions/{subscription_id}/events",
                    "params": {
                        "subscription_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all webhook event types that can be subscribed to.
            {
                "name": "list_webhook_event_types",
                "table_name": "event_type",
                "endpoint": {
                    "path": "/v2/webhooks/event-types",
                    "params": {
                        # the parameters below can optionally be configured
                        # "api_version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of evidence associated with a dispute.
            {
                "name": "list_dispute_evidence",
                "table_name": "evidence",
                "endpoint": {
                    "path": "/v2/disputes/{dispute_id}/evidence",
                    "params": {
                        "dispute_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metadata for the evidence specified in the request URL path.  You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be downloaded after you upload it.
            {
                "name": "retrieve_dispute_evidence",
                "table_name": "evidence",
                "endpoint": {
                    "path": "/v2/disputes/{dispute_id}/evidence/{evidence_id}",
                    "params": {
                        "dispute_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "evidence_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists all gift cards. You can specify optional filters to retrieve  a subset of the gift cards. Results are sorted by `created_at` in ascending order.
            {
                "name": "list_gift_cards",
                "table_name": "gift_card",
                "endpoint": {
                    "path": "/v2/gift-cards",
                    "params": {
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "state": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "customer_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a gift card using the gift card ID.
            {
                "name": "retrieve_gift_card",
                "table_name": "gift_card",
                "endpoint": {
                    "path": "/v2/gift-cards/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the list of customer groups of a business.
            {
                "name": "list_customer_groups",
                "table_name": "group",
                "endpoint": {
                    "path": "/v2/customers/groups",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a specific customer group as identified by the `group_id` value.
            {
                "name": "retrieve_customer_group",
                "table_name": "group",
                "endpoint": {
                    "path": "/v2/customers/groups/{group_id}",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves information about the Square Catalog API, such as batch size limits that can be used by the `BatchUpsertCatalogObjects` endpoint.
            {
                "name": "catalog_info",
                "table_name": "info",
                "endpoint": {
                    "path": "/v2/catalog/info",
                    "paginator": "auto",
                },
            },
            # Retrieves the current calculated stock count for a given [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject) at a given set of [Location](https://developer.squareup.com/reference/square_2024-04-17/objects/Location)s. Responses are paginated and unsorted. For more sophisticated queries, use a batch endpoint.
            {
                "name": "retrieve_inventory_count",
                "table_name": "inventory",
                "endpoint": {
                    "path": "/v2/inventory/{catalog_object_id}",
                    "params": {
                        "catalog_object_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "location_ids": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of invoices for a given location. The response  is paginated. If truncated, the response includes a `cursor` that you     use in a subsequent request to retrieve the next set of invoices.
            {
                "name": "list_invoices",
                "table_name": "invoice",
                "endpoint": {
                    "path": "/v2/invoices",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves an invoice by invoice ID.
            {
                "name": "get_invoice",
                "table_name": "invoice",
                "endpoint": {
                    "path": "/v2/invoices/{invoice_id}",
                    "params": {
                        "invoice_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject)s of the specified types in the catalog.   The `types` parameter is specified as a comma-separated list of the [CatalogObjectType](https://developer.squareup.com/reference/square_2024-04-17/enums/CatalogObjectType) values,  for example, "`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`".  __Important:__ ListCatalog does not return deleted catalog items. To retrieve deleted catalog items, use [SearchCatalogObjects](https://developer.squareup.com/reference/square_2024-04-17/catalog-api/search-catalog-objects) and set the `include_deleted_objects` attribute value to `true`.
            {
                "name": "list_catalog",
                "table_name": "list",
                "endpoint": {
                    "path": "/v2/catalog/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "types": "OPTIONAL_CONFIG",
                        # "catalog_version": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Provides details about all of the seller's [locations](https://developer.squareup.com/docs/locations-api), including those with an inactive status. Locations are listed alphabetically by `name`.
            {
                "name": "list_locations",
                "table_name": "location",
                "endpoint": {
                    "path": "/v2/locations",
                    "paginator": "auto",
                },
            },
            # Retrieves details of a single location. Specify "main" as the location ID to retrieve details of the [main location](https://developer.squareup.com/docs/locations-api#about-the-main-location).
            {
                "name": "retrieve_location",
                "table_name": "location",
                "endpoint": {
                    "path": "/v2/locations/{location_id}",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists location booking profiles of a seller.
            {
                "name": "list_location_booking_profiles",
                "table_name": "location_booking_profile",
                "endpoint": {
                    "path": "/v2/bookings/location-booking-profiles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a seller's location booking profile.
            {
                "name": "retrieve_location_booking_profile",
                "table_name": "location_booking_profile",
                "endpoint": {
                    "path": "/v2/bookings/location-booking-profiles/{location_id}",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the location-level settings for a Square-hosted checkout page.
            {
                "name": "retrieve_location_settings",
                "table_name": "location_setting",
                "endpoint": {
                    "path": "/v2/online-checkout/location-settings/{location_id}",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Provides details about the merchant associated with a given access token.  The access token used to connect your application to a Square seller is associated with a single merchant. That means that `ListMerchants` returns a list with a single `Merchant` object. You can specify your personal access token to get your own merchant information or specify an OAuth token to get the information for the merchant that granted your application access.  If you know the merchant ID, you can also use the [RetrieveMerchant](https://developer.squareup.com/reference/square_2024-04-17/merchants-api/retrieve-merchant) endpoint to retrieve the merchant information.
            {
                "name": "list_merchants",
                "table_name": "merchant",
                "endpoint": {
                    "path": "/v2/merchants",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the `Merchant` object for the given `merchant_id`.
            {
                "name": "retrieve_merchant",
                "table_name": "merchant",
                "endpoint": {
                    "path": "/v2/merchants/{merchant_id}",
                    "params": {
                        "merchant_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the merchant-level settings for a Square-hosted checkout page.
            {
                "name": "retrieve_merchant_settings",
                "table_name": "merchant_setting",
                "endpoint": {
                    "path": "/v2/online-checkout/merchant-settings",
                    "paginator": "auto",
                },
            },
            # Returns a single [CatalogItem](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogItem) as a [CatalogObject](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogObject) based on the provided ID. The returned object includes all of the relevant [CatalogItem](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogItem) information including: [CatalogItemVariation](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogItemVariation) children, references to its [CatalogModifierList](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogModifierList) objects, and the ids of any [CatalogTax](https://developer.squareup.com/reference/square_2024-04-17/objects/CatalogTax) objects that apply to it.
            {
                "name": "retrieve_catalog_object",
                "table_name": "object",
                "endpoint": {
                    "path": "/v2/catalog/object/{object_id}",
                    "params": {
                        "object_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "include_related_objects": "OPTIONAL_CONFIG",
                        # "catalog_version": "OPTIONAL_CONFIG",
                        # "include_category_path_to_root": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Provides summary information for a merchant's online store orders.
            {
                "name": "v1_list_orders",
                "table_name": "order",
                "endpoint": {
                    "path": "/v1/{location_id}/orders",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "order": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "batch_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Provides comprehensive information for a single online store order, including the order's history.
            {
                "name": "v1_retrieve_order",
                "table_name": "order",
                "endpoint": {
                    "path": "/v1/{location_id}/orders/{order_id}",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves an [Order](https://developer.squareup.com/reference/square_2024-04-17/objects/Order) by ID.
            {
                "name": "retrieve_order",
                "table_name": "order",
                "endpoint": {
                    "path": "/v2/orders/{order_id}",
                    "params": {
                        "order_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of payments taken by the account making the request.  Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.  The maximum results per page is 100.
            {
                "name": "list_payments",
                "table_name": "payment",
                "endpoint": {
                    "path": "/v2/payments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "begin_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                        # "total": "OPTIONAL_CONFIG",
                        # "last_4": "OPTIONAL_CONFIG",
                        # "card_brand": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details for a specific payment.
            {
                "name": "get_payment",
                "table_name": "payment",
                "endpoint": {
                    "path": "/v2/payments/{payment_id}",
                    "params": {
                        "payment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists all payment links.
            {
                "name": "list_payment_links",
                "table_name": "payment_link",
                "endpoint": {
                    "path": "/v2/online-checkout/payment-links",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a payment link.
            {
                "name": "retrieve_payment_link",
                "table_name": "payment_link",
                "endpoint": {
                    "path": "/v2/online-checkout/payment-links/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of all payouts for the default location. You can filter payouts by location ID, status, time range, and order them in ascending or descending order. To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
            {
                "name": "list_payouts",
                "table_name": "payout",
                "endpoint": {
                    "path": "/v2/payouts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "location_id": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "begin_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details of a specific payout identified by a payout ID. To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
            {
                "name": "get_payout",
                "table_name": "payout",
                "endpoint": {
                    "path": "/v2/payouts/{payout_id}",
                    "params": {
                        "payout_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of all payout entries for a specific payout. To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.
            {
                "name": "list_payout_entries",
                "table_name": "payout_entry",
                "endpoint": {
                    "path": "/v2/payouts/{payout_id}/payout-entries",
                    "params": {
                        "payout_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2024-04-17/inventory-api/retrieve-inventory-physical-count) after the endpoint URL is updated to conform to the standard convention.
            {
                "name": "deprecated_retrieve_inventory_physical_count",
                "table_name": "physical_count",
                "endpoint": {
                    "path": "/v2/inventory/physical-count/{physical_count_id}",
                    "params": {
                        "physical_count_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2024-04-17/objects/InventoryPhysicalCount) object with the provided `physical_count_id`.
            {
                "name": "retrieve_inventory_physical_count",
                "table_name": "physical_count",
                "endpoint": {
                    "path": "/v2/inventory/physical-counts/{physical_count_id}",
                    "params": {
                        "physical_count_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of loyalty programs in the seller's account. Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).   Replaced with [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2024-04-17/loyalty-api/retrieve-loyalty-program) when used with the keyword `main`.
            {
                "name": "list_loyalty_programs",
                "table_name": "program",
                "endpoint": {
                    "path": "/v2/loyalty/programs",
                    "paginator": "auto",
                },
            },
            # Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.  Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).
            {
                "name": "retrieve_loyalty_program",
                "table_name": "program",
                "endpoint": {
                    "path": "/v2/loyalty/programs/{program_id}",
                    "params": {
                        "program_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists the loyalty promotions associated with a [loyalty program](https://developer.squareup.com/reference/square_2024-04-17/objects/LoyaltyProgram). Results are sorted by the `created_at` date in descending order (newest to oldest).
            {
                "name": "list_loyalty_promotions",
                "table_name": "promotion",
                "endpoint": {
                    "path": "/v2/loyalty/programs/{program_id}/promotions",
                    "params": {
                        "program_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a loyalty promotion.
            {
                "name": "retrieve_loyalty_promotion",
                "table_name": "promotion",
                "endpoint": {
                    "path": "/v2/loyalty/programs/{program_id}/promotions/{promotion_id}",
                    "params": {
                        "program_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "promotion_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of refunds for the account making the request.  Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.  The maximum results per page is 100.
            {
                "name": "list_payment_refunds",
                "table_name": "refund",
                "endpoint": {
                    "path": "/v2/refunds",
                    "params": {
                        # the parameters below can optionally be configured
                        # "begin_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "source_type": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a specific refund using the `refund_id`.
            {
                "name": "get_payment_refund",
                "table_name": "refund",
                "endpoint": {
                    "path": "/v2/refunds/{refund_id}",
                    "params": {
                        "refund_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.
            {
                "name": "get_terminal_refund",
                "table_name": "refund",
                "endpoint": {
                    "path": "/v2/terminals/refunds/{terminal_refund_id}",
                    "params": {
                        "terminal_refund_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a loyalty reward.
            {
                "name": "retrieve_loyalty_reward",
                "table_name": "reward",
                "endpoint": {
                    "path": "/v2/loyalty/rewards/{reward_id}",
                    "params": {
                        "reward_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the list of customer segments of a business.
            {
                "name": "list_customer_segments",
                "table_name": "segment",
                "endpoint": {
                    "path": "/v2/customers/segments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a specific customer segment as identified by the `segment_id` value.
            {
                "name": "retrieve_customer_segment",
                "table_name": "segment",
                "endpoint": {
                    "path": "/v2/customers/segments/{segment_id}",
                    "params": {
                        "segment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Provides the details for all of the cash drawer shifts for a location in a date range.
            {
                "name": "list_cash_drawer_shifts",
                "table_name": "shift",
                "endpoint": {
                    "path": "/v2/cash-drawers/shifts",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "begin_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Provides the summary details for a single cash drawer shift. See [ListCashDrawerShiftEvents](https://developer.squareup.com/reference/square_2024-04-17/cash-drawers-api/list-cash-drawer-shift-events) for a list of cash drawer shift events.
            {
                "name": "retrieve_cash_drawer_shift",
                "table_name": "shift",
                "endpoint": {
                    "path": "/v2/cash-drawers/shifts/{shift_id}",
                    "params": {
                        "shift_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "location_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single `Shift` specified by `id`.
            {
                "name": "get_shift",
                "table_name": "shift",
                "endpoint": {
                    "path": "/v2/labor/shifts/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the `created_at` date.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
            {
                "name": "list_sites",
                "table_name": "site",
                "endpoint": {
                    "path": "/v2/sites",
                    "paginator": "auto",
                },
            },
            # Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.  You can call [ListSites](https://developer.squareup.com/reference/square_2024-04-17/sites-api/list-sites) to get the IDs of the sites that belong to a seller.   __Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).
            {
                "name": "retrieve_snippet",
                "table_name": "snippet",
                "endpoint": {
                    "path": "/v2/sites/{site_id}/snippet",
                    "params": {
                        "site_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a specific subscription.
            {
                "name": "retrieve_subscription",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v2/subscriptions/{subscription_id}",
                    "params": {
                        "subscription_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "include": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists all webhook subscriptions owned by your application.
            {
                "name": "list_webhook_subscriptions",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v2/webhooks/subscriptions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "include_disabled": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a webhook subscription identified by its ID.
            {
                "name": "retrieve_webhook_subscription",
                "table_name": "subscription",
                "endpoint": {
                    "path": "/v2/webhooks/subscriptions/{subscription_id}",
                    "params": {
                        "subscription_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a `TeamMember` object for the given `TeamMember.id`. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).
            {
                "name": "retrieve_team_member",
                "table_name": "team_member",
                "endpoint": {
                    "path": "/v2/team-members/{team_member_id}",
                    "params": {
                        "team_member_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists booking profiles for team members.
            {
                "name": "list_team_member_booking_profiles",
                "table_name": "team_member_booking_profile",
                "endpoint": {
                    "path": "/v2/bookings/team-member-booking-profiles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "bookable_only": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "location_id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a team member's booking profile.
            {
                "name": "retrieve_team_member_booking_profile",
                "table_name": "team_member_booking_profile",
                "endpoint": {
                    "path": "/v2/bookings/team-member-booking-profiles/{team_member_id}",
                    "params": {
                        "team_member_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a paginated list of `TeamMemberWage` instances for a business.
            {
                "name": "list_team_member_wages",
                "table_name": "team_member_wage",
                "endpoint": {
                    "path": "/v2/labor/team-member-wages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "team_member_id": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a single `TeamMemberWage` specified by `id`.
            {
                "name": "get_team_member_wage",
                "table_name": "team_member_wage",
                "endpoint": {
                    "path": "/v2/labor/team-member-wages/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists transactions for a particular location.  Transactions include payment information from sales and exchanges and refund information from returns and exchanges.  Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50
            {
                "name": "list_transactions",
                "table_name": "transaction",
                "endpoint": {
                    "path": "/v2/locations/{location_id}/transactions",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "begin_time": "OPTIONAL_CONFIG",
                        # "end_time": "OPTIONAL_CONFIG",
                        # "sort_order": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details for a single transaction.
            {
                "name": "retrieve_transaction",
                "table_name": "transaction",
                "endpoint": {
                    "path": "/v2/locations/{location_id}/transactions/{transaction_id}",
                    "params": {
                        "location_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "transaction_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2024-04-17/objects/InventoryTransfer) object with the provided `transfer_id`.
            {
                "name": "retrieve_inventory_transfer",
                "table_name": "transfer",
                "endpoint": {
                    "path": "/v2/inventory/transfers/{transfer_id}",
                    "params": {
                        "transfer_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the vendor of a specified [Vendor](https://developer.squareup.com/reference/square_2024-04-17/objects/Vendor) ID.
            {
                "name": "retrieve_vendor",
                "table_name": "vendor",
                "endpoint": {
                    "path": "/v2/vendors/{vendor_id}",
                    "params": {
                        "vendor_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a `WageSetting` object for a team member specified by `TeamMember.id`. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).
            {
                "name": "retrieve_wage_setting",
                "table_name": "wage_setting",
                "endpoint": {
                    "path": "/v2/team-members/{team_member_id}/wage-setting",
                    "params": {
                        "team_member_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of `WorkweekConfig` instances for a business.
            {
                "name": "list_workweek_configs",
                "table_name": "workweek_config",
                "endpoint": {
                    "path": "/v2/labor/workweek-configs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "limit": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
