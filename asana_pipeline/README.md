# asana pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/asana.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /users/{user_gid}/favorites_ 
  *resource*: get_favorites_for_user  
  *description*: Returns all of a user's favorites in the given workspace, of the given type. Results are given in order (The same order as Asana's sidebar).
* _GET /workspaces/{workspace_gid}/typeahead_ 
  *resource*: typeahead_for_workspace  
  *description*: Retrieves objects in the workspace based via an auto-completion/typeahead search algorithm. This feature is meant to provide results quickly, so do not rely on this API to provide extremely accurate search results. The result set is limited to a single page of results with a maximum size, so you won’t be able to fetch large numbers of results.  The typeahead search API provides search for objects from a single workspace. This endpoint should be used to query for objects when creating an auto-completion/typeahead search feature. This API is meant to provide results quickly and should not be relied upon for accurate or exhaustive search results. The results sets are limited in size and cannot be paginated.  Queries return a compact representation of each object which is typically the gid and name fields. Interested in a specific set of fields or all of the fields?! Of course you are. Use field selectors to manipulate what data is included in a response.  Resources with type `user` are returned in order of most contacted to least contacted. This is determined by task assignments, adding the user to projects, and adding the user as a follower to tasks, messages, etc.  Resources with type `project` are returned in order of recency. This is determined when the user visits the project, is added to the project, and completes tasks in the project.  Resources with type `task` are returned with priority placed on tasks the user is following, but no guarantee on the order of those tasks.  Resources with type `project_template` are returned with priority placed on favorited project templates.  Leaving the `query` string empty or omitted will give you results, still following the resource ordering above. This could be used to list users or projects that are relevant for the requesting user's api token.
* _GET /attachments_ 
  *resource*: get_attachments_for_object  
  *description*: Returns the compact records for all attachments on the object.  There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the "Key resources" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.
* _GET /attachments/{attachment_gid}_ 
  *resource*: get_attachment  
  *description*: Get the full record for a single attachment.
* _GET /workspaces/{workspace_gid}/audit_log_events_ 
  *resource*: get_audit_log_events  
  *description*: Retrieve the audit log events that have been captured in your domain.  This endpoint will return a list of [AuditLogEvent](/docs/audit-log-event) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.  There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/docs/audit-log-event) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.  The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.  When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/docs/audit-log-event) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.
* _GET /custom_fields/{custom_field_gid}_ 
  *resource*: get_custom_field  
  *description*: Get the complete definition of a custom field’s metadata.  Since custom fields can be defined for one of a number of types, and these types have different data and behaviors, there are fields that are relevant to a particular type. For instance, as noted above, enum_options is only relevant for the enum type and defines the set of choices that the enum could represent. The examples below show some of these type-specific custom field definitions.
* _GET /workspaces/{workspace_gid}/custom_fields_ 
  *resource*: get_custom_fields_for_workspace  
  *description*: Returns a list of the compact representation of all of the custom fields in a workspace.
* _GET /portfolios/{portfolio_gid}/custom_field_settings_ 
  *resource*: get_custom_field_settings_for_portfolio  
  *description*: Returns a list of all of the custom fields settings on a portfolio, in compact form.
* _GET /projects/{project_gid}/custom_field_settings_ 
  *resource*: get_custom_field_settings_for_project  
  *description*: Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [getting started guide on input/output options](https://developers.asana.com/docs/#input-output-options) for more information.
* _GET /events_ 
  *resource*: get_events  
  *description*: Returns the full record for all events that have occurred since the sync token was created.  A `GET` request to the endpoint `/[path_to_resource]/events` can be made in lieu of including the resource ID in the data for the request.  Asana limits a single sync token to 100 events. If more than 100 events exist for a given resource, `has_more: true` will be returned in the response, indicating that there are more events to pull.   *Note: The resource returned will be the resource that triggered the event. This may be different from the one that the events were requested for. For example, a subscription to a project will contain events for tasks contained within the project.*
* _GET /goals_ 
  *resource*: get_goals  
  *description*: Returns compact goal records.
* _GET /goals/{goal_gid}/parentGoals_ 
  *resource*: get_parent_goals_for_goal  
  *description*: Returns a compact representation of all of the parent goals of a goal.
* _GET /goal_relationships_ 
  *resource*: get_goal_relationships  
  *description*: Returns compact goal relationship records.
* _GET /goal_relationships/{goal_relationship_gid}_ 
  *resource*: get_goal_relationship  
  *description*: Returns the complete updated goal relationship record for a single goal relationship.
* _GET /goals/{goal_gid}_ 
  *resource*: get_goal  
  *description*: Returns the complete goal record for a single goal.
* _GET /jobs/{job_gid}_ 
  *resource*: get_job  
  *description*: Returns the full record for a job.
* _GET /stories/{story_gid}_ 
  *resource*: get_story  
  *description*: Returns the full record for a single story.
* _GET /organization_exports/{organization_export_gid}_ 
  *resource*: get_organization_export  
  *description*: Returns details of a previously-requested Organization export.
* _GET /portfolios_ 
  *resource*: get_portfolios  
  *description*: Returns a list of the portfolios in compact representation that are owned by the current API user.
* _GET /portfolio_memberships/{portfolio_membership_gid}_ 
  *resource*: get_portfolio_membership  
  *description*: Returns the complete portfolio record for a single portfolio membership.
* _GET /portfolio_memberships_ 
  *resource*: get_portfolio_memberships  
  *description*: Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.
* _GET /portfolios/{portfolio_gid}/portfolio_memberships_ 
  *resource*: get_portfolio_memberships_for_portfolio  
  *description*: Returns the compact portfolio membership records for the portfolio.
* _GET /portfolios/{portfolio_gid}_ 
  *resource*: get_portfolio  
  *description*: Returns the complete portfolio record for a single portfolio.
* _GET /project_briefs/{project_brief_gid}_ 
  *resource*: get_project_brief  
  *description*: Get the full record for a project brief.
* _GET /portfolios/{portfolio_gid}/items_ 
  *resource*: get_items_for_portfolio  
  *description*: Get a list of the items in compact form in a portfolio.
* _GET /projects_ 
  *resource*: get_projects  
  *description*: Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned. *Note: This endpoint may timeout for large domains. Try filtering by team!*
* _GET /tasks/{task_gid}/projects_ 
  *resource*: get_projects_for_task  
  *description*: Returns a compact representation of all of the projects the task is in.
* _GET /teams/{team_gid}/projects_ 
  *resource*: get_projects_for_team  
  *description*: Returns the compact project records for all projects in the team.
* _GET /workspaces/{workspace_gid}/projects_ 
  *resource*: get_projects_for_workspace  
  *description*: Returns the compact project records for all projects in the workspace. *Note: This endpoint may timeout for large domains. Prefer the `/teams/{team_gid}/projects` endpoint.*
* _GET /projects/{project_gid}/project_memberships_ 
  *resource*: get_project_memberships_for_project  
  *description*: Returns the compact project membership records for the project.
* _GET /project_memberships/{project_membership_gid}_ 
  *resource*: get_project_membership  
  *description*: Returns the complete project record for a single project membership.
* _GET /projects/{project_gid}_ 
  *resource*: get_project  
  *description*: Returns the complete project record for a single project.
* _GET /projects/{project_gid}/project_statuses_ 
  *resource*: get_project_statuses_for_project  
  *description*: *Deprecated: new integrations should prefer the `/status_updates` route.*  Returns the compact project status update records for all updates on the project.
* _GET /project_statuses/{project_status_gid}_ 
  *resource*: get_project_status  
  *description*: *Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*  Returns the complete record for a single status update.
* _GET /project_templates_ 
  *resource*: get_project_templates  
  *description*: Returns the compact project template records for all project templates in the given team or workspace.
* _GET /teams/{team_gid}/project_templates_ 
  *resource*: get_project_templates_for_team  
  *description*: Returns the compact project template records for all project templates in the team.
* _GET /project_templates/{project_template_gid}_ 
  *resource*: get_project_template  
  *description*: Returns the complete project template record for a single project template.
* _GET /projects/{project_gid}/sections_ 
  *resource*: get_sections_for_project  
  *description*: Returns the compact records for all sections in the specified project.
* _GET /sections/{section_gid}_ 
  *resource*: get_section  
  *description*: Returns the complete record for a single section.
* _GET /status_updates_ 
  *resource*: get_statuses_for_object  
  *description*: Returns the compact status update records for all updates on the object.
* _GET /status_updates/{status_gid}_ 
  *resource*: get_status  
  *description*: Returns the complete record for a single status update.
* _GET /tasks/{task_gid}/stories_ 
  *resource*: get_stories_for_task  
  *description*: Returns the compact records for all stories on the task.
* _GET /tags_ 
  *resource*: get_tags  
  *description*: Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.
* _GET /tasks/{task_gid}/tags_ 
  *resource*: get_tags_for_task  
  *description*: Get a compact representation of all of the tags the task has.
* _GET /workspaces/{workspace_gid}/tags_ 
  *resource*: get_tags_for_workspace  
  *description*: Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.
* _GET /projects/{project_gid}/tasks_ 
  *resource*: get_tasks_for_project  
  *description*: Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.
* _GET /sections/{section_gid}/tasks_ 
  *resource*: get_tasks_for_section  
  *description*: *Board view only*: Returns the compact section records for all tasks within the given section.
* _GET /tags/{tag_gid}/tasks_ 
  *resource*: get_tasks_for_tag  
  *description*: Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.
* _GET /tasks_ 
  *resource*: get_tasks  
  *description*: Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.  For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/docs/search-tasks-in-a-workspace).
* _GET /tasks/{task_gid}/dependencies_ 
  *resource*: get_dependencies_for_task  
  *description*: Returns the compact representations of all of the dependencies of a task.
* _GET /tasks/{task_gid}/dependents_ 
  *resource*: get_dependents_for_task  
  *description*: Returns the compact representations of all of the dependents of a task.
* _GET /tasks/{task_gid}/subtasks_ 
  *resource*: get_subtasks_for_task  
  *description*: Returns a compact representation of all of the subtasks of a task.
* _GET /user_task_lists/{user_task_list_gid}/tasks_ 
  *resource*: get_tasks_for_user_task_list  
  *description*: Returns the compact list of tasks in a user’s My Tasks list. *Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.* *Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*
* _GET /workspaces/{workspace_gid}/tasks/search_ 
  *resource*: search_tasks_for_workspace  
  *description*: To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need. #### Premium access Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:  - The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace  Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error. #### Pagination Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter. #### Eventual consistency Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product. #### Rate limits You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits). #### Custom field parameters | Parameter name | Custom field type | Accepted type | |---|---|---| | custom_fields.{gid}.is_set | All | Boolean | | custom_fields.{gid}.value | Text | String | | custom_fields.{gid}.value | Number | Number | | custom_fields.{gid}.value | Enum | Enum option ID | | custom_fields.{gid}.starts_with | Text only | String | | custom_fields.{gid}.ends_with | Text only | String | | custom_fields.{gid}.contains | Text only | String | | custom_fields.{gid}.less_than | Number only | Number | | custom_fields.{gid}.greater_than | Number only | Number |   For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.  **Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field  *Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*
* _GET /projects/{project_gid}/task_counts_ 
  *resource*: get_task_counts_for_project  
  *description*: Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/input-output-options) using `opt_fields` to get any information from this endpoint.  This endpoint has an additional [rate limit](/docs/standard-rate-limits) and each field counts especially high against our [cost limits](/docs/cost-limits).  Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.
* _GET /tasks/{task_gid}_ 
  *resource*: get_task  
  *description*: Returns the complete task record for a single task.
* _GET /users/{user_gid}/teams_ 
  *resource*: get_teams_for_user  
  *description*: Returns the compact records for all teams to which the given user is assigned.
* _GET /workspaces/{workspace_gid}/teams_ 
  *resource*: get_teams_for_workspace  
  *description*: Returns the compact records for all teams in the workspace visible to the authorized user.
* _GET /team_memberships/{team_membership_gid}_ 
  *resource*: get_team_membership  
  *description*: Returns the complete team membership record for a single team membership.
* _GET /team_memberships_ 
  *resource*: get_team_memberships  
  *description*: Returns compact team membership records.
* _GET /teams/{team_gid}/team_memberships_ 
  *resource*: get_team_memberships_for_team  
  *description*: Returns the compact team memberships for the team.
* _GET /users/{user_gid}/team_memberships_ 
  *resource*: get_team_memberships_for_user  
  *description*: Returns the compact team membership records for the user.
* _GET /teams/{team_gid}_ 
  *resource*: get_team  
  *description*: Returns the full record for a single team.
* _GET /time_periods_ 
  *resource*: get_time_periods  
  *description*: Returns compact time period records.
* _GET /time_periods/{time_period_gid}_ 
  *resource*: get_time_period  
  *description*: Returns the full record for a single time period.
* _GET /tags/{tag_gid}_ 
  *resource*: get_tag  
  *description*: Returns the complete tag record for a single tag.
* _GET /teams/{team_gid}/users_ 
  *resource*: get_users_for_team  
  *description*: Returns the compact records for all users that are members of the team. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.
* _GET /users_ 
  *resource*: get_users  
  *description*: Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter. Results are sorted by user ID.
* _GET /workspaces/{workspace_gid}/users_ 
  *resource*: get_users_for_workspace  
  *description*: Returns the compact records for all users in the specified workspace or organization. Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.
* _GET /users/{user_gid}_ 
  *resource*: get_user  
  *description*: Returns the full user record for the single user with the provided ID.
* _GET /user_task_lists/{user_task_list_gid}_ 
  *resource*: get_user_task_list  
  *description*: Returns the full record for a user task list.
* _GET /users/{user_gid}/user_task_list_ 
  *resource*: get_user_task_list_for_user  
  *description*: Returns the full record for a user's task list.
* _GET /webhooks_ 
  *resource*: get_webhooks  
  *description*: Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.
* _GET /webhooks/{webhook_gid}_ 
  *resource*: get_webhook  
  *description*: Returns the full record for the given webhook.
* _GET /workspaces_ 
  *resource*: get_workspaces  
  *description*: Returns the compact records for all workspaces visible to the authorized user.
* _GET /users/{user_gid}/workspace_memberships_ 
  *resource*: get_workspace_memberships_for_user  
  *description*: Returns the compact workspace membership records for the user.
* _GET /workspaces/{workspace_gid}/workspace_memberships_ 
  *resource*: get_workspace_memberships_for_workspace  
  *description*: Returns the compact workspace membership records for the workspace.
* _GET /workspace_memberships/{workspace_membership_gid}_ 
  *resource*: get_workspace_membership  
  *description*: Returns the complete workspace record for a single workspace membership.
* _GET /workspaces/{workspace_gid}_ 
  *resource*: get_workspace  
  *description*: Returns the full workspace record for a single workspace.
