# google_drive pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/google_drive.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /about_ 
  *resource*: drive_about_get  
  *description*: Gets information about the user, the user's Drive, and system capabilities.
* _GET /apps_ 
  *resource*: drive_apps_list  
  *description*: Lists a user's installed apps.
* _GET /apps/{appId}_ 
  *resource*: drive_apps_get  
  *description*: Gets a specific app.
* _GET /changes_ 
  *resource*: drive_changes_list  
  *description*: Lists the changes for a user or shared drive.
* _GET /files/{fileId}/comments_ 
  *resource*: drive_comments_list  
  *description*: Lists a file's comments.
* _GET /files/{fileId}/comments/{commentId}_ 
  *resource*: drive_comments_get  
  *description*: Gets a comment by ID.
* _GET /drives_ 
  *resource*: drive_drives_list  
  *description*:  Lists the user's shared drives. This method accepts the `q` parameter, which is a search query combining one or more search terms. For more information, see the [Search for shared drives](/drive/api/guides/search-shareddrives) guide.
* _GET /drives/{driveId}_ 
  *resource*: drive_drives_get  
  *description*: Gets a shared drive's metadata by ID.
* _GET /files/{fileId}/export_ 
  *resource*: drive_files_export  
  *description*: Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.
* _GET /files_ 
  *resource*: drive_files_list  
  *description*:  Lists the user's files. This method accepts the `q` parameter, which is a search query combining one or more search terms. For more information, see the [Search for files & folders](/drive/api/guides/search-files) guide. *Note:* This method returns *all* files by default, including trashed files. If you don't want trashed files to appear in the list, use the `trashed=false` query parameter to remove trashed files from the results.
* _GET /files/{fileId}_ 
  *resource*: drive_files_get  
  *description*:  Gets a file's metadata or content by ID. If you provide the URL parameter `alt=media`, then the response includes the file contents in the response body. Downloading content with `alt=media` only works if the file is stored in Drive. To download Google Docs, Sheets, and Slides use [`files.export`](/drive/api/reference/rest/v3/files/export) instead. For more information, see [Download & export files](/drive/api/guides/manage-downloads).
* _GET /files/generateIds_ 
  *resource*: drive_files_generate_ids  
  *description*: Generates a set of file IDs which can be provided in create or copy requests.
* _GET /files/{fileId}/listLabels_ 
  *resource*: drive_files_list_labels  
  *description*: Lists the labels on a file.
* _GET /files/{fileId}/permissions_ 
  *resource*: drive_permissions_list  
  *description*: Lists a file's or shared drive's permissions.
* _GET /files/{fileId}/permissions/{permissionId}_ 
  *resource*: drive_permissions_get  
  *description*: Gets a permission by ID.
* _GET /files/{fileId}/comments/{commentId}/replies_ 
  *resource*: drive_replies_list  
  *description*: Lists a comment's replies.
* _GET /files/{fileId}/comments/{commentId}/replies/{replyId}_ 
  *resource*: drive_replies_get  
  *description*: Gets a reply by ID.
* _GET /files/{fileId}/revisions_ 
  *resource*: drive_revisions_list  
  *description*: Lists a file's revisions.
* _GET /files/{fileId}/revisions/{revisionId}_ 
  *resource*: drive_revisions_get  
  *description*: Gets a revision's metadata or content by ID.
* _GET /changes/startPageToken_ 
  *resource*: drive_changes_get_start_page_token  
  *description*: Gets the starting pageToken for listing future changes.
* _GET /teamdrives_ 
  *resource*: drive_teamdrives_list  
  *description*: Deprecated: Use `drives.list` instead.
* _GET /teamdrives/{teamDriveId}_ 
  *resource*: drive_teamdrives_get  
  *description*: Deprecated: Use `drives.get` instead.
