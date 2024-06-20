from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="gitlab_source", max_table_nesting=2)
def gitlab_source(
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
                "name": "Private-Token",
                "location": "header",
            },
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # Get the current appearance
            {
                "name": "get_api_v4_application_appearance",
                "table_name": "api_entities_appearance",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/application/appearance",
                },
            },
            # List all registered applications
            {
                "name": "get_api_v4_applications",
                "table_name": "api_entities_application",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/applications",
                },
            },
            # Return avatar url for a user
            {
                "name": "get_api_v4_avatar",
                "table_name": "api_entities_avatar",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/avatar",
                    "params": {
                        "email": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "size": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This feature was introduced in GitLab 10.6.
            {
                "name": "get_api_v4_groups_id_badges_badge_id",
                "table_name": "api_entities_badge",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{id}/badges/{badge_id}",
                    "params": {
                        "badge_id": {
                            "type": "resolve",
                            "resource": "get_api_v4_groups_id_badges",
                            "field": "id",
                        },
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This feature was introduced in GitLab 10.6.
            {
                "name": "get_api_v4_groups_id_badges",
                "table_name": "api_entities_badge",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{id}/badges",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This feature was introduced in GitLab 10.6.
            {
                "name": "get_api_v4_projects_id_badges_badge_id",
                "table_name": "api_entities_badge",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/badges/{badge_id}",
                    "params": {
                        "badge_id": {
                            "type": "resolve",
                            "resource": "get_api_v4_projects_id_badges",
                            "field": "id",
                        },
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This feature was introduced in GitLab 10.6.
            {
                "name": "get_api_v4_projects_id_badges",
                "table_name": "api_entities_badge",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/badges",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This feature was introduced in GitLab 10.6.
            {
                "name": "get_api_v4_groups_id_badges_render",
                "table_name": "api_entities_basic_badge_details",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{id}/badges/render",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_api_v4_groups_id_badges",
                            "field": "id",
                        },
                        "link_url": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "image_url": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # This feature was introduced in GitLab 10.6.
            {
                "name": "get_api_v4_projects_id_badges_render",
                "table_name": "api_entities_basic_badge_details",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/badges/render",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_api_v4_projects_id_badges",
                            "field": "id",
                        },
                        "link_url": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "image_url": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Retrieve a batched background migration
            {
                "name": "get_api_v4_admin_batched_background_migrations_id",
                "table_name": "api_entities_batched_background_migration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/batched_background_migrations/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_api_v4_admin_batched_background_migrations",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "database": "main",
                    },
                },
            },
            # Get the list of batched background migrations
            {
                "name": "get_api_v4_admin_batched_background_migrations",
                "table_name": "api_entities_batched_background_migration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/batched_background_migrations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "database": "main",
                    },
                },
            },
            # Get a single repository branch
            {
                "name": "get_api_v4_projects_id_repository_branches_branch",
                "table_name": "api_entities_branch",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/repository/branches/{branch}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get a project repository branches
            {
                "name": "get_api_v4_projects_id_repository_branches",
                "table_name": "api_entities_branch",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/repository/branches",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "search": "OPTIONAL_CONFIG",
                        # "regex": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This feature was introduced in GitLab 8.12.
            {
                "name": "get_api_v4_broadcast_messages_id",
                "table_name": "api_entities_broadcast_message",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/broadcast_messages/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This feature was introduced in GitLab 8.12.
            {
                "name": "get_api_v4_broadcast_messages",
                "table_name": "api_entities_broadcast_message",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/broadcast_messages",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # This feature was introduced in GitLab 14.1.
            {
                "name": "get_api_v4_bulk_imports_import_id",
                "table_name": "api_entities_bulk_import",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/bulk_imports/{import_id}",
                    "params": {
                        "import_id": {
                            "type": "resolve",
                            "resource": "get_api_v4_bulk_imports",
                            "field": "id",
                        },
                    },
                },
            },
            # This feature was introduced in GitLab 14.1.
            {
                "name": "get_api_v4_bulk_imports",
                "table_name": "api_entities_bulk_import",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/bulk_imports",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "sort": "desc",
                        # "status": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This feature was introduced in GitLab 14.1.
            {
                "name": "get_api_v4_bulk_imports_import_id_entities_entity_id",
                "table_name": "api_entities_bulk_imports",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/bulk_imports/{import_id}/entities/{entity_id}",
                    "params": {
                        "entity_id": {
                            "type": "resolve",
                            "resource": "get_api_v4_bulk_imports_import_id_entities",
                            "field": "id",
                        },
                        "import_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This feature was introduced in GitLab 14.1.
            {
                "name": "get_api_v4_bulk_imports_import_id_entities",
                "table_name": "api_entities_bulk_imports",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/bulk_imports/{import_id}/entities",
                    "params": {
                        "import_id": {
                            "type": "resolve",
                            "resource": "get_api_v4_bulk_imports",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                        # "per_page": "20",
                    },
                },
            },
            # This feature was introduced in GitLab 14.1.
            {
                "name": "get_api_v4_bulk_imports_entities",
                "table_name": "api_entities_bulk_imports",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/bulk_imports/entities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "sort": "desc",
                        # "status": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the details of a specific instance-level variable
            {
                "name": "get_api_v4_admin_ci_variables_key",
                "table_name": "api_entities_ci_variable",
                "primary_key": "key",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/ci/variables/{key}",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all instance-level variables
            {
                "name": "get_api_v4_admin_ci_variables",
                "table_name": "api_entities_ci_variable",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/ci/variables",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # This feature was introduced in GitLab 13.2. Returns a single instance cluster.
            {
                "name": "get_api_v4_admin_clusters_cluster_id",
                "table_name": "api_entities_cluster",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/clusters/{cluster_id}",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "get_api_v4_admin_clusters",
                            "field": "id",
                        },
                    },
                },
            },
            # This feature was introduced in GitLab 13.2. Returns a list of instance clusters.
            {
                "name": "get_api_v4_admin_clusters",
                "table_name": "api_entities_cluster",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/clusters",
                },
            },
            # This feature was introduced in GitLab 8.11.
            {
                "name": "get_api_v4_groups_id_access_requests",
                "table_name": "api_entities_custom_attribute",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/groups/{id}/access_requests",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # This feature was introduced in GitLab 8.11.
            {
                "name": "get_api_v4_projects_id_access_requests",
                "table_name": "api_entities_custom_attribute",
                "endpoint": {
                    "data_selector": "custom_attributes",
                    "path": "/projects/{id}/access_requests",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # Retrieve dictionary details
            {
                "name": "get_api_v4_admin_databases_database_name_dictionary_tables_table_name",
                "table_name": "api_entities_dictionary_table",
                "primary_key": "table_name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/databases/{database_name}/dictionary/tables/{table_name}",
                    "params": {
                        "database_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "table_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "list_project_jobs",
                "table_name": "api_entities_job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/jobs",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "scope": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_single_job",
                "table_name": "api_entities_job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/jobs/{job_id}",
                    "params": {
                        "job_id": {
                            "type": "resolve",
                            "resource": "list_project_jobs",
                            "field": "id",
                        },
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This feature was introduced in GitLab 15.2.
            {
                "name": "get_api_v4_metadata",
                "table_name": "api_entities_metadata",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/metadata",
                },
            },
            # This feature was introduced in GitLab 8.13 and deprecated in 15.5. We recommend you instead use the Metadata API.
            {
                "name": "get_api_v4_version",
                "table_name": "api_entities_metadata",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/version",
                },
            },
            # Metric Images for alert
            {
                "name": "get_api_v4_projects_id_alert_management_alerts_alert_iid_metric_images",
                "table_name": "api_entities_metric_image",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{id}/alert_management_alerts/{alert_iid}/metric_images",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "alert_iid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List the current limits of a plan on the GitLab instance.
            {
                "name": "get_api_v4_application_plan_limits",
                "table_name": "api_entities_plan_limit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/application/plan_limits",
                    "params": {
                        # the parameters below can optionally be configured
                        # "plan_name": "default",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
