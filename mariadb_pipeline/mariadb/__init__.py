from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="mariadb_source", max_table_nesting=2)
def mariadb_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "get_billingv_1_account",
                "table_name": "account",
                "endpoint": {
                    "path": "/billing/v1/account",
                    "paginator": "auto",
                },
            },
            # Retrieve the list of IPv4 addresses and netblocks in the allowlist for the specified service.
            {
                "name": "get_provisioningv_1_servicesservice_idsecurityallowlist",
                "table_name": "allowlist",
                "endpoint": {
                    "path": "/provisioning/v1/services/{service_id}/security/allowlist",
                    "params": {
                        "service_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available hardware architectures for the specified cloud provider and specified topology.
            {
                "name": "get_provisioningv_1_architectures",
                "table_name": "architecture",
                "endpoint": {
                    "path": "/provisioning/v1/architectures",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of custom configurations (Configuration Manager) available to the user/team.
            {
                "name": "get_provisioningv_1_configs",
                "table_name": "config",
                "endpoint": {
                    "path": "/provisioning/v1/configs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                        # "include_default": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a custom configuration (Configuration Manager) and its values.
            {
                "name": "get_provisioningv_1_configsconfig_id",
                "table_name": "config",
                "endpoint": {
                    "path": "/provisioning/v1/configs/{config_id}",
                    "params": {
                        "config_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available configuration parameters and values (Configuration Manager) for the specified topology.
            {
                "name": "get_provisioningv_1_topologiestopology_nameconfigs",
                "table_name": "config",
                "endpoint": {
                    "path": "/provisioning/v1/topologies/{topology_name}/configs",
                    "params": {
                        "topology_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_localecountry",
                "table_name": "country",
                "endpoint": {
                    "path": "/billing/v1/locale/country",
                    "params": {
                        # the parameters below can optionally be configured
                        # "active": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available hardware architectures for the specified cloud provider and specified topology.
            {
                "name": "get_provisioningv_1_cpu_architectures",
                "table_name": "cpu_architecture",
                "endpoint": {
                    "path": "/provisioning/v1/cpu-architectures",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the default credentials for the service. These credentials are not intended for long-term use, but should be replaced with credentials of your own choosing using a MariaDB client.
            {
                "name": "get_provisioningv_1_servicesservice_idsecuritycredentials",
                "table_name": "credential",
                "endpoint": {
                    "path": "/provisioning/v1/services/{service_id}/security/credentials",
                    "params": {
                        "service_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_pricesendpoint",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/billing/v1/prices/endpoint",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "product": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                        # "tier": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of entitlements for the current organization.
            {
                "name": "get_provisioningv_1_entitlements",
                "table_name": "entitlement",
                "endpoint": {
                    "path": "/provisioning/v1/entitlements",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_entitlements",
                "table_name": "entitlement",
                "endpoint": {
                    "path": "/billing/v1/entitlements",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_pricesinstance",
                "table_name": "instance",
                "endpoint": {
                    "path": "/billing/v1/prices/instance",
                    "params": {
                        # the parameters below can optionally be configured
                        # "arch": "OPTIONAL_CONFIG",
                        # "provider": "OPTIONAL_CONFIG",
                        # "product": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_invoices",
                "table_name": "invoice",
                "endpoint": {
                    "path": "/billing/v1/invoices",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_invoicesinvoice_uid",
                "table_name": "invoice",
                "endpoint": {
                    "path": "/billing/v1/invoices/{invoice_uid}",
                    "params": {
                        "invoice_uid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available IOPS settings for the specified cloud provider.
            {
                "name": "get_provisioningv_1_providersprovider_nameiops",
                "table_name": "iop",
                "endpoint": {
                    "path": "/provisioning/v1/providers/{provider_name}/iops",
                    "params": {
                        "provider_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_pricesiops",
                "table_name": "iop",
                "endpoint": {
                    "path": "/billing/v1/prices/iops",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "product": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                        # "tier": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available maintenance windows
            {
                "name": "get_provisioningv_1_maintenance_windows",
                "table_name": "maintenance_window",
                "endpoint": {
                    "path": "/provisioning/v1/maintenance-windows",
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available node options for the specified topology.
            {
                "name": "get_provisioningv_1_topologiestopology_namenodes",
                "table_name": "node",
                "endpoint": {
                    "path": "/provisioning/v1/topologies/{topology_name}/nodes",
                    "params": {
                        "topology_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available options (features) for the specified topology.
            {
                "name": "get_provisioningv_1_topologiestopology_nameoptions",
                "table_name": "option",
                "endpoint": {
                    "path": "/provisioning/v1/topologies/{topology_name}/options",
                    "params": {
                        "topology_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_usagepreview",
                "table_name": "preview",
                "endpoint": {
                    "path": "/billing/v1/usage/preview",
                    "params": {
                        # the parameters below can optionally be configured
                        # "start_date": "OPTIONAL_CONFIG",
                        # "end_date": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_prices",
                "table_name": "price",
                "endpoint": {
                    "path": "/billing/v1/prices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "arch": "OPTIONAL_CONFIG",
                        # "provider": "OPTIONAL_CONFIG",
                        # "product": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of products available in the specified topology.
            {
                "name": "get_provisioningv_1_products",
                "table_name": "product",
                "endpoint": {
                    "path": "/provisioning/v1/products",
                    "params": {
                        # the parameters below can optionally be configured
                        # "topology_id": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_paymentprofile",
                "table_name": "profile",
                "endpoint": {
                    "path": "/billing/v1/payment/profile",
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available cloud providers.
            {
                "name": "get_provisioningv_1_providers",
                "table_name": "provider",
                "endpoint": {
                    "path": "/provisioning/v1/providers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "name": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_publicservicesouspublic_keykey_version",
                "table_name": "public_key",
                "endpoint": {
                    "path": "/public/services/ous/public-key/{key_version}",
                    "params": {
                        "key_version": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available geographic regions for a cloud provider.
            {
                "name": "get_provisioningv_1_regions",
                "table_name": "region",
                "endpoint": {
                    "path": "/provisioning/v1/regions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of services that are replicas for the specified service.
            {
                "name": "get_provisioningv_1_servicesservice_idreplicas",
                "table_name": "replica",
                "endpoint": {
                    "path": "/provisioning/v1/services/{service_id}/replicas",
                    "params": {
                        "service_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of services managed by the user/team.
            {
                "name": "get_provisioningv_1_services",
                "table_name": "service",
                "endpoint": {
                    "path": "/provisioning/v1/services",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the information and status of the specified service.
            {
                "name": "get_provisioningv_1_servicesservice_id",
                "table_name": "service",
                "endpoint": {
                    "path": "/provisioning/v1/services/{service_id}",
                    "params": {
                        "service_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_usageservice",
                "table_name": "service",
                "endpoint": {
                    "path": "/billing/v1/usage/service",
                    "params": {
                        # the parameters below can optionally be configured
                        # "start_date": "OPTIONAL_CONFIG",
                        # "end_date": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_usageserviceservice_id",
                "table_name": "service",
                "endpoint": {
                    "path": "/billing/v1/usage/service/{service_id}",
                    "params": {
                        "service_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "start_date": "OPTIONAL_CONFIG",
                        # "end_date": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available service types.
            {
                "name": "get_provisioningv_1_service_types",
                "table_name": "service_type",
                "endpoint": {
                    "path": "/provisioning/v1/service-types",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available node sizes.
            {
                "name": "get_provisioningv_1_sizes",
                "table_name": "size",
                "endpoint": {
                    "path": "/provisioning/v1/sizes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "architecture": "OPTIONAL_CONFIG",
                        # "service_type": "OPTIONAL_CONFIG",
                        # "provider": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_localestate_province",
                "table_name": "state_province",
                "endpoint": {
                    "path": "/billing/v1/locale/state-province",
                    "params": {
                        # the parameters below can optionally be configured
                        # "active": "OPTIONAL_CONFIG",
                        # "country": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_pricesstorage",
                "table_name": "storage",
                "endpoint": {
                    "path": "/billing/v1/prices/storage",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "product": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                        # "tier": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available storage sizes for the specified topology.
            {
                "name": "get_provisioningv_1_topologiestopology_namestorage_sizes",
                "table_name": "storage_size",
                "endpoint": {
                    "path": "/provisioning/v1/topologies/{topology_name}/storage-sizes",
                    "params": {
                        "topology_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_billingv_1_pricesthroughput",
                "table_name": "throughput",
                "endpoint": {
                    "path": "/billing/v1/prices/throughput",
                    "params": {
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "product": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                        # "tier": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available tiers and the topologies they support.
            {
                "name": "get_provisioningv_1_tiers",
                "table_name": "tier",
                "endpoint": {
                    "path": "/provisioning/v1/tiers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available topologies for the specified service type.
            {
                "name": "get_provisioningv_1_topologies",
                "table_name": "topology",
                "endpoint": {
                    "path": "/provisioning/v1/topologies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "service_type": "OPTIONAL_CONFIG",
                        # "only_legacy": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the selected values for the given configuration ID.
            {
                "name": "get_provisioningv_1_configsconfig_idvalues",
                "table_name": "value",
                "endpoint": {
                    "path": "/provisioning/v1/configs/{config_id}/values",
                    "params": {
                        "config_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available software versions.
            {
                "name": "get_provisioningv_1_versions",
                "table_name": "version",
                "endpoint": {
                    "path": "/provisioning/v1/versions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                        # "topology": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of available storage volume types for the specified cloud provider.
            {
                "name": "get_provisioningv_1_providersprovider_namevolume_types",
                "table_name": "volume_type",
                "endpoint": {
                    "path": "/provisioning/v1/providers/{provider_name}/volume-types",
                    "params": {
                        "provider_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of availability zones for a specific provider.
            {
                "name": "get_provisioningv_1_providersprovider_namezones",
                "table_name": "zone",
                "endpoint": {
                    "path": "/provisioning/v1/providers/{provider_name}/zones",
                    "params": {
                        "provider_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "region": "OPTIONAL_CONFIG",
                        # "provider": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of zones for specific region
            {
                "name": "get_provisioningv_1_regionsregion_namezones",
                "table_name": "zone",
                "endpoint": {
                    "path": "/provisioning/v1/regions/{region_name}/zones",
                    "params": {
                        "region_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "provider": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                        # "page_order": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
