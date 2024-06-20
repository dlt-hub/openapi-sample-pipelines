from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="magento_source", max_table_nesting=2)
def magento_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "analytics_link_provider_v1_get_get",
                "table_name": "analytics_data_link_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/analytics/link",
                    "paginator": "auto",
                },
            },
            # Get Bulk summary data with list of operations items full data.
            {
                "name": "asynchronous_operations_bulk_status_v1_get_bulk_detailed_status_get",
                "table_name": "asynchronous_operations_data_detailed_operation_status_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "operations_list",
                    "path": "/V1/bulk/{bulkUuid}/detailed-status",
                    "params": {
                        "bulkUuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get Bulk summary data with list of operations items short data.
            {
                "name": "asynchronous_operations_bulk_status_v1_get_bulk_short_status_get",
                "table_name": "asynchronous_operations_data_summary_operation_status_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "operations_list",
                    "path": "/V1/bulk/{bulkUuid}/status",
                    "params": {
                        "bulkUuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all children for Bundle product
            {
                "name": "bundle_product_link_management_v1_get_children_get",
                "table_name": "bundle_data_link_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/bundle-products/{productSku}/children",
                    "params": {
                        "productSku": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "optionId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get all options for bundle product
            {
                "name": "bundle_product_option_repository_v1_get_list_get",
                "table_name": "bundle_data_option_interface",
                "primary_key": "sku",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/bundle-products/{sku}/options/all",
                    "params": {
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get option for bundle product
            {
                "name": "bundle_product_option_repository_v1_get_get",
                "table_name": "bundle_data_option_interface",
                "primary_key": "option_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/bundle-products/{sku}/options/{optionId}",
                    "params": {
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "optionId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all types for options for bundle products
            {
                "name": "bundle_product_option_type_list_v1_get_items_get",
                "table_name": "bundle_data_option_type_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/bundle-products/options/types",
                    "paginator": "auto",
                },
            },
            # Retrieve all attributes for entity type
            {
                "name": "catalog_category_attribute_repository_v1_get_list_get",
                "table_name": "catalog_data_category_attribute_interface",
                "primary_key": "attribute_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/categories/attributes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve specific attribute
            {
                "name": "catalog_category_attribute_repository_v1_get_get",
                "table_name": "catalog_data_category_attribute_interface",
                "primary_key": "attribute_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/categories/attributes/{attributeCode}",
                    "params": {
                        "attributeCode": {
                            "type": "resolve",
                            "resource": "catalog_category_attribute_repository_v1_get_list_get",
                            "field": "attribute_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get category list
            {
                "name": "catalog_category_list_v1_get_list_get",
                "table_name": "catalog_data_category_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/categories/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get info about category by category id
            {
                "name": "catalog_category_repository_v1_get_get",
                "table_name": "catalog_data_category_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/categories/{categoryId}",
                    "params": {
                        "categoryId": {
                            "type": "resolve",
                            "resource": "catalog_category_management_v1_get_tree_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "storeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get products assigned to category
            {
                "name": "catalog_category_link_management_v1_get_assigned_products_get",
                "table_name": "catalog_data_category_product_link_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/categories/{categoryId}/products",
                    "params": {
                        "categoryId": {
                            "type": "resolve",
                            "resource": "catalog_category_management_v1_get_tree_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of categories
            {
                "name": "catalog_category_management_v1_get_tree_get",
                "table_name": "catalog_data_category_tree_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "children_data",
                    "path": "/V1/categories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "rootCategoryId": "OPTIONAL_CONFIG",
                        # "depth": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve related attributes based on given attribute set ID
            {
                "name": "catalog_product_attribute_management_v1_get_attributes_get",
                "table_name": "catalog_data_product_attribute_interface",
                "primary_key": "attribute_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/attribute-sets/{attributeSetId}/attributes",
                    "params": {
                        "attributeSetId": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve all attributes for entity type
            {
                "name": "catalog_product_attribute_repository_v1_get_list_get",
                "table_name": "catalog_data_product_attribute_interface",
                "primary_key": "attribute_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/products/attributes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve specific attribute
            {
                "name": "catalog_product_attribute_repository_v1_get_get",
                "table_name": "catalog_data_product_attribute_interface",
                "primary_key": "attribute_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/attributes/{attributeCode}",
                    "params": {
                        "attributeCode": {
                            "type": "resolve",
                            "resource": "catalog_product_attribute_repository_v1_get_list_get",
                            "field": "attribute_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.
            {
                "name": "catalog_product_media_attribute_management_v1_get_list_get",
                "table_name": "catalog_data_product_attribute_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/media/types/{attributeSetName}",
                    "params": {
                        "attributeSetName": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the list of gallery entries associated with given product
            {
                "name": "catalog_product_attribute_media_gallery_management_v1_get_list_get",
                "table_name": "catalog_data_product_attribute_media_gallery_entry_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/media",
                    "params": {
                        "sku": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "sku",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return information about gallery entry
            {
                "name": "catalog_product_attribute_media_gallery_management_v1_get_get",
                "table_name": "catalog_data_product_attribute_media_gallery_entry_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/media/{entryId}",
                    "params": {
                        "entryId": {
                            "type": "resolve",
                            "resource": "catalog_product_attribute_media_gallery_management_v1_get_list_get",
                            "field": "id",
                        },
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of product attribute types
            {
                "name": "catalog_product_attribute_types_list_v1_get_items_get",
                "table_name": "catalog_data_product_attribute_type_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/attributes/types",
                    "paginator": "auto",
                },
            },
            # Get the list of custom options for a specific product
            {
                "name": "catalog_product_custom_option_repository_v1_get_list_get",
                "table_name": "catalog_data_product_custom_option_interface",
                "primary_key": "sku",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/options",
                    "params": {
                        "sku": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "sku",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get custom option for a specific product
            {
                "name": "catalog_product_custom_option_repository_v1_get_get",
                "table_name": "catalog_data_product_custom_option_interface",
                "primary_key": "option_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/options/{optionId}",
                    "params": {
                        "optionId": {
                            "type": "resolve",
                            "resource": "catalog_product_custom_option_repository_v1_get_list_get",
                            "field": "sku",
                        },
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get custom option types
            {
                "name": "catalog_product_custom_option_type_list_v1_get_items_get",
                "table_name": "catalog_data_product_custom_option_type_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/options/types",
                    "paginator": "auto",
                },
            },
            # Get all children for Configurable product
            {
                "name": "configurable_product_link_management_v1_get_children_get",
                "table_name": "catalog_data_product_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/configurable-products/{sku}/children",
                    "params": {
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get product list
            {
                "name": "catalog_product_repository_v1_get_list_get",
                "table_name": "catalog_data_product_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/products",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get info about product by product SKU
            {
                "name": "catalog_product_repository_v1_get_get",
                "table_name": "catalog_data_product_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}",
                    "params": {
                        "sku": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "sku",
                        },
                        # the parameters below can optionally be configured
                        # "editMode": "OPTIONAL_CONFIG",
                        # "storeId": "OPTIONAL_CONFIG",
                        # "forceReload": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Provide a list of the product link type attributes
            {
                "name": "catalog_product_link_type_list_v1_get_item_attributes_get",
                "table_name": "catalog_data_product_link_attribute_interface",
                "primary_key": "type",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/links/{type}/attributes",
                    "params": {
                        "type": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Provide the list of links for a specific product
            {
                "name": "catalog_product_link_management_v1_get_linked_items_by_type_get",
                "table_name": "catalog_data_product_link_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/links/{type}",
                    "params": {
                        "type": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "id",
                        },
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve information about available product link types
            {
                "name": "catalog_product_link_type_list_v1_get_items_get",
                "table_name": "catalog_data_product_link_type_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/links/types",
                    "paginator": "auto",
                },
            },
            # Collect and retrieve the list of product render info This info contains raw prices and formated prices, product name, stock status, store_id, etc
            {
                "name": "catalog_product_render_list_v1_get_list_get",
                "table_name": "catalog_data_product_render_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/products-render-info",
                    "params": {
                        "storeId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "currencyCode": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get tier price of product
            {
                "name": "catalog_product_tier_price_management_v1_get_list_get",
                "table_name": "catalog_data_product_tier_price_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/group-prices/{customerGroupId}/tiers",
                    "params": {
                        "customerGroupId": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "id",
                        },
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve available product types
            {
                "name": "catalog_product_type_list_v1_get_product_types_get",
                "table_name": "catalog_data_product_type_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/types",
                    "paginator": "auto",
                },
            },
            # Retrieves a list of SKU's with low inventory qty
            {
                "name": "catalog_inventory_stock_registry_v1_get_low_stock_items_get",
                "table_name": "catalog_inventory_data_stock_item_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/stockItems/lowStock/",
                    "params": {
                        "scopeId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "qty": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "currentPage": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get",
                "table_name": "catalog_inventory_data_stock_item_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/stockItems/{productSku}",
                    "params": {
                        "productSku": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "scopeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get",
                "table_name": "catalog_inventory_data_stock_status_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/stockStatuses/{productSku}",
                    "params": {
                        "productSku": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "scopeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the list of categories in the selected shared catalog.
            {
                "name": "shared_catalog_category_management_v1_get_categories_get",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/sharedCatalog/{id}/categories",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "shared_catalog_shared_catalog_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "gift_card_account_guest_gift_card_account_management_v1_check_gift_card_get",
                "table_name": "check_gift_card",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode}",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "giftCardCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "gift_card_account_gift_card_account_management_v1_check_gift_card_get",
                "table_name": "check_gift_card",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/checkGiftCard/{giftCardCode}",
                    "params": {
                        "giftCardCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists active checkout agreements.
            {
                "name": "checkout_agreements_checkout_agreements_repository_v1_get_list_get",
                "table_name": "checkout_agreements_data_agreement_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/licence",
                    "paginator": "auto",
                },
            },
            # Retrieve blocks matching the specified criteria.
            {
                "name": "cms_block_repository_v1_get_list_get",
                "table_name": "cms_data_block_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/cmsBlock/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve block.
            {
                "name": "cms_block_repository_v1_get_by_id_get",
                "table_name": "cms_data_block_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/cmsBlock/{blockId}",
                    "params": {
                        "blockId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve pages matching the specified criteria.
            {
                "name": "cms_page_repository_v1_get_list_get",
                "table_name": "cms_data_page_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/cmsPage/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve page.
            {
                "name": "cms_page_repository_v1_get_by_id_get",
                "table_name": "cms_data_page_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/cmsPage/{pageId}",
                    "params": {
                        "pageId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the list of company IDs for the companies assigned to the selected catalog.
            {
                "name": "shared_catalog_company_management_v1_get_companies_get",
                "table_name": "company",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/sharedCatalog/{sharedCatalogId}/companies",
                    "params": {
                        "sharedCatalogId": {
                            "type": "resolve",
                            "resource": "shared_catalog_shared_catalog_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of credits for specified companies.
            {
                "name": "company_credit_credit_limit_repository_v1_get_list_get",
                "table_name": "company_credit_data_credit_data_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/companyCredits/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns data on the credit limit for a specified company.
            {
                "name": "company_credit_credit_limit_management_v1_get_credit_by_company_id_get",
                "table_name": "company_credit_data_credit_limit_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/companyCredits/company/{companyId}",
                    "params": {
                        "companyId": {
                            "type": "resolve",
                            "resource": "company_credit_credit_limit_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns data on the credit limit for a specified credit limit ID.
            {
                "name": "company_credit_credit_limit_repository_v1_get_get",
                "table_name": "company_credit_data_credit_limit_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/companyCredits/{creditId}",
                    "params": {
                        "creditId": {
                            "type": "resolve",
                            "resource": "company_credit_credit_limit_repository_v1_get_list_get",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "reload": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the credit history for one or more companies.
            {
                "name": "company_credit_credit_history_management_v1_get_list_get",
                "table_name": "company_credit_data_history_data_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/companyCredits/history",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of companies. The list is an array of objects, and detailed information about item attributes might not be included.
            {
                "name": "company_company_repository_v1_get_list_get",
                "table_name": "company_data_company_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/company/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns company details.
            {
                "name": "company_company_repository_v1_get_get",
                "table_name": "company_data_company_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/company/{companyId}",
                    "params": {
                        "companyId": {
                            "type": "resolve",
                            "resource": "company_company_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of teams and company users in the company structure.
            {
                "name": "company_company_hierarchy_v1_get_company_hierarchy_get",
                "table_name": "company_data_hierarchy_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/hierarchy/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of roles and permissions for a specified company.
            {
                "name": "company_role_repository_v1_get_list_get",
                "table_name": "company_data_role_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/company/role/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of permissions for a specified role.
            {
                "name": "company_role_repository_v1_get_get",
                "table_name": "company_data_role_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/company/role/{roleId}",
                    "params": {
                        "roleId": {
                            "type": "resolve",
                            "resource": "company_role_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of teams for the specified search criteria (team name or description).
            {
                "name": "company_team_repository_v1_get_list_get",
                "table_name": "company_data_team_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/team/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns data for a team in the company, by entity id.
            {
                "name": "company_team_repository_v1_get_get",
                "table_name": "company_data_team_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/team/{teamId}",
                    "params": {
                        "teamId": {
                            "type": "resolve",
                            "resource": "company_team_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get all options for configurable product
            {
                "name": "configurable_product_option_repository_v1_get_list_get",
                "table_name": "configurable_product_data_option_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/configurable-products/{sku}/options/all",
                    "params": {
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get option for configurable product
            {
                "name": "configurable_product_option_repository_v1_get_get",
                "table_name": "configurable_product_data_option_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/configurable-products/{sku}/options/{id}",
                    "params": {
                        "sku": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Gets the account confirmation status.
            {
                "name": "customer_account_management_v1_get_confirmation_status_get",
                "table_name": "confirm",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customers/{customerId}/confirm",
                    "params": {
                        "customerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns information for a coupon in a specified cart.
            {
                "name": "quote_coupon_management_v1_get_get",
                "table_name": "coupon",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/coupons",
                    "paginator": "auto",
                },
            },
            # Returns information for a coupon in a specified cart.
            {
                "name": "get_v1_cartscart_idcoupons",
                "table_name": "coupon",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}/coupons",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return information for a coupon in a specified cart.
            {
                "name": "quote_guest_coupon_management_v1_get_get",
                "table_name": "coupon",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/coupons",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get currency information for the store.
            {
                "name": "directory_currency_information_acquirer_v1_get_currency_info_get",
                "table_name": "currency",
                "endpoint": {
                    "data_selector": "available_currency_codes",
                    "path": "/V1/directory/currency",
                    "paginator": "auto",
                },
            },
            # Retrieve customer address.
            {
                "name": "customer_address_repository_v1_get_by_id_get",
                "table_name": "customer_data_address_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customers/addresses/{addressId}",
                    "params": {
                        "addressId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get customer by Customer ID.
            {
                "name": "customer_customer_repository_v1_get_by_id_get",
                "table_name": "customer_data_address_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "addresses",
                    "path": "/V1/customers/me",
                    "paginator": "auto",
                },
            },
            # Get all attribute metadata.
            {
                "name": "customer_customer_metadata_v1_get_all_attributes_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customer",
                    "paginator": "auto",
                },
            },
            # Retrieve attribute metadata.
            {
                "name": "customer_customer_metadata_v1_get_attribute_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customer/attribute/{attributeCode}",
                    "params": {
                        "attributeCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get custom attributes metadata for the given data interface.
            {
                "name": "customer_customer_metadata_v1_get_custom_attributes_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customer/custom",
                    "params": {
                        # the parameters below can optionally be configured
                        # "dataInterfaceName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve all attributes filtered by form code
            {
                "name": "customer_customer_metadata_v1_get_attributes_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customer/form/{formCode}",
                    "params": {
                        "formCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all attribute metadata.
            {
                "name": "customer_address_metadata_v1_get_all_attributes_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customerAddress",
                    "paginator": "auto",
                },
            },
            # Retrieve attribute metadata.
            {
                "name": "customer_address_metadata_v1_get_attribute_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customerAddress/attribute/{attributeCode}",
                    "params": {
                        "attributeCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get custom attributes metadata for the given data interface.
            {
                "name": "customer_address_metadata_v1_get_custom_attributes_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customerAddress/custom",
                    "params": {
                        # the parameters below can optionally be configured
                        # "dataInterfaceName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve all attributes filtered by form code
            {
                "name": "customer_address_metadata_v1_get_attributes_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/attributeMetadata/customerAddress/form/{formCode}",
                    "params": {
                        "formCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all attribute metadata.
            {
                "name": "rma_rma_attributes_management_v1_get_all_attributes_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/returnsAttributeMetadata",
                    "paginator": "auto",
                },
            },
            # Retrieve all attributes filtered by form code
            {
                "name": "rma_rma_attributes_management_v1_get_attributes_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/returnsAttributeMetadata/form/{formCode}",
                    "params": {
                        "formCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve attribute metadata.
            {
                "name": "rma_rma_attributes_management_v1_get_attribute_metadata_get",
                "table_name": "customer_data_attribute_metadata_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/returnsAttributeMetadata/{attributeCode}",
                    "params": {
                        "attributeCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # View the list of company users assigned to a specified role.
            {
                "name": "company_acl_v1_get_users_by_role_id_get",
                "table_name": "customer_data_customer_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/company/role/{roleId}/users",
                    "params": {
                        "roleId": {
                            "type": "resolve",
                            "resource": "company_role_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve customers which match a specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#CustomerRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "customer_customer_repository_v1_get_list_get",
                "table_name": "customer_data_customer_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/customers/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get customer by Customer ID.
            {
                "name": "get_v1_customerscustomer_id",
                "table_name": "customer_data_customer_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customers/{customerId}",
                    "params": {
                        "customerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get default customer group.
            {
                "name": "customer_group_management_v1_get_default_group_get",
                "table_name": "customer_data_group_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customerGroups/default",
                    "params": {
                        # the parameters below can optionally be configured
                        # "storeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get default customer group.
            {
                "name": "get_v1_customer_groupsdefaultstore_id",
                "table_name": "customer_data_group_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customerGroups/default/{storeId}",
                    "params": {
                        "storeId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve customer groups. The list of groups can be filtered to exclude the NOT_LOGGED_IN group using the first parameter and/or it can be filtered by tax class. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#GroupRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "customer_group_repository_v1_get_list_get",
                "table_name": "customer_data_group_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/customerGroups/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get customer group by group ID.
            {
                "name": "customer_group_repository_v1_get_by_id_get",
                "table_name": "customer_data_group_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customerGroups/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get all countries and regions information for the store.
            {
                "name": "directory_country_information_acquirer_v1_get_countries_info_get",
                "table_name": "directory_data_country_information_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/directory/countries",
                    "paginator": "auto",
                },
            },
            # Get country and region information for the store.
            {
                "name": "directory_country_information_acquirer_v1_get_country_info_get",
                "table_name": "directory_data_country_information_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/directory/countries/{countryId}",
                    "params": {
                        "countryId": {
                            "type": "resolve",
                            "resource": "directory_country_information_acquirer_v1_get_countries_info_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List of links with associated samples
            {
                "name": "downloadable_link_repository_v1_get_list_get",
                "table_name": "downloadable_data_link_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/downloadable-links",
                    "params": {
                        "sku": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "sku",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List of samples for downloadable product
            {
                "name": "downloadable_sample_repository_v1_get_list_get",
                "table_name": "downloadable_data_sample_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/{sku}/downloadable-links/samples",
                    "params": {
                        "sku": {
                            "type": "resolve",
                            "resource": "downloadable_link_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of attribute groups
            {
                "name": "catalog_product_attribute_group_repository_v1_get_list_get",
                "table_name": "eav_data_attribute_group_interface",
                "primary_key": "attribute_group_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/products/attribute-sets/groups/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of attribute options
            {
                "name": "catalog_category_attribute_option_management_v1_get_items_get",
                "table_name": "eav_data_attribute_option_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/categories/attributes/{attributeCode}/options",
                    "params": {
                        "attributeCode": {
                            "type": "resolve",
                            "resource": "catalog_category_attribute_repository_v1_get_list_get",
                            "field": "attribute_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of attribute options
            {
                "name": "catalog_product_attribute_option_management_v1_get_items_get",
                "table_name": "eav_data_attribute_option_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/attributes/{attributeCode}/options",
                    "params": {
                        "attributeCode": {
                            "type": "resolve",
                            "resource": "catalog_product_attribute_repository_v1_get_list_get",
                            "field": "attribute_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of Attribute Sets This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#AttributeSetRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "eav_attribute_set_repository_v1_get_list_get",
                "table_name": "eav_data_attribute_set_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/eav/attribute-sets/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve attribute set information based on given ID
            {
                "name": "eav_attribute_set_repository_v1_get_get",
                "table_name": "eav_data_attribute_set_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/eav/attribute-sets/{attributeSetId}",
                    "params": {
                        "attributeSetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of Attribute Sets
            {
                "name": "catalog_attribute_set_repository_v1_get_list_get",
                "table_name": "eav_data_attribute_set_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/products/attribute-sets/sets/list",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve attribute set information based on given ID
            {
                "name": "catalog_attribute_set_repository_v1_get_get",
                "table_name": "eav_data_attribute_set_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/products/attribute-sets/{attributeSetId}",
                    "params": {
                        "attributeSetId": {
                            "type": "resolve",
                            "resource": "catalog_product_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the billing address for a specified quote.
            {
                "name": "quote_billing_address_management_v1_get_get",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/carts/mine/billing-address",
                    "paginator": "auto",
                },
            },
            # Returns the billing address for a specified quote.
            {
                "name": "get_v1_cartscart_idbilling_address",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/carts/{cartId}/billing-address",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve default billing address for the given customerId.
            {
                "name": "customer_account_management_v1_get_default_billing_address_get",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/customers/me/billingAddress",
                    "paginator": "auto",
                },
            },
            # Retrieve default shipping address for the given customerId.
            {
                "name": "customer_account_management_v1_get_default_shipping_address_get",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/customers/me/shippingAddress",
                    "paginator": "auto",
                },
            },
            # Retrieve default billing address for the given customerId.
            {
                "name": "get_v1_customerscustomer_idbilling_address",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/customers/{customerId}/billingAddress",
                    "params": {
                        "customerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve default shipping address for the given customerId.
            {
                "name": "get_v1_customerscustomer_idshipping_address",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/customers/{customerId}/shippingAddress",
                    "params": {
                        "customerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the billing address for a specified quote.
            {
                "name": "quote_guest_billing_address_management_v1_get_get",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/guest-carts/{cartId}/billing-address",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the billing address for a specified quote.
            {
                "name": "negotiable_quote_billing_address_management_v1_get_get",
                "table_name": "framework_attribute_interface",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/V1/negotiable-carts/{cartId}/billing-address",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get custom attribute metadata for the given Data object's attribute set
            {
                "name": "rma_rma_attributes_management_v1_get_custom_attributes_metadata_get",
                "table_name": "framework_metadata_object_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/returnsAttributeMetadata/custom",
                    "params": {
                        # the parameters below can optionally be configured
                        # "dataObjectClassName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Make Full Text Search and return found Documents
            {
                "name": "search_v1_search_get",
                "table_name": "framework_search_document_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[requestName]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return GiftCard Account cards
            {
                "name": "gift_card_account_gift_card_account_management_v1_get_list_by_quote_id_get",
                "table_name": "gift_card",
                "endpoint": {
                    "data_selector": "gift_cards",
                    "path": "/V1/carts/{quoteId}/giftCards",
                    "params": {
                        "quoteId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the gift message for a specified order.
            {
                "name": "gift_message_cart_repository_v1_get_get",
                "table_name": "gift_message_data_message_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/gift-message",
                    "paginator": "auto",
                },
            },
            # Return the gift message for a specified item in a specified shopping cart.
            {
                "name": "gift_message_item_repository_v1_get_get",
                "table_name": "gift_message_data_message_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/gift-message/{itemId}",
                    "params": {
                        "itemId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the gift message for a specified order.
            {
                "name": "get_v1_cartscart_idgift_message",
                "table_name": "gift_message_data_message_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}/gift-message",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the gift message for a specified item in a specified shopping cart.
            {
                "name": "get_v1_cartscart_idgift_messageitem_id",
                "table_name": "gift_message_data_message_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}/gift-message/{itemId}",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itemId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the gift message for a specified order.
            {
                "name": "gift_message_guest_cart_repository_v1_get_get",
                "table_name": "gift_message_data_message_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/gift-message",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the gift message for a specified item in a specified shopping cart.
            {
                "name": "gift_message_guest_item_repository_v1_get_get",
                "table_name": "gift_message_data_message_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/gift-message/{itemId}",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itemId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return list of gift wrapping data objects based on search criteria
            {
                "name": "gift_wrapping_wrapping_repository_v1_get_list_get",
                "table_name": "gift_wrapping_data_wrapping_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/gift-wrappings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return data object for specified wrapping ID and store.
            {
                "name": "gift_wrapping_wrapping_repository_v1_get_get",
                "table_name": "gift_wrapping_data_wrapping_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/gift-wrappings/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "storeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get shipping label int the PDF format
            {
                "name": "rma_track_management_v1_get_shipping_label_pdf_get",
                "table_name": "label",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/returns/{id}/labels",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Gets a specified shipment label.
            {
                "name": "sales_shipment_management_v1_get_label_get",
                "table_name": "label",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/shipment/{id}/label",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns an array of enabled modules
            {
                "name": "backend_module_service_v1_get_modules_get",
                "table_name": "module",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/modules",
                    "paginator": "auto",
                },
            },
            # Returns content for one or more files attached on the quote comment.
            {
                "name": "negotiable_quote_attachment_content_management_v1_get_get",
                "table_name": "negotiable_quote_data_attachment_content_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/negotiableQuote/attachmentContent",
                    "params": {
                        "attachmentIds": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns comments for a specified negotiable quote.
            {
                "name": "negotiable_quote_comment_locator_v1_get_list_for_quote_get",
                "table_name": "negotiable_quote_data_comment_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/negotiableQuote/{quoteId}/comments",
                    "params": {
                        "quoteId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get operations count by bulk uuid and status.
            {
                "name": "asynchronous_operations_bulk_status_v1_get_operations_count_by_bulk_id_and_status_get",
                "table_name": "operation_statu",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/bulk/{bulkUuid}/operation-status/{status}",
                    "params": {
                        "bulkUuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "status": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Check if customer group can be deleted.
            {
                "name": "customer_group_management_v1_is_readonly_get",
                "table_name": "permission",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customerGroups/{id}/permissions",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the list of product SKUs in the selected shared catalog.
            {
                "name": "shared_catalog_product_management_v1_get_products_get",
                "table_name": "product",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/sharedCatalog/{id}/products",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "shared_catalog_shared_catalog_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Enables administrative users to list carts that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#CartRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "quote_cart_repository_v1_get_list_get",
                "table_name": "quote_data_cart_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/carts/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Enables an administrative user to return information for a specified cart.
            {
                "name": "quote_cart_repository_v1_get_get",
                "table_name": "quote_data_cart_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Enable a guest user to return information for a specified cart.
            {
                "name": "quote_guest_cart_repository_v1_get_get",
                "table_name": "quote_data_cart_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns information for the cart for a specified customer.
            {
                "name": "quote_cart_management_v1_get_cart_for_customer_get",
                "table_name": "quote_data_cart_item_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/carts/mine",
                    "paginator": "auto",
                },
            },
            # Lists items that are assigned to a specified cart.
            {
                "name": "quote_cart_item_repository_v1_get_list_get",
                "table_name": "quote_data_cart_item_interface",
                "primary_key": "item_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/items",
                    "paginator": "auto",
                },
            },
            # Lists items that are assigned to a specified cart.
            {
                "name": "get_v1_cartscart_iditems",
                "table_name": "quote_data_cart_item_interface",
                "primary_key": "item_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}/items",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List items that are assigned to a specified cart.
            {
                "name": "quote_guest_cart_item_repository_v1_get_list_get",
                "table_name": "quote_data_cart_item_interface",
                "primary_key": "item_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/items",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get payment information
            {
                "name": "checkout_payment_information_management_v1_get_payment_information_get",
                "table_name": "quote_data_payment_method_interface",
                "endpoint": {
                    "data_selector": "payment_methods",
                    "path": "/V1/carts/mine/payment-information",
                    "paginator": "auto",
                },
            },
            # Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "quote_payment_method_management_v1_get_list_get",
                "table_name": "quote_data_payment_method_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/payment-methods",
                    "paginator": "auto",
                },
            },
            # Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "get_v1_cartscart_idpayment_methods",
                "table_name": "quote_data_payment_method_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}/payment-methods",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get payment information
            {
                "name": "checkout_guest_payment_information_management_v1_get_payment_information_get",
                "table_name": "quote_data_payment_method_interface",
                "endpoint": {
                    "data_selector": "payment_methods",
                    "path": "/V1/guest-carts/{cartId}/payment-information",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "quote_guest_payment_method_management_v1_get_list_get",
                "table_name": "quote_data_payment_method_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/payment-methods",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get payment information
            {
                "name": "negotiable_quote_payment_information_management_v1_get_payment_information_get",
                "table_name": "quote_data_payment_method_interface",
                "endpoint": {
                    "data_selector": "payment_methods",
                    "path": "/V1/negotiable-carts/{cartId}/payment-information",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists applicable shipping methods for a specified quote.
            {
                "name": "quote_shipping_method_management_v1_get_list_get",
                "table_name": "quote_data_shipping_method_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/shipping-methods",
                    "paginator": "auto",
                },
            },
            # Lists applicable shipping methods for a specified quote.
            {
                "name": "get_v1_cartscart_idshipping_methods",
                "table_name": "quote_data_shipping_method_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/{cartId}/shipping-methods",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List applicable shipping methods for a specified quote.
            {
                "name": "quote_guest_shipping_method_management_v1_get_list_get",
                "table_name": "quote_data_shipping_method_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/shipping-methods",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns quote totals data for a specified cart.
            {
                "name": "quote_cart_total_repository_v1_get_get",
                "table_name": "quote_data_totals_item_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/carts/mine/totals",
                    "paginator": "auto",
                },
            },
            # Returns quote totals data for a specified cart.
            {
                "name": "get_v1_cartscart_idtotals",
                "table_name": "quote_data_totals_item_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/carts/{cartId}/totals",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return quote totals data for a specified cart.
            {
                "name": "quote_guest_cart_total_repository_v1_get_get",
                "table_name": "quote_data_totals_item_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/guest-carts/{cartId}/totals",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns quote totals data for a specified cart.
            {
                "name": "negotiable_quote_cart_total_repository_v1_get_get",
                "table_name": "quote_data_totals_item_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/negotiable-carts/{cartId}/totals",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Check if customer can be deleted.
            {
                "name": "customer_account_management_v1_is_readonly_get",
                "table_name": "readonly",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customers/{customerId}/permissions/readonly",
                    "params": {
                        "customerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Check if password reset token is valid.
            {
                "name": "customer_account_management_v1_validate_reset_password_link_token_get",
                "table_name": "reset_link_token",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}",
                    "params": {
                        "customerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "resetPasswordLinkToken": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Comments list
            {
                "name": "rma_comment_management_v1_comments_list_get",
                "table_name": "rma_data_comment_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/returns/{id}/comments",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return list of rma data objects based on search criteria
            {
                "name": "rma_rma_management_v1_search_get",
                "table_name": "rma_data_rma_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/returns",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return data object for specified RMA id
            {
                "name": "rma_rma_repository_v1_get_get",
                "table_name": "rma_data_rma_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/returns/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get track list
            {
                "name": "rma_track_management_v1_get_tracks_get",
                "table_name": "rma_data_track_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/returns/{id}/tracking-numbers",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists comments for a specified credit memo.
            {
                "name": "sales_creditmemo_management_v1_get_comments_list_get",
                "table_name": "sales_data_creditmemo_comment_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/creditmemo/{id}/comments",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Loads a specified credit memo.
            {
                "name": "sales_creditmemo_repository_v1_get_get",
                "table_name": "sales_data_creditmemo_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/creditmemo/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists credit memos that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#CreditmemoRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_creditmemo_repository_v1_get_list_get",
                "table_name": "sales_data_creditmemo_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/creditmemos",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists comments for a specified invoice.
            {
                "name": "sales_invoice_management_v1_get_comments_list_get",
                "table_name": "sales_data_invoice_comment_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/invoices/{id}/comments",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists invoices that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#InvoiceRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_invoice_repository_v1_get_list_get",
                "table_name": "sales_data_invoice_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/invoices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Loads a specified invoice.
            {
                "name": "sales_invoice_repository_v1_get_get",
                "table_name": "sales_data_invoice_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/invoices/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists orders that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#OrderRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_order_repository_v1_get_list_get",
                "table_name": "sales_data_order_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/orders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Loads a specified order.
            {
                "name": "sales_order_repository_v1_get_get",
                "table_name": "sales_data_order_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/orders/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists order items that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#OrderItemRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_order_item_repository_v1_get_list_get",
                "table_name": "sales_data_order_item_interface",
                "primary_key": "item_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/orders/items",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Loads a specified order item.
            {
                "name": "sales_order_item_repository_v1_get_get",
                "table_name": "sales_data_order_item_interface",
                "primary_key": "item_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/orders/items/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "sales_order_item_repository_v1_get_list_get",
                            "field": "item_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Lists comments for a specified order.
            {
                "name": "sales_order_management_v1_get_comments_list_get",
                "table_name": "sales_data_order_status_history_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/orders/{id}/comments",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists comments for a specified shipment.
            {
                "name": "sales_shipment_management_v1_get_comments_list_get",
                "table_name": "sales_data_shipment_comment_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/shipment/{id}/comments",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Loads a specified shipment.
            {
                "name": "sales_shipment_repository_v1_get_get",
                "table_name": "sales_data_shipment_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/shipment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists shipments that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#ShipmentRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_shipment_repository_v1_get_list_get",
                "table_name": "sales_data_shipment_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/shipments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists transactions that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TransactionRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_transaction_repository_v1_get_list_get",
                "table_name": "sales_data_transaction_interface",
                "primary_key": "transaction_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/transactions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Loads a specified transaction.
            {
                "name": "sales_transaction_repository_v1_get_get",
                "table_name": "sales_data_transaction_interface",
                "primary_key": "transaction_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/transactions/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "sales_transaction_repository_v1_get_list_get",
                            "field": "transaction_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a coupon using the specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#CouponRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_rule_coupon_repository_v1_get_list_get",
                "table_name": "sales_rule_data_coupon_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/coupons/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get coupon by coupon id.
            {
                "name": "sales_rule_coupon_repository_v1_get_by_id_get",
                "table_name": "sales_rule_data_coupon_interface",
                "primary_key": "coupon_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/coupons/{couponId}",
                    "params": {
                        "couponId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve sales rules that match te specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#RuleRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "sales_rule_rule_repository_v1_get_list_get",
                "table_name": "sales_rule_data_rule_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/salesRules/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get rule by ID.
            {
                "name": "sales_rule_rule_repository_v1_get_by_id_get",
                "table_name": "sales_rule_data_rule_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/salesRules/{ruleId}",
                    "params": {
                        "ruleId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the payment method for a specified shopping cart.
            {
                "name": "quote_payment_method_management_v1_get_get",
                "table_name": "selected_payment_method",
                "endpoint": {
                    "data_selector": "additional_data",
                    "path": "/V1/carts/mine/selected-payment-method",
                    "paginator": "auto",
                },
            },
            # Returns the payment method for a specified shopping cart.
            {
                "name": "get_v1_cartscart_idselected_payment_method",
                "table_name": "selected_payment_method",
                "endpoint": {
                    "data_selector": "additional_data",
                    "path": "/V1/carts/{cartId}/selected-payment-method",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the payment method for a specified shopping cart.
            {
                "name": "quote_guest_payment_method_management_v1_get_get",
                "table_name": "selected_payment_method",
                "endpoint": {
                    "data_selector": "additional_data",
                    "path": "/V1/guest-carts/{cartId}/selected-payment-method",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the list of shared catalogs and basic properties for each catalog.
            {
                "name": "shared_catalog_shared_catalog_repository_v1_get_list_get",
                "table_name": "shared_catalog_data_shared_catalog_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/sharedCatalog/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the following properties for the selected shared catalog: ID, Store Group ID, Name, Type, Description, Customer Group, Tax Class.
            {
                "name": "shared_catalog_shared_catalog_repository_v1_get_get",
                "table_name": "shared_catalog_data_shared_catalog_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/sharedCatalog/{sharedCatalogId}",
                    "params": {
                        "sharedCatalogId": {
                            "type": "resolve",
                            "resource": "shared_catalog_shared_catalog_repository_v1_get_list_get",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Gets the status for a specified order.
            {
                "name": "sales_order_management_v1_get_status_get",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/orders/{id}/statuses",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of all groups
            {
                "name": "store_group_repository_v1_get_list_get",
                "table_name": "store_data_group_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/store/storeGroups",
                    "paginator": "auto",
                },
            },
            {
                "name": "store_store_config_manager_v1_get_store_configs_get",
                "table_name": "store_data_store_config_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/store/storeConfigs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "storeCodes": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve list of all stores
            {
                "name": "store_store_repository_v1_get_list_get",
                "table_name": "store_data_store_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/store/storeViews",
                    "paginator": "auto",
                },
            },
            # Retrieve list of all websites
            {
                "name": "store_website_repository_v1_get_list_get",
                "table_name": "store_data_website_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/store/websites",
                    "paginator": "auto",
                },
            },
            # Retrieve tax classes which match a specific criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxClassRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "tax_tax_class_repository_v1_get_list_get",
                "table_name": "tax_data_tax_class_interface",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/taxClasses/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get a tax class with the given tax class id.
            {
                "name": "tax_tax_class_repository_v1_get_get",
                "table_name": "tax_data_tax_class_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/taxClasses/{taxClassId}",
                    "params": {
                        "taxClassId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search TaxRates This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxRateRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "tax_tax_rate_repository_v1_get_list_get",
                "table_name": "tax_data_tax_rate_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/taxRates/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get tax rate
            {
                "name": "tax_tax_rate_repository_v1_get_get",
                "table_name": "tax_data_tax_rate_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/taxRates/{rateId}",
                    "params": {
                        "rateId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Search TaxRules This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxRuleRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
            {
                "name": "tax_tax_rule_repository_v1_get_list_get",
                "table_name": "tax_data_tax_rule_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/V1/taxRules/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "searchCriteria[filterGroups][0][filters][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][value]": "OPTIONAL_CONFIG",
                        # "searchCriteria[filterGroups][0][filters][0][conditionType]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][field]": "OPTIONAL_CONFIG",
                        # "searchCriteria[sortOrders][0][direction]": "OPTIONAL_CONFIG",
                        # "searchCriteria[pageSize]": "OPTIONAL_CONFIG",
                        # "searchCriteria[currentPage]": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get TaxRule
            {
                "name": "tax_tax_rule_repository_v1_get_get",
                "table_name": "tax_data_tax_rule_interface",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/taxRules/{ruleId}",
                    "params": {
                        "ruleId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "temando_shipping_collection_point_cart_collection_point_management_v1_get_collection_points_get",
                "table_name": "temando_shipping_data_collection_point_quote_collection_point_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/carts/mine/collection-point/search-result",
                    "paginator": "auto",
                },
            },
            {
                "name": "temando_shipping_collection_point_guest_cart_collection_point_management_v1_get_collection_points_get",
                "table_name": "temando_shipping_data_collection_point_quote_collection_point_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/V1/guest-carts/{cartId}/collection-point/search-result",
                    "params": {
                        "cartId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
