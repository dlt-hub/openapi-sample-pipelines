# magento pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/magento.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /V1/analytics/link_ 
  *resource*: analytics_link_provider_v1_get_get  
* _GET /V1/bulk/{bulkUuid}/detailed-status_ 
  *resource*: asynchronous_operations_bulk_status_v1_get_bulk_detailed_status_get  
  *description*: Get Bulk summary data with list of operations items full data.
* _GET /V1/bulk/{bulkUuid}/status_ 
  *resource*: asynchronous_operations_bulk_status_v1_get_bulk_short_status_get  
  *description*: Get Bulk summary data with list of operations items short data.
* _GET /V1/bundle-products/{productSku}/children_ 
  *resource*: bundle_product_link_management_v1_get_children_get  
  *description*: Get all children for Bundle product
* _GET /V1/bundle-products/{sku}/options/all_ 
  *resource*: bundle_product_option_repository_v1_get_list_get  
  *description*: Get all options for bundle product
* _GET /V1/bundle-products/{sku}/options/{optionId}_ 
  *resource*: bundle_product_option_repository_v1_get_get  
  *description*: Get option for bundle product
* _GET /V1/bundle-products/options/types_ 
  *resource*: bundle_product_option_type_list_v1_get_items_get  
  *description*: Get all types for options for bundle products
* _GET /V1/categories/attributes_ 
  *resource*: catalog_category_attribute_repository_v1_get_list_get  
  *description*: Retrieve all attributes for entity type
* _GET /V1/categories/attributes/{attributeCode}_ 
  *resource*: catalog_category_attribute_repository_v1_get_get  
  *description*: Retrieve specific attribute
* _GET /V1/categories/list_ 
  *resource*: catalog_category_list_v1_get_list_get  
  *description*: Get category list
* _GET /V1/categories/{categoryId}_ 
  *resource*: catalog_category_repository_v1_get_get  
  *description*: Get info about category by category id
* _GET /V1/categories/{categoryId}/products_ 
  *resource*: catalog_category_link_management_v1_get_assigned_products_get  
  *description*: Get products assigned to category
* _GET /V1/categories_ 
  *resource*: catalog_category_management_v1_get_tree_get  
  *description*: Retrieve list of categories
* _GET /V1/products/attribute-sets/{attributeSetId}/attributes_ 
  *resource*: catalog_product_attribute_management_v1_get_attributes_get  
  *description*: Retrieve related attributes based on given attribute set ID
* _GET /V1/products/attributes_ 
  *resource*: catalog_product_attribute_repository_v1_get_list_get  
  *description*: Retrieve all attributes for entity type
* _GET /V1/products/attributes/{attributeCode}_ 
  *resource*: catalog_product_attribute_repository_v1_get_get  
  *description*: Retrieve specific attribute
* _GET /V1/products/media/types/{attributeSetName}_ 
  *resource*: catalog_product_media_attribute_management_v1_get_list_get  
  *description*: Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.
* _GET /V1/products/{sku}/media_ 
  *resource*: catalog_product_attribute_media_gallery_management_v1_get_list_get  
  *description*: Retrieve the list of gallery entries associated with given product
* _GET /V1/products/{sku}/media/{entryId}_ 
  *resource*: catalog_product_attribute_media_gallery_management_v1_get_get  
  *description*: Return information about gallery entry
* _GET /V1/products/attributes/types_ 
  *resource*: catalog_product_attribute_types_list_v1_get_items_get  
  *description*: Retrieve list of product attribute types
* _GET /V1/products/{sku}/options_ 
  *resource*: catalog_product_custom_option_repository_v1_get_list_get  
  *description*: Get the list of custom options for a specific product
* _GET /V1/products/{sku}/options/{optionId}_ 
  *resource*: catalog_product_custom_option_repository_v1_get_get  
  *description*: Get custom option for a specific product
* _GET /V1/products/options/types_ 
  *resource*: catalog_product_custom_option_type_list_v1_get_items_get  
  *description*: Get custom option types
* _GET /V1/configurable-products/{sku}/children_ 
  *resource*: configurable_product_link_management_v1_get_children_get  
  *description*: Get all children for Configurable product
* _GET /V1/products_ 
  *resource*: catalog_product_repository_v1_get_list_get  
  *description*: Get product list
* _GET /V1/products/{sku}_ 
  *resource*: catalog_product_repository_v1_get_get  
  *description*: Get info about product by product SKU
* _GET /V1/products/links/{type}/attributes_ 
  *resource*: catalog_product_link_type_list_v1_get_item_attributes_get  
  *description*: Provide a list of the product link type attributes
* _GET /V1/products/{sku}/links/{type}_ 
  *resource*: catalog_product_link_management_v1_get_linked_items_by_type_get  
  *description*: Provide the list of links for a specific product
* _GET /V1/products/links/types_ 
  *resource*: catalog_product_link_type_list_v1_get_items_get  
  *description*: Retrieve information about available product link types
* _GET /V1/products-render-info_ 
  *resource*: catalog_product_render_list_v1_get_list_get  
  *description*: Collect and retrieve the list of product render info This info contains raw prices and formated prices, product name, stock status, store_id, etc
* _GET /V1/products/{sku}/group-prices/{customerGroupId}/tiers_ 
  *resource*: catalog_product_tier_price_management_v1_get_list_get  
  *description*: Get tier price of product
* _GET /V1/products/types_ 
  *resource*: catalog_product_type_list_v1_get_product_types_get  
  *description*: Retrieve available product types
* _GET /V1/stockItems/lowStock/_ 
  *resource*: catalog_inventory_stock_registry_v1_get_low_stock_items_get  
  *description*: Retrieves a list of SKU's with low inventory qty
* _GET /V1/stockItems/{productSku}_ 
  *resource*: catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get  
* _GET /V1/stockStatuses/{productSku}_ 
  *resource*: catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get  
* _GET /V1/sharedCatalog/{id}/categories_ 
  *resource*: shared_catalog_category_management_v1_get_categories_get  
  *description*: Return the list of categories in the selected shared catalog.
* _GET /V1/carts/guest-carts/{cartId}/checkGiftCard/{giftCardCode}_ 
  *resource*: gift_card_account_guest_gift_card_account_management_v1_check_gift_card_get  
* _GET /V1/carts/mine/checkGiftCard/{giftCardCode}_ 
  *resource*: gift_card_account_gift_card_account_management_v1_check_gift_card_get  
* _GET /V1/carts/licence_ 
  *resource*: checkout_agreements_checkout_agreements_repository_v1_get_list_get  
  *description*: Lists active checkout agreements.
* _GET /V1/cmsBlock/search_ 
  *resource*: cms_block_repository_v1_get_list_get  
  *description*: Retrieve blocks matching the specified criteria.
* _GET /V1/cmsBlock/{blockId}_ 
  *resource*: cms_block_repository_v1_get_by_id_get  
  *description*: Retrieve block.
* _GET /V1/cmsPage/search_ 
  *resource*: cms_page_repository_v1_get_list_get  
  *description*: Retrieve pages matching the specified criteria.
* _GET /V1/cmsPage/{pageId}_ 
  *resource*: cms_page_repository_v1_get_by_id_get  
  *description*: Retrieve page.
* _GET /V1/sharedCatalog/{sharedCatalogId}/companies_ 
  *resource*: shared_catalog_company_management_v1_get_companies_get  
  *description*: Return the list of company IDs for the companies assigned to the selected catalog.
* _GET /V1/companyCredits/_ 
  *resource*: company_credit_credit_limit_repository_v1_get_list_get  
  *description*: Returns the list of credits for specified companies.
* _GET /V1/companyCredits/company/{companyId}_ 
  *resource*: company_credit_credit_limit_management_v1_get_credit_by_company_id_get  
  *description*: Returns data on the credit limit for a specified company.
* _GET /V1/companyCredits/{creditId}_ 
  *resource*: company_credit_credit_limit_repository_v1_get_get  
  *description*: Returns data on the credit limit for a specified credit limit ID.
* _GET /V1/companyCredits/history_ 
  *resource*: company_credit_credit_history_management_v1_get_list_get  
  *description*: Returns the credit history for one or more companies.
* _GET /V1/company/_ 
  *resource*: company_company_repository_v1_get_list_get  
  *description*: Returns the list of companies. The list is an array of objects, and detailed information about item attributes might not be included.
* _GET /V1/company/{companyId}_ 
  *resource*: company_company_repository_v1_get_get  
  *description*: Returns company details.
* _GET /V1/hierarchy/{id}_ 
  *resource*: company_company_hierarchy_v1_get_company_hierarchy_get  
  *description*: Returns the list of teams and company users in the company structure.
* _GET /V1/company/role/_ 
  *resource*: company_role_repository_v1_get_list_get  
  *description*: Returns the list of roles and permissions for a specified company.
* _GET /V1/company/role/{roleId}_ 
  *resource*: company_role_repository_v1_get_get  
  *description*: Returns the list of permissions for a specified role.
* _GET /V1/team/_ 
  *resource*: company_team_repository_v1_get_list_get  
  *description*: Returns the list of teams for the specified search criteria (team name or description).
* _GET /V1/team/{teamId}_ 
  *resource*: company_team_repository_v1_get_get  
  *description*: Returns data for a team in the company, by entity id.
* _GET /V1/configurable-products/{sku}/options/all_ 
  *resource*: configurable_product_option_repository_v1_get_list_get  
  *description*: Get all options for configurable product
* _GET /V1/configurable-products/{sku}/options/{id}_ 
  *resource*: configurable_product_option_repository_v1_get_get  
  *description*: Get option for configurable product
* _GET /V1/customers/{customerId}/confirm_ 
  *resource*: customer_account_management_v1_get_confirmation_status_get  
  *description*: Gets the account confirmation status.
* _GET /V1/carts/mine/coupons_ 
  *resource*: quote_coupon_management_v1_get_get  
  *description*: Returns information for a coupon in a specified cart.
* _GET /V1/carts/{cartId}/coupons_ 
  *resource*: get_v1_cartscart_idcoupons  
  *description*: Returns information for a coupon in a specified cart.
* _GET /V1/guest-carts/{cartId}/coupons_ 
  *resource*: quote_guest_coupon_management_v1_get_get  
  *description*: Return information for a coupon in a specified cart.
* _GET /V1/directory/currency_ 
  *resource*: directory_currency_information_acquirer_v1_get_currency_info_get  
  *description*: Get currency information for the store.
* _GET /V1/customers/addresses/{addressId}_ 
  *resource*: customer_address_repository_v1_get_by_id_get  
  *description*: Retrieve customer address.
* _GET /V1/customers/me_ 
  *resource*: customer_customer_repository_v1_get_by_id_get  
  *description*: Get customer by Customer ID.
* _GET /V1/attributeMetadata/customer_ 
  *resource*: customer_customer_metadata_v1_get_all_attributes_metadata_get  
  *description*: Get all attribute metadata.
* _GET /V1/attributeMetadata/customer/attribute/{attributeCode}_ 
  *resource*: customer_customer_metadata_v1_get_attribute_metadata_get  
  *description*: Retrieve attribute metadata.
* _GET /V1/attributeMetadata/customer/custom_ 
  *resource*: customer_customer_metadata_v1_get_custom_attributes_metadata_get  
  *description*: Get custom attributes metadata for the given data interface.
* _GET /V1/attributeMetadata/customer/form/{formCode}_ 
  *resource*: customer_customer_metadata_v1_get_attributes_get  
  *description*: Retrieve all attributes filtered by form code
* _GET /V1/attributeMetadata/customerAddress_ 
  *resource*: customer_address_metadata_v1_get_all_attributes_metadata_get  
  *description*: Get all attribute metadata.
* _GET /V1/attributeMetadata/customerAddress/attribute/{attributeCode}_ 
  *resource*: customer_address_metadata_v1_get_attribute_metadata_get  
  *description*: Retrieve attribute metadata.
* _GET /V1/attributeMetadata/customerAddress/custom_ 
  *resource*: customer_address_metadata_v1_get_custom_attributes_metadata_get  
  *description*: Get custom attributes metadata for the given data interface.
* _GET /V1/attributeMetadata/customerAddress/form/{formCode}_ 
  *resource*: customer_address_metadata_v1_get_attributes_get  
  *description*: Retrieve all attributes filtered by form code
* _GET /V1/returnsAttributeMetadata_ 
  *resource*: rma_rma_attributes_management_v1_get_all_attributes_metadata_get  
  *description*: Get all attribute metadata.
* _GET /V1/returnsAttributeMetadata/form/{formCode}_ 
  *resource*: rma_rma_attributes_management_v1_get_attributes_get  
  *description*: Retrieve all attributes filtered by form code
* _GET /V1/returnsAttributeMetadata/{attributeCode}_ 
  *resource*: rma_rma_attributes_management_v1_get_attribute_metadata_get  
  *description*: Retrieve attribute metadata.
* _GET /V1/company/role/{roleId}/users_ 
  *resource*: company_acl_v1_get_users_by_role_id_get  
  *description*: View the list of company users assigned to a specified role.
* _GET /V1/customers/search_ 
  *resource*: customer_customer_repository_v1_get_list_get  
  *description*: Retrieve customers which match a specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#CustomerRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/customers/{customerId}_ 
  *resource*: get_v1_customerscustomer_id  
  *description*: Get customer by Customer ID.
* _GET /V1/customerGroups/default_ 
  *resource*: customer_group_management_v1_get_default_group_get  
  *description*: Get default customer group.
* _GET /V1/customerGroups/default/{storeId}_ 
  *resource*: get_v1_customer_groupsdefaultstore_id  
  *description*: Get default customer group.
* _GET /V1/customerGroups/search_ 
  *resource*: customer_group_repository_v1_get_list_get  
  *description*: Retrieve customer groups. The list of groups can be filtered to exclude the NOT_LOGGED_IN group using the first parameter and/or it can be filtered by tax class. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#GroupRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/customerGroups/{id}_ 
  *resource*: customer_group_repository_v1_get_by_id_get  
  *description*: Get customer group by group ID.
* _GET /V1/directory/countries_ 
  *resource*: directory_country_information_acquirer_v1_get_countries_info_get  
  *description*: Get all countries and regions information for the store.
* _GET /V1/directory/countries/{countryId}_ 
  *resource*: directory_country_information_acquirer_v1_get_country_info_get  
  *description*: Get country and region information for the store.
* _GET /V1/products/{sku}/downloadable-links_ 
  *resource*: downloadable_link_repository_v1_get_list_get  
  *description*: List of links with associated samples
* _GET /V1/products/{sku}/downloadable-links/samples_ 
  *resource*: downloadable_sample_repository_v1_get_list_get  
  *description*: List of samples for downloadable product
* _GET /V1/products/attribute-sets/groups/list_ 
  *resource*: catalog_product_attribute_group_repository_v1_get_list_get  
  *description*: Retrieve list of attribute groups
* _GET /V1/categories/attributes/{attributeCode}/options_ 
  *resource*: catalog_category_attribute_option_management_v1_get_items_get  
  *description*: Retrieve list of attribute options
* _GET /V1/products/attributes/{attributeCode}/options_ 
  *resource*: catalog_product_attribute_option_management_v1_get_items_get  
  *description*: Retrieve list of attribute options
* _GET /V1/eav/attribute-sets/list_ 
  *resource*: eav_attribute_set_repository_v1_get_list_get  
  *description*: Retrieve list of Attribute Sets This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#AttributeSetRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/eav/attribute-sets/{attributeSetId}_ 
  *resource*: eav_attribute_set_repository_v1_get_get  
  *description*: Retrieve attribute set information based on given ID
* _GET /V1/products/attribute-sets/sets/list_ 
  *resource*: catalog_attribute_set_repository_v1_get_list_get  
  *description*: Retrieve list of Attribute Sets
* _GET /V1/products/attribute-sets/{attributeSetId}_ 
  *resource*: catalog_attribute_set_repository_v1_get_get  
  *description*: Retrieve attribute set information based on given ID
* _GET /V1/carts/mine/billing-address_ 
  *resource*: quote_billing_address_management_v1_get_get  
  *description*: Returns the billing address for a specified quote.
* _GET /V1/carts/{cartId}/billing-address_ 
  *resource*: get_v1_cartscart_idbilling_address  
  *description*: Returns the billing address for a specified quote.
* _GET /V1/customers/me/billingAddress_ 
  *resource*: customer_account_management_v1_get_default_billing_address_get  
  *description*: Retrieve default billing address for the given customerId.
* _GET /V1/customers/me/shippingAddress_ 
  *resource*: customer_account_management_v1_get_default_shipping_address_get  
  *description*: Retrieve default shipping address for the given customerId.
* _GET /V1/customers/{customerId}/billingAddress_ 
  *resource*: get_v1_customerscustomer_idbilling_address  
  *description*: Retrieve default billing address for the given customerId.
* _GET /V1/customers/{customerId}/shippingAddress_ 
  *resource*: get_v1_customerscustomer_idshipping_address  
  *description*: Retrieve default shipping address for the given customerId.
* _GET /V1/guest-carts/{cartId}/billing-address_ 
  *resource*: quote_guest_billing_address_management_v1_get_get  
  *description*: Return the billing address for a specified quote.
* _GET /V1/negotiable-carts/{cartId}/billing-address_ 
  *resource*: negotiable_quote_billing_address_management_v1_get_get  
  *description*: Returns the billing address for a specified quote.
* _GET /V1/returnsAttributeMetadata/custom_ 
  *resource*: rma_rma_attributes_management_v1_get_custom_attributes_metadata_get  
  *description*: Get custom attribute metadata for the given Data object's attribute set
* _GET /V1/search_ 
  *resource*: search_v1_search_get  
  *description*: Make Full Text Search and return found Documents
* _GET /V1/carts/{quoteId}/giftCards_ 
  *resource*: gift_card_account_gift_card_account_management_v1_get_list_by_quote_id_get  
  *description*: Return GiftCard Account cards
* _GET /V1/carts/mine/gift-message_ 
  *resource*: gift_message_cart_repository_v1_get_get  
  *description*: Return the gift message for a specified order.
* _GET /V1/carts/mine/gift-message/{itemId}_ 
  *resource*: gift_message_item_repository_v1_get_get  
  *description*: Return the gift message for a specified item in a specified shopping cart.
* _GET /V1/carts/{cartId}/gift-message_ 
  *resource*: get_v1_cartscart_idgift_message  
  *description*: Return the gift message for a specified order.
* _GET /V1/carts/{cartId}/gift-message/{itemId}_ 
  *resource*: get_v1_cartscart_idgift_messageitem_id  
  *description*: Return the gift message for a specified item in a specified shopping cart.
* _GET /V1/guest-carts/{cartId}/gift-message_ 
  *resource*: gift_message_guest_cart_repository_v1_get_get  
  *description*: Return the gift message for a specified order.
* _GET /V1/guest-carts/{cartId}/gift-message/{itemId}_ 
  *resource*: gift_message_guest_item_repository_v1_get_get  
  *description*: Return the gift message for a specified item in a specified shopping cart.
* _GET /V1/gift-wrappings_ 
  *resource*: gift_wrapping_wrapping_repository_v1_get_list_get  
  *description*: Return list of gift wrapping data objects based on search criteria
* _GET /V1/gift-wrappings/{id}_ 
  *resource*: gift_wrapping_wrapping_repository_v1_get_get  
  *description*: Return data object for specified wrapping ID and store.
* _GET /V1/returns/{id}/labels_ 
  *resource*: rma_track_management_v1_get_shipping_label_pdf_get  
  *description*: Get shipping label int the PDF format
* _GET /V1/shipment/{id}/label_ 
  *resource*: sales_shipment_management_v1_get_label_get  
  *description*: Gets a specified shipment label.
* _GET /V1/modules_ 
  *resource*: backend_module_service_v1_get_modules_get  
  *description*: Returns an array of enabled modules
* _GET /V1/negotiableQuote/attachmentContent_ 
  *resource*: negotiable_quote_attachment_content_management_v1_get_get  
  *description*: Returns content for one or more files attached on the quote comment.
* _GET /V1/negotiableQuote/{quoteId}/comments_ 
  *resource*: negotiable_quote_comment_locator_v1_get_list_for_quote_get  
  *description*: Returns comments for a specified negotiable quote.
* _GET /V1/bulk/{bulkUuid}/operation-status/{status}_ 
  *resource*: asynchronous_operations_bulk_status_v1_get_operations_count_by_bulk_id_and_status_get  
  *description*: Get operations count by bulk uuid and status.
* _GET /V1/customerGroups/{id}/permissions_ 
  *resource*: customer_group_management_v1_is_readonly_get  
  *description*: Check if customer group can be deleted.
* _GET /V1/sharedCatalog/{id}/products_ 
  *resource*: shared_catalog_product_management_v1_get_products_get  
  *description*: Return the list of product SKUs in the selected shared catalog.
* _GET /V1/carts/search_ 
  *resource*: quote_cart_repository_v1_get_list_get  
  *description*: Enables administrative users to list carts that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#CartRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/carts/{cartId}_ 
  *resource*: quote_cart_repository_v1_get_get  
  *description*: Enables an administrative user to return information for a specified cart.
* _GET /V1/guest-carts/{cartId}_ 
  *resource*: quote_guest_cart_repository_v1_get_get  
  *description*: Enable a guest user to return information for a specified cart.
* _GET /V1/carts/mine_ 
  *resource*: quote_cart_management_v1_get_cart_for_customer_get  
  *description*: Returns information for the cart for a specified customer.
* _GET /V1/carts/mine/items_ 
  *resource*: quote_cart_item_repository_v1_get_list_get  
  *description*: Lists items that are assigned to a specified cart.
* _GET /V1/carts/{cartId}/items_ 
  *resource*: get_v1_cartscart_iditems  
  *description*: Lists items that are assigned to a specified cart.
* _GET /V1/guest-carts/{cartId}/items_ 
  *resource*: quote_guest_cart_item_repository_v1_get_list_get  
  *description*: List items that are assigned to a specified cart.
* _GET /V1/carts/mine/payment-information_ 
  *resource*: checkout_payment_information_management_v1_get_payment_information_get  
  *description*: Get payment information
* _GET /V1/carts/mine/payment-methods_ 
  *resource*: quote_payment_method_management_v1_get_list_get  
  *description*: Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/carts/{cartId}/payment-methods_ 
  *resource*: get_v1_cartscart_idpayment_methods  
  *description*: Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/guest-carts/{cartId}/payment-information_ 
  *resource*: checkout_guest_payment_information_management_v1_get_payment_information_get  
  *description*: Get payment information
* _GET /V1/guest-carts/{cartId}/payment-methods_ 
  *resource*: quote_guest_payment_method_management_v1_get_list_get  
  *description*: List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/negotiable-carts/{cartId}/payment-information_ 
  *resource*: negotiable_quote_payment_information_management_v1_get_payment_information_get  
  *description*: Get payment information
* _GET /V1/carts/mine/shipping-methods_ 
  *resource*: quote_shipping_method_management_v1_get_list_get  
  *description*: Lists applicable shipping methods for a specified quote.
* _GET /V1/carts/{cartId}/shipping-methods_ 
  *resource*: get_v1_cartscart_idshipping_methods  
  *description*: Lists applicable shipping methods for a specified quote.
* _GET /V1/guest-carts/{cartId}/shipping-methods_ 
  *resource*: quote_guest_shipping_method_management_v1_get_list_get  
  *description*: List applicable shipping methods for a specified quote.
* _GET /V1/carts/mine/totals_ 
  *resource*: quote_cart_total_repository_v1_get_get  
  *description*: Returns quote totals data for a specified cart.
* _GET /V1/carts/{cartId}/totals_ 
  *resource*: get_v1_cartscart_idtotals  
  *description*: Returns quote totals data for a specified cart.
* _GET /V1/guest-carts/{cartId}/totals_ 
  *resource*: quote_guest_cart_total_repository_v1_get_get  
  *description*: Return quote totals data for a specified cart.
* _GET /V1/negotiable-carts/{cartId}/totals_ 
  *resource*: negotiable_quote_cart_total_repository_v1_get_get  
  *description*: Returns quote totals data for a specified cart.
* _GET /V1/customers/{customerId}/permissions/readonly_ 
  *resource*: customer_account_management_v1_is_readonly_get  
  *description*: Check if customer can be deleted.
* _GET /V1/customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken}_ 
  *resource*: customer_account_management_v1_validate_reset_password_link_token_get  
  *description*: Check if password reset token is valid.
* _GET /V1/returns/{id}/comments_ 
  *resource*: rma_comment_management_v1_comments_list_get  
  *description*: Comments list
* _GET /V1/returns_ 
  *resource*: rma_rma_management_v1_search_get  
  *description*: Return list of rma data objects based on search criteria
* _GET /V1/returns/{id}_ 
  *resource*: rma_rma_repository_v1_get_get  
  *description*: Return data object for specified RMA id
* _GET /V1/returns/{id}/tracking-numbers_ 
  *resource*: rma_track_management_v1_get_tracks_get  
  *description*: Get track list
* _GET /V1/creditmemo/{id}/comments_ 
  *resource*: sales_creditmemo_management_v1_get_comments_list_get  
  *description*: Lists comments for a specified credit memo.
* _GET /V1/creditmemo/{id}_ 
  *resource*: sales_creditmemo_repository_v1_get_get  
  *description*: Loads a specified credit memo.
* _GET /V1/creditmemos_ 
  *resource*: sales_creditmemo_repository_v1_get_list_get  
  *description*: Lists credit memos that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#CreditmemoRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/invoices/{id}/comments_ 
  *resource*: sales_invoice_management_v1_get_comments_list_get  
  *description*: Lists comments for a specified invoice.
* _GET /V1/invoices_ 
  *resource*: sales_invoice_repository_v1_get_list_get  
  *description*: Lists invoices that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#InvoiceRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/invoices/{id}_ 
  *resource*: sales_invoice_repository_v1_get_get  
  *description*: Loads a specified invoice.
* _GET /V1/orders_ 
  *resource*: sales_order_repository_v1_get_list_get  
  *description*: Lists orders that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#OrderRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/orders/{id}_ 
  *resource*: sales_order_repository_v1_get_get  
  *description*: Loads a specified order.
* _GET /V1/orders/items_ 
  *resource*: sales_order_item_repository_v1_get_list_get  
  *description*: Lists order items that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#OrderItemRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/orders/items/{id}_ 
  *resource*: sales_order_item_repository_v1_get_get  
  *description*: Loads a specified order item.
* _GET /V1/orders/{id}/comments_ 
  *resource*: sales_order_management_v1_get_comments_list_get  
  *description*: Lists comments for a specified order.
* _GET /V1/shipment/{id}/comments_ 
  *resource*: sales_shipment_management_v1_get_comments_list_get  
  *description*: Lists comments for a specified shipment.
* _GET /V1/shipment/{id}_ 
  *resource*: sales_shipment_repository_v1_get_get  
  *description*: Loads a specified shipment.
* _GET /V1/shipments_ 
  *resource*: sales_shipment_repository_v1_get_list_get  
  *description*: Lists shipments that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#ShipmentRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/transactions_ 
  *resource*: sales_transaction_repository_v1_get_list_get  
  *description*: Lists transactions that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TransactionRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/transactions/{id}_ 
  *resource*: sales_transaction_repository_v1_get_get  
  *description*: Loads a specified transaction.
* _GET /V1/coupons/search_ 
  *resource*: sales_rule_coupon_repository_v1_get_list_get  
  *description*: Retrieve a coupon using the specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#CouponRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/coupons/{couponId}_ 
  *resource*: sales_rule_coupon_repository_v1_get_by_id_get  
  *description*: Get coupon by coupon id.
* _GET /V1/salesRules/search_ 
  *resource*: sales_rule_rule_repository_v1_get_list_get  
  *description*: Retrieve sales rules that match te specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#RuleRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/salesRules/{ruleId}_ 
  *resource*: sales_rule_rule_repository_v1_get_by_id_get  
  *description*: Get rule by ID.
* _GET /V1/carts/mine/selected-payment-method_ 
  *resource*: quote_payment_method_management_v1_get_get  
  *description*: Returns the payment method for a specified shopping cart.
* _GET /V1/carts/{cartId}/selected-payment-method_ 
  *resource*: get_v1_cartscart_idselected_payment_method  
  *description*: Returns the payment method for a specified shopping cart.
* _GET /V1/guest-carts/{cartId}/selected-payment-method_ 
  *resource*: quote_guest_payment_method_management_v1_get_get  
  *description*: Return the payment method for a specified shopping cart.
* _GET /V1/sharedCatalog/_ 
  *resource*: shared_catalog_shared_catalog_repository_v1_get_list_get  
  *description*: Return the list of shared catalogs and basic properties for each catalog.
* _GET /V1/sharedCatalog/{sharedCatalogId}_ 
  *resource*: shared_catalog_shared_catalog_repository_v1_get_get  
  *description*: Return the following properties for the selected shared catalog: ID, Store Group ID, Name, Type, Description, Customer Group, Tax Class.
* _GET /V1/orders/{id}/statuses_ 
  *resource*: sales_order_management_v1_get_status_get  
  *description*: Gets the status for a specified order.
* _GET /V1/store/storeGroups_ 
  *resource*: store_group_repository_v1_get_list_get  
  *description*: Retrieve list of all groups
* _GET /V1/store/storeConfigs_ 
  *resource*: store_store_config_manager_v1_get_store_configs_get  
* _GET /V1/store/storeViews_ 
  *resource*: store_store_repository_v1_get_list_get  
  *description*: Retrieve list of all stores
* _GET /V1/store/websites_ 
  *resource*: store_website_repository_v1_get_list_get  
  *description*: Retrieve list of all websites
* _GET /V1/taxClasses/search_ 
  *resource*: tax_tax_class_repository_v1_get_list_get  
  *description*: Retrieve tax classes which match a specific criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxClassRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/taxClasses/{taxClassId}_ 
  *resource*: tax_tax_class_repository_v1_get_get  
  *description*: Get a tax class with the given tax class id.
* _GET /V1/taxRates/search_ 
  *resource*: tax_tax_rate_repository_v1_get_list_get  
  *description*: Search TaxRates This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxRateRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/taxRates/{rateId}_ 
  *resource*: tax_tax_rate_repository_v1_get_get  
  *description*: Get tax rate
* _GET /V1/taxRules/search_ 
  *resource*: tax_tax_rule_repository_v1_get_list_get  
  *description*: Search TaxRules This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#TaxRuleRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.
* _GET /V1/taxRules/{ruleId}_ 
  *resource*: tax_tax_rule_repository_v1_get_get  
  *description*: Get TaxRule
* _GET /V1/carts/mine/collection-point/search-result_ 
  *resource*: temando_shipping_collection_point_cart_collection_point_management_v1_get_collection_points_get  
* _GET /V1/guest-carts/{cartId}/collection-point/search-result_ 
  *resource*: temando_shipping_collection_point_guest_cart_collection_point_management_v1_get_collection_points_get  
