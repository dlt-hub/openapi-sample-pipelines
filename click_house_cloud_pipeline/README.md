# click_house_cloud pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/click_house_cloud.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /v1/organizations/:organizationId/activities_ 
  *resource*: v_1_organizations_organization_id_activities  
  *description*: Returns a list of all organization activities.
* _GET /v1/organizations/:organizationId/activities/:activityId_ 
  *resource*: v_1_organizations_organization_id_activities_activity_id  
  *description*: Returns a single organization activity by ID.
* _GET /v1/organizations/:organizationId/keys_ 
  *resource*: v_1_organizations_organization_id_keys  
  *description*: Returns a list of all keys in the organization.
* _GET /v1/organizations/:organizationId/services/:serviceId/backups_ 
  *resource*: v_1_organizations_organization_id_services_service_id_backups  
  *description*: Returns a list of all backups for the service. The most recent backups comes first in the list.
* _GET /v1/organizations/:organizationId/services/:serviceId/backups/:backupId_ 
  *resource*: v_1_organizations_organization_id_services_service_id_backups_backup_id  
  *description*: Returns a single backup info.
* _GET /v1/organizations/:organizationId/invitations_ 
  *resource*: v_1_organizations_organization_id_invitations  
  *description*: Returns list of all organization invitations.
* _GET /v1/organizations/:organizationId/invitations/:invitationId_ 
  *resource*: v_1_organizations_organization_id_invitations_invitation_id  
  *description*: Returns details for a single organization invitation.
* _GET /v1/organizations/:organizationId/keys/:keyId_ 
  *resource*: v_1_organizations_organization_id_keys_key_id  
  *description*: Returns a single key details.
* _GET /v1/organizations/:organizationId/members_ 
  *resource*: v_1_organizations_organization_id_members  
  *description*: Returns a list of all members in the organization.
* _GET /v1/organizations_ 
  *resource*: v1_organizations  
  *description*: Returns a list with a single organization associated with the API key in the request.
* _GET /v1/organizations/:organizationId_ 
  *resource*: v_1_organizations_organization_id  
  *description*: Returns details of a single organization. In order to get the details, the auth key must belong to the organization.
* _GET /v1/organizations/:organizationId/services/:serviceId/privateEndpointConfig_ 
  *resource*: v_1_organizations_organization_id_services_service_id_private_endpoint_config  
  *description*: Information required to set up a private endpoint
* _GET /v1/organizations/:organizationId/privateEndpointConfig_ 
  *resource*: v_1_organizations_organization_id_private_endpoint_config  
  *description*: Information required to set up a private endpoint
* _GET /v1/organizations/:organizationId/services/:serviceId/prometheus_ 
  *resource*: v_1_organizations_organization_id_services_service_id_prometheus  
  *description*: Returns prometheus metrics for a service. Please contact support to enable this feature.
* _GET /v1/organizations/:organizationId/services_ 
  *resource*: v_1_organizations_organization_id_services  
  *description*: Returns a list of all services in the organization.
* _GET /v1/organizations/:organizationId/services/:serviceId_ 
  *resource*: v_1_organizations_organization_id_services_service_id  
  *description*: Returns a service that belongs to the organization
* _GET /v1/organizations/:organizationId/members/:userId_ 
  *resource*: v_1_organizations_organization_id_members_user_id  
  *description*: Returns a single organization member details.
