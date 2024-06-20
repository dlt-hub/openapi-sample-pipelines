# cisco_meraki pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/cisco_meraki.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /networks/{networkId}/switch/accessControlLists_ 
  *resource*: get_network_switch_access_control_lists  
  *description*: Return the access control lists for a MS network
* _GET /networks/{networkId}/switch/accessPolicies_ 
  *resource*: get_network_switch_access_policies  
  *description*: List the access policies for a switch network. Only returns access policies with 'my RADIUS server' as authentication method
* _GET /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}_ 
  *resource*: get_network_switch_access_policy  
  *description*: Return a specific access policy for a switch network
* _GET /organizations/{organizationId}/adaptivePolicy/acls_ 
  *resource*: get_organization_adaptive_policy_acls  
  *description*: List adaptive policy ACLs in a organization
* _GET /organizations/{organizationId}/adaptivePolicy/acls/{aclId}_ 
  *resource*: get_organization_adaptive_policy_acl  
  *description*: Returns the adaptive policy ACL information
* _GET /organizations/{organizationId}/actionBatches_ 
  *resource*: get_organization_action_batches  
  *description*: Return the list of action batches in the organization
* _GET /organizations/{organizationId}/actionBatches/{actionBatchId}_ 
  *resource*: get_organization_action_batch  
  *description*: Return an action batch
* _GET /organizations/{organizationId}/admins_ 
  *resource*: get_organization_admins  
  *description*: List the dashboard administrators in this organization
* _GET /networks/{networkId}/wireless/airMarshal_ 
  *resource*: get_network_wireless_air_marshal  
  *description*: List Air Marshal scan results from a network
* _GET /networks/{networkId}/health/alerts_ 
  *resource*: get_network_health_alerts  
  *description*: Return all global alerts on this network
* _GET /organizations/{organizationId}/webhooks/alertTypes_ 
  *resource*: get_organization_webhooks_alert_types  
  *description*: Return a list of alert types to be used with managing webhook alerts
* _GET /networks/{networkId}/switch/alternateManagementInterface_ 
  *resource*: get_network_switch_alternate_management_interface  
  *description*: Return the switch alternate management interface for the network
* _GET /networks/{networkId}/wireless/alternateManagementInterface_ 
  *resource*: get_network_wireless_alternate_management_interface  
  *description*: Return alternate management interface and devices with IP assigned
* _GET /organizations/{organizationId}/apiRequests_ 
  *resource*: get_organization_api_requests  
  *description*: List the API requests made by an organization
* _GET /organizations/{organizationId}/sm/apnsCert_ 
  *resource*: get_organization_sm_apns_cert  
  *description*: Get the organization's APNS certificate
* _GET /organizations/{organizationId}/insight/applications_ 
  *resource*: get_organization_insight_applications  
  *description*: List all Insight tracked applications
* _GET /networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories_ 
  *resource*: get_network_appliance_firewall_l7_firewall_rules_application_categories  
  *description*: Return the L7 firewall application categories and their associated applications for an MX network
* _GET /networks/{networkId}/trafficShaping/applicationCategories_ 
  *resource*: get_network_traffic_shaping_application_categories  
  *description*: Returns the application categories for traffic shaping rules.
* _GET /networks/{networkId}/clients/applicationUsage_ 
  *resource*: get_network_clients_application_usage  
  *description*: Return the application usage data for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.
* _GET /organizations/{organizationId}/camera/customAnalytics/artifacts_ 
  *resource*: get_organization_camera_custom_analytics_artifacts  
  *description*: List Custom Analytics Artifacts
* _GET /organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId}_ 
  *resource*: get_organization_camera_custom_analytics_artifact  
  *description*: Get Custom Analytics Artifact
* _GET /organizations/{organizationId}/devices/availabilities_ 
  *resource*: get_organization_devices_availabilities  
  *description*: List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.
* _GET /networks/{networkId}/clients/bandwidthUsageHistory_ 
  *resource*: get_network_clients_bandwidth_usage_history  
  *description*: Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.
* _GET /organizations/{organizationId}/clients/bandwidthUsageHistory_ 
  *resource*: get_organization_clients_bandwidth_usage_history  
  *description*: Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.
* _GET /networks/{networkId}/appliance/vpn/bgp_ 
  *resource*: get_network_appliance_vpn_bgp  
  *description*: Return a Hub BGP Configuration
* _GET /networks/{networkId}/wireless/billing_ 
  *resource*: get_network_wireless_billing  
  *description*: Return the billing settings of this network
* _GET /networks/{networkId}/bluetoothClients_ 
  *resource*: get_network_bluetooth_clients  
  *description*: List the Bluetooth clients seen by APs in this network
* _GET /networks/{networkId}/bluetoothClients/{bluetoothClientId}_ 
  *resource*: get_network_bluetooth_client  
  *description*: Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.
* _GET /networks/{networkId}/wireless/ssids/{number}/bonjourForwarding_ 
  *resource*: get_network_wireless_ssid_bonjour_forwarding  
  *description*: List the Bonjour forwarding setting and rules for the SSID
* _GET /organizations/{organizationId}/brandingPolicies_ 
  *resource*: get_organization_branding_policies  
  *description*: List the branding policies of an organization
* _GET /organizations/{organizationId}/brandingPolicies/{brandingPolicyId}_ 
  *resource*: get_organization_branding_policy  
  *description*: Return a branding policy
* _GET /networks/{networkId}/policies/byClient_ 
  *resource*: get_network_policies_by_client  
  *description*: Get policies for all clients with policies
* _GET /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice_ 
  *resource*: get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device  
  *description*: Return the devices that have a Dynamic ARP Inspection warning and their warnings
* _GET /organizations/{organizationId}/devices/powerModules/statuses/byDevice_ 
  *resource*: get_organization_devices_power_modules_statuses_by_device  
  *description*: List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.
* _GET /organizations/{organizationId}/devices/uplinks/addresses/byDevice_ 
  *resource*: get_organization_devices_uplinks_addresses_by_device  
  *description*: List the current uplink addresses for devices in an organization.
* _GET /organizations/{organizationId}/firmware/upgrades/byDevice_ 
  *resource*: get_organization_firmware_upgrades_by_device  
  *description*: Get firmware upgrade status for the filtered devices
* _GET /organizations/{organizationId}/summary/top/switches/byEnergyUsage_ 
  *resource*: get_organization_summary_top_switches_by_energy_usage  
  *description*: Return metrics for organization's top 10 switches by energy usage over given time range. Default unit is joules.
* _GET /organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval_ 
  *resource*: get_organization_api_requests_overview_response_codes_by_interval  
  *description*: Tracks organizations' API requests by response code across a given time period
* _GET /networks/{networkId}/sensor/alerts/current/overview/byMetric_ 
  *resource*: get_network_sensor_alerts_current_overview_by_metric  
  *description*: Return an overview of currently alerting sensors by metric
* _GET /networks/{networkId}/sensor/alerts/overview/byMetric_ 
  *resource*: get_network_sensor_alerts_overview_by_metric  
  *description*: Return an overview of alert occurrences over a timespan, by metric
* _GET /organizations/{organizationId}/switch/ports/bySwitch_ 
  *resource*: get_organization_switch_ports_by_switch  
  *description*: List the switchports in an organization by switch
* _GET /organizations/{organizationId}/summary/top/clients/byUsage_ 
  *resource*: get_organization_summary_top_clients_by_usage  
  *description*: Return metrics for organization's top 10 clients by data usage (in mb) over given time range.
* _GET /organizations/{organizationId}/summary/top/clients/manufacturers/byUsage_ 
  *resource*: get_organization_summary_top_clients_manufacturers_by_usage  
  *description*: Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.
* _GET /organizations/{organizationId}/summary/top/devices/byUsage_ 
  *resource*: get_organization_summary_top_devices_by_usage  
  *description*: Return metrics for organization's top 10 devices sorted by data usage over given time range. Default unit is megabytes.
* _GET /organizations/{organizationId}/summary/top/devices/models/byUsage_ 
  *resource*: get_organization_summary_top_devices_models_by_usage  
  *description*: Return metrics for organization's top 10 device models sorted by data usage over given time range. Default unit is megabytes.
* _GET /organizations/{organizationId}/summary/top/ssids/byUsage_ 
  *resource*: get_organization_summary_top_ssids_by_usage  
  *description*: Return metrics for organization's top 10 ssids by data usage over given time range. Default unit is megabytes.
* _GET /organizations/{organizationId}/summary/top/appliances/byUtilization_ 
  *resource*: get_organization_summary_top_appliances_by_utilization  
  *description*: Return the top 10 appliances sorted by utilization over given time range.
* _GET /networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}_ 
  *resource*: get_network_sm_bypass_activation_lock_attempt  
  *description*: Bypass activation lock attempt status
* _GET /networks/{networkId}/appliance/contentFiltering/categories_ 
  *resource*: get_network_appliance_content_filtering_categories  
  *description*: List all available content filtering categories for an MX network
* _GET /networks/{networkId}/appliance/firewall/cellularFirewallRules_ 
  *resource*: get_network_appliance_firewall_cellular_firewall_rules  
  *description*: Return the cellular firewall rules for an MX network
* _GET /networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory_ 
  *resource*: get_network_sm_device_cellular_usage_history  
  *description*: Return the client's daily cellular data usage history. Usage data is in kilobytes.
* _GET /networks/{networkId}/sm/devices/{deviceId}/certs_ 
  *resource*: get_network_sm_device_certs  
  *description*: List the certs on a device
* _GET /networks/{networkId}/networkHealth/channelUtilization_ 
  *resource*: get_network_network_health_channel_utilization  
  *description*: Get the channel utilization over each radio for all APs in a network.
* _GET /networks/{networkId}/wireless/channelUtilizationHistory_ 
  *resource*: get_network_wireless_channel_utilization_history  
  *description*: Return AP channel utilization over time for a device or network client
* _GET /devices/{serial}/clients_ 
  *resource*: get_device_clients  
  *description*: List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.
* _GET /networks/{networkId}/clients_ 
  *resource*: get_network_clients  
  *description*: List the clients that have used this network in the timespan
* _GET /networks/{networkId}/clients/{clientId}_ 
  *resource*: get_network_client  
  *description*: Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
* _GET /networks/{networkId}/wireless/clientCountHistory_ 
  *resource*: get_network_wireless_client_count_history  
  *description*: Return wireless client counts over time for a network, device, or network client
* _GET /organizations/{organizationId}/configTemplates_ 
  *resource*: get_organization_config_templates  
  *description*: List the configuration templates for this organization
* _GET /organizations/{organizationId}/configTemplates/{configTemplateId}_ 
  *resource*: get_organization_config_template  
  *description*: Return a single configuration template
* _GET /organizations/{organizationId}/configurationChanges_ 
  *resource*: get_organization_configuration_changes  
  *description*: View the Change Log for your organization
* _GET /devices/{serial}/wireless/connectionStats_ 
  *resource*: get_device_wireless_connection_stats  
  *description*: Aggregated connectivity info for a given AP on this network
* _GET /networks/{networkId}/wireless/clients/connectionStats_ 
  *resource*: get_network_wireless_clients_connection_stats  
  *description*: Aggregated connectivity info for this network, grouped by clients
* _GET /networks/{networkId}/wireless/clients/{clientId}/connectionStats_ 
  *resource*: get_network_wireless_client_connection_stats  
  *description*: Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.
* _GET /networks/{networkId}/wireless/connectionStats_ 
  *resource*: get_network_wireless_connection_stats  
  *description*: Aggregated connectivity info for this network
* _GET /networks/{networkId}/wireless/devices/connectionStats_ 
  *resource*: get_network_wireless_devices_connection_stats  
  *description*: Aggregated connectivity info for this network, grouped by node
* _GET /networks/{networkId}/sm/devices/{deviceId}/connectivity_ 
  *resource*: get_network_sm_device_connectivity  
  *description*: Returns historical connectivity data (whether a device is regularly checking in to Dashboard).
* _GET /networks/{networkId}/wireless/clients/{clientId}/connectivityEvents_ 
  *resource*: get_network_wireless_client_connectivity_events  
  *description*: List the wireless connectivity events for a client within a network in the timespan.
* _GET /networks/{networkId}/appliance/connectivityMonitoringDestinations_ 
  *resource*: get_network_appliance_connectivity_monitoring_destinations  
  *description*: Return the connectivity testing destinations for an MX network
* _GET /networks/{networkId}/cellularGateway/connectivityMonitoringDestinations_ 
  *resource*: get_network_cellular_gateway_connectivity_monitoring_destinations  
  *description*: Return the connectivity testing destinations for an MG network
* _GET /networks/{networkId}/appliance/contentFiltering_ 
  *resource*: get_network_appliance_content_filtering  
  *description*: Return the content filtering settings for an MX network
* _GET /devices/{serial}/camera/customAnalytics_ 
  *resource*: get_device_camera_custom_analytics  
  *description*: Return custom analytics settings for a camera
* _GET /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses_ 
  *resource*: get_network_appliance_traffic_shaping_custom_performance_classes  
  *description*: List all custom performance classes for an MX network
* _GET /networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}_ 
  *resource*: get_network_appliance_traffic_shaping_custom_performance_class  
  *description*: Return a custom performance class for an MX network
* _GET /networks/{networkId}/wireless/dataRateHistory_ 
  *resource*: get_network_wireless_data_rate_history  
  *description*: Return PHY data rates over time for a network, device, or network client
* _GET /devices/{serial}/appliance/prefixes/delegated_ 
  *resource*: get_device_appliance_prefixes_delegated  
  *description*: Return current delegated IPv6 prefixes on an appliance.
* _GET /networks/{networkId}/sm/devices/{deviceId}/desktopLogs_ 
  *resource*: get_network_sm_device_desktop_logs  
  *description*: Return historical records of various Systems Manager network connection details for desktop devices.
* _GET /devices/{serial}_ 
  *resource*: get_device  
  *description*: Return a single device
* _GET /networks/{networkId}/devices_ 
  *resource*: get_network_devices  
  *description*: List the devices in a network
* _GET /networks/{networkId}/sm/devices_ 
  *resource*: get_network_sm_devices  
  *description*: List the devices enrolled in an SM network with various specified fields and filters
* _GET /organizations/{organizationId}/devices_ 
  *resource*: get_organization_devices  
  *description*: List the devices in an organization
* _GET /organizations/{organizationId}/inventory/devices_ 
  *resource*: get_organization_inventory_devices  
  *description*: Return the device inventory for an organization
* _GET /organizations/{organizationId}/inventory/devices/{serial}_ 
  *resource*: get_organization_inventory_device  
  *description*: Return a single device from the inventory of an organization
* _GET /networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs_ 
  *resource*: get_network_sm_device_device_command_logs  
  *description*: Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.
* _GET /networks/{networkId}/sm/devices/{deviceId}/deviceProfiles_ 
  *resource*: get_network_sm_device_device_profiles  
  *description*: Get the installed profiles associated with a device
* _GET /networks/{networkId}/sm/users/{userId}/deviceProfiles_ 
  *resource*: get_network_sm_user_device_profiles  
  *description*: Get the profiles associated with a user
* _GET /networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies_ 
  *resource*: get_network_wireless_ssid_device_type_group_policies  
  *description*: List the device type group policies for the SSID
* _GET /devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp_ 
  *resource*: get_device_switch_routing_interface_dhcp  
  *description*: Return a layer 3 interface DHCP configuration for a switch
* _GET /networks/{networkId}/cellularGateway/dhcp_ 
  *resource*: get_network_cellular_gateway_dhcp  
  *description*: List common DHCP settings of MGs
* _GET /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp_ 
  *resource*: get_network_switch_stack_routing_interface_dhcp  
  *description*: Return a layer 3 interface DHCP configuration for a switch stack
* _GET /networks/{networkId}/switch/dhcpServerPolicy_ 
  *resource*: get_network_switch_dhcp_server_policy  
  *description*: Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively
* _GET /networks/{networkId}/trafficShaping/dscpTaggingOptions_ 
  *resource*: get_network_traffic_shaping_dscp_tagging_options  
  *description*: Returns the available DSCP tagging options for your traffic shaping rules.
* _GET /networks/{networkId}/switch/dscpToCosMappings_ 
  *resource*: get_network_switch_dscp_to_cos_mappings  
  *description*: Return the DSCP to CoS mappings
* _GET /networks/{networkId}/wireless/ssids/{number}/eapOverride_ 
  *resource*: get_network_wireless_ssid_eap_override  
  *description*: Return the EAP overridden parameters for an SSID
* _GET /networks/{networkId}/appliance/clients/{clientId}/security/events_ 
  *resource*: get_network_appliance_client_security_events  
  *description*: List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
* _GET /networks/{networkId}/appliance/security/events_ 
  *resource*: get_network_appliance_security_events  
  *description*: List the security events for a network
* _GET /networks/{networkId}/events_ 
  *resource*: get_network_events  
  *description*: List the events for the network
* _GET /networks/{networkId}/firmwareUpgrades/staged/events_ 
  *resource*: get_network_firmware_upgrades_staged_events  
  *description*: Get the Staged Upgrade Event from a network
* _GET /organizations/{organizationId}/appliance/security/events_ 
  *resource*: get_organization_appliance_security_events  
  *description*: List the security events for an organization
* _GET /networks/{networkId}/events/eventTypes_ 
  *resource*: get_network_events_event_types  
  *description*: List the event type to human-readable description
* _GET /networks/{networkId}/wireless/failedConnections_ 
  *resource*: get_network_wireless_failed_connections  
  *description*: List of all failed client connection events on this network in a given time range
* _GET /organizations/{organizationId}/earlyAccess/features_ 
  *resource*: get_organization_early_access_features  
  *description*: List the available early access features for organization
* _GET /networks/{networkId}/appliance/firewall/firewalledServices_ 
  *resource*: get_network_appliance_firewall_firewalled_services  
  *description*: List the appliance services and their accessibility rules
* _GET /networks/{networkId}/appliance/firewall/firewalledServices/{service}_ 
  *resource*: get_network_appliance_firewall_firewalled_service  
  *description*: Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')
* _GET /networks/{networkId}/firmwareUpgrades_ 
  *resource*: get_network_firmware_upgrades  
  *description*: Get firmware upgrade information for a network
* _GET /networks/{networkId}/floorPlans_ 
  *resource*: get_network_floor_plans  
  *description*: List the floor plans that belong to your network
* _GET /networks/{networkId}/floorPlans/{floorPlanId}_ 
  *resource*: get_network_floor_plan  
  *description*: Find a floor plan by ID
* _GET /networks/{networkId}/firmwareUpgrades/staged/groups_ 
  *resource*: get_network_firmware_upgrades_staged_groups  
  *description*: List of Staged Upgrade Groups in a network
* _GET /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}_ 
  *resource*: get_network_firmware_upgrades_staged_group  
  *description*: Get a Staged Upgrade Group from a network
* _GET /organizations/{organizationId}/adaptivePolicy/groups_ 
  *resource*: get_organization_adaptive_policy_groups  
  *description*: List adaptive policy groups in a organization
* _GET /organizations/{organizationId}/adaptivePolicy/groups/{id}_ 
  *resource*: get_organization_adaptive_policy_group  
  *description*: Returns an adaptive policy group
* _GET /organizations/{organizationId}/policyObjects/groups_ 
  *resource*: get_organization_policy_objects_groups  
  *description*: Lists Policy Object Groups belonging to the organization.
* _GET /organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}_ 
  *resource*: get_organization_policy_objects_group  
  *description*: Shows details of a Policy Object Group.
* _GET /networks/{networkId}/groupPolicies_ 
  *resource*: get_network_group_policies  
  *description*: List the group policies in a network
* _GET /networks/{networkId}/groupPolicies/{groupPolicyId}_ 
  *resource*: get_network_group_policy  
  *description*: Display a group policy
* _GET /networks/{networkId}/insight/applications/{applicationId}/healthByTime_ 
  *resource*: get_network_insight_application_health_by_time  
  *description*: Get application health by time
* _GET /devices/{serial}/camera/analytics/zones/{zoneId}/history_ 
  *resource*: get_device_camera_analytics_zone_history  
  *description*: Return historical records for analytic zones
* _GET /networks/{networkId}/alerts/history_ 
  *resource*: get_network_alerts_history  
  *description*: Return the alert history for this network
* _GET /organizations/{organizationId}/sensor/readings/history_ 
  *resource*: get_organization_sensor_readings_history  
  *description*: Return all reported readings from sensors in a given timespan, sorted by timestamp
* _GET /networks/{networkId}/wireless/ssids/{number}/hotspot20_ 
  *resource*: get_network_wireless_ssid_hotspot_20  
  *description*: Return the Hotspot 2.0 settings for an SSID
* _GET /networks/{networkId}/webhooks/httpServers_ 
  *resource*: get_network_webhooks_http_servers  
  *description*: List the HTTP servers for a network
* _GET /networks/{networkId}/webhooks/httpServers/{httpServerId}_ 
  *resource*: get_network_webhooks_http_server  
  *description*: Return an HTTP server for a network
* _GET /networks/{networkId}/wireless/ssids/{number}/identityPsks_ 
  *resource*: get_network_wireless_ssid_identity_psks  
  *description*: List all Identity PSKs in a wireless network
* _GET /networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}_ 
  *resource*: get_network_wireless_ssid_identity_psk  
  *description*: Return an Identity PSK
* _GET /organizations/{organizationId}/saml/idps_ 
  *resource*: get_organization_saml_idps  
  *description*: List the SAML IdPs in your organization.
* _GET /organizations/{organizationId}/saml/idps/{idpId}_ 
  *resource*: get_organization_saml_idp  
  *description*: Get a SAML IdP from your organization.
* _GET /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports_ 
  *resource*: get_organization_inventory_onboarding_cloud_monitoring_imports  
  *description*: Check the status of a committed Import operation
* _GET /networks/{networkId}/appliance/firewall/inboundCellularFirewallRules_ 
  *resource*: get_network_appliance_firewall_inbound_cellular_firewall_rules  
  *description*: Return the inbound cellular firewall rules for an MX network
* _GET /networks/{networkId}/appliance/firewall/inboundFirewallRules_ 
  *resource*: get_network_appliance_firewall_inbound_firewall_rules  
  *description*: Return the inbound firewall rules for an MX network
* _GET /devices/{serial}/switch/routing/interfaces_ 
  *resource*: get_device_switch_routing_interfaces  
  *description*: List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.
* _GET /devices/{serial}/switch/routing/interfaces/{interfaceId}_ 
  *resource*: get_device_switch_routing_interface  
  *description*: Return a layer 3 interface for a switch
* _GET /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces_ 
  *resource*: get_network_switch_stack_routing_interfaces  
  *description*: List layer 3 interfaces for a switch stack
* _GET /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}_ 
  *resource*: get_network_switch_stack_routing_interface  
  *description*: Return a layer 3 interface from a switch stack
* _GET /networks/{networkId}/appliance/security/intrusion_ 
  *resource*: get_network_appliance_security_intrusion  
  *description*: Returns all supported intrusion settings for an MX network
* _GET /organizations/{organizationId}/appliance/security/intrusion_ 
  *resource*: get_organization_appliance_security_intrusion  
  *description*: Returns all supported intrusion settings for an organization
* _GET /networks/{networkId}/appliance/firewall/l3FirewallRules_ 
  *resource*: get_network_appliance_firewall_l3_firewall_rules  
  *description*: Return the L3 firewall rules for an MX network
* _GET /networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules_ 
  *resource*: get_network_wireless_ssid_firewall_l3_firewall_rules  
  *description*: Return the L3 firewall rules for an SSID on an MR network
* _GET /networks/{networkId}/appliance/firewall/l7FirewallRules_ 
  *resource*: get_network_appliance_firewall_l7_firewall_rules  
  *description*: List the MX L7 firewall rules for an MX network
* _GET /networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules_ 
  *resource*: get_network_wireless_ssid_firewall_l7_firewall_rules  
  *description*: Return the L7 firewall rules for an SSID on an MR network
* _GET /devices/{serial}/cellularGateway/lan_ 
  *resource*: get_device_cellular_gateway_lan  
  *description*: Show the LAN Settings of a MG
* _GET /networks/{networkId}/wireless/clients/{clientId}/latencyHistory_ 
  *resource*: get_network_wireless_client_latency_history  
  *description*: Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.
* _GET /networks/{networkId}/wireless/latencyHistory_ 
  *resource*: get_network_wireless_latency_history  
  *description*: Return average wireless latency over time for a network, device, or network client
* _GET /devices/{serial}/wireless/latencyStats_ 
  *resource*: get_device_wireless_latency_stats  
  *description*: Aggregated latency info for a given AP on this network
* _GET /networks/{networkId}/wireless/clients/latencyStats_ 
  *resource*: get_network_wireless_clients_latency_stats  
  *description*: Aggregated latency info for this network, grouped by clients
* _GET /networks/{networkId}/wireless/clients/{clientId}/latencyStats_ 
  *resource*: get_network_wireless_client_latency_stats  
  *description*: Aggregated latency info for a given client on this network. Clients are identified by their MAC.
* _GET /networks/{networkId}/wireless/devices/latencyStats_ 
  *resource*: get_network_wireless_devices_latency_stats  
  *description*: Aggregated latency info for this network, grouped by node
* _GET /networks/{networkId}/wireless/latencyStats_ 
  *resource*: get_network_wireless_latency_stats  
  *description*: Aggregated latency info for this network
* _GET /organizations/{organizationId}/sensor/readings/latest_ 
  *resource*: get_organization_sensor_readings_latest  
  *description*: Return the latest available reading for each metric from each sensor, sorted by sensor serial
* _GET /organizations/{organizationId}/licenses_ 
  *resource*: get_organization_licenses  
  *description*: List the licenses for an organization
* _GET /organizations/{organizationId}/licenses/{licenseId}_ 
  *resource*: get_organization_license  
  *description*: Display a license
* _GET /organizations/{organizationId}/licensing/coterm/licenses_ 
  *resource*: get_organization_licensing_coterm_licenses  
  *description*: List the licenses in a coterm organization
* _GET /networks/{networkId}/switch/linkAggregations_ 
  *resource*: get_network_switch_link_aggregations  
  *description*: List link aggregation groups
* _GET /networks/{networkId}/topology/linkLayer_ 
  *resource*: get_network_topology_link_layer  
  *description*: List the LLDP and CDP information for all discovered devices and connections in a network.
* _GET /devices/{serial}/camera/analytics/live_ 
  *resource*: get_device_camera_analytics_live  
  *description*: Returns live state from camera of analytics zones
* _GET /devices/{serial}/lldpCdp_ 
  *resource*: get_device_lldp_cdp  
  *description*: List LLDP and CDP information for a device
* _GET /organizations/{organizationId}/webhooks/logs_ 
  *resource*: get_organization_webhooks_logs  
  *description*: Return the log of webhook POSTs sent
* _GET /organizations/{organizationId}/loginSecurity_ 
  *resource*: get_organization_login_security  
  *description*: Returns the login security settings for an organization.
* _GET /devices/{serial}/lossAndLatencyHistory_ 
  *resource*: get_device_loss_and_latency_history  
  *description*: Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
* _GET /networks/{networkId}/appliance/security/malware_ 
  *resource*: get_network_appliance_security_malware  
  *description*: Returns all supported malware settings for an MX network
* _GET /devices/{serial}/managementInterface_ 
  *resource*: get_device_management_interface  
  *description*: Return the management interface settings for a device
* _GET /administered/identities/me_ 
  *resource*: get_administered_identities_me  
  *description*: Returns the identity of the current user.
* _GET /networks/{networkId}/merakiAuthUsers_ 
  *resource*: get_network_meraki_auth_users  
  *description*: List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)
* _GET /networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}_ 
  *resource*: get_network_meraki_auth_user  
  *description*: Return the Meraki Auth splash guest, RADIUS, or client VPN user
* _GET /networks/{networkId}/wireless/meshStatuses_ 
  *resource*: get_network_wireless_mesh_statuses  
  *description*: List wireless mesh statuses for repeaters
* _GET /organizations/{organizationId}/insight/monitoredMediaServers_ 
  *resource*: get_organization_insight_monitored_media_servers  
  *description*: List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.
* _GET /organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}_ 
  *resource*: get_organization_insight_monitored_media_server  
  *description*: Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.
* _GET /networks/{networkId}/mqttBrokers_ 
  *resource*: get_network_mqtt_brokers  
  *description*: List the MQTT brokers for this network
* _GET /networks/{networkId}/mqttBrokers/{mqttBrokerId}_ 
  *resource*: get_network_mqtt_broker  
  *description*: Return an MQTT broker
* _GET /networks/{networkId}/switch/mtu_ 
  *resource*: get_network_switch_mtu  
  *description*: Return the MTU configuration
* _GET /networks/{networkId}/switch/routing/multicast_ 
  *resource*: get_network_switch_routing_multicast  
  *description*: Return multicast settings for a network
* _GET /networks/{networkId}/netflow_ 
  *resource*: get_network_netflow  
  *description*: Return the NetFlow traffic reporting settings for a network
* _GET /networks/{networkId}_ 
  *resource*: get_network  
  *description*: Return a network
* _GET /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks_ 
  *resource*: get_organization_inventory_onboarding_cloud_monitoring_networks  
  *description*: Returns list of networks eligible for adding cloud monitored device
* _GET /organizations/{organizationId}/networks_ 
  *resource*: get_organization_networks  
  *description*: List the networks that the user has privileges on in an organization
* _GET /networks/{networkId}/sm/devices/{deviceId}/networkAdapters_ 
  *resource*: get_network_sm_device_network_adapters  
  *description*: List the network adapters of a device
* _GET /devices/{serial}/camera/sense/objectDetectionModels_ 
  *resource*: get_device_camera_sense_object_detection_models  
  *description*: Returns the MV Sense object detection model list for the given camera
* _GET /networks/{networkId}/appliance/firewall/oneToManyNatRules_ 
  *resource*: get_network_appliance_firewall_one_to_many_nat_rules  
  *description*: Return the 1:Many NAT mapping rules for an MX network
* _GET /networks/{networkId}/appliance/firewall/oneToOneNatRules_ 
  *resource*: get_network_appliance_firewall_one_to_one_nat_rules  
  *description*: Return the 1:1 NAT mapping rules for an MX network
* _GET /organizations/{organizationId}/openapiSpec_ 
  *resource*: get_organization_openapi_spec  
  *description*: Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON
* _GET /organizations/{organizationId}/earlyAccess/features/optIns_ 
  *resource*: get_organization_early_access_features_opt_ins  
  *description*: List the early access feature opt-ins for an organization
* _GET /organizations/{organizationId}/earlyAccess/features/optIns/{optInId}_ 
  *resource*: get_organization_early_access_features_opt_in  
  *description*: Show an early access feature opt-in for an organization
* _GET /networks/{networkId}/switch/qosRules/order_ 
  *resource*: get_network_switch_qos_rules_order  
  *description*: Return the quality of service rule IDs by order in which they will be processed by the switch
* _GET /organizations_ 
  *resource*: get_organizations  
  *description*: List the organizations that the user has privileges on
* _GET /organizations/{organizationId}_ 
  *resource*: get_organization  
  *description*: Return an organization
* _GET /networks/{networkId}/switch/routing/ospf_ 
  *resource*: get_network_switch_routing_ospf  
  *description*: Return layer 3 OSPF routing configuration
* _GET /devices/{serial}/camera/analytics/overview_ 
  *resource*: get_device_camera_analytics_overview  
  *description*: Returns an overview of aggregate analytics data for a timespan
* _GET /networks/{networkId}/clients/overview_ 
  *resource*: get_network_clients_overview  
  *description*: Return overview statistics for network clients
* _GET /organizations/{organizationId}/adaptivePolicy/overview_ 
  *resource*: get_organization_adaptive_policy_overview  
  *description*: Returns adaptive policy aggregate statistics for an organization
* _GET /organizations/{organizationId}/apiRequests/overview_ 
  *resource*: get_organization_api_requests_overview  
  *description*: Return an aggregated overview of API requests data
* _GET /organizations/{organizationId}/clients/overview_ 
  *resource*: get_organization_clients_overview  
  *description*: Return summary information around client data usage (in mb) across the given organization.
* _GET /organizations/{organizationId}/devices/statuses/overview_ 
  *resource*: get_organization_devices_statuses_overview  
  *description*: Return an overview of current device statuses
* _GET /organizations/{organizationId}/licenses/overview_ 
  *resource*: get_organization_licenses_overview  
  *description*: Return an overview of the license state for an organization
* _GET /devices/{serial}/switch/ports/statuses/packets_ 
  *resource*: get_device_switch_ports_statuses_packets  
  *description*: Return the packet counters for all the ports of a switch
* _GET /networks/{networkId}/webhooks/payloadTemplates_ 
  *resource*: get_network_webhooks_payload_templates  
  *description*: List the webhook payload templates for a network
* _GET /networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}_ 
  *resource*: get_network_webhooks_payload_template  
  *description*: Get the webhook payload template for a network
* _GET /devices/{serial}/appliance/performance_ 
  *resource*: get_device_appliance_performance  
  *description*: Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.
* _GET /networks/{networkId}/sm/devices/{deviceId}/performanceHistory_ 
  *resource*: get_network_sm_device_performance_history  
  *description*: Return historical records of various Systems Manager client metrics for desktop devices.
* _GET /networks/{networkId}/pii/piiKeys_ 
  *resource*: get_network_pii_pii_keys  
  *description*: List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/piiKeys ```
* _GET /devices/{serial}/liveTools/ping/{id}_ 
  *resource*: get_device_live_tools_ping  
  *description*: Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.
* _GET /devices/{serial}/liveTools/pingDevice/{id}_ 
  *resource*: get_device_live_tools_ping_device  
  *description*: Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.
* _GET /networks/{networkId}/clients/{clientId}/policy_ 
  *resource*: get_network_client_policy  
  *description*: Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
* _GET /organizations/{organizationId}/adaptivePolicy/policies_ 
  *resource*: get_organization_adaptive_policy_policies  
  *description*: List adaptive policies in an organization
* _GET /organizations/{organizationId}/adaptivePolicy/policies/{id}_ 
  *resource*: get_organization_adaptive_policy_policy  
  *description*: Return an adaptive policy
* _GET /organizations/{organizationId}/policyObjects_ 
  *resource*: get_organization_policy_objects  
  *description*: Lists Policy Objects belonging to the organization.
* _GET /organizations/{organizationId}/policyObjects/{policyObjectId}_ 
  *resource*: get_organization_policy_object  
  *description*: Shows details of a Policy Object.
* _GET /devices/{serial}/switch/ports_ 
  *resource*: get_device_switch_ports  
  *description*: List the switch ports for a switch
* _GET /devices/{serial}/switch/ports/{portId}_ 
  *resource*: get_device_switch_port  
  *description*: Return a switch port
* _GET /networks/{networkId}/appliance/ports_ 
  *resource*: get_network_appliance_ports  
  *description*: List per-port VLAN settings for all ports of a MX.
* _GET /networks/{networkId}/appliance/ports/{portId}_ 
  *resource*: get_network_appliance_port  
  *description*: Return per-port VLAN settings for a single MX port.
* _GET /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports_ 
  *resource*: get_organization_config_template_switch_profile_ports  
  *description*: Return all the ports of a switch profile
* _GET /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}_ 
  *resource*: get_organization_config_template_switch_profile_port  
  *description*: Return a switch profile port
* _GET /devices/{serial}/cellularGateway/portForwardingRules_ 
  *resource*: get_device_cellular_gateway_port_forwarding_rules  
  *description*: Returns the port forwarding rules for a single MG.
* _GET /networks/{networkId}/appliance/firewall/portForwardingRules_ 
  *resource*: get_network_appliance_firewall_port_forwarding_rules  
  *description*: Return the port forwarding rules for an MX network
* _GET /networks/{networkId}/switch/portSchedules_ 
  *resource*: get_network_switch_port_schedules  
  *description*: List switch port schedules
* _GET /organizations/{organizationId}/brandingPolicies/priorities_ 
  *resource*: get_organization_branding_policies_priorities  
  *description*: Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).
* _GET /networks/{networkId}/sensor/alerts/profiles_ 
  *resource*: get_network_sensor_alerts_profiles  
  *description*: Lists all sensor alert profiles for a network.
* _GET /networks/{networkId}/sensor/alerts/profiles/{id}_ 
  *resource*: get_network_sensor_alerts_profile  
  *description*: Show details of a sensor alert profile for a network.
* _GET /networks/{networkId}/sm/profiles_ 
  *resource*: get_network_sm_profiles  
  *description*: List all profiles in a network
* _GET /organizations/{organizationId}/alerts/profiles_ 
  *resource*: get_organization_alerts_profiles  
  *description*: List all organization-wide alert configurations
* _GET /organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles_ 
  *resource*: get_organization_config_template_switch_profiles  
  *description*: List the switch profiles for your switch template configuration
* _GET /networks/{networkId}/switch/qosRules_ 
  *resource*: get_network_switch_qos_rules  
  *description*: List quality of service rules
* _GET /networks/{networkId}/switch/qosRules/{qosRuleId}_ 
  *resource*: get_network_switch_qos_rule  
  *description*: Return a quality of service rule
* _GET /devices/{serial}/camera/qualityAndRetention_ 
  *resource*: get_device_camera_quality_and_retention  
  *description*: Returns quality and retention settings for the given camera
* _GET /networks/{networkId}/camera/qualityRetentionProfiles_ 
  *resource*: get_network_camera_quality_retention_profiles  
  *description*: List the quality retention profiles for this network
* _GET /networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}_ 
  *resource*: get_network_camera_quality_retention_profile  
  *description*: Retrieve a single quality retention profile
* _GET /devices/{serial}/camera/analytics/recent_ 
  *resource*: get_device_camera_analytics_recent  
  *description*: Returns most recent record for analytics zones
* _GET /devices/{serial}/sensor/relationships_ 
  *resource*: get_device_sensor_relationships  
  *description*: List the sensor roles for a given sensor or camera device.
* _GET /networks/{networkId}/sensor/relationships_ 
  *resource*: get_network_sensor_relationships  
  *description*: List the sensor roles for devices in a given network
* _GET /networks/{networkId}/switch/routing/multicast/rendezvousPoints_ 
  *resource*: get_network_switch_routing_multicast_rendezvous_points  
  *description*: List multicast rendezvous points
* _GET /networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}_ 
  *resource*: get_network_switch_routing_multicast_rendezvous_point  
  *description*: Return a multicast rendezvous point
* _GET /networks/{networkId}/pii/requests_ 
  *resource*: get_network_pii_requests  
  *description*: List the PII requests for this network or organization  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/requests ```
* _GET /networks/{networkId}/pii/requests/{requestId}_ 
  *resource*: get_network_pii_request  
  *description*: Return a PII request  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/requests/{requestId} ```
* _GET /networks/{networkId}/sm/devices/{deviceId}/restrictions_ 
  *resource*: get_network_sm_device_restrictions  
  *description*: List the restrictions on a device
* _GET /networks/{networkId}/wireless/rfProfiles_ 
  *resource*: get_network_wireless_rf_profiles  
  *description*: List the non-basic RF profiles for this network
* _GET /networks/{networkId}/wireless/rfProfiles/{rfProfileId}_ 
  *resource*: get_network_wireless_rf_profile  
  *description*: Return a RF profile
* _GET /networks/{networkId}/appliance/trafficShaping/rules_ 
  *resource*: get_network_appliance_traffic_shaping_rules  
  *description*: Display the traffic shaping settings rules for an MX network
* _GET /networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules_ 
  *resource*: get_network_wireless_ssid_traffic_shaping_rules  
  *description*: Display the traffic shaping settings for a SSID on an MR network
* _GET /organizations/{organizationId}/saml_ 
  *resource*: get_organization_saml  
  *description*: Returns the SAML SSO enabled settings for an organization.
* _GET /organizations/{organizationId}/samlRoles_ 
  *resource*: get_organization_saml_roles  
  *description*: List the SAML roles for this organization
* _GET /organizations/{organizationId}/samlRoles/{samlRoleId}_ 
  *resource*: get_organization_saml_role  
  *description*: Return a SAML role
* _GET /networks/{networkId}/camera/schedules_ 
  *resource*: get_network_camera_schedules  
  *description*: Returns a list of all camera recording schedules.
* _GET /networks/{networkId}/wireless/ssids/{number}/schedules_ 
  *resource*: get_network_wireless_ssid_schedules  
  *description*: List the outage schedule for the SSID
* _GET /organizations/{organizationId}/clients/search_ 
  *resource*: get_organization_clients_search  
  *description*: Return the client details in an organization
* _GET /networks/{networkId}/sm/devices/{deviceId}/securityCenters_ 
  *resource*: get_network_sm_device_security_centers  
  *description*: List the security centers on a device
* _GET /networks/{networkId}/switch/dhcp/v4/servers/seen_ 
  *resource*: get_network_switch_dhcp_v4_servers_seen  
  *description*: Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)
* _GET /devices/{serial}/camera/sense_ 
  *resource*: get_device_camera_sense  
  *description*: Returns sense settings for a given camera
* _GET /devices/{serial}/appliance/uplinks/settings_ 
  *resource*: get_device_appliance_uplinks_settings  
  *description*: Return the uplink settings for an MX appliance
* _GET /devices/{serial}/camera/video/settings_ 
  *resource*: get_device_camera_video_settings  
  *description*: Returns video settings for the given camera
* _GET /devices/{serial}/wireless/bluetooth/settings_ 
  *resource*: get_device_wireless_bluetooth_settings  
  *description*: Return the bluetooth settings for a wireless device
* _GET /devices/{serial}/wireless/radio/settings_ 
  *resource*: get_device_wireless_radio_settings  
  *description*: Return the radio settings of a device
* _GET /networks/{networkId}/alerts/settings_ 
  *resource*: get_network_alerts_settings  
  *description*: Return the alert configuration for this network
* _GET /networks/{networkId}/appliance/firewall/settings_ 
  *resource*: get_network_appliance_firewall_settings  
  *description*: Return the firewall settings for this network
* _GET /networks/{networkId}/appliance/settings_ 
  *resource*: get_network_appliance_settings  
  *description*: Return the appliance settings for a network
* _GET /networks/{networkId}/appliance/vlans/settings_ 
  *resource*: get_network_appliance_vlans_settings  
  *description*: Returns the enabled status of VLANs for the network
* _GET /networks/{networkId}/settings_ 
  *resource*: get_network_settings  
  *description*: Return the settings for a network
* _GET /networks/{networkId}/switch/settings_ 
  *resource*: get_network_switch_settings  
  *description*: Returns the switch network settings
* _GET /networks/{networkId}/wireless/bluetooth/settings_ 
  *resource*: get_network_wireless_bluetooth_settings  
  *description*: Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.
* _GET /networks/{networkId}/wireless/settings_ 
  *resource*: get_network_wireless_settings  
  *description*: Return the wireless settings for a network
* _GET /networks/{networkId}/wireless/ssids/{number}/splash/settings_ 
  *resource*: get_network_wireless_ssid_splash_settings  
  *description*: Display the splash page settings for the given SSID
* _GET /organizations/{organizationId}/adaptivePolicy/settings_ 
  *resource*: get_organization_adaptive_policy_settings  
  *description*: Returns global adaptive policy settings in an organization
* _GET /networks/{networkId}/wireless/signalQualityHistory_ 
  *resource*: get_network_wireless_signal_quality_history  
  *description*: Return signal quality (SNR/RSSI) over time for a device or network client
* _GET /devices/{serial}/cellular/sims_ 
  *resource*: get_device_cellular_sims  
  *description*: Return the SIM and APN configurations for a cellular device.
* _GET /networks/{networkId}/appliance/singleLan_ 
  *resource*: get_network_appliance_single_lan  
  *description*: Return single LAN configuration
* _GET /networks/{networkId}/appliance/vpn/siteToSiteVpn_ 
  *resource*: get_network_appliance_vpn_site_to_site_vpn  
  *description*: Return the site-to-site VPN settings of a network. Only valid for MX networks.
* _GET /networks/{networkId}/pii/smDevicesForKey_ 
  *resource*: get_network_pii_sm_devices_for_key  
  *description*: Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smDevicesForKey ```
* _GET /networks/{networkId}/pii/smOwnersForKey_ 
  *resource*: get_network_pii_sm_owners_for_key  
  *description*: Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smOwnersForKey ```
* _GET /networks/{networkId}/snmp_ 
  *resource*: get_network_snmp  
  *description*: Return the SNMP settings for a network
* _GET /organizations/{organizationId}/snmp_ 
  *resource*: get_organization_snmp  
  *description*: Return the SNMP settings for an organization
* _GET /networks/{networkId}/sm/devices/{deviceId}/softwares_ 
  *resource*: get_network_sm_device_softwares  
  *description*: Get a list of softwares associated with a device
* _GET /networks/{networkId}/sm/users/{userId}/softwares_ 
  *resource*: get_network_sm_user_softwares  
  *description*: Get a list of softwares associated with a user
* _GET /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus_ 
  *resource*: get_network_client_splash_authorization_status  
  *description*: Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
* _GET /networks/{networkId}/splashLoginAttempts_ 
  *resource*: get_network_splash_login_attempts  
  *description*: List the splash login attempts for a network
* _GET /networks/{networkId}/appliance/ssids_ 
  *resource*: get_network_appliance_ssids  
  *description*: List the MX SSIDs in a network
* _GET /networks/{networkId}/appliance/ssids/{number}_ 
  *resource*: get_network_appliance_ssid  
  *description*: Return a single MX SSID
* _GET /networks/{networkId}/wireless/ssids_ 
  *resource*: get_network_wireless_ssids  
  *description*: List the MR SSIDs in a network
* _GET /networks/{networkId}/wireless/ssids/{number}_ 
  *resource*: get_network_wireless_ssid  
  *description*: Return a single MR SSID
* _GET /networks/{networkId}/switch/stacks_ 
  *resource*: get_network_switch_stacks  
  *description*: List the switch stacks in a network
* _GET /networks/{networkId}/switch/stacks/{switchStackId}_ 
  *resource*: get_network_switch_stack  
  *description*: Show a switch stack
* _GET /networks/{networkId}/firmwareUpgrades/staged/stages_ 
  *resource*: get_network_firmware_upgrades_staged_stages  
  *description*: Order of Staged Upgrade Groups in a network
* _GET /organizations/{organizationId}/appliance/vpn/stats_ 
  *resource*: get_organization_appliance_vpn_stats  
  *description*: Show VPN history stat for networks in an organization
* _GET /networks/{networkId}/appliance/prefixes/delegated/statics_ 
  *resource*: get_network_appliance_prefixes_delegated_statics  
  *description*: List static delegated prefixes for a network
* _GET /networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}_ 
  *resource*: get_network_appliance_prefixes_delegated_static  
  *description*: Return a static delegated prefix from a network
* _GET /devices/{serial}/switch/routing/staticRoutes_ 
  *resource*: get_device_switch_routing_static_routes  
  *description*: List layer 3 static routes for a switch
* _GET /devices/{serial}/switch/routing/staticRoutes/{staticRouteId}_ 
  *resource*: get_device_switch_routing_static_route  
  *description*: Return a layer 3 static route for a switch
* _GET /networks/{networkId}/appliance/staticRoutes_ 
  *resource*: get_network_appliance_static_routes  
  *description*: List the static routes for an MX or teleworker network
* _GET /networks/{networkId}/appliance/staticRoutes/{staticRouteId}_ 
  *resource*: get_network_appliance_static_route  
  *description*: Return a static route for an MX or teleworker network
* _GET /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes_ 
  *resource*: get_network_switch_stack_routing_static_routes  
  *description*: List layer 3 static routes for a switch stack
* _GET /networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}_ 
  *resource*: get_network_switch_stack_routing_static_route  
  *description*: Return a layer 3 static route for a switch stack
* _GET /devices/{serial}/wireless/status_ 
  *resource*: get_device_wireless_status  
  *description*: Return the SSID statuses of an access point
* _GET /devices/{serial}/switch/ports/statuses_ 
  *resource*: get_device_switch_ports_statuses  
  *description*: Return the status for all the ports of a switch
* _GET /organizations/{organizationId}/appliance/uplink/statuses_ 
  *resource*: get_organization_appliance_uplink_statuses  
  *description*: List the uplink status of every Meraki MX and Z series appliances in the organization
* _GET /organizations/{organizationId}/appliance/vpn/statuses_ 
  *resource*: get_organization_appliance_vpn_statuses  
  *description*: Show VPN status for networks in an organization
* _GET /organizations/{organizationId}/camera/onboarding/statuses_ 
  *resource*: get_organization_camera_onboarding_statuses  
  *description*: Fetch onboarding status of cameras
* _GET /organizations/{organizationId}/cellularGateway/uplink/statuses_ 
  *resource*: get_organization_cellular_gateway_uplink_statuses  
  *description*: List the uplink status of every Meraki MG cellular gateway in the organization
* _GET /organizations/{organizationId}/devices/statuses_ 
  *resource*: get_organization_devices_statuses  
  *description*: List the status of every Meraki device in the organization
* _GET /organizations/{organizationId}/uplinks/statuses_ 
  *resource*: get_organization_uplinks_statuses  
  *description*: List the uplink status of every Meraki MX, MG and Z series devices in the organization
* _GET /organizations/{organizationId}/wireless/devices/ethernet/statuses_ 
  *resource*: get_organization_wireless_devices_ethernet_statuses  
  *description*: Endpoint to see power status for wireless devices
* _GET /networks/{networkId}/switch/stormControl_ 
  *resource*: get_network_switch_storm_control  
  *description*: Return the storm control configuration for a switch network
* _GET /networks/{networkId}/switch/stp_ 
  *resource*: get_network_switch_stp  
  *description*: Returns STP settings
* _GET /devices/{serial}/appliance/dhcp/subnets_ 
  *resource*: get_device_appliance_dhcp_subnets  
  *description*: Return the DHCP subnet information for an appliance
* _GET /networks/{networkId}/cellularGateway/subnetPool_ 
  *resource*: get_network_cellular_gateway_subnet_pool  
  *description*: Return the subnet pool and mask configured for MGs in the network.
* _GET /networks/{networkId}/syslogServers_ 
  *resource*: get_network_syslog_servers  
  *description*: List the syslog servers for a network
* _GET /networks/{networkId}/sm/targetGroups_ 
  *resource*: get_network_sm_target_groups  
  *description*: List the target groups in this network
* _GET /networks/{networkId}/sm/targetGroups/{targetGroupId}_ 
  *resource*: get_network_sm_target_group  
  *description*: Return a target group
* _GET /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers_ 
  *resource*: get_organization_appliance_vpn_third_party_vpn_peers  
  *description*: Return the third party VPN peers for an organization
* _GET /networks/{networkId}/traffic_ 
  *resource*: get_network_traffic  
  *description*: Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.
* _GET /networks/{networkId}/trafficAnalysis_ 
  *resource*: get_network_traffic_analysis  
  *description*: Return the traffic analysis settings for a network
* _GET /networks/{networkId}/clients/{clientId}/trafficHistory_ 
  *resource*: get_network_client_traffic_history  
  *description*: Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
* _GET /networks/{networkId}/appliance/trafficShaping_ 
  *resource*: get_network_appliance_traffic_shaping  
  *description*: Display the traffic shaping settings for an MX network
* _GET /networks/{networkId}/sm/trustedAccessConfigs_ 
  *resource*: get_network_sm_trusted_access_configs  
  *description*: List Trusted Access Configs
* _GET /networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers_ 
  *resource*: get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers  
  *description*: Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries
* _GET /organizations/{organizationId}/firmware/upgrades_ 
  *resource*: get_organization_firmware_upgrades  
  *description*: Get firmware upgrade information for an organization
* _GET /networks/{networkId}/cellularGateway/uplink_ 
  *resource*: get_network_cellular_gateway_uplink  
  *description*: Returns the uplink settings for your MG network.
* _GET /networks/{networkId}/appliance/trafficShaping/uplinkBandwidth_ 
  *resource*: get_network_appliance_traffic_shaping_uplink_bandwidth  
  *description*: Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device's hardware capabilities.  For more information on your device's hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]
* _GET /networks/{networkId}/appliance/trafficShaping/uplinkSelection_ 
  *resource*: get_network_appliance_traffic_shaping_uplink_selection  
  *description*: Show uplink selection settings for an MX network
* _GET /organizations/{organizationId}/devices/uplinksLossAndLatency_ 
  *resource*: get_organization_devices_uplinks_loss_and_latency  
  *description*: Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
* _GET /networks/{networkId}/appliance/uplinks/usageHistory_ 
  *resource*: get_network_appliance_uplinks_usage_history  
  *description*: Get the sent and received bytes for each uplink of a network.
* _GET /networks/{networkId}/clients/usageHistories_ 
  *resource*: get_network_clients_usage_histories  
  *description*: Return the usage histories for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.
* _GET /networks/{networkId}/clients/{clientId}/usageHistory_ 
  *resource*: get_network_client_usage_history  
  *description*: Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
* _GET /networks/{networkId}/wireless/usageHistory_ 
  *resource*: get_network_wireless_usage_history  
  *description*: Return AP usage over time for a device or network client
* _GET /networks/{networkId}/sm/users_ 
  *resource*: get_network_sm_users  
  *description*: List the owners in an SM network with various specified fields and filters
* _GET /networks/{networkId}/sm/userAccessDevices_ 
  *resource*: get_network_sm_user_access_devices  
  *description*: List User Access Devices and its Trusted Access Connections
* _GET /devices/{serial}/camera/videoLink_ 
  *resource*: get_device_camera_video_link  
  *description*: Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.
* _GET /networks/{networkId}/appliance/vlans_ 
  *resource*: get_network_appliance_vlans  
  *description*: List the VLANs for an MX network
* _GET /networks/{networkId}/appliance/vlans/{vlanId}_ 
  *resource*: get_network_appliance_vlan  
  *description*: Return a VLAN
* _GET /devices/{serial}/appliance/prefixes/delegated/vlanAssignments_ 
  *resource*: get_device_appliance_prefixes_delegated_vlan_assignments  
  *description*: Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
* _GET /networks/{networkId}/wireless/ssids/{number}/vpn_ 
  *resource*: get_network_wireless_ssid_vpn  
  *description*: List the VPN settings for the SSID.
* _GET /organizations/{organizationId}/appliance/vpn/vpnFirewallRules_ 
  *resource*: get_organization_appliance_vpn_vpn_firewall_rules  
  *description*: Return the firewall rules for an organization's site-to-site VPN
* _GET /organizations/{organizationId}/sm/vppAccounts_ 
  *resource*: get_organization_sm_vpp_accounts  
  *description*: List the VPP accounts in the organization
* _GET /organizations/{organizationId}/sm/vppAccounts/{vppAccountId}_ 
  *resource*: get_organization_sm_vpp_account  
  *description*: Get a hash containing the unparsed token of the VPP account with the given ID
* _GET /devices/{serial}/switch/warmSpare_ 
  *resource*: get_device_switch_warm_spare  
  *description*: Return warm spare configuration for a switch
* _GET /networks/{networkId}/appliance/warmSpare_ 
  *resource*: get_network_appliance_warm_spare  
  *description*: Return MX warm spare settings
* _GET /networks/{networkId}/webhooks/webhookTests/{webhookTestId}_ 
  *resource*: get_network_webhooks_webhook_test  
  *description*: Return the status of a webhook test for a network
* _GET /devices/{serial}/camera/wirelessProfiles_ 
  *resource*: get_device_camera_wireless_profiles  
  *description*: Returns wireless profile assigned to the given camera
* _GET /networks/{networkId}/camera/wirelessProfiles_ 
  *resource*: get_network_camera_wireless_profiles  
  *description*: List the camera wireless profiles for this network.
* _GET /networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId}_ 
  *resource*: get_network_camera_wireless_profile  
  *description*: Retrieve a single camera wireless profile.
* _GET /networks/{networkId}/sm/devices/{deviceId}/wlanLists_ 
  *resource*: get_network_sm_device_wlan_lists  
  *description*: List the saved SSID names on a device
* _GET /devices/{serial}/camera/analytics/zones_ 
  *resource*: get_device_camera_analytics_zones  
  *description*: Returns all configured analytic zones for this camera
