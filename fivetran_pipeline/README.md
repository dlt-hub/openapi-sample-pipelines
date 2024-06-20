# fivetran pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/fivetran.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['username', 'password'] in your 
secrets.toml.

## Available resources
* _GET /v1/connectors/{connectorId}/certificates_ 
  *resource*: get_connector_certificates_list  
  *description*: Returns the list of approved certificates for specified connector.
* _GET /v1/destinations/{destinationId}/certificates_ 
  *resource*: get_destination_certificates_list  
  *description*: Returns the list of approved certificates for specified destination.
* _GET /v1/destinations/{destinationId}/certificates/{hash}_ 
  *resource*: get_destination_certificate_details  
  *description*: Returns details of the certificate approved for specified destination with specified hash.
* _GET /v1/connectors/{connectorId}/certificates/{hash}_ 
  *resource*: get_connector_certificate_details  
  *description*: Returns details of the certificate approved for specified connector with specified hash.
* _GET /v1/connectors/{connectorId}/schemas/{schema}/tables/{table}/columns_ 
  *resource*: connector_column_config  
  *description*: Returns the source table columns config for an existing connector within your Fivetran account
* _GET /v1/proxy/{agentId}/connections_ 
  *resource*: get_proxy_agent_connections  
  *description*: Returns all connections attached to the proxy agent.
* _GET /v1/teams/{teamId}/connectors_ 
  *resource*: get_team_memberships_in_connectors  
  *description*: Returns connector memberships within a team.
* _GET /v1/users/{userId}/connectors/{connectorId}_ 
  *resource*: get_user_membership_in_connector  
  *description*: Returns a connector membership object.
* _GET /v1/connectors/{connectorId}_ 
  *resource*: connector_details  
  *description*: Returns a connector object if a valid identifier was provided
* _GET /v1/teams/{teamId}/connectors/{connectorId}_ 
  *resource*: get_team_membership_in_connector  
  *description*: Returns a connector membership within a team
* _GET /v1/groups/{groupId}/connectors_ 
  *resource*: list_all_connectors_in_group  
  *description*: Returns a list of information about all connectors within a group in your Fivetran account.
* _GET /v1/users/{userId}/connectors_ 
  *resource*: get_user_memberships_in_connectors  
  *description*: Returns all connector membership objects for a user within your Fivetran account
* _GET /v1/metadata/connector-types/{service}_ 
  *resource*: metadata_connector_config  
  *description*: Returns metadata of configuration parameters and authorization parameters for a specified connector type.
* _GET /v1/metadata/connector-types_ 
  *resource*: metadata_connectors  
  *description*: Returns all available source types within your Fivetran account. This endpoint makes it easier to display Fivetran connectors within your application because it provides metadata including the proper source name ('Facebook Ads' instead of 'facebook_ads'), the source icon, and links to Fivetran resources. As we update source names and icons, that metadata will automatically update within this endpoint
* _GET /v1/destinations/{destinationId}_ 
  *resource*: destination_details  
  *description*: Returns a destination object if a valid identifier was provided.
* _GET /v1/external-logging/{logId}_ 
  *resource*: get_log_service_details  
  *description*: Returns a logging service object if a valid identifier was provided.
* _GET /v1/destinations/{destinationId}/fingerprints/{hash}_ 
  *resource*: get_destination_fingerprint_details  
  *description*: Returns SSH fingerprint details approved for specified destination with specified hash
* _GET /v1/connectors/{connectorId}/fingerprints/{hash}_ 
  *resource*: get_connector_fingerprint_details  
  *description*: Returns SSH fingerprint details approved for specified connector with specified hash
* _GET /v1/destinations/{destinationId}/fingerprints_ 
  *resource*: get_destination_fingerprints_list  
  *description*: Returns the list of approved SSH fingerprints for specified destination
* _GET /v1/connectors/{connectorId}/fingerprints_ 
  *resource*: get_connector_fingerprints_list  
  *description*: Returns the list of approved SSH fingerprints for specified connector
* _GET /v1/users/{userId}/groups_ 
  *resource*: get_user_memberships_in_groups  
  *description*: Returns all group membership objects for a user within your Fivetran account.
* _GET /v1/teams/{teamId}/groups_ 
  *resource*: get_team_memberships_in_groups  
  *description*: Returns a group membership within a team
* _GET /v1/groups/{groupId}_ 
  *resource*: group_details  
  *description*: Returns a group object if a valid identifier was provided.
* _GET /v1/teams/{teamId}/groups/{groupId}_ 
  *resource*: get_team_membership_in_group  
  *description*: Returns a group membership within a team.
* _GET /v1/groups_ 
  *resource*: list_all_groups  
  *description*: Returns a list of all groups within your Fivetran account.
* _GET /v1/users/{userId}/groups/{groupId}_ 
  *resource*: get_user_membership_in_group  
  *description*: Returns a group membership object.
* _GET /v1/account/info_ 
  *resource*: get_account_info  
  *description*: Returns information about current account from API key.
* _GET /v1/local-processing-agents/{agentId}_ 
  *resource*: get_local_processing_agent  
  *description*: Returns Local Processing Agent Details.
* _GET /v1/local-processing-agents_ 
  *resource*: get_local_processing_agent_list  
  *description*: Returns list of all Local Processing Agents within your Fivetran account, along with usage. Optionally filtered to a single group.
* _GET /v1/dbt/models_ 
  *resource*: list_dbt_project_models  
  *description*: Returns a list of all dbt Models within dbt Project.
* _GET /v1/dbt/projects/{projectId}/models_ 
  *resource*: list_dbt_project_models_deprecated  
  *description*: Returns a list of all dbt Models within dbt Project. (Deprecated)
* _GET /v1/dbt/models/{modelId}_ 
  *resource*: dbt_model_details  
  *description*: Returns a dbt Model details if a valid identifier was provided.
* _GET /v1/groups/{groupId}/private-links_ 
  *resource*: get_private_links  
  *description*: Returns a list of all private links.
* _GET /v1/private-links/{privateLinkId}_ 
  *resource*: get_private_link_details  
  *description*: Returns a private link object if a valid identifier was provided.
* _GET /v1/dbt/projects/{projectId}_ 
  *resource*: dbt_project_details  
  *description*: Returns a dbt Project details if a valid identifier was provided.
* _GET /v1/dbt/projects_ 
  *resource*: list_dbt_projects  
  *description*: Returns a list of all dbt Projects within your Fivetran account.
* _GET /v1/proxy_ 
  *resource*: get_proxy_agent  
  *description*: Returns a list of all proxy agents.
* _GET /v1/proxy/{agentId}_ 
  *resource*: get_proxy_agent_details  
  *description*: Returns a proxy agent object if a valid identifier was provided.
* _GET /v1/groups/{groupId}/public-key_ 
  *resource*: group_ssh_public_key  
  *description*: Returns public key from SSH key pair associated with the group.
* _GET /v1/roles_ 
  *resource*: list_all_roles  
  *description*: Returns a list of all predefined and custom roles within your Fivetran account.
* _GET /v1/connectors/{connectorId}/schemas_ 
  *resource*: connector_schema_config  
  *description*: Returns the connector schema config for an existing connector within your Fivetran account
* _GET /v1/groups/{groupId}/service-account_ 
  *resource*: group_service_account  
  *description*: Returns Fivetran service account associated with the group.
* _GET /v1/connectors/{connectorId}/state_ 
  *resource*: connector_state  
  *description*: Returns the connector state. This endpoint is only supported for function connectors.
* _GET /v1/teams/{teamId}_ 
  *resource*: team_details  
  *description*: Returns information for a given team within your Fivetran account
* _GET /v1/teams_ 
  *resource*: list_all_teams  
  *description*: Returns a list of all teams within your Fivetran account
* _GET /v1/dbt/transformations/{transformationId}_ 
  *resource*: dbt_transformation_details  
  *description*: Returns a dbt Transformation details if a valid identifier was provided.
* _GET /v1/dbt/transformations_ 
  *resource*: list_dbt_project_transformations  
  *description*: Returns a list of all dbt Transformations within dbt Project.
* _GET /v1/dbt/projects/{projectId}/transformations_ 
  *resource*: list_dbt_project_transformations_deprecated  
  *description*: Returns a list of all dbt Transformations within dbt Project. (Deprecated)
* _GET /v1/teams/{teamId}/users/{userId}_ 
  *resource*: get_user_in_team  
  *description*: Returns the user role a user has within a team
* _GET /v1/users_ 
  *resource*: list_all_users  
  *description*: Returns a list of all users within your Fivetran account.
* _GET /v1/users/{userId}_ 
  *resource*: user_details  
  *description*: Returns a user object if a valid identifier was provided.
* _GET /v1/groups/{groupId}/users_ 
  *resource*: list_all_users_in_group  
  *description*: Returns a list of information about all users within a group in your Fivetran account.
* _GET /v1/teams/{teamId}/users_ 
  *resource*: list_users_in_team  
  *description*: Returns a list of users and their roles within a team in your Fivetran account
* _GET /v1/webhooks/{webhookId}_ 
  *resource*: webhook_details  
  *description*: This endpoint allows you to retrieve details of the existing webhook for a given identifier
* _GET /v1/webhooks_ 
  *resource*: list_all_webhooks  
  *description*: The endpoint allows you to retrieve the list of existing webhooks available for the current account
