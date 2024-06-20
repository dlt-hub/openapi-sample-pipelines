from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_drive_source", max_table_nesting=2)
def google_drive_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Gets information about the user, the user's Drive, and system capabilities.
            {
                "name": "drive_about_get",
                "table_name": "about",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "driveThemes",
                    "path": "/about",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists a user's installed apps.
            {
                "name": "drive_apps_list",
                "table_name": "app",
                "endpoint": {
                    "data_selector": "defaultAppIds",
                    "path": "/apps",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "appFilterExtensions": "OPTIONAL_CONFIG",
                        # "appFilterMimeTypes": "OPTIONAL_CONFIG",
                        # "languageCode": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a specific app.
            {
                "name": "drive_apps_get",
                "table_name": "app",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/apps/{appId}",
                    "params": {
                        "appId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the changes for a user or shared drive.
            {
                "name": "drive_changes_list",
                "table_name": "change",
                "endpoint": {
                    "data_selector": "changes",
                    "path": "/changes",
                    "params": {
                        "pageToken": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "driveId": "OPTIONAL_CONFIG",
                        # "includeCorpusRemovals": "OPTIONAL_CONFIG",
                        # "includeItemsFromAllDrives": "OPTIONAL_CONFIG",
                        # "includeLabels": "OPTIONAL_CONFIG",
                        # "includePermissionsForView": "OPTIONAL_CONFIG",
                        # "includeRemoved": "OPTIONAL_CONFIG",
                        # "includeTeamDriveItems": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "restrictToMyDrive": "OPTIONAL_CONFIG",
                        # "spaces": "OPTIONAL_CONFIG",
                        # "supportsAllDrives": "OPTIONAL_CONFIG",
                        # "supportsTeamDrives": "OPTIONAL_CONFIG",
                        # "teamDriveId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists a file's comments.
            {
                "name": "drive_comments_list",
                "table_name": "comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "comments",
                    "path": "/files/{fileId}/comments",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "drive_files_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "includeDeleted": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "startModifiedTime": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a comment by ID.
            {
                "name": "drive_comments_get",
                "table_name": "comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{fileId}/comments/{commentId}",
                    "params": {
                        "commentId": {
                            "type": "resolve",
                            "resource": "drive_comments_list",
                            "field": "id",
                        },
                        "fileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "includeDeleted": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #  Lists the user's shared drives. This method accepts the `q` parameter, which is a search query combining one or more search terms. For more information, see the [Search for shared drives](/drive/api/guides/search-shareddrives) guide.
            {
                "name": "drive_drives_list",
                "table_name": "drive",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "drives",
                    "path": "/drives",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "q": "OPTIONAL_CONFIG",
                        # "useDomainAdminAccess": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a shared drive's metadata by ID.
            {
                "name": "drive_drives_get",
                "table_name": "drive",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/drives/{driveId}",
                    "params": {
                        "driveId": {
                            "type": "resolve",
                            "resource": "drive_drives_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "useDomainAdminAccess": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.
            {
                "name": "drive_files_export",
                "table_name": "export",
                "endpoint": {
                    "path": "/files/{fileId}/export",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "drive_files_list",
                            "field": "id",
                        },
                        "mimeType": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #  Lists the user's files. This method accepts the `q` parameter, which is a search query combining one or more search terms. For more information, see the [Search for files & folders](/drive/api/guides/search-files) guide. *Note:* This method returns *all* files by default, including trashed files. If you don't want trashed files to appear in the list, use the `trashed=false` query parameter to remove trashed files from the results.
            {
                "name": "drive_files_list",
                "table_name": "file",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "files",
                    "path": "/files",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "corpora": "OPTIONAL_CONFIG",
                        # "corpus": "OPTIONAL_CONFIG",
                        # "driveId": "OPTIONAL_CONFIG",
                        # "includeItemsFromAllDrives": "OPTIONAL_CONFIG",
                        # "includeLabels": "OPTIONAL_CONFIG",
                        # "includePermissionsForView": "OPTIONAL_CONFIG",
                        # "includeTeamDriveItems": "OPTIONAL_CONFIG",
                        # "orderBy": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "q": "OPTIONAL_CONFIG",
                        # "spaces": "OPTIONAL_CONFIG",
                        # "supportsAllDrives": "OPTIONAL_CONFIG",
                        # "supportsTeamDrives": "OPTIONAL_CONFIG",
                        # "teamDriveId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #  Gets a file's metadata or content by ID. If you provide the URL parameter `alt=media`, then the response includes the file contents in the response body. Downloading content with `alt=media` only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [`files.export`](/drive/api/reference/rest/v3/files/export) instead. For more information, see [Download & export files](/drive/api/guides/manage-downloads).
            {
                "name": "drive_files_get",
                "table_name": "file",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{fileId}",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "drive_files_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "acknowledgeAbuse": "OPTIONAL_CONFIG",
                        # "includeLabels": "OPTIONAL_CONFIG",
                        # "includePermissionsForView": "OPTIONAL_CONFIG",
                        # "supportsAllDrives": "OPTIONAL_CONFIG",
                        # "supportsTeamDrives": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Generates a set of file IDs which can be provided in create or copy requests.
            {
                "name": "drive_files_generate_ids",
                "table_name": "generate_id",
                "endpoint": {
                    "data_selector": "ids",
                    "path": "/files/generateIds",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "count": "OPTIONAL_CONFIG",
                        # "space": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists the labels on a file.
            {
                "name": "drive_files_list_labels",
                "table_name": "label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "labels",
                    "path": "/files/{fileId}/listLabels",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "drive_files_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists a file's or shared drive's permissions.
            {
                "name": "drive_permissions_list",
                "table_name": "permission",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "permissions",
                    "path": "/files/{fileId}/permissions",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "drive_files_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "includePermissionsForView": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "supportsAllDrives": "OPTIONAL_CONFIG",
                        # "supportsTeamDrives": "OPTIONAL_CONFIG",
                        # "useDomainAdminAccess": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a permission by ID.
            {
                "name": "drive_permissions_get",
                "table_name": "permission",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{fileId}/permissions/{permissionId}",
                    "params": {
                        "permissionId": {
                            "type": "resolve",
                            "resource": "drive_permissions_list",
                            "field": "id",
                        },
                        "fileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "supportsAllDrives": "OPTIONAL_CONFIG",
                        # "supportsTeamDrives": "OPTIONAL_CONFIG",
                        # "useDomainAdminAccess": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists a comment's replies.
            {
                "name": "drive_replies_list",
                "table_name": "reply",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "replies",
                    "path": "/files/{fileId}/comments/{commentId}/replies",
                    "params": {
                        "commentId": {
                            "type": "resolve",
                            "resource": "drive_comments_list",
                            "field": "id",
                        },
                        "fileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "includeDeleted": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a reply by ID.
            {
                "name": "drive_replies_get",
                "table_name": "reply",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{fileId}/comments/{commentId}/replies/{replyId}",
                    "params": {
                        "replyId": {
                            "type": "resolve",
                            "resource": "drive_replies_list",
                            "field": "id",
                        },
                        "fileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commentId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "includeDeleted": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Lists a file's revisions.
            {
                "name": "drive_revisions_list",
                "table_name": "revision",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "revisions",
                    "path": "/files/{fileId}/revisions",
                    "params": {
                        "fileId": {
                            "type": "resolve",
                            "resource": "drive_files_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets a revision's metadata or content by ID.
            {
                "name": "drive_revisions_get",
                "table_name": "revision",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/files/{fileId}/revisions/{revisionId}",
                    "params": {
                        "revisionId": {
                            "type": "resolve",
                            "resource": "drive_revisions_list",
                            "field": "id",
                        },
                        "fileId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "acknowledgeAbuse": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Gets the starting pageToken for listing future changes.
            {
                "name": "drive_changes_get_start_page_token",
                "table_name": "start_page_token",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/changes/startPageToken",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "driveId": "OPTIONAL_CONFIG",
                        # "supportsAllDrives": "OPTIONAL_CONFIG",
                        # "supportsTeamDrives": "OPTIONAL_CONFIG",
                        # "teamDriveId": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Deprecated: Use `drives.list` instead.
            {
                "name": "drive_teamdrives_list",
                "table_name": "team_drive",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "teamDrives",
                    "path": "/teamdrives",
                    "params": {
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                        # "pageToken": "OPTIONAL_CONFIG",
                        # "q": "OPTIONAL_CONFIG",
                        # "useDomainAdminAccess": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Deprecated: Use `drives.get` instead.
            {
                "name": "drive_teamdrives_get",
                "table_name": "team_drive",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teamdrives/{teamDriveId}",
                    "params": {
                        "teamDriveId": {
                            "type": "resolve",
                            "resource": "drive_teamdrives_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "useDomainAdminAccess": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
