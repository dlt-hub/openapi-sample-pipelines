# mariadb pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/mariadb.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /billing/v1/account_ 
  *resource*: get_billingv_1_account  
* _GET /provisioning/v1/services/{service_id}/security/allowlist_ 
  *resource*: get_provisioningv_1_servicesservice_idsecurityallowlist  
  *description*: Retrieve the list of IPv4 addresses and netblocks in the allowlist for the specified service.
* _GET /provisioning/v1/architectures_ 
  *resource*: get_provisioningv_1_architectures  
  *description*: Retrieve a list of available hardware architectures for the specified cloud provider and specified topology.
* _GET /provisioning/v1/configs_ 
  *resource*: get_provisioningv_1_configs  
  *description*: Retrieve a list of custom configurations (Configuration Manager) available to the user/team.
* _GET /provisioning/v1/configs/{config_id}_ 
  *resource*: get_provisioningv_1_configsconfig_id  
  *description*: Retrieve a custom configuration (Configuration Manager) and its values.
* _GET /provisioning/v1/topologies/{topology_name}/configs_ 
  *resource*: get_provisioningv_1_topologiestopology_nameconfigs  
  *description*: Retrieve a list of available configuration parameters and values (Configuration Manager) for the specified topology.
* _GET /billing/v1/locale/country_ 
  *resource*: get_billingv_1_localecountry  
* _GET /provisioning/v1/cpu-architectures_ 
  *resource*: get_provisioningv_1_cpu_architectures  
  *description*: Retrieve a list of available hardware architectures for the specified cloud provider and specified topology.
* _GET /provisioning/v1/services/{service_id}/security/credentials_ 
  *resource*: get_provisioningv_1_servicesservice_idsecuritycredentials  
  *description*: Retrieve the default credentials for the service. These credentials are not intended for long-term use, but should be replaced with credentials of your own choosing using a MariaDB client.
* _GET /billing/v1/prices/endpoint_ 
  *resource*: get_billingv_1_pricesendpoint  
* _GET /provisioning/v1/entitlements_ 
  *resource*: get_provisioningv_1_entitlements  
  *description*: Retrieve a list of entitlements for the current organization.
* _GET /billing/v1/entitlements_ 
  *resource*: get_billingv_1_entitlements  
* _GET /billing/v1/prices/instance_ 
  *resource*: get_billingv_1_pricesinstance  
* _GET /billing/v1/invoices_ 
  *resource*: get_billingv_1_invoices  
* _GET /billing/v1/invoices/{invoice_uid}_ 
  *resource*: get_billingv_1_invoicesinvoice_uid  
* _GET /provisioning/v1/providers/{provider_name}/iops_ 
  *resource*: get_provisioningv_1_providersprovider_nameiops  
  *description*: Retrieve a list of available IOPS settings for the specified cloud provider.
* _GET /billing/v1/prices/iops_ 
  *resource*: get_billingv_1_pricesiops  
* _GET /provisioning/v1/maintenance-windows_ 
  *resource*: get_provisioningv_1_maintenance_windows  
  *description*: Retrieve a list of available maintenance windows
* _GET /provisioning/v1/topologies/{topology_name}/nodes_ 
  *resource*: get_provisioningv_1_topologiestopology_namenodes  
  *description*: Retrieve a list of available node options for the specified topology.
* _GET /provisioning/v1/topologies/{topology_name}/options_ 
  *resource*: get_provisioningv_1_topologiestopology_nameoptions  
  *description*: Retrieve a list of available options (features) for the specified topology.
* _GET /billing/v1/usage/preview_ 
  *resource*: get_billingv_1_usagepreview  
* _GET /billing/v1/prices_ 
  *resource*: get_billingv_1_prices  
* _GET /provisioning/v1/products_ 
  *resource*: get_provisioningv_1_products  
  *description*: Retrieve a list of products available in the specified topology.
* _GET /billing/v1/payment/profile_ 
  *resource*: get_billingv_1_paymentprofile  
* _GET /provisioning/v1/providers_ 
  *resource*: get_provisioningv_1_providers  
  *description*: Retrieve a list of available cloud providers.
* _GET /public/services/ous/public-key/{key_version}_ 
  *resource*: get_publicservicesouspublic_keykey_version  
* _GET /provisioning/v1/regions_ 
  *resource*: get_provisioningv_1_regions  
  *description*: Retrieve a list of available geographic regions for a cloud provider.
* _GET /provisioning/v1/services/{service_id}/replicas_ 
  *resource*: get_provisioningv_1_servicesservice_idreplicas  
  *description*: Retrieve a list of services that are replicas for the specified service.
* _GET /provisioning/v1/services_ 
  *resource*: get_provisioningv_1_services  
  *description*: Retrieve a list of services managed by the user/team.
* _GET /provisioning/v1/services/{service_id}_ 
  *resource*: get_provisioningv_1_servicesservice_id  
  *description*: Retrieve the information and status of the specified service.
* _GET /billing/v1/usage/service_ 
  *resource*: get_billingv_1_usageservice  
* _GET /billing/v1/usage/service/{service_id}_ 
  *resource*: get_billingv_1_usageserviceservice_id  
* _GET /provisioning/v1/service-types_ 
  *resource*: get_provisioningv_1_service_types  
  *description*: Retrieve a list of available service types.
* _GET /provisioning/v1/sizes_ 
  *resource*: get_provisioningv_1_sizes  
  *description*: Retrieve a list of available node sizes.
* _GET /billing/v1/locale/state-province_ 
  *resource*: get_billingv_1_localestate_province  
* _GET /billing/v1/prices/storage_ 
  *resource*: get_billingv_1_pricesstorage  
* _GET /provisioning/v1/topologies/{topology_name}/storage-sizes_ 
  *resource*: get_provisioningv_1_topologiestopology_namestorage_sizes  
  *description*: Retrieve a list of available storage sizes for the specified topology.
* _GET /billing/v1/prices/throughput_ 
  *resource*: get_billingv_1_pricesthroughput  
* _GET /provisioning/v1/tiers_ 
  *resource*: get_provisioningv_1_tiers  
  *description*: Retrieve a list of available tiers and the topologies they support.
* _GET /provisioning/v1/topologies_ 
  *resource*: get_provisioningv_1_topologies  
  *description*: Retrieve a list of available topologies for the specified service type.
* _GET /provisioning/v1/configs/{config_id}/values_ 
  *resource*: get_provisioningv_1_configsconfig_idvalues  
  *description*: Retrieve the selected values for the given configuration ID.
* _GET /provisioning/v1/versions_ 
  *resource*: get_provisioningv_1_versions  
  *description*: Retrieve a list of available software versions.
* _GET /provisioning/v1/providers/{provider_name}/volume-types_ 
  *resource*: get_provisioningv_1_providersprovider_namevolume_types  
  *description*: Retrieve a list of available storage volume types for the specified cloud provider.
* _GET /provisioning/v1/providers/{provider_name}/zones_ 
  *resource*: get_provisioningv_1_providersprovider_namezones  
  *description*: Retrieve a list of availability zones for a specific provider.
* _GET /provisioning/v1/regions/{region_name}/zones_ 
  *resource*: get_provisioningv_1_regionsregion_namezones  
  *description*: Retrieve a list of zones for specific region
