# box_platform pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/box_platform.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /authorize_ 
  *resource*: get_authorize  
  *description*: Authorize a user by sending them through the [Box](https://box.com) website and request their permission to act on their behalf.  This is the first step when authenticating a user using OAuth 2.0. To request a user's authorization to use the Box APIs on their behalf you will need to send a user to the URL with this format.
* _GET /users/{user_id}/avatar_ 
  *resource*: get_users_id_avatar  
  *description*: Retrieves an image of a the user's avatar.
* _GET /files/{file_id}/metadata/global/boxSkillsCards_ 
  *resource*: get_files_id_metadata_global_box_skills_cards  
  *description*: List the Box Skills metadata cards that are attached to a file.
* _GET /files/{file_id}/content_ 
  *resource*: get_files_id_content  
  *description*: Returns the contents of a file in binary format.
* _GET /files/{file_id}/metadata/enterprise/securityClassification-6VMVochwUWo_ 
  *resource*: get_files_id_metadata_enterprise_security_classification_6vm_vochw_u_wo  
  *description*: Retrieves the classification metadata instance that has been applied to a file.  This API can also be called by including the enterprise ID in the URL explicitly, for example `/files/:id//enterprise_12345/securityClassification-6VMVochwUWo`.
* _GET /files/{file_id}/metadata/{scope}/{template_key}_ 
  *resource*: get_files_id_metadata_id_id  
  *description*: Retrieves the instance of a metadata template that has been applied to a file.
* _GET /folders/{folder_id}/metadata/enterprise/securityClassification-6VMVochwUWo_ 
  *resource*: get_folders_id_metadata_enterprise_security_classification_6vm_vochw_u_wo  
  *description*: Retrieves the classification metadata instance that has been applied to a folder.  This API can also be called by including the enterprise ID in the URL explicitly, for example `/folders/:id//enterprise_12345/securityClassification-6VMVochwUWo`.
* _GET /folders/{folder_id}/metadata/{scope}/{template_key}_ 
  *resource*: get_folders_id_metadata_id_id  
  *description*: Retrieves the instance of a metadata template that has been applied to a folder. This can not be used on the root folder with ID `0`.
* _GET /collaborations_ 
  *resource*: get_collaborations  
  *description*: Retrieves all pending collaboration invites for this user.
* _GET /collaborations/{collaboration_id}_ 
  *resource*: get_collaborations_id  
  *description*: Retrieves a single collaboration.
* _GET /files/{file_id}/collaborations_ 
  *resource*: get_files_id_collaborations  
  *description*: Retrieves a list of pending and active collaborations for a file. This returns all the users that have access to the file or have been invited to the file.
* _GET /folders/{folder_id}/collaborations_ 
  *resource*: get_folders_id_collaborations  
  *description*: Retrieves a list of pending and active collaborations for a folder. This returns all the users that have access to the folder or have been invited to the folder.
* _GET /groups/{group_id}/collaborations_ 
  *resource*: get_groups_id_collaborations  
  *description*: Retrieves all the collaborations for a group. The user must have admin permissions to inspect enterprise's groups.  Each collaboration object has details on which files or folders the group has access to and with what role.
* _GET /collaboration_whitelist_entries_ 
  *resource*: get_collaboration_whitelist_entries  
  *description*: Returns the list domains that have been deemed safe to create collaborations for within the current enterprise.
* _GET /collaboration_whitelist_entries/{collaboration_whitelist_entry_id}_ 
  *resource*: get_collaboration_whitelist_entries_id  
  *description*: Returns a domain that has been deemed safe to create collaborations for within the current enterprise.
* _GET /collaboration_whitelist_exempt_targets_ 
  *resource*: get_collaboration_whitelist_exempt_targets  
  *description*: Returns a list of users who have been exempt from the collaboration domain restrictions.
* _GET /collaboration_whitelist_exempt_targets/{collaboration_whitelist_exempt_target_id}_ 
  *resource*: get_collaboration_whitelist_exempt_targets_id  
  *description*: Returns a users who has been exempt from the collaboration domain restrictions.
* _GET /collections_ 
  *resource*: get_collections  
  *description*: Retrieves all collections for a given user.  Currently, only the `favorites` collection is supported.
* _GET /files/{file_id}/comments_ 
  *resource*: get_files_id_comments  
  *description*: Retrieves a list of comments for a file.
* _GET /comments/{comment_id}_ 
  *resource*: get_comments_id  
  *description*: Retrieves the message and metadata for a specific comment, as well as information on the user who created the comment.
* _GET /zip_downloads/{zip_download_id}/content_ 
  *resource*: get_zip_downloads_id_content  
  *description*: Returns the contents of a `zip` archive in binary format. This URL does not require any form of authentication and could be used in a user's browser to download the archive to a user's device.  By default, this URL is only valid for a few seconds from the creation of the request for this archive. Once a download has started it can not be stopped and resumed, instead a new request for a zip archive would need to be created.  The URL of this endpoint should not be considered as fixed. Instead, use the [Create zip download](e://post_zip_downloads) API to request to create a `zip` archive, and then follow the `download_url` field in the response to this endpoint.
* _GET /device_pinners/{device_pinner_id}_ 
  *resource*: get_device_pinners_id  
  *description*: Retrieves information about an individual device pin.
* _GET /enterprises/{enterprise_id}/device_pinners_ 
  *resource*: get_enterprises_id_device_pinners  
  *description*: Retrieves all the device pins within an enterprise.  The user must have admin privileges, and the application needs the "manage enterprise" scope to make this call.
* _GET /users/{user_id}/email_aliases_ 
  *resource*: get_users_id_email_aliases  
  *description*: Retrieves all email aliases for a user. The collection does not include the primary login for the user.
* _GET /events_ 
  *resource*: get_events  
  *description*: Returns up to a year of past events for a given user or for the entire enterprise.  By default this returns events for the authenticated user. To retrieve events for the entire enterprise, set the `stream_type` to `admin_logs_streaming` for live monitoring of new events, or `admin_logs` for querying across historical events. The user making the API call will need to have admin privileges, and the application will need to have the scope `manage enterprise properties` checked.
* _GET /files/{file_id}_ 
  *resource*: get_files_id  
  *description*: Retrieves the details about a file.
* _GET /files/{file_id}#get_shared_link_ 
  *resource*: get_files_idget_shared_link  
  *description*: Gets the information for a shared link on a file.
* _GET /retention_policy_assignments/{retention_policy_assignment_id}/file_versions_under_retention_ 
  *resource*: get_retention_policy_assignments_id_file_versions_under_retention  
  *description*: Returns a list of file versions under retention for a retention policy assignment.
* _GET /retention_policy_assignments/{retention_policy_assignment_id}/files_under_retention_ 
  *resource*: get_retention_policy_assignments_id_files_under_retention  
  *description*: Returns a list of files under retention for a retention policy assignment.
* _GET /file_requests/{file_request_id}_ 
  *resource*: get_file_requests_id  
  *description*: Retrieves the information about a file request.
* _GET /files/{file_id}/versions/{file_version_id}_ 
  *resource*: get_files_id_versions_id  
  *description*: Retrieve a specific version of a file.  Versions are only tracked for Box users with premium accounts.
* _GET /file_version_legal_holds_ 
  *resource*: get_file_version_legal_holds  
  *description*: Get a list of file versions on legal hold for a legal hold assignment.  Due to ongoing re-architecture efforts this API might not return all file versions for this policy ID.  Instead, this API will only return file versions held in the legacy architecture. Two new endpoints will available to request any file versions held in the new architecture.  For file versions held in the new architecture, the `GET /legal_hold_policy_assignments/:id/file_versions_on_hold` API can be used to return all past file versions available for this policy assignment, and the `GET /legal_hold_policy_assignments/:id/files_on_hold` API can be used to return any current (latest) versions of a file under legal hold.  The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to find a list of policy assignments for a given policy ID.  Once the re-architecture is completed this API will be deprecated.
* _GET /file_version_legal_holds/{file_version_legal_hold_id}_ 
  *resource*: get_file_version_legal_holds_id  
  *description*: Retrieves information about the legal hold policies assigned to a file version.
* _GET /legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/file_versions_on_hold_ 
  *resource*: get_legal_hold_policy_assignments_id_file_versions_on_hold  
  *description*: Get a list of previous file versions for a legal hold assignment.  In some cases you may only need the latest file versions instead. In these cases, use the `GET  /legal_hold_policy_assignments/:id/files_on_hold` API instead to return any current (latest) versions of a file for this legal hold policy assignment.  Due to ongoing re-architecture efforts this API might not return all files held for this policy ID. Instead, this API will only return past file versions held in the newly developed architecture. The `GET /file_version_legal_holds` API can be used to fetch current and past versions of files held within the legacy architecture.  The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to find a list of policy assignments for a given policy ID.
* _GET /legal_hold_policy_assignments/{legal_hold_policy_assignment_id}/files_on_hold_ 
  *resource*: get_legal_hold_policy_assignments_id_files_on_hold  
  *description*: Get a list of current file versions for a legal hold assignment.  In some cases you may want to get previous file versions instead. In these cases, use the `GET  /legal_hold_policy_assignments/:id/file_versions_on_hold` API instead to return any previous versions of a file for this legal hold policy assignment.  Due to ongoing re-architecture efforts this API might not return all file versions held for this policy ID. Instead, this API will only return the latest file version held in the newly developed architecture. The `GET /file_version_legal_holds` API can be used to fetch current and past versions of files held within the legacy architecture.  The `GET /legal_hold_policy_assignments?policy_id={id}` API can be used to find a list of policy assignments for a given policy ID.
* _GET /file_version_retentions_ 
  *resource*: get_file_version_retentions  
  *description*: Retrieves all file version retentions for the given enterprise.
* _GET /file_version_retentions/{file_version_retention_id}_ 
  *resource*: get_file_version_retentions_id  
  *description*: Returns information about a file version retention.
* _GET /folders/{folder_id}_ 
  *resource*: get_folders_id  
  *description*: Retrieves details for a folder, including the first 100 entries in the folder.  To fetch more items within the folder, please use the [Get items in a folder](#get-folders-id-items) endpoint.
* _GET /folders/{folder_id}#get_shared_link_ 
  *resource*: get_folders_idget_shared_link  
  *description*: Gets the information for a shared link on a folder.
* _GET /folder_locks_ 
  *resource*: get_folder_locks  
  *description*: Retrieves folder lock details for a given folder.  You must be authenticated as the owner or co-owner of the folder to use this endpoint.
* _GET /shared_items#web_links_ 
  *resource*: get_shared_itemsweb_links  
  *description*: Returns the web link represented by a shared link.  A shared web link can be represented by a shared link, which can originate within the current enterprise or within another.  This endpoint allows an application to retrieve information about a shared web link when only given a shared link.
* _GET /web_links/{web_link_id}#get_shared_link_ 
  *resource*: get_web_links_idget_shared_link  
  *description*: Gets the information for a shared link on a web link.
* _GET /groups_ 
  *resource*: get_groups  
  *description*: Retrieves all of the groups for a given enterprise. The user must have admin permissions to inspect enterprise's groups.
* _GET /groups/{group_id}_ 
  *resource*: get_groups_id  
  *description*: Retrieves information about a group. Only members of this group or users with admin-level permissions will be able to use this API.
* _GET /group_memberships/{group_membership_id}_ 
  *resource*: get_group_memberships_id  
  *description*: Retrieves a specific group membership. Only admins of this group or users with admin-level permissions will be able to use this API.
* _GET /invites/{invite_id}_ 
  *resource*: get_invites_id  
  *description*: Returns the status of a user invite.
* _GET /collections/{collection_id}/items_ 
  *resource*: get_collections_id_items  
  *description*: Retrieves the files and/or folders contained within this collection.
* _GET /folders/trash/items_ 
  *resource*: get_folders_trash_items  
  *description*: Retrieves the files and folders that have been moved to the trash.  Any attribute in the full files or folders objects can be passed in with the `fields` parameter to retrieve those specific attributes that are not returned by default.  This endpoint defaults to use offset-based pagination, yet also supports marker-based pagination using the `marker` parameter.
* _GET /folders/{folder_id}/items_ 
  *resource*: get_folders_id_items  
  *description*: Retrieves a page of items in a folder. These items can be files, folders, and web links.  To request more information about the folder itself, like its size, please use the [Get a folder](#get-folders-id) endpoint instead.
* _GET /legal_hold_policies_ 
  *resource*: get_legal_hold_policies  
  *description*: Retrieves a list of legal hold policies that belong to an enterprise.
* _GET /legal_hold_policies/{legal_hold_policy_id}_ 
  *resource*: get_legal_hold_policies_id  
  *description*: Retrieve a legal hold policy.
* _GET /legal_hold_policy_assignments/{legal_hold_policy_assignment_id}_ 
  *resource*: get_legal_hold_policy_assignments_id  
  *description*: Retrieve a legal hold policy assignment.
* _GET /legal_hold_policy_assignments_ 
  *resource*: get_legal_hold_policy_assignments  
  *description*: Retrieves a list of items a legal hold policy has been assigned to.
* _GET /users/me_ 
  *resource*: get_users_me  
  *description*: Retrieves information about the user who is currently authenticated.  In the case of a client-side authenticated OAuth 2.0 application this will be the user who authorized the app.  In the case of a JWT, server-side authenticated application this will be the service account that belongs to the application by default.  Use the `As-User` header to change who this API call is made on behalf of.
* _GET /groups/{group_id}/memberships_ 
  *resource*: get_groups_id_memberships  
  *description*: Retrieves all the members for a group. Only members of this group or users with admin-level permissions will be able to use this API.
* _GET /users/{user_id}/memberships_ 
  *resource*: get_users_id_memberships  
  *description*: Retrieves all the groups for a user. Only members of this group or users with admin-level permissions will be able to use this API.
* _GET /files/{file_id}/metadata_ 
  *resource*: get_files_id_metadata  
  *description*: Retrieves all metadata for a given file.
* _GET /folders/{folder_id}/metadata_ 
  *resource*: get_folders_id_metadata  
  *description*: Retrieves all metadata for a given folder. This can not be used on the root folder with ID `0`.
* _GET /metadata_cascade_policies_ 
  *resource*: get_metadata_cascade_policies  
  *description*: Retrieves a list of all the metadata cascade policies that are applied to a given folder. This can not be used on the root folder with ID `0`.
* _GET /metadata_cascade_policies/{metadata_cascade_policy_id}_ 
  *resource*: get_metadata_cascade_policies_id  
  *description*: Retrieve a specific metadata cascade policy assigned to a folder.
* _GET /metadata_templates/{scope}/{template_key}/schema_ 
  *resource*: get_metadata_templates_id_id_schema  
  *description*: Retrieves a metadata template by its `scope` and `templateKey` values.  To find the `scope` and `templateKey` for a template, list all templates for an enterprise or globally, or list all templates applied to a file or folder.
* _GET /metadata_query_indices_ 
  *resource*: get_metadata_query_indices  
  *description*: Retrieves the metadata query indices for a given scope and template key.
* _GET /metadata_templates_ 
  *resource*: get_metadata_templates  
  *description*: Finds a metadata template by searching for the ID of an instance of the template.
* _GET /metadata_templates/enterprise_ 
  *resource*: get_metadata_templates_enterprise  
  *description*: Used to retrieve all metadata templates created to be used specifically within the user's enterprise
* _GET /metadata_templates/global_ 
  *resource*: get_metadata_templates_global  
  *description*: Used to retrieve all generic, global metadata templates available to all enterprises using Box.
* _GET /metadata_templates/{template_id}_ 
  *resource*: get_metadata_templates_id  
  *description*: Retrieves a metadata template by its ID.
* _GET /files/upload_sessions/{upload_session_id}/parts_ 
  *resource*: get_files_upload_sessions_id_parts  
  *description*: Return a list of the chunks uploaded to the upload session so far.
* _GET /recent_items_ 
  *resource*: get_recent_items  
  *description*: Returns information about the recent items accessed by a user, either in the last 90 days or up to the last 1000 items accessed.
* _GET /retention_policies/{retention_policy_id}_ 
  *resource*: get_retention_policies_id  
  *description*: Retrieves a retention policy.
* _GET /retention_policy_assignments/{retention_policy_assignment_id}_ 
  *resource*: get_retention_policy_assignments_id  
  *description*: Retrieves a retention policy assignment
* _GET /retention_policies/{retention_policy_id}/assignments_ 
  *resource*: get_retention_policies_id_assignments  
  *description*: Returns a list of all retention policy assignments associated with a specified retention policy.
* _GET /retention_policies_ 
  *resource*: get_retention_policies  
  *description*: Retrieves all of the retention policies for an enterprise.
* _GET /metadata_templates/enterprise/securityClassification-6VMVochwUWo/schema_ 
  *resource*: get_metadata_templates_enterprise_security_classification_6vm_vochw_u_wo_schema  
  *description*: Retrieves the classification metadata template and lists all the classifications available to this enterprise.  This API can also be called by including the enterprise ID in the URL explicitly, for example `/metadata_templates/enterprise_12345/securityClassification-6VMVochwUWo/schema`.
* _GET /search_ 
  *resource*: get_search  
  *description*: Searches for files, folders, web links, and shared files across the users content or across the entire enterprise.
* _GET /shared_items_ 
  *resource*: get_shared_items  
  *description*: Returns the file represented by a shared link.  A shared file can be represented by a shared link, which can originate within the current enterprise or within another.  This endpoint allows an application to retrieve information about a shared file when only given a shared link.  The `shared_link_permission_options` array field can be returned by requesting it in the `fields` query parameter.
* _GET /shared_items#folders_ 
  *resource*: get_shared_itemsfolders  
  *description*: Return the folder represented by a shared link.  A shared folder can be represented by a shared link, which can originate within the current enterprise or within another.  This endpoint allows an application to retrieve information about a shared folder when only given a shared link.
* _GET /shield_information_barriers_ 
  *resource*: get_shield_information_barriers  
  *description*: Retrieves a list of shield information barrier objects for the enterprise of JWT.
* _GET /shield_information_barriers/{shield_information_barrier_id}_ 
  *resource*: get_shield_information_barriers_id  
  *description*: Get shield information barrier based on provided ID..
* _GET /shield_information_barrier_reports_ 
  *resource*: get_shield_information_barrier_reports  
  *description*: Lists shield information barrier reports with specific IDs.
* _GET /shield_information_barrier_reports/{shield_information_barrier_report_id}_ 
  *resource*: get_shield_information_barrier_reports_id  
  *description*: Retrieves a shield information barrier report by its ID.
* _GET /shield_information_barrier_segments_ 
  *resource*: get_shield_information_barrier_segments  
  *description*: Retrieves a list of shield information barrier segment objects for the specified Information Barrier ID.
* _GET /shield_information_barrier_segments/{shield_information_barrier_segment_id}_ 
  *resource*: get_shield_information_barrier_segments_id  
  *description*: Retrieves shield information barrier segment based on provided ID..
* _GET /shield_information_barrier_segment_members_ 
  *resource*: get_shield_information_barrier_segment_members  
  *description*: Lists shield information barrier segment members based on provided segment IDs.
* _GET /shield_information_barrier_segment_members/{shield_information_barrier_segment_member_id}_ 
  *resource*: get_shield_information_barrier_segment_members_id  
  *description*: Retrieves a shield information barrier segment member by its ID.
* _GET /shield_information_barrier_segment_restrictions_ 
  *resource*: get_shield_information_barrier_segment_restrictions  
  *description*: Lists shield information barrier segment restrictions based on provided segment ID.
* _GET /shield_information_barrier_segment_restrictions/{shield_information_barrier_segment_restriction_id}_ 
  *resource*: get_shield_information_barrier_segment_restrictions_id  
  *description*: Retrieves a shield information barrier segment restriction based on provided ID.
* _GET /sign_requests_ 
  *resource*: get_sign_requests  
  *description*: Gets sign requests created by a user. If the `sign_files` and/or `parent_folder` are deleted, the sign request will not return in the list.
* _GET /sign_requests/{sign_request_id}_ 
  *resource*: get_sign_requests_id  
  *description*: Gets a sign request by ID.
* _GET /storage_policies_ 
  *resource*: get_storage_policies  
  *description*: Fetches all the storage policies in the enterprise.
* _GET /storage_policies/{storage_policy_id}_ 
  *resource*: get_storage_policies_id  
  *description*: Fetches a specific storage policy.
* _GET /storage_policy_assignments_ 
  *resource*: get_storage_policy_assignments  
  *description*: Fetches all the storage policy assignment for an enterprise or user.
* _GET /storage_policy_assignments/{storage_policy_assignment_id}_ 
  *resource*: get_storage_policy_assignments_id  
  *description*: Fetches a specific storage policy assignment.
* _GET /files/{file_id}/tasks_ 
  *resource*: get_files_id_tasks  
  *description*: Retrieves a list of all the tasks for a file. This endpoint does not support pagination.
* _GET /tasks/{task_id}_ 
  *resource*: get_tasks_id  
  *description*: Retrieves information about a specific task.
* _GET /task_assignments/{task_assignment_id}_ 
  *resource*: get_task_assignments_id  
  *description*: Retrieves information about a task assignment.
* _GET /tasks/{task_id}/assignments_ 
  *resource*: get_tasks_id_assignments  
  *description*: Lists all of the assignments for a given task.
* _GET /terms_of_services_ 
  *resource*: get_terms_of_services  
  *description*: Returns the current terms of service text and settings for the enterprise.
* _GET /terms_of_services/{terms_of_service_id}_ 
  *resource*: get_terms_of_services_id  
  *description*: Fetches a specific terms of service.
* _GET /terms_of_service_user_statuses_ 
  *resource*: get_terms_of_service_user_statuses  
  *description*: Retrieves an overview of users and their status for a terms of service, including Whether they have accepted the terms and when.
* _GET /files/{file_id}/thumbnail.{extension}_ 
  *resource*: get_files_id_thumbnail_id  
  *description*: Retrieves a thumbnail, or smaller image representation, of a file.  Sizes of `32x32`,`64x64`, `128x128`, and `256x256` can be returned in the `.png` format and sizes of `32x32`, `160x160`, and `320x320` can be returned in the `.jpg` format.  Thumbnails can be generated for the image and video file formats listed [found on our community site][1].  [1]: https://community.box.com/t5/Migrating-and-Previewing-Content/File-Types-and-Fonts-Supported-in-Box-Content-Preview/ta-p/327
* _GET /files/{file_id}/trash_ 
  *resource*: get_files_id_trash  
  *description*: Retrieves a file that has been moved to the trash.  Please note that only if the file itself has been moved to the trash can it be retrieved with this API call. If instead one of its parent folders was moved to the trash, only that folder can be inspected using the [`GET /folders/:id/trash`](e://get_folders_id_trash) API.  To list all items that have been moved to the trash, please use the [`GET /folders/trash/items`](e://get-folders-trash-items/) API.
* _GET /folders/{folder_id}/trash_ 
  *resource*: get_folders_id_trash  
  *description*: Retrieves a folder that has been moved to the trash.  Please note that only if the folder itself has been moved to the trash can it be retrieved with this API call. If instead one of its parent folders was moved to the trash, only that folder can be inspected using the [`GET /folders/:id/trash`](e://get_folders_id_trash) API.  To list all items that have been moved to the trash, please use the [`GET /folders/trash/items`](e://get-folders-trash-items/) API.
* _GET /web_links/{web_link_id}/trash_ 
  *resource*: get_web_links_id_trash  
  *description*: Retrieves a web link that has been moved to the trash.
* _GET /files/upload_sessions/{upload_session_id}_ 
  *resource*: get_files_upload_sessions_id  
  *description*: Return information about an upload session.
* _GET /users_ 
  *resource*: get_users  
  *description*: Returns a list of all users for the Enterprise along with their `user_id`, `public_name`, and `login`.  The application and the authenticated user need to have the permission to look up users in the entire enterprise.
* _GET /users/{user_id}_ 
  *resource*: get_users_id  
  *description*: Retrieves information about a user in the enterprise.  The application and the authenticated user need to have the permission to look up users in the entire enterprise.  This endpoint also returns a limited set of information for external users who are collaborated on content owned by the enterprise for authenticated users with the right scopes. In this case, disallowed fields will return null instead.
* _GET /files/{file_id}/versions_ 
  *resource*: get_files_id_versions  
  *description*: Retrieve a list of the past versions for a file.  Versions are only tracked by Box users with premium accounts. To fetch the ID of the current version of a file, use the `GET /file/:id` API.
* _GET /files/{file_id}/watermark_ 
  *resource*: get_files_id_watermark  
  *description*: Retrieve the watermark for a file.
* _GET /folders/{folder_id}/watermark_ 
  *resource*: get_folders_id_watermark  
  *description*: Retrieve the watermark for a folder.
* _GET /web_links/{web_link_id}_ 
  *resource*: get_web_links_id  
  *description*: Retrieve information about a web link.
* _GET /webhooks/{webhook_id}_ 
  *resource*: get_webhooks_id  
  *description*: Retrieves a specific webhook
* _GET /webhooks_ 
  *resource*: get_webhooks  
  *description*: Returns all defined webhooks for the requesting application.  This API only returns webhooks that are applied to files or folders that are owned by the authenticated user. This means that an admin can not see webhooks created by a service account unless the admin has access to those folders, and vice versa.
* _GET /workflows_ 
  *resource*: get_workflows  
  *description*: Returns list of workflows that act on a given `folder ID`, and have a flow with a trigger type of `WORKFLOW_MANUAL_START`.  You application must be authorized to use the `Manage Box Relay` application scope within the developer console in to use this endpoint.
* _GET /zip_downloads/{zip_download_id}/status_ 
  *resource*: get_zip_downloads_id_status  
  *description*: Returns the download status of a `zip` archive, allowing an application to inspect the progress of the download as well as the number of items that might have been skipped.  This endpoint can only be accessed once the download has started. Subsequently this endpoint is valid for 12 hours from the start of the download.  The URL of this endpoint should not be considered as fixed. Instead, use the [Create zip download](e://post_zip_downloads) API to request to create a `zip` archive, and then follow the `status_url` field in the response to this endpoint.
