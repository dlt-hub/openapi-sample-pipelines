from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="click_house_cloud_source", max_table_nesting=2)
def click_house_cloud_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Returns a list of all organization activities.
            {
                "name": "v_1_organizations_organization_id_activities",
                "table_name": "activity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations/:organizationId/activities",
                    "paginator": "auto",
                },
            },
            # Returns a single organization activity by ID.
            {
                "name": "v_1_organizations_organization_id_activities_activity_id",
                "table_name": "activity_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/activities/:activityId",
                    "paginator": "auto",
                },
            },
            # Returns a list of all keys in the organization.
            {
                "name": "v_1_organizations_organization_id_keys",
                "table_name": "api_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations/:organizationId/keys",
                    "paginator": "auto",
                },
            },
            # Returns a list of all backups for the service. The most recent backups comes first in the list.
            {
                "name": "v_1_organizations_organization_id_services_service_id_backups",
                "table_name": "backup",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations/:organizationId/services/:serviceId/backups",
                    "paginator": "auto",
                },
            },
            # Returns a single backup info.
            {
                "name": "v_1_organizations_organization_id_services_service_id_backups_backup_id",
                "table_name": "backup_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/services/:serviceId/backups/:backupId",
                    "paginator": "auto",
                },
            },
            # Returns list of all organization invitations.
            {
                "name": "v_1_organizations_organization_id_invitations",
                "table_name": "invitation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations/:organizationId/invitations",
                    "paginator": "auto",
                },
            },
            # Returns details for a single organization invitation.
            {
                "name": "v_1_organizations_organization_id_invitations_invitation_id",
                "table_name": "invitation_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/invitations/:invitationId",
                    "paginator": "auto",
                },
            },
            # Returns a single key details.
            {
                "name": "v_1_organizations_organization_id_keys_key_id",
                "table_name": "key_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/keys/:keyId",
                    "paginator": "auto",
                },
            },
            # Returns a list of all members in the organization.
            {
                "name": "v_1_organizations_organization_id_members",
                "table_name": "member",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations/:organizationId/members",
                    "paginator": "auto",
                },
            },
            # Returns a list with a single organization associated with the API key in the request.
            {
                "name": "v1_organizations",
                "table_name": "organization",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations",
                    "paginator": "auto",
                },
            },
            # Returns details of a single organization. In order to get the details, the auth key must belong to the organization.
            {
                "name": "v_1_organizations_organization_id",
                "table_name": "organization_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId",
                    "paginator": "auto",
                },
            },
            # Information required to set up a private endpoint
            {
                "name": "v_1_organizations_organization_id_services_service_id_private_endpoint_config",
                "table_name": "private_endpoint_config",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/services/:serviceId/privateEndpointConfig",
                    "paginator": "auto",
                },
            },
            # Information required to set up a private endpoint
            {
                "name": "v_1_organizations_organization_id_private_endpoint_config",
                "table_name": "private_endpoint_config",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/privateEndpointConfig",
                    "params": {
                        "Cloud provider identifier": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "Cloud provider region": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns prometheus metrics for a service. Please contact support to enable this feature.
            {
                "name": "v_1_organizations_organization_id_services_service_id_prometheus",
                "table_name": "prometheu",
                "endpoint": {
                    "path": "/v1/organizations/:organizationId/services/:serviceId/prometheus",
                    "paginator": "auto",
                },
            },
            # Returns a list of all services in the organization.
            {
                "name": "v_1_organizations_organization_id_services",
                "table_name": "service",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "result",
                    "path": "/v1/organizations/:organizationId/services",
                    "paginator": "auto",
                },
            },
            # Returns a service that belongs to the organization
            {
                "name": "v_1_organizations_organization_id_services_service_id",
                "table_name": "service_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/services/:serviceId",
                    "paginator": "auto",
                },
            },
            # Returns a single organization member details.
            {
                "name": "v_1_organizations_organization_id_members_user_id",
                "table_name": "user_id",
                "primary_key": "requestId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/organizations/:organizationId/members/:userId",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
