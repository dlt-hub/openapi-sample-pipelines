from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="cisco_meraki_source", max_table_nesting=2)
def cisco_meraki_source(
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
                "name": "X-Cisco-Meraki-API-Key",
                "location": "header",
            },
        },
        "resources": [
            # Return the access control lists for a MS network
            {
                "name": "get_network_switch_access_control_lists",
                "table_name": "access_control_list",
                "endpoint": {
                    "data_selector": "rules",
                    "path": "/networks/{networkId}/switch/accessControlLists",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the access policies for a switch network. Only returns access policies with 'my RADIUS server' as authentication method
            {
                "name": "get_network_switch_access_policies",
                "table_name": "access_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/accessPolicies",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a specific access policy for a switch network
            {
                "name": "get_network_switch_access_policy",
                "table_name": "access_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "accessPolicyNumber": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List adaptive policy ACLs in a organization
            {
                "name": "get_organization_adaptive_policy_acls",
                "table_name": "acl",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/acls",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the adaptive policy ACL information
            {
                "name": "get_organization_adaptive_policy_acl",
                "table_name": "acl",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/acls/{aclId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "aclId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the list of action batches in the organization
            {
                "name": "get_organization_action_batches",
                "table_name": "action_batch",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/actionBatches",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return an action batch
            {
                "name": "get_organization_action_batch",
                "table_name": "action_batch",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/actionBatches/{actionBatchId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "actionBatchId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the dashboard administrators in this organization
            {
                "name": "get_organization_admins",
                "table_name": "admin",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/admins",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List Air Marshal scan results from a network
            {
                "name": "get_network_wireless_air_marshal",
                "table_name": "air_marshal",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/airMarshal",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return all global alerts on this network
            {
                "name": "get_network_health_alerts",
                "table_name": "alert",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/health/alerts",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a list of alert types to be used with managing webhook alerts
            {
                "name": "get_organization_webhooks_alert_types",
                "table_name": "alert_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/webhooks/alertTypes",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "productType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the switch alternate management interface for the network
            {
                "name": "get_network_switch_alternate_management_interface",
                "table_name": "alternate_management_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/alternateManagementInterface",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return alternate management interface and devices with IP assigned
            {
                "name": "get_network_wireless_alternate_management_interface",
                "table_name": "alternate_management_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/alternateManagementInterface",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the API requests made by an organization
            {
                "name": "get_organization_api_requests",
                "table_name": "api_request",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/apiRequests",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "adminId": "OPTIONAL_CONFIG",
                        # "path": "OPTIONAL_CONFIG",
                        # "method": "OPTIONAL_CONFIG",
                        # "responseCode": "OPTIONAL_CONFIG",
                        # "sourceIp": "OPTIONAL_CONFIG",
                        # "userAgent": "OPTIONAL_CONFIG",
                        # "version": "OPTIONAL_CONFIG",
                        # "operationIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the organization's APNS certificate
            {
                "name": "get_organization_sm_apns_cert",
                "table_name": "apns_cert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/sm/apnsCert",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List all Insight tracked applications
            {
                "name": "get_organization_insight_applications",
                "table_name": "application",
                "primary_key": "applicationId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/insight/applications",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the L7 firewall application categories and their associated applications for an MX network
            {
                "name": "get_network_appliance_firewall_l7_firewall_rules_application_categories",
                "table_name": "application_category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/l7FirewallRules/applicationCategories",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the application categories for traffic shaping rules.
            {
                "name": "get_network_traffic_shaping_application_categories",
                "table_name": "application_category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/trafficShaping/applicationCategories",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the application usage data for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_clients_application_usage",
                "table_name": "application_usage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/applicationUsage",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clients": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "ssidNumber": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List Custom Analytics Artifacts
            {
                "name": "get_organization_camera_custom_analytics_artifacts",
                "table_name": "artifact",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/camera/customAnalytics/artifacts",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get Custom Analytics Artifact
            {
                "name": "get_organization_camera_custom_analytics_artifact",
                "table_name": "artifact",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/camera/customAnalytics/artifacts/{artifactId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "artifactId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the availability information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.
            {
                "name": "get_organization_devices_availabilities",
                "table_name": "availability",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/devices/availabilities",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "productTypes": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a timeseries of total traffic consumption rates for all clients on a network within a given timespan, in megabits per second.
            {
                "name": "get_network_clients_bandwidth_usage_history",
                "table_name": "bandwidth_usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/bandwidthUsageHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return data usage (in megabits per second) over time for all clients in the given organization within a given time range.
            {
                "name": "get_organization_clients_bandwidth_usage_history",
                "table_name": "bandwidth_usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/clients/bandwidthUsageHistory",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a Hub BGP Configuration
            {
                "name": "get_network_appliance_vpn_bgp",
                "table_name": "bgp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/vpn/bgp",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the billing settings of this network
            {
                "name": "get_network_wireless_billing",
                "table_name": "billing",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/billing",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the Bluetooth clients seen by APs in this network
            {
                "name": "get_network_bluetooth_clients",
                "table_name": "bluetooth_client",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/bluetoothClients",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "includeConnectivityHistory": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a Bluetooth client. Bluetooth clients can be identified by their ID or their MAC.
            {
                "name": "get_network_bluetooth_client",
                "table_name": "bluetooth_client",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/bluetoothClients/{bluetoothClientId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "bluetoothClientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "includeConnectivityHistory": "OPTIONAL_CONFIG",
                        # "connectivityHistoryTimespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the Bonjour forwarding setting and rules for the SSID
            {
                "name": "get_network_wireless_ssid_bonjour_forwarding",
                "table_name": "bonjour_forwarding",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/bonjourForwarding",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the branding policies of an organization
            {
                "name": "get_organization_branding_policies",
                "table_name": "branding_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/brandingPolicies",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return a branding policy
            {
                "name": "get_organization_branding_policy",
                "table_name": "branding_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/brandingPolicies/{brandingPolicyId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "brandingPolicyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get policies for all clients with policies
            {
                "name": "get_network_policies_by_client",
                "table_name": "by_client",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/policies/byClient",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the devices that have a Dynamic ARP Inspection warning and their warnings
            {
                "name": "get_network_switch_dhcp_server_policy_arp_inspection_warnings_by_device",
                "table_name": "by_device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/warnings/byDevice",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the power status information for devices in an organization. The data returned by this endpoint is updated every 5 minutes.
            {
                "name": "get_organization_devices_power_modules_statuses_by_device",
                "table_name": "by_device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/devices/powerModules/statuses/byDevice",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "productTypes": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the current uplink addresses for devices in an organization.
            {
                "name": "get_organization_devices_uplinks_addresses_by_device",
                "table_name": "by_device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/devices/uplinks/addresses/byDevice",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "productTypes": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get firmware upgrade status for the filtered devices
            {
                "name": "get_organization_firmware_upgrades_by_device",
                "table_name": "by_device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/firmware/upgrades/byDevice",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organization_firmware_upgrades",
                            "field": "upgradeId",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "macs": "OPTIONAL_CONFIG",
                        # "firmwareUpgradeIds": "OPTIONAL_CONFIG",
                        # "firmwareUpgradeBatchIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return metrics for organization's top 10 switches by energy usage over given time range. Default unit is joules.
            {
                "name": "get_organization_summary_top_switches_by_energy_usage",
                "table_name": "by_energy_usage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/switches/byEnergyUsage",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Tracks organizations' API requests by response code across a given time period
            {
                "name": "get_organization_api_requests_overview_response_codes_by_interval",
                "table_name": "by_interval",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "interval": "OPTIONAL_CONFIG",
                        # "version": "OPTIONAL_CONFIG",
                        # "operationIds": "OPTIONAL_CONFIG",
                        # "sourceIps": "OPTIONAL_CONFIG",
                        # "adminIds": "OPTIONAL_CONFIG",
                        # "userAgent": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return an overview of currently alerting sensors by metric
            {
                "name": "get_network_sensor_alerts_current_overview_by_metric",
                "table_name": "by_metric",
                "endpoint": {
                    "data_selector": "supportedMetrics",
                    "path": "/networks/{networkId}/sensor/alerts/current/overview/byMetric",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return an overview of alert occurrences over a timespan, by metric
            {
                "name": "get_network_sensor_alerts_overview_by_metric",
                "table_name": "by_metric",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sensor/alerts/overview/byMetric",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "interval": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the switchports in an organization by switch
            {
                "name": "get_organization_switch_ports_by_switch",
                "table_name": "by_switch",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/switch/ports/bySwitch",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "portProfileIds": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                        # "mac": "OPTIONAL_CONFIG",
                        # "macs": "OPTIONAL_CONFIG",
                        # "serial": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "configurationUpdatedAfter": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return metrics for organization's top 10 clients by data usage (in mb) over given time range.
            {
                "name": "get_organization_summary_top_clients_by_usage",
                "table_name": "by_usage",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/clients/byUsage",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return metrics for organization's top clients by data usage (in mb) over given time range, grouped by manufacturer.
            {
                "name": "get_organization_summary_top_clients_manufacturers_by_usage",
                "table_name": "by_usage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/clients/manufacturers/byUsage",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return metrics for organization's top 10 devices sorted by data usage over given time range. Default unit is megabytes.
            {
                "name": "get_organization_summary_top_devices_by_usage",
                "table_name": "by_usage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/devices/byUsage",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return metrics for organization's top 10 device models sorted by data usage over given time range. Default unit is megabytes.
            {
                "name": "get_organization_summary_top_devices_models_by_usage",
                "table_name": "by_usage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/devices/models/byUsage",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return metrics for organization's top 10 ssids by data usage over given time range. Default unit is megabytes.
            {
                "name": "get_organization_summary_top_ssids_by_usage",
                "table_name": "by_usage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/ssids/byUsage",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the top 10 appliances sorted by utilization over given time range.
            {
                "name": "get_organization_summary_top_appliances_by_utilization",
                "table_name": "by_utilization",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/summary/top/appliances/byUtilization",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Bypass activation lock attempt status
            {
                "name": "get_network_sm_bypass_activation_lock_attempt",
                "table_name": "bypass_activation_lock_attempt",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/bypassActivationLockAttempts/{attemptId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "attemptId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all available content filtering categories for an MX network
            {
                "name": "get_network_appliance_content_filtering_categories",
                "table_name": "category",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/contentFiltering/categories",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the cellular firewall rules for an MX network
            {
                "name": "get_network_appliance_firewall_cellular_firewall_rules",
                "table_name": "cellular_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/cellularFirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the client's daily cellular data usage history. Usage data is in kilobytes.
            {
                "name": "get_network_sm_device_cellular_usage_history",
                "table_name": "cellular_usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/cellularUsageHistory",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the certs on a device
            {
                "name": "get_network_sm_device_certs",
                "table_name": "cert",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/certs",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get the channel utilization over each radio for all APs in a network.
            {
                "name": "get_network_network_health_channel_utilization",
                "table_name": "channel_utilization",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/networkHealth/channelUtilization",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return AP channel utilization over time for a device or network client
            {
                "name": "get_network_wireless_channel_utilization_history",
                "table_name": "channel_utilization_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/channelUtilizationHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "autoResolution": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the clients of a device, up to a maximum of a month ago. The usage of each client is returned in kilobytes. If the device is a switch, the switchport is returned; otherwise the switchport field is null.
            {
                "name": "get_device_clients",
                "table_name": "client",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/clients",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the clients that have used this network in the timespan
            {
                "name": "get_network_clients",
                "table_name": "client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "statuses": "OPTIONAL_CONFIG",
                        # "ip": "OPTIONAL_CONFIG",
                        # "ip6": "OPTIONAL_CONFIG",
                        # "ip6Local": "OPTIONAL_CONFIG",
                        # "mac": "OPTIONAL_CONFIG",
                        # "os": "OPTIONAL_CONFIG",
                        # "description": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "recentDeviceConnections": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the client associated with the given identifier. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_client",
                "table_name": "client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/{clientId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return wireless client counts over time for a network, device, or network client
            {
                "name": "get_network_wireless_client_count_history",
                "table_name": "client_count_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clientCountHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "autoResolution": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the configuration templates for this organization
            {
                "name": "get_organization_config_templates",
                "table_name": "config_template",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/configTemplates",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return a single configuration template
            {
                "name": "get_organization_config_template",
                "table_name": "config_template",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/configTemplates/{configTemplateId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "configTemplateId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # View the Change Log for your organization
            {
                "name": "get_organization_configuration_changes",
                "table_name": "configuration_change",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/configurationChanges",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkId": "OPTIONAL_CONFIG",
                        # "adminId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated connectivity info for a given AP on this network
            {
                "name": "get_device_wireless_connection_stats",
                "table_name": "connection_stat",
                "primary_key": "serial",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/wireless/connectionStats",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated connectivity info for this network, grouped by clients
            {
                "name": "get_network_wireless_clients_connection_stats",
                "table_name": "connection_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clients/connectionStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated connectivity info for a given client on this network. Clients are identified by their MAC.
            {
                "name": "get_network_wireless_client_connection_stats",
                "table_name": "connection_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clients/{clientId}/connectionStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated connectivity info for this network
            {
                "name": "get_network_wireless_connection_stats",
                "table_name": "connection_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/connectionStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated connectivity info for this network, grouped by node
            {
                "name": "get_network_wireless_devices_connection_stats",
                "table_name": "connection_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/devices/connectionStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns historical connectivity data (whether a device is regularly checking in to Dashboard).
            {
                "name": "get_network_sm_device_connectivity",
                "table_name": "connectivity",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/connectivity",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the wireless connectivity events for a client within a network in the timespan.
            {
                "name": "get_network_wireless_client_connectivity_events",
                "table_name": "connectivity_event",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clients/{clientId}/connectivityEvents",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "types": "OPTIONAL_CONFIG",
                        # "includedSeverities": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssidNumber": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the connectivity testing destinations for an MX network
            {
                "name": "get_network_appliance_connectivity_monitoring_destinations",
                "table_name": "connectivity_monitoring_destination",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/connectivityMonitoringDestinations",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the connectivity testing destinations for an MG network
            {
                "name": "get_network_cellular_gateway_connectivity_monitoring_destinations",
                "table_name": "connectivity_monitoring_destination",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/cellularGateway/connectivityMonitoringDestinations",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the content filtering settings for an MX network
            {
                "name": "get_network_appliance_content_filtering",
                "table_name": "content_filtering",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/contentFiltering",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return custom analytics settings for a camera
            {
                "name": "get_device_camera_custom_analytics",
                "table_name": "custom_analytic",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/customAnalytics",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all custom performance classes for an MX network
            {
                "name": "get_network_appliance_traffic_shaping_custom_performance_classes",
                "table_name": "custom_performance_class",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a custom performance class for an MX network
            {
                "name": "get_network_appliance_traffic_shaping_custom_performance_class",
                "table_name": "custom_performance_class",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/trafficShaping/customPerformanceClasses/{customPerformanceClassId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "customPerformanceClassId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return PHY data rates over time for a network, device, or network client
            {
                "name": "get_network_wireless_data_rate_history",
                "table_name": "data_rate_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/dataRateHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "autoResolution": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return current delegated IPv6 prefixes on an appliance.
            {
                "name": "get_device_appliance_prefixes_delegated",
                "table_name": "delegated",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/appliance/prefixes/delegated",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return historical records of various Systems Manager network connection details for desktop devices.
            {
                "name": "get_network_sm_device_desktop_logs",
                "table_name": "desktop_log",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/desktopLogs",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a single device
            {
                "name": "get_device",
                "table_name": "device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the devices in a network
            {
                "name": "get_network_devices",
                "table_name": "device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/devices",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the devices enrolled in an SM network with various specified fields and filters
            {
                "name": "get_network_sm_devices",
                "table_name": "device",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "wifiMacs": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "ids": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the devices in an organization
            {
                "name": "get_organization_devices",
                "table_name": "device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/devices",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "configurationUpdatedAfter": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "productTypes": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                        # "mac": "OPTIONAL_CONFIG",
                        # "serial": "OPTIONAL_CONFIG",
                        # "model": "OPTIONAL_CONFIG",
                        # "macs": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "sensorMetrics": "OPTIONAL_CONFIG",
                        # "sensorAlertProfileIds": "OPTIONAL_CONFIG",
                        # "models": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the device inventory for an organization
            {
                "name": "get_organization_inventory_devices",
                "table_name": "device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/inventory/devices",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "usedState": "OPTIONAL_CONFIG",
                        # "search": "OPTIONAL_CONFIG",
                        # "macs": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "models": "OPTIONAL_CONFIG",
                        # "orderNumbers": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                        # "productTypes": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a single device from the inventory of an organization
            {
                "name": "get_organization_inventory_device",
                "table_name": "device",
                "primary_key": "serial",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/inventory/devices/{serial}",
                    "params": {
                        "serial": {
                            "type": "resolve",
                            "resource": "get_organization_inventory_devices",
                            "field": "serial",
                        },
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return historical records of commands sent to Systems Manager devices. Note that this will include the name of the Dashboard user who initiated the command if it was generated by a Dashboard admin rather than the automatic behavior of the system; you may wish to filter this out of any reports.
            {
                "name": "get_network_sm_device_device_command_logs",
                "table_name": "device_command_log",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/deviceCommandLogs",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the installed profiles associated with a device
            {
                "name": "get_network_sm_device_device_profiles",
                "table_name": "device_profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/deviceProfiles",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get the profiles associated with a user
            {
                "name": "get_network_sm_user_device_profiles",
                "table_name": "device_profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/users/{userId}/deviceProfiles",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "get_network_sm_users",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the device type group policies for the SSID
            {
                "name": "get_network_wireless_ssid_device_type_group_policies",
                "table_name": "device_type_group_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/deviceTypeGroupPolicies",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a layer 3 interface DHCP configuration for a switch
            {
                "name": "get_device_switch_routing_interface_dhcp",
                "table_name": "dhcp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/routing/interfaces/{interfaceId}/dhcp",
                    "params": {
                        "interfaceId": {
                            "type": "resolve",
                            "resource": "get_device_switch_routing_interfaces",
                            "field": "interfaceId",
                        },
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List common DHCP settings of MGs
            {
                "name": "get_network_cellular_gateway_dhcp",
                "table_name": "dhcp",
                "endpoint": {
                    "data_selector": "dnsCustomNameservers",
                    "path": "/networks/{networkId}/cellularGateway/dhcp",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a layer 3 interface DHCP configuration for a switch stack
            {
                "name": "get_network_switch_stack_routing_interface_dhcp",
                "table_name": "dhcp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "switchStackId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "interfaceId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the DHCP server settings. Blocked/allowed servers are only applied when default policy is allow/block, respectively
            {
                "name": "get_network_switch_dhcp_server_policy",
                "table_name": "dhcp_server_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/dhcpServerPolicy",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the available DSCP tagging options for your traffic shaping rules.
            {
                "name": "get_network_traffic_shaping_dscp_tagging_options",
                "table_name": "dscp_tagging_option",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/trafficShaping/dscpTaggingOptions",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the DSCP to CoS mappings
            {
                "name": "get_network_switch_dscp_to_cos_mappings",
                "table_name": "dscp_to_cos_mapping",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/dscpToCosMappings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the EAP overridden parameters for an SSID
            {
                "name": "get_network_wireless_ssid_eap_override",
                "table_name": "eap_override",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/eapOverride",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the security events for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_appliance_client_security_events",
                "table_name": "event",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/clients/{clientId}/security/events",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "sortOrder": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the security events for a network
            {
                "name": "get_network_appliance_security_events",
                "table_name": "event",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/security/events",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "sortOrder": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the events for the network
            {
                "name": "get_network_events",
                "table_name": "event",
                "primary_key": "networkId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "events",
                    "path": "/networks/{networkId}/events",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "productType": "OPTIONAL_CONFIG",
                        # "includedEventTypes": "OPTIONAL_CONFIG",
                        # "excludedEventTypes": "OPTIONAL_CONFIG",
                        # "deviceMac": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "deviceName": "OPTIONAL_CONFIG",
                        # "clientIp": "OPTIONAL_CONFIG",
                        # "clientMac": "OPTIONAL_CONFIG",
                        # "clientName": "OPTIONAL_CONFIG",
                        # "smDeviceMac": "OPTIONAL_CONFIG",
                        # "smDeviceName": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the Staged Upgrade Event from a network
            {
                "name": "get_network_firmware_upgrades_staged_events",
                "table_name": "event",
                "endpoint": {
                    "data_selector": "reasons",
                    "path": "/networks/{networkId}/firmwareUpgrades/staged/events",
                    "params": {
                        "networkId": {
                            "type": "resolve",
                            "resource": "get_network_firmware_upgrades",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List the security events for an organization
            {
                "name": "get_organization_appliance_security_events",
                "table_name": "event",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/appliance/security/events",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "sortOrder": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the event type to human-readable description
            {
                "name": "get_network_events_event_types",
                "table_name": "event_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/events/eventTypes",
                    "params": {
                        "networkId": {
                            "type": "resolve",
                            "resource": "get_network_events",
                            "field": "networkId",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List of all failed client connection events on this network in a given time range
            {
                "name": "get_network_wireless_failed_connections",
                "table_name": "failed_connection",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/failedConnections",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "serial": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the available early access features for organization
            {
                "name": "get_organization_early_access_features",
                "table_name": "feature",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/earlyAccess/features",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List the appliance services and their accessibility rules
            {
                "name": "get_network_appliance_firewall_firewalled_services",
                "table_name": "firewalled_service",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/firewalledServices",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the accessibility settings of the given service ('ICMP', 'web', or 'SNMP')
            {
                "name": "get_network_appliance_firewall_firewalled_service",
                "table_name": "firewalled_service",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/firewalledServices/{service}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "service": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get firmware upgrade information for a network
            {
                "name": "get_network_firmware_upgrades",
                "table_name": "firmware_upgrade",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "products.appliance.availableVersions",
                    "path": "/networks/{networkId}/firmwareUpgrades",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the floor plans that belong to your network
            {
                "name": "get_network_floor_plans",
                "table_name": "floor_plan",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/floorPlans",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Find a floor plan by ID
            {
                "name": "get_network_floor_plan",
                "table_name": "floor_plan",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/floorPlans/{floorPlanId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "floorPlanId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of Staged Upgrade Groups in a network
            {
                "name": "get_network_firmware_upgrades_staged_groups",
                "table_name": "group",
                "primary_key": "groupId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/firmwareUpgrades/staged/groups",
                    "params": {
                        "networkId": {
                            "type": "resolve",
                            "resource": "get_network_firmware_upgrades",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a Staged Upgrade Group from a network
            {
                "name": "get_network_firmware_upgrades_staged_group",
                "table_name": "group",
                "primary_key": "groupId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}",
                    "params": {
                        "groupId": {
                            "type": "resolve",
                            "resource": "get_network_firmware_upgrades_staged_groups",
                            "field": "groupId",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List adaptive policy groups in a organization
            {
                "name": "get_organization_adaptive_policy_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/groups",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns an adaptive policy group
            {
                "name": "get_organization_adaptive_policy_group",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/groups/{id}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists Policy Object Groups belonging to the organization.
            {
                "name": "get_organization_policy_objects_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/policyObjects/groups",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Shows details of a Policy Object Group.
            {
                "name": "get_organization_policy_objects_group",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/policyObjects/groups/{policyObjectGroupId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "policyObjectGroupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the group policies in a network
            {
                "name": "get_network_group_policies",
                "table_name": "group_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/groupPolicies",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Display a group policy
            {
                "name": "get_network_group_policy",
                "table_name": "group_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/groupPolicies/{groupPolicyId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "groupPolicyId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get application health by time
            {
                "name": "get_network_insight_application_health_by_time",
                "table_name": "health_by_time",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/insight/applications/{applicationId}/healthByTime",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "applicationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return historical records for analytic zones
            {
                "name": "get_device_camera_analytics_zone_history",
                "table_name": "history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/analytics/zones/{zoneId}/history",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "zoneId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "objectType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the alert history for this network
            {
                "name": "get_network_alerts_history",
                "table_name": "history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/alerts/history",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return all reported readings from sensors in a given timespan, sorted by timestamp
            {
                "name": "get_organization_sensor_readings_history",
                "table_name": "history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/sensor/readings/history",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "metrics": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the Hotspot 2.0 settings for an SSID
            {
                "name": "get_network_wireless_ssid_hotspot_20",
                "table_name": "hotspot20",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/hotspot20",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the HTTP servers for a network
            {
                "name": "get_network_webhooks_http_servers",
                "table_name": "http_server",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/webhooks/httpServers",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return an HTTP server for a network
            {
                "name": "get_network_webhooks_http_server",
                "table_name": "http_server",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/webhooks/httpServers/{httpServerId}",
                    "params": {
                        "httpServerId": {
                            "type": "resolve",
                            "resource": "get_network_webhooks_http_servers",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all Identity PSKs in a wireless network
            {
                "name": "get_network_wireless_ssid_identity_psks",
                "table_name": "identity_psk",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/identityPsks",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return an Identity PSK
            {
                "name": "get_network_wireless_ssid_identity_psk",
                "table_name": "identity_psk",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/identityPsks/{identityPskId}",
                    "params": {
                        "identityPskId": {
                            "type": "resolve",
                            "resource": "get_network_wireless_ssid_identity_psks",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the SAML IdPs in your organization.
            {
                "name": "get_organization_saml_idps",
                "table_name": "idp",
                "primary_key": "idpId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/saml/idps",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a SAML IdP from your organization.
            {
                "name": "get_organization_saml_idp",
                "table_name": "idp",
                "primary_key": "idpId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/saml/idps/{idpId}",
                    "params": {
                        "idpId": {
                            "type": "resolve",
                            "resource": "get_organization_saml_idps",
                            "field": "idpId",
                        },
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Check the status of a committed Import operation
            {
                "name": "get_organization_inventory_onboarding_cloud_monitoring_imports",
                "table_name": "import",
                "primary_key": "importId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        "importIds": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the inbound cellular firewall rules for an MX network
            {
                "name": "get_network_appliance_firewall_inbound_cellular_firewall_rules",
                "table_name": "inbound_cellular_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/inboundCellularFirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the inbound firewall rules for an MX network
            {
                "name": "get_network_appliance_firewall_inbound_firewall_rules",
                "table_name": "inbound_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/inboundFirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.
            {
                "name": "get_device_switch_routing_interfaces",
                "table_name": "interface",
                "primary_key": "interfaceId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/routing/interfaces",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a layer 3 interface for a switch
            {
                "name": "get_device_switch_routing_interface",
                "table_name": "interface",
                "primary_key": "interfaceId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/routing/interfaces/{interfaceId}",
                    "params": {
                        "interfaceId": {
                            "type": "resolve",
                            "resource": "get_device_switch_routing_interfaces",
                            "field": "interfaceId",
                        },
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List layer 3 interfaces for a switch stack
            {
                "name": "get_network_switch_stack_routing_interfaces",
                "table_name": "interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "switchStackId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a layer 3 interface from a switch stack
            {
                "name": "get_network_switch_stack_routing_interface",
                "table_name": "interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "switchStackId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "interfaceId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all supported intrusion settings for an MX network
            {
                "name": "get_network_appliance_security_intrusion",
                "table_name": "intrusion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/security/intrusion",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all supported intrusion settings for an organization
            {
                "name": "get_organization_appliance_security_intrusion",
                "table_name": "intrusion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/appliance/security/intrusion",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the L3 firewall rules for an MX network
            {
                "name": "get_network_appliance_firewall_l3_firewall_rules",
                "table_name": "l_3_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/l3FirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the L3 firewall rules for an SSID on an MR network
            {
                "name": "get_network_wireless_ssid_firewall_l3_firewall_rules",
                "table_name": "l_3_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/firewall/l3FirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the MX L7 firewall rules for an MX network
            {
                "name": "get_network_appliance_firewall_l7_firewall_rules",
                "table_name": "l_7_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/l7FirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the L7 firewall rules for an SSID on an MR network
            {
                "name": "get_network_wireless_ssid_firewall_l7_firewall_rules",
                "table_name": "l_7_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/firewall/l7FirewallRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Show the LAN Settings of a MG
            {
                "name": "get_device_cellular_gateway_lan",
                "table_name": "lan",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/cellularGateway/lan",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the latency history for a client. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP. The latency data is from a sample of 2% of packets and is grouped into 4 traffic categories: background, best effort, video, voice. Within these categories the sampled packet counters are bucketed by latency in milliseconds.
            {
                "name": "get_network_wireless_client_latency_history",
                "table_name": "latency_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clients/{clientId}/latencyHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return average wireless latency over time for a network, device, or network client
            {
                "name": "get_network_wireless_latency_history",
                "table_name": "latency_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/latencyHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "autoResolution": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "accessCategory": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated latency info for a given AP on this network
            {
                "name": "get_device_wireless_latency_stats",
                "table_name": "latency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/wireless/latencyStats",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated latency info for this network, grouped by clients
            {
                "name": "get_network_wireless_clients_latency_stats",
                "table_name": "latency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clients/latencyStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated latency info for a given client on this network. Clients are identified by their MAC.
            {
                "name": "get_network_wireless_client_latency_stats",
                "table_name": "latency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/clients/{clientId}/latencyStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated latency info for this network, grouped by node
            {
                "name": "get_network_wireless_devices_latency_stats",
                "table_name": "latency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/devices/latencyStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Aggregated latency info for this network
            {
                "name": "get_network_wireless_latency_stats",
                "table_name": "latency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/latencyStats",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                        # "vlan": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the latest available reading for each metric from each sensor, sorted by sensor serial
            {
                "name": "get_organization_sensor_readings_latest",
                "table_name": "latest",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/sensor/readings/latest",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "metrics": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the licenses for an organization
            {
                "name": "get_organization_licenses",
                "table_name": "license",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/licenses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "networkId": "OPTIONAL_CONFIG",
                        # "state": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Display a license
            {
                "name": "get_organization_license",
                "table_name": "license",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/licenses/{licenseId}",
                    "params": {
                        "licenseId": {
                            "type": "resolve",
                            "resource": "get_organization_licenses",
                            "field": "id",
                        },
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the licenses in a coterm organization
            {
                "name": "get_organization_licensing_coterm_licenses",
                "table_name": "license",
                "primary_key": "organizationId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/licensing/coterm/licenses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "invalidated": "OPTIONAL_CONFIG",
                        # "expired": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List link aggregation groups
            {
                "name": "get_network_switch_link_aggregations",
                "table_name": "link_aggregation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/linkAggregations",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the LLDP and CDP information for all discovered devices and connections in a network.
            {
                "name": "get_network_topology_link_layer",
                "table_name": "link_layer",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/topology/linkLayer",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns live state from camera of analytics zones
            {
                "name": "get_device_camera_analytics_live",
                "table_name": "live",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/analytics/live",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List LLDP and CDP information for a device
            {
                "name": "get_device_lldp_cdp",
                "table_name": "lldp_cdp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/lldpCdp",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the log of webhook POSTs sent
            {
                "name": "get_organization_webhooks_logs",
                "table_name": "log",
                "primary_key": "organizationId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/webhooks/logs",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "url": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the login security settings for an organization.
            {
                "name": "get_organization_login_security",
                "table_name": "login_security",
                "endpoint": {
                    "data_selector": "loginIpRanges",
                    "path": "/organizations/{organizationId}/loginSecurity",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get the uplink loss percentage and latency in milliseconds, and goodput in kilobits per second for a wired network device.
            {
                "name": "get_device_loss_and_latency_history",
                "table_name": "loss_and_latency_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/lossAndLatencyHistory",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ip": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "uplink": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all supported malware settings for an MX network
            {
                "name": "get_network_appliance_security_malware",
                "table_name": "malware",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/security/malware",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the management interface settings for a device
            {
                "name": "get_device_management_interface",
                "table_name": "management_interface",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/managementInterface",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the identity of the current user.
            {
                "name": "get_administered_identities_me",
                "table_name": "me",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/administered/identities/me",
                    "paginator": "auto",
                },
            },
            # List the users configured under Meraki Authentication for a network (splash guest or RADIUS users for a wireless network, or client VPN users for a wired network)
            {
                "name": "get_network_meraki_auth_users",
                "table_name": "meraki_auth_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/merakiAuthUsers",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the Meraki Auth splash guest, RADIUS, or client VPN user
            {
                "name": "get_network_meraki_auth_user",
                "table_name": "meraki_auth_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/merakiAuthUsers/{merakiAuthUserId}",
                    "params": {
                        "merakiAuthUserId": {
                            "type": "resolve",
                            "resource": "get_network_meraki_auth_users",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List wireless mesh statuses for repeaters
            {
                "name": "get_network_wireless_mesh_statuses",
                "table_name": "mesh_status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/meshStatuses",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the monitored media servers for this organization. Only valid for organizations with Meraki Insight.
            {
                "name": "get_organization_insight_monitored_media_servers",
                "table_name": "monitored_media_server",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/insight/monitoredMediaServers",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return a monitored media server for this organization. Only valid for organizations with Meraki Insight.
            {
                "name": "get_organization_insight_monitored_media_server",
                "table_name": "monitored_media_server",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/insight/monitoredMediaServers/{monitoredMediaServerId}",
                    "params": {
                        "monitoredMediaServerId": {
                            "type": "resolve",
                            "resource": "get_organization_insight_monitored_media_servers",
                            "field": "id",
                        },
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the MQTT brokers for this network
            {
                "name": "get_network_mqtt_brokers",
                "table_name": "mqtt_broker",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/mqttBrokers",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return an MQTT broker
            {
                "name": "get_network_mqtt_broker",
                "table_name": "mqtt_broker",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/mqttBrokers/{mqttBrokerId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "mqttBrokerId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the MTU configuration
            {
                "name": "get_network_switch_mtu",
                "table_name": "mtu",
                "endpoint": {
                    "data_selector": "overrides",
                    "path": "/networks/{networkId}/switch/mtu",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return multicast settings for a network
            {
                "name": "get_network_switch_routing_multicast",
                "table_name": "multicast",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/routing/multicast",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the NetFlow traffic reporting settings for a network
            {
                "name": "get_network_netflow",
                "table_name": "netflow",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/netflow",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a network
            {
                "name": "get_network",
                "table_name": "network",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns list of networks eligible for adding cloud monitored device
            {
                "name": "get_organization_inventory_onboarding_cloud_monitoring_networks",
                "table_name": "network",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/inventory/onboarding/cloudMonitoring/networks",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        "deviceType": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the networks that the user has privileges on in an organization
            {
                "name": "get_organization_networks",
                "table_name": "network",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/networks",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "configTemplateId": "OPTIONAL_CONFIG",
                        # "isBoundToConfigTemplate": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the network adapters of a device
            {
                "name": "get_network_sm_device_network_adapters",
                "table_name": "network_adapter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/networkAdapters",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the MV Sense object detection model list for the given camera
            {
                "name": "get_device_camera_sense_object_detection_models",
                "table_name": "object_detection_model",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/sense/objectDetectionModels",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the 1:Many NAT mapping rules for an MX network
            {
                "name": "get_network_appliance_firewall_one_to_many_nat_rules",
                "table_name": "one_to_many_nat_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/oneToManyNatRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the 1:1 NAT mapping rules for an MX network
            {
                "name": "get_network_appliance_firewall_one_to_one_nat_rules",
                "table_name": "one_to_one_nat_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/oneToOneNatRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the OpenAPI 2.0 Specification of the organization's API documentation in JSON
            {
                "name": "get_organization_openapi_spec",
                "table_name": "openapi_spec",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/openapiSpec",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List the early access feature opt-ins for an organization
            {
                "name": "get_organization_early_access_features_opt_ins",
                "table_name": "opt_in",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/earlyAccess/features/optIns",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Show an early access feature opt-in for an organization
            {
                "name": "get_organization_early_access_features_opt_in",
                "table_name": "opt_in",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "optInId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the quality of service rule IDs by order in which they will be processed by the switch
            {
                "name": "get_network_switch_qos_rules_order",
                "table_name": "order",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/qosRules/order",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the organizations that the user has privileges on
            {
                "name": "get_organizations",
                "table_name": "organization",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations",
                    "paginator": "auto",
                },
            },
            # Return an organization
            {
                "name": "get_organization",
                "table_name": "organization",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return layer 3 OSPF routing configuration
            {
                "name": "get_network_switch_routing_ospf",
                "table_name": "ospf",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/routing/ospf",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns an overview of aggregate analytics data for a timespan
            {
                "name": "get_device_camera_analytics_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/analytics/overview",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "objectType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return overview statistics for network clients
            {
                "name": "get_network_clients_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/overview",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns adaptive policy aggregate statistics for an organization
            {
                "name": "get_organization_adaptive_policy_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/overview",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return an aggregated overview of API requests data
            {
                "name": "get_organization_api_requests_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/apiRequests/overview",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return summary information around client data usage (in mb) across the given organization.
            {
                "name": "get_organization_clients_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/clients/overview",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return an overview of current device statuses
            {
                "name": "get_organization_devices_statuses_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "counts.byStatus",
                    "path": "/organizations/{organizationId}/devices/statuses/overview",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "productTypes": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return an overview of the license state for an organization
            {
                "name": "get_organization_licenses_overview",
                "table_name": "overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/licenses/overview",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organization_licenses",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the packet counters for all the ports of a switch
            {
                "name": "get_device_switch_ports_statuses_packets",
                "table_name": "packet",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/ports/statuses/packets",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the webhook payload templates for a network
            {
                "name": "get_network_webhooks_payload_templates",
                "table_name": "payload_template",
                "primary_key": "payloadTemplateId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/webhooks/payloadTemplates",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get the webhook payload template for a network
            {
                "name": "get_network_webhooks_payload_template",
                "table_name": "payload_template",
                "primary_key": "payloadTemplateId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/webhooks/payloadTemplates/{payloadTemplateId}",
                    "params": {
                        "payloadTemplateId": {
                            "type": "resolve",
                            "resource": "get_network_webhooks_payload_templates",
                            "field": "payloadTemplateId",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the performance score for a single MX. Only primary MX devices supported. If no data is available, a 204 error code is returned.
            {
                "name": "get_device_appliance_performance",
                "table_name": "performance",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/appliance/performance",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return historical records of various Systems Manager client metrics for desktop devices.
            {
                "name": "get_network_sm_device_performance_history",
                "table_name": "performance_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/performanceHistory",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the keys required to access Personally Identifiable Information (PII) for a given identifier. Exactly one identifier will be accepted. If the organization contains org-wide Systems Manager users matching the key provided then there will be an entry with the key "0" containing the applicable keys.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/piiKeys ```
            {
                "name": "get_network_pii_pii_keys",
                "table_name": "pii_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/pii/piiKeys",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "username": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                        # "mac": "OPTIONAL_CONFIG",
                        # "serial": "OPTIONAL_CONFIG",
                        # "imei": "OPTIONAL_CONFIG",
                        # "bluetoothMac": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a ping job. Latency unit in response is in milliseconds. Size is in bytes.
            {
                "name": "get_device_live_tools_ping",
                "table_name": "ping",
                "primary_key": "pingId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/liveTools/ping/{id}",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a ping device job. Latency unit in response is in milliseconds. Size is in bytes.
            {
                "name": "get_device_live_tools_ping_device",
                "table_name": "ping_device",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/liveTools/pingDevice/{id}",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the policy assigned to a client on the network. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_client_policy",
                "table_name": "policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/{clientId}/policy",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List adaptive policies in an organization
            {
                "name": "get_organization_adaptive_policy_policies",
                "table_name": "policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/policies",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return an adaptive policy
            {
                "name": "get_organization_adaptive_policy_policy",
                "table_name": "policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/policies/{id}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists Policy Objects belonging to the organization.
            {
                "name": "get_organization_policy_objects",
                "table_name": "policy_object",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/policyObjects",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Shows details of a Policy Object.
            {
                "name": "get_organization_policy_object",
                "table_name": "policy_object",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/policyObjects/{policyObjectId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "policyObjectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the switch ports for a switch
            {
                "name": "get_device_switch_ports",
                "table_name": "port",
                "primary_key": "portId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/ports",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a switch port
            {
                "name": "get_device_switch_port",
                "table_name": "port",
                "primary_key": "portId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/ports/{portId}",
                    "params": {
                        "portId": {
                            "type": "resolve",
                            "resource": "get_device_switch_ports",
                            "field": "portId",
                        },
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List per-port VLAN settings for all ports of a MX.
            {
                "name": "get_network_appliance_ports",
                "table_name": "port",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/ports",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return per-port VLAN settings for a single MX port.
            {
                "name": "get_network_appliance_port",
                "table_name": "port",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/ports/{portId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "portId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return all the ports of a switch profile
            {
                "name": "get_organization_config_template_switch_profile_ports",
                "table_name": "port",
                "primary_key": "portId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "configTemplateId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "profileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a switch profile port
            {
                "name": "get_organization_config_template_switch_profile_port",
                "table_name": "port",
                "primary_key": "portId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles/{profileId}/ports/{portId}",
                    "params": {
                        "portId": {
                            "type": "resolve",
                            "resource": "get_organization_config_template_switch_profile_ports",
                            "field": "portId",
                        },
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "configTemplateId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "profileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the port forwarding rules for a single MG.
            {
                "name": "get_device_cellular_gateway_port_forwarding_rules",
                "table_name": "port_forwarding_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/cellularGateway/portForwardingRules",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the port forwarding rules for an MX network
            {
                "name": "get_network_appliance_firewall_port_forwarding_rules",
                "table_name": "port_forwarding_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/portForwardingRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List switch port schedules
            {
                "name": "get_network_switch_port_schedules",
                "table_name": "port_schedule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/portSchedules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).
            {
                "name": "get_organization_branding_policies_priorities",
                "table_name": "priority",
                "endpoint": {
                    "data_selector": "brandingPolicyIds",
                    "path": "/organizations/{organizationId}/brandingPolicies/priorities",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Lists all sensor alert profiles for a network.
            {
                "name": "get_network_sensor_alerts_profiles",
                "table_name": "profile",
                "primary_key": "profileId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sensor/alerts/profiles",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Show details of a sensor alert profile for a network.
            {
                "name": "get_network_sensor_alerts_profile",
                "table_name": "profile",
                "primary_key": "profileId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sensor/alerts/profiles/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_network_sensor_alerts_profiles",
                            "field": "profileId",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all profiles in a network
            {
                "name": "get_network_sm_profiles",
                "table_name": "profile",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/profiles",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all organization-wide alert configurations
            {
                "name": "get_organization_alerts_profiles",
                "table_name": "profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/alerts/profiles",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List the switch profiles for your switch template configuration
            {
                "name": "get_organization_config_template_switch_profiles",
                "table_name": "profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/configTemplates/{configTemplateId}/switch/profiles",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "configTemplateId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List quality of service rules
            {
                "name": "get_network_switch_qos_rules",
                "table_name": "qos_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/qosRules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a quality of service rule
            {
                "name": "get_network_switch_qos_rule",
                "table_name": "qos_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/qosRules/{qosRuleId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "qosRuleId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns quality and retention settings for the given camera
            {
                "name": "get_device_camera_quality_and_retention",
                "table_name": "quality_and_retention",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/qualityAndRetention",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the quality retention profiles for this network
            {
                "name": "get_network_camera_quality_retention_profiles",
                "table_name": "quality_retention_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/camera/qualityRetentionProfiles",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a single quality retention profile
            {
                "name": "get_network_camera_quality_retention_profile",
                "table_name": "quality_retention_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/camera/qualityRetentionProfiles/{qualityRetentionProfileId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "qualityRetentionProfileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns most recent record for analytics zones
            {
                "name": "get_device_camera_analytics_recent",
                "table_name": "recent",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/analytics/recent",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "objectType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the sensor roles for a given sensor or camera device.
            {
                "name": "get_device_sensor_relationships",
                "table_name": "relationship",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/sensor/relationships",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the sensor roles for devices in a given network
            {
                "name": "get_network_sensor_relationships",
                "table_name": "relationship",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sensor/relationships",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List multicast rendezvous points
            {
                "name": "get_network_switch_routing_multicast_rendezvous_points",
                "table_name": "rendezvous_point",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/routing/multicast/rendezvousPoints",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a multicast rendezvous point
            {
                "name": "get_network_switch_routing_multicast_rendezvous_point",
                "table_name": "rendezvous_point",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/routing/multicast/rendezvousPoints/{rendezvousPointId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "rendezvousPointId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the PII requests for this network or organization  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/requests ```
            {
                "name": "get_network_pii_requests",
                "table_name": "request",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/pii/requests",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a PII request  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/requests/{requestId} ```
            {
                "name": "get_network_pii_request",
                "table_name": "request",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/pii/requests/{requestId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "requestId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the restrictions on a device
            {
                "name": "get_network_sm_device_restrictions",
                "table_name": "restriction",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/restrictions",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the non-basic RF profiles for this network
            {
                "name": "get_network_wireless_rf_profiles",
                "table_name": "rf_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/rfProfiles",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "includeTemplateProfiles": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a RF profile
            {
                "name": "get_network_wireless_rf_profile",
                "table_name": "rf_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/rfProfiles/{rfProfileId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "rfProfileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Display the traffic shaping settings rules for an MX network
            {
                "name": "get_network_appliance_traffic_shaping_rules",
                "table_name": "rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/trafficShaping/rules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Display the traffic shaping settings for a SSID on an MR network
            {
                "name": "get_network_wireless_ssid_traffic_shaping_rules",
                "table_name": "rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/trafficShaping/rules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the SAML SSO enabled settings for an organization.
            {
                "name": "get_organization_saml",
                "table_name": "saml",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/saml",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List the SAML roles for this organization
            {
                "name": "get_organization_saml_roles",
                "table_name": "saml_role",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/samlRoles",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return a SAML role
            {
                "name": "get_organization_saml_role",
                "table_name": "saml_role",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/samlRoles/{samlRoleId}",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "samlRoleId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all camera recording schedules.
            {
                "name": "get_network_camera_schedules",
                "table_name": "schedule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/camera/schedules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the outage schedule for the SSID
            {
                "name": "get_network_wireless_ssid_schedules",
                "table_name": "schedule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/schedules",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the client details in an organization
            {
                "name": "get_organization_clients_search",
                "table_name": "search",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/clients/search",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        "mac": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the security centers on a device
            {
                "name": "get_network_sm_device_security_centers",
                "table_name": "security_center",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/securityCenters",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the network's DHCPv4 servers seen within the selected timeframe (default 1 day)
            {
                "name": "get_network_switch_dhcp_v4_servers_seen",
                "table_name": "seen",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/dhcp/v4/servers/seen",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns sense settings for a given camera
            {
                "name": "get_device_camera_sense",
                "table_name": "sense",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/sense",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the uplink settings for an MX appliance
            {
                "name": "get_device_appliance_uplinks_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "interfaces.wan1.svis.ipv4.nameservers.addresses",
                    "path": "/devices/{serial}/appliance/uplinks/settings",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns video settings for the given camera
            {
                "name": "get_device_camera_video_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/video/settings",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the bluetooth settings for a wireless device
            {
                "name": "get_device_wireless_bluetooth_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/wireless/bluetooth/settings",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the radio settings of a device
            {
                "name": "get_device_wireless_radio_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/wireless/radio/settings",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the alert configuration for this network
            {
                "name": "get_network_alerts_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/alerts/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the firewall settings for this network
            {
                "name": "get_network_appliance_firewall_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/firewall/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the appliance settings for a network
            {
                "name": "get_network_appliance_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the enabled status of VLANs for the network
            {
                "name": "get_network_appliance_vlans_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/vlans/settings",
                    "params": {
                        "networkId": {
                            "type": "resolve",
                            "resource": "get_network_appliance_vlans",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the settings for a network
            {
                "name": "get_network_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the switch network settings
            {
                "name": "get_network_switch_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "powerExceptions",
                    "path": "/networks/{networkId}/switch/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the Bluetooth settings for a network. <a href="https://documentation.meraki.com/MR/Bluetooth/Bluetooth_Low_Energy_(BLE)">Bluetooth settings</a> must be enabled on the network.
            {
                "name": "get_network_wireless_bluetooth_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/bluetooth/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the wireless settings for a network
            {
                "name": "get_network_wireless_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Display the splash page settings for the given SSID
            {
                "name": "get_network_wireless_ssid_splash_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "sentryEnrollment.enforcedSystems",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/splash/settings",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns global adaptive policy settings in an organization
            {
                "name": "get_organization_adaptive_policy_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/adaptivePolicy/settings",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return signal quality (SNR/RSSI) over time for a device or network client
            {
                "name": "get_network_wireless_signal_quality_history",
                "table_name": "signal_quality_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/signalQualityHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "autoResolution": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the SIM and APN configurations for a cellular device.
            {
                "name": "get_device_cellular_sims",
                "table_name": "sim",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/cellular/sims",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return single LAN configuration
            {
                "name": "get_network_appliance_single_lan",
                "table_name": "single_lan",
                "endpoint": {
                    "data_selector": "ipv6.prefixAssignments",
                    "path": "/networks/{networkId}/appliance/singleLan",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the site-to-site VPN settings of a network. Only valid for MX networks.
            {
                "name": "get_network_appliance_vpn_site_to_site_vpn",
                "table_name": "site_to_site_vpn",
                "endpoint": {
                    "data_selector": "hubs",
                    "path": "/networks/{networkId}/appliance/vpn/siteToSiteVpn",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Given a piece of Personally Identifiable Information (PII), return the Systems Manager device ID(s) associated with that identifier. These device IDs can be used with the Systems Manager API endpoints to retrieve device details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smDevicesForKey ```
            {
                "name": "get_network_pii_sm_devices_for_key",
                "table_name": "sm_devices_for_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/pii/smDevicesForKey",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "username": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                        # "mac": "OPTIONAL_CONFIG",
                        # "serial": "OPTIONAL_CONFIG",
                        # "imei": "OPTIONAL_CONFIG",
                        # "bluetoothMac": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Given a piece of Personally Identifiable Information (PII), return the Systems Manager owner ID(s) associated with that identifier. These owner IDs can be used with the Systems Manager API endpoints to retrieve owner details. Exactly one identifier will be accepted.  ## ALTERNATE PATH  ``` /organizations/{organizationId}/pii/smOwnersForKey ```
            {
                "name": "get_network_pii_sm_owners_for_key",
                "table_name": "sm_owners_for_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/pii/smOwnersForKey",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "username": "OPTIONAL_CONFIG",
                        # "email": "OPTIONAL_CONFIG",
                        # "mac": "OPTIONAL_CONFIG",
                        # "serial": "OPTIONAL_CONFIG",
                        # "imei": "OPTIONAL_CONFIG",
                        # "bluetoothMac": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the SNMP settings for a network
            {
                "name": "get_network_snmp",
                "table_name": "snmp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/snmp",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the SNMP settings for an organization
            {
                "name": "get_organization_snmp",
                "table_name": "snmp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/snmp",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of softwares associated with a device
            {
                "name": "get_network_sm_device_softwares",
                "table_name": "software",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/softwares",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Get a list of softwares associated with a user
            {
                "name": "get_network_sm_user_softwares",
                "table_name": "software",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/users/{userId}/softwares",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "get_network_sm_users",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the splash authorization for a client, for each SSID they've associated with through splash. Only enabled SSIDs with Click-through splash enabled will be included. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_client_splash_authorization_status",
                "table_name": "splash_authorization_statu",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/{clientId}/splashAuthorizationStatus",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the splash login attempts for a network
            {
                "name": "get_network_splash_login_attempts",
                "table_name": "splash_login_attempt",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/splashLoginAttempts",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ssidNumber": "OPTIONAL_CONFIG",
                        # "loginIdentifier": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the MX SSIDs in a network
            {
                "name": "get_network_appliance_ssids",
                "table_name": "ssid",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/ssids",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a single MX SSID
            {
                "name": "get_network_appliance_ssid",
                "table_name": "ssid",
                "primary_key": "number",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/ssids/{number}",
                    "params": {
                        "number": {
                            "type": "resolve",
                            "resource": "get_network_appliance_ssids",
                            "field": "number",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the MR SSIDs in a network
            {
                "name": "get_network_wireless_ssids",
                "table_name": "ssid",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a single MR SSID
            {
                "name": "get_network_wireless_ssid",
                "table_name": "ssid",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the switch stacks in a network
            {
                "name": "get_network_switch_stacks",
                "table_name": "stack",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Show a switch stack
            {
                "name": "get_network_switch_stack",
                "table_name": "stack",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks/{switchStackId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "switchStackId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Order of Staged Upgrade Groups in a network
            {
                "name": "get_network_firmware_upgrades_staged_stages",
                "table_name": "stage",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/firmwareUpgrades/staged/stages",
                    "params": {
                        "networkId": {
                            "type": "resolve",
                            "resource": "get_network_firmware_upgrades",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Show VPN history stat for networks in an organization
            {
                "name": "get_organization_appliance_vpn_stats",
                "table_name": "stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/appliance/vpn/stats",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List static delegated prefixes for a network
            {
                "name": "get_network_appliance_prefixes_delegated_statics",
                "table_name": "static",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/prefixes/delegated/statics",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a static delegated prefix from a network
            {
                "name": "get_network_appliance_prefixes_delegated_static",
                "table_name": "static",
                "primary_key": "staticDelegatedPrefixId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/prefixes/delegated/statics/{staticDelegatedPrefixId}",
                    "params": {
                        "staticDelegatedPrefixId": {
                            "type": "resolve",
                            "resource": "get_network_appliance_prefixes_delegated_statics",
                            "field": "staticDelegatedPrefixId",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List layer 3 static routes for a switch
            {
                "name": "get_device_switch_routing_static_routes",
                "table_name": "static_route",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/routing/staticRoutes",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a layer 3 static route for a switch
            {
                "name": "get_device_switch_routing_static_route",
                "table_name": "static_route",
                "primary_key": "staticRouteId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/routing/staticRoutes/{staticRouteId}",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "staticRouteId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the static routes for an MX or teleworker network
            {
                "name": "get_network_appliance_static_routes",
                "table_name": "static_route",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/staticRoutes",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a static route for an MX or teleworker network
            {
                "name": "get_network_appliance_static_route",
                "table_name": "static_route",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/staticRoutes/{staticRouteId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "staticRouteId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List layer 3 static routes for a switch stack
            {
                "name": "get_network_switch_stack_routing_static_routes",
                "table_name": "static_route",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "switchStackId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a layer 3 static route for a switch stack
            {
                "name": "get_network_switch_stack_routing_static_route",
                "table_name": "static_route",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stacks/{switchStackId}/routing/staticRoutes/{staticRouteId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "switchStackId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "staticRouteId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the SSID statuses of an access point
            {
                "name": "get_device_wireless_status",
                "table_name": "statu",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/wireless/status",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the status for all the ports of a switch
            {
                "name": "get_device_switch_ports_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/ports/statuses",
                    "params": {
                        "serial": {
                            "type": "resolve",
                            "resource": "get_device_switch_ports",
                            "field": "portId",
                        },
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the uplink status of every Meraki MX and Z series appliances in the organization
            {
                "name": "get_organization_appliance_uplink_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/appliance/uplink/statuses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "iccids": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Show VPN status for networks in an organization
            {
                "name": "get_organization_appliance_vpn_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/appliance/vpn/statuses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Fetch onboarding status of cameras
            {
                "name": "get_organization_camera_onboarding_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/camera/onboarding/statuses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "serials": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the uplink status of every Meraki MG cellular gateway in the organization
            {
                "name": "get_organization_cellular_gateway_uplink_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/cellularGateway/uplink/statuses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "iccids": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the status of every Meraki device in the organization
            {
                "name": "get_organization_devices_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/organizations/{organizationId}/devices/statuses",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "statuses": "OPTIONAL_CONFIG",
                        # "productTypes": "OPTIONAL_CONFIG",
                        # "models": "OPTIONAL_CONFIG",
                        # "tags": "OPTIONAL_CONFIG",
                        # "tagsFilterType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the uplink status of every Meraki MX, MG and Z series devices in the organization
            {
                "name": "get_organization_uplinks_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/uplinks/statuses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                        # "serials": "OPTIONAL_CONFIG",
                        # "iccids": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Endpoint to see power status for wireless devices
            {
                "name": "get_organization_wireless_devices_ethernet_statuses",
                "table_name": "status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/wireless/devices/ethernet/statuses",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "networkIds": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the storm control configuration for a switch network
            {
                "name": "get_network_switch_storm_control",
                "table_name": "storm_control",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stormControl",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns STP settings
            {
                "name": "get_network_switch_stp",
                "table_name": "stp",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/stp",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the DHCP subnet information for an appliance
            {
                "name": "get_device_appliance_dhcp_subnets",
                "table_name": "subnet",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/appliance/dhcp/subnets",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the subnet pool and mask configured for MGs in the network.
            {
                "name": "get_network_cellular_gateway_subnet_pool",
                "table_name": "subnet_pool",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/cellularGateway/subnetPool",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the syslog servers for a network
            {
                "name": "get_network_syslog_servers",
                "table_name": "syslog_server",
                "endpoint": {
                    "data_selector": "servers",
                    "path": "/networks/{networkId}/syslogServers",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the target groups in this network
            {
                "name": "get_network_sm_target_groups",
                "table_name": "target_group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/targetGroups",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "withDetails": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return a target group
            {
                "name": "get_network_sm_target_group",
                "table_name": "target_group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/targetGroups/{targetGroupId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "targetGroupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "withDetails": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the third party VPN peers for an organization
            {
                "name": "get_organization_appliance_vpn_third_party_vpn_peers",
                "table_name": "third_party_vpn_peer",
                "endpoint": {
                    "data_selector": "peers",
                    "path": "/organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Return the traffic analysis data for this network. Traffic analysis with hostname visibility must be enabled on the network.
            {
                "name": "get_network_traffic",
                "table_name": "traffic",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/traffic",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "deviceType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the traffic analysis settings for a network
            {
                "name": "get_network_traffic_analysis",
                "table_name": "traffic_analysi",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/trafficAnalysis",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the client's network traffic data over time. Usage data is in kilobytes. This endpoint requires detailed traffic analysis to be enabled on the Network-wide > General page. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_client_traffic_history",
                "table_name": "traffic_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/{clientId}/trafficHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Display the traffic shaping settings for an MX network
            {
                "name": "get_network_appliance_traffic_shaping",
                "table_name": "traffic_shaping",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/trafficShaping",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List Trusted Access Configs
            {
                "name": "get_network_sm_trusted_access_configs",
                "table_name": "trusted_access_config",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/trustedAccessConfigs",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the list of servers trusted by Dynamic ARP Inspection on this network. These are also known as whitelisted snoop entries
            {
                "name": "get_network_switch_dhcp_server_policy_arp_inspection_trusted_servers",
                "table_name": "trusted_server",
                "primary_key": "trustedServerId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/switch/dhcpServerPolicy/arpInspection/trustedServers",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get firmware upgrade information for an organization
            {
                "name": "get_organization_firmware_upgrades",
                "table_name": "upgrade",
                "primary_key": "upgradeId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/firmware/upgrades",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                        # "productType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the uplink settings for your MG network.
            {
                "name": "get_network_cellular_gateway_uplink",
                "table_name": "uplink",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/cellularGateway/uplink",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device's hardware capabilities.  For more information on your device's hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]
            {
                "name": "get_network_appliance_traffic_shaping_uplink_bandwidth",
                "table_name": "uplink_bandwidth",
                "endpoint": {
                    "data_selector": "bandwidthLimits",
                    "path": "/networks/{networkId}/appliance/trafficShaping/uplinkBandwidth",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Show uplink selection settings for an MX network
            {
                "name": "get_network_appliance_traffic_shaping_uplink_selection",
                "table_name": "uplink_selection",
                "endpoint": {
                    "data_selector": "vpnTrafficUplinkPreferences",
                    "path": "/networks/{networkId}/appliance/trafficShaping/uplinkSelection",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
            {
                "name": "get_organization_devices_uplinks_loss_and_latency",
                "table_name": "uplinks_loss_and_latency",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/devices/uplinksLossAndLatency",
                    "params": {
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "uplink": "OPTIONAL_CONFIG",
                        # "ip": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the sent and received bytes for each uplink of a network.
            {
                "name": "get_network_appliance_uplinks_usage_history",
                "table_name": "usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/uplinks/usageHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the usage histories for clients. Usage data is in kilobytes. Clients can be identified by client keys or either the MACs or IPs depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_clients_usage_histories",
                "table_name": "usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/usageHistories",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clients": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "ssidNumber": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return the client's daily usage history. Usage data is in kilobytes. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.
            {
                "name": "get_network_client_usage_history",
                "table_name": "usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/clients/{clientId}/usageHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "clientId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return AP usage over time for a device or network client
            {
                "name": "get_network_wireless_usage_history",
                "table_name": "usage_history",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/usageHistory",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "t0": "OPTIONAL_CONFIG",
                        # "t1": "OPTIONAL_CONFIG",
                        # "timespan": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "autoResolution": "OPTIONAL_CONFIG",
                        # "clientId": "OPTIONAL_CONFIG",
                        # "deviceSerial": "OPTIONAL_CONFIG",
                        # "apTag": "OPTIONAL_CONFIG",
                        # "band": "OPTIONAL_CONFIG",
                        # "ssid": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the owners in an SM network with various specified fields and filters
            {
                "name": "get_network_sm_users",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/users",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ids": "OPTIONAL_CONFIG",
                        # "usernames": "OPTIONAL_CONFIG",
                        # "emails": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List User Access Devices and its Trusted Access Connections
            {
                "name": "get_network_sm_user_access_devices",
                "table_name": "user_access_device",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/userAccessDevices",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "startingAfter": "OPTIONAL_CONFIG",
                        # "endingBefore": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns video link to the specified camera. If a timestamp is supplied, it links to that timestamp.
            {
                "name": "get_device_camera_video_link",
                "table_name": "video_link",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/videoLink",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "timestamp": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # List the VLANs for an MX network
            {
                "name": "get_network_appliance_vlans",
                "table_name": "vlan",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/vlans",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return a VLAN
            {
                "name": "get_network_appliance_vlan",
                "table_name": "vlan",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/vlans/{vlanId}",
                    "params": {
                        "vlanId": {
                            "type": "resolve",
                            "resource": "get_network_appliance_vlans",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return prefixes assigned to all IPv6 enabled VLANs on an appliance.
            {
                "name": "get_device_appliance_prefixes_delegated_vlan_assignments",
                "table_name": "vlan_assignment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/appliance/prefixes/delegated/vlanAssignments",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the VPN settings for the SSID.
            {
                "name": "get_network_wireless_ssid_vpn",
                "table_name": "vpn",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/wireless/ssids/{number}/vpn",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the firewall rules for an organization's site-to-site VPN
            {
                "name": "get_organization_appliance_vpn_vpn_firewall_rules",
                "table_name": "vpn_firewall_rule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/appliance/vpn/vpnFirewallRules",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # List the VPP accounts in the organization
            {
                "name": "get_organization_sm_vpp_accounts",
                "table_name": "vpp_account",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/sm/vppAccounts",
                    "params": {
                        "organizationId": {
                            "type": "resolve",
                            "resource": "get_organizations",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Get a hash containing the unparsed token of the VPP account with the given ID
            {
                "name": "get_organization_sm_vpp_account",
                "table_name": "vpp_account",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations/{organizationId}/sm/vppAccounts/{vppAccountId}",
                    "params": {
                        "vppAccountId": {
                            "type": "resolve",
                            "resource": "get_organization_sm_vpp_accounts",
                            "field": "id",
                        },
                        "organizationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return warm spare configuration for a switch
            {
                "name": "get_device_switch_warm_spare",
                "table_name": "warm_spare",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/switch/warmSpare",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return MX warm spare settings
            {
                "name": "get_network_appliance_warm_spare",
                "table_name": "warm_spare",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/appliance/warmSpare",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Return the status of a webhook test for a network
            {
                "name": "get_network_webhooks_webhook_test",
                "table_name": "webhook_test",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/webhooks/webhookTests/{webhookTestId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "webhookTestId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns wireless profile assigned to the given camera
            {
                "name": "get_device_camera_wireless_profiles",
                "table_name": "wireless_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/wirelessProfiles",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the camera wireless profiles for this network.
            {
                "name": "get_network_camera_wireless_profiles",
                "table_name": "wireless_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/camera/wirelessProfiles",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a single camera wireless profile.
            {
                "name": "get_network_camera_wireless_profile",
                "table_name": "wireless_profile",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/camera/wirelessProfiles/{wirelessProfileId}",
                    "params": {
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "wirelessProfileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List the saved SSID names on a device
            {
                "name": "get_network_sm_device_wlan_lists",
                "table_name": "wlan_list",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{networkId}/sm/devices/{deviceId}/wlanLists",
                    "params": {
                        "deviceId": {
                            "type": "resolve",
                            "resource": "get_network_sm_devices",
                            "field": "id",
                        },
                        "networkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all configured analytic zones for this camera
            {
                "name": "get_device_camera_analytics_zones",
                "table_name": "zone",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/devices/{serial}/camera/analytics/zones",
                    "params": {
                        "serial": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
