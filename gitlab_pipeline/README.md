# gitlab pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/gitlab.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /application/appearance_ 
  *resource*: get_api_v4_application_appearance  
  *description*: Get the current appearance
* _GET /applications_ 
  *resource*: get_api_v4_applications  
  *description*: List all registered applications
* _GET /avatar_ 
  *resource*: get_api_v4_avatar  
  *description*: Return avatar url for a user
* _GET /groups/{id}/badges/{badge_id}_ 
  *resource*: get_api_v4_groups_id_badges_badge_id  
  *description*: This feature was introduced in GitLab 10.6.
* _GET /groups/{id}/badges_ 
  *resource*: get_api_v4_groups_id_badges  
  *description*: This feature was introduced in GitLab 10.6.
* _GET /projects/{id}/badges/{badge_id}_ 
  *resource*: get_api_v4_projects_id_badges_badge_id  
  *description*: This feature was introduced in GitLab 10.6.
* _GET /projects/{id}/badges_ 
  *resource*: get_api_v4_projects_id_badges  
  *description*: This feature was introduced in GitLab 10.6.
* _GET /groups/{id}/badges/render_ 
  *resource*: get_api_v4_groups_id_badges_render  
  *description*: This feature was introduced in GitLab 10.6.
* _GET /projects/{id}/badges/render_ 
  *resource*: get_api_v4_projects_id_badges_render  
  *description*: This feature was introduced in GitLab 10.6.
* _GET /admin/batched_background_migrations/{id}_ 
  *resource*: get_api_v4_admin_batched_background_migrations_id  
  *description*: Retrieve a batched background migration
* _GET /admin/batched_background_migrations_ 
  *resource*: get_api_v4_admin_batched_background_migrations  
  *description*: Get the list of batched background migrations
* _GET /projects/{id}/repository/branches/{branch}_ 
  *resource*: get_api_v4_projects_id_repository_branches_branch  
  *description*: Get a single repository branch
* _GET /projects/{id}/repository/branches_ 
  *resource*: get_api_v4_projects_id_repository_branches  
  *description*: Get a project repository branches
* _GET /broadcast_messages/{id}_ 
  *resource*: get_api_v4_broadcast_messages_id  
  *description*: This feature was introduced in GitLab 8.12.
* _GET /broadcast_messages_ 
  *resource*: get_api_v4_broadcast_messages  
  *description*: This feature was introduced in GitLab 8.12.
* _GET /bulk_imports/{import_id}_ 
  *resource*: get_api_v4_bulk_imports_import_id  
  *description*: This feature was introduced in GitLab 14.1.
* _GET /bulk_imports_ 
  *resource*: get_api_v4_bulk_imports  
  *description*: This feature was introduced in GitLab 14.1.
* _GET /bulk_imports/{import_id}/entities/{entity_id}_ 
  *resource*: get_api_v4_bulk_imports_import_id_entities_entity_id  
  *description*: This feature was introduced in GitLab 14.1.
* _GET /bulk_imports/{import_id}/entities_ 
  *resource*: get_api_v4_bulk_imports_import_id_entities  
  *description*: This feature was introduced in GitLab 14.1.
* _GET /bulk_imports/entities_ 
  *resource*: get_api_v4_bulk_imports_entities  
  *description*: This feature was introduced in GitLab 14.1.
* _GET /admin/ci/variables/{key}_ 
  *resource*: get_api_v4_admin_ci_variables_key  
  *description*: Get the details of a specific instance-level variable
* _GET /admin/ci/variables_ 
  *resource*: get_api_v4_admin_ci_variables  
  *description*: List all instance-level variables
* _GET /admin/clusters/{cluster_id}_ 
  *resource*: get_api_v4_admin_clusters_cluster_id  
  *description*: This feature was introduced in GitLab 13.2. Returns a single instance cluster.
* _GET /admin/clusters_ 
  *resource*: get_api_v4_admin_clusters  
  *description*: This feature was introduced in GitLab 13.2. Returns a list of instance clusters.
* _GET /groups/{id}/access_requests_ 
  *resource*: get_api_v4_groups_id_access_requests  
  *description*: This feature was introduced in GitLab 8.11.
* _GET /projects/{id}/access_requests_ 
  *resource*: get_api_v4_projects_id_access_requests  
  *description*: This feature was introduced in GitLab 8.11.
* _GET /admin/databases/{database_name}/dictionary/tables/{table_name}_ 
  *resource*: get_api_v4_admin_databases_database_name_dictionary_tables_table_name  
  *description*: Retrieve dictionary details
* _GET /projects/{id}/jobs_ 
  *resource*: list_project_jobs  
* _GET /projects/{id}/jobs/{job_id}_ 
  *resource*: get_single_job  
* _GET /metadata_ 
  *resource*: get_api_v4_metadata  
  *description*: This feature was introduced in GitLab 15.2.
* _GET /version_ 
  *resource*: get_api_v4_version  
  *description*: This feature was introduced in GitLab 8.13 and deprecated in 15.5. We recommend you instead use the Metadata API.
* _GET /projects/{id}/alert_management_alerts/{alert_iid}/metric_images_ 
  *resource*: get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images  
  *description*: Metric Images for alert
* _GET /application/plan_limits_ 
  *resource*: get_api_v4_application_plan_limits  
  *description*: List the current limits of a plan on the GitLab instance.
