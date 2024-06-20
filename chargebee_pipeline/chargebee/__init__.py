from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="chargebee_source", max_table_nesting=2)
def chargebee_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Returns the current announcement banner configuration.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_banner",
                "table_name": "announcement_banner_configuration",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/announcementBanner",
                    "paginator": "auto",
                },
            },
            # Returns all application properties or an application property.  If you specify a value for the `key` parameter, then an application property is returned as an object (not in an array). Otherwise, an array of all editable application properties is returned. See [Set application property](#api-rest-api-3-application-properties-id-put) for descriptions of editable properties.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_application_property",
                "table_name": "application_property",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/application-properties",
                    "params": {
                        # the parameters below can optionally be configured
                        # "key": "OPTIONAL_CONFIG",
                        # "permissionLevel": "OPTIONAL_CONFIG",
                        # "keyFilter": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the application properties that are accessible on the *Advanced Settings* page. To navigate to the *Advanced Settings* page in Jira, choose the Jira icon > **Jira settings** > **System**, **General Configuration** and then click **Advanced Settings** (in the upper right).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_advanced_settings",
                "table_name": "application_property",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/application-properties/advanced-settings",
                    "paginator": "auto",
                },
            },
            # Returns all application roles. In Jira, application roles are managed using the [Application access configuration](https://confluence.atlassian.com/x/3YxjL) page.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_application_roles",
                "table_name": "application_role",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/applicationrole",
                    "paginator": "auto",
                },
            },
            # Returns an application role.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_application_role",
                "table_name": "application_role",
                "primary_key": "key",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/applicationrole/{key}",
                    "params": {
                        "key": {
                            "type": "resolve",
                            "resource": "get_all_application_roles",
                            "field": "key",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns details for the current user.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_current_user",
                "table_name": "application_role",
                "endpoint": {
                    "data_selector": "applicationRoles.items",
                    "path": "/rest/api/3/myself",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a user.  Privacy controls are applied to the response based on the user's preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_user",
                "table_name": "application_role",
                "endpoint": {
                    "data_selector": "applicationRoles.items",
                    "path": "/rest/api/3/user",
                    "params": {
                        # the parameters below can optionally be configured
                        # "accountId": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the draft workflow scheme for an active workflow scheme. Draft workflow schemes allow changes to be made to the active workflow schemes: When an active workflow scheme is updated, a draft copy is created. The draft is modified, then the changes in the draft are copied back to the active workflow scheme. See [Configuring workflow schemes](https://confluence.atlassian.com/x/tohKLg) for more information.   Note that:   *  Only active workflow schemes can have draft workflow schemes.  *  An active workflow scheme can only have one draft workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow_scheme_draft",
                "table_name": "application_role",
                "endpoint": {
                    "data_selector": "lastModifiedUser.applicationRoles.items",
                    "path": "/rest/api/3/workflowscheme/{id}/draft",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_workflow_schemes",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported.  Use this operation if you are processing the data without presenting it to the user, as this operation only returns the metadata for the contents of the attachment. Otherwise, to retrieve data to present to the user, use [ Get all metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-human-get) which also returns the metadata for the attachment itself, such as the attachment's ID and name.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** For the issue containing the attachment:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "expand_attachment_for_machines",
                "table_name": "attachment_archive_entry",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/rest/api/3/attachment/{id}/expand/raw",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the attachment itself. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format is supported.  Use this operation to retrieve data that is presented to the user, as this operation returns the metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which only returns the metadata for the attachment's contents.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** For the issue containing the attachment:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "expand_attachment_for_humans",
                "table_name": "attachment_archive_item_readable",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/rest/api/3/attachment/{id}/expand/human",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the metadata for an attachment. Note that the attachment itself is not returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_attachment",
                "table_name": "attachment_metadata",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/attachment/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed.  Note that there are also [project permissions](https://confluence.atlassian.com/x/yodKLg) that restrict whether users can create and delete attachments.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_attachment_meta",
                "table_name": "attachment_settings",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/attachment/meta",
                    "paginator": "auto",
                },
            },
            # Returns a list of audit records. The list can be filtered to include items:   *  where each item in `filter` has at least one match in any of these fields:           *  `summary`      *  `category`      *  `eventSource`      *  `objectItem.name` If the object is a user, account ID is available to filter.      *  `objectItem.parentName`      *  `objectItem.typeName`      *  `changedValues.changedFrom`      *  `changedValues.changedTo`      *  `remoteAddress`          For example, if `filter` contains *man ed*, an audit record containing `summary": "User added to group"` and `"category": "group management"` is returned.  *  created on or after a date and time.  *  created or or before a date and time.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_audit_records",
                "table_name": "audit_record_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "records",
                    "path": "/rest/api/3/auditing/record",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "to": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 1000,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "total",
                    },
                },
            },
            # Returns the JQL search auto complete suggestions for a field.  Suggestions can be obtained by providing:   *  `fieldName` to get a list of all values for the field.  *  `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`.  *  `fieldName` and `predicateName` to get a list of all predicate values for the field.  *  `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing the text in `predicateValue`.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_field_auto_complete_for_query_string",
                "table_name": "auto_complete_suggestion",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/rest/api/3/jql/autocompletedata/suggestions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fieldName": "OPTIONAL_CONFIG",
                        # "fieldValue": "OPTIONAL_CONFIG",
                        # "predicateName": "OPTIONAL_CONFIG",
                        # "predicateValue": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder.  To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_auto_complete",
                "table_name": "autocompletedatum",
                "endpoint": {
                    "data_selector": "jqlReservedWords",
                    "path": "/rest/api/3/jql/autocompletedata",
                    "paginator": "auto",
                },
            },
            # Gets a list of all available gadgets that can be added to all dashboards.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_available_dashboard_gadgets",
                "table_name": "available_dashboard_gadget",
                "endpoint": {
                    "data_selector": "gadgets",
                    "path": "/rest/api/3/dashboard/gadgets",
                    "paginator": "auto",
                },
            },
            # Get the list of workflow capabilities for a specific workflow using either the workflow ID, or the project and issue type ID pair. The response includes the scope of the workflow, defined as global/project-based, and a list of project types that the workflow is scoped to. It also includes all rules organised into their broad categories (conditions, validators, actions, triggers, screens) as well as the source location (Atlassian-provided, Connect, Forge).  **[Permissions](#permissions) required:**   *  *Administer Jira* project permission to access all, including global-scoped, workflows  *  *Administer projects* project permissions to access project-scoped workflows  The current list of Atlassian-provided rules:  #### Validators ####  A validator rule that checks if a user has the required permissions to execute the transition in the workflow.  ##### Permission validator #####  A validator rule that checks if a user has the required permissions to execute the transition in the workflow.      {        "ruleKey": "system:check-permission-validator",        "parameters": {          "permissionKey": "ADMINISTER_PROJECTS"        }      }  Parameters:   *  `permissionKey` The permission required to perform the transition. Allowed values: [built-in Jira permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permission-schemes/#built-in-permissions).  ##### Parent or child blocking validator #####  A validator to block the child issue\\u2019s transition depending on the parent issue\\u2019s status.      {        "ruleKey" : "system:parent-or-child-blocking-validator"        "parameters" : {          "blocker" : "PARENT"          "statusIds" : "1,2,3"        }      }  Parameters:   *  `blocker` currently only supports `PARENT`.  *  `statusIds` a comma-separated list of status IDs.  ##### Previous status validator #####  A validator that checks if an issue has transitioned through specified previous status(es) before allowing the current transition to occur.      {        "ruleKey": "system:previous-status-validator",        "parameters": {          "previousStatusIds": "10014",          "mostRecentStatusOnly": "true"        }      }  Parameters:   *  `previousStatusIds` a comma-separated list of status IDs, currently only support one ID.  *  `mostRecentStatusOnly` when `true` only considers the most recent status for the condition evaluation. Allowed values: `true`, `false`.  ##### Validate a field value #####  A validation that ensures a specific field's value meets the defined criteria before allowing an issue to transition in the workflow.  Depending on the rule type, the result will vary:  ###### Field required ######      {        "ruleKey": "system:validate-field-value",        "parameters": {          "ruleType": "fieldRequired",          "fieldsRequired": "assignee",          "ignoreContext": "true",          "errorMessage": "An assignee must be set!"        }      }  Parameters:   *  `fieldsRequired` the ID of the field that is required. For a custom field, it would look like `customfield_123`.  *  `ignoreContext` controls the impact of context settings on field validation. When set to `true`, the validator doesn't check a required field if its context isn't configured for the current issue. When set to `false`, the validator requires a field even if its context is invalid. Allowed values: `true`, `false`.  *  `errorMessage` is the error message to display if the user does not provide a value during the transition. A default error message will be shown if you don't provide one (Optional).  ###### Field changed ######      {        "ruleKey": "system:validate-field-value",        "parameters": {          "ruleType": "fieldChanged",          "groupsExemptFromValidation": "6862ac20-8672-4f68-896d-4854f5efb79e",          "fieldKey": "versions",          "errorMessage": "Affect versions must be modified before transition"        }      }  Parameters:   *  `groupsExemptFromValidation` a comma-separated list of group IDs to be exempt from the validation.  *  `fieldKey` the ID of the field that has changed. For a custom field, it would look like `customfield_123`.  *  `errorMessage` the error message to display if the user does not provide a value during the transition. A default error message will be shown if you don't provide one (Optional).  ###### Field has a single value ######      {        "ruleKey": "system:validate-field-value",        "parameters": {          "ruleType": "fieldHasSingleValue",          "fieldKey": "created",          "excludeSubtasks": "true"        }      }  Parameters:   *  `fieldKey` the ID of the field to validate. For a custom field, it would look like `customfield_123`.  *  `excludeSubtasks` Option to exclude values copied from sub-tasks. Allowed values: `true`, `false`.  ###### Field matches regular expression ######      {        "ruleKey": "system:validate-field-value",        "parameters": {          "ruleType": "fieldMatchesRegularExpression",          "regexp": "[0-9]{4}",          "fieldKey": "description"        }      }  Parameters:   *  `regexp` the regular expression used to validate the field\\u2019s content.  *  `fieldKey` the ID of the field to validate. For a custom field, it would look like `customfield_123`.  ###### Date field comparison ######      {        "ruleKey": "system:validate-field-value",        "parameters": {          "ruleType": "dateFieldComparison",          "date1FieldKey": "duedate",          "date2FieldKey": "customfield_10054",          "includeTime": "true",          "conditionSelected": ">="        }      }  Parameters:   *  `date1FieldKey` the ID of the first field to compare. For a custom field, it would look like `customfield_123`.  *  `date2FieldKey` the ID of the second field to compare. For a custom field, it would look like `customfield_123`.  *  `includeTime` if `true`, compares both date and time. Allowed values: `true`, `false`.  *  `conditionSelected` the condition to compare with. Allowed values: `>`, `>=`, `=`, `<=`, `<`, `!=`.  ###### Date range comparison ######      {        "ruleKey": "system:validate-field-value",        "parameters": {          "ruleType": "windowDateComparison",          "date1FieldKey": "customfield_10009",          "date2FieldKey": "customfield_10054",          "numberOfDays": "3"        }      }  Parameters:   *  `date1FieldKey` the ID of the first field to compare. For a custom field, it would look like `customfield_123`.  *  `date2FieldKey` the ID of the second field to compare. For a custom field, it would look like `customfield_123`.  *  `numberOfDays` maximum number of days past the reference date (`date2FieldKey`) to pass validation.  This rule is composed by aggregating the following legacy rules:   *  FieldRequiredValidator  *  FieldChangedValidator  *  FieldHasSingleValueValidator  *  RegexpFieldValidator  *  DateFieldValidator  *  WindowsDateValidator  ##### Proforma: Forms attached validator #####  Validates that one or more forms are attached to the issue.      {        "ruleKey" : "system:proforma-forms-attached"        "parameters" : {}      }  ##### Proforma: Forms submitted validator #####  Validates that all forms attached to the issue have been submitted.      {        "ruleKey" : "system:proforma-forms-submitted"        "parameters" : {}      }  #### Conditions ####  Conditions enable workflow rules that govern whether a transition can execute.  ##### Check field value #####  A condition rule evaluates as true if a specific field's value meets the defined criteria. This rule ensures that an issue can only transition to the next step in the workflow if the field's value matches the desired condition.      {        "ruleKey": "system:check-field-value",        "parameters": {          "fieldId": "description",          "fieldValue": "[\"Done\"]",          "comparator": "=",          "comparisonType": "STRING"        }      }  Parameters:   *  `fieldId` The ID of the field to check the value of. For non-system fields, it will look like `customfield_123`. Note: `fieldId` is used interchangeably with the idea of `fieldKey` here, they refer to the same field.  *  `fieldValue` the list of values to check against the field\\u2019s value.  *  `comparator` The comparison logic. Allowed values: `>`, `>=`, `=`, `<=`, `<`, `!=`.  *  `comparisonType` The type of data being compared. Allowed values: `STRING`, `NUMBER`, `DATE`, `DATE_WITHOUT_TIME`, `OPTIONID`.  ##### Restrict issue transition #####  This rule ensures that issue transitions are restricted based on user accounts, roles, group memberships, and permissions, maintaining control over who can transition an issue. This condition evaluates as `true` if any of the following criteria is met.      {        "ruleKey": "system:restrict-issue-transition",        "parameters": {          "accountIds": "allow-reporter,5e68ac137d64450d01a77fa0",          "roleIds": "10002,10004",          "groupIds": "703ff44a-7dc8-4f4b-9aa6-a65bf3574fa4",          "permissionKeys": "ADMINISTER_PROJECTS",          "groupCustomFields": "customfield_10028",          "allowUserCustomFields": "customfield_10072,customfield_10144,customfield_10007",          "denyUserCustomFields": "customfield_10107"        }      }  Parameters:   *  `accountIds` a comma-separated list of the user account IDs. It also allows generic values like: `allow-assignee`, `allow-reporter`, and `accountIds` Note: This is only supported in team-managed projects  *  `roleIds` a comma-separated list of role IDs.  *  `groupIds` a comma-separated list of group IDs.  *  `permissionKeys` a comma-separated list of permission keys. Allowed values: [built-in Jira permissions](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-permission-schemes/#built-in-permissions).  *  `groupCustomFields` a comma-separated list of group custom field IDs.  *  `allowUserCustomFields` a comma-separated list of user custom field IDs to allow for issue transition.  *  `denyUserCustomFields` a comma-separated list of user custom field IDs to deny for issue transition.  This rule is composed by aggregating the following legacy rules:   *  AllowOnlyAssignee  *  AllowOnlyReporter  *  InAnyProjectRoleCondition  *  InProjectRoleCondition  *  UserInAnyGroupCondition  *  UserInGroupCondition  *  PermissionCondtion  *  InGroupCFCondition  *  UserIsInCustomFieldCondition  ##### Previous status condition #####  A condition that evaluates based on an issue's previous status(es) and specific criteria.      {        "ruleKey" : "system:previous-status-condition"        "parameters" : {          "previousStatusIds" : "10004",          "not": "true",          "mostRecentStatusOnly" : "true",          "includeCurrentStatus": "true",          "ignoreLoopTransitions": "true"        }      }  Parameters:   *  `previousStatusIds` a comma-separated list of status IDs, current only support one ID.  *  `not` indicates if the condition should be reversed. When `true` it checks that the issue has not been in the selected statuses. Allowed values: `true`, `false`.  *  `mostRecentStatusOnly` when true only considers the most recent status for the condition evaluation. Allowed values: `true`, `false`.  *  `includeCurrentStatus` includes the current status when evaluating if the issue has been through the selected statuses. Allowed values: `true`, `false`.  *  `ignoreLoopTransitions` ignore loop transitions. Allowed values: `true`, `false`.  ##### Parent or child blocking condition #####  A condition to block the parent\\u2019s issue transition depending on the child\\u2019s issue status.      {        "ruleKey" : "system:parent-or-child-blocking-condition"        "parameters" : {          "blocker" : "CHILD",          "statusIds" : "1,2,3"        }      }  Parameters:   *  `blocker` currently only supports `CHILD`.  *  `statusIds` a comma-separated list of status IDs.  ##### Separation of duties #####  A condition preventing the user from performing, if the user has already performed a transition on the issue.      {        "ruleKey": "system:separation-of-duties",        "parameters": {          "fromStatusId": "10161",          "toStatusId": "10160"        }      }  Parameters:   *  `fromStatusId` represents the status ID from which the issue is transitioning. It ensures that the user performing the current transition has not performed any actions when the issue was in the specified status.  *  `toStatusId` represents the status ID to which the issue is transitioning. It ensures that the user performing the current transition is not the same user who has previously transitioned the issue.  ##### Restrict transitions #####  A condition preventing all users from transitioning the issue can also optionally include APIs as well.      {        "ruleKey": "system:restrict-from-all-users",        "parameters": {          "restrictMode": "users"        }      }  Parameters:   *  `restrictMode` restricts the issue transition including/excluding APIs. Allowed values: `"users"`, `"usersAndAPI"`.  ##### Jira Service Management block until approved #####  Block an issue transition until approval. Note: This is only supported in team-managed projects.      {        "ruleKey": "system:jsd-approvals-block-until-approved",        "parameters": {          "approvalConfigurationJson": "{"statusExternalUuid...}"        }      }  Parameters:   *  `approvalConfigurationJson` a stringified JSON holding the Jira Service Management approval configuration.  ##### Jira Service Management block until rejected #####  Block an issue transition until rejected. Note: This is only supported in team-managed projects.      {        "ruleKey": "system:jsd-approvals-block-until-rejected",        "parameters": {          "approvalConfigurationJson": "{"statusExternalUuid...}"        }      }  Parameters:   *  `approvalConfigurationJson` a stringified JSON holding the Jira Service Management approval configuration.  ##### Block in progress approval #####  Condition to block issue transition if there is pending approval. Note: This is only supported in company-managed projects.      {        "ruleKey": "system:block-in-progress-approval",        "parameters": {}      }  #### Post functions ####  Post functions carry out any additional processing required after a workflow transition is executed.  ##### Change assignee #####  A post function rule that changes the assignee of an issue after a transition.      {        "ruleKey": "system:change-assignee",        "parameters": {          "type": "to-selected-user",          "accountId": "example-account-id"        }      }  Parameters:   *  `type` the parameter used to determine the new assignee. Allowed values: `to-selected-user`, `to-unassigned`, `to-current-user`, `to-current-user`, `to-default-user`, `to-default-user`  *  `accountId` the account ID of the user to assign the issue to. This parameter is required only when the type is `"to-selected-user"`.  ##### Copy field value #####  A post function that automates the process of copying values between fields during a specific transition, ensuring data consistency and reducing manual effort.      {        "ruleKey": "system:copy-value-from-other-field",        "parameters": {          "sourceFieldKey": "description",          "targetFieldKey": "components",          "issueSource": "SAME"        }      }  Parameters:   *  `sourceFieldKey` the field key to copy from. For a custom field, it would look like `customfield_123`  *  `targetFieldKey` the field key to copy to. For a custom field, it would look like `customfield_123`  *  `issueSource` `SAME` or `PARENT`. Defaults to `SAME` if no value is provided.  ##### Update field #####  A post function that updates or appends a specific field with the given value.      {        "ruleKey": "system:update-field",        "parameters": {          "field": "customfield_10056",          "value": "asdf",          "mode": "append"        }      }  Parameters:   *  `field` the ID of the field to update. For a custom field, it would look like `customfield_123`  *  `value` the value to update the field with.  *  `mode` `append` or `replace`. Determines if a value will be appended to the current value, or if the current value will be replaced.  ##### Trigger webhook #####  A post function that automatically triggers a predefined webhook when a transition occurs in the workflow.      {        "ruleKey": "system:trigger-webhook",        "parameters": {          "webhookId": "1"        }      }  Parameters:   *  `webhookId` the ID of the webhook.  #### Screen ####  ##### Remind people to update fields #####  A screen rule that prompts users to update a specific field when they interact with an issue screen during a transition. This rule is useful for ensuring that users provide or modify necessary information before moving an issue to the next step in the workflow.      {        "ruleKey": "system:remind-people-to-update-fields",        "params": {          "remindingFieldIds": "assignee,customfield_10025",          "remindingMessage": "The message",          "remindingAlwaysAsk": "true"        }      }  Parameters:   *  `remindingFieldIds` a comma-separated list of field IDs. Note: `fieldId` is used interchangeably with the idea of `fieldKey` here, they refer to the same field.  *  `remindingMessage` the message to display when prompting the users to update the fields.  *  `remindingAlwaysAsk` always remind to update fields. Allowed values: `true`, `false`.  ##### Shared transition screen #####  A common screen that is shared between transitions in a workflow.      {        "ruleKey": "system:transition-screen",        "params": {          "screenId": "3"        }      }  Parameters:   *  `screenId` the ID of the screen.  #### Connect & Forge ####  ##### Connect rules #####  Validator/Condition/Post function for Connect app.      {        "ruleKey": "connect:expression-validator",        "parameters": {          "appKey": "com.atlassian.app",          "config": "",          "id": "90ce590f-e90c-4cd3-8281-165ce41f2ac3",          "disabled": "false",          "tag": ""        }      }  Parameters:   *  `ruleKey` Validator: `connect:expression-validator`, Condition: `connect:expression-condition`, and Post function: `connect:remote-workflow-function`  *  `appKey` the reference to the Connect app  *  `config` a JSON payload string describing the configuration  *  `id` the ID of the rule  *  `disabled` determine if the Connect app is disabled. Allowed values: `true`, `false`.  *  `tag` additional tags for the Connect app  ##### Forge rules #####  Validator/Condition/Post function for Forge app.      {        "ruleKey": "forge:expression-validator",        "parameters": {          "key": "ari:cloud:ecosystem::extension/{appId}/{environmentId}/static/{moduleKey}",          "config": "{"searchString":"workflow validator"}",          "id": "a865ddf6-bb3f-4a7b-9540-c2f8b3f9f6c2"        }      }  Parameters:   *  `ruleKey` Validator: `forge:expression-validator`, Condition: `forge:expression-condition`, and Post function: `forge:workflow-post-function`  *  `key` the identifier for the Forge app  *  `config` the persistent stringified JSON configuration for the Forge rule  *  `id` the ID of the Forge rule
            {
                "name": "workflow_capabilities",
                "table_name": "available_workflow_connect_rule",
                "endpoint": {
                    "data_selector": "connectRules",
                    "path": "/rest/api/3/workflows/capabilities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "workflowId": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "issueTypeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of system avatar details by owner type, where the owner types are issue type, project, or user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_system_avatars",
                "table_name": "avatar",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "system",
                    "path": "/rest/api/3/avatar/{type}/system",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all project avatars, grouped by system and custom avatars.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_all_project_avatars",
                "table_name": "avatar",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom",
                    "path": "/rest/api/3/project/{projectIdOrKey}/avatars",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the system and custom avatars for a project or issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  for custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.  *  for custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.  *  for system avatars, none.
            {
                "name": "get_avatars",
                "table_name": "avatars",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/universal_avatar/type/{type}/owner/{entityId}",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "entityId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of IDs and delete timestamps for worklogs deleted after a date and time.  This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.  This resource does not return worklogs deleted during the minute preceding the request.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_ids_of_worklogs_deleted_since",
                "table_name": "changed_worklog",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/worklog/deleted",
                    "paginator": {
                        "type": "cursor",
                        "cursor_path": "since",
                        "cursor_param": "since",
                    },
                },
            },
            # Returns a list of IDs and update timestamps for worklogs updated after a date and time.  This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs.  This resource does not return worklogs updated during the minute preceding the request.  **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true:   *  the worklog is set as *Viewable by All Users*.  *  the user is a member of a project role or group with permission to view the worklog.
            {
                "name": "get_ids_of_worklogs_modified_since",
                "table_name": "changed_worklog",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/worklog/updated",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "cursor",
                        "cursor_path": "since",
                        "cursor_param": "since",
                    },
                },
            },
            # Returns a [paginated](#pagination) list of all changelogs for an issue sorted by date, starting from the oldest.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_change_logs",
                "table_name": "changelog",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/changelog",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in *List View* with the *Columns* set to *Filter*.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, column details are only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.
            {
                "name": "get_columns",
                "table_name": "column_item",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/{id}/columns",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the default issue navigator columns.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_navigator_default_columns",
                "table_name": "column_item",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/settings/columns",
                    "paginator": "auto",
                },
            },
            # Returns the default [issue table columns](https://confluence.atlassian.com/x/XYdKLg) for the user. If `accountId` is not passed in the request, the calling user's details are returned.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLgl), to get the column details for any user.  *  Permission to access Jira, to get the calling user's column details.
            {
                "name": "get_user_default_columns",
                "table_name": "column_item",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/columns",
                    "params": {
                        # the parameters below can optionally be configured
                        # "accountId": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all comments for an issue.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Comments are included in the response where the user has:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the comment has visibility restrictions, belongs to the group or has the role visibility is role visibility is restricted to.
            {
                "name": "get_comments",
                "table_name": "comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "comments",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/comment",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "5000",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a comment.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the comment.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the comment has visibility restrictions, the user belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_comment",
                "table_name": "comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/comment/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_comments",
                            "field": "id",
                        },
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the counts of issues assigned to the component.  This operation can be accessed anonymously.  **Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.   *  **Classic**: `read:jira-work`  *  **Granular**: `read:field:jira`, `read:project.component:jira`  **[Permissions](#permissions) required:** None.
            {
                "name": "get_component_related_issues",
                "table_name": "component_issues_count",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/component/{id}/relatedIssueCounts",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_components_for_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all components in a project, including global (Compass) components when applicable.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "find_components_for_projects",
                "table_name": "component_json_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/component",
                    "params": {
                        # the parameters below can optionally be configured
                        # "projectIdsOrKeys": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all components in a project. See the [Get project components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a full list of versions without pagination.  If your project uses Compass components, this API will return a list of Compass components that are linked to issues in that project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_components_paginated",
                "table_name": "component_with_issue_count",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/project/{projectIdOrKey}/component",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "componentSource": "jira",
                        # "query": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [global settings](https://confluence.atlassian.com/x/qYXKM) in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_configuration",
                "table_name": "configuration",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/configuration",
                    "paginator": "auto",
                },
            },
            # Returns all modules registered dynamically by the calling app.  **[Permissions](#permissions) required:** Only Connect apps can make this request.
            {
                "name": "dynamic_modules_resource_get_modules_get",
                "table_name": "connect_module",
                "endpoint": {
                    "data_selector": "modules",
                    "path": "/rest/atlassian-connect/1/app/module/dynamic",
                    "paginator": "auto",
                },
            },
            # Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) for details.  To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-thumbnail-id-get).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** For the issue containing the attachment:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_attachment_content",
                "table_name": "content",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/attachment/content/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "redirect": "true",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get custom field contexts](#api-rest-api-3-field-fieldId-context-get).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_contexts_for_field_deprecated",
                "table_name": "context",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/contexts",
                    "params": {
                        "fieldId": {
                            "type": "resolve",
                            "resource": "get_fields",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "20",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of configurations for a custom field of a [type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/) created by a [Forge app](https://developer.atlassian.com/platform/forge/).  The result can be filtered by one of these criteria:   *  `id`.  *  `fieldContextId`.  *  `issueId`.  *  `projectKeyOrId` and `issueTypeId`.  Otherwise, all configurations are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that provided the custom field type.
            {
                "name": "get_custom_field_configuration",
                "table_name": "contextual_configuration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/app/field/{fieldIdOrKey}/context/configuration",
                    "params": {
                        "fieldIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "id": "OPTIONAL_CONFIG",
                        # "fieldContextId": "OPTIONAL_CONFIG",
                        # "issueId": "OPTIONAL_CONFIG",
                        # "projectKeyOrId": "OPTIONAL_CONFIG",
                        # "issueTypeId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows:   *  With no other parameters set, all contexts.  *  By defining `id` only, all contexts from the list of IDs.  *  By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false)  *  By defining `isGlobalContext`, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_contexts_for_field",
                "table_name": "custom_field_context",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/context",
                    "params": {
                        "fieldId": {
                            "type": "resolve",
                            "resource": "get_fields",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "isAnyIssueType": "OPTIONAL_CONFIG",
                        # "isGlobalContext": "OPTIONAL_CONFIG",
                        # "contextId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is returned.   The returned object depends on type of the custom field:   *  `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.  *  `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.  *  `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select lists and radio buttons.  *  `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice select lists and checkboxes.  *  `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select lists.  *  `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.  *  `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.  *  `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice group pickers.  *  `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple choice group pickers.  *  `CustomFieldContextDefaultValueURL` (type `url`) for URLs.  *  `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.  *  `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).  *  `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.  *  `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.  *  `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.  *  `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.  *  `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice version pickers.  *  `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice version pickers.  Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field-type/#data-types) are also supported, returning:   *  `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string fields.  *  `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge string collection fields.  *  `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object fields.  *  `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-time fields.  *  `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.  *  `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge group collection fields.  *  `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number fields.  *  `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.  *  `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user collection fields.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_default_values",
                "table_name": "custom_field_context_default_value",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/context/defaultValue",
                    "params": {
                        "fieldId": {
                            "type": "resolve",
                            "resource": "get_contexts_for_field",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "contextId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira.  This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.**  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_options_for_context",
                "table_name": "custom_field_context_option",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/context/{contextId}/option",
                    "params": {
                        "contextId": {
                            "type": "resolve",
                            "resource": "get_contexts_for_field",
                            "field": "id",
                        },
                        "fieldId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "optionId": "OPTIONAL_CONFIG",
                        # "onlyOptions": "false",
                        # "startAt": "0",
                        # "maxResults": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of context to project mappings for a custom field. The result can be filtered by `contextId`. Otherwise, all mappings are returned. Invalid IDs are ignored.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_project_context_mapping",
                "table_name": "custom_field_context_project_mapping",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/context/projectmapping",
                    "params": {
                        "fieldId": {
                            "type": "resolve",
                            "resource": "get_contexts_for_field",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "contextId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a custom field option. For example, an option in a select list.  Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The custom field option is returned as follows:   *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.
            {
                "name": "get_custom_field_option",
                "table_name": "custom_field_option",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/customFieldOption/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_dashboards",
                "table_name": "dashboard",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "dashboards",
                    "path": "/rest/api/3/dashboard",
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "next",
                    },
                },
            },
            # Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The following dashboards that match the query parameters are returned:   *  Dashboards owned by the user. Not returned for anonymous users.  *  Dashboards shared with a group that the user is a member of. Not returned for anonymous users.  *  Dashboards shared with a private project that the user can browse. Not returned for anonymous users.  *  Dashboards shared with a public project.  *  Dashboards shared with the public.
            {
                "name": "get_dashboards_paginated",
                "table_name": "dashboard",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/dashboard/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "dashboardName": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "owner": "OPTIONAL_CONFIG",
                        # "groupname": "OPTIONAL_CONFIG",
                        # "groupId": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "orderBy": "name",
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "status": "active",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a dashboard.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.  However, to get a dashboard, the dashboard must be shared with the user or the user must own it. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users.
            {
                "name": "get_dashboard",
                "table_name": "dashboard",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/dashboard/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_dashboards",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of dashboard gadgets on a dashboard.  This operation returns:   *  Gadgets from a list of IDs, when `id` is set.  *  Gadgets with a module key, when `moduleKey` is set.  *  Gadgets from a list of URIs, when `uri` is set.  *  All gadgets, when no other parameters are set.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_gadgets",
                "table_name": "dashboard_gadget",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "gadgets",
                    "path": "/rest/api/3/dashboard/{dashboardId}/gadget",
                    "params": {
                        "dashboardId": {
                            "type": "resolve",
                            "resource": "get_all_dashboards",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "moduleKey": "OPTIONAL_CONFIG",
                        # "uri": "OPTIONAL_CONFIG",
                        # "gadgetId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all classification levels.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_user_data_classification_levels",
                "table_name": "data_classification_tag_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "classifications",
                    "path": "/rest/api/3/classification-levels",
                    "params": {
                        # the parameters below can optionally be configured
                        # "status": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the default data classification for a project.  **[Permissions](#permissions) required:**   *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_default_project_classification",
                "table_name": "default",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/classification-level/default",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the default sharing settings for new filters and dashboards for a user.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_default_share_scope",
                "table_name": "default_share_scope",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/defaultShareScope",
                    "paginator": "auto",
                },
            },
            # Returns the default workflow for a workflow scheme. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_default_workflow",
                "table_name": "default_workflow",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflowscheme/{id}/default",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_workflow_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "returnDraftIfExists": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the default workflow for a workflow scheme's draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_draft_default_workflow",
                "table_name": "default_workflow",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflowscheme/{id}/draft/default",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all workflows in Jira or a workflow. Deprecated, use [Get workflows paginated](#api-rest-api-3-workflow-search-get).  If the `workflowName` parameter is specified, the workflow is returned as an object (not in an array). Otherwise, an array of workflow objects is returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_workflows",
                "table_name": "deprecated_workflow",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflow",
                    "params": {
                        # the parameters below can optionally be configured
                        # "workflowName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the edit screen fields for an issue that are visible to and editable by the user. Use the information to populate the requests in [Edit issue](#api-rest-api-3-issue-issueIdOrKey-put).  This endpoint will check for these conditions:  1.  Field is available on a field screen - through screen, screen scheme, issue type screen scheme, and issue type scheme configuration. `overrideScreenSecurity=true` skips this condition. 2.  Field is visible in the [field configuration](https://support.atlassian.com/jira-cloud-administration/docs/change-a-field-configuration/). `overrideScreenSecurity=true` skips this condition. 3.  Field is shown on the issue: each field has different conditions here. For example: Attachment field only shows if attachments are enabled. Assignee only shows if user has permissions to assign the issue. 4.  If a field is custom then it must have valid custom field context, applicable for its project and issue type. All system fields are assumed to have context in all projects and all issue types. 5.  Issue has a project, issue type, and status defined. 6.  Issue is assigned to a valid workflow, and the current status has assigned a workflow step. `overrideEditableFlag=true` skips this condition. 7.  The current workflow step is editable. This is true by default, but [can be disabled by setting](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) the `jira.issue.editable` property to `false`. `overrideEditableFlag=true` skips this condition. 8.  User has [Edit issues permission](https://support.atlassian.com/jira-cloud-administration/docs/permissions-for-company-managed-projects/). 9.  Workflow permissions allow editing a field. This is true by default but [can be modified](https://support.atlassian.com/jira-cloud-administration/docs/use-workflow-properties/) using `jira.permission.*` workflow properties.  Fields hidden using [Issue layout settings page](https://support.atlassian.com/jira-software-cloud/docs/configure-field-layout-in-the-issue-view/) remain editable.  Connect apps having an app user with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), and Forge apps acting on behalf of users with *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), can return additional details using:   *  `overrideScreenSecurity` When this flag is `true`, then this endpoint skips checking if fields are available through screens, and field configuration (conditions 1. and 2. from the list above).  *  `overrideEditableFlag` When this flag is `true`, then this endpoint skips checking if workflow is present and if the current step is editable (conditions 6. and 7. from the list above).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  Note: For any fields to be editable the user must have the *Edit issues* [project permission](https://confluence.atlassian.com/x/yodKLg) for the issue.
            {
                "name": "get_edit_issue_meta",
                "table_name": "editmetum",
                "endpoint": {
                    "data_selector": "fields",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/editmeta",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "overrideScreenSecurity": "false",
                        # "overrideEditableFlag": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [project's sender email address](https://confluence.atlassian.com/x/dolKLg).  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_email",
                "table_name": "email",
                "endpoint": {
                    "data_selector": "emailAddressStatus",
                    "path": "/rest/api/3/project/{projectId}/email",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the value of a comment property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_comment_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/comment/{commentId}/properties/{propertyKey}",
                    "params": {
                        "commentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the key and value of a dashboard item property.  A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ).  When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.  There is no resource to set or get dashboard items.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the dashboard shared with them. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users, and is accessible to anonymous users when Jira\\u2019s anonymous access is permitted.
            {
                "name": "get_dashboard_item_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties/{propertyKey}",
                    "params": {
                        "dashboardId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "itemId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the key and value of an issue's property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_issue_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/properties/{propertyKey}",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the value of a worklog property.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_worklog_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties/{propertyKey}",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "worklogId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the key and value of the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the details of any issue type.  *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the details of any issue types associated with the projects the user has permission to browse.
            {
                "name": "get_issue_type_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issuetype/{issueTypeId}/properties/{propertyKey}",
                    "params": {
                        "issueTypeId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the value of a [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the property.
            {
                "name": "get_project_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/properties/{propertyKey}",
                    "params": {
                        "projectIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the value of a user's property. If no property key is provided [Get user property keys](#api-rest-api-3-user-properties-get) is called.  Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get a property from any user.  *  Access to Jira, to get a property from the calling user's record.
            {
                "name": "get_user_property",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/properties/{propertyKey}",
                    "params": {
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "accountId": "OPTIONAL_CONFIG",
                        # "userKey": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the key and value of an app's property.  **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
            {
                "name": "addon_properties_resource_get_addon_property_get",
                "table_name": "entity_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/atlassian-connect/1/addons/{addonKey}/properties/{propertyKey}",
                    "params": {
                        "addonKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "propertyKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns webhooks that have recently failed to be delivered to the requesting app after the maximum number of retries.  After 72 hours the failure may no longer be returned by this operation.  The oldest failure is returned first.  This method uses a cursor-based pagination. To request the next page use the failure time of the last webhook on the list as the `failedAfter` value or use the URL provided in `next`.  **[Permissions](#permissions) required:** Only [Connect apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this operation.
            {
                "name": "get_failed_webhooks",
                "table_name": "failed_webhook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/webhook/failed",
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "next",
                    },
                },
            },
            # Returns a [paginated](#pagination) list of fields for Classic Jira projects. The list can include:   *  all fields  *  specific fields, by defining `id`  *  fields that contain a string in the field name or description, by defining `query`  *  specific fields that contain a string in the field name or description, by defining `id` and `query`  Only custom fields can be queried, `type` must be set to `custom`.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_fields_paginated",
                "table_name": "field",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "type": "OPTIONAL_CONFIG",
                        # "id": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of fields in the trash. The list may be restricted to fields whose field name or description partially match a string.  Only custom fields can be queried, `type` must be set to `custom`.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_trashed_fields_paginated",
                "table_name": "field",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/search/trashed",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of field configurations. The list can be for all field configurations or a subset determined by any combination of these criteria:   *  a list of field configuration item IDs.  *  whether the field configuration is a default.  *  whether the field configuration name or description contains a query string.  Only field configurations used in company-managed (classic) projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_field_configurations",
                "table_name": "field_configuration_details",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/fieldconfiguration",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "isDefault": "false",
                        # "query": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of field configuration issue type items.  Only items used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_field_configuration_scheme_mappings",
                "table_name": "field_configuration_issue_type_item",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/fieldconfigurationscheme/mapping",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "fieldConfigurationSchemeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all fields for a configuration.  Only the fields from configurations used in company-managed (classic) projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_field_configuration_items",
                "table_name": "field_configuration_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/fieldconfiguration/{id}/fields",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of field configuration schemes.  Only field configuration schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_field_configuration_schemes",
                "table_name": "field_configuration_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/fieldconfigurationscheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list of the projects that use it.  The list is sorted by field configuration scheme ID. The first item contains the list of project IDs assigned to the default field configuration scheme.  Only field configuration schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_field_configuration_scheme_project_mapping",
                "table_name": "field_configuration_scheme_projects",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/fieldconfigurationscheme/project",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns system and custom issue fields according to the following rules:   *  Fields that cannot be added to the issue navigator are always returned.  *  Fields that cannot be placed on an issue screen are always returned.  *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is, timetracking fields, subtasks, votes, and watches.  *  For all other fields, this operation only returns the fields that the user has permission to view (that is, the field is used in at least one project that the user has *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.)  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_fields",
                "table_name": "field_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/field",
                    "paginator": "auto",
                },
            },
            # Returns the visible favorite filters of the user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the filter is:   *  owned by the user.  *  shared with a group that the user is a member of.  *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  shared with a public project.  *  shared with the public.  For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.
            {
                "name": "get_favourite_filters",
                "table_name": "filter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/favourite",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the filters owned by the user. If `includeFavourites` is `true`, the user's visible favorite filters are also returned.  **[Permissions](#permissions) required:** Permission to access Jira, however, a favorite filters is only visible to the user where the filter is:   *  owned by the user.  *  shared with a group that the user is a member of.  *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  shared with a public project.  *  shared with the public.  For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.
            {
                "name": "get_my_filters",
                "table_name": "filter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/my",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "includeFavourites": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a filter.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, the filter is only returned where it is:   *  owned by the user.  *  shared with a group that the user is a member of.  *  shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  shared with a public project.  *  shared with the public.
            {
                "name": "get_filter",
                "table_name": "filter",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "overrideSharePermissions": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of filters. Use this operation to get:   *  specific filters, by defining `id` only.  *  filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. When multiple attributes are specified only filters matching all attributes are returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, only the following filters that match the query parameters are returned:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.
            {
                "name": "get_filters_paginated",
                "table_name": "filter_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/filter/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filterName": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "owner": "OPTIONAL_CONFIG",
                        # "groupname": "OPTIONAL_CONFIG",
                        # "groupId": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "id": "OPTIONAL_CONFIG",
                        # "orderBy": "name",
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "expand": "OPTIONAL_CONFIG",
                        # "overrideSharePermissions": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of groups whose names contain a query string. A list of group names can be provided to exclude groups from the results.  The primary use case for this resource is to populate a group picker suggestions list. To this end, the returned object includes the `html` field where the matched query term is highlighted in the group name with the HTML strong tag. Also, the groups list is wrapped in a response object that contains a header for use in the picker, specifically *Showing X of Y matching groups*.  The list returns with the groups sorted. If no groups match the list criteria, an empty list is returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without the required permission return an empty list.  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without this permission, calls where query is not an exact match to an existing group will return an empty list.
            {
                "name": "find_groups",
                "table_name": "found_group",
                "endpoint": {
                    "data_selector": "groups",
                    "path": "/rest/api/3/groups/picker",
                    "params": {
                        # the parameters below can optionally be configured
                        # "accountId": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "excludeId": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "caseInsensitive": "false",
                        # "userName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users and groups matching a string. The string is used:   *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required.  *  for groups, to find a case-sensitive match with group name.  For example, if the string *tin* is used, records with the display name *Tina*, email address *sarah@tinplatetraining.com*, and the group *accounting* would be returned.  Optionally, the search can be refined to:   *  the projects and issue types associated with a custom field, such as a user picker. The search can then be further refined to return only users and groups that have permission to view specific:           *  projects.      *  issue types.          If multiple projects or issue types are specified, they must be a subset of those enabled for the custom field or no results are returned. For example, if a field is enabled for projects A, B, and C then the search could be limited to projects B and C. However, if the search is limited to projects B and D, nothing is returned.  *  not return Connect app users and groups.  *  return groups that have a case-insensitive match with the query.  The primary use case for this resource is to populate a picker field suggestion list with users or groups. To this end, the returned object includes an `html` field for each list. This field highlights the matched query term in the item name with the HTML strong tag. Also, each list is wrapped in a response object that contains a header for use in a picker, specifically *Showing X of Y matching groups*.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/yodKLg).
            {
                "name": "find_users_and_groups",
                "table_name": "found_group",
                "endpoint": {
                    "data_selector": "groups.groups",
                    "path": "/rest/api/3/groupuserpicker",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "50",
                        # "showAvatar": "false",
                        # "fieldId": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "issueTypeId": "OPTIONAL_CONFIG",
                        # "avatarSize": "xsmall",
                        # "caseInsensitive": "false",
                        # "excludeConnectAddons": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of groups.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "bulk_get_groups",
                "table_name": "group_details",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/group/bulk",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "groupId": "OPTIONAL_CONFIG",
                        # "groupName": "OPTIONAL_CONFIG",
                        # "accessType": "OPTIONAL_CONFIG",
                        # "applicationKey": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the groups to which a user belongs.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_user_groups",
                "table_name": "group_name",
                "primary_key": "groupId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/groups",
                    "params": {
                        "accountId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "username": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns information about the Jira instance.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_server_info",
                "table_name": "health_check_result",
                "endpoint": {
                    "data_selector": "healthChecks",
                    "path": "/rest/api/3/serverInfo",
                    "paginator": "auto",
                },
            },
            # Returns the details for an issue.  The issue is identified by its ID or key, however, if the identifier doesn't match an issue, a case-insensitive search and check for moved issues is performed. If a matching issue is found its details are returned, a 302 or other redirect is **not** returned. The issue key returned in the response is the key of the issue found.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_issue",
                "table_name": "issue_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "fieldsByKeys": "false",
                        # "expand": "OPTIONAL_CONFIG",
                        # "properties": "OPTIONAL_CONFIG",
                        # "updateHistory": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ).  If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-rest-api-3-search-post) version of this resource.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Issues are included in the response where the user has:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "search_for_issues_using_jql",
                "table_name": "issue_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "issues",
                    "path": "/rest/api/3/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "jql": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "validateQuery": "strict",
                        # "fields": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                        # "properties": "OPTIONAL_CONFIG",
                        # "fieldsByKeys": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all issue events.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_events",
                "table_name": "issue_event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/events",
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all the options of a select list issue field. A select list issue field is a type of [issue field](https://developer.atlassian.com/cloud/jira/platform/modules/issue-field/) that enables a user to select a value from a list of options.  Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
            {
                "name": "get_all_issue_field_options",
                "table_name": "issue_field_option",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldKey}/option",
                    "params": {
                        "fieldKey": {
                            "type": "resolve",
                            "resource": "get_fields",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed and selected by the user.  Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_selectable_issue_field_options",
                "table_name": "issue_field_option",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldKey}/option/suggestions/edit",
                    "params": {
                        "fieldKey": {
                            "type": "resolve",
                            "resource": "get_all_issue_field_options",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "projectId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of options for a select list issue field that can be viewed by the user.  Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_visible_issue_field_options",
                "table_name": "issue_field_option",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldKey}/option/suggestions/search",
                    "params": {
                        "fieldKey": {
                            "type": "resolve",
                            "resource": "get_all_issue_field_options",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "projectId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns an option from a select list issue field.  Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.
            {
                "name": "get_issue_field_option",
                "table_name": "issue_field_option",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/field/{fieldKey}/option/{optionId}",
                    "params": {
                        "optionId": {
                            "type": "resolve",
                            "resource": "get_all_issue_field_options",
                            "field": "id",
                        },
                        "fieldKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all issues breaching and approaching per-issue limits.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) is required for the project the issues are in. Results may be incomplete otherwise  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_limit_report",
                "table_name": "issue_limit_report_response_bean",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/limit/report",
                    "paginator": "auto",
                },
            },
            # Returns an issue link.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the linked issues.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, permission to view both of the issues.
            {
                "name": "get_issue_link",
                "table_name": "issue_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issueLink/{linkId}",
                    "params": {
                        "linkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all issue link types.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.
            {
                "name": "get_issue_link_types",
                "table_name": "issue_link_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "issueLinkTypes",
                    "path": "/rest/api/3/issueLinkType",
                    "paginator": "auto",
                },
            },
            # Returns an issue link type.  To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.
            {
                "name": "get_issue_link_type",
                "table_name": "issue_link_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issueLinkType/{issueLinkTypeId}",
                    "params": {
                        "issueLinkTypeId": {
                            "type": "resolve",
                            "resource": "get_issue_link_types",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns lists of issues matching a query string. Use this resource to provide auto-completion suggestions when the user is looking for an issue using a word or string.  This operation returns two lists:   *  `History Search` which includes issues from the user's history of created, edited, or viewed issues that contain the string in the `query` parameter.  *  `Current Search` which includes issues that match the JQL expression in `currentJQL` and contain the string in the `query` parameter.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_issue_picker_resource",
                "table_name": "issue_picker_suggestions_issue_type",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "sections",
                    "path": "/rest/api/3/issue/picker",
                    "params": {
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "currentJQL": "OPTIONAL_CONFIG",
                        # "currentIssueKey": "OPTIONAL_CONFIG",
                        # "currentProjectId": "OPTIONAL_CONFIG",
                        # "showSubTasks": "OPTIONAL_CONFIG",
                        # "showSubTaskParent": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns issue security level members.  Only issue security level members in context of classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_security_level_members",
                "table_name": "issue_security_level_member",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuesecurityschemes/{issueSecuritySchemeId}/members",
                    "params": {
                        "issueSecuritySchemeId": {
                            "type": "resolve",
                            "resource": "get_issue_security_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "issueSecurityLevelId": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) mapping of projects that are using security schemes. You can provide either one or multiple security scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Only issue security schemes in the context of classic projects are supported. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "search_projects_using_security_schemes",
                "table_name": "issue_security_scheme_to_project_mapping",
                "primary_key": "projectId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuesecurityschemes/project",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "issueSecuritySchemeId": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns either all transitions or a transition that can be performed by the user on an issue, based on the issue's status.  Note, if a request is made for a transition that does not exist or cannot be performed on the issue, given its status, the response will return any empty transitions list.  This operation can be accessed anonymously.  **[Permissions](#permissions) required: A list or transition is returned only when the user has:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  However, if the user does not have the *Transition issues* [ project permission](https://confluence.atlassian.com/x/yodKLg) the response will not list any transitions.
            {
                "name": "get_transitions",
                "table_name": "issue_transition",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "transitions",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/transitions",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "transitionId": "OPTIONAL_CONFIG",
                        # "skipRemoteOnlyCondition": "false",
                        # "includeUnavailableTransitions": "false",
                        # "sortByOpsBarAndStatus": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all issue types.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Issue types are only returned as follows:   *  if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.  *  if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types associated with the projects the user has permission to browse are returned.
            {
                "name": "get_issue_all_types",
                "table_name": "issue_type_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issuetype",
                    "paginator": "auto",
                },
            },
            # Returns issue types for a project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in the relevant project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_types_for_project",
                "table_name": "issue_type_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issuetype/project",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "level": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns an issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type",
                "table_name": "issue_type_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issuetype/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_issue_all_types",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_alternative_issue_types",
                "table_name": "issue_type_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issuetype/{id}/alternatives",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_issue_all_types",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a page of issue type metadata for a specified project. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
            {
                "name": "get_create_issue_meta_issue_types",
                "table_name": "issue_type_issue_create_metadata",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "createMetaIssueType",
                    "path": "/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_create_issue_meta",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue type schemes.  Only issue type schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_issue_type_schemes",
                "table_name": "issue_type_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "orderBy": "id",
                        # "expand": "OPTIONAL_CONFIG",
                        # "queryString": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue type scheme items.  Only issue type scheme items used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type_schemes_mapping",
                "table_name": "issue_type_scheme_mapping",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescheme/mapping",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "issueTypeSchemeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue type schemes and, for each issue type scheme, a list of the projects that use it.  Only issue type schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type_scheme_for_projects",
                "table_name": "issue_type_scheme_projects",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescheme/project",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue type screen schemes.  Only issue type screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type_screen_schemes",
                "table_name": "issue_type_screen_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescreenscheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "queryString": "OPTIONAL_CONFIG",
                        # "orderBy": "id",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue type screen scheme items.  Only issue type screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type_screen_scheme_mappings",
                "table_name": "issue_type_screen_scheme_item",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescreenscheme/mapping",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "issueTypeScreenSchemeId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue type screen schemes and, for each issue type screen scheme, a list of the projects that use it.  Only issue type screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type_screen_scheme_project_associations",
                "table_name": "issue_type_screen_schemes_projects",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescreenscheme/project",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_type_mappings_for_contexts",
                "table_name": "issue_type_to_context_mapping",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/context/issuetypemapping",
                    "params": {
                        "fieldId": {
                            "type": "resolve",
                            "resource": "get_contexts_for_field",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "contextId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_all_statuses",
                "table_name": "issue_type_with_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/statuses",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow_scheme_draft_issue_type",
                "table_name": "issue_type_workflow_mapping",
                "primary_key": "issueType",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflowscheme/{id}/draft/issuetype/{issueType}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "issueType": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the issue type-workflow mapping for an issue type in a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow_scheme_issue_type",
                "table_name": "issue_type_workflow_mapping",
                "primary_key": "issueType",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflowscheme/{id}/issuetype/{issueType}",
                    "params": {
                        "issueType": {
                            "type": "resolve",
                            "resource": "get_all_workflow_schemes",
                            "field": "id",
                        },
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "returnDraftIfExists": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of the statuses specified by one or more status IDs.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
            {
                "name": "get_statuses_by_id",
                "table_name": "jira_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/statuses",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project.  **[Permissions](#permissions) required:**   *  *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg)  *  *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg)
            {
                "name": "search",
                "table_name": "jira_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/statuses/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "200",
                        # "searchString": "OPTIONAL_CONFIG",
                        # "statusCategory": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of a function's precomputations along with information about when they were created, updated, and last used. Each precomputation has a `value` \- the JQL fragment to replace the custom function clause with.  **[Permissions](#permissions) required:** This API is only accessible to apps and apps can only inspect their own functions.
            {
                "name": "get_precomputations",
                "table_name": "jql_function_precomputation_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/jql/function/computation",
                    "params": {
                        # the parameters below can optionally be configured
                        # "functionKey": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "100",
                        # "orderBy": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Validates a project key by confirming the key is a valid string and not in use.  **[Permissions](#permissions) required:** None.
            {
                "name": "validate_project_key",
                "table_name": "key",
                "endpoint": {
                    "data_selector": "errorMessages",
                    "path": "/rest/api/3/projectvalidate/key",
                    "params": {
                        # the parameters below can optionally be configured
                        # "key": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of labels.
            {
                "name": "get_all_labels",
                "table_name": "label",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/label",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "1000",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the approximate number of user accounts across all Jira licenses. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_approximate_license_count",
                "table_name": "license_metric",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/license/approximateLicenseCount",
                    "paginator": "auto",
                },
            },
            # Returns the total approximate number of user accounts for a single Jira license. Note that this information is cached with a 7-day lifecycle and could be stale at the time of call.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_approximate_application_license_count",
                "table_name": "license_metric",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/license/approximateLicenseCount/product/{applicationKey}",
                    "params": {
                        "applicationKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns licensing information about the Jira instance.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_license",
                "table_name": "licensed_application",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "applications",
                    "path": "/rest/api/3/instance/license",
                    "paginator": "auto",
                },
            },
            # Returns the locale for the user.  If the user has no language preference set (which is the default setting) or this resource is accessed anonymous, the browser locale detected by Jira is returned. Jira detects the browser locale using the *Accept-Language* header in the request. However, if this doesn't match a locale available Jira, the site default locale is returned.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_locale",
                "table_name": "locale",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/mypreferences/locale",
                    "paginator": "auto",
                },
            },
            # Returns a list of permissions indicating which permissions the user has. Details of the user's permissions can be obtained in a global, project, issue or comment context.  The user is reported as having a project permission:   *  in the global context, if the user has the project permission in any project.  *  for a project, where the project permission is determined using issue data, if the user meets the permission's criteria for any issue in the project. Otherwise, if the user has the project permission in the project.  *  for an issue, where a project permission is determined using issue data, if the user has the permission in the issue. Otherwise, if the user has the project permission in the project containing the issue.  *  for a comment, where the user has both the permission to browse the comment and the project permission for the comment's parent issue. Only the BROWSE\_PROJECTS permission is supported. If a `commentId` is provided whose `permissions` does not equal BROWSE\_PROJECTS, a 400 error will be returned.  This means that users may be shown as having an issue permission (such as EDIT\_ISSUES) in the global context or a project context but may not have the permission for any or all issues. For example, if Reporters have the EDIT\_ISSUES permission a user would be shown as having this permission in the global context or the context of a project, because any user can be a reporter. However, if they are not the user who reported the issue queried they would not have EDIT\_ISSUES permission for that issue.  Global permissions are unaffected by context.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_my_permissions",
                "table_name": "mypermission",
                "endpoint": {
                    "data_selector": "permissions",
                    "path": "/rest/api/3/mypermissions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "projectKey": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "issueKey": "OPTIONAL_CONFIG",
                        # "issueId": "OPTIONAL_CONFIG",
                        # "permissions": "OPTIONAL_CONFIG",
                        # "projectUuid": "OPTIONAL_CONFIG",
                        # "projectConfigurationUuid": "OPTIONAL_CONFIG",
                        # "commentId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the value of a preference of the current user.  Note that these keys are deprecated:   *  *jira.user.locale* The locale of the user. By default this is not set and the user takes the locale of the instance.  *  *jira.user.timezone* The time zone of the user. By default this is not set and the user takes the timezone of the instance.  These system preferences keys will be deprecated by 15/07/2024. You can still retrieve these keys, but it will not have any impact on Notification behaviour.   *  *user.notifications.watcher* Whether the user gets notified when they are watcher.  *  *user.notifications.assignee* Whether the user gets notified when they are assignee.  *  *user.notifications.reporter* Whether the user gets notified when they are reporter.  *  *user.notifications.mentions* Whether the user gets notified when they are mentions.  Use [ Update a user profile](https://developer.atlassian.com/cloud/admin/user-management/rest/#api-users-account-id-manage-profile-patch) from the user management REST API to manage timezone and locale instead.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_preference",
                "table_name": "mypreference",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/mypreferences",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of [notification schemes](https://confluence.atlassian.com/x/8YdKLg) ordered by the display name.  *Note that you should allow for events without recipients to appear in responses.*  **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with a notification scheme for it to be returned.
            {
                "name": "get_notification_schemes",
                "table_name": "notification_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/notificationscheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "onlyDefault": "false",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [notification scheme](https://confluence.atlassian.com/x/8YdKLg), including the list of events and the recipients who will receive notifications for those events.  **[Permissions](#permissions) required:** Permission to access Jira, however, the user must have permission to administer at least one project associated with the notification scheme.
            {
                "name": "get_notification_scheme",
                "table_name": "notification_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/notificationscheme/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_notification_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) mapping of project that have notification scheme assigned. You can provide either one or multiple notification scheme IDs or project IDs to filter by. If you don't provide any, this will return a list of all mappings. Note that only company-managed (classic) projects are supported. This is because team-managed projects don't have a concept of a default notification scheme. The mappings are ordered by projectId.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_notification_scheme_to_project_mappings",
                "table_name": "notification_scheme_and_project_mapping_json_bean",
                "primary_key": "projectId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/notificationscheme/project",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "notificationSchemeId": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a [notification scheme](https://confluence.atlassian.com/x/8YdKLg) associated with the project.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
            {
                "name": "get_notification_scheme_for_project",
                "table_name": "notification_scheme_event",
                "endpoint": {
                    "data_selector": "notificationSchemeEvents",
                    "path": "/rest/api/3/project/{projectKeyOrId}/notificationscheme",
                    "params": {
                        "projectKeyOrId": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a page of field metadata for a specified project and issuetype id. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
            {
                "name": "get_create_issue_meta_issue_type_id",
                "table_name": "page_of_create_meta_issue_type_with_field",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/createmeta/{projectIdOrKey}/issuetypes/{issueTypeId}",
                    "params": {
                        "issueTypeId": {
                            "type": "resolve",
                            "resource": "get_create_issue_meta_issue_types",
                            "field": "id",
                        },
                        "projectIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all permissions, including:   *  global permissions.  *  project permissions.  *  global permissions added by plugins.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_permissions",
                "table_name": "permission",
                "endpoint": {
                    "data_selector": "permissions",
                    "path": "/rest/api/3/permissions",
                    "paginator": "auto",
                },
            },
            # Returns all permission grants for a permission scheme.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_permission_scheme_grants",
                "table_name": "permission_grant",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "permissions",
                    "path": "/rest/api/3/permissionscheme/{schemeId}/permission",
                    "params": {
                        "schemeId": {
                            "type": "resolve",
                            "resource": "get_all_permission_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a permission grant.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_permission_scheme_grant",
                "table_name": "permission_grant",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/permissionscheme/{schemeId}/permission/{permissionId}",
                    "params": {
                        "permissionId": {
                            "type": "resolve",
                            "resource": "get_permission_scheme_grants",
                            "field": "id",
                        },
                        "schemeId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
            {
                "name": "get_assigned_permission_scheme",
                "table_name": "permission_grant",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "permissions",
                    "path": "/rest/api/3/project/{projectKeyOrId}/permissionscheme",
                    "params": {
                        "projectKeyOrId": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all permission schemes.  ### About permission schemes and grants ###  A permission scheme is a collection of permission grants. A permission grant consists of a `holder` and a `permission`.  #### Holder object ####  The `holder` object contains information about the user or group being granted the permission. For example, the *Administer projects* permission is granted to a group named *Teams in space administrators*. In this case, the type is `"type": "group"`, and the parameter is the group name, `"parameter": "Teams in space administrators"` and the value is group ID, `"value": "ca85fac0-d974-40ca-a615-7af99c48d24f"`.  The `holder` object is defined by the following properties:   *  `type` Identifies the user or group (see the list of types below).  *  `parameter` As a group's name can change, use of `value` is recommended. The value of this property depends on the `type`. For example, if the `type` is a group, then you need to specify the group name.  *  `value` The value of this property depends on the `type`. If the `type` is a group, then you need to specify the group ID. For other `type` it has the same value as `parameter`  The following `types` are available. The expected values for `parameter` and `value` are given in parentheses (some types may not have a `parameter` or `value`):   *  `anyone` Grant for anonymous users.  *  `applicationRole` Grant for users with access to the specified application (application name, application name). See [Update product access settings](https://confluence.atlassian.com/x/3YxjL) for more information.  *  `assignee` Grant for the user currently assigned to an issue.  *  `group` Grant for the specified group (`parameter` : group name, `value` : group ID).  *  `groupCustomField` Grant for a user in the group selected in the specified custom field (`parameter` : custom field ID, `value` : custom field ID).  *  `projectLead` Grant for a project lead.  *  `projectRole` Grant for the specified project role (`parameter` :project role ID, `value` : project role ID).  *  `reporter` Grant for the user who reported the issue.  *  `sd.customer.portal.only` Jira Service Desk only. Grants customers permission to access the customer portal but not Jira. See [Customizing Jira Service Desk permissions](https://confluence.atlassian.com/x/24dKLg) for more information.  *  `user` Grant for the specified user (`parameter` : user ID - historically this was the userkey but that is deprecated and the account ID should be used, `value` : user ID).  *  `userCustomField` Grant for a user selected in the specified custom field (`parameter` : custom field ID, `value` : custom field ID).  #### Built-in permissions ####  The [built-in Jira permissions](https://confluence.atlassian.com/x/yodKLg) are listed below. Apps can also define custom permissions. See the [project permission](https://developer.atlassian.com/cloud/jira/platform/modules/project-permission/) and [global permission](https://developer.atlassian.com/cloud/jira/platform/modules/global-permission/) module documentation for more information.  **Project permissions**   *  `ADMINISTER_PROJECTS`  *  `BROWSE_PROJECTS`  *  `MANAGE_SPRINTS_PERMISSION` (Jira Software only)  *  `SERVICEDESK_AGENT` (Jira Service Desk only)  *  `VIEW_DEV_TOOLS` (Jira Software only)  *  `VIEW_READONLY_WORKFLOW`  **Issue permissions**   *  `ASSIGNABLE_USER`  *  `ASSIGN_ISSUES`  *  `CLOSE_ISSUES`  *  `CREATE_ISSUES`  *  `DELETE_ISSUES`  *  `EDIT_ISSUES`  *  `LINK_ISSUES`  *  `MODIFY_REPORTER`  *  `MOVE_ISSUES`  *  `RESOLVE_ISSUES`  *  `SCHEDULE_ISSUES`  *  `SET_ISSUE_SECURITY`  *  `TRANSITION_ISSUES`  **Voters and watchers permissions**   *  `MANAGE_WATCHERS`  *  `VIEW_VOTERS_AND_WATCHERS`  **Comments permissions**   *  `ADD_COMMENTS`  *  `DELETE_ALL_COMMENTS`  *  `DELETE_OWN_COMMENTS`  *  `EDIT_ALL_COMMENTS`  *  `EDIT_OWN_COMMENTS`  **Attachments permissions**   *  `CREATE_ATTACHMENTS`  *  `DELETE_ALL_ATTACHMENTS`  *  `DELETE_OWN_ATTACHMENTS`  **Time tracking permissions**   *  `DELETE_ALL_WORKLOGS`  *  `DELETE_OWN_WORKLOGS`  *  `EDIT_ALL_WORKLOGS`  *  `EDIT_OWN_WORKLOGS`  *  `WORK_ON_ISSUES`  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_all_permission_schemes",
                "table_name": "permission_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "permissionSchemes",
                    "path": "/rest/api/3/permissionscheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a permission scheme.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_permission_scheme",
                "table_name": "permission_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/permissionscheme/{schemeId}",
                    "params": {
                        "schemeId": {
                            "type": "resolve",
                            "resource": "get_all_permission_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of all issue priorities.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_priorities",
                "table_name": "priority",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/priority",
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of priorities. The list can contain all priorities or a subset determined by any combination of these criteria:   *  a list of priority IDs. Any invalid priority IDs are ignored.  *  a list of project IDs. Only priorities that are available in these projects will be returned. Any invalid project IDs are ignored.  *  whether the field configuration is a default. This returns priorities from company-managed (classic) projects only, as there is no concept of default priorities in team-managed projects.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "search_priorities",
                "table_name": "priority",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/priority/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                        # "priorityName": "OPTIONAL_CONFIG",
                        # "onlyDefault": "false",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns an issue priority.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_priority",
                "table_name": "priority",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/priority/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_priorities",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-api-3-project-search-get) that supports search and pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_all_projects",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "recent": "OPTIONAL_CONFIG",
                        # "properties": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of up to 20 projects recently viewed by the user that are still visible to the user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Projects are returned only where the user has one of:   *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_recent",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/recent",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "properties": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of projects visible to the user.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Projects are returned only where the user has one of:   *  *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "search_projects",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/project/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "orderBy": "key",
                        # "id": "OPTIONAL_CONFIG",
                        # "keys": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "typeKey": "OPTIONAL_CONFIG",
                        # "categoryId": "OPTIONAL_CONFIG",
                        # "action": "view",
                        # "expand": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "properties": "OPTIONAL_CONFIG",
                        # "propertyQuery": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [project details](https://confluence.atlassian.com/x/ahLpNw) for a project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                        # "properties": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all project categories.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_all_project_categories",
                "table_name": "project_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/projectCategory",
                    "paginator": "auto",
                },
            },
            # Returns a project category.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_project_category_by_id",
                "table_name": "project_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/projectCategory/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_project_categories",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a component.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for project containing the component.
            {
                "name": "get_component",
                "table_name": "project_component",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/component/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "find_components_for_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all components in a project. See the [Get project components paginated](#api-rest-api-3-project-projectIdOrKey-component-get) resource if you want to get a full list of components with pagination.  If your project uses Compass components, this API will return a paginated list of Compass components that are linked to issues in that project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_components",
                "table_name": "project_component",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/components",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "componentSource": "jira",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of projects associated with an issue type screen scheme.  Only company-managed projects associated with an issue type screen scheme are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_projects_for_issue_type_screen_scheme",
                "table_name": "project_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuetypescreenscheme/{issueTypeScreenSchemeId}/project",
                    "params": {
                        "issueTypeScreenSchemeId": {
                            "type": "resolve",
                            "resource": "get_issue_type_screen_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "query": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of features for a project.
            {
                "name": "get_features_for_project",
                "table_name": "project_feature",
                "endpoint": {
                    "data_selector": "features",
                    "path": "/rest/api/3/project/{projectIdOrKey}/features",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns details of projects, issue types within projects, and, when requested, the create screen fields for each issue type for the user. Use the information to populate the requests in [ Create issue](#api-rest-api-3-issue-post) and [Create issues](#api-rest-api-3-issue-bulk-post).  Deprecated, see [Create Issue Meta Endpoint Deprecation Notice](https://developer.atlassian.com/cloud/jira/platform/changelog/#CHANGE-1304).  The request can be restricted to specific projects or issue types using the query parameters. The response will contain information for the valid projects, issue types, or project and issue type combinations requested. Note that invalid project, issue type, or project and issue type combinations do not generate errors.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Create issues* [project permission](https://confluence.atlassian.com/x/yodKLg) in the requested projects.
            {
                "name": "get_create_issue_meta",
                "table_name": "project_issue_create_metadata",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "projects",
                    "path": "/rest/api/3/issue/createmeta",
                    "params": {
                        # the parameters below can optionally be configured
                        # "projectIds": "OPTIONAL_CONFIG",
                        # "projectKeys": "OPTIONAL_CONFIG",
                        # "issuetypeIds": "OPTIONAL_CONFIG",
                        # "issuetypeNames": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Get the issue type hierarchy for a next-gen project.  The issue type hierarchy for a project consists of:   *  *Epic* at level 1 (optional).  *  One or more issue types at level 0 such as *Story*, *Task*, or *Bug*. Where the issue type *Epic* is defined, these issue types are used to break down the content of an epic.  *  *Subtask* at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_hierarchy",
                "table_name": "project_issue_types_hierarchy_level",
                "primary_key": "entityId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "hierarchy",
                    "path": "/rest/api/3/project/{projectId}/hierarchy",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a project role's details and actors associated with the project. The list of actors is sorted by display name.  To check whether a user belongs to a role based on their group memberships, use [Get user](#api-rest-api-3-user-get) with the `groups` expand parameter selected. Then check whether the user keys and groups match with the actors returned for the project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_project_role",
                "table_name": "project_role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/role/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        "projectIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "excludeInactiveUsers": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a list of all project roles, complete with project role details and default actors.  ### About project roles ###  [Project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) are a flexible way to to associate users and groups with projects. In Jira Cloud, the list of project roles is shared globally with all projects, but each project can have a different set of actors associated with it (unlike groups, which have the same membership throughout all Jira applications).  Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and workflow conditions.  #### Members and actors ####  In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user associated with a project role.  Actors may be set as [default members](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/#Specifying-'default-members'-for-a-project-role) of the project role or set at the project level:   *  Default actors: Users and groups that are assigned to the project role for all newly created projects. The default actors can be removed at the project level later if desired.  *  Actors: Users and groups that are associated with a project role for a project, which may differ from the default actors. This enables you to assign a user to different roles in different projects.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_project_roles",
                "table_name": "project_role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/role",
                    "paginator": "auto",
                },
            },
            # Gets the project role details and the default actors associated with the role. The list of default actors is sorted by display name.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_project_role_by_id",
                "table_name": "project_role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/role/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_project_roles",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) and the details for each role. Note that the list of project roles is common to all projects.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_role_details",
                "table_name": "project_role_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/roledetails",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "currentMember": "false",
                        # "excludeConnectAddons": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all [project types](https://confluence.atlassian.com/x/Var1Nw), whether or not the instance has a valid license for each type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_all_project_types",
                "table_name": "project_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/type",
                    "paginator": "auto",
                },
            },
            # Returns all [project types](https://confluence.atlassian.com/x/Var1Nw) with a valid license.
            {
                "name": "get_all_accessible_project_types",
                "table_name": "project_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/type/accessible",
                    "paginator": "auto",
                },
            },
            # Returns a [project type](https://confluence.atlassian.com/x/Var1Nw).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_project_type_by_key",
                "table_name": "project_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/type/{projectTypeKey}",
                    "params": {
                        "projectTypeKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [project type](https://confluence.atlassian.com/x/Var1Nw) if it is accessible to the user.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_accessible_project_type_by_key",
                "table_name": "project_type",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/type/{projectTypeKey}/accessible",
                    "params": {
                        "projectTypeKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns data policies for the projects specified in the request.
            {
                "name": "get_policies",
                "table_name": "project_with_data_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "projectDataPolicies",
                    "path": "/rest/api/3/data-policy/project",
                    "params": {
                        # the parameters below can optionally be configured
                        # "ids": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the keys of all the properties of a comment.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_comment_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/comment/{commentId}/properties",
                    "params": {
                        "commentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the keys of all properties for a dashboard item.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the dashboard shared with them. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users, and is accessible to anonymous users when Jira\\u2019s anonymous access is permitted.
            {
                "name": "get_dashboard_item_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/dashboard/{dashboardId}/items/{itemId}/properties",
                    "params": {
                        "itemId": {
                            "type": "resolve",
                            "resource": "get_all_dashboards",
                            "field": "id",
                        },
                        "dashboardId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the URLs and keys of an issue's properties.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Property details are only returned where the user has:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_issue_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/properties",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the keys of all properties for a worklog.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_worklog_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/worklog/{worklogId}/properties",
                    "params": {
                        "worklogId": {
                            "type": "resolve",
                            "resource": "get_issue_worklog",
                            "field": "id",
                        },
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns all the [issue type property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys of the issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the property keys of any issue type.  *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the property keys of any issue types associated with the projects the user has permission to browse.
            {
                "name": "get_issue_type_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/issuetype/{issueTypeId}/properties",
                    "params": {
                        "issueTypeId": {
                            "type": "resolve",
                            "resource": "get_issue_all_types",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all [project property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-jira-entity-properties-a-jira-entity-properties) keys for the project.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/project/{projectIdOrKey}/properties",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the keys of all properties for a user.  Note: This operation does not access the [user properties](https://confluence.atlassian.com/x/8YxjL) created and maintained in Jira.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to access the property keys on any user.  *  Access to Jira, to access the calling user's property keys.
            {
                "name": "get_user_property_keys",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/api/3/user/properties",
                    "params": {
                        # the parameters below can optionally be configured
                        # "accountId": "OPTIONAL_CONFIG",
                        # "userKey": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets all the properties of an app.  **[Permissions](#permissions) required:** Only a Connect app whose key matches `addonKey` can make this request. Additionally, Forge apps can access Connect app properties (stored against the same `app.connect.key`).
            {
                "name": "addon_properties_resource_get_addon_properties_get",
                "table_name": "property_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/rest/atlassian-connect/1/addons/{addonKey}/properties",
                    "params": {
                        "addonKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_remote_issue_links",
                "table_name": "remote_issue_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/remotelink",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "globalId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a remote issue link for an issue.  This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_remote_issue_link_by_id",
                "table_name": "remote_issue_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/remotelink/{linkId}",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "linkId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all issue resolution values.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_resolutions",
                "table_name": "resolution",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/resolution",
                    "paginator": "auto",
                },
            },
            # Returns an issue resolution value.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_resolution",
                "table_name": "resolution",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/resolution/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_resolutions",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of resolutions. The list can contain all resolutions or a subset determined by any combination of these criteria:   *  a list of resolutions IDs.  *  whether the field configuration is a default. This returns resolutions from company-managed (classic) projects only, as there is no concept of default resolutions in team-managed projects.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "search_resolutions",
                "table_name": "resolution_json_bean",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/resolution/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "onlyDefault": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of [project roles](https://support.atlassian.com/jira-cloud-administration/docs/manage-project-roles/) for the project returning the name and self URL for each role.  Note that all project roles are shared with all projects in Jira Cloud. See [Get all project roles](#api-rest-api-3-role-get) for more information.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_project_roles",
                "table_name": "role",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/role",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [default actors](#api-rest-api-3-resolution-get) for the project role.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_project_role_actors_for_role",
                "table_name": "role_actor",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actors",
                    "path": "/rest/api/3/role/{id}/actors",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_project_roles",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_screens",
                "table_name": "screen",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/screens",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "100",
                        # "id": "OPTIONAL_CONFIG",
                        # "queryString": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of screen schemes.  Only screen schemes used in classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_screen_schemes",
                "table_name": "screen_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/screenscheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "25",
                        # "id": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                        # "queryString": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of the screens a field is used in.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_screens_for_field",
                "table_name": "screen_with_tab",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/field/{fieldId}/screens",
                    "params": {
                        "fieldId": {
                            "type": "resolve",
                            "resource": "get_fields",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "100",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the fields that can be added to a tab on a screen.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_available_screen_fields",
                "table_name": "screenable_field",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/screens/{screenId}/availableFields",
                    "params": {
                        "screenId": {
                            "type": "resolve",
                            "resource": "get_screens",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all fields for a screen tab.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.
            {
                "name": "get_all_screen_tab_fields",
                "table_name": "screenable_field",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/screens/{screenId}/tabs/{tabId}/fields",
                    "params": {
                        "tabId": {
                            "type": "resolve",
                            "resource": "get_all_screen_tabs",
                            "field": "id",
                        },
                        "screenId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "projectKey": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of tabs for a screen.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) when the project key is specified, providing that the screen is associated with the project through a Screen Scheme and Issue Type Screen Scheme.
            {
                "name": "get_all_screen_tabs",
                "table_name": "screenable_tab",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/screens/{screenId}/tabs",
                    "params": {
                        "screenId": {
                            "type": "resolve",
                            "resource": "get_screens",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "projectKey": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue security levels.  Only issue security levels in the context of classic projects are returned.  Filtering using IDs is inclusive: if you specify both security scheme IDs and level IDs, the result will include both specified issue security levels and all issue security levels from the specified schemes.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_security_levels",
                "table_name": "security_level",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuesecurityschemes/level",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "schemeId": "OPTIONAL_CONFIG",
                        # "onlyDefault": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the [issue security scheme](https://confluence.atlassian.com/x/J4lKLg) associated with the project.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or the *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg).
            {
                "name": "get_project_issue_security_scheme",
                "table_name": "security_level",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "levels",
                    "path": "/rest/api/3/project/{projectKeyOrId}/issuesecuritylevelscheme",
                    "params": {
                        "projectKeyOrId": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all [issue security](https://confluence.atlassian.com/x/J4lKLg) levels for the project that the user has access to.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project, however, issue security levels are only returned for authenticated user with *Set Issue Security* [global permission](https://confluence.atlassian.com/x/x4dKLg) for the project.
            {
                "name": "get_security_levels_for_project",
                "table_name": "security_level",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "levels",
                    "path": "/rest/api/3/project/{projectKeyOrId}/securitylevel",
                    "params": {
                        "projectKeyOrId": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns details of an issue security level.  Use [Get issue security scheme](#api-rest-api-3-issuesecurityschemes-id-get) to obtain the IDs of issue security levels associated with the issue security scheme.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_issue_security_level",
                "table_name": "security_level",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/securitylevel/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue security level members.  Only issue security level members in the context of classic projects are returned.  Filtering using parameters is inclusive: if you specify both security scheme IDs and level IDs, the result will include all issue security level members from the specified schemes and levels.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_security_level_members",
                "table_name": "security_level_member",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuesecurityschemes/level/member",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "schemeId": "OPTIONAL_CONFIG",
                        # "levelId": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all [issue security schemes](https://confluence.atlassian.com/x/J4lKLg).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_issue_security_schemes",
                "table_name": "security_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "issueSecuritySchemes",
                    "path": "/rest/api/3/issuesecurityschemes",
                    "paginator": "auto",
                },
            },
            # Returns an issue security scheme along with its security levels.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project that uses the requested issue security scheme.
            {
                "name": "get_issue_security_scheme",
                "table_name": "security_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issuesecurityschemes/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_issue_security_schemes",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of issue security schemes.   If you specify the project ID parameter, the result will contain issue security schemes and related project IDs you filter by. Use \{@link IssueSecuritySchemeResource\#searchProjectsUsingSecuritySchemes(String, String, Set, Set)\} to obtain all projects related to scheme.  Only issue security schemes in the context of classic projects are returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "search_security_schemes",
                "table_name": "security_scheme_with_projects",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/issuesecurityschemes/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "id": "OPTIONAL_CONFIG",
                        # "projectId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the attributes of given service registries.  **[Permissions](#permissions) required:** Only Connect apps can make this request and the servicesIds belong to the tenant you are requesting
            {
                "name": "service_registry_resource_services_get",
                "table_name": "service_registry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/atlassian-connect/1/service-registry",
                    "params": {
                        "serviceIds": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, share permissions are only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.
            {
                "name": "get_share_permissions",
                "table_name": "share_permission",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/{id}/permission",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None, however, a share permission is only returned for:   *  filters owned by the user.  *  filters shared with a group that the user is a member of.  *  filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for.  *  filters shared with a public project.  *  filters shared with the public.
            {
                "name": "get_share_permission",
                "table_name": "share_permission",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/filter/{id}/permission/{permissionId}",
                    "params": {
                        "permissionId": {
                            "type": "resolve",
                            "resource": "get_share_permissions",
                            "field": "id",
                        },
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all status categories.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_status_categories",
                "table_name": "status_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/statuscategory",
                    "paginator": "auto",
                },
            },
            # Returns a status category. Status categories provided a mechanism for categorizing [statuses](#api-rest-api-3-status-idOrName-get).  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "get_status_category",
                "table_name": "status_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/statuscategory/{idOrKey}",
                    "params": {
                        "idOrKey": {
                            "type": "resolve",
                            "resource": "get_status_categories",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all statuses associated with active workflows.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_statuses",
                "table_name": "status_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/status",
                    "paginator": "auto",
                },
            },
            # Returns a status. The status must be associated with an active workflow to be returned.  If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable.  This operation can be accessed anonymously.  [Permissions](#permissions) required: None.
            {
                "name": "get_status",
                "table_name": "status_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/status/{idOrName}",
                    "params": {
                        "idOrName": {
                            "type": "resolve",
                            "resource": "get_statuses",
                            "field": "id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns the default project or issue type avatar image.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_avatar_image_by_type",
                "table_name": "streaming_response_body",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/universal_avatar/view/type/{type}",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "size": "OPTIONAL_CONFIG",
                        # "format": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a project or issue type avatar image by ID.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  For system avatars, none.  *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.  *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
            {
                "name": "get_avatar_image_by_id",
                "table_name": "streaming_response_body",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/universal_avatar/view/type/{type}/avatar/{id}",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "size": "OPTIONAL_CONFIG",
                        # "format": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the avatar image for a project or issue type.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  For system avatars, none.  *  For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to.  *  For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.
            {
                "name": "get_avatar_image_by_owner",
                "table_name": "streaming_response_body",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/universal_avatar/view/type/{type}/owner/{entityId}",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "entityId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "size": "OPTIONAL_CONFIG",
                        # "format": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the list of tabs for a bulk of screens.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_bulk_screen_tabs",
                "table_name": "tab",
                "endpoint": {
                    "path": "/rest/api/3/screens/tabs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "screenId": "OPTIONAL_CONFIG",
                        # "tabId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResult": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the status of a [long-running asynchronous task](#async).  When a task has finished, this operation returns the JSON blob applicable to the task. See the documentation of the operation that created the task for details. Task details are not permanently retained. As of September 2019, details are retained for 14 days although this period may change without notice.  **Deprecation notice:** The required OAuth 2.0 scopes will be updated on June 15, 2024.   *  `read:jira-work`  **[Permissions](#permissions) required:** either of:   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  Creator of the task.
            {
                "name": "get_task",
                "table_name": "task_progress_bean_object",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/task/{taskId}",
                    "params": {
                        "taskId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the thumbnail of an attachment.  To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-id-get).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** For the issue containing the attachment:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.
            {
                "name": "get_attachment_thumbnail",
                "table_name": "thumbnail",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/attachment/thumbnail/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "redirect": "true",
                        # "fallbackToDefault": "true",
                        # "width": "OPTIONAL_CONFIG",
                        # "height": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_shared_time_tracking_configuration",
                "table_name": "time_tracking_configuration",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/configuration/timetracking/options",
                    "paginator": "auto",
                },
            },
            # Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_selected_time_tracking_implementation",
                "table_name": "time_tracking_provider",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/configuration/timetracking",
                    "paginator": "auto",
                },
            },
            # Returns all time tracking providers. By default, Jira only has one time tracking provider: *JIRA provided time tracking*. However, you can install other time tracking providers via apps from the Atlassian Marketplace. For more information on time tracking providers, see the documentation for the [ Time Tracking Provider](https://developer.atlassian.com/cloud/jira/platform/modules/time-tracking-provider/) module.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_available_time_tracking_implementations",
                "table_name": "time_tracking_provider",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/configuration/timetracking/list",
                    "paginator": "auto",
                },
            },
            # Gets UI modifications. UI modifications can only be retrieved by Forge apps.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_ui_modifications",
                "table_name": "ui_modification_details",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/uiModifications",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a user's email address. This API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).
            {
                "name": "get_user_email",
                "table_name": "unrestricted_user_email",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/email",
                    "params": {
                        "accountId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a user's email address. This API is only available to apps approved by Atlassian, according to these [guidelines](https://community.developer.atlassian.com/t/guidelines-for-requesting-access-to-email-address/27603).
            {
                "name": "get_user_email_bulk",
                "table_name": "unrestricted_user_email",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/email/bulk",
                    "params": {
                        "accountId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns details about the votes on an issue.  This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  Note that users with the necessary permissions for this operation but without the *View voters and watchers* project permissions are not returned details in the `voters` field.
            {
                "name": "get_votes",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "voters",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/votes",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string.  This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned issues in the projects. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned issues in the projects, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.
            {
                "name": "find_bulk_assignable_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/assignable/multiProjectSearch",
                    "params": {
                        "projectKeys": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to:   *  a new issue, by providing the `projectKeyOrId`.  *  an updated issue, by providing the `issueKey`.  *  to an issue during a transition (workflow action), by providing the `issueKey` and the transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-issueIdOrKey-get).  In all these cases, you can pass an account ID to determine if a user can be assigned to an issue. The user is returned in the response if they can be assigned to the issue or issue transition.  This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned the issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Assign issues* [project permission](https://confluence.atlassian.com/x/yodKLg)
            {
                "name": "find_assignable_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/assignable/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "sessionId": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "project": "OPTIONAL_CONFIG",
                        # "issueKey": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "actionDescriptorId": "OPTIONAL_CONFIG",
                        # "recommend": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of the users specified by one or more account IDs.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "bulk_get_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/user/bulk",
                    "params": {
                        "accountId": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "10",
                        # "username": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users who fulfill these criteria:   *  their user attributes match a search string.  *  they have a set of permissions for a project or issue.  If no search string is provided, a list of all users with the permissions is returned.  This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission for the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project.  *  *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.
            {
                "name": "find_users_with_all_permissions",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/permission/search",
                    "params": {
                        "permissions": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "issueKey": "OPTIONAL_CONFIG",
                        # "projectKey": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of active users that match the search string and property.  This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  This operation can be accessed anonymously.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without the required permission return empty search results.
            {
                "name": "find_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "property": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Finds users with a structured query and returns a [paginated](#pagination) list of user details.  This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).  The query statements are:   *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project *PROJ*.  *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*.  *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*.  *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*.  *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.  *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*.  *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*.  *  `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value.  The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example:  `is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`
            {
                "name": "find_users_by_query",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/user/search/query",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users who fulfill these criteria:   *  their user attributes match a search string.  *  they have permission to browse issues.  Use this resource to find users who can browse:   *  an issue, by providing the `issueKey`.  *  any issue in a project, by providing the `projectKey`.  This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission to browse issues. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission to browse issues, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return empty search results.
            {
                "name": "find_users_with_browse_permission",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/viewissue/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "username": "OPTIONAL_CONFIG",
                        # "accountId": "OPTIONAL_CONFIG",
                        # "issueKey": "OPTIONAL_CONFIG",
                        # "projectKey": "OPTIONAL_CONFIG",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_users_default",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all users, including active users, inactive users and previously deleted users that have an Atlassian account.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/users/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # This operation is deprecated, use [`group/member`](#api-rest-api-3-group-member-get).  Returns all users in a group.  **[Permissions](#permissions) required:** either of:   *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_group",
                "table_name": "user_details",
                "endpoint": {
                    "data_selector": "users.items",
                    "path": "/rest/api/3/group",
                    "params": {
                        # the parameters below can optionally be configured
                        # "groupname": "OPTIONAL_CONFIG",
                        # "groupId": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all users in a group.  Note that users are ordered by username, however the username is not returned in the results due to privacy reasons.  **[Permissions](#permissions) required:** either of:   *  *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).  *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_users_from_group",
                "table_name": "user_details",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/group/member",
                    "params": {
                        # the parameters below can optionally be configured
                        # "groupname": "OPTIONAL_CONFIG",
                        # "groupId": "OPTIONAL_CONFIG",
                        # "includeInactiveUsers": "false",
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the watchers for an issue.  This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  To see details of users on the watchlist other than themselves, *View voters and watchers* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.
            {
                "name": "get_issue_watchers",
                "table_name": "user_details",
                "endpoint": {
                    "data_selector": "watchers",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/watchers",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Finds users with a structured query and returns a [paginated](#pagination) list of user keys.  This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).  The query statements are:   *  `is assignee of PROJ` Returns the users that are assignees of at least one issue in project *PROJ*.  *  `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*.  *  `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*.  *  `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*.  *  `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*.  *  `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*.  *  `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*.  *  `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value.  The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example:  `is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`
            {
                "name": "find_user_keys_by_query",
                "table_name": "user_key",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/user/search/query/key",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResult": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the account IDs for the users specified in the `key` or `username` parameters. Note that multiple `key` or `username` parameters can be specified.  **[Permissions](#permissions) required:** Permission to access Jira.
            {
                "name": "bulk_get_users_migration",
                "table_name": "user_migration_bean",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/user/bulk/migration",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "10",
                        # "username": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of users whose attributes match the query term. The returned object includes the `html` field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results.  This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and then returns only the users from that range that match the query term. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the query term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code.  Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return search results for an exact name match only.
            {
                "name": "find_users_for_picker",
                "table_name": "user_picker_user",
                "endpoint": {
                    "data_selector": "users",
                    "path": "/rest/api/3/user/picker",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "50",
                        # "showAvatar": "false",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "excludeAccountIds": "OPTIONAL_CONFIG",
                        # "avatarSize": "OPTIONAL_CONFIG",
                        # "excludeConnectUsers": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Validates a project key and, if the key is invalid or in use, generates a valid random string for the project key.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_valid_project_key",
                "table_name": "valid_project_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/projectvalidate/validProjectKey",
                    "params": {
                        # the parameters below can optionally be configured
                        # "key": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Checks that a project name isn't in use. If the name isn't in use, the passed string is returned. If the name is in use, this operation attempts to generate a valid project name based on the one supplied, usually by adding a sequence number. If a valid project name cannot be generated, a 404 response is returned.  **[Permissions](#permissions) required:** None.
            {
                "name": "get_valid_project_name",
                "table_name": "valid_project_name",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/projectvalidate/validProjectName",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all versions in a project. See the [Get project versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full list of versions without pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_versions_paginated",
                "table_name": "version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/project/{projectIdOrKey}/version",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a project with pagination.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.
            {
                "name": "get_project_versions",
                "table_name": "version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/project/{projectIdOrKey}/versions",
                    "params": {
                        "projectIdOrKey": {
                            "type": "resolve",
                            "resource": "get_all_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a project version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.
            {
                "name": "get_version",
                "table_name": "version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/version/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns related work items for the given version id.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.
            {
                "name": "get_related_work",
                "table_name": "version_related_work",
                "primary_key": "relatedWorkId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/version/{id}/relatedwork",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns counts of the issues and unresolved issues for the project version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
            {
                "name": "get_version_unresolved_issues",
                "table_name": "version_unresolved_issues_count",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/version/{id}/unresolvedIssueCount",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the following counts for a version:   *  Number of issues where the `fixVersion` is set to the version.  *  Number of issues where the `affectedVersion` is set to the version.  *  Number of issues where a version custom field is set to the version.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.
            {
                "name": "get_version_related_issues",
                "table_name": "version_usage_in_custom_field",
                "endpoint": {
                    "data_selector": "customFieldUsage",
                    "path": "/rest/api/3/version/{id}/relatedIssueCounts",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of the webhooks registered by the calling app.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth 2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this operation.
            {
                "name": "get_dynamic_webhooks_for_app",
                "table_name": "webhook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/webhook",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "100",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of published classic workflows. When workflow names are specified, details of those workflows are returned. Otherwise, all published classic workflows are returned.  This operation does not return next-gen workflows.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflows_paginated",
                "table_name": "workflow",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/workflow/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                        # "workflowName": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                        # "queryString": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "isActive": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the workflow-issue type mappings for a workflow scheme's draft.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_draft_workflow",
                "table_name": "workflow",
                "endpoint": {
                    "data_selector": "issueTypes",
                    "path": "/rest/api/3/workflowscheme/{id}/draft/workflow",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "workflowName": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the workflow-issue type mappings for a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow",
                "table_name": "workflow",
                "endpoint": {
                    "data_selector": "issueTypes",
                    "path": "/rest/api/3/workflowscheme/{id}/workflow",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_workflow_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "workflowName": "OPTIONAL_CONFIG",
                        # "returnDraftIfExists": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of all workflow schemes, not including draft workflow schemes.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_all_workflow_schemes",
                "table_name": "workflow_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/workflowscheme",
                    "params": {
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "50",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a workflow scheme.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow_scheme",
                "table_name": "workflow_scheme",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflowscheme/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_all_workflow_schemes",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "returnDraftIfExists": "false",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of the workflow schemes associated with a list of projects. Each returned workflow scheme includes a list of the requested projects associated with it. Any team-managed or non-existent projects in the request are ignored and no errors are returned.  If the project is associated with the `Default Workflow Scheme` no ID is returned. This is because the way the `Default Workflow Scheme` is stored means it has no ID.  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow_scheme_project_associations",
                "table_name": "workflow_scheme_associations",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/workflowscheme/project",
                    "params": {
                        "projectId": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns the properties on a workflow transition. Transition properties are used to change the behavior of a transition. For more information, see [Transition properties](https://confluence.atlassian.com/x/zIhKLg#Advancedworkflowconfiguration-transitionproperties) and [Workflow properties](https://confluence.atlassian.com/x/JYlKLg).  **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).
            {
                "name": "get_workflow_transition_properties",
                "table_name": "workflow_transition_property",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/workflow/transitions/{transitionId}/properties",
                    "params": {
                        "transitionId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "workflowName": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "includeReservedKeys": "false",
                        # "key": "OPTIONAL_CONFIG",
                        # "workflowMode": "live",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a [paginated](#pagination) list of workflows with transition rules. The workflows can be filtered to return only those containing workflow transition rules:   *  of one or more transition rule types, such as [workflow post functions](https://developer.atlassian.com/cloud/jira/platform/modules/workflow-post-function/).  *  matching one or more transition rule keys.  Only workflows containing transition rules created by the calling [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) app are returned.  Due to server-side optimizations, workflows with an empty list of rules may be returned; these workflows can be ignored.  **[Permissions](#permissions) required:** Only [Connect](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) or [Forge](https://developer.atlassian.com/cloud/jira/platform/index/#forge-apps) apps can use this operation.
            {
                "name": "get_workflow_transition_rule_configurations",
                "table_name": "workflow_transition_rules",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/rest/api/3/workflow/rule/config",
                    "params": {
                        "types": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "10",
                        # "keys": "OPTIONAL_CONFIG",
                        # "workflowNames": "OPTIONAL_CONFIG",
                        # "withTags": "OPTIONAL_CONFIG",
                        # "draft": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or after a date and time.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** Workloads are only returned where the user has:   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_issue_worklog",
                "table_name": "worklog",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "worklogs",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/worklog",
                    "params": {
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "startAt": "0",
                        # "maxResults": "5000",
                        # "startedAfter": "OPTIONAL_CONFIG",
                        # "startedBefore": "OPTIONAL_CONFIG",
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a worklog.  Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM).  This operation can be accessed anonymously.  **[Permissions](#permissions) required:**   *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.  *  If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.  *  If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.
            {
                "name": "get_worklog",
                "table_name": "worklog",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/issue/{issueIdOrKey}/worklog/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_issue_worklog",
                            "field": "id",
                        },
                        "issueIdOrKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "expand": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns data policy for the workspace.
            {
                "name": "get_policy",
                "table_name": "workspace_data_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rest/api/3/data-policy",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
