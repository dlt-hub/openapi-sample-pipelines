from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="osi_api_source", max_table_nesting=2)
def osi_api_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # #### Returns A JSON object with `meta` and `links` keys.  The `meta` key contains information such as a welcome message from the API, the specified version of the request, and the full representation of the current user, if authentication credentials were provided in the request.  The `links` key contains links to the following entity collections: [addons](#tag/Addons), [collections](), [institutions](#tag/Institutions), [licenses](#tag/Licenses), [registration schemas](#tag/Registration Schemas), [nodes](#tag/Nodes), [registrations](#tag/Registrations), [users](#tag/Users)
            {
                "name": "base_read",
                "table_name": "",
                "endpoint": {
                    "path": "/",
                    "paginator": "auto",
                },
            },
            #  A paginated list of addon accounts authorized by this user.  #### Permissions  Addon accounts are visible only to the user that authorized the account.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of at most 10 addon account objects. Each resource in the array is a separate  addon account object and contains the full representation of the addon account.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "users_addon_accounts_list",
                "table_name": "account",
                "endpoint": {
                    "path": "/users/{user_id}/addons/{provider}/accounts/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of an addon account  #### Permissions  Addon accounts are visible only to the user that authorized the account.  #### Returns Returns a JSON object with a `data` key containing the representation of the requested addon account, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "users_addon_accounts_read",
                "table_name": "account",
                "endpoint": {
                    "path": "/users/{user_id}/addons/{provider}/accounts/{account_id}/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "account_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A log can have one of many actions. The complete list of loggable actions (in the format {identifier}: {description}) is as follows: * `project_created`: A Node is created * `project_registered`: A Node is registered * `project_deleted`: A Node is deleted * `created_from`: A Node is created using an existing Node as a template * `pointer_created`: A Pointer is created * `pointer_forked`: A Pointer is forked * `pointer_removed`: A Pointer is removed * `node_removed`: A component is deleted * `node_forked`: A Node is forked --- * `made_public`: A Node is made public * `made_private`: A Node is made private * `tag_added`: A tag is added to a Node * `tag_removed`: A tag is removed from a Node * `edit_title`: A Node's title is changed * `edit_description`: A Node's description is changed * `updated_fields`: One or more of a Node's fields are changed * `external_ids_added`: An external identifier is added to a Node (e.g. DOI, ARK) * `view_only_link_added`: A view-only link was added to a Node * `view_only_link_removed`:  A view-only link was removed from a Node --- * `contributor_added`: A Contributor is added to a Node * `contributor_removed`: A Contributor is removed from a Node * `contributors_reordered`: A Contributor's position in a Node's bibliography is changed * `permissions_updated`: A Contributor`s permissions on a Node are changed * `made_contributor_visible`: A Contributor is made bibliographically visible on a Node * `made_contributor_invisible`: A Contributor is made bibliographically invisible on a Node --- * `wiki_updated`: A Node's wiki is updated * `wiki_deleted`: A Node's wiki is deleted * `wiki_renamed`: A Node's wiki is renamed * `made_wiki_public`: A Node's wiki is made public * `made_wiki_private`: A Node's wiki is made private --- * `addon_added`: An add-on is linked to a Node * `addon_removed`: An add-on is unlinked from a Node * `addon_file_moved`: A File in a Node's linked add-on is moved * `addon_file_copied`: A File in a Node's linked add-on is copied * `addon_file_renamed`: A File in a Node's linked add-on is renamed * `node_authorized`: An addon is authorized for a project * `node_deauthorized`: An addon is deauthorized for a project * `folder_created`: A Folder is created in a Node's linked add-on * `file_added`: A File is added to a Node's linked add-on * `file_updated`: A File is updated on a Node's linked add-on * `file_removed`: A File is removed from a Node's linked add-on * `file_restored`: A File is restored in a Node's linked add-on --- * `comment_added`: A Comment is added to some item * `comment_removed`: A Comment is removed from some item * `comment_updated`: A Comment is updated on some item --- * `embargo_initiated`: An embargoed Registration is proposed on a Node * `embargo_approved`: A proposed Embargo of a Node is approved * `embargo_cancelled`: A proposed Embargo of a Node is cancelled * `embargo_completed`: A proposed Embargo of a Node is completed * `retraction_initiated`: A Withdrawal of a Registration is proposed * `retraction_approved`: A Withdrawal of a Registration is approved * `retraction_cancelled`: A Withdrawal of a Registration is cancelled * `registration_initiated`: A Registration of a Node is proposed * `registration_approved`: A proposed Registration is approved * `registration_cancelled`: A proposed Registration is cancelled
            {
                "name": "logs_actions",
                "table_name": "action",
                "endpoint": {
                    "path": "/actions/",
                    "paginator": "auto",
                },
            },
            # This retrieves a paginated list of all Schema Response Actions created for a Schema Response. #### Returns Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "schema_response_action_read",
                "table_name": "action",
                "endpoint": {
                    "path": "/schema_responses/{schema_response_id}/actions/",
                    "params": {
                        "schema_response_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a Schema Response Action by it's ID. #### Returns Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "schema_response_action_read",
                "table_name": "action",
                "endpoint": {
                    "path": "/schema_responses/{schema_response_id}/actions/{schema_response_action_id}",
                    "params": {
                        "schema_response_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "schema_response_action_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns a list of the actions that have changed the Collection Submission moderation state. #### Permissions This information is only available to an admin or moderator of a Collection when it is private, however if the Collection is public the data is available to all. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_submission_list",
                "table_name": "action",
                "endpoint": {
                    "path": "/collection_submissions/{collection_submission_id}/actions/",
                    "params": {
                        "collection_submission_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of addons configurable with the OSF, for read purposes only. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.
            {
                "name": "addons_list",
                "table_name": "addon",
                "endpoint": {
                    "path": "/addons/",
                    "paginator": "auto",
                },
            },
            #  A paginated list of addons connected to the given node or project. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of at most 10 addon objects. Each resource in the array is a separate addon object and contains the full representation of the addon, meaning additional requests to a addon's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "nodes_addons_list",
                "table_name": "addon",
                "endpoint": {
                    "path": "/nodes/{node_id}/addons/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve details of an individual addon connected to this node. #### Permissions NodeSettings that are attached to public nodes will give read-only access to everyone. Private nodes require explicit read permission. Write and admin access are the same for public and private nodes. Administrators on a parent node have implicit read permissions for all child nodes. Any users with write or admin access to the node are able to deauthorize an enabled addon, but only the addon authorizer is able to change the configuration (i.e. selected folder) of an already-configured NodeSettings entity. #### Returns Returns a JSON object with a `data` key containing the details of the requested addon, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_addon_read",
                "table_name": "addon",
                "endpoint": {
                    "path": "/nodes/{node_id}/addons/{provider}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of authorized user addons  #### Permissions  User addons are visible only to the user that authorized the addon.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 addons. Each resource in the array is a separate addon object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.
            {
                "name": "users_addons_list",
                "table_name": "addon",
                "endpoint": {
                    "path": "/users/{user_id}/addons/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of an authorized user addon  #### Permissions  User addons are visible only to the user that authorized the addon.  #### Returns Returns a JSON object with a `data` key containing the representation of the requested user addon, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.
            {
                "name": "users_addons_read",
                "table_name": "addon",
                "endpoint": {
                    "path": "/users/{user_id}/addons/{provider}/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of the Preprint's Bibliographic Contributors, sorted by their index. Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.  Contributors may be filtered by their `bibliographic` and `permission` attributes.
            {
                "name": "preprints_bibliographic_contributors_list",
                "table_name": "bibliographic_contributor",
                "endpoint": {
                    "path": "/preprints/{preprint_id}/bibliographic_contributors/",
                    "params": {
                        "preprint_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the next level child nodes for the given node. The returned nodes are sorted by their `date_modified`, with the most recently updated child nodes appearing first.  The list will include child nodes that are public, as well as child nodes that are private, if the authenticated user has permission to view them. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 child nodes. If the given node has zero child nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the child node, meaning additional requests to the child node's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/children/?filter[title]=reproducibility.  Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.  Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.
            {
                "name": "nodes_children_list",
                "table_name": "child",
                "endpoint": {
                    "path": "/nodes/{node_id}/children/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of children of a registration.  The list consists of the next level child registrations for the given registration. The returned registrations are sorted by their `date_modified`, with the most recently updated child registrations appearing first.  The list will include child registrations that are public, as well as child registrations that are private, if the authenticated user has permission to view them. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 child registrations. If the given registration has zero child registrations, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the child registration.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/children/?filter[title]=reproducibility.  Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.  Most fields are string fields and will be filtered using simple substring matching. Public is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.
            {
                "name": "registrations_children_list",
                "table_name": "child",
                "endpoint": {
                    "path": "/registrations/{registration_id}/children/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # The citation details for a node, in CSL format. #### Returns Returns a JSON object with a `data` key that contains the representation of the details necessary for the node citation.
            {
                "name": "nodes_citation_list",
                "table_name": "citation",
                "endpoint": {
                    "path": "/nodes/{node_id}/citation/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # The citation for a node in a specific style. #### Returns Returns a JSON object with a `data` key that contains the representation of the node citation, in the requested style.
            {
                "name": "nodes_citation_read",
                "table_name": "citation",
                "endpoint": {
                    "path": "/nodes/{node_id}/citation/{style_id}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "style_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # The citation details for a preprint, in CSL format. #### Returns Returns a JSON object with a `data` key that contains the representation of the details necessary for the preprint citation.
            {
                "name": "preprints_citation_list",
                "table_name": "citation",
                "endpoint": {
                    "path": "/preprints/{preprint_id}/citation/",
                    "params": {
                        "preprint_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # The citation for a preprint in a specific style. #### Returns Returns a JSON object with a `data` key that contains the representation of the preprint citation, in the requested style.
            {
                "name": "preprints_citation_read",
                "table_name": "citation",
                "endpoint": {
                    "path": "/preprints/{preprint_id}/citation/{style_id}/",
                    "params": {
                        "preprint_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "style_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the registration's alternative citation styles  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 citation styles. Each resource in the array is a separate citation styles object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/citations/?filter[title]=open.  Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`.
            {
                "name": "registrations_citations_list",
                "table_name": "citation",
                "endpoint": {
                    "path": "/registrations/{registration_id}/citations/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the citation style details for a registration, in CSL format. #### Returns Returns a JSON object with a `data` key that contains the representation of the details necessary for the citation style.
            {
                "name": "registrations_citation_read",
                "table_name": "citation",
                "endpoint": {
                    "path": "/registrations/{registration_id}/citations/{citation_id}/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "citation_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of user created metadata for entities within a collection. #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.
            {
                "name": "collections_metadata_registrations_list",
                "table_name": "collected_metadatum",
                "endpoint": {
                    "path": "/collections/{collection_id}/collected_metadata/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  #### Permissions In order to view this metadata it must be public or a user must have read permissions for collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.
            {
                "name": "collections_metadata_registrations_detail",
                "table_name": "collected_metadatum",
                "endpoint": {
                    "path": "/collections/{collection_id}/collected_metadata/{cgm_id}",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cgm_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list collections, either public or related to the user #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing `data` and `links` keys. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_list",
                "table_name": "collection",
                "endpoint": {
                    "path": "/collections/",
                    "paginator": "auto",
                },
            },
            # Retrieves a collection, if the user has appropriate permissions.  #### Permissions Anonymous users are able to see all public collections at this endpoint. Logged in users will only be able to see their own content. #### Returns Returns a JSON object containing `data` and `links` keys.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_detail",
                "table_name": "collection",
                "endpoint": {
                    "path": "/collections/{collection_id}/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns a list of the Collections Providers. #### Permissions This information is public. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of collection provider ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_provider_list",
                "table_name": "collection",
                "endpoint": {
                    "path": "/provider/collections/",
                    "paginator": "auto",
                },
            },
            #  This returns a single Collections Provider entity. #### Permissions This information is public. #### Returns Returns a JSON object containing `data` and `links` keys. Returns a JSON object with a `data` key containing the representation of the requested collection provider object, if the request is successful.
            {
                "name": "collection_provider_detail",
                "table_name": "collection",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  #### Permissions This information is only available to an admin on the Collection Submission in question. #### Returns Returns a JSON object containing `data` and `links` keys.  Returns a JSON object with a `data` key containing the representation of the requested collection submission action object, if the request is successful.
            {
                "name": "collection_submission_actions",
                "table_name": "collection_submission_action",
                "endpoint": {
                    "path": "/collection_submission_actions/{collection_submission_id}/",
                    "params": {
                        "collection_submission_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a comment #### Returns Returns a JSON object with a `data` key containing the representation of the requested comment, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "comments_read",
                "table_name": "comment",
                "endpoint": {
                    "path": "/comments/{comment_id}/",
                    "params": {
                        "comment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of comments related to a given node.  The returned comments are sorted by their creation date, with the most recent comments appearing first. #### Permissions Comments on public nodes are given read-only access to everyone.  If the node comment-level is `private`, only contributors have permission to comment.  If the comment-level is `public`, any logged-in OSF user can comment.  Comments on private nodes are only visible to contributors and administrators on the parent node. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/comments/?filter[target_id]=jg7sezmdnt93  Nodes may be filtered by their `deleted`, `target_id`, `date_created`, `date_modified`.  Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.
            {
                "name": "nodes_comments_list",
                "table_name": "comment",
                "endpoint": {
                    "path": "/nodes/{node_id}/comments/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the registration's comments.  The returned comments are sorted by their creation date, with the most recent comments appearing first. #### Permissions Comments of public registrations are given read-only access to everyone.  If the comment-level is `private`, only registration contributors have permission to comment.  If the comment-level is `public`, any logged-in OSF user can comment.  Comments of private registrations are only visible to contributors and administrators on the registration. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of comment objects. Each resource in the array is a separate comment object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include comments that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wuerf/comments/?filter[target]=wuerf  Comments may be filtered by their `deleted`, `target`, `date_created`, `date_modified`.  Most fields are string fields and will be filtered using simple substring matching. Deleted is a boolean field, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting `true` or `false` in the query will cause the match to fail.
            {
                "name": "registrations_comments_list",
                "table_name": "comment",
                "endpoint": {
                    "path": "/registrations/{registration_id}/comments/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the plaintext content of a wiki in markdown format. #### Returns Returns `text/markdown` of the wiki content itself. If the request is unsuccessful, plaintext with the error message will be displayed.
            {
                "name": "wiki_content",
                "table_name": "content",
                "endpoint": {
                    "path": "/wikis/{wiki_id}/content/",
                    "params": {
                        "wiki_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of the node's contributors, sorted by their index.  Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.  Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/y9jdt/contributors/?filter[bibliographic]=true.  Contributors may be filtered by their `bibliographic` and `permission` attributes.
            {
                "name": "nodes_contributors_list",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/nodes/{node_id}/contributors/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a given contributor.  Contributors are users who can make changes to the node or, in the case of private nodes, have read access to the node.  Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not. #### Returns Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_contributors_read",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/nodes/{node_id}/contributors/{user_id}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of the Preprint's Contributors, sorted by their index.  Contributors are users who can make changes to the Preprint. Contributors with WRITE permissions may edit preprint details, and ADMIN Contributors may add or remove other Contributors.  Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of Contributors, the user relationship will not be exposed and the Contributor ID will be an empty string.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 contributors. Each resource in the array contains the full representation of the contributor, meaning additional requests to a contributor's detail view are not necessary. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/y9jdt/contributors/?filter[bibliographic]=true.  Contributors may be filtered by their `bibliographic` and `permission` attributes.
            {
                "name": "preprints_contributors_list",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/preprints/{preprint_id}/contributors/",
                    "params": {
                        "preprint_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a contributor on this Preprint. Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string. #### Returns Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "preprints_contributor_read",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/preprints/{preprint_id}/contributors/{user_id}/",
                    "params": {
                        "preprint_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of all contributors on this registration. The returned contributors are sorted by their index.  Contributors are users who can make changes to the registration or, in the case of private registration, have read access to the registration.  Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed in the contributors list on the OSF, while non-bibliographic contributors are not.  Note that if an anonymous view_only key is being used to view the list of contributors, the user relationship will not be exposed and the contributor ID will be an empty string.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 contributors. Each resource in the array contains the full representation of the contributor. Additionally, the full representation of the user this contributor represents is automatically embedded within the `data` key of the response.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include contributors that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/contributors/?filter[bibliographic]=true.  Contributors may be filtered by their `bibliographic` and `permission` attributes.
            {
                "name": "registrations_contributors_list",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/registrations/{registration_id}/contributors/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a contributor on this registration.  #### Returns Returns a JSON object with a `data` key containing the representation of the requested contributor, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "registrations_contributors_read",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/registrations/{registration_id}/contributors/{user_id}/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of all given Contributors for a Draft Registration. Contributors are users who can make changes to the Draft Registration. Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
            {
                "name": "draft_registration_contributors_list",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/draft_registrations/{draft_id}/contributors/",
                    "params": {
                        "draft_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a given contributor.  Contributors are users who can view or edit to the Draft Registrations.  Contributors are categorized as either "bibliographic" or "non-bibliographic". From a permissions standpoint, both are the same, but bibliographic contributors are included in citations and are listed on the project overview page on the OSF, while non-bibliographic contributors are not.
            {
                "name": "draft_registration_contributors_create",
                "table_name": "contributor",
                "endpoint": {
                    "path": "/draft_registrations/{draft_id}/contributors/{user_id}/",
                    "params": {
                        "draft_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of all of the draft registrations of a given node.  Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.  Your original project remains editable but will now have the draft registration linked to it. #### Permissions Only project administrators may view draft registrations. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 draft registrations. Each resource in the array is a separate draft registration object and contains the full representation of the draft registration, meaning additional requests to a draft registration's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "nodes_draft_registrations_list",
                "table_name": "draft_registration",
                "endpoint": {
                    "path": "/nodes/{node_id}/draft_registrations/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve the details of a given draft registration. Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.  Your original project remains editable but will now have the draft registration linked to it. #### Permissions Only project administrators may view draft registrations. #### Returns Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_draft_registrations_read",
                "table_name": "draft_registration",
                "endpoint": {
                    "path": "/nodes/{node_id}/draft_registrations/{draft_id}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "draft_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a list of all currently available Draft Registrations for that user. #### Permissions Only Draft Registration contributors may view draft registrations. #### Returns Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "draft_registrations_read",
                "table_name": "draft_registration",
                "endpoint": {
                    "path": "/draft_registrations/",
                    "paginator": "auto",
                },
            },
            # Retrieve the details of a given Draft Registration Draft Registrations contain Registration questions that will become part of the Registration. A Registration is a frozen version of the project that can never be deleted, but can be withdrawn and have it's metadata edited.  If you based your Draft Registration on a Project, your original Project remains editable but will now have the Draft Registration linked to it. #### Permissions Only draft registration contributors may view draft registrations. #### Returns Returns a JSON object with a `data` key containing the representation of the requested draft registration, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_draft_registrations_read",
                "table_name": "draft_registration",
                "endpoint": {
                    "path": "/draft_registrations/{draft_id}/",
                    "params": {
                        "draft_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a file (or folder) #### Returns Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. ### Waterbutler API actions  Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).  #### Download (files)  To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.  #### Create Subfolder (folders)  You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.  #### Upload New File (folders)     To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.   #### Update Existing File (file)  To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.  #### Rename (files, folders)  To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.  #### Move & Copy (files, folders)  Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name. Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers. If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.  #### Delete (file, folders)  To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.
            {
                "name": "files_detail",
                "table_name": "file",
                "endpoint": {
                    "path": "/files/{file_id}/",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all storage providers that are configured for this node  Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.   #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of files. Each resource in the array is a separate file object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.
            {
                "name": "nodes_providers_list",
                "table_name": "file",
                "endpoint": {
                    "path": "/nodes/{node_id}/files/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all the files/folders that are attached to your project for a given storage provider. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Filtering  You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/files/osfstorage/?filter[kind]=file  Node files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.  ### Waterbutler API actions  Files can be modified through the Waterbutler API routes found in `links` (`new_folder`, `move`, `upload`, `download`, and `delete`).  #### Download (files)  To download a file, issue a GET request against the download link. The response will have the Content-Disposition header set, which will will trigger a download in a browser.  #### Create Subfolder (folders)  You can create a subfolder of an existing folder by issuing a PUT request against the new_folder link. The ?kind=folder portion of the query parameter is already included in the new_folder link. The name of the new subfolder should be provided in the name query parameter. The response will contain a WaterButler folder entity. If a folder with that name already exists in the parent directory, the server will return a 409 Conflict error response.  #### Upload New File (folders)  To upload a file to a folder, issue a PUT request to the folder's upload link with the raw file data in the request body, and the kind and name query parameters set to 'file' and the desired name of the file. The response will contain a WaterButler file entity that describes the new file. If a file with the same name already exists in the folder, the server will return a 409 Conflict error response.  #### Update Existing File (file)  To update an existing file, issue a PUT request to the file's upload link with the raw file data in the request body and the kind query parameter set to "file". The update action will create a new version of the file. The response will contain a WaterButler file entity that describes the updated file.  #### Rename (files, folders)  To rename a file or folder, issue a POST request to the move link with the action body parameter set to "rename" and the rename body parameter set to the desired name. The response will contain either a folder entity or file entity with the new name.  #### Move & Copy (files, folders)  Move and copy actions both use the same request structure, a POST to the move url, but with different values for the action body parameters. The path parameter is also required and should be the OSF path attribute of the folder being written to. The rename and conflict parameters are optional. If you wish to change the name of the file or folder at its destination, set the rename parameter to the new name. The conflict param governs how name clashes are resolved. Possible values are replace and keep. replace is the default and will overwrite the file that already exists in the target folder. keep will attempt to keep both by adding a suffix to the new file's name until it no longer conflicts. The suffix will be ' (x)' where x is a increasing integer starting from 1. This behavior is intended to mimic that of the OS X Finder. The response will contain either a folder entity or file entity with the new name. Files and folders can also be moved between nodes and providers. The resource parameter is the id of the node under which the file/folder should be moved. It must agree with the path parameter, that is the path must identify a valid folder under the node identified by resource. Likewise, the provider parameter may be used to move the file/folder to another storage provider, but both the resource and path parameters must belong to a node and folder already extant on that provider. Both resource and provider default to the current node and providers. If a moved/copied file is overwriting an existing file, a 200 OK response will be returned. Otherwise, a 201 Created will be returned.  #### Delete (file, folders)  To delete a file or folder send a DELETE request to the delete link. Nothing will be returned in the response body.
            {
                "name": "nodes_files_list",
                "table_name": "file",
                "endpoint": {
                    "path": "/nodes/{node_id}/files/{provider}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a file attached to given node (project or component) for the given storage provider. #### Returns Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_files_read",
                "table_name": "file",
                "endpoint": {
                    "path": "/nodes/{node_id}/files/{provider}/{path}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of storage providers enabled on the registration  Users of the OSF may access their data on a [number of cloud-storage services](https://api.osf.io/v2/#storage-providers) that have integrations with the OSF. We call these **providers**. By default, every node has access to the OSF-provided storage but may use as many of the supported providers as desired.   #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 files. Each resource in the array is a separate file object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  Note: In the OSF filesystem model, providers are treated as folders, but with special properties that distinguish them from regular folders. Every provider folder is considered a root folder, and may not be deleted through the regular file API.
            {
                "name": "registrations_providers_list",
                "table_name": "file",
                "endpoint": {
                    "path": "/registrations/{registration_id}/files/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all the registration's files/folders for a given storage provider.  #### Returns  Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of files. Each resource in the array is a separate file object and contains the full representation of the file.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Filtering  You can optionally request that the response only include files that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/files/osfstorage/?filter[kind]=file  Files may be filtered by `id`, `name`, `node`, `kind`, `path`, `provider`, `size`, and `last_touched`.
            {
                "name": "registrations_files_list",
                "table_name": "file",
                "endpoint": {
                    "path": "/registrations/{registration_id}/files/{provider}/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a registration file for the given storage provider. #### Returns Returns a JSON object with a `data` key containing the representation of the requested registration file object, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "registrations_files_read",
                "table_name": "file",
                "endpoint": {
                    "path": "/registrations/{registration_id}/files/{provider}/{path}/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of folders retrieved from the associated third-party (provider) service. #### Permissions Folders are visible only to the user that authorized the addon. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of addon folder objects. Each resource in the array is a separate addon folder object and contains the full representation of the addon folder, meaning additional requests to a addon folder's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "nodes_addons_folders_list",
                "table_name": "folder",
                "endpoint": {
                    "path": "/nodes/{node_id}/addons/{provider}/folders/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the current node's forks. The returned fork nodes are sorted by their `forked_date`, with the most recently forked nodes appearing first.  Forking a project creates a copy of an existing node and all of its contents. The fork always points back to the original node, forming a network of nodes. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 forked nodes. If the current node has zero forked nodes, the `data` key will contain an empty array. Each resource in the array is a separate node object and contains the full representation of the forked node, meaning additional requests to the forked node's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error.
            {
                "name": "nodes_forks_list",
                "table_name": "fork",
                "endpoint": {
                    "path": "/nodes/{node_id}/forks/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the registration’s forks  The returned forks are sorted by their `forked_date`, with the most recent forks appearing first.  Forking a registration creates a copy of an existing registration and all of its contents. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 forks. If the current registration has no fork, the `data` key will contain an empty array. Each resource in the array is a separate registration object and contains the full representation of the registration's fork.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "registrations_forks_list",
                "table_name": "fork",
                "endpoint": {
                    "path": "/registrations/{registration_id}/forks/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns a list of highlighted subjects for a Collections Provider. #### Permissions This information is public. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of subject ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_provider_detail",
                "table_name": "highlighted",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/subjects/highlighted/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List all identifiers associated with a given node. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering  You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/identifiers/?filter[category]=ark  Identifiers may be filtered by their `category` e.g `ark` or `doi`.
            {
                "name": "nodes_identifiers_list",
                "table_name": "identifier",
                "endpoint": {
                    "path": "/nodes/{node_id}/identifiers/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of the registration's identifiers. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of identifiers. Each resource in the array is a separate identifier object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering  You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/identifiers/?filter[category]=ark  Identifiers may be filtered by their `category` e.g `ark` or `doi`.
            {
                "name": "registrations_identifiers_list",
                "table_name": "identifier",
                "endpoint": {
                    "path": "/registrations/{registration_id}/identifiers/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of all verified institutions. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 institutions. Each resource in the array is a separate institution object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include institutions that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/?filter[id]=cos.  Institutions may be filtered by their `id`, `name`, and `auth_url`
            {
                "name": "institutions_list",
                "table_name": "institution",
                "endpoint": {
                    "path": "/institutions/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of an institution #### Returns Returns a JSON object with a `data` key containing the representation of the requested institution, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "institutions_detail",
                "table_name": "institution",
                "endpoint": {
                    "path": "/institutions/{institution_id}/",
                    "params": {
                        "institution_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all institutions affiliated with this node. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 affilited institutions. Each resource in the array is a separate institution object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "nodes_institutions_list",
                "table_name": "institution",
                "endpoint": {
                    "path": "/nodes/{node_id}/institutions/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of institutions affiliated with the registration. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 affiliated institutions. Each resource in the array is a separate institution object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "registrations_institutions_list",
                "table_name": "institution",
                "endpoint": {
                    "path": "/registrations/{registration_id}/institutions/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Once a properly authenticated user has marked their registration as affiliated with an institution, that institution and any others added will appear in this list.
            {
                "name": "nodes_draft_registrations_read",
                "table_name": "institution",
                "endpoint": {
                    "path": "/draft_registrations/{draft_id}/institutions/",
                    "params": {
                        "draft_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of institutions that the user is affiliated with. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 institutions. Each resource in the array is a complete institution object and contains the full representation of the institution, meaning additional requests to a institution's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "users_institutions_list",
                "table_name": "institution",
                "endpoint": {
                    "path": "/users/{user_id}/institutions/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of licenses. The returned licenses are sorted by their name. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 licenses. Each resource in the array is a separate license object and contains the full representation of the license, meaning additional requests to a license's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include licenses that match your filters by utilizing the `filter` query parameter, e.g. [https://api.osf.io/v2/licenses/?filter[name]=apache](https://api.osf.io/v2/licenses/?filter[name]=apache).  Licenses may be filtered by their `id`, and `name`.
            {
                "name": "license_list",
                "table_name": "license",
                "endpoint": {
                    "path": "/licenses/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a license. #### Returns Returns a JSON object with a `data` key containing the representation of the requested license, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "licenses_read",
                "table_name": "license",
                "endpoint": {
                    "path": "/license/{license_id}/",
                    "params": {
                        "license_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the licenses allowed by a preprint provider. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "preprint_provider_licenses_list",
                "table_name": "license",
                "endpoint": {
                    "path": "/preprint_providers/{preprint_provider_id}/licenses/",
                    "params": {
                        "preprint_provider_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns the lists of possible licenses for a Collection. #### Permissions This information is public. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of license ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_provider_detail",
                "table_name": "license",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/licenses/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all nodes linked to the given node. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.  Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.
            {
                "name": "nodes_linked_nodes_list",
                "table_name": "linked_node",
                "endpoint": {
                    "path": "/nodes/{node_id}/linked_nodes/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all nodes linked to the registration. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/linked_nodes/?filter[title]=reproducibility/?filter[title]=reproducibility.  Nodes may be filtered by their `title`, `category`, `description`, `public`, `registration`, or `tags`. `title`, `description`, and `category` are string fields and will be filteres using simple substring matching. `public`, `registration` are boolean and can be filtered using truthy values, such as `true`, `false`, `0`, `1`. `tags` is an array of simple strings.
            {
                "name": "registrations_linked_nodes_list",
                "table_name": "linked_node",
                "endpoint": {
                    "path": "/registrations/{registration_id}/linked_nodes/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all nodes linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_linked_nodes_list",
                "table_name": "linked_node",
                "endpoint": {
                    "path": "/collections/{collection_id}/linked_nodes",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all preprints linked to the given collection. #### Permissions This returns all public preprints associated with this collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_linked_preprints_list",
                "table_name": "linked_preprint",
                "endpoint": {
                    "path": "/collections/{collection_id}/linked_preprints/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all registrations linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_linked_registrations_list",
                "table_name": "linked_registration",
                "endpoint": {
                    "path": "/collections/{collection_id}/linked_registrations/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a log. A log is permanent immutable record of a node's history. A log is created when a user performs one of many actions. See the [actions](#Logs_logs_actions) section for more details. #### Returns Returns a JSON object with a `data` key containing the representation of the requested log, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "logs_read",
                "table_name": "log",
                "endpoint": {
                    "path": "/logs/{log_id}/",
                    "params": {
                        "log_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of all logs associated with a given node.  The returned logs are sorted by their `date`, with the most recents logs appearing first.  This list includes the logs of the specified node as well as the logs of that node's children to which the current user has read-only access.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/logs/?filter[action]=made_private.  Nodes may be filtered by their `action`, and `date`.
            {
                "name": "nodes_logs_list",
                "table_name": "log",
                "endpoint": {
                    "path": "/nodes/{node_id}/logs/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of the registration's logs.  The returned logs are sorted by their `date`, with the most recents logs appearing first.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 logs. Each resource in the array is a separate logs object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include logs that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wucr8/logs/?filter[action]=made_private.  Logs may be filtered by their `action`, and `date`.
            {
                "name": "registrations_logs_list",
                "table_name": "log",
                "endpoint": {
                    "path": "/registrations/{registration_id}/logs/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns a list of moderators for a Collections Provider. #### Permissions This information is only available to Collection Provider moderators or admins. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of moderator ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_provider_detail",
                "table_name": "moderator",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/moderators/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns details for a moderator of a Collections Provider. #### Permissions This information is only available to Collection Provider moderators or admins. #### Returns Returns a JSON object containing `data` and `links` keys. Returns a JSON object with a `data` key containing the representation of the requested collection provider moderator object, if the request is successful.
            {
                "name": "collection_provider_detail",
                "table_name": "moderator",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/moderators/{moderator_id}/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "moderator_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of all nodes affiliated with an institution. #### Versioning As of version `2.2`, affiliated components (in addition to affiliated top-level projects) are returned from this endpoint. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 nodes. Each resource in the array is a separate nodes object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/nodes?filter[title]=science.  Nodes may be filtered by their `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`
            {
                "name": "institutions_node_list",
                "table_name": "node",
                "endpoint": {
                    "path": "/institutions/{institution_id}/nodes/",
                    "params": {
                        "institution_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of nodes, representing projects and components, on the OSF.  The returned nodes are those which are public or which the user has access to view.  The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.  Registrations cannot be accessed through this endpoint (use the [registrations](#tag/Registrations) endpoints instead). #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/?filter[title]=reproducibility.  Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.  Most fields are string fields and will be filtered using simple substring matching. Public and preprint are boolean fields, and can be filtered using truthy values, such as **true**, **false**, **0** or **1**. Note that quoting true or false in the query will cause the match to fail.
            {
                "name": "nodes_list",
                "table_name": "node",
                "endpoint": {
                    "path": "/nodes/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a given node (project or component). #### Permissions Only project contributors may retrieve the details of a private node. Attempting to retreive a private node for which you are not a contributor will result in a **403 Forbidden** response.  Authentication is not required to view the details of a public node, as public nodes give read-only access to everyone. #### Returns Returns a JSON object with a `data` key containing the representation of the requested node, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_read",
                "table_name": "node",
                "endpoint": {
                    "path": "/nodes/{node_id}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of nodes that the user is a contributor to. The returned nodes are sorted by their `date_modified`, with the most recently updated nodes appearing first.  If the user ID in the path is the same as the logged-in user, all nodes will be returned. Otherwise, only the user's public nodes will be returned.  User registrations are not available at this endpoint. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/nodes/?filter[title]=open.  Nodes may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, `preprint`, and `contributors`.
            {
                "name": "users_nodes_list",
                "table_name": "node",
                "endpoint": {
                    "path": "/users/{user_id}/nodes/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  The list of nodes which this view only link gives read-only access to. #### Permissions Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "view_only_links_node_list",
                "table_name": "node",
                "endpoint": {
                    "path": "/view_only_links/{link_id}/nodes/",
                    "params": {
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of preprints related to a given node. The returned preprints are sorted by their creation date, with the most recent preprints appearing first.  **Note: This API endpoint is under active development, and is subject to change in the future.** #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 preprints. Each resource in the array is a separate preprint object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "nodes_preprints_list",
                "table_name": "preprint",
                "endpoint": {
                    "path": "/nodes/{node_id}/preprints/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of preprints from all preprint providers. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprints/?filter[provider]=socarxiv.  Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.
            {
                "name": "preprints_list",
                "table_name": "preprint",
                "endpoint": {
                    "path": "/preprints/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a preprint. #### Returns Returns a JSON object with a `data` key containing the representation of the requested preprint, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "preprints_read",
                "table_name": "preprint",
                "endpoint": {
                    "path": "/preprints/{preprint_id}/",
                    "params": {
                        "preprint_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of preprints from the specified preprint provider. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 preprints. Each resource in the array is a separate preprint object.  The `links` key contains a dictionary with keys that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/osf/preprints/?filter[is_published]=true.  Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.
            {
                "name": "preprint_providers_preprints_list",
                "table_name": "preprint",
                "endpoint": {
                    "path": "/preprint_providers/{preprint_provider_id}/preprints/",
                    "params": {
                        "preprint_provider_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of preprints that the user contributes to. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 preprints. Each resource in the array is a complete preprint object and contains the full representation of the preprint, meaning additional requests to a preprint's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/preprints/?filter[provider]=psyarxiv.  Preprints may be filtered by their `id`, `is_published`, `date_created`, `date_modified`, and `provider`.
            {
                "name": "users_preprints_list",
                "table_name": "preprint",
                "endpoint": {
                    "path": "/users/{user_id}/preprints/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of all preprint providers. The returned preprint providers are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include preprint providers that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/preprint_providers/?filter[id]=osf.  Preprint Providers may be filtered by their `id`, `name`,  and `description`
            {
                "name": "preprint_provider_list",
                "table_name": "preprint_provider",
                "endpoint": {
                    "path": "/preprint_providers/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a preprint provider. #### Returns Returns a JSON object with a `data` key containing the representation of the requested preprint provider, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  #### Acceptable Subjects Structure Each preprint provider specifies acceptable subjects. `subjects_acceptable` is an array found in `attributes`. Subjects consist of general parent subjects (e.g., Engineering), more specific child subjects (e.g., Aerospace Engineering), and even more specific grandchild subjects (e.g., Aerodynamics and Fluid Mechanics). Subjects can only be nested 3 deep.       "subjects_acceptable": [         [             [                 # Parent Subject:                 # Architecture                 "584240d954be81056ceca9e5",                  # Child Subject:                 # Architectural Engineering                 "584240da54be81056cecac87"             ],             # Include all Architectural Engineering's children:             true         ],         [             [                 # Parent Subject:                 # Engineering                 "584240da54be81056cecaca9",                  # Child Subject:                 # Aerospace Engineering                 "584240db54be81056cecacd6",                  # Grandchild Subject:                 # Aerodynamics and Fluid Mechanics                 "584240da54be81056cecaa74"             ],             # All nestings 3 deep must be false             false         ]     ]  The above structure would allow Architecture, Architectural Engineering, all of Architectural Engineering's children, Engineering, Aerospace Engineering, and Aerodynamics and Fluid Mechanics.
            {
                "name": "preprint_provider_detail",
                "table_name": "preprint_provider",
                "endpoint": {
                    "path": "/preprint_providers/{preprint_provider_id}/",
                    "params": {
                        "preprint_provider_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a storage provider enabled on this node. #### Returns Returns a JSON object with a `data` key containing the representation of the requested file object, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "nodes_providers_read",
                "table_name": "provider",
                "endpoint": {
                    "path": "/nodes/{node_id}/files/providers/{provider}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "provider": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of all registrations affiliated with an institution. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 registrations. Each resource in the array is a separate users object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/registrations?filter[title]=science.  Registrations may be filtered by their  `id`, `title`, `description`, `public`, `tags`, `category`, `date_created`, `date_modified`, `root`, `parent`, `contributors`, and `preprint`
            {
                "name": "institutions_registration_list",
                "table_name": "registration",
                "endpoint": {
                    "path": "/institutions/{institution_id}/registrations/",
                    "params": {
                        "institution_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieve a paginated list of all active Registration Schemas. Registration Schemas describe the supplemental questions that accompany a registration. Registration Schemas are read-only for API users. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Registration Schemas. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.
            {
                "name": "registration_schemas_list",
                "table_name": "registration",
                "endpoint": {
                    "path": "/schemas/registrations/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a given Registration Schema. Registration Schemas defines the desired supplemental information that should accompany be included in a Registration. Registration Schemas are Read-only to API users. #### Returns Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "registration_schema_read",
                "table_name": "registration",
                "endpoint": {
                    "path": "/schemas/registrations/{registration_schema_id}",
                    "params": {
                        "registration_schema_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all registrations of the given node. #### Returns  Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 registrations. Each resource in the array is a separate registrations object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering  You can optionally request that the response only include registrations that match your filters by utilizing the filter query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.  Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.
            {
                "name": "nodes_registrations_list",
                "table_name": "registration",
                "endpoint": {
                    "path": "/nodes/{node_id}/registrations/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of registrations on the OSF to which the user has access.  The returned registrations are those which are public or which the user has access to view.  Non-registered nodes cannot be accessed through this endpoint (use the [nodes](#Nodes_nodes_list) endpoints instead).  #### Registrations A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.  Registrations can be made public immediately or embargoed for up to 4 years.  #### Withdrawals Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/?filter[title]=open.  Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.
            {
                "name": "registrations_list",
                "table_name": "registration",
                "endpoint": {
                    "path": "/registrations/",
                    "paginator": "auto",
                },
            },
            # Retrieve the details of a given registration. #### Permissions Only project contributors may retrieve the details of a registration that is embargoed, or has not yet been made public. Attempting to retrieve a private registration for which you are not a contributor will result in a **403 Forbidden** response.  Authentication is not required to view the details of a public registration, as public registrations give read-only access to everyone. #### Registrations A registration on the OSF creates a frozen, time-stamped version of a project that cannot be edited or deleted. The *original project* can still be edited, while the registered version cannot.  Registrations can be made public immediately or embargoed for up to 4 years.  #### Withdrawals Registrations cannot be deleted, but they can be withdrawn. Withdrawing a registration removes the content of the registration but leaves behind basic metadata. A withdrawn registration will display a limited subset of information, namely, title, description, date_created, date_registered, date_withdrawn, registration, withdrawn, withdrawal_justification, and registration supplement. All other fields will be displayed as null. Additionally, the only relationship that remains accesible for a withdrawn registration is the contributors. All other relationships will return a **403 Forbidden** response. #### Returns Returns a JSON object with a `data` key containing the representation of the requested registration, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "registrations_read",
                "table_name": "registration",
                "endpoint": {
                    "path": "/registrations/{registration_id}/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of registrations that the user is a contributor to. The returned registrations are sorted by their `date_modified`, with the most recently updated registrations appearing first.  If the user ID in the path is the same as the logged-in user, all registrations will be returned. Otherwise, only the user's public registrations will be returned.  User nodes are not available at this endpoint. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/cdi38/registrations/?filter[title]=replication.  Registrations may be filtered by their `id`, `title`, `category`, `description`, `public`, `tags`, `date_created`, `date_modified`, `root`, `parent`, and `contributors`.
            {
                "name": "users_registrations_list",
                "table_name": "registration",
                "endpoint": {
                    "path": "/users/{user_id}/registrations/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all the node ids linked to the given collection. #### Permissions This returns all public nodes associated with this collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_linked_nodes_relationships_create",
                "table_name": "relationship",
                "endpoint": {
                    "path": "/collections/{collection_id}/linked_nodes/relationships/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of all the registration ids linked to the given collection. #### Permissions This returns all public registrations associated with this collection. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_linked_registrations_relationships_create",
                "table_name": "relationship",
                "endpoint": {
                    "path": "/collections/{collection_id}/linked_registrations/relationships/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This returns a list of all the Registration Schema Blocks are contained in Registration Schema. #### Returns Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "schema_response_blocks_read",
                "table_name": "schema_block",
                "endpoint": {
                    "path": "/schema_responses/{schema_response_id}/schema_blocks/",
                    "params": {
                        "schema_response_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This returns a Registration Schema Block by it's ID. #### Returns Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "schema_response_blocks_read",
                "table_name": "schema_block",
                "endpoint": {
                    "path": "/schema_responses/{schema_response_id}/schema_blocks/{schema_response_block_id}",
                    "params": {
                        "schema_response_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "schema_response_block_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This retrieves a paginated list of all active Schema Responses that are public. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error.
            {
                "name": "schema_responses_list",
                "table_name": "schema_response",
                "endpoint": {
                    "path": "/schema_responses/",
                    "paginator": "auto",
                },
            },
            # This retrieves a single Schema response using it's id. #### Returns Returns a JSON object with a `data` key containing the representation of the requested Schema Response, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "schema_responses_read",
                "table_name": "schema_response",
                "endpoint": {
                    "path": "/schema_responses/{schema_response_id}",
                    "params": {
                        "schema_response_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of all standard citation styles available for rendering citations. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 citation styles. Each resource in the array is a separate citation syle and contains the full representation of the citation style object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include citation styles that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/citations/styles/?filter[title]=open.  Citation styles may be filtered by their `id`, `title`, `short-title`, and `summary`. #### Errors This request should never return an error.
            {
                "name": "citations_styles_list",
                "table_name": "style",
                "endpoint": {
                    "path": "/citations/styles/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a citation style. #### Returns Returns a JSON object with a `data` key containing the representation of the requested citation style, if the request is successful. #### Errors If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "citations_styles_read",
                "table_name": "style",
                "endpoint": {
                    "path": "/citations/styles/{style_id}/",
                    "params": {
                        "style_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This retrieves a list of subjects associated with a Draft Registration. Subjects are formatted here in a flat paginated list, but are hierarchical and nested by specificity of subject matter.
            {
                "name": "nodes_draft_registrations_subjects",
                "table_name": "subject",
                "endpoint": {
                    "path": "/draft_registrations/{draft_id}/subjects/",
                    "params": {
                        "draft_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  #### Permissions In order to view these subject it must be a public collection or a user must have read permissions for collection.  #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Errors This request should never return an error, other then permissions errors.
            {
                "name": "collections_collected_metadata",
                "table_name": "subject",
                "endpoint": {
                    "path": "/collections/{collection_id}/collected_metadata/{cgm_id}/subjects/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cgm_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  #### Permissions This is public for a logged out user when an entity is public. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of nodes ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collections_metadata_subjects_relationships",
                "table_name": "subject",
                "endpoint": {
                    "path": "/collections/{collection_id}/collected_metadata/{cgm_id}/relationships/subjects/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cgm_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns a list of acceptable subjects for a Collections Provider. #### Permissions This information is public. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of subject ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_provider_detail",
                "table_name": "subject",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/subjects/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  This returns a list of all submissions to a Collections Provider entity. #### Permissions This information is public. #### Returns Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of node and preprint ids. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
            {
                "name": "collection_provider_detail",
                "table_name": "submission",
                "endpoint": {
                    "path": "/provider/collections/{collection_id}/submissions/",
                    "params": {
                        "collection_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of the taxonomies for a preprint provider. The returned preprint providers taxonomies are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 preprint providers. Each resource in the array is a separate preprint provider object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "preprint_provider_taxonomies_list",
                "table_name": "taxonomy",
                "endpoint": {
                    "path": "/preprint_providers/{preprint_provider_id}/taxonomies/",
                    "params": {
                        "preprint_provider_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of all [bepress disciplines taxonomies](https://www.bepress.com/wp-content/uploads/2016/12/Digital-Commons-Disciplines-taxonomy-2017-01.pdf). Note: this API endpoint is under active development, and is subject to change in the future. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 taxonomies. Each resource in the array is a separate taxonomy object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include taxonomies that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/taxonomies/?filter['id']='{taxonomy_id}'.  Taxonomies may be filtered by their `id`, `parents`, and `text`.
            {
                "name": "taxonomies_list",
                "table_name": "taxonomy",
                "endpoint": {
                    "path": "/taxonomies/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a taxonomy. #### Returns  Returns a JSON object with a `data` key containing the representation of the requested taxonomy, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "taxonomies_read",
                "table_name": "taxonomy",
                "endpoint": {
                    "path": "/taxonomies/{taxonomy_id}/",
                    "params": {
                        "taxonomy_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of all users affiliated with an institution. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 users. Each resource in the array is a separate users object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering You can optionally request that the response only include users that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/institutions/cos/users?filter[family_name]=Nosek.  Users may be filtered by their `id`, `full_name`, `given_name`, `middle_names`, and `family_name`
            {
                "name": "institutions_users_list",
                "table_name": "user",
                "endpoint": {
                    "path": "/institutions/{institution_id}/users/",
                    "params": {
                        "institution_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of all users registered on the OSF. The returned users are sorted by their `date_registered`, with the most recently registered users appearing first.  The subroute `/users/me/` is a special endpoint that always points to the currently logged-in user. #### Versioning As of version `2.3`, merged users will not be returned from this endpoint. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 users. Each resource in the array is a separate users object and contains the full representation of the user, meaning additional requests to a user's detail view are not necessary.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/users/?filter[family_name]=Nosek.  Users may be filtered by their `id`, `full_name`, `given_name`, `middle_name`, or `family_name`.
            {
                "name": "users_list",
                "table_name": "user",
                "endpoint": {
                    "path": "/users/",
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a given users.  The returned information includes the user's bibliographic information and the date the user was registered.  Additionally, relationships to the list of institutions with which the user is affiliated, and to the list of nodes which the user contributes to (that the requesting user has permission to see) are returned.  If `me` is given as the `user_id` in the request path, the record of the currently logged-in user will be returned. #### Returns Returns a JSON object with a `data` key containing the representation of the requested user, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "users_read",
                "table_name": "user",
                "endpoint": {
                    "path": "/users/{user_id}/",
                    "params": {
                        "user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #  A paginated list of all file versions. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of 10 file versions. Each resource in the array is a separate file version object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "files_versions",
                "table_name": "version",
                "endpoint": {
                    "path": "/files/{file_id}/versions/",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a file version #### Returns  Returns a JSON object with a `data` key containing the representation of the requested file, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "files_version_detail",
                "table_name": "version",
                "endpoint": {
                    "path": "/files/{file_id}/versions/{version_id}/",
                    "params": {
                        "file_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "version_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of view only links on a node. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Permissions  View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.  #### Filtering  You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/nodes/ezcuj/view_only_links/?filter[anonymous]=true.  View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
            {
                "name": "nodes_view_only_links_list",
                "table_name": "view_only_link",
                "endpoint": {
                    "path": "/nodes/{node_id}/view_only_links/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a view only link on a node. #### Returns Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Permissions  View only links on a node, public or private, are readable and writeable only by users that are administrators on the node.
            {
                "name": "nodes_view_only_links_read",
                "table_name": "view_only_link",
                "endpoint": {
                    "path": "/nodes/{node_id}/view_only_links/{link_id}/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of view only links created for this registration. #### Returns Returns a JSON object containing `data` and `links` keys.  The `data` key contains an array of up to 10 view only links. Each resource in the array is a view only link object.  The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  #### Permissions  View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.  #### Filtering  You can optionally request that the response only include view only links that match your filters by utilizing the `filter` query parameter, e.g. https://api.osf.io/v2/registrations/wu3a4/view_only_links/?filter[anonymous]=true.  View Only Links may be filtered based on their `name`, `anonymous` and `date_created` fields. Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
            {
                "name": "registrations_view_only_links_list",
                "table_name": "view_only_link",
                "endpoint": {
                    "path": "/registrations/{registration_id}/view_only_links/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details of a view only link created from this registration. #### Returns Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Permissions  View only links on a registration, public or private, are readable and writeable only by users that are administrators on the registration.
            {
                "name": "registrations_view_only_links_read",
                "table_name": "view_only_link",
                "endpoint": {
                    "path": "/registrations/{registration_id}/view_only_links/{link_id}/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details about a specific view only link. #### Permissions Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object with a `data` key containing the representation of the requested view only link, if the request is successful. If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "view_only_links_read",
                "table_name": "view_only_link",
                "endpoint": {
                    "path": "/view_only_links/{link_id}/",
                    "params": {
                        "link_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List of wiki pages on a node. #### Returns Paginated list of the node's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.  Note that if an anonymous view_only key is being used, the user relationship will not be exposed.  If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering Wiki pages can be filtered based on their `name` and `date_modified` fields. + `filter[name]=<Str>` -- filter wiki pages by name + `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.  Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
            {
                "name": "nodes_wikis_list",
                "table_name": "wiki",
                "endpoint": {
                    "path": "/nodes/{node_id}/wikis/",
                    "params": {
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A paginated list of the registration's wiki pages #### Returns A list of all registration's current wiki page versions ordered by their date_modified. Each resource contains the full representation of the wiki, meaning additional requests to an individual wiki's detail view are not necessary.  If the request is unsuccessful, a JSON object with an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed. #### Filtering Wiki pages can be filtered based on their `name` and `date_modified` fields. + `filter[name]=<Str>` -- filter wiki pages by name + `filter[date_modified][comparison_operator]=YYYY-MM-DDTH:M:S` -- filter wiki pages based on date modified.  Possible comparison operators include 'gt' (greater than), 'gte'(greater than or equal to), 'lt' (less than) and 'lte' (less than or equal to). The date must be in the format YYYY-MM-DD and the time is optional.
            {
                "name": "registrations_wikis_list",
                "table_name": "wiki",
                "endpoint": {
                    "path": "/registrations/{registration_id}/wikis/",
                    "params": {
                        "registration_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the details about a specific wiki. A wiki is a collection of markdown text pages that can be used to describe the project or dataset of contained in the attached node. #### Returns Returns a JSON object with a `data` key containing the representation of the requested wiki, if the request was successful.  If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.
            {
                "name": "wiki_read",
                "table_name": "wiki",
                "endpoint": {
                    "path": "/wikis/{wiki_id}/",
                    "params": {
                        "wiki_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
