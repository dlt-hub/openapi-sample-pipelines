from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="klaviyo_source", max_table_nesting=2)
def klaviyo_source(
    api_key: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "api_key",
                "api_key": api_key,
                "name": "Authorization",
                "location": "header",
            },
            "paginator": {
                "type": "json_response",
                "next_url_path": "links.next",
            },
        },
        "resources": [
            # Retrieve the account(s) associated with a given private API key. This will return 1 account object within the array.  You can use this to retrieve account-specific data (contact information, timezone, currency, Public API key, etc.) or test if a Private API Key belongs to the correct account prior to performing subsequent actions with the API.<br><br>*Rate limits*:<br>Burst: `1/s`<br>Steady: `15/m`  **Scopes:** `accounts:read`
            {
                "name": "get_accounts",
                "table_name": "account_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/accounts/",
                },
            },
            # Retrieve a single account object by its account ID. You can only request the account by which the private API key was generated.<br><br>*Rate limits*:<br>Burst: `1/s`<br>Steady: `15/m`  **Scopes:** `accounts:read`
            {
                "name": "get_account",
                "table_name": "account_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/accounts/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_accounts",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[account]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the ID of the related campaign<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_message_relationships_campaign",
                "table_name": "campaign",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaign-messages/{id}/relationships/campaign/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return the related campaign<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_message_campaign",
                "table_name": "campaign",
                "endpoint": {
                    "data_selector": "data.attributes.audiences.included",
                    "path": "/api/campaign-messages/{id}/campaign/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[campaign]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the IDs of all campaigns associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `campaigns:read` `tags:read`
            {
                "name": "get_tag_relationships_campaigns",
                "table_name": "campaign",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/{id}/relationships/campaigns/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the IDs of all messages associated with the given campaign.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_relationships_campaign_messages",
                "table_name": "campaign_message",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaigns/{id}/relationships/campaign-messages/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_campaigns",
                            "field": "id",
                        },
                    },
                },
            },
            # Return all messages that belong to the given campaign.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_campaign_messages",
                "table_name": "campaign_message_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaigns/{id}/campaign-messages/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_campaigns",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieve the status of a recipient estimation job triggered with the `Create Campaign Recipient Estimation Job` endpoint.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_recipient_estimation_job",
                "table_name": "campaign_recipient_estimation_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaign-recipient-estimation-jobs/{id}/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[campaign-recipient-estimation-job]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the estimated recipient count for a campaign with the provided campaign ID. You can refresh this count by using the `Create Campaign Recipient Estimation Job` endpoint.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_recipient_estimation",
                "table_name": "campaign_recipient_estimation_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaign-recipient-estimations/{id}/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[campaign-recipient-estimation]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns some or all campaigns based on filters.  A channel filter is required to list campaigns. Please provide either: `?filter=equals(messages.channel,'email')` to list email campaigns, or `?filter=equals(messages.channel,'sms')` to list SMS campaigns.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaigns",
                "table_name": "campaign_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaigns/",
                },
            },
            # Get a campaign send job<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_send_job",
                "table_name": "campaign_send_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaign-send-jobs/{id}/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[campaign-send-job]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all catalog category bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_create_categories_jobs",
                "table_name": "catalog_category_create_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-category-bulk-create-jobs/",
                },
            },
            # Get all catalog category bulk delete jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_delete_categories_jobs",
                "table_name": "catalog_category_delete_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-category-bulk-delete-jobs/",
                },
            },
            # Get a catalog category bulk delete job with the given job ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_delete_categories_job",
                "table_name": "catalog_category_delete_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-category-bulk-delete-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_delete_categories_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-category-bulk-delete-job]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all catalog categories in an account.  Catalog categories can be sorted by the following fields, in ascending and descending order: `created`  Currently, the only supported integration type is `$custom`, and the only supported catalog type is `$default`.  Returns a maximum of 100 categories per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_categories",
                "table_name": "catalog_category_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-categories/",
                },
            },
            # Get a catalog category with the given category ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_category",
                "table_name": "catalog_category_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-categories/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_categories",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-category]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all catalog categories that an item with the given item ID is in.  Catalog categories can be sorted by the following fields, in ascending and descending order: `created`  Returns a maximum of 100 categories per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_item_categories",
                "table_name": "catalog_category_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-items/{id}/categories/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_items",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all catalog category bulk update jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_update_categories_jobs",
                "table_name": "catalog_category_update_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-category-bulk-update-jobs/",
                },
            },
            # Get all catalog item bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_create_items_jobs",
                "table_name": "catalog_item_create_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-item-bulk-create-jobs/",
                },
            },
            # Get all catalog item bulk delete jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_delete_items_jobs",
                "table_name": "catalog_item_delete_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-item-bulk-delete-jobs/",
                },
            },
            # Get a catalog item bulk delete job with the given job ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_delete_items_job",
                "table_name": "catalog_item_delete_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-item-bulk-delete-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_delete_items_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-item-bulk-delete-job]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all catalog items in an account.  Catalog items can be sorted by the following fields, in ascending and descending order: `created`  Currently, the only supported integration type is `$custom`, and the only supported catalog type is `$default`.  Returns a maximum of 100 items per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_items",
                "table_name": "catalog_item_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-items/",
                },
            },
            # Get all items in a category with the given category ID.  Items can be sorted by the following fields, in ascending and descending order: `created`  Returns a maximum of 100 items per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_category_items",
                "table_name": "catalog_item_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-categories/{id}/items/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_categories",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all catalog item bulk update jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_update_items_jobs",
                "table_name": "catalog_item_update_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-item-bulk-update-jobs/",
                },
            },
            # Get all catalog variant bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_create_variants_jobs",
                "table_name": "catalog_variant_create_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-variant-bulk-create-jobs/",
                },
            },
            # Get all catalog variant bulk delete jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_delete_variants_jobs",
                "table_name": "catalog_variant_delete_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-variant-bulk-delete-jobs/",
                },
            },
            # Get a catalog variant bulk delete job with the given job ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_delete_variants_job",
                "table_name": "catalog_variant_delete_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-variant-bulk-delete-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_delete_variants_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-variant-bulk-delete-job]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all variants in an account.  Variants can be sorted by the following fields, in ascending and descending order: `created`  Currently, the only supported integration type is `$custom`, and the only supported catalog type is `$default`.  Returns a maximum of 100 variants per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_variants",
                "table_name": "catalog_variant_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-variants/",
                },
            },
            # Get a catalog item variant with the given variant ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_variant",
                "table_name": "catalog_variant_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-variants/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_variants",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-variant]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all variants related to the given item ID.  Variants can be sorted by the following fields, in ascending and descending order: `created`  Returns a maximum of 100 variants per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_item_variants",
                "table_name": "catalog_variant_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-items/{id}/variants/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_items",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all catalog variant bulk update jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_update_variants_jobs",
                "table_name": "catalog_variant_update_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-variant-bulk-update-jobs/",
                },
            },
            # Get all catalog categories that a particular item is in.  Returns a maximum of 100 categories per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_item_relationships_categories",
                "table_name": "category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-items/{id}/relationships/categories/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_items",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "page[cursor]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets the coupon relationship associated with the given coupon code id<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
            {
                "name": "get_coupon_relationships_coupon_codes",
                "table_name": "coupon",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupon-codes/{id}/relationships/coupon/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_coupon_codes",
                            "field": "id",
                        },
                    },
                },
            },
            # Gets a list of coupon code relationships associated with the given coupon id<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
            {
                "name": "get_coupon_code_relationships_coupon",
                "table_name": "coupon_code",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupons/{id}/relationships/coupon-codes/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_coupons",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "page[cursor]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all coupon code bulk create jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
            {
                "name": "get_coupon_code_bulk_create_jobs",
                "table_name": "coupon_code_create_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupon-code-bulk-create-jobs/",
                },
            },
            # Gets a list of coupon codes associated with a coupon/coupons or a profile/profiles.  A coupon/coupons or a profile/profiles must be provided as required filter params.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `coupon-codes:read`
            {
                "name": "get_coupon_codes",
                "table_name": "coupon_code_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupon-codes/",
                },
            },
            # Gets a list of coupon codes associated with the given coupon id<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
            {
                "name": "get_coupon_codes_for_coupon",
                "table_name": "coupon_code_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupons/{id}/coupon-codes/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_coupons",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all coupons in an account.  To learn more, see our [Coupons API guide](https://developers.klaviyo.com/en/docs/use_klaviyos_coupons_api).<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
            {
                "name": "get_coupons",
                "table_name": "coupon_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupons/",
                },
            },
            # Get a specific coupon with the given coupon ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
            {
                "name": "get_coupon",
                "table_name": "coupon_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupons/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_coupons",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[coupon]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the coupon associated with a given coupon code ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupons:read`
            {
                "name": "get_coupon_for_coupon_code",
                "table_name": "coupon_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/coupon-codes/{id}/coupon/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_coupon_codes",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all events in an account  Requests can be sorted by the following fields: `datetime`, `timestamp`  Returns a maximum of 200 events per page.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read`
            {
                "name": "get_events",
                "table_name": "event_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/events/",
                },
            },
            # Get the flow associated with the given action ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_action_relationships_flow",
                "table_name": "flow",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-actions/{id}/relationships/flow/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the IDs of all flows associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read` `tags:read`
            {
                "name": "get_tag_relationships_flows",
                "table_name": "flow",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/{id}/relationships/flows/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for flow actions associated with the given flow ID.  Flow action relationships can be sorted by the following fields, in ascending and descending order: `id`,  `status`, `created`, `updated`  Use filters to narrow your results.  Returns a maximum of 50 flow action relationships per request, which can be paginated with offset pagination. Offset pagination uses the following parameters: `page[size]` and `page[number]`.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_relationships_flow_actions",
                "table_name": "flow_action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flows/{id}/relationships/flow-actions/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_flows",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "page[size]": "50",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the flow action for a flow message with the given message ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_message_action",
                "table_name": "flow_action",
                "endpoint": {
                    "data_selector": "data.attributes.tracking_options.utm_params",
                    "path": "/api/flow-messages/{id}/flow-action/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[flow-action]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the [relationship](https://developers.klaviyo.com/en/reference/api_overview#relationships) for a flow message's flow action, given the flow ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_message_relationships_action",
                "table_name": "flow_action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-messages/{id}/relationships/flow-action/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get all flow actions associated with the given flow ID.  Returns a maximum of 50 flows per request, which can be paginated with cursor-based pagination.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_flow_actions",
                "table_name": "flow_action_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flows/{id}/flow-actions/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_flows",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all relationships for flow messages associated with the given flow action ID.  Returns a maximum of 50 flow message relationships per request, which can be paginated with cursor-based pagination.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_action_relationships_messages",
                "table_name": "flow_message",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-actions/{id}/relationships/flow-messages/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "page[cursor]": "OPTIONAL_CONFIG",
                        # "page[size]": "50",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all flow messages associated with the given action ID.  Flow messages can be sorted by the following fields, in ascending and descending order:  ascending: `id`,  `name`, `created`, `updated` descending: `-id`,  `-name`, `-created`, `-updated`  Returns a maximum of 50 flows per request, which can be paginated with offset pagination. Offset pagination uses the following parameters: `page[size]` and `page[number]`<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_action_messages",
                "table_name": "flow_message_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-actions/{id}/flow-messages/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get all flows in an account.  Returns a maximum of 50 flows per request, which can be paginated with cursor-based pagination.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flows",
                "table_name": "flow_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flows/",
                },
            },
            # Get the flow associated with the given action ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_action_flow",
                "table_name": "flow_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-actions/{id}/flow/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[flow]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a specific message based on a required id.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign_message",
                "table_name": "get_campaign_message_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/campaign-messages/{id}/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[campaign-message]": "OPTIONAL_CONFIG",
                        # "fields[campaign]": "OPTIONAL_CONFIG",
                        # "fields[template]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a specific campaign based on a required id.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read`
            {
                "name": "get_campaign",
                "table_name": "get_campaign_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/campaigns/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_campaigns",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[campaign-message]": "OPTIONAL_CONFIG",
                        # "fields[campaign]": "OPTIONAL_CONFIG",
                        # "fields[tag]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a catalog category bulk create job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `categories`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_create_categories_job",
                "table_name": "get_catalog_category_create_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-category-bulk-create-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_create_categories_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-category-bulk-create-job]": "OPTIONAL_CONFIG",
                        # "fields[catalog-category]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a catalog category bulk update job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `categories`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_update_categories_job",
                "table_name": "get_catalog_category_update_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-category-bulk-update-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_update_categories_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-category-bulk-update-job]": "OPTIONAL_CONFIG",
                        # "fields[catalog-category]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a catalog item bulk create job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `items`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_create_items_job",
                "table_name": "get_catalog_item_create_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-item-bulk-create-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_create_items_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-item-bulk-create-job]": "OPTIONAL_CONFIG",
                        # "fields[catalog-item]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a specific catalog item with the given item ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_item",
                "table_name": "get_catalog_item_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-items/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_items",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-item]": "OPTIONAL_CONFIG",
                        # "fields[catalog-variant]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a catalog item bulk update job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `items`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_update_items_job",
                "table_name": "get_catalog_item_update_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-item-bulk-update-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_update_items_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-item-bulk-update-job]": "OPTIONAL_CONFIG",
                        # "fields[catalog-item]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a catalog variant bulk create job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `variants`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_create_variants_job",
                "table_name": "get_catalog_variant_create_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-variant-bulk-create-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_create_variants_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-variant-bulk-create-job]": "OPTIONAL_CONFIG",
                        # "fields[catalog-variant]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a catalog variate bulk update job with the given job ID.  An `include` parameter can be provided to get the following related resource data: `variants`.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_update_variants_job",
                "table_name": "get_catalog_variant_update_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/catalog-variant-bulk-update-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_update_variants_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[catalog-variant-bulk-update-job]": "OPTIONAL_CONFIG",
                        # "fields[catalog-variant]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a coupon code bulk create job with the given job ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `coupon-codes:read`
            {
                "name": "get_coupon_code_bulk_create_job",
                "table_name": "get_coupon_code_create_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/coupon-code-bulk-create-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_coupon_code_bulk_create_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[coupon-code-bulk-create-job]": "OPTIONAL_CONFIG",
                        # "fields[coupon-code]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a Coupon Code specified by the given identifier.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `coupon-codes:read`
            {
                "name": "get_coupon_code",
                "table_name": "get_coupon_code_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/coupon-codes/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_coupon_codes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[coupon-code]": "OPTIONAL_CONFIG",
                        # "fields[coupon]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `events:read`
            {
                "name": "get_event",
                "table_name": "get_event_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/events/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_events",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[event]": "OPTIONAL_CONFIG",
                        # "fields[metric]": "OPTIONAL_CONFIG",
                        # "fields[profile]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a flow action from a flow with the given flow action ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_action",
                "table_name": "get_flow_action_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/flow-actions/{id}/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[flow-action]": "OPTIONAL_CONFIG",
                        # "fields[flow-message]": "OPTIONAL_CONFIG",
                        # "fields[flow]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the flow message of a flow with the given message ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow_message",
                "table_name": "get_flow_message_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/flow-messages/{id}/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[flow-action]": "OPTIONAL_CONFIG",
                        # "fields[flow-message]": "OPTIONAL_CONFIG",
                        # "fields[template]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a flow with the given flow ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read`
            {
                "name": "get_flow",
                "table_name": "get_flow_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/flows/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_flows",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[flow-action]": "OPTIONAL_CONFIG",
                        # "fields[flow]": "OPTIONAL_CONFIG",
                        # "fields[tag]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a list with the given list ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[list]=profile_count` parameter in your API request:<br>Burst: `1/s`<br>Steady: `15/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `lists:read`
            {
                "name": "get_list",
                "table_name": "get_list_retrieve_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/lists/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_lists",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "additional-fields[list]": "OPTIONAL_CONFIG",
                        # "fields[list]": "OPTIONAL_CONFIG",
                        # "fields[tag]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a bulk profile import job with the given job ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read` `profiles:read`
            {
                "name": "get_bulk_profile_import_job",
                "table_name": "get_profile_import_job_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/profile-bulk-import-jobs/{job_id}/",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "get_bulk_profile_import_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[list]": "OPTIONAL_CONFIG",
                        # "fields[profile-bulk-import-job]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `profiles:read`
            {
                "name": "get_profile",
                "table_name": "get_profile_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/profiles/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_profiles",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "additional-fields[profile]": "OPTIONAL_CONFIG",
                        # "fields[list]": "OPTIONAL_CONFIG",
                        # "fields[profile]": "OPTIONAL_CONFIG",
                        # "fields[segment]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a segment with the given segment ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[segment]=profile_count` parameter in your API request:<br>Burst: `1/s`<br>Steady: `15/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `segments:read`
            {
                "name": "get_segment",
                "table_name": "get_segment_retrieve_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/segments/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_segments",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "additional-fields[segment]": "OPTIONAL_CONFIG",
                        # "fields[segment]": "OPTIONAL_CONFIG",
                        # "fields[tag]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve the tag with the given tag ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag",
                "table_name": "get_tag_response_compound_document",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/tags/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[tag-group]": "OPTIONAL_CONFIG",
                        # "fields[tag]": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all images in an account.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `images:read`
            {
                "name": "get_images",
                "table_name": "image_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/images/",
                },
            },
            # Get the image with the given image ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `images:read`
            {
                "name": "get_image",
                "table_name": "image_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/images/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_images",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[image]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get import errors for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `profiles:read`
            {
                "name": "get_bulk_profile_import_job_import_errors",
                "table_name": "import_error_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profile-bulk-import-jobs/{id}/import-errors/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_bulk_profile_import_jobs",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all items in the given category ID.  Returns a maximum of 100 items per request.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `catalogs:read`
            {
                "name": "get_catalog_category_relationships_items",
                "table_name": "item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/catalog-categories/{id}/relationships/items/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_catalog_categories",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "page[cursor]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get list memberships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `profiles:read`
            {
                "name": "get_profile_relationships_lists",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profiles/{id}/relationships/lists/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_profiles",
                            "field": "id",
                        },
                    },
                },
            },
            # Get list relationship for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read`
            {
                "name": "get_bulk_profile_import_job_relationships_lists",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profile-bulk-import-jobs/{id}/relationships/lists/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_bulk_profile_import_jobs",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the IDs of all lists associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `tags:read`
            {
                "name": "get_tag_relationships_lists",
                "table_name": "list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/{id}/relationships/lists/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all lists in an account.  Filter to request a subset of all lists. Lists can be filtered by `id`, `name`, `created`, and `updated` fields.  Returns a maximum of 10 results per page.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `lists:read`
            {
                "name": "get_lists",
                "table_name": "list_list_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/lists/",
                },
            },
            # Get all profiles within a list with the given list ID.  Filter to request a subset of all profiles. Profiles can be filtered by `email`, `phone_number`, `push_token`, and `joined_group_at` fields. Profiles can be sorted by the following fields, in ascending and descending order: `joined_group_at`<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[profile]=predictive_analytics` parameter in your API request:<br>Burst: `10/s`<br>Steady: `150/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `lists:read` `profiles:read`
            {
                "name": "get_list_profiles",
                "table_name": "list_member_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/lists/{id}/profiles/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_lists",
                            "field": "id",
                        },
                    },
                },
            },
            # Get list memberships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `profiles:read`
            {
                "name": "get_profile_lists",
                "table_name": "list_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profiles/{id}/lists/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_profiles",
                            "field": "id",
                        },
                    },
                },
            },
            # Get list for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read`
            {
                "name": "get_bulk_profile_import_job_lists",
                "table_name": "list_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profile-bulk-import-jobs/{id}/lists/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_bulk_profile_import_jobs",
                            "field": "id",
                        },
                    },
                },
            },
            # Get a list of related Metrics for an Event<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `metrics:read`
            {
                "name": "get_event_relationships_metric",
                "table_name": "metric",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/events/{id}/relationships/metric/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_events",
                            "field": "id",
                        },
                    },
                },
            },
            # Get the metric for an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `metrics:read`
            {
                "name": "get_event_metric",
                "table_name": "metric_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/events/{id}/metric/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_events",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[metric]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all metrics in an account.  Requests can be filtered by the following fields: integration `name`, integration `category`  Returns a maximum of 200 results per page.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `metrics:read`
            {
                "name": "get_metrics",
                "table_name": "metric_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/metrics/",
                },
            },
            # Get a metric with the given metric ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `metrics:read`
            {
                "name": "get_metric",
                "table_name": "metric_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/metrics/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_metrics",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[metric]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get profile [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `profiles:read`
            {
                "name": "get_event_relationships_profile",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/events/{id}/relationships/profile/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_events",
                            "field": "id",
                        },
                    },
                },
            },
            # Get profile membership [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for a list with the given list ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `lists:read` `profiles:read`
            {
                "name": "get_list_relationships_profiles",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/lists/{id}/relationships/profiles/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_lists",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "page[cursor]": "OPTIONAL_CONFIG",
                        # "page[size]": "20",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get profile relationships for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `profiles:read`
            {
                "name": "get_bulk_profile_import_job_relationships_profiles",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profile-bulk-import-jobs/{id}/relationships/profiles/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_bulk_profile_import_jobs",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "page[cursor]": "OPTIONAL_CONFIG",
                        # "page[size]": "20",
                    },
                },
            },
            # Get all profile membership [relationships](https://developers.klaviyo.com/en/reference/api_overview#relationships) for the given segment ID.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `profiles:read` `segments:read`
            {
                "name": "get_segment_relationships_profiles",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/segments/{id}/relationships/profiles/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_segments",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "page[cursor]": "OPTIONAL_CONFIG",
                        # "page[size]": "20",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all bulk profile import jobs.  Returns a maximum of 100 jobs per request.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `lists:read` `profiles:read`
            {
                "name": "get_bulk_profile_import_jobs",
                "table_name": "profile_import_job_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profile-bulk-import-jobs/",
                },
            },
            # Get the profile associated with an event with the given event ID.<br><br>*Rate limits*:<br>Burst: `350/s`<br>Steady: `3500/m`  **Scopes:** `events:read` `profiles:read`
            {
                "name": "get_event_profile",
                "table_name": "profile_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/events/{id}/profile/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_events",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "additional-fields[profile]": "OPTIONAL_CONFIG",
                        # "fields[profile]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all profiles in an account.  Profiles can be sorted by the following fields in ascending and descending order: `id`, `created`, `updated`, `email`, `subscriptions.email.marketing.suppression.timestamp`, `subscriptions.email.marketing.list_suppressions.timestamp`<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`<br><br>Rate limits when using the `additional-fields[profile]=predictive_analytics` parameter in your API request:<br>Burst: `10/s`<br>Steady: `150/m`<br><br>To learn more about how the `additional-fields` parameter impacts rate limits, check out our [Rate limits, status codes, and errors](https://developers.klaviyo.com/en/v2024-02-15/docs/rate_limits_and_error_handling) guide.  **Scopes:** `profiles:read`
            {
                "name": "get_profiles",
                "table_name": "profile_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profiles/",
                },
            },
            # Get profiles for the bulk profile import job with the given ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `profiles:read`
            {
                "name": "get_bulk_profile_import_job_profiles",
                "table_name": "profile_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profile-bulk-import-jobs/{id}/profiles/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_bulk_profile_import_jobs",
                            "field": "id",
                        },
                    },
                },
            },
            # Get segment membership relationships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `profiles:read` `segments:read`
            {
                "name": "get_profile_relationships_segments",
                "table_name": "segment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profiles/{id}/relationships/segments/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_profiles",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the IDs of all segments associated with the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `segments:read` `tags:read`
            {
                "name": "get_tag_relationships_segments",
                "table_name": "segment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/{id}/relationships/segments/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                    },
                },
            },
            # Get all segments in an account.  Filter to request a subset of all segments. Segments can be filtered by `name`, `created`, and `updated` fields.  Returns a maximum of 10 results per page.<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `segments:read`
            {
                "name": "get_segments",
                "table_name": "segment_list_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/segments/",
                },
            },
            # Get all profiles within a segment with the given segment ID.  Filter to request a subset of all profiles. Profiles can be filtered by `email`, `phone_number`, `push_token`, and `joined_group_at` fields. Profiles can be sorted by the following fields, in ascending and descending order: `joined_group_at`<br><br>*Rate limits*:<br>Burst: `75/s`<br>Steady: `700/m`  **Scopes:** `profiles:read` `segments:read`
            {
                "name": "get_segment_profiles",
                "table_name": "segment_member_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/segments/{id}/profiles/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_segments",
                            "field": "id",
                        },
                    },
                },
            },
            # Get segment memberships for a profile with the given profile ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `profiles:read` `segments:read`
            {
                "name": "get_profile_segments",
                "table_name": "segment_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/profiles/{id}/segments/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_profiles",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the IDs of all tags associated with the given campaign.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `campaigns:read` `tags:read`
            {
                "name": "get_campaign_relationships_tags",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaigns/{id}/relationships/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_campaigns",
                            "field": "id",
                        },
                    },
                },
            },
            # Return the tag IDs of all tags associated with the given flow.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read` `tags:read`
            {
                "name": "get_flow_relationships_tags",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flows/{id}/relationships/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_flows",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the tag IDs of all tags associated with the given list.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `tags:read`
            {
                "name": "get_list_relationships_tags",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/lists/{id}/relationships/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_lists",
                            "field": "id",
                        },
                    },
                },
            },
            # If `related_resource` is `tags`, returns the tag IDs of all tags associated with the given segment ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `segments:read` `tags:read`
            {
                "name": "get_segment_relationships_tags",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/segments/{id}/relationships/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_segments",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the tag IDs of all tags inside the given tag group.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag_group_relationships_tags",
                "table_name": "tag",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tag-groups/{id}/relationships/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tag_groups",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the id of the tag group related to the given tag.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag_relationships_tag_group",
                "table_name": "tag_group",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/{id}/relationships/tag-group/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                    },
                },
            },
            # List all tag groups in an account. Every account has one default tag group.  Tag groups can be filtered by `name`, `exclusive`, and `default`, and sorted by `name` or `id` in ascending or descending order.  Returns a maximum of 25 tag groups per request, which can be paginated with [cursor-based pagination](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#pagination).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag_groups",
                "table_name": "tag_group_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tag-groups/",
                },
            },
            # Retrieve the tag group with the given tag group ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag_group",
                "table_name": "tag_group_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tag-groups/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tag_groups",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[tag-group]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the tag group resource for a given tag ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag_tag_group",
                "table_name": "tag_group_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/{id}/tag-group/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tags",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[tag-group]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Return all tags that belong to the given campaign.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `campaigns:read` `tags:read`
            {
                "name": "get_campaign_tags",
                "table_name": "tag_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaigns/{id}/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_campaigns",
                            "field": "id",
                        },
                    },
                },
            },
            # Return all tags associated with the given flow ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `flows:read` `tags:read`
            {
                "name": "get_flow_tags",
                "table_name": "tag_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flows/{id}/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_flows",
                            "field": "id",
                        },
                    },
                },
            },
            # Return all tags associated with the given list ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `lists:read` `tags:read`
            {
                "name": "get_list_tags",
                "table_name": "tag_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/lists/{id}/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_lists",
                            "field": "id",
                        },
                    },
                },
            },
            # Return all tags associated with the given segment ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `segments:read` `tags:read`
            {
                "name": "get_segment_tags",
                "table_name": "tag_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/segments/{id}/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_segments",
                            "field": "id",
                        },
                    },
                },
            },
            # List all tags in an account.  Tags can be filtered by `name`, and sorted by `name` or `id` in ascending or descending order.  Returns a maximum of 50 tags per request, which can be paginated with [cursor-based pagination](https://developers.klaviyo.com/en/v2022-10-17/reference/api_overview#pagination).<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tags",
                "table_name": "tag_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tags/",
                },
            },
            # Return the tags for a given tag group ID.<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `tags:read`
            {
                "name": "get_tag_group_tags",
                "table_name": "tag_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/tag-groups/{id}/tags/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_tag_groups",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns the ID of the related template<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read` `templates:read`
            {
                "name": "get_campaign_message_relationships_template",
                "table_name": "template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaign-messages/{id}/relationships/template/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the ID of the related template<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `templates:read`
            {
                "name": "get_flow_message_relationships_template",
                "table_name": "template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-messages/{id}/relationships/template/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return the related template<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `campaigns:read` `templates:read`
            {
                "name": "get_campaign_message_template",
                "table_name": "template_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/campaign-messages/{id}/template/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[template]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Return the related template<br><br>*Rate limits*:<br>Burst: `3/s`<br>Steady: `60/m`  **Scopes:** `templates:read`
            {
                "name": "get_flow_message_template",
                "table_name": "template_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/flow-messages/{id}/template/",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields[template]": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get all templates in an account.  Filter to request a subset of all templates. Templates can be sorted by the following fields, in ascending and descending order: `id`, `name`, `created`, `updated`  Returns a maximum of 10 results per page.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `templates:read`
            {
                "name": "get_templates",
                "table_name": "template_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/templates/",
                },
            },
            # Get a template with the given template ID.<br><br>*Rate limits*:<br>Burst: `10/s`<br>Steady: `150/m`  **Scopes:** `templates:read`
            {
                "name": "get_template",
                "table_name": "template_response_object_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/api/templates/{id}/",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_templates",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields[template]": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
