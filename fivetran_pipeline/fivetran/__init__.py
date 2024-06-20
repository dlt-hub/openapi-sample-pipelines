from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="fivetran_source", max_table_nesting=2)
def fivetran_source(
    username: str = dlt.secrets.value,
    password: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "http_basic",
                "username": username,
                "password": password,
            },
        },
        "resources": [
            # Returns the list of approved certificates for specified connector.
            {
                "name": "get_connector_certificates_list",
                "table_name": "certificate",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/certificates",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of approved certificates for specified destination.
            {
                "name": "get_destination_certificates_list",
                "table_name": "certificate",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/destinations/{destinationId}/certificates",
                    "params": {
                        "destinationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns details of the certificate approved for specified destination with specified hash.
            {
                "name": "get_destination_certificate_details",
                "table_name": "certificate",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/destinations/{destinationId}/certificates/{hash}",
                    "params": {
                        "destinationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns details of the certificate approved for specified connector with specified hash.
            {
                "name": "get_connector_certificate_details",
                "table_name": "certificate",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/certificates/{hash}",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the source table columns config for an existing connector within your Fivetran account
            {
                "name": "connector_column_config",
                "table_name": "column",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/schemas/{schema}/tables/{table}/columns",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "schema": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "table": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all connections attached to the proxy agent.
            {
                "name": "get_proxy_agent_connections",
                "table_name": "connection",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/proxy/{agentId}/connections",
                    "params": {
                        "agentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns connector memberships within a team.
            {
                "name": "get_team_memberships_in_connectors",
                "table_name": "connector",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}/connectors",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a connector membership object.
            {
                "name": "get_user_membership_in_connector",
                "table_name": "connector",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{userId}/connectors/{connectorId}",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a connector object if a valid identifier was provided
            {
                "name": "connector_details",
                "table_name": "connector",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a connector membership within a team
            {
                "name": "get_team_membership_in_connector",
                "table_name": "connector",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}/connectors/{connectorId}",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of information about all connectors within a group in your Fivetran account.
            {
                "name": "list_all_connectors_in_group",
                "table_name": "connector",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups/{groupId}/connectors",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "schema": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all connector membership objects for a user within your Fivetran account
            {
                "name": "get_user_memberships_in_connectors",
                "table_name": "connector",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{userId}/connectors",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns metadata of configuration parameters and authorization parameters for a specified connector type.
            {
                "name": "metadata_connector_config",
                "table_name": "connector_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/metadata/connector-types/{service}",
                    "params": {
                        "service": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all available source types within your Fivetran account. This endpoint makes it easier to display Fivetran connectors within your application because it provides metadata including the proper source name ('Facebook Ads' instead of 'facebook_ads'), the source icon, and links to Fivetran resources. As we update source names and icons, that metadata will automatically update within this endpoint
            {
                "name": "metadata_connectors",
                "table_name": "connector_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/metadata/connector-types",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a destination object if a valid identifier was provided.
            {
                "name": "destination_details",
                "table_name": "destination",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/destinations/{destinationId}",
                    "params": {
                        "destinationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a logging service object if a valid identifier was provided.
            {
                "name": "get_log_service_details",
                "table_name": "external_logging",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/external-logging/{logId}",
                    "params": {
                        "logId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns SSH fingerprint details approved for specified destination with specified hash
            {
                "name": "get_destination_fingerprint_details",
                "table_name": "fingerprint",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/destinations/{destinationId}/fingerprints/{hash}",
                    "params": {
                        "destinationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns SSH fingerprint details approved for specified connector with specified hash
            {
                "name": "get_connector_fingerprint_details",
                "table_name": "fingerprint",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/fingerprints/{hash}",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of approved SSH fingerprints for specified destination
            {
                "name": "get_destination_fingerprints_list",
                "table_name": "fingerprint",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/destinations/{destinationId}/fingerprints",
                    "params": {
                        "destinationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of approved SSH fingerprints for specified connector
            {
                "name": "get_connector_fingerprints_list",
                "table_name": "fingerprint",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/fingerprints",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all group membership objects for a user within your Fivetran account.
            {
                "name": "get_user_memberships_in_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{userId}/groups",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a group membership within a team
            {
                "name": "get_team_memberships_in_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}/groups",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a group object if a valid identifier was provided.
            {
                "name": "group_details",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups/{groupId}",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a group membership within a team.
            {
                "name": "get_team_membership_in_group",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}/groups/{groupId}",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all groups within your Fivetran account.
            {
                "name": "list_all_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a group membership object.
            {
                "name": "get_user_membership_in_group",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{userId}/groups/{groupId}",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns information about current account from API key.
            {
                "name": "get_account_info",
                "table_name": "info",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/account/info",
                    "paginator": "auto",
                },
            },
            # Returns Local Processing Agent Details.
            {
                "name": "get_local_processing_agent",
                "table_name": "local_processing_agent",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/local-processing-agents/{agentId}",
                    "params": {
                        "agentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns list of all Local Processing Agents within your Fivetran account, along with usage. Optionally filtered to a single group.
            {
                "name": "get_local_processing_agent_list",
                "table_name": "local_processing_agent",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/local-processing-agents",
                    "params": {
                        # the parameters below can optionally be configured
                        # "groupId": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all dbt Models within dbt Project.
            {
                "name": "list_dbt_project_models",
                "table_name": "model",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/models",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all dbt Models within dbt Project. (Deprecated)
            {
                "name": "list_dbt_project_models_deprecated",
                "table_name": "model",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/projects/{projectId}/models",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a dbt Model details if a valid identifier was provided.
            {
                "name": "dbt_model_details",
                "table_name": "model",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/models/{modelId}",
                    "params": {
                        "modelId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all private links.
            {
                "name": "get_private_links",
                "table_name": "private_link",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups/{groupId}/private-links",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a private link object if a valid identifier was provided.
            {
                "name": "get_private_link_details",
                "table_name": "private_link",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/private-links/{privateLinkId}",
                    "params": {
                        "privateLinkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a dbt Project details if a valid identifier was provided.
            {
                "name": "dbt_project_details",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/projects/{projectId}",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all dbt Projects within your Fivetran account.
            {
                "name": "list_dbt_projects",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/projects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "group_id": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all proxy agents.
            {
                "name": "get_proxy_agent",
                "table_name": "proxy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/proxy",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a proxy agent object if a valid identifier was provided.
            {
                "name": "get_proxy_agent_details",
                "table_name": "proxy_agent_response",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/proxy/{agentId}",
                    "params": {
                        "agentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns public key from SSH key pair associated with the group.
            {
                "name": "group_ssh_public_key",
                "table_name": "public_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups/{groupId}/public-key",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all predefined and custom roles within your Fivetran account.
            {
                "name": "list_all_roles",
                "table_name": "role",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/roles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the connector schema config for an existing connector within your Fivetran account
            {
                "name": "connector_schema_config",
                "table_name": "schema",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/schemas",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns Fivetran service account associated with the group.
            {
                "name": "group_service_account",
                "table_name": "service_account",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups/{groupId}/service-account",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the connector state. This endpoint is only supported for function connectors.
            {
                "name": "connector_state",
                "table_name": "state",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/connectors/{connectorId}/state",
                    "params": {
                        "connectorId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns information for a given team within your Fivetran account
            {
                "name": "team_details",
                "table_name": "team",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all teams within your Fivetran account
            {
                "name": "list_all_teams",
                "table_name": "team",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a dbt Transformation details if a valid identifier was provided.
            {
                "name": "dbt_transformation_details",
                "table_name": "transformation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/transformations/{transformationId}",
                    "params": {
                        "transformationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all dbt Transformations within dbt Project.
            {
                "name": "list_dbt_project_transformations",
                "table_name": "transformation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/transformations",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all dbt Transformations within dbt Project. (Deprecated)
            {
                "name": "list_dbt_project_transformations_deprecated",
                "table_name": "transformation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/dbt/projects/{projectId}/transformations",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the user role a user has within a team
            {
                "name": "get_user_in_team",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}/users/{userId}",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all users within your Fivetran account.
            {
                "name": "list_all_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a user object if a valid identifier was provided.
            {
                "name": "user_details",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/users/{userId}",
                    "params": {
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of information about all users within a group in your Fivetran account.
            {
                "name": "list_all_users_in_group",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/groups/{groupId}/users",
                    "params": {
                        "groupId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users and their roles within a team in your Fivetran account
            {
                "name": "list_users_in_team",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/teams/{teamId}/users",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint allows you to retrieve details of the existing webhook for a given identifier
            {
                "name": "webhook_details",
                "table_name": "webhook",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/webhooks/{webhookId}",
                    "params": {
                        "webhookId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # The endpoint allows you to retrieve the list of existing webhooks available for the current account
            {
                "name": "list_all_webhooks",
                "table_name": "webhook",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/webhooks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
