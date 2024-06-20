from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="asana_source", max_table_nesting=2)
def asana_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
            "paginator": {
                "type": "offset",
                "limit": 20,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            # Returns all of a user's favorites in the given workspace, of the given type. Results are given in order (The same order as Asana's sidebar).
            {
                "name": "get_favorites_for_user",
                "table_name": "asana_named_resource",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/users/{user_gid}/favorites",
                    "params": {
                        "user_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "resource_type": "project",  # TODO: fill in required query parameter
                        "workspace": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves objects in the workspace based via an auto-completion/typeahead search algorithm. This feature is meant to provide results quickly, so do not rely on this API to provide extremely accurate search results. The result set is limited to a single page of results with a maximum size, so you won’t be able to fetch large numbers of results.  The typeahead search API provides search for objects from a single workspace. This endpoint should be used to query for objects when creating an auto-completion/typeahead search feature. This API is meant to provide results quickly and should not be relied upon for accurate or exhaustive search results. The results sets are limited in size and cannot be paginated.  Queries return a compact representation of each object which is typically the gid and name fields. Interested in a specific set of fields or all of the fields?! Of course you are. Use field selectors to manipulate what data is included in a response.  Resources with type `user` are returned in order of most contacted to least contacted. This is determined by task assignments, adding the user to projects, and adding the user as a follower to tasks, messages, etc.  Resources with type `project` are returned in order of recency. This is determined when the user visits the project, is added to the project, and completes tasks in the project.  Resources with type `task` are returned with priority placed on tasks the user is following, but no guarantee on the order of those tasks.  Resources with type `project_template` are returned with priority placed on favorited project templates.  Leaving the `query` string empty or omitted will give you results, still following the resource ordering above. This could be used to list users or projects that are relevant for the requesting user's api token.
            {
                "name": "typeahead_for_workspace",
                "table_name": "asana_named_resource",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/typeahead",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "resource_type": "user",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "type": "user",
                        # "query": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all attachments on the object.  There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the "Key resources" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.
            {
                "name": "get_attachments_for_object",
                "table_name": "attachment_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/attachments",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the full record for a single attachment.
            {
                "name": "get_attachment",
                "table_name": "attachment_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/attachments/{attachment_gid}",
                    "params": {
                        "attachment_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/docs/audit-log-event) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/docs/audit-log-event) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/docs/audit-log-event) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.
            {
                "name": "get_audit_log_events",
                "table_name": "audit_log_event",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/audit_log_events",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "start_at": "OPTIONAL_CONFIG",
                        # "end_at": "OPTIONAL_CONFIG",
                        # "event_type": "OPTIONAL_CONFIG",
                        # "actor_type": "OPTIONAL_CONFIG",
                        # "actor_gid": "OPTIONAL_CONFIG",
                        # "resource_gid": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the complete definition of a custom field’s metadata.  Since custom fields can be defined for one of a number of types, and these types have different data and behaviors, there are fields that are relevant to a particular type. For instance, as noted above, enum_options is only relevant for the enum type and defines the set of choices that the enum could represent. The examples below show some of these type-specific custom field definitions.
            {
                "name": "get_custom_field",
                "table_name": "custom_field_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/custom_fields/{custom_field_gid}",
                    "params": {
                        "custom_field_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of the compact representation of all of the custom fields in a workspace.
            {
                "name": "get_custom_fields_for_workspace",
                "table_name": "custom_field_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/custom_fields",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of all of the custom fields settings on a portfolio, in compact form.
            {
                "name": "get_custom_field_settings_for_portfolio",
                "table_name": "custom_field_setting_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/portfolios/{portfolio_gid}/custom_field_settings",
                    "params": {
                        "portfolio_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [getting started guide on input/output options](https://developers.asana.com/docs/#input-output-options) for more information.
            {
                "name": "get_custom_field_settings_for_project",
                "table_name": "custom_field_setting_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}/custom_field_settings",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for all events that have occurred since the sync token was created.  A `GET` request to the endpoint `/[path_to_resource]/events` can be made in lieu of including the resource ID in the data for the request.  Asana limits a single sync token to 100 events. If more than 100 events exist for a given resource, `has_more: true` will be returned in the response, indicating that there are more events to pull.   *Note: The resource returned will be the resource that triggered the event. This may be different from the one that the events were requested for. For example, a subscription to a project will contain events for tasks contained within the project.*
            {
                "name": "get_events",
                "table_name": "event_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/events",
                    "params": {
                        "resource": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sync": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns compact goal records.
            {
                "name": "get_goals",
                "table_name": "goal_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/goals",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "portfolio": "OPTIONAL_CONFIG",
                        # "project": "OPTIONAL_CONFIG",
                        # "is_workspace_level": "OPTIONAL_CONFIG",
                        # "team": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                        # "time_periods": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a compact representation of all of the parent goals of a goal.
            {
                "name": "get_parent_goals_for_goal",
                "table_name": "goal_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/goals/{goal_gid}/parentGoals",
                    "params": {
                        "goal_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns compact goal relationship records.
            {
                "name": "get_goal_relationships",
                "table_name": "goal_relationship_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/goal_relationships",
                    "params": {
                        "supported_goal": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "resource_subtype": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete updated goal relationship record for a single goal relationship.
            {
                "name": "get_goal_relationship",
                "table_name": "goal_relationship_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/goal_relationships/{goal_relationship_gid}",
                    "params": {
                        "goal_relationship_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete goal record for a single goal.
            {
                "name": "get_goal",
                "table_name": "goal_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/goals/{goal_gid}",
                    "params": {
                        "goal_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for a job.
            {
                "name": "get_job",
                "table_name": "job",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/jobs/{job_gid}",
                    "params": {
                        "job_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for a single story.
            {
                "name": "get_story",
                "table_name": "like",
                "endpoint": {
                    "data_selector": "data.hearts",
                    "path": "/stories/{story_gid}",
                    "params": {
                        "story_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns details of a previously-requested Organization export.
            {
                "name": "get_organization_export",
                "table_name": "organization_export",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organization_exports/{organization_export_gid}",
                    "params": {
                        "organization_export_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of the portfolios in compact representation that are owned by the current API user.
            {
                "name": "get_portfolios",
                "table_name": "portfolio_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/portfolios",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "owner": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete portfolio record for a single portfolio membership.
            {
                "name": "get_portfolio_membership",
                "table_name": "portfolio_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/portfolio_memberships/{portfolio_membership_gid}",
                    "params": {
                        "portfolio_membership_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.
            {
                "name": "get_portfolio_memberships",
                "table_name": "portfolio_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/portfolio_memberships",
                    "params": {
                        # the parameters below can optionally be configured
                        # "portfolio": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                        # "user": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact portfolio membership records for the portfolio.
            {
                "name": "get_portfolio_memberships_for_portfolio",
                "table_name": "portfolio_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/portfolios/{portfolio_gid}/portfolio_memberships",
                    "params": {
                        "portfolio_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "user": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete portfolio record for a single portfolio.
            {
                "name": "get_portfolio",
                "table_name": "portfolio_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/portfolios/{portfolio_gid}",
                    "params": {
                        "portfolio_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the full record for a project brief.
            {
                "name": "get_project_brief",
                "table_name": "project_brief_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/project_briefs/{project_brief_gid}",
                    "params": {
                        "project_brief_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a list of the items in compact form in a portfolio.
            {
                "name": "get_items_for_portfolio",
                "table_name": "project_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/portfolios/{portfolio_gid}/items",
                    "params": {
                        "portfolio_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned. *Note: This endpoint may timeout for large domains. Try filtering by team!*
            {
                "name": "get_projects",
                "table_name": "project_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                        # "team": "OPTIONAL_CONFIG",
                        # "archived": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a compact representation of all of the projects the task is in.
            {
                "name": "get_projects_for_task",
                "table_name": "project_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks/{task_gid}/projects",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact project records for all projects in the team.
            {
                "name": "get_projects_for_team",
                "table_name": "project_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/teams/{team_gid}/projects",
                    "params": {
                        "team_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "archived": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact project records for all projects in the workspace. *Note: This endpoint may timeout for large domains. Prefer the `/teams/{team_gid}/projects` endpoint.*
            {
                "name": "get_projects_for_workspace",
                "table_name": "project_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/projects",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "archived": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact project membership records for the project.
            {
                "name": "get_project_memberships_for_project",
                "table_name": "project_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}/project_memberships",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "user": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete project record for a single project membership.
            {
                "name": "get_project_membership",
                "table_name": "project_membership_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/project_memberships/{project_membership_gid}",
                    "params": {
                        "project_membership_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete project record for a single project.
            {
                "name": "get_project",
                "table_name": "project_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # *Deprecated: new integrations should prefer the `/status_updates` route.*  Returns the compact project status update records for all updates on the project.
            {
                "name": "get_project_statuses_for_project",
                "table_name": "project_status_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}/project_statuses",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Returns the complete record for a single status update.
            {
                "name": "get_project_status",
                "table_name": "project_status_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/project_statuses/{project_status_gid}",
                    "params": {
                        "project_status_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact project template records for all project templates in the given team or workspace.
            {
                "name": "get_project_templates",
                "table_name": "project_template_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/project_templates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                        # "team": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact project template records for all project templates in the team.
            {
                "name": "get_project_templates_for_team",
                "table_name": "project_template_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/teams/{team_gid}/project_templates",
                    "params": {
                        "team_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete project template record for a single project template.
            {
                "name": "get_project_template",
                "table_name": "project_template_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/project_templates/{project_template_gid}",
                    "params": {
                        "project_template_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all sections in the specified project.
            {
                "name": "get_sections_for_project",
                "table_name": "section_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}/sections",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete record for a single section.
            {
                "name": "get_section",
                "table_name": "section_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/sections/{section_gid}",
                    "params": {
                        "section_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact status update records for all updates on the object.
            {
                "name": "get_statuses_for_object",
                "table_name": "status_update_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/status_updates",
                    "params": {
                        "parent": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "created_since": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete record for a single status update.
            {
                "name": "get_status",
                "table_name": "status_update_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/status_updates/{status_gid}",
                    "params": {
                        "status_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all stories on the task.
            {
                "name": "get_stories_for_task",
                "table_name": "story",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/tasks/{task_gid}/stories",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.
            {
                "name": "get_tags",
                "table_name": "tag_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tags",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a compact representation of all of the tags the task has.
            {
                "name": "get_tags_for_task",
                "table_name": "tag_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks/{task_gid}/tags",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.
            {
                "name": "get_tags_for_workspace",
                "table_name": "tag_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/tags",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.
            {
                "name": "get_tasks_for_project",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}/tasks",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "completed_since": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # *Board view only*: Returns the compact section records for all tasks within the given section.
            {
                "name": "get_tasks_for_section",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/sections/{section_gid}/tasks",
                    "params": {
                        "section_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.
            {
                "name": "get_tasks_for_tag",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tags/{tag_gid}/tasks",
                    "params": {
                        "tag_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/docs/search-tasks-in-a-workspace).
            {
                "name": "get_tasks",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "assignee": "OPTIONAL_CONFIG",
                        # "project": "OPTIONAL_CONFIG",
                        # "section": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                        # "completed_since": "OPTIONAL_CONFIG",
                        # "modified_since": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact representations of all of the dependencies of a task.
            {
                "name": "get_dependencies_for_task",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks/{task_gid}/dependencies",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact representations of all of the dependents of a task.
            {
                "name": "get_dependents_for_task",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks/{task_gid}/dependents",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a compact representation of all of the subtasks of a task.
            {
                "name": "get_subtasks_for_task",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks/{task_gid}/subtasks",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact list of tasks in a user’s My Tasks list. *Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.* *Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*
            {
                "name": "get_tasks_for_user_task_list",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/user_task_lists/{user_task_list_gid}/tasks",
                    "params": {
                        "user_task_list_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "completed_since": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need. #### Premium access Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:  - The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace  Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter. #### Eventual consistency Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product. #### Rate limits You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits). #### Custom field parameters | Parameter name | Custom field type | Accepted type | |---|---|---| | custom_fields.{gid}.is_set | All | Boolean | | custom_fields.{gid}.value | Text | String | | custom_fields.{gid}.value | Number | Number | | custom_fields.{gid}.value | Enum | Enum option ID | | custom_fields.{gid}.starts_with | Text only | String | | custom_fields.{gid}.ends_with | Text only | String | | custom_fields.{gid}.contains | Text only | String | | custom_fields.{gid}.less_than | Number only | Number | | custom_fields.{gid}.greater_than | Number only | Number |   For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.  **Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field  *Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*
            {
                "name": "search_tasks_for_workspace",
                "table_name": "task_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/tasks/search",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "text": "OPTIONAL_CONFIG",
                        # "resource_subtype": "milestone",
                        # "assignee.any": "OPTIONAL_CONFIG",
                        # "assignee.not": "OPTIONAL_CONFIG",
                        # "portfolios.any": "OPTIONAL_CONFIG",
                        # "projects.any": "OPTIONAL_CONFIG",
                        # "projects.not": "OPTIONAL_CONFIG",
                        # "projects.all": "OPTIONAL_CONFIG",
                        # "sections.any": "OPTIONAL_CONFIG",
                        # "sections.not": "OPTIONAL_CONFIG",
                        # "sections.all": "OPTIONAL_CONFIG",
                        # "tags.any": "OPTIONAL_CONFIG",
                        # "tags.not": "OPTIONAL_CONFIG",
                        # "tags.all": "OPTIONAL_CONFIG",
                        # "teams.any": "OPTIONAL_CONFIG",
                        # "followers.not": "OPTIONAL_CONFIG",
                        # "created_by.any": "OPTIONAL_CONFIG",
                        # "created_by.not": "OPTIONAL_CONFIG",
                        # "assigned_by.any": "OPTIONAL_CONFIG",
                        # "assigned_by.not": "OPTIONAL_CONFIG",
                        # "liked_by.not": "OPTIONAL_CONFIG",
                        # "commented_on_by.not": "OPTIONAL_CONFIG",
                        # "due_on.before": "OPTIONAL_CONFIG",
                        # "due_on.after": "OPTIONAL_CONFIG",
                        # "due_on": "OPTIONAL_CONFIG",
                        # "due_at.before": "OPTIONAL_CONFIG",
                        # "due_at.after": "OPTIONAL_CONFIG",
                        # "start_on.before": "OPTIONAL_CONFIG",
                        # "start_on.after": "OPTIONAL_CONFIG",
                        # "start_on": "OPTIONAL_CONFIG",
                        # "created_on.before": "OPTIONAL_CONFIG",
                        # "created_on.after": "OPTIONAL_CONFIG",
                        # "created_on": "OPTIONAL_CONFIG",
                        # "created_at.before": "OPTIONAL_CONFIG",
                        # "created_at.after": "OPTIONAL_CONFIG",
                        # "completed_on.before": "OPTIONAL_CONFIG",
                        # "completed_on.after": "OPTIONAL_CONFIG",
                        # "completed_on": "OPTIONAL_CONFIG",
                        # "completed_at.before": "OPTIONAL_CONFIG",
                        # "completed_at.after": "OPTIONAL_CONFIG",
                        # "modified_on.before": "OPTIONAL_CONFIG",
                        # "modified_on.after": "OPTIONAL_CONFIG",
                        # "modified_on": "OPTIONAL_CONFIG",
                        # "modified_at.before": "OPTIONAL_CONFIG",
                        # "modified_at.after": "OPTIONAL_CONFIG",
                        # "is_blocking": "OPTIONAL_CONFIG",
                        # "is_blocked": "OPTIONAL_CONFIG",
                        # "has_attachment": "OPTIONAL_CONFIG",
                        # "completed": "OPTIONAL_CONFIG",
                        # "is_subtask": "OPTIONAL_CONFIG",
                        # "sort_by": "modified_at",
                        # "sort_ascending": "false",
                    },
                },
            },
            # Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/input-output-options) using `opt_fields` to get any information from this endpoint.  This endpoint has an additional [rate limit](/docs/standard-rate-limits) and each field counts especially high against our [cost limits](/docs/cost-limits).  Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.
            {
                "name": "get_task_counts_for_project",
                "table_name": "task_count_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/projects/{project_gid}/task_counts",
                    "params": {
                        "project_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete task record for a single task.
            {
                "name": "get_task",
                "table_name": "task_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/tasks/{task_gid}",
                    "params": {
                        "task_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all teams to which the given user is assigned.
            {
                "name": "get_teams_for_user",
                "table_name": "team_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/users/{user_gid}/teams",
                    "params": {
                        "user_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "organization": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all teams in the workspace visible to the authorized user.
            {
                "name": "get_teams_for_workspace",
                "table_name": "team_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/teams",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete team membership record for a single team membership.
            {
                "name": "get_team_membership",
                "table_name": "team_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/team_memberships/{team_membership_gid}",
                    "params": {
                        "team_membership_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns compact team membership records.
            {
                "name": "get_team_memberships",
                "table_name": "team_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/team_memberships",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "team": "OPTIONAL_CONFIG",
                        # "user": "OPTIONAL_CONFIG",
                        # "workspace": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact team memberships for the team.
            {
                "name": "get_team_memberships_for_team",
                "table_name": "team_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/teams/{team_gid}/team_memberships",
                    "params": {
                        "team_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact team membership records for the user.
            {
                "name": "get_team_memberships_for_user",
                "table_name": "team_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/users/{user_gid}/team_memberships",
                    "params": {
                        "user_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "workspace": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for a single team.
            {
                "name": "get_team",
                "table_name": "team_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/teams/{team_gid}",
                    "params": {
                        "team_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns compact time period records.
            {
                "name": "get_time_periods",
                "table_name": "time_period_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time_periods",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "start_on": "OPTIONAL_CONFIG",
                        # "end_on": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for a single time period.
            {
                "name": "get_time_period",
                "table_name": "time_period_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time_periods/{time_period_gid}",
                    "params": {
                        "time_period_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete tag record for a single tag.
            {
                "name": "get_tag",
                "table_name": "user_compact",
                "endpoint": {
                    "data_selector": "data.followers",
                    "path": "/tags/{tag_gid}",
                    "params": {
                        "tag_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all users that are members of the team. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.
            {
                "name": "get_users_for_team",
                "table_name": "user_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/teams/{team_gid}/users",
                    "params": {
                        "team_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter. Results are sorted by user ID.
            {
                "name": "get_users",
                "table_name": "user_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "workspace": "OPTIONAL_CONFIG",
                        # "team": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all users in the specified workspace or organization. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.
            {
                "name": "get_users_for_workspace",
                "table_name": "user_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/users",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "offset": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full user record for the single user with the provided ID.
            {
                "name": "get_user",
                "table_name": "user_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/users/{user_gid}",
                    "params": {
                        "user_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for a user task list.
            {
                "name": "get_user_task_list",
                "table_name": "user_task_list",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user_task_lists/{user_task_list_gid}",
                    "params": {
                        "user_task_list_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for a user's task list.
            {
                "name": "get_user_task_list_for_user",
                "table_name": "user_task_list",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_gid}/user_task_list",
                    "params": {
                        "user_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "workspace": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.
            {
                "name": "get_webhooks",
                "table_name": "webhook_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/webhooks",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                        # "resource": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full record for the given webhook.
            {
                "name": "get_webhook",
                "table_name": "webhook_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/webhooks/{webhook_gid}",
                    "params": {
                        "webhook_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact records for all workspaces visible to the authorized user.
            {
                "name": "get_workspaces",
                "table_name": "workspace_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces",
                    "params": {
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact workspace membership records for the user.
            {
                "name": "get_workspace_memberships_for_user",
                "table_name": "workspace_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/users/{user_gid}/workspace_memberships",
                    "params": {
                        "user_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the compact workspace membership records for the workspace.
            {
                "name": "get_workspace_memberships_for_workspace",
                "table_name": "workspace_membership_compact",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}/workspace_memberships",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "user": "OPTIONAL_CONFIG",
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the complete workspace record for a single workspace membership.
            {
                "name": "get_workspace_membership",
                "table_name": "workspace_membership_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspace_memberships/{workspace_membership_gid}",
                    "params": {
                        "workspace_membership_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the full workspace record for a single workspace.
            {
                "name": "get_workspace",
                "table_name": "workspace_response",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/workspaces/{workspace_gid}",
                    "params": {
                        "workspace_gid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "opt_pretty": "OPTIONAL_CONFIG",
                        # "opt_fields": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
