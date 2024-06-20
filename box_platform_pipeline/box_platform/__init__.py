from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="box_platform_source", max_table_nesting=2)
def box_platform_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "offset",
                "limit": 1000,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "total_count",
            },
        },
        "resources": [
            # Authorize a user by sending them through the [Box](https://box.com) website and request their permission to act on their behalf.  This is the first step when authenticating a user using OAuth 2.0. To request a user's authorization to use the Box APIs on their behalf you will need to send a user to the URL with this format.
            {
                "name": "get_authorize",
                "table_name": "authorize",
                "endpoint": {
                    "path": "/authorize",
                    "params": {
                        "response_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "client_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "redirect_uri": "OPTIONAL_CONFIG",
                        # "state": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves an image of a the user's avatar.
            {
                "name": "get_users_id_avatar",
                "table_name": "avatar",
                "endpoint": {
                    "path": "/users/{user_id}/avatar",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List the Box Skills metadata cards that are attached to a file.
            {
                "name": "get_files_id_metadata_global_box_skills_cards",
                "table_name": "box_skills_card",
                "endpoint": {
                    "data_selector": "cards",
                    "path": "/files/{file_id}/metadata/global/boxSkillsCards",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the contents of a file in binary format.
            {
                "name": "get_files_id_content",
                "table_name": "client_error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{file_id}/content",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "version": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the classification metadata instance that has been applied to a file.  This API can also be called by including the enterprise ID in the URL explicitly, for example `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.
            {
                "name": "get_files_id_metadata_enterprise_security_classification_6vm_vochw_u_wo",
                "table_name": "client_error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the instance of a metadata template that has been applied to a file.
            {
                "name": "get_files_id_metadata_id_id",
                "table_name": "client_error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{file_id}/metadata/{scope}/{template_key}",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "scope": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "template_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the classification metadata instance that has been applied to a folder.  This API can also be called by including the enterprise ID in the URL explicitly, for example `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.
            {
                "name": "get_folders_id_metadata_enterprise_security_classification_6vm_vochw_u_wo",
                "table_name": "client_error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the instance of a metadata template that has been applied to a folder. This can not be used on the root folder with ID `0`.
            {
                "name": "get_folders_id_metadata_id_id",
                "table_name": "client_error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/folders/{folder_id}/metadata/{scope}/{template_key}",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "scope": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "template_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all pending collaboration invites for this user.
            {
                "name": "get_collaborations",
                "table_name": "collaboration",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/collaborations",
                    "params": {
                        "status": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a single collaboration.
            {
                "name": "get_collaborations_id",
                "table_name": "collaboration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/collaborations/{collaboration_id}",
                    "params": {
                        "collaboration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of pending and active collaborations for a file. This returns all the users that have access to the file or have been invited to the file.
            {
                "name": "get_files_id_collaborations",
                "table_name": "collaboration",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/files/{file_id}/collaborations",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of pending and active collaborations for a folder. This returns all the users that have access to the folder or have been invited to the folder.
            {
                "name": "get_folders_id_collaborations",
                "table_name": "collaboration",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/folders/{folder_id}/collaborations",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves all the collaborations for a group. The user must have admin permissions to inspect enterprise's groups.  Each collaboration object has details on which files or folders the group has access to and with what role.
            {
                "name": "get_groups_id_collaborations",
                "table_name": "collaboration",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/groups/{group_id}/collaborations",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the list domains that have been deemed safe to create collaborations for within the current enterprise.
            {
                "name": "get_collaboration_whitelist_entries",
                "table_name": "collaboration_allowlist_entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/collaboration_whitelist_entries",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a domain that has been deemed safe to create collaborations for within the current enterprise.
            {
                "name": "get_collaboration_whitelist_entries_id",
                "table_name": "collaboration_allowlist_entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/collaboration_whitelist_entries/{collaboration_whitelist_entry_id}",
                    "params": {
                        "collaboration_whitelist_entry_id": {
                            "type": "resolve",
                            "resource": "get_collaboration_whitelist_entries",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of users who have been exempt from the collaboration domain restrictions.
            {
                "name": "get_collaboration_whitelist_exempt_targets",
                "table_name": "collaboration_allowlist_exempt_target",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/collaboration_whitelist_exempt_targets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a users who has been exempt from the collaboration domain restrictions.
            {
                "name": "get_collaboration_whitelist_exempt_targets_id",
                "table_name": "collaboration_allowlist_exempt_target",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}",
                    "params": {
                        "collaboration_whitelist_exempt_target_id": {
                            "type": "resolve",
                            "resource": "get_collaboration_whitelist_exempt_targets",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves all collections for a given user.  Currently, only the `favorites` collection is supported.
            {
                "name": "get_collections",
                "table_name": "collection",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/collections",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of comments for a file.
            {
                "name": "get_files_id_comments",
                "table_name": "comment",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/files/{file_id}/comments",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the message and metadata for a specific comment, as well as information on the user who created the comment.
            {
                "name": "get_comments_id",
                "table_name": "comment_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/comments/{comment_id}",
                    "params": {
                        "comment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the contents of a `zip` archive in binary format. This URL does not require any form of authentication and could be used in a user's browser to download the archive to a user's device.  By default, this URL is only valid for a few seconds from the creation of the request for this archive. Once a download has started it can not be stopped and resumed, instead a new request for a zip archive would need to be created.  The URL of this endpoint should not be considered as fixed. Instead, use the [Create zip download](e://post_zip_downloads) API to request to create a `zip` archive, and then follow the `download_url` field in the response to this endpoint.
            {
                "name": "get_zip_downloads_id_content",
                "table_name": "content",
                "endpoint": {
                    "path": "/zip_downloads/{zip_download_id}/content",
                    "params": {
                        "zip_download_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves information about an individual device pin.
            {
                "name": "get_device_pinners_id",
                "table_name": "device_pinner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/device_pinners/{device_pinner_id}",
                    "params": {
                        "device_pinner_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all the device pins within an enterprise.  The user must have admin privileges, and the application needs the "manage enterprise" scope to make this call.
            {
                "name": "get_enterprises_id_device_pinners",
                "table_name": "device_pinner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/enterprises/{enterprise_id}/device_pinners",
                    "params": {
                        "enterprise_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves all email aliases for a user. The collection does not include the primary login for the user.
            {
                "name": "get_users_id_email_aliases",
                "table_name": "email_alias",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/users/{user_id}/email_aliases",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns up to a year of past events for a given user or for the entire enterprise.  By default this returns events for the authenticated user. To retrieve events for the entire enterprise, set the `stream_type` to `admin_logs_streaming` for live monitoring of new events, or `admin_logs` for querying across historical events. The user making the API call will need to have admin privileges, and the application will need to have the scope `manage enterprise properties` checked.
            {
                "name": "get_events",
                "table_name": "event",
                "primary_key": "event_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "stream_type": "all",
                        # "stream_position": "OPTIONAL_CONFIG",
                        # "limit": "100",
                        # "event_type": "OPTIONAL_CONFIG",
                        # "created_after": "OPTIONAL_CONFIG",
                        # "created_before": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the details about a file.
            {
                "name": "get_files_id",
                "table_name": "file_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{file_id}",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets the information for a shared link on a file.
            {
                "name": "get_files_idget_shared_link",
                "table_name": "file_idget_shared_link",
                "endpoint": {
                    "data_selector": "allowed_invitee_roles",
                    "path": "/files/{file_id}#get_shared_link",
                    "params": {
                        "fields": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Returns a list of file versions under retention for a retention policy assignment.
            {
                "name": "get_retention_policy_assignments_id_file_versions_under_retention",
                "table_name": "file_mini",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/retention_policy_assignments/{retention_policy_assignment_id}/file_versions_under_retention",
                    "params": {
                        "retention_policy_assignment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of files under retention for a retention policy assignment.
            {
                "name": "get_retention_policy_assignments_id_files_under_retention",
                "table_name": "file_mini",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention",
                    "params": {
                        "retention_policy_assignment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the information about a file request.
            {
                "name": "get_file_requests_id",
                "table_name": "file_request",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/file_requests/{file_request_id}",
                    "params": {
                        "file_request_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a specific version of a file.  Versions are only tracked for Box users with premium accounts.
            {
                "name": "get_files_id_versions_id",
                "table_name": "file_version_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{file_id}/versions/{file_version_id}",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "file_version_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a list of file versions on legal hold for a legal hold assignment.  Due to ongoing re-architecture efforts this API might not return all file versions for this policy ID.  Instead, this API will only return file versions held in the legacy architecture. Two new endpoints will available to request any file versions held in the new architecture.  For file versions held in the new architecture, the `GET /legal_hold_policy_assignments/:id/file_versions_on_hold` API can be used to return all past file versions available for this policy assignment, and the `GET /legal_hold_policy_assignments/:id/files_on_hold` API can be used to return any current (latest) versions of a file under legal hold.  The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to find a list of policy assignments for a given policy ID.  Once the re-architecture is completed this API will be deprecated.
            {
                "name": "get_file_version_legal_holds",
                "table_name": "file_version_legal_hold",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/file_version_legal_holds",
                    "params": {
                        "policy_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about the legal hold policies assigned to a file version.
            {
                "name": "get_file_version_legal_holds_id",
                "table_name": "file_version_legal_hold",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/file_version_legal_holds/{file_version_legal_hold_id}",
                    "params": {
                        "file_version_legal_hold_id": {
                            "type": "resolve",
                            "resource": "get_file_version_legal_holds",
                            "field": "id",
                        },
                    },
                },
            },
            # Get a list of previous file versions for a legal hold assignment.  In some cases you may only need the latest file versions instead. In these cases, use the `GET  /legal_hold_policy_assignments/:id/files_on_hold` API instead to return any current (latest) versions of a file for this legal hold policy assignment.  Due to ongoing re-architecture efforts this API might not return all files held for this policy ID. Instead, this API will only return past file versions held in the newly developed architecture. The `GET /file_version_legal_holds` API can be used to fetch current and past versions of files held within the legacy architecture.  The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to find a list of policy assignments for a given policy ID.
            {
                "name": "get_legal_hold_policy_assignments_id_file_versions_on_hold",
                "table_name": "file_version_legal_hold",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/file_versions_on_hold",
                    "params": {
                        "legal_hold_policy_assignment_id": {
                            "type": "resolve",
                            "resource": "get_legal_hold_policy_assignments",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a list of current file versions for a legal hold assignment.  In some cases you may want to get previous file versions instead. In these cases, use the `GET  /legal_hold_policy_assignments/:id/file_versions_on_hold` API instead to return any previous versions of a file for this legal hold policy assignment.  Due to ongoing re-architecture efforts this API might not return all file versions held for this policy ID. Instead, this API will only return the latest file version held in the newly developed architecture. The `GET /file_version_legal_holds` API can be used to fetch current and past versions of files held within the legacy architecture.  The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to find a list of policy assignments for a given policy ID.
            {
                "name": "get_legal_hold_policy_assignments_id_files_on_hold",
                "table_name": "file_version_legal_hold",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold",
                    "params": {
                        "legal_hold_policy_assignment_id": {
                            "type": "resolve",
                            "resource": "get_legal_hold_policy_assignments",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves all file version retentions for the given enterprise.
            {
                "name": "get_file_version_retentions",
                "table_name": "file_version_retention",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/file_version_retentions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "file_id": "OPTIONAL_CONFIG",
                        # "file_version_id": "OPTIONAL_CONFIG",
                        # "policy_id": "OPTIONAL_CONFIG",
                        # "disposition_action": "OPTIONAL_CONFIG",
                        # "disposition_before": "OPTIONAL_CONFIG",
                        # "disposition_after": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns information about a file version retention.
            {
                "name": "get_file_version_retentions_id",
                "table_name": "file_version_retention",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/file_version_retentions/{file_version_retention_id}",
                    "params": {
                        "file_version_retention_id": {
                            "type": "resolve",
                            "resource": "get_file_version_retentions",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves details for a folder, including the first 100 entries in the folder.  To fetch more items within the folder, please use the [Get items in a folder](#get-folders-id-items) endpoint.
            {
                "name": "get_folders_id",
                "table_name": "folder_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/folders/{folder_id}",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets the information for a shared link on a folder.
            {
                "name": "get_folders_idget_shared_link",
                "table_name": "folder_idget_shared_link",
                "endpoint": {
                    "data_selector": "allowed_invitee_roles",
                    "path": "/folders/{folder_id}#get_shared_link",
                    "params": {
                        "fields": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Retrieves folder lock details for a given folder.  You must be authenticated as the owner or co-owner of the folder to use this endpoint.
            {
                "name": "get_folder_locks",
                "table_name": "folder_lock",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/folder_locks",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Returns the web link represented by a shared link.  A shared web link can be represented by a shared link, which can originate within the current enterprise or within another.  This endpoint allows an application to retrieve information about a shared web link when only given a shared link.
            {
                "name": "get_shared_itemsweb_links",
                "table_name": "folder_mini",
                "endpoint": {
                    "data_selector": "path_collection.entries",
                    "path": "/shared_items#web_links",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets the information for a shared link on a web link.
            {
                "name": "get_web_links_idget_shared_link",
                "table_name": "folder_mini",
                "endpoint": {
                    "data_selector": "path_collection.entries",
                    "path": "/web_links/{web_link_id}#get_shared_link",
                    "params": {
                        "fields": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Retrieves all of the groups for a given enterprise. The user must have admin permissions to inspect enterprise's groups.
            {
                "name": "get_groups",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/groups",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter_term": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about a group. Only members of this group or users with admin-level permissions will be able to use this API.
            {
                "name": "get_groups_id",
                "table_name": "group_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/groups/{group_id}",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a specific group membership. Only admins of this group or users with admin-level permissions will be able to use this API.
            {
                "name": "get_group_memberships_id",
                "table_name": "group_membership",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/group_memberships/{group_membership_id}",
                    "params": {
                        "group_membership_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the status of a user invite.
            {
                "name": "get_invites_id",
                "table_name": "invite",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/invites/{invite_id}",
                    "params": {
                        "invite_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the files and/or folders contained within this collection.
            {
                "name": "get_collections_id_items",
                "table_name": "item",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/collections/{collection_id}/items",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the files and folders that have been moved to the trash.  Any attribute in the full files or folders objects can be passed in with the `fields` parameter to retrieve those specific attributes that are not returned by default.  This endpoint defaults to use offset-based pagination, yet also supports marker-based pagination using the `marker` parameter.
            {
                "name": "get_folders_trash_items",
                "table_name": "item",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/folders/trash/items",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "usemarker": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a page of items in a folder. These items can be files, folders, and web links.  To request more information about the folder itself, like its size, please use the [Get a folder](#get-folders-id) endpoint instead.
            {
                "name": "get_folders_id_items",
                "table_name": "item",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/folders/{folder_id}/items",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "usemarker": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of legal hold policies that belong to an enterprise.
            {
                "name": "get_legal_hold_policies",
                "table_name": "legal_hold_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/legal_hold_policies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "policy_name": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a legal hold policy.
            {
                "name": "get_legal_hold_policies_id",
                "table_name": "legal_hold_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/legal_hold_policies/{legal_hold_policy_id}",
                    "params": {
                        "legal_hold_policy_id": {
                            "type": "resolve",
                            "resource": "get_legal_hold_policies",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieve a legal hold policy assignment.
            {
                "name": "get_legal_hold_policy_assignments_id",
                "table_name": "legal_hold_policy_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/legal_hold_policy_assignments/{legal_hold_policy_assignment_id}",
                    "params": {
                        "legal_hold_policy_assignment_id": {
                            "type": "resolve",
                            "resource": "get_legal_hold_policy_assignments",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of items a legal hold policy has been assigned to.
            {
                "name": "get_legal_hold_policy_assignments",
                "table_name": "legal_hold_policy_assignment_base",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/legal_hold_policy_assignments",
                    "params": {
                        "policy_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "assign_to_type": "OPTIONAL_CONFIG",
                        # "assign_to_id": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about the user who is currently authenticated.  In the case of a client-side authenticated OAuth 2.0 application this will be the user who authorized the app.  In the case of a JWT, server-side authenticated application this will be the service account that belongs to the application by default.  Use the `As-User` header to change who this API call is made on behalf of.
            {
                "name": "get_users_me",
                "table_name": "me",
                "endpoint": {
                    "data_selector": "my_tags",
                    "path": "/users/me",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves all the members for a group. Only members of this group or users with admin-level permissions will be able to use this API.
            {
                "name": "get_groups_id_memberships",
                "table_name": "membership",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/groups/{group_id}/memberships",
                    "params": {
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all the groups for a user. Only members of this group or users with admin-level permissions will be able to use this API.
            {
                "name": "get_users_id_memberships",
                "table_name": "membership",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/users/{user_id}/memberships",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all metadata for a given file.
            {
                "name": "get_files_id_metadata",
                "table_name": "metadata",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/files/{file_id}/metadata",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves all metadata for a given folder. This can not be used on the root folder with ID `0`.
            {
                "name": "get_folders_id_metadata",
                "table_name": "metadata",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/folders/{folder_id}/metadata",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves a list of all the metadata cascade policies that are applied to a given folder. This can not be used on the root folder with ID `0`.
            {
                "name": "get_metadata_cascade_policies",
                "table_name": "metadata_cascade_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/metadata_cascade_policies",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "owner_enterprise_id": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "offset": "0",
                    },
                },
            },
            # Retrieve a specific metadata cascade policy assigned to a folder.
            {
                "name": "get_metadata_cascade_policies_id",
                "table_name": "metadata_cascade_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/metadata_cascade_policies/{metadata_cascade_policy_id}",
                    "params": {
                        "metadata_cascade_policy_id": {
                            "type": "resolve",
                            "resource": "get_metadata_cascade_policies",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a metadata template by its `scope` and `templateKey` values.  To find the `scope` and `templateKey` for a template, list all templates for an enterprise or globally, or list all templates applied to a file or folder.
            {
                "name": "get_metadata_templates_id_id_schema",
                "table_name": "metadata_field_write",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "fields",
                    "path": "/metadata_templates/{scope}/{template_key}/schema",
                    "params": {
                        "template_key": {
                            "type": "resolve",
                            "resource": "get_metadata_templates",
                            "field": "id",
                        },
                        "scope": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the metadata query indices for a given scope and template key.
            {
                "name": "get_metadata_query_indices",
                "table_name": "metadata_query_index",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/metadata_query_indices",
                    "params": {
                        "scope": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "template_key": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Finds a metadata template by searching for the ID of an instance of the template.
            {
                "name": "get_metadata_templates",
                "table_name": "metadata_template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/metadata_templates",
                    "params": {
                        "metadata_instance_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Used to retrieve all metadata templates created to be used specifically within the user's enterprise
            {
                "name": "get_metadata_templates_enterprise",
                "table_name": "metadata_template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/metadata_templates/enterprise",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Used to retrieve all generic, global metadata templates available to all enterprises using Box.
            {
                "name": "get_metadata_templates_global",
                "table_name": "metadata_template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/metadata_templates/global",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a metadata template by its ID.
            {
                "name": "get_metadata_templates_id",
                "table_name": "metadata_template",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/metadata_templates/{template_id}",
                    "params": {
                        "template_id": {
                            "type": "resolve",
                            "resource": "get_metadata_templates",
                            "field": "id",
                        },
                    },
                },
            },
            # Return a list of the chunks uploaded to the upload session so far.
            {
                "name": "get_files_upload_sessions_id_parts",
                "table_name": "part",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/files/upload_sessions/{upload_session_id}/parts",
                    "params": {
                        "upload_session_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns information about the recent items accessed by a user, either in the last 90 days or up to the last 1000 items accessed.
            {
                "name": "get_recent_items",
                "table_name": "recent_item",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/recent_items",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a retention policy.
            {
                "name": "get_retention_policies_id",
                "table_name": "retention_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/retention_policies/{retention_policy_id}",
                    "params": {
                        "retention_policy_id": {
                            "type": "resolve",
                            "resource": "get_retention_policies",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a retention policy assignment
            {
                "name": "get_retention_policy_assignments_id",
                "table_name": "retention_policy_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/retention_policy_assignments/{retention_policy_assignment_id}",
                    "params": {
                        "retention_policy_assignment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of all retention policy assignments associated with a specified retention policy.
            {
                "name": "get_retention_policies_id_assignments",
                "table_name": "retention_policy_assignment_base",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/retention_policies/{retention_policy_id}/assignments",
                    "params": {
                        "retention_policy_id": {
                            "type": "resolve",
                            "resource": "get_retention_policies",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves all of the retention policies for an enterprise.
            {
                "name": "get_retention_policies",
                "table_name": "retention_policy_mini",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/retention_policies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "policy_name": "OPTIONAL_CONFIG",
                        # "policy_type": "OPTIONAL_CONFIG",
                        # "created_by_user_id": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the classification metadata template and lists all the classifications available to this enterprise.  This API can also be called by including the enterprise ID in the URL explicitly, for example `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.
            {
                "name": "get_metadata_templates_enterprise_security_classification_6vm_vochw_u_wo_schema",
                "table_name": "schema",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "fields",
                    "path": "/metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema",
                },
            },
            # Searches for files, folders, web links, and shared files across the users content or across the entire enterprise.
            {
                "name": "get_search",
                "table_name": "search_result_with_shared_link",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "query": "OPTIONAL_CONFIG",
                        # "scope": "user_content",
                        # "file_extensions": "OPTIONAL_CONFIG",
                        # "created_at_range": "OPTIONAL_CONFIG",
                        # "updated_at_range": "OPTIONAL_CONFIG",
                        # "size_range": "OPTIONAL_CONFIG",
                        # "owner_user_ids": "OPTIONAL_CONFIG",
                        # "recent_updater_user_ids": "OPTIONAL_CONFIG",
                        # "ancestor_folder_ids": "OPTIONAL_CONFIG",
                        # "content_types": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "trash_content": "non_trashed_only",
                        # "mdfilters": "OPTIONAL_CONFIG",
                        # "sort": "relevance",
                        # "direction": "DESC",
                        # "include_recent_shared_links": "false",
                        # "fields": "OPTIONAL_CONFIG",
                        # "deleted_user_ids": "OPTIONAL_CONFIG",
                        # "deleted_at_range": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "offset",
                        "limit": 200,
                        "offset_param": "offset",
                        "limit_param": "limit",
                        "total_path": "total_count",
                    },
                },
            },
            # Returns the file represented by a shared link.  A shared file can be represented by a shared link, which can originate within the current enterprise or within another.  This endpoint allows an application to retrieve information about a shared file when only given a shared link.  The `shared_link_permission_options` array field can be returned by requesting it in the `fields` query parameter.
            {
                "name": "get_shared_items",
                "table_name": "shared_item",
                "endpoint": {
                    "data_selector": "allowed_invitee_roles",
                    "path": "/shared_items",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Return the folder represented by a shared link.  A shared folder can be represented by a shared link, which can originate within the current enterprise or within another.  This endpoint allows an application to retrieve information about a shared folder when only given a shared link.
            {
                "name": "get_shared_itemsfolders",
                "table_name": "shared_itemsfolder",
                "endpoint": {
                    "data_selector": "allowed_invitee_roles",
                    "path": "/shared_items#folders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a list of shield information barrier objects for the enterprise of JWT.
            {
                "name": "get_shield_information_barriers",
                "table_name": "shield_information_barrier",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/shield_information_barriers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get shield information barrier based on provided ID..
            {
                "name": "get_shield_information_barriers_id",
                "table_name": "shield_information_barrier",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/shield_information_barriers/{shield_information_barrier_id}",
                    "params": {
                        "shield_information_barrier_id": {
                            "type": "resolve",
                            "resource": "get_shield_information_barriers",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists shield information barrier reports with specific IDs.
            {
                "name": "get_shield_information_barrier_reports",
                "table_name": "shield_information_barrier_report",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/shield_information_barrier_reports",
                    "params": {
                        "shield_information_barrier_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a shield information barrier report by its ID.
            {
                "name": "get_shield_information_barrier_reports_id",
                "table_name": "shield_information_barrier_report",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/shield_information_barrier_reports/{shield_information_barrier_report_id}",
                    "params": {
                        "shield_information_barrier_report_id": {
                            "type": "resolve",
                            "resource": "get_shield_information_barrier_reports",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a list of shield information barrier segment objects for the specified Information Barrier ID.
            {
                "name": "get_shield_information_barrier_segments",
                "table_name": "shield_information_barrier_segment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/shield_information_barrier_segments",
                    "params": {
                        "shield_information_barrier_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves shield information barrier segment based on provided ID..
            {
                "name": "get_shield_information_barrier_segments_id",
                "table_name": "shield_information_barrier_segment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/shield_information_barrier_segments/{shield_information_barrier_segment_id}",
                    "params": {
                        "shield_information_barrier_segment_id": {
                            "type": "resolve",
                            "resource": "get_shield_information_barrier_segments",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists shield information barrier segment members based on provided segment IDs.
            {
                "name": "get_shield_information_barrier_segment_members",
                "table_name": "shield_information_barrier_segment_member",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/shield_information_barrier_segment_members",
                    "params": {
                        "shield_information_barrier_segment_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a shield information barrier segment member by its ID.
            {
                "name": "get_shield_information_barrier_segment_members_id",
                "table_name": "shield_information_barrier_segment_member",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}",
                    "params": {
                        "shield_information_barrier_segment_member_id": {
                            "type": "resolve",
                            "resource": "get_shield_information_barrier_segment_members",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists shield information barrier segment restrictions based on provided segment ID.
            {
                "name": "get_shield_information_barrier_segment_restrictions",
                "table_name": "shield_information_barrier_segment_restriction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/shield_information_barrier_segment_restrictions",
                    "params": {
                        "shield_information_barrier_segment_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a shield information barrier segment restriction based on provided ID.
            {
                "name": "get_shield_information_barrier_segment_restrictions_id",
                "table_name": "shield_information_barrier_segment_restriction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}",
                    "params": {
                        "shield_information_barrier_segment_restriction_id": {
                            "type": "resolve",
                            "resource": "get_shield_information_barrier_segment_restrictions",
                            "field": "id",
                        },
                    },
                },
            },
            # Gets sign requests created by a user. If the `sign_files` and/or `parent_folder` are deleted, the sign request will not return in the list.
            {
                "name": "get_sign_requests",
                "table_name": "sign_request",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/sign_requests",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a sign request by ID.
            {
                "name": "get_sign_requests_id",
                "table_name": "sign_request",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/sign_requests/{sign_request_id}",
                    "params": {
                        "sign_request_id": {
                            "type": "resolve",
                            "resource": "get_sign_requests",
                            "field": "id",
                        },
                    },
                },
            },
            # Fetches all the storage policies in the enterprise.
            {
                "name": "get_storage_policies",
                "table_name": "storage_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/storage_policies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetches a specific storage policy.
            {
                "name": "get_storage_policies_id",
                "table_name": "storage_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/storage_policies/{storage_policy_id}",
                    "params": {
                        "storage_policy_id": {
                            "type": "resolve",
                            "resource": "get_storage_policies",
                            "field": "id",
                        },
                    },
                },
            },
            # Fetches all the storage policy assignment for an enterprise or user.
            {
                "name": "get_storage_policy_assignments",
                "table_name": "storage_policy_assignment",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/storage_policy_assignments",
                    "params": {
                        "resolved_for_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "resolved_for_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetches a specific storage policy assignment.
            {
                "name": "get_storage_policy_assignments_id",
                "table_name": "storage_policy_assignment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/storage_policy_assignments/{storage_policy_assignment_id}",
                    "params": {
                        "storage_policy_assignment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves a list of all the tasks for a file. This endpoint does not support pagination.
            {
                "name": "get_files_id_tasks",
                "table_name": "task",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/files/{file_id}/tasks",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves information about a specific task.
            {
                "name": "get_tasks_id",
                "table_name": "task",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/tasks/{task_id}",
                    "params": {
                        "task_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves information about a task assignment.
            {
                "name": "get_task_assignments_id",
                "table_name": "task_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/task_assignments/{task_assignment_id}",
                    "params": {
                        "task_assignment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all of the assignments for a given task.
            {
                "name": "get_tasks_id_assignments",
                "table_name": "task_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/tasks/{task_id}/assignments",
                    "params": {
                        "task_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the current terms of service text and settings for the enterprise.
            {
                "name": "get_terms_of_services",
                "table_name": "terms_of_service",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/terms_of_services",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tos_type": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetches a specific terms of service.
            {
                "name": "get_terms_of_services_id",
                "table_name": "terms_of_service",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/terms_of_services/{terms_of_service_id}",
                    "params": {
                        "terms_of_service_id": {
                            "type": "resolve",
                            "resource": "get_terms_of_services",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves an overview of users and their status for a terms of service, including Whether they have accepted the terms and when.
            {
                "name": "get_terms_of_service_user_statuses",
                "table_name": "terms_of_service_user_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/terms_of_service_user_statuses",
                    "params": {
                        "tos_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "user_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a thumbnail, or smaller image representation, of a file.  Sizes of `32x32`,`64x64`, `128x128`, and `256x256` can be returned in the `.png` format and sizes of `32x32`, `160x160`, and `320x320` can be returned in the `.jpg` format.  Thumbnails can be generated for the image and video file formats listed [found on our community site][1].  [1]: https://community.box.com/t5/Migrating-and-Previewing-Content/File-Types-and-Fonts-Supported-in-Box-Content-Preview/ta-p/327
            {
                "name": "get_files_id_thumbnail_id",
                "table_name": "thumbnail",
                "endpoint": {
                    "path": "/files/{file_id}/thumbnail.{extension}",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "min_height": "OPTIONAL_CONFIG",
                        # "min_width": "OPTIONAL_CONFIG",
                        # "max_height": "OPTIONAL_CONFIG",
                        # "max_width": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a file that has been moved to the trash.  Please note that only if the file itself has been moved to the trash can it be retrieved with this API call. If instead one of its parent folders was moved to the trash, only that folder can be inspected using the [`GET /folders/:id/trash`](e://get_folders_id_trash) API.  To list all items that have been moved to the trash, please use the [`GET /folders/trash/items`](e://get-folders-trash-items/) API.
            {
                "name": "get_files_id_trash",
                "table_name": "trash",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "path_collection.entries",
                    "path": "/files/{file_id}/trash",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a folder that has been moved to the trash.  Please note that only if the folder itself has been moved to the trash can it be retrieved with this API call. If instead one of its parent folders was moved to the trash, only that folder can be inspected using the [`GET /folders/:id/trash`](e://get_folders_id_trash) API.  To list all items that have been moved to the trash, please use the [`GET /folders/trash/items`](e://get-folders-trash-items/) API.
            {
                "name": "get_folders_id_trash",
                "table_name": "trash",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "path_collection.entries",
                    "path": "/folders/{folder_id}/trash",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves a web link that has been moved to the trash.
            {
                "name": "get_web_links_id_trash",
                "table_name": "trash",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "path_collection.entries",
                    "path": "/web_links/{web_link_id}/trash",
                    "params": {
                        "web_link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Return information about an upload session.
            {
                "name": "get_files_upload_sessions_id",
                "table_name": "upload_session",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/upload_sessions/{upload_session_id}",
                    "params": {
                        "upload_session_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of all users for the Enterprise along with their `user_id`, `public_name`, and `login`.  The application and the authenticated user need to have the permission to look up users in the entire enterprise.
            {
                "name": "get_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter_term": "OPTIONAL_CONFIG",
                        # "user_type": "OPTIONAL_CONFIG",
                        # "external_app_user_id": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "usemarker": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves information about a user in the enterprise.  The application and the authenticated user need to have the permission to look up users in the entire enterprise.  This endpoint also returns a limited set of information for external users who are collaborated on content owned by the enterprise for authenticated users with the right scopes. In this case, disallowed fields will return null instead.
            {
                "name": "get_users_id",
                "table_name": "user_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{user_id}",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of the past versions for a file.  Versions are only tracked by Box users with premium accounts. To fetch the ID of the current version of a file, use the `GET /file/:id` API.
            {
                "name": "get_files_id_versions",
                "table_name": "version",
                "endpoint": {
                    "data_selector": "order",
                    "path": "/files/{file_id}/versions",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "fields": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve the watermark for a file.
            {
                "name": "get_files_id_watermark",
                "table_name": "watermark",
                "endpoint": {
                    "data_selector": "watermark",
                    "path": "/files/{file_id}/watermark",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the watermark for a folder.
            {
                "name": "get_folders_id_watermark",
                "table_name": "watermark",
                "endpoint": {
                    "data_selector": "watermark",
                    "path": "/folders/{folder_id}/watermark",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve information about a web link.
            {
                "name": "get_web_links_id",
                "table_name": "web_link",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/web_links/{web_link_id}",
                    "params": {
                        "web_link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves a specific webhook
            {
                "name": "get_webhooks_id",
                "table_name": "webhook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/webhooks/{webhook_id}",
                    "params": {
                        "webhook_id": {
                            "type": "resolve",
                            "resource": "get_webhooks",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns all defined webhooks for the requesting application.  This API only returns webhooks that are applied to files or folders that are owned by the authenticated user. This means that an admin can not see webhooks created by a service account unless the admin has access to those folders, and vice versa.
            {
                "name": "get_webhooks",
                "table_name": "webhook_mini",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/webhooks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "marker": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns list of workflows that act on a given `folder ID`, and have a flow with a trigger type of `WORKFLOW_MANUAL_START`.  You application must be authorized to use the `Manage Box Relay` application scope within the developer console in to use this endpoint.
            {
                "name": "get_workflows",
                "table_name": "workflow",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "entries",
                    "path": "/workflows",
                    "params": {
                        "folder_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "trigger_type": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "marker": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the download status of a `zip` archive, allowing an application to inspect the progress of the download as well as the number of items that might have been skipped.  This endpoint can only be accessed once the download has started. Subsequently this endpoint is valid for 12 hours from the start of the download.  The URL of this endpoint should not be considered as fixed. Instead, use the [Create zip download](e://post_zip_downloads) API to request to create a `zip` archive, and then follow the `status_url` field in the response to this endpoint.
            {
                "name": "get_zip_downloads_id_status",
                "table_name": "zip_download_status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/zip_downloads/{zip_download_id}/status",
                    "params": {
                        "zip_download_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
