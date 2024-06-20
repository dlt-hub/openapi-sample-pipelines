from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="bitbucket_source", max_table_nesting=2)
def bitbucket_source(
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
                "name": "Authorization",
                "location": "header",
            },
            "paginator": {
                "type": "json_response",
                "next_url_path": "next",
            },
        },
        "resources": [
            # Returns the repository's default reviewers.  These are the users that are automatically added as reviewers on every new pull request that is created. To obtain the repository's default reviewers as well as the default reviewers inherited from the project, use the [effective-default-reveiwers](#api-repositories-workspace-repo-slug-effective-default-reviewers-get) endpoint.
            {
                "name": "get_repositoriesworkspacerepo_slugdefault_reviewers",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/default-reviewers",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified reviewer.  This can be used to test whether a user is among the repository's default reviewers list. A 404 indicates that that specified user is not a default reviewer.
            {
                "name": "get_repositoriesworkspacerepo_slugdefault_reviewerstarget_username",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/default-reviewers/{target_username}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "target_username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all the watchers on the specified repository.
            {
                "name": "get_repositoriesworkspacerepo_slugwatchers",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/watchers",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all users watching a specific snippet.
            {
                "name": "get_snippetsworkspaceencoded_idwatchers",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/snippets/{workspace}/{encoded_id}/watchers",
                    "params": {
                        "encoded_id": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the currently logged in user.
            {
                "name": "get_user",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user",
                },
            },
            # Gets the public information associated with a user account.  If the user's profile is private, `location`, `website` and `created_on` elements are omitted.  Note that the user object returned by this operation is changing significantly, due to privacy changes. See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#changes-to-bitbucket-user-objects) for details.
            {
                "name": "get_usersselected_user",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{selected_user}",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of the pull request's activity log.  This handler serves both a v20 and internal endpoint. The v20 endpoint returns reviewer comments, updates, approvals and request changes. The internal endpoint includes those plus tasks and attachments.  Comments created on a file or a line of code have an inline property.  Comment example: ``` {     "pagelen": 20,     "values": [         {             "comment": {                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695/comments/118571088"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695/_/diff#comment-118571088"                     }                 },                 "deleted": false,                 "pullrequest": {                     "type": "pullrequest",                     "id": 5695,                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                         },                         "html": {                             "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                         }                     },                     "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"                 },                 "content": {                     "raw": "inline with to a dn from lines",                     "markup": "markdown",                     "html": "<p>inline with to a dn from lines</p>",                     "type": "rendered"                 },                 "created_on": "2019-09-27T00:33:46.039178+00:00",                 "user": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 },                 "created_on": "2019-09-27T00:33:46.039178+00:00",                 "user": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 },                 "updated_on": "2019-09-27T00:33:46.055384+00:00",                 "inline": {                     "context_lines": "",                     "to": null,                     "path": "",                     "outdated": false,                     "from": 211                 },                 "type": "pullrequest_comment",                 "id": 118571088             },             "pull_request": {                 "type": "pullrequest",                 "id": 5695,                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                     }                 },                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"             }         }     ] } ```  Updates include a state property of OPEN, MERGED, or DECLINED.  Update example: ``` {     "pagelen": 20,     "values": [         {             "update": {                 "description": "",                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it",                 "destination": {                     "commit": {                         "type": "commit",                         "hash": "6a2c16e4a152",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/commits/6a2c16e4a152"                             }                         }                     },                     "branch": {                         "name": "master"                     },                     "repository": {                         "name": "Atlaskit-MK-2",                         "type": "repository",                         "full_name": "atlassian/atlaskit-mk-2",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2"                             },                             "avatar": {                                 "href": "https://bytebucket.org/ravatar/%7B%7D?ts=js"                             }                         },                         "uuid": "{}"                     }                 },                 "reason": "",                 "source": {                     "commit": {                         "type": "commit",                         "hash": "728c8bad1813",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/commits/728c8bad1813"                             }                         }                     },                     "branch": {                         "name": "username/NONE-add-onClick-prop-for-accessibility"                     },                     "repository": {                         "name": "Atlaskit-MK-2",                         "type": "repository",                         "full_name": "atlassian/atlaskit-mk-2",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2"                             },                             "avatar": {                                 "href": "https://bytebucket.org/ravatar/%7B%7D?ts=js"                             }                         },                         "uuid": "{}"                     }                 },                 "state": "OPEN",                 "author": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 },                 "date": "2019-05-10T06:48:25.305565+00:00"             },             "pull_request": {                 "type": "pullrequest",                 "id": 5695,                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                     }                 },                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"             }         }     ] } ```  Approval example: ``` {     "pagelen": 20,     "values": [         {             "approval": {                 "date": "2019-09-27T00:37:19.849534+00:00",                 "pullrequest": {                     "type": "pullrequest",                     "id": 5695,                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                         },                         "html": {                             "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                         }                     },                     "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"                 },                 "user": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 }             },             "pull_request": {                 "type": "pullrequest",                 "id": 5695,                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                     }                 },                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"             }         }     ] } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestsactivity",
                "table_name": "activity",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/activity",
                    "params": {
                        "repo_slug": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of the pull request's activity log.  This handler serves both a v20 and internal endpoint. The v20 endpoint returns reviewer comments, updates, approvals and request changes. The internal endpoint includes those plus tasks and attachments.  Comments created on a file or a line of code have an inline property.  Comment example: ``` {     "pagelen": 20,     "values": [         {             "comment": {                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695/comments/118571088"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695/_/diff#comment-118571088"                     }                 },                 "deleted": false,                 "pullrequest": {                     "type": "pullrequest",                     "id": 5695,                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                         },                         "html": {                             "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                         }                     },                     "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"                 },                 "content": {                     "raw": "inline with to a dn from lines",                     "markup": "markdown",                     "html": "<p>inline with to a dn from lines</p>",                     "type": "rendered"                 },                 "created_on": "2019-09-27T00:33:46.039178+00:00",                 "user": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 },                 "created_on": "2019-09-27T00:33:46.039178+00:00",                 "user": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 },                 "updated_on": "2019-09-27T00:33:46.055384+00:00",                 "inline": {                     "context_lines": "",                     "to": null,                     "path": "",                     "outdated": false,                     "from": 211                 },                 "type": "pullrequest_comment",                 "id": 118571088             },             "pull_request": {                 "type": "pullrequest",                 "id": 5695,                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                     }                 },                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"             }         }     ] } ```  Updates include a state property of OPEN, MERGED, or DECLINED.  Update example: ``` {     "pagelen": 20,     "values": [         {             "update": {                 "description": "",                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it",                 "destination": {                     "commit": {                         "type": "commit",                         "hash": "6a2c16e4a152",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/6a2c16e4a152"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/commits/6a2c16e4a152"                             }                         }                     },                     "branch": {                         "name": "master"                     },                     "repository": {                         "name": "Atlaskit-MK-2",                         "type": "repository",                         "full_name": "atlassian/atlaskit-mk-2",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2"                             },                             "avatar": {                                 "href": "https://bytebucket.org/ravatar/%7B%7D?ts=js"                             }                         },                         "uuid": "{}"                     }                 },                 "reason": "",                 "source": {                     "commit": {                         "type": "commit",                         "hash": "728c8bad1813",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/commit/728c8bad1813"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/commits/728c8bad1813"                             }                         }                     },                     "branch": {                         "name": "username/NONE-add-onClick-prop-for-accessibility"                     },                     "repository": {                         "name": "Atlaskit-MK-2",                         "type": "repository",                         "full_name": "atlassian/atlaskit-mk-2",                         "links": {                             "self": {                                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2"                             },                             "html": {                                 "href": "https://bitbucket.org/atlassian/atlaskit-mk-2"                             },                             "avatar": {                                 "href": "https://bytebucket.org/ravatar/%7B%7D?ts=js"                             }                         },                         "uuid": "{}"                     }                 },                 "state": "OPEN",                 "author": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 },                 "date": "2019-05-10T06:48:25.305565+00:00"             },             "pull_request": {                 "type": "pullrequest",                 "id": 5695,                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                     }                 },                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"             }         }     ] } ```  Approval example: ``` {     "pagelen": 20,     "values": [         {             "approval": {                 "date": "2019-09-27T00:37:19.849534+00:00",                 "pullrequest": {                     "type": "pullrequest",                     "id": 5695,                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                         },                         "html": {                             "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                         }                     },                     "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"                 },                 "user": {                     "display_name": "Name Lastname",                     "uuid": "{}",                     "links": {                         "self": {                             "href": "https://api.bitbucket.org/2.0/users/%7B%7D"                         },                         "html": {                             "href": "https://bitbucket.org/%7B%7D/"                         },                         "avatar": {                             "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/:/128"                         }                     },                     "type": "user",                     "nickname": "Name",                     "account_id": ""                 }             },             "pull_request": {                 "type": "pullrequest",                 "id": 5695,                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/atlaskit-mk-2/pullrequests/5695"                     },                     "html": {                         "href": "https://bitbucket.org/atlassian/atlaskit-mk-2/pull-requests/5695"                     }                 },                 "title": "username/NONE: small change from onFocus to onClick to handle tabbing through the page and not expand the editor unless a click event triggers it"             }         }     ] } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idactivity",
                "table_name": "activity",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/activity",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.
            {
                "name": "get_commit_hosted_property_value",
                "table_name": "application_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "app_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "property_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.
            {
                "name": "get_repository_hosted_property_value",
                "table_name": "application_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "app_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "property_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.
            {
                "name": "get_pull_request_hosted_property_value",
                "table_name": "application_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name}",
                    "params": {
                        "property_name": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pullrequest_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "app_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a user.
            {
                "name": "retrieve_user_hosted_property_value",
                "table_name": "application_property",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{selected_user}/properties/{app_key}/{property_name}",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "app_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "property_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the contents of the specified file attachment.  Note that this endpoint does not return a JSON response, but instead returns a redirect pointing to the actual file that in turn will return the raw contents.  The redirect URL contains a one-time token that has a limited lifetime. As a result, the link should not be persisted, stored, or shared.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idattachmentspath",
                "table_name": "attachment",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "issue_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of `git log`. Like these tools, the DAG can be filtered.  #### GET /repositories/{workspace}/{repo_slug}/commits/  Returns all commits in the repo in topological order (newest commit first). All branches and tags are included (similar to `git log --all`).  #### GET /repositories/{workspace}/{repo_slug}/commits/?exclude=master  Returns all commits in the repo that are not on master (similar to `git log --all ^master`).  #### GET /repositories/{workspace}/{repo_slug}/commits/?include=foo&include=bar&exclude=fu&exclude=fubar  Returns all commits that are on refs `foo` or `bar`, but not on `fu` or `fubar` (similar to `git log foo bar ^fu ^fubar`).  An optional `path` parameter can be specified that will limit the results to commits that affect that path. `path` can either be a file or a directory. If a directory is specified, commits are returned that have modified any file in the directory tree rooted by `path`. It is important to note that if the `path` parameter is specified, the commits returned by this endpoint may no longer be a DAG, parent commits that do not modify the path will be omitted from the response.  #### GET /repositories/{workspace}/{repo_slug}/commits/?path=README.md&include=foo&include=bar&exclude=master  Returns all commits that are on refs `foo` or `bar`, but not on `master` that changed the file README.md.  #### GET /repositories/{workspace}/{repo_slug}/commits/?path=src/&include=foo&include=bar&exclude=master  Returns all commits that are on refs `foo` or `bar`, but not on `master` that changed to a file in any file in the directory src or its children.  Because the response could include a very large number of commits, it is paginated. Follow the 'next' link in the response to navigate to the next page of commits. As with other paginated resources, do not construct your own links.  When the include and exclude parameters are more than can fit in a query string, clients can use a `x-www-form-urlencoded` POST instead.
            {
                "name": "get_repositoriesworkspacerepo_slugcommits",
                "table_name": "base_commit",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commits",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # These are the repository's commits. They are paginated and returned in reverse chronological order, similar to the output of `git log`. Like these tools, the DAG can be filtered.  #### GET /repositories/{workspace}/{repo_slug}/commits/master  Returns all commits on ref `master` (similar to `git log master`).  #### GET /repositories/{workspace}/{repo_slug}/commits/dev?include=foo&exclude=master  Returns all commits on ref `dev` or `foo`, except those that are reachable on `master` (similar to `git log dev foo ^master`).  An optional `path` parameter can be specified that will limit the results to commits that affect that path. `path` can either be a file or a directory. If a directory is specified, commits are returned that have modified any file in the directory tree rooted by `path`. It is important to note that if the `path` parameter is specified, the commits returned by this endpoint may no longer be a DAG, parent commits that do not modify the path will be omitted from the response.  #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=README.md&include=foo&include=bar&exclude=master  Returns all commits that are on refs `dev` or `foo` or `bar`, but not on `master` that changed the file README.md.  #### GET /repositories/{workspace}/{repo_slug}/commits/dev?path=src/&include=foo&exclude=master  Returns all commits that are on refs `dev` or `foo`, but not on `master` that changed to a file in any file in the directory src or its children.  Because the response could include a very large number of commits, it is paginated. Follow the 'next' link in the response to navigate to the next page of commits. As with other paginated resources, do not construct your own links.  When the include and exclude parameters are more than can fit in a query string, clients can use a `x-www-form-urlencoded` POST instead.
            {
                "name": "get_repositoriesworkspacerepo_slugcommitsrevision",
                "table_name": "base_commit",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commits/{revision}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "revision": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of all open branches within the specified repository.         Results will be in the order the source control manager returns them.          ```         $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1 | jq .         {           "pagelen": 1,           "size": 187,           "values": [             {               "name": "issue-9.3/AUI-5343-assistive-class",               "links": {                 "commits": {                   "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/issue-9.3/AUI-5343-assistive-class"                 },                 "self": {                   "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/issue-9.3/AUI-5343-assistive-class"                 },                 "html": {                   "href": "https://bitbucket.org/atlassian/aui/branch/issue-9.3/AUI-5343-assistive-class"                 }               },               "default_merge_strategy": "squash",               "merge_strategies": [                 "merge_commit",                 "squash",                 "fast_forward"               ],               "type": "branch",               "target": {                 "hash": "e5d1cde9069fcb9f0af90403a4de2150c125a148",                 "repository": {                   "links": {                     "self": {                       "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui"                     },                     "html": {                       "href": "https://bitbucket.org/atlassian/aui"                     },                     "avatar": {                       "href": "https://bytebucket.org/ravatar/%7B585074de-7b60-4fd1-81ed-e0bc7fafbda5%7D?ts=86317"                     }                   },                   "type": "repository",                   "name": "aui",                   "full_name": "atlassian/aui",                   "uuid": "{585074de-7b60-4fd1-81ed-e0bc7fafbda5}"                 },                 "links": {                   "self": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1cde9069fcb9f0af90403a4de2150c125a148"                   },                   "comments": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1cde9069fcb9f0af90403a4de2150c125a148/comments"                   },                   "patch": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e5d1cde9069fcb9f0af90403a4de2150c125a148"                   },                   "html": {                     "href": "https://bitbucket.org/atlassian/aui/commits/e5d1cde9069fcb9f0af90403a4de2150c125a148"                   },                   "diff": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e5d1cde9069fcb9f0af90403a4de2150c125a148"                   },                   "approve": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1cde9069fcb9f0af90403a4de2150c125a148/approve"                   },                   "statuses": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e5d1cde9069fcb9f0af90403a4de2150c125a148/statuses"                   }                 },                 "author": {                   "raw": "Marcin Konopka <mkonopka@atlassian.com>",                   "type": "author",                   "user": {                     "display_name": "Marcin Konopka",                     "uuid": "{47cc24f4-2a05-4420-88fe-0417535a110a}",                     "links": {                       "self": {                         "href": "https://api.bitbucket.org/2.0/users/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D"                       },                       "html": {                         "href": "https://bitbucket.org/%7B47cc24f4-2a05-4420-88fe-0417535a110a%7D/"                       },                       "avatar": {                         "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/initials/MK-1.png"                       }                     },                     "nickname": "Marcin Konopka",                     "type": "user",                     "account_id": "60113d2b47a9540069f4de03"                   }                 },                 "parents": [                   {                     "hash": "87f7fc92b00464ae47b13ef65c91884e4ac9be51",                     "type": "commit",                     "links": {                       "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/87f7fc92b00464ae47b13ef65c91884e4ac9be51"                       },                       "html": {                         "href": "https://bitbucket.org/atlassian/aui/commits/87f7fc92b00464ae47b13ef65c91884e4ac9be51"                       }                     }                   }                 ],                 "date": "2021-04-13T13:44:49+00:00",                 "message": "wip ",                 "type": "commit"               }             }           ],           "page": 1,           "next": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches?pagelen=1&page=2"         }         ```          Branches support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering)         that can be used to search for specific branches. For instance, to find         all branches that have "stab" in their name:          ```         curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches -G --data-urlencode 'q=name ~ "stab"'         ```          By default, results will be in the order the underlying source control system returns them and identical to         the ordering one sees when running "$ git branch --list". Note that this follows simple         lexical ordering of the ref names.          This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are         sorted ["v10", "v11", "v9"] instead of ["v9", "v10", "v11"].          Sorting can be changed using the ?q= query parameter. When using ?q=name to explicitly sort on ref name,         Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.
            {
                "name": "get_repositoriesworkspacerepo_slugrefsbranches",
                "table_name": "branch",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/refs/branches",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a branch object within the specified repository.          ```         $ curl -s https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master | jq .         {           "name": "master",           "links": {             "commits": {               "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commits/master"             },             "self": {               "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/refs/branches/master"             },             "html": {               "href": "https://bitbucket.org/atlassian/aui/branch/master"             }           },           "default_merge_strategy": "squash",           "merge_strategies": [             "merge_commit",             "squash",             "fast_forward"           ],           "type": "branch",           "target": {             "hash": "e7d158ff7ed5538c28f94cd97a9ad569680fc94e",             "repository": {               "links": {                 "self": {                   "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui"                 },                 "html": {                   "href": "https://bitbucket.org/atlassian/aui"                 },                 "avatar": {                   "href": "https://bytebucket.org/ravatar/%7B585074de-7b60-4fd1-81ed-e0bc7fafbda5%7D?ts=86317"                 }               },               "type": "repository",               "name": "aui",               "full_name": "atlassian/aui",               "uuid": "{585074de-7b60-4fd1-81ed-e0bc7fafbda5}"             },             "links": {               "self": {                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff7ed5538c28f94cd97a9ad569680fc94e"               },               "comments": {                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff7ed5538c28f94cd97a9ad569680fc94e/comments"               },               "patch": {                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/patch/e7d158ff7ed5538c28f94cd97a9ad569680fc94e"               },               "html": {                 "href": "https://bitbucket.org/atlassian/aui/commits/e7d158ff7ed5538c28f94cd97a9ad569680fc94e"               },               "diff": {                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/diff/e7d158ff7ed5538c28f94cd97a9ad569680fc94e"               },               "approve": {                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff7ed5538c28f94cd97a9ad569680fc94e/approve"               },               "statuses": {                 "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/e7d158ff7ed5538c28f94cd97a9ad569680fc94e/statuses"               }             },             "author": {               "raw": "psre-renovate-bot <psre-renovate-bot@atlassian.com>",               "type": "author",               "user": {                 "display_name": "psre-renovate-bot",                 "uuid": "{250a442a-3ab3-4fcb-87c3-3c8f3df65ec7}",                 "links": {                   "self": {                     "href": "https://api.bitbucket.org/2.0/users/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D"                   },                   "html": {                     "href": "https://bitbucket.org/%7B250a442a-3ab3-4fcb-87c3-3c8f3df65ec7%7D/"                   },                   "avatar": {                     "href": "https://secure.gravatar.com/avatar/6972ee037c9f36360170a86f544071a2?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FP-3.png"                   }                 },                 "nickname": "Renovate Bot",                 "type": "user",                 "account_id": "5d5355e8c6b9320d9ea5b28d"               }             },             "parents": [               {                 "hash": "eab868a309e75733de80969a7bed1ec6d4651e06",                 "type": "commit",                 "links": {                   "self": {                     "href": "https://api.bitbucket.org/2.0/repositories/atlassian/aui/commit/eab868a309e75733de80969a7bed1ec6d4651e06"                   },                   "html": {                     "href": "https://bitbucket.org/atlassian/aui/commits/eab868a309e75733de80969a7bed1ec6d4651e06"                   }                 }               }             ],             "date": "2021-04-12T06:44:38+00:00",             "message": "Merged in issue/NONE-renovate-master-babel-monorepo (pull request #2883)  chore(deps): update babel monorepo to v7.13.15 (master)  Approved-by: Chris "Daz" Darroch ",             "type": "commit"           }         }         ```          This call requires authentication. Private repositories require the         caller to authenticate with an account that has appropriate         authorization.          For Git, the branch name should not include any prefixes (e.g.         refs/heads).
            {
                "name": "get_repositoriesworkspacerepo_slugrefsbranchesname",
                "table_name": "branch",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/refs/branches/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugrefsbranches",
                            "field": "name",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return the branching model as applied to the repository. This view is read-only. The branching model settings can be changed using the [settings](#api-repositories-workspace-repo-slug-branching-model-settings-get) API.  The returned object:  1. Always has a `development` property. `development.branch` contains    the actual repository branch object that is considered to be the    `development` branch. `development.branch` will not be present    if it does not exist. 2. Might have a `production` property. `production` will not    be present when `production` is disabled.    `production.branch` contains the actual branch object that is    considered to be the `production` branch. `production.branch` will    not be present if it does not exist. 3. Always has a `branch_types` array which contains all enabled branch    types.  Example body:  ``` {   "development": {     "name": "master",     "branch": {       "type": "branch",       "name": "master",       "target": {         "hash": "16dffcb0de1b22e249db6799532074cf32efe80f"       }     },     "use_mainbranch": true   },   "production": {     "name": "production",     "branch": {       "type": "branch",       "name": "production",       "target": {         "hash": "16dffcb0de1b22e249db6799532074cf32efe80f"       }     },     "use_mainbranch": false   },   "branch_types": [     {       "kind": "release",       "prefix": "release/"     },     {       "kind": "hotfix",       "prefix": "hotfix/"     },     {       "kind": "feature",       "prefix": "feature/"     },     {       "kind": "bugfix",       "prefix": "bugfix/"     }   ],   "type": "branching_model",   "links": {     "self": {       "href": "https://api.bitbucket.org/.../branching-model"     }   } } ```
            {
                "name": "get_repositoriesworkspacerepo_slugbranching_model",
                "table_name": "branching_model",
                "endpoint": {
                    "data_selector": "branch_types",
                    "path": "/repositories/{workspace}/{repo_slug}/branching-model",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return the branching model set at the project level. This view is read-only. The branching model settings can be changed using the [settings](#api-workspaces-workspace-projects-project-key-branching-model-settings-get) API.  The returned object:  1. Always has a `development` property. `development.name` is    the user-specified branch that can be inherited by an individual repository's    branching model. 2. Might have a `production` property. `production` will not    be present when `production` is disabled.    `production.name` is the user-specified branch that can be    inherited by an individual repository's branching model. 3. Always has a `branch_types` array which contains all enabled branch    types.  Example body:  ``` {   "development": {     "name": "master",     "use_mainbranch": true   },   "production": {     "name": "production",     "use_mainbranch": false   },   "branch_types": [     {       "kind": "release",       "prefix": "release/"     },     {       "kind": "hotfix",       "prefix": "hotfix/"     },     {       "kind": "feature",       "prefix": "feature/"     },     {       "kind": "bugfix",       "prefix": "bugfix/"     }   ],   "type": "project_branching_model",   "links": {     "self": {       "href": "https://api.bitbucket.org/.../branching-model"     }   } } ```
            {
                "name": "get_workspacesworkspaceprojectsproject_keybranching_model",
                "table_name": "branching_model",
                "endpoint": {
                    "data_selector": "branch_types",
                    "path": "/workspaces/{workspace}/projects/{project_key}/branching-model",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all branch restrictions on the repository.
            {
                "name": "get_repositoriesworkspacerepo_slugbranch_restrictions",
                "table_name": "branchrestriction",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/branch-restrictions",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a specific branch restriction rule.
            {
                "name": "get_repositoriesworkspacerepo_slugbranch_restrictionsid",
                "table_name": "branchrestriction",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/branch-restrictions/{id}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified commit.  Example:  ``` $ curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a1 {     "rendered": {         "message": {         "raw": "Add a GEORDI_OUTPUT_DIR setting",         "markup": "markdown",         "html": "<p>Add a GEORDI_OUTPUT_DIR setting</p>",         "type": "rendered"         }     },     "hash": "f7591a13eda445d9a9167f98eb870319f4b6c2d8",     "repository": {         "name": "geordi",         "type": "repository",         "full_name": "bitbucket/geordi",         "links": {             "self": {                 "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi"             },             "html": {                 "href": "https://bitbucket.org/bitbucket/geordi"             },             "avatar": {                 "href": "https://bytebucket.org/ravatar/%7B85d08b4e-571d-44e9-a507-fa476535aa98%7D?ts=1730260"             }         },         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"     },     "links": {         "self": {             "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8"         },         "comments": {             "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8/comments"         },         "patch": {             "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/patch/f7591a13eda445d9a9167f98eb870319f4b6c2d8"         },         "html": {             "href": "https://bitbucket.org/bitbucket/geordi/commits/f7591a13eda445d9a9167f98eb870319f4b6c2d8"         },         "diff": {             "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diff/f7591a13eda445d9a9167f98eb870319f4b6c2d8"         },         "approve": {             "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8/approve"         },         "statuses": {             "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f7591a13eda445d9a9167f98eb870319f4b6c2d8/statuses"         }     },     "author": {         "raw": "Brodie Rao <a@b.c>",         "type": "author",         "user": {             "display_name": "Brodie Rao",             "uuid": "{9484702e-c663-4afd-aefb-c93a8cd31c28}",             "links": {                 "self": {                     "href": "https://api.bitbucket.org/2.0/users/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D"                 },                 "html": {                     "href": "https://bitbucket.org/%7B9484702e-c663-4afd-aefb-c93a8cd31c28%7D/"                 },                 "avatar": {                     "href": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca/613070db-28b0-421f-8dba-ae8a87e2a5c7/128"                 }             },             "type": "user",             "nickname": "brodie",             "account_id": "557058:3aae1e05-702a-41e5-81c8-f36f29afb6ca"         }     },     "summary": {         "raw": "Add a GEORDI_OUTPUT_DIR setting",         "markup": "markdown",         "html": "<p>Add a GEORDI_OUTPUT_DIR setting</p>",         "type": "rendered"     },     "participants": [],     "parents": [         {             "type": "commit",             "hash": "f06941fec4ef6bcb0c2456927a0cf258fa4f899b",             "links": {                 "self": {                     "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/commit/f06941fec4ef6bcb0c2456927a0cf258fa4f899b"                 },                 "html": {                     "href": "https://bitbucket.org/bitbucket/geordi/commits/f06941fec4ef6bcb0c2456927a0cf258fa4f899b"                 }             }         }     ],     "date": "2012-07-16T19:37:54+00:00",     "message": "Add a GEORDI_OUTPUT_DIR setting",     "type": "commit" } ```
            {
                "name": "get_repositoriesworkspacerepo_slugcommitcommit",
                "table_name": "commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the best common ancestor between two commits, specified in a revspec of 2 commits (e.g. 3a8b42..9ff173).  If more than one best common ancestor exists, only one will be returned. It is unspecified which will be returned.
            {
                "name": "get_repositoriesworkspacerepo_slugmerge_baserevspec",
                "table_name": "commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/merge-base/{revspec}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "revspec": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of the pull request's commits.  These are the commits that are being merged into the destination branch when the pull requests gets accepted.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idcommits",
                "table_name": "commit",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/commits",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the commit's comments.  This includes both global and inline comments.  The default sorting is oldest to newest and can be overridden with the `sort` query parameter.
            {
                "name": "get_repositoriesworkspacerepo_slugcommitcommitcomments",
                "table_name": "commit_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified commit comment.
            {
                "name": "get_repositoriesworkspacerepo_slugcommitcommitcommentscomment_id",
                "table_name": "commit_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugcommitcommitcomments",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of commits that modified the specified file.  Commits are returned in reverse chronological order. This is roughly equivalent to the following commands:      $ git log --follow --date-order <sha> <path>  By default, Bitbucket will follow renames and the path name in the returned entries reflects that. This can be turned off using the `?renames=false` query parameter.  Results are returned in descending chronological order by default, and like most endpoints you can [filter and sort](/cloud/bitbucket/rest/intro/#filtering) the response to only provide exactly the data you want.  For example, if you wanted to find commits made before 2011-05-18 against a file named `README.rst`, but you only wanted the path and date, your query would look like this:  ``` $ curl 'https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/filehistory/master/README.rst'\   '?fields=values.next,values.path,values.commit.date&q=commit.date<=2011-05-18' {   "values": [     {       "commit": {         "date": "2011-05-17T07:32:09+00:00"       },       "path": "README.rst"     },     {       "commit": {         "date": "2011-05-16T06:33:28+00:00"       },       "path": "README.txt"     },     {       "commit": {         "date": "2011-05-16T06:15:39+00:00"       },       "path": "README.txt"     }   ] } ```  In the response you can see that the file was renamed to `README.rst` by the commit made on 2011-05-16, and was previously named `README.txt`.
            {
                "name": "get_repositoriesworkspacerepo_slugfilehistorycommitpath",
                "table_name": "commit_file",
                "primary_key": "path",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/filehistory/{commit}/{path}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all statuses (e.g. build results) for a specific commit.
            {
                "name": "get_repositoriesworkspacerepo_slugcommitcommitstatuses",
                "table_name": "commitstatus",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified build status for a commit.
            {
                "name": "get_repositoriesworkspacerepo_slugcommitcommitstatusesbuildkey",
                "table_name": "commitstatus",
                "primary_key": "key",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/statuses/build/{key}",
                    "params": {
                        "key": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugcommitcommitstatuses",
                            "field": "key",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all statuses (e.g. build results) for the given pull request.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idstatuses",
                "table_name": "commitstatus",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/statuses",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the components that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.
            {
                "name": "get_repositoriesworkspacerepo_slugcomponents",
                "table_name": "component",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/components",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified issue tracker component object.
            {
                "name": "get_repositoriesworkspacerepo_slugcomponentscomponent_id",
                "table_name": "component",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/components/{component_id}",
                    "params": {
                        "component_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugcomponents",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the repository's effective default reviewers. This includes both default reviewers defined at the repository level as well as those inherited from its project.  These are the users that are automatically added as reviewers on every new pull request that is created.  ``` $ curl https://api.bitbucket.org/2.0/repositories/{workspace_slug}/{repo_slug}/effective-default-reviewers?page=1&pagelen=20 {     "pagelen": 20,     "values": [         {             "user": {                 "display_name": "Patrick Wolf",                 "uuid": "{9565301a-a3cf-4b5d-88f4-dd6af8078d7e}"             },             "reviewer_type": "project",             "type": "default_reviewer",         },         {             "user": {                 "display_name": "Davis Lee",                 "uuid": "{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}"             },             "reviewer_type": "repository",             "type": "default_reviewer",         }     ],     "page": 1,     "size": 2 } ```
            {
                "name": "get_repositoriesworkspacerepo_slugeffective_default_reviewers",
                "table_name": "default_reviewer_and_type",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/effective-default-reviewers",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return a list of all default reviewers for a project. This is a list of users that will be added as default reviewers to pull requests for any repository within the project.  Example: ``` $ curl https://api.bitbucket.org/2.0/.../projects/.../default-reviewers | jq . {     "pagelen": 10,     "values": [         {             "user": {                 "display_name": "Davis Lee",                 "uuid": "{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}"             },             "reviewer_type": "project",             "type": "default_reviewer"         },         {             "user": {                 "display_name": "Jorge Rodriguez",                 "uuid": "{1aa43376-260d-4a0b-9660-f62672b9655d}"             },             "reviewer_type": "project",             "type": "default_reviewer"         }     ],     "page": 1,     "size": 2 } ```
            {
                "name": "get_workspacesworkspaceprojectsproject_keydefault_reviewers",
                "table_name": "default_reviewer_and_type",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/projects/{project_key}/default-reviewers",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all deploy-keys belonging to a repository.  Example: ``` $ curl -H "Authorization <auth header>" \ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys  Output: {     "pagelen": 10,     "values": [         {             "id": 123,             "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5",             "label": "mykey",             "type": "deploy_key",             "created_on": "2018-08-15T23:50:59.993890+00:00",             "repository": {                 "full_name": "mleu/test",                 "name": "test",                 "type": "repository",                 "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"             },             "links":{                 "self":{                     "href": "https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-keys/123"                 }             }             "last_used": null,             "comment": "mleu@C02W454JHTD8"         }     ],     "page": 1,     "size": 1 } ```
            {
                "name": "get_repositoriesworkspacerepo_slugdeploy_keys",
                "table_name": "deploy_key",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/deploy-keys",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the deploy key belonging to a specific key.  Example: ``` $ curl -H "Authorization <auth header>" \ https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234  Output: {     "comment": "mleu@C02W454JHTD8",     "last_used": null,     "links": {         "self": {             "href": https://api.bitbucket.org/2.0/repositories/mleu/test/deploy-key/1234"         }     },     "repository": {         "full_name": "mleu/test",         "name": "test",         "type": "repository",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"     },     "label": "mykey",     "created_on": "2018-08-15T23:50:59.993890+00:00",     "key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDAK/b1cHHDr/TEV1JGQl+WjCwStKG6Bhrv0rFpEsYlyTBm1fzN0VOJJYn4ZOPCPJwqse6fGbXntEs+BbXiptR+++HycVgl65TMR0b5ul5AgwrVdZdT7qjCOCgaSV74/9xlHDK8oqgGnfA7ZoBBU+qpVyaloSjBdJfLtPY/xqj4yHnXKYzrtn/uFc4Kp9Tb7PUg9Io3qohSTGJGVHnsVblq/rToJG7L5xIo0OxK0SJSQ5vuId93ZuFZrCNMXj8JDHZeSEtjJzpRCBEXHxpOPhAcbm4MzULgkFHhAVgp4JbkrT99/wpvZ7r9AdkTg7HGqL3rlaDrEcWfL7Lu6TnhBdq5",     "id": 1234,     "type": "deploy_key" } ```
            {
                "name": "get_repositoriesworkspacerepo_slugdeploy_keyskey_id",
                "table_name": "deploy_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/deploy-keys/{key_id}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find deployments
            {
                "name": "get_deployments_for_repository",
                "table_name": "deployment",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/deployments",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a deployment
            {
                "name": "get_deployment_for_repository",
                "table_name": "deployment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/deployments/{deployment_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "deployment_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find environments
            {
                "name": "get_environments_for_repository",
                "table_name": "deployment_environment",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/environments",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve an environment
            {
                "name": "get_environment_for_repository",
                "table_name": "deployment_environment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/environments/{environment_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "environment_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find deployment environment level variables.
            {
                "name": "get_deployment_variables",
                "table_name": "deployment_variable",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/deployments_config/environments/{environment_uuid}/variables",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "environment_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Produces a raw git-style diff.  #### Single commit spec  If the `spec` argument to this API is a single commit, the diff is produced against the first parent of the specified commit.  #### Two commit spec  Two commits separated by `..` may be provided as the `spec`, e.g., `3a8b42..9ff173`. When two commits are provided and the `topic` query parameter is true or absent, this API produces a 2-way three dot diff. This is the diff between source commit and the merge base of the source commit and the destination commit. When the `topic` query param is false, a simple git-style diff is produced.  The two commits are interpreted as follows:  * First commit: the commit containing the changes we wish to preview * Second commit: the commit representing the state to which we want to   compare the first commit * **Note**: This is the opposite of the order used in `git diff`.  #### Comparison to patches  While similar to patches, diffs:  * Don't have a commit header (username, commit message, etc) * Support the optional `path=foo/bar.py` query param to filter   the diff to just that one file diff  #### Response  The raw diff is returned as-is, in whatever encoding the files in the repository use. It is not decoded into unicode. As such, the content-type is `text/plain`.
            {
                "name": "get_repositoriesworkspacerepo_slugdiffspec",
                "table_name": "diff",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/diff/{spec}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "spec": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "context": "OPTIONAL_CONFIG",
                        # "path": "OPTIONAL_CONFIG",
                        # "ignore_whitespace": "OPTIONAL_CONFIG",
                        # "binary": "OPTIONAL_CONFIG",
                        # "renames": "OPTIONAL_CONFIG",
                        # "merge": "OPTIONAL_CONFIG",
                        # "topic": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Redirects to the [repository diff](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-diff-spec-get) with the revspec that corresponds to the pull request.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_iddiff",
                "table_name": "diff",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diff",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the diff of the specified commit against its first parent.  Note that this resource is different in functionality from the `patch` resource.  The differences between a diff and a patch are:  * patches have a commit header with the username, message, etc * diffs support the optional `path=foo/bar.py` query param to filter the   diff to just that one file diff (not supported for patches) * for a merge, the diff will show the diff between the merge commit and   its first parent (identical to how PRs work), while patch returns a   response containing separate patches for each commit on the second   parent's ancestry, up to the oldest common ancestor (identical to   its reachability).  Note that the character encoding of the contents of the diff is unspecified as Git does not track this, making it hard for Bitbucket to reliably determine this.
            {
                "name": "get_snippetsworkspaceencoded_idrevisiondiff",
                "table_name": "diff",
                "endpoint": {
                    "path": "/snippets/{workspace}/{encoded_id}/{revision}/diff",
                    "params": {
                        "revision": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Produces a response in JSON format with a record for every path modified, including information on the type of the change and the number of lines added and removed.  #### Single commit spec  If the `spec` argument to this API is a single commit, the diff is produced against the first parent of the specified commit.  #### Two commit spec  Two commits separated by `..` may be provided as the `spec`, e.g., `3a8b42..9ff173`. When two commits are provided and the `topic` query parameter is true or absent, this API produces a 2-way three dot diff. This is the diff between source commit and the merge base of the source commit and the destination commit. When the `topic` query param is false, a simple git-style diff is produced.  The two commits are interpreted as follows:  * First commit: the commit containing the changes we wish to preview * Second commit: the commit representing the state to which we want to   compare the first commit * **Note**: This is the opposite of the order used in `git diff`.  #### Sample output ``` curl https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/diffstat/d222fa2..e174964 {     "pagelen": 500,     "values": [         {             "type": "diffstat",             "status": "modified",             "lines_removed": 1,             "lines_added": 2,             "old": {                 "path": "setup.py",                 "escaped_path": "setup.py",                 "type": "commit_file",                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/e1749643d655d7c7014001a6c0f58abaf42ad850/setup.py"                     }                 }             },             "new": {                 "path": "setup.py",                 "escaped_path": "setup.py",                 "type": "commit_file",                 "links": {                     "self": {                         "href": "https://api.bitbucket.org/2.0/repositories/bitbucket/geordi/src/d222fa235229c55dad20b190b0b571adf737d5a6/setup.py"                     }                 }             }         }     ],     "page": 1,     "size": 1 } ```
            {
                "name": "get_repositoriesworkspacerepo_slugdiffstatspec",
                "table_name": "diffstat",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/diffstat/{spec}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "spec": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Redirects to the [repository diffstat](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-diffstat-spec-get) with the revspec that corresponds to the pull request.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_iddiffstat",
                "table_name": "diffstat",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/diffstat",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of download links associated with the repository.
            {
                "name": "get_repositoriesworkspacerepo_slugdownloads",
                "table_name": "download",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/downloads",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return a redirect to the contents of a download artifact.  This endpoint returns the actual file contents and not the artifact's metadata.      $ curl -s -L https://api.bitbucket.org/2.0/repositories/evzijst/git-tests/downloads/hello.txt     Hello World
            {
                "name": "get_repositoriesworkspacerepo_slugdownloadsfilename",
                "table_name": "download",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/downloads/{filename}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filename": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_repositoriesworkspacerepo_slugeffective_branching_model",
                "table_name": "effective_branching_model",
                "endpoint": {
                    "data_selector": "branch_types",
                    "path": "/repositories/{workspace}/{repo_slug}/effective-branching-model",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Check whether the authenticated user has voted for this issue. A 204 status code indicates that the user has voted, while a 404 implies they haven't.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idvote",
                "table_name": "error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote",
                    "params": {
                        "issue_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Indicated whether or not the authenticated user is watching this issue.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idwatch",
                "table_name": "error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch",
                    "params": {
                        "issue_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all the authenticated user's email addresses. Both confirmed and unconfirmed.
            {
                "name": "get_useremails",
                "table_name": "error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/emails",
                },
            },
            # Returns details about a specific one of the authenticated user's email addresses.  Details describe whether the address has been confirmed by the user and whether it is the user's primary address or not.
            {
                "name": "get_useremailsemail",
                "table_name": "error",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/emails/{email}",
                    "params": {
                        "email": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Convenience resource for getting to a snippet's raw files without the need for first having to retrieve the snippet itself and having to pull out the versioned file links.
            {
                "name": "get_snippetsworkspaceencoded_idfilespath",
                "table_name": "file",
                "endpoint": {
                    "path": "/snippets/{workspace}/{encoded_id}/files/{path}",
                    "params": {
                        "path": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves the raw contents of a specific file in the snippet. The `Content-Disposition` header will be "attachment" to avoid issues with malevolent executable files.  The file's mime type is derived from its filename and returned in the `Content-Type` header.  Note that for text files, no character encoding is included as part of the content type.
            {
                "name": "get_snippetsworkspaceencoded_idnode_idfilespath",
                "table_name": "file",
                "endpoint": {
                    "path": "/snippets/{workspace}/{encoded_id}/{node_id}/files/{path}",
                    "params": {
                        "path": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "node_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all valid webhook events for the specified entity. **The team and user webhooks are deprecated, and you should use workspace instead. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).**  This is public data that does not require any scopes or authentication.  Example:  NOTE: The following example is a truncated response object for the `workspace` `subject_type`. We return the same structure for the other `subject_type` objects.  ``` $ curl https://api.bitbucket.org/2.0/hook_events/workspace {     "page": 1,     "pagelen": 30,     "size": 21,     "values": [         {             "category": "Repository",             "description": "Whenever a repository push occurs",             "event": "repo:push",             "label": "Push"         },         {             "category": "Repository",             "description": "Whenever a repository fork occurs",             "event": "repo:fork",             "label": "Fork"         },         {             "category": "Repository",             "description": "Whenever a repository import occurs",             "event": "repo:imported",             "label": "Import"         },         ...         {             "category":"Pull Request",             "label":"Approved",             "description":"When someone has approved a pull request",             "event":"pullrequest:approved"         },     ] } ```
            {
                "name": "get_hook_eventssubject_type",
                "table_name": "hook_event",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/hook_events/{subject_type}",
                    "params": {
                        "subject_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the issues in the issue tracker.
            {
                "name": "get_repositoriesworkspacerepo_slugissues",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/issues",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified issue.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_id",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}",
                    "params": {
                        "issue_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all attachments for this issue.  This returns the files' meta data. This does not return the files' actual contents.  The files are always ordered by their upload date.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idattachments",
                "table_name": "issue_attachment",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments",
                    "params": {
                        "issue_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the list of all changes that have been made to the specified issue. Changes are returned in chronological order with the oldest change first.  Each time an issue is edited in the UI or through the API, an immutable change record is created under the `/issues/123/changes` endpoint. It also has a comment associated with the change.  Note that this operation is changing significantly, due to privacy changes. See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#changes-to-the-issue-changes-api) for details.  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .  {   "pagelen": 20,   "values": [     {       "changes": {         "priority": {           "new": "trivial",           "old": "major"         },         "assignee": {           "new": "",           "old": "evzijst"         },         "assignee_account_id": {           "new": "",           "old": "557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443"         },         "kind": {           "new": "enhancement",           "old": "bug"         }       },       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2"         },         "html": {           "href": "https://bitbucket.org/evzijst/dogslow/issues/1#comment-2"         }       },       "issue": {         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1"           }         },         "type": "issue",         "id": 1,         "repository": {           "links": {             "self": {               "href": "https://api.bitbucket.org/2.0/repositories/evzijst/dogslow"             },             "html": {               "href": "https://bitbucket.org/evzijst/dogslow"             },             "avatar": {               "href": "https://bitbucket.org/evzijst/dogslow/avatar/32/"             }           },           "type": "repository",           "name": "dogslow",           "full_name": "evzijst/dogslow",           "uuid": "{988b17c6-1a47-4e70-84ee-854d5f012bf6}"         },         "title": "Updated title"       },       "created_on": "2018-03-03T00:35:28.353630+00:00",       "user": {         "username": "evzijst",         "nickname": "evzijst",         "display_name": "evzijst",         "type": "user",         "uuid": "{aaa7972b-38af-4fb1-802d-6e3854c95778}",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/users/evzijst"           },           "html": {             "href": "https://bitbucket.org/evzijst/"           },           "avatar": {             "href": "https://bitbucket.org/account/evzijst/avatar/32/"           }         }       },       "message": {         "raw": "Removed assignee, changed kind and priority.",         "markup": "markdown",         "html": "<p>Removed assignee, changed kind and priority.</p>",         "type": "rendered"       },       "type": "issue_change",       "id": 2     }   ],   "page": 1 } ```  Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that can be used to search for specific changes. For instance, to see when an issue transitioned to "resolved":  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \    -G --data-urlencode='q=changes.state.new = "resolved"' ```  This resource is only available on repositories that have the issue tracker enabled.  N.B.  The `changes.assignee` and `changes.assignee_account_id` fields are not a `user` object. Instead, they contain the raw `username` and `account_id` of the user. This is to protect the integrity of the audit log even after a user account gets deleted.  The `changes.assignee` field is deprecated will disappear in the future. Use `changes.assignee_account_id` instead.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idchanges",
                "table_name": "issue_change",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes",
                    "params": {
                        "issue_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified issue change object.  This resource is only available on repositories that have the issue tracker enabled.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idchangeschange_id",
                "table_name": "issue_change",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "issue_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "change_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all comments that were made on the specified issue.  The default sorting is oldest to newest and can be overridden with the `sort` query parameter.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idcomments",
                "table_name": "issue_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments",
                    "params": {
                        "issue_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified issue comment object.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesissue_idcommentscomment_id",
                "table_name": "issue_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissuesissue_idcomments",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "issue_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This endpoint is used to poll for the progress of an issue export job and return the zip file after the job is complete. As long as the job is running, this will return a 200 response with in the response body a description of the current status.  After the job has been scheduled, but before it starts executing, this endpoint's response is:  {  "type": "issue_job_status",  "status": "ACCEPTED",  "phase": "Initializing",  "total": 0,  "count": 0,  "pct": 0 }   Then once it starts running, it becomes:  {  "type": "issue_job_status",  "status": "STARTED",  "phase": "Attachments",  "total": 15,  "count": 11,  "pct": 73 }  Once the job has successfully completed, it returns a stream of the zip file.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesexportrepo_name_issues_task_id_zip",
                "table_name": "issue_job_status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/export/{repo_name}-issues-{task_id}.zip",
                    "params": {
                        "repo_name}-issues-{task_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # When using GET, this endpoint reports the status of the current import task. Request example:  ``` $ curl -u <username> -X GET https://api.bitbucket.org/2.0/repositories/<owner_username>/<repo_slug>/issues/import ```  After the job has been scheduled, but before it starts executing, this endpoint's response is:  ``` < HTTP/1.1 202 Accepted {     "type": "issue_job_status",     "status": "PENDING",     "phase": "Attachments",     "total": 15,     "count": 0,     "percent": 0 } ```  Once it starts running, it is a 202 response with status STARTED and progress filled.  After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.
            {
                "name": "get_repositoriesworkspacerepo_slugissuesimport",
                "table_name": "issue_job_status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/issues/import",
                    "params": {
                        "repo_slug": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugissues",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/
            {
                "name": "get_oidc_keys",
                "table_name": "key",
                "endpoint": {
                    "path": "/workspaces/{workspace}/pipelines-config/identity/oidc/keys.json",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the repository pipelines configuration.
            {
                "name": "get_repository_pipeline_config",
                "table_name": "link",
                "endpoint": {
                    "data_selector": "repository.links.clone",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a list of all [linkers](/cloud/bitbucket/modules/linker/) for the authenticated application.
            {
                "name": "get_addonlinkers",
                "table_name": "linker",
                "endpoint": {
                    "path": "/addon/linkers",
                },
            },
            # Gets a [linker](/cloud/bitbucket/modules/linker/) specified by `linker_key` for the authenticated application.
            {
                "name": "get_addonlinkerslinker_key",
                "table_name": "linker",
                "endpoint": {
                    "path": "/addon/linkers/{linker_key}",
                    "params": {
                        "linker_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the log file for a given step of a pipeline.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.
            {
                "name": "get_pipeline_step_log_for_repository",
                "table_name": "log",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/log",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "step_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the log file for a build container or service container.  This endpoint supports (and encourages!) the use of [HTTP Range requests](https://tools.ietf.org/html/rfc7233) to deal with potentially very large log files.
            {
                "name": "get_pipeline_container_log",
                "table_name": "log",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/logs/{log_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "step_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "log_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the milestones that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.
            {
                "name": "get_repositoriesworkspacerepo_slugmilestones",
                "table_name": "milestone",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/milestones",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified issue tracker milestone object.
            {
                "name": "get_repositoriesworkspacerepo_slugmilestonesmilestone_id",
                "table_name": "milestone",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/milestones/{milestone_id}",
                    "params": {
                        "milestone_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugmilestones",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This is part of OpenID Connect for Pipelines, see https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/
            {
                "name": "get_oidc_configuration",
                "table_name": "oidc",
                "endpoint": {
                    "path": "/workspaces/{workspace}/pipelines-config/identity/oidc/.well-known/openid-configuration",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Produces a raw patch for a single commit (diffed against its first parent), or a patch-series for a revspec of 2 commits (e.g. `3a8b42..9ff173` where the first commit represents the source and the second commit the destination).  In case of the latter (diffing a revspec), a patch series is returned for the commits on the source branch (`3a8b42` and its ancestors in our example).  While similar to diffs, patches:  * Have a commit header (username, commit message, etc) * Do not support the `path=foo/bar.py` query parameter  The raw patch is returned as-is, in whatever encoding the files in the repository use. It is not decoded into unicode. As such, the content-type is `text/plain`.
            {
                "name": "get_repositoriesworkspacerepo_slugpatchspec",
                "table_name": "patch",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/patch/{spec}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "spec": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Redirects to the [repository patch](/cloud/bitbucket/rest/api-group-commits/#api-repositories-workspace-repo-slug-patch-spec-get) with the revspec that corresponds to pull request.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idpatch",
                "table_name": "patch",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/patch",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the patch of the specified commit against its first parent.  Note that this resource is different in functionality from the `diff` resource.  The differences between a diff and a patch are:  * patches have a commit header with the username, message, etc * diffs support the optional `path=foo/bar.py` query param to filter the   diff to just that one file diff (not supported for patches) * for a merge, the diff will show the diff between the merge commit and   its first parent (identical to how PRs work), while patch returns a   response containing separate patches for each commit on the second   parent's ancestry, up to the oldest common ancestor (identical to   its reachability).  Note that the character encoding of the contents of the patch is unspecified as Git does not track this, making it hard for Bitbucket to reliably determine this.
            {
                "name": "get_snippetsworkspaceencoded_idrevisionpatch",
                "table_name": "patch",
                "endpoint": {
                    "path": "/snippets/{workspace}/{encoded_id}/{revision}/patch",
                    "params": {
                        "revision": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find pipelines
            {
                "name": "get_pipelines_for_repository",
                "table_name": "pipeline",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a specified pipeline
            {
                "name": "get_pipeline_for_repository",
                "table_name": "pipeline",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the repository pipelines caches.
            {
                "name": "get_repository_pipeline_caches",
                "table_name": "pipeline_cache",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines-config/caches",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the URI of the content of the specified cache.
            {
                "name": "get_repository_pipeline_cache_content_uri",
                "table_name": "pipeline_cache_content_uri",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines-config/caches/{cache_uuid}/content-uri",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "cache_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find repository level known hosts.
            {
                "name": "get_repository_pipeline_known_hosts",
                "table_name": "pipeline_known_host",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a repository level known host.
            {
                "name": "get_repository_pipeline_known_host",
                "table_name": "pipeline_known_host",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/known_hosts/{known_host_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "known_host_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the configured schedules for the given repository.
            {
                "name": "get_repository_pipeline_schedules",
                "table_name": "pipeline_schedule",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a schedule by its UUID.
            {
                "name": "get_repository_pipeline_schedule",
                "table_name": "pipeline_schedule",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "schedule_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the executions of a given schedule.
            {
                "name": "get_repository_pipeline_schedule_executions",
                "table_name": "pipeline_schedule_execution",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/schedules/{schedule_uuid}/executions",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "schedule_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the repository SSH key pair excluding the SSH private key. The private key is a write only field and will never be exposed in the logs or the REST API.
            {
                "name": "get_repository_pipeline_ssh_key_pair",
                "table_name": "pipeline_ssh_key_pair",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/ssh/key_pair",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find steps for the given pipeline.
            {
                "name": "get_pipeline_steps_for_repository",
                "table_name": "pipeline_step",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a given step of a pipeline.
            {
                "name": "get_pipeline_step_for_repository",
                "table_name": "pipeline_step",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "step_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find repository level variables.
            {
                "name": "get_repository_pipeline_variables",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/variables",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a repository level variable.
            {
                "name": "get_repository_pipeline_variable",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines_config/variables/{variable_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "variable_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find account level variables. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).
            {
                "name": "get_pipeline_variables_for_team",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/teams/{username}/pipelines_config/variables",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a team level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).
            {
                "name": "get_pipeline_variable_for_team",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{username}/pipelines_config/variables/{variable_uuid}",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "variable_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find user level variables. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).
            {
                "name": "get_pipeline_variables_for_user",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/users/{selected_user}/pipelines_config/variables",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a user level variable. This endpoint has been deprecated, and you should use the new workspaces endpoint. For more information, see [the announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-teams-deprecation/).
            {
                "name": "get_pipeline_variable_for_user",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{selected_user}/pipelines_config/variables/{variable_uuid}",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "variable_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Find workspace level variables.
            {
                "name": "get_pipeline_variables_for_workspace",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/pipelines-config/variables",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a workspace level variable.
            {
                "name": "get_pipeline_variable_for_workspace",
                "table_name": "pipeline_variable",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}/pipelines-config/variables/{variable_uuid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "variable_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the list of projects in this workspace.
            {
                "name": "get_workspacesworkspaceprojects",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/projects",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the requested project.
            {
                "name": "get_workspacesworkspaceprojectsproject_key",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}/projects/{project_key}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all deploy keys belonging to a project.  Example: ``` $ curl -H "Authorization <auth header>" \ https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys  Output: {     "pagelen":10,     "values":[         {             "comment":"thakseth@C02W454JHTD8",             "last_used":null,             "links":{                 "self":{                     "href":"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234"                 }             },             "label":"test",             "project":{                 "links":{                     "self":{                         "href":"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT"                     }                 },                 "type":"project",                 "name":"cooperative standard",                 "key":"TEST_PROJECT",                 "uuid":"{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}"             },             "created_on":"2021-07-28T21:20:19.491721+00:00",             "key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWvY3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3DNhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye0r",             "type":"project_deploy_key",             "id":1234         }     ],     "page":1,     "size":1 } ```
            {
                "name": "get_workspacesworkspaceprojectsproject_keydeploy_keys",
                "table_name": "project_deploy_key",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/projects/{project_key}/deploy-keys",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the deploy key belonging to a specific key ID.  Example: ``` $ curl -H "Authorization <auth header>" \ https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234  Output: {     "pagelen":10,     "values":[         {             "comment":"thakseth@C02W454JHTD8",             "last_used":null,             "links":{                 "self":{                     "href":"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT/deploy-keys/1234"                 }             },             "label":"test",             "project":{                 "links":{                     "self":{                         "href":"https://api.bitbucket.org/2.0/workspaces/standard/projects/TEST_PROJECT"                     }                 },                 "type":"project",                 "name":"cooperative standard",                 "key":"TEST_PROJECT",                 "uuid":"{3b3e510b-7f2b-414d-a2b7-76c4e405c1c0}"             },             "created_on":"2021-07-28T21:20:19.491721+00:00",             "key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDX5yfMOEw6HG9jKTYTisbmDTJ4MCUTSVGr5e4OWvY3UuI2A6F8SdzQqa2f5BABA/4g5Sk5awJrYHlNu3EzV1V2I44tR3A4fnZAG71ZKyDPi1wvdO7UYmFgxV/Vd18H9QZFFjICGDM7W0PT2mI0kON/jN3qNWi+GiB/xgaeQKSqynysdysDp8lnnI/8Sh3ikURP9UP83ShRCpAXszOUNaa+UUlcYQYBDLIGowsg51c4PCkC3DNhAMxppkNRKoSOWwyl+oRVXHSDylkiJSBHW3HH4Q6WHieD54kGrjbhWBKdnnxKX7QAAZBDseY+t01N36m6/ljvXSUEcBWtHxBYye0r",             "type":"project_deploy_key",             "id":1234         }     ], } ```
            {
                "name": "get_workspacesworkspaceprojectsproject_keydeploy_keyskey_id",
                "table_name": "project_deploy_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}/projects/{project_key}/deploy-keys/{key_id}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all pull requests authored by the specified user.  By default only open pull requests are returned. This can be controlled using the `state` query parameter. To retrieve pull requests that are in one of multiple states, repeat the `state` parameter for each individual state.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_pullrequestsselected_user",
                "table_name": "pullrequest",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/pullrequests/{selected_user}",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all pull requests as part of which this commit was reviewed. Pull Request Commit Links app must be installed first before using this API; installation automatically occurs when 'Go to pull request' is clicked from the web interface for a commit's details.
            {
                "name": "get_pullrequests_for_commit",
                "table_name": "pullrequest",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/pullrequests",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pagelen": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # Returns all pull requests on the specified repository.  By default only open pull requests are returned. This can be controlled using the `state` query parameter. To retrieve pull requests that are in one of multiple states, repeat the `state` parameter for each individual state.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequests",
                "table_name": "pullrequest",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified pull request.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_id",
                "table_name": "pullrequest",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of the pull request's comments.  This includes both global, inline comments and replies.  The default sorting is oldest to newest and can be overridden with the `sort` query parameter.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idcomments",
                "table_name": "pullrequest_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments",
                    "params": {
                        "pull_request_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a specific pull request comment.
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idcommentscomment_id",
                "table_name": "pullrequest_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idcomments",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pull_request_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the branches and tags in the repository.  By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees when running "$ git show-ref". Note that this follows simple lexical ordering of the ref names.  This can be undesirable as it does apply any natural sorting semantics, meaning for instance that refs are sorted ["branch1", "branch10", "branch2", "v10", "v11", "v9"] instead of ["branch1", "branch2", "branch10", "v9", "v10", "v11"].  Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on ref name, Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.
            {
                "name": "get_repositoriesworkspacerepo_slugrefs",
                "table_name": "ref",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/refs",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of Reports linked to this commit.
            {
                "name": "get_reports_for_commit",
                "table_name": "report",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a single Report matching the provided ID.
            {
                "name": "get_report",
                "table_name": "report",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "reportId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of Annotations for a specified report.
            {
                "name": "get_annotations_for_report",
                "table_name": "report_annotation",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "reportId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a single Annotation matching the provided ID.
            {
                "name": "get_annotation",
                "table_name": "report_annotation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/commit/{commit}/reports/{reportId}/annotations/{annotationId}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "reportId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "annotationId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all public repositories.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_repositories",
                "table_name": "repository",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories",
                },
            },
            # Returns a paginated list of all repositories owned by the specified workspace.  The result can be narrowed down based on the authenticated user's role.  E.g. with `?role=contributor`, only those repositories that the authenticated user has write access to are returned (this includes any repo the user is an admin on, as that implies write access).  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_repositoriesworkspace",
                "table_name": "repository",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the object describing this repository.
            {
                "name": "get_repositoriesworkspacerepo_slug",
                "table_name": "repository",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of all the forks of the specified repository.
            {
                "name": "get_repositoriesworkspacerepo_slugforks",
                "table_name": "repository",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/forks",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of explicit group permissions for the given repository. This endpoint does not support BBQL features.  Example:  ``` $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups  HTTP/1.1 200 Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups  {   "pagelen": 10,   "values": [     {       "type": "repository_group_permission",       "group": {         "type": "group",         "name": "Administrators",         "slug": "administrators"       },       "permission": "admin",       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/                    geordi/permissions-config/groups/administrators"         }       }     },     {       "type": "repository_group_permission",       "group": {         "type": "group",         "name": "Developers",         "slug": "developers"       },       "permission": "read",       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/                    geordi/permissions-config/groups/developers"         }       }     }   ],   "page": 1,   "size": 2 } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpermissions_configgroups",
                "table_name": "repository_group_permission",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/permissions-config/groups",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the group permission for a given group slug and repository  Only users with admin permission for the repository may access this resource.  Permissions can be:  * `admin` * `write` * `read` * `none`  Example:  ``` $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers  HTTP/1.1 200 Location: https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers  {     "type": "repository_group_permission",     "group": {         "type": "group",         "name": "Developers",         "slug": "developers"     },     "repository": {         "type": "repository",         "name": "geordi",         "full_name": "atlassian_tutorial/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"     },     "permission": "read",     "links": {       "self": {         "href":         "https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/groups/developers"       }     } } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpermissions_configgroupsgroup_slug",
                "table_name": "repository_group_permission",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/permissions-config/groups/{group_slug}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "group_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_repositoriesworkspacerepo_slugoverride_settings",
                "table_name": "repository_inheritance_state",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/override-settings",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns an object for each repository the caller has explicit access to and their effective permission — the highest level of permission the caller has. This does not return public repositories that the user was not granted any specific permission in, and does not distinguish between explicit and implicit privileges.  Permissions can be:  * `admin` * `write` * `read`  Example:  ``` $ curl https://api.bitbucket.org/2.0/user/permissions/repositories  {   "pagelen": 10,   "values": [     {       "type": "repository_permission",       "user": {         "type": "user",         "nickname": "evzijst",         "display_name": "Erik van Zijst",         "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}"       },       "repository": {         "type": "repository",         "name": "geordi",         "full_name": "bitbucket/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"       },       "permission": "admin"     }   ],   "page": 1,   "size": 1 } ```  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by repository or permission by adding the following query string parameters:  * `q=repository.name="geordi"` or `q=permission>"read"` * `sort=repository.name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.
            {
                "name": "get_userpermissionsrepositories",
                "table_name": "repository_permission",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/user/permissions/repositories",
                },
            },
            # Returns an object for each repository permission for all of a workspace's repositories.  Permissions returned are effective permissions: the highest level of permission the user has. This does not distinguish between direct and indirect (group) privileges.  Only users with admin permission for the team may access this resource.  Permissions can be:  * `admin` * `write` * `read`  Example:  ``` $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories  {   "pagelen": 10,   "values": [     {       "type": "repository_permission",       "user": {         "type": "user",         "display_name": "Erik van Zijst",         "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}"       },       "repository": {         "type": "repository",         "name": "geordi",         "full_name": "atlassian_tutorial/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"       },       "permission": "admin"     },     {       "type": "repository_permission",       "user": {         "type": "user",         "display_name": "Sean Conaty",         "uuid": "{504c3b62-8120-4f0c-a7bc-87800b9d6f70}"       },       "repository": {         "type": "repository",         "name": "geordi",         "full_name": "atlassian_tutorial/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"       },       "permission": "write"     },     {       "type": "repository_permission",       "user": {         "type": "user",         "display_name": "Jeff Zeng",         "uuid": "{47f92a9a-c3a3-4d0b-bc4e-782a969c5c72}"       },       "repository": {         "type": "repository",         "name": "whee",         "full_name": "atlassian_tutorial/whee",         "uuid": "{30ba25e9-51ff-4555-8dd0-fc7ee2fa0895}"       },       "permission": "admin"     }   ],   "page": 1,   "size": 3 } ```  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by repository, user, or permission by adding the following query string parameters:  * `q=repository.name="geordi"` or `q=permission>"read"` * `sort=user.display_name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.
            {
                "name": "get_workspacesworkspacepermissionsrepositories",
                "table_name": "repository_permission",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/permissions/repositories",
                    "params": {
                        "workspace": {
                            "type": "resolve",
                            "resource": "get_workspacesworkspacepermissions",
                            "field": "workspace",
                        },
                    },
                },
            },
            # Returns an object for the repository permission of each user in the requested repository.  Permissions returned are effective permissions: the highest level of permission the user has. This does not distinguish between direct and indirect (group) privileges.  Only users with admin permission for the repository may access this resource.  Permissions can be:  * `admin` * `write` * `read`  Example:  ``` $ curl https://api.bitbucket.org/2.0/workspaces/atlassian_tutorial/permissions/repositories/geordi  {   "pagelen": 10,   "values": [     {       "type": "repository_permission",       "user": {         "type": "user",         "display_name": "Erik van Zijst",         "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}"       },       "repository": {         "type": "repository",         "name": "geordi",         "full_name": "atlassian_tutorial/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"       },       "permission": "admin"     },     {       "type": "repository_permission",       "user": {         "type": "user",         "display_name": "Sean Conaty",         "uuid": "{504c3b62-8120-4f0c-a7bc-87800b9d6f70}"       },       "repository": {         "type": "repository",         "name": "geordi",         "full_name": "atlassian_tutorial/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"       },       "permission": "write"     }   ],   "page": 1,   "size": 2 } ```  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by user, or permission by adding the following query string parameters:  * `q=permission>"read"` * `sort=user.display_name`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.
            {
                "name": "get_workspacesworkspacepermissionsrepositoriesrepo_slug",
                "table_name": "repository_permission",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/permissions/repositories/{repo_slug}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of explicit user permissions for the given repository. This endpoint does not support BBQL features.  Example:  ``` $ curl https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/permissions-config/users  {   "pagelen": 10,   "values": [     {         "type": "repository_user_permission",         "user": {             "type": "user",             "display_name": "Colin Cameron",             "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}",             "account_id": "557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a"         },         "permission": "admin",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/                      permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a"           }         }     },     {       "type": "repository_user_permission",       "user": {         "type": "user",         "display_name": "Sean Conaty",         "uuid": "{504c3b62-8120-4f0c-a7bc-87800b9d6f70}",         "account_id": "557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c"       },       "permission": "write",       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0//repositories/atlassian_tutorial/geordi/                    permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324c"         }       }     }   ],   "page": 1,   "size": 2 } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpermissions_configusers",
                "table_name": "repository_user_permission",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/permissions-config/users",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the explicit user permission for a given user and repository.  Only users with admin permission for the repository may access this resource.  Permissions can be:  * `admin` * `write` * `read` * `none`  Example:  ``` $ curl 'https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/         permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a'  HTTP/1.1 200 Location: 'https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/            permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a'  {     "type": "repository_user_permission",     "user": {         "type": "user",         "display_name": "Colin Cameron",         "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}",         "account_id": "557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a"     },     "repository": {         "type": "repository",         "name": "geordi",         "full_name": "atlassian_tutorial/geordi",         "uuid": "{85d08b4e-571d-44e9-a507-fa476535aa98}"     },     "permission": "admin",     "links": {         "self": {             "href": "https://api.bitbucket.org/2.0/repositories/atlassian_tutorial/geordi/                      permissions-config/users/557058:ba8948b2-49da-43a9-9e8b-e7249b8e324a"         }     } } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpermissions_configusersselected_user_id",
                "table_name": "repository_user_permission",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/permissions-config/users/{selected_user_id}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "selected_user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Search for code in the repositories of the specified team.  Searching across all repositories:  ``` curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo' {   "size": 1,   "page": 1,   "pagelen": 10,   "query_substituted": false,   "values": [     {       "type": "code_search_result",       "content_match_count": 2,       "content_matches": [         {           "lines": [             {               "line": 2,               "segments": []             },             {               "line": 3,               "segments": [                 {                   "text": "def "                 },                 {                   "text": "foo",                   "match": true                 },                 {                   "text": "():"                 }               ]             },             {               "line": 4,               "segments": [                 {                   "text": "    print(\"snek\")"                 }               ]             },             {               "line": 5,               "segments": []             }           ]         }       ],       "path_matches": [         {           "text": "src/"         },         {           "text": "foo",           "match": true         },         {           "text": ".py"         }       ],       "file": {         "path": "src/foo.py",         "type": "commit_file",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py"           }         }       }     }   ] } ```  Note that searches can match in the file's text (`content_matches`), the path (`path_matches`), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  ``` curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code?search_query=foo+repo:demo' # results from the "demo" repository ```  Similar to other APIs, you can request more fields using a `fields` query parameter. E.g. to get some more information about the repository of matched files (the `%2B` is a URL-encoded `+`):  ``` curl 'https://api.bitbucket.org/2.0/teams/team_name/search/code'\      '?search_query=foo&fields=%2Bvalues.file.commit.repository' {   "size": 1,   "page": 1,   "pagelen": 10,   "query_substituted": false,   "values": [     {       "type": "code_search_result",       "content_match_count": 1,       "content_matches": [...],       "path_matches": [...],       "file": {         "commit": {           "type": "commit",           "hash": "ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b",           "links": {             "self": {               "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b"             },             "html": {               "href": "https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b"             }           },           "repository": {             "name": "demo",             "type": "repository",             "full_name": "my-workspace/demo",             "links": {               "self": {                 "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo"               },               "html": {                 "href": "https://bitbucket.org/my-workspace/demo"               },               "avatar": {                 "href": "https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default"               }             },             "uuid": "{850e1749-781a-4115-9316-df39d0600e7a}"           }         },         "type": "commit_file",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py"           }         },         "path": "src/foo.py"       }     }   ] } ```  Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.
            {
                "name": "search_team",
                "table_name": "search_code_search_result",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/teams/{username}/search/code",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "search_query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "pagelen": "10",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # Search for code in the repositories of the specified user.  Searching across all repositories:  ``` curl 'https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code?search_query=foo' {   "size": 1,   "page": 1,   "pagelen": 10,   "query_substituted": false,   "values": [     {       "type": "code_search_result",       "content_match_count": 2,       "content_matches": [         {           "lines": [             {               "line": 2,               "segments": []             },             {               "line": 3,               "segments": [                 {                   "text": "def "                 },                 {                   "text": "foo",                   "match": true                 },                 {                   "text": "():"                 }               ]             },             {               "line": 4,               "segments": [                 {                   "text": "    print(\"snek\")"                 }               ]             },             {               "line": 5,               "segments": []             }           ]         }       ],       "path_matches": [         {           "text": "src/"         },         {           "text": "foo",           "match": true         },         {           "text": ".py"         }       ],       "file": {         "path": "src/foo.py",         "type": "commit_file",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py"           }         }       }     }   ] } ```  Note that searches can match in the file's text (`content_matches`), the path (`path_matches`), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  ``` curl 'https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code?search_query=foo+repo:demo' # results from the "demo" repository ```  Similar to other APIs, you can request more fields using a `fields` query parameter. E.g. to get some more information about the repository of matched files (the `%2B` is a URL-encoded `+`):  ``` curl 'https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/search/code'\      '?search_query=foo&fields=%2Bvalues.file.commit.repository' {   "size": 1,   "page": 1,   "pagelen": 10,   "query_substituted": false,   "values": [     {       "type": "code_search_result",       "content_match_count": 1,       "content_matches": [...],       "path_matches": [...],       "file": {         "commit": {           "type": "commit",           "hash": "ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b",           "links": {             "self": {               "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b"             },             "html": {               "href": "https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b"             }           },           "repository": {             "name": "demo",             "type": "repository",             "full_name": "my-workspace/demo",             "links": {               "self": {                 "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo"               },               "html": {                 "href": "https://bitbucket.org/my-workspace/demo"               },               "avatar": {                 "href": "https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default"               }             },             "uuid": "{850e1749-781a-4115-9316-df39d0600e7a}"           }         },         "type": "commit_file",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py"           }         },         "path": "src/foo.py"       }     }   ] } ```  Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.
            {
                "name": "search_account",
                "table_name": "search_code_search_result",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/users/{selected_user}/search/code",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "search_query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "pagelen": "10",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # Search for code in the repositories of the specified workspace.  Searching across all repositories:  ``` curl 'https://api.bitbucket.org/2.0/workspaces/workspace_slug_or_uuid/search/code?search_query=foo' {   "size": 1,   "page": 1,   "pagelen": 10,   "query_substituted": false,   "values": [     {       "type": "code_search_result",       "content_match_count": 2,       "content_matches": [         {           "lines": [             {               "line": 2,               "segments": []             },             {               "line": 3,               "segments": [                 {                   "text": "def "                 },                 {                   "text": "foo",                   "match": true                 },                 {                   "text": "():"                 }               ]             },             {               "line": 4,               "segments": [                 {                   "text": "    print(\"snek\")"                 }               ]             },             {               "line": 5,               "segments": []             }           ]         }       ],       "path_matches": [         {           "text": "src/"         },         {           "text": "foo",           "match": true         },         {           "text": ".py"         }       ],       "file": {         "path": "src/foo.py",         "type": "commit_file",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py"           }         }       }     }   ] } ```  Note that searches can match in the file's text (`content_matches`), the path (`path_matches`), or both as in the example above.  You can use the same syntax for the search query as in the UI, e.g. to only search within a specific repository:  ``` curl 'https://api.bitbucket.org/2.0/workspaces/my-workspace/search/code?search_query=foo+repo:demo' # results from the "demo" repository ```  Similar to other APIs, you can request more fields using a `fields` query parameter. E.g. to get some more information about the repository of matched files (the `%2B` is a URL-encoded `+`):  ``` curl 'https://api.bitbucket.org/2.0/workspaces/my-workspace/search/code'\      '?search_query=foo&fields=%2Bvalues.file.commit.repository' {   "size": 1,   "page": 1,   "pagelen": 10,   "query_substituted": false,   "values": [     {       "type": "code_search_result",       "content_match_count": 1,       "content_matches": [...],       "path_matches": [...],       "file": {         "commit": {           "type": "commit",           "hash": "ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b",           "links": {             "self": {               "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/commit/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b"             },             "html": {               "href": "https://bitbucket.org/my-workspace/demo/commits/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b"             }           },           "repository": {             "name": "demo",             "type": "repository",             "full_name": "my-workspace/demo",             "links": {               "self": {                 "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo"               },               "html": {                 "href": "https://bitbucket.org/my-workspace/demo"               },               "avatar": {                 "href": "https://bytebucket.org/ravatar/%7B850e1749-781a-4115-9316-df39d0600e7a%7D?ts=default"               }             },             "uuid": "{850e1749-781a-4115-9316-df39d0600e7a}"           }         },         "type": "commit_file",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/my-workspace/demo/src/ad6964b5fe2880dbd9ddcad1c89000f1dbcbc24b/src/foo.py"           }         },         "path": "src/foo.py"       }     }   ] } ```  Try `fields=%2Bvalues.*.*.*.*` to get an idea what's possible.
            {
                "name": "search_workspace",
                "table_name": "search_code_search_result",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/search/code",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "search_query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "pagelen": "10",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # Return the branching model configuration for a repository. The returned object:  1. Always has a `development` property for the development branch. 2. Always a `production` property for the production branch. The    production branch can be disabled. 3. The `branch_types` contains all the branch types.  This is the raw configuration for the branching model. A client wishing to see the branching model with its actual current branches may find the [active model API](/cloud/bitbucket/rest/api-group-branching-model/#api-repositories-workspace-repo-slug-branching-model-get) more useful.  Example body:  ``` {   "development": {     "is_valid": true,     "name": null,     "use_mainbranch": true   },   "production": {     "is_valid": true,     "name": "production",     "use_mainbranch": false,     "enabled": false   },   "branch_types": [     {       "kind": "release",       "enabled": true,       "prefix": "release/"     },     {       "kind": "hotfix",       "enabled": true,       "prefix": "hotfix/"     },     {       "kind": "feature",       "enabled": true,       "prefix": "feature/"     },     {       "kind": "bugfix",       "enabled": false,       "prefix": "bugfix/"     }   ],   "type": "branching_model_settings",   "links": {     "self": {       "href": "https://api.bitbucket.org/.../branching-model/settings"     }   } } ```
            {
                "name": "get_repositoriesworkspacerepo_slugbranching_modelsettings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "branch_types",
                    "path": "/repositories/{workspace}/{repo_slug}/branching-model/settings",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Return the branching model configuration for a project. The returned object:  1. Always has a `development` property for the development branch. 2. Always a `production` property for the production branch. The    production branch can be disabled. 3. The `branch_types` contains all the branch types.   This is the raw configuration for the branching model. A client wishing to see the branching model with its actual current branches may find the [active model API](#api-workspaces-workspace-projects-project-key-branching-model-get) more useful.  Example body:  ``` {   "development": {     "name": null,     "use_mainbranch": true   },   "production": {     "name": "production",     "use_mainbranch": false,     "enabled": false   },   "branch_types": [     {       "kind": "release",       "enabled": true,       "prefix": "release/"     },     {       "kind": "hotfix",       "enabled": true,       "prefix": "hotfix/"     },     {       "kind": "feature",       "enabled": true,       "prefix": "feature/"     },     {       "kind": "bugfix",       "enabled": false,       "prefix": "bugfix/"     }   ],   "type": "branching_model_settings",   "links": {     "self": {       "href": "https://api.bitbucket.org/.../branching-model/settings"     }   } } ```
            {
                "name": "get_workspacesworkspaceprojectsproject_keybranching_modelsettings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "branch_types",
                    "path": "/workspaces/{workspace}/projects/{project_key}/branching-model/settings",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns all snippets. Like pull requests, repositories and workspaces, the full set of snippets is defined by what the current user has access to.  This includes all snippets owned by any of the workspaces the user is a member of, or snippets by other users that the current user is either watching or has collaborated on (for instance by commenting on it).  To limit the set of returned snippets, apply the `?role=[owner|contributor|member]` query parameter where the roles are defined as follows:  * `owner`: all snippets owned by the current user * `contributor`: all snippets owned by, or watched by the current user * `member`: created in a workspaces or watched by the current user  When no role is specified, all public snippets are returned, as well as all privately owned snippets watched or commented on.  The returned response is a normal paginated JSON list. This endpoint only supports `application/json` responses and no `multipart/form-data` or `multipart/related`. As a result, it is not possible to include the file contents.
            {
                "name": "get_snippets",
                "table_name": "snippet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/snippets",
                },
            },
            # Identical to [`/snippets`](/cloud/bitbucket/rest/api-group-snippets/#api-snippets-get), except that the result is further filtered by the snippet owner and only those that are owned by `{workspace}` are returned.
            {
                "name": "get_snippetsworkspace",
                "table_name": "snippet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/snippets/{workspace}",
                    "params": {
                        "workspace": {
                            "type": "resolve",
                            "resource": "get_snippets",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves a single snippet.  Snippets support multiple content types:  * application/json * multipart/related * multipart/form-data   application/json ----------------  The default content type of the response is `application/json`. Since JSON is always `utf-8`, it cannot reliably contain file contents for files that are not text. Therefore, JSON snippet documents only contain the filename and links to the file contents.  This means that in order to retrieve all parts of a snippet, N+1 requests need to be made (where N is the number of files in the snippet).   multipart/related -----------------  To retrieve an entire snippet in a single response, use the `Accept: multipart/related` HTTP request header.      $ curl -H "Accept: multipart/related" https://api.bitbucket.org/2.0/snippets/evzijst/1  Response:      HTTP/1.1 200 OK     Content-Length: 2214     Content-Type: multipart/related; start="snippet"; boundary="===============1438169132528273974=="     MIME-Version: 1.0      --===============1438169132528273974==     Content-Type: application/json; charset="utf-8"     MIME-Version: 1.0     Content-ID: snippet      {       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj"         },         "html": {           "href": "https://bitbucket.org/snippets/evzijst/kypj"         },         "comments": {           "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/comments"         },         "watchers": {           "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/watchers"         },         "commits": {           "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/commits"         }       },       "id": kypj,       "title": "My snippet",       "created_on": "2014-12-29T22:22:04.790331+00:00",       "updated_on": "2014-12-29T22:22:04.790331+00:00",       "is_private": false,       "files": {         "foo.txt": {           "links": {             "self": {               "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/foo.txt"             },             "html": {               "href": "https://bitbucket.org/snippets/evzijst/kypj#file-foo.txt"             }           }         },         "image.png": {           "links": {             "self": {               "href": "https://api.bitbucket.org/2.0/snippets/evzijst/kypj/files/367ab19/image.png"             },             "html": {               "href": "https://bitbucket.org/snippets/evzijst/kypj#file-image.png"             }           }         }       ],       "owner": {         "username": "evzijst",         "nickname": "evzijst",         "display_name": "Erik van Zijst",         "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/users/evzijst"           },           "html": {             "href": "https://bitbucket.org/evzijst"           },           "avatar": {             "href": "https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png"           }         }       },       "creator": {         "username": "evzijst",         "nickname": "evzijst",         "display_name": "Erik van Zijst",         "uuid": "{d301aafa-d676-4ee0-88be-962be7417567}",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/users/evzijst"           },           "html": {             "href": "https://bitbucket.org/evzijst"           },           "avatar": {             "href": "https://bitbucket-staging-assetroot.s3.amazonaws.com/c/photos/2013/Jul/31/erik-avatar-725122544-0_avatar.png"           }         }       }     }      --===============1438169132528273974==     Content-Type: text/plain; charset="us-ascii"     MIME-Version: 1.0     Content-Transfer-Encoding: 7bit     Content-ID: "foo.txt"     Content-Disposition: attachment; filename="foo.txt"      foo      --===============1438169132528273974==     Content-Type: image/png     MIME-Version: 1.0     Content-Transfer-Encoding: base64     Content-ID: "image.png"     Content-Disposition: attachment; filename="image.png"      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==     --===============1438169132528273974==--  multipart/form-data -------------------  As with creating new snippets, `multipart/form-data` can be used as an alternative to `multipart/related`. However, the inherently flat structure of form-data means that only basic, root-level properties can be returned, while nested elements like `links` are omitted:      $ curl -H "Accept: multipart/form-data" https://api.bitbucket.org/2.0/snippets/evzijst/kypj  Response:      HTTP/1.1 200 OK     Content-Length: 951     Content-Type: multipart/form-data; boundary=----------------------------63a4b224c59f      ------------------------------63a4b224c59f     Content-Disposition: form-data; name="title"     Content-Type: text/plain; charset="utf-8"      My snippet     ------------------------------63a4b224c59f--     Content-Disposition: attachment; name="file"; filename="foo.txt"     Content-Type: text/plain      foo      ------------------------------63a4b224c59f     Content-Disposition: attachment; name="file"; filename="image.png"     Content-Transfer-Encoding: base64     Content-Type: application/octet-stream      iVBORw0KGgoAAAANSUhEUgAAABQAAAAoCAYAAAD+MdrbAAABD0lEQVR4Ae3VMUoDQRTG8ccUaW2m     TKONFxArJYJamCvkCnZTaa+VnQdJSBFl2SMsLFrEWNjZBZs0JgiL/+KrhhVmJRbCLPx4O+/DT2TB     cbblJxf+UWFVVRNsEGAtgvJxnLm2H+A5RQ93uIl+3632PZyl/skjfOn9Gvdwmlcw5aPUwimG+NT5     EnNN036IaZePUuIcK533NVfal7/5yjWeot2z9ta1cAczHEf7I+3J0ws9Cgx0fsOFpmlfwKcWPuBQ     73Oc4FHzBaZ8llq4q1mr5B2mOUCt815qYR8eB1hG2VJ7j35q4RofaH7IG+Xrf/PfJhfmwtfFYoIN     AqxFUD6OMxcvkO+UfKfkOyXfKdsv/AYCHMLVkHAFWgAAAABJRU5ErkJggg==     ------------------------------5957323a6b76--
            {
                "name": "get_snippetsworkspaceencoded_id",
                "table_name": "snippet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/snippets/{workspace}/{encoded_id}",
                    "params": {
                        "encoded_id": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Identical to `GET /snippets/encoded_id`, except that this endpoint can be used to retrieve the contents of the snippet as it was at an older revision, while `/snippets/encoded_id` always returns the snippet's current revision.  Note that only the snippet's file contents are versioned, not its meta data properties like the title.  Other than that, the two endpoints are identical in behavior.
            {
                "name": "get_snippetsworkspaceencoded_idnode_id",
                "table_name": "snippet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/snippets/{workspace}/{encoded_id}/{node_id}",
                    "params": {
                        "node_id": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Used to retrieve a paginated list of all comments for a specific snippet.  This resource works identical to commit and pull request comments.  The default sorting is oldest to newest and can be overridden with the `sort` query parameter.
            {
                "name": "get_snippetsworkspaceencoded_idcomments",
                "table_name": "snippet_comment",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/snippets/{workspace}/{encoded_id}/comments",
                    "params": {
                        "encoded_id": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specific snippet comment.
            {
                "name": "get_snippetsworkspaceencoded_idcommentscomment_id",
                "table_name": "snippet_comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/snippets/{workspace}/{encoded_id}/comments/{comment_id}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the changes (commits) made on this snippet.
            {
                "name": "get_snippetsworkspaceencoded_idcommits",
                "table_name": "snippet_commit",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/snippets/{workspace}/{encoded_id}/commits",
                    "params": {
                        "encoded_id": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the changes made on this snippet in this commit.
            {
                "name": "get_snippetsworkspaceencoded_idcommitsrevision",
                "table_name": "snippet_commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/snippets/{workspace}/{encoded_id}/commits/{revision}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "encoded_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "revision": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of the user's SSH public keys.  Example:  ``` $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys {     "page": 1,     "pagelen": 10,     "size": 1,     "values": [         {             "comment": "user@myhost",             "created_on": "2018-03-14T13:17:05.196003+00:00",             "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY",             "label": "",             "last_used": "2018-03-20T13:18:05.196003+00:00",             "links": {                 "self": {                     "href": "https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/b15b6026-9c02-4626-b4ad-b905f99f763a"                 }             },             "owner": {                 "display_name": "Mark Adams",                 "links": {                     "avatar": {                         "href": "https://bitbucket.org/account/markadams-atl/avatar/32/"                     },                     "html": {                         "href": "https://bitbucket.org/markadams-atl/"                     },                     "self": {                         "href": "https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}"                     }                 },                 "type": "user",                 "username": "markadams-atl",                 "nickname": "markadams-atl",                 "uuid": "{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}"             },             "type": "ssh_key",             "uuid": "{b15b6026-9c02-4626-b4ad-b905f99f763a}"         }     ] } ```
            {
                "name": "get_usersselected_userssh_keys",
                "table_name": "ssh_account_key",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/users/{selected_user}/ssh-keys",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a specific SSH public key belonging to a user.  Example: ``` $ curl https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/{fbe4bbab-f6f7-4dde-956b-5c58323c54b3}  {     "comment": "user@myhost",     "created_on": "2018-03-14T13:17:05.196003+00:00",     "key": "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY",     "label": "",     "last_used": "2018-03-20T13:18:05.196003+00:00",     "links": {         "self": {             "href": "https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}/ssh-keys/b15b6026-9c02-4626-b4ad-b905f99f763a"         }     },     "owner": {         "display_name": "Mark Adams",         "links": {             "avatar": {                 "href": "https://bitbucket.org/account/markadams-atl/avatar/32/"             },             "html": {                 "href": "https://bitbucket.org/markadams-atl/"             },             "self": {                 "href": "https://api.bitbucket.org/2.0/users/{ed08f5e1-605b-4f4a-aee4-6c97628a673e}"             }         },         "type": "user",         "username": "markadams-atl",         "nickname": "markadams-atl",         "uuid": "{d7dd0e2d-3994-4a50-a9ee-d260b6cefdab}"     },     "type": "ssh_key",     "uuid": "{b15b6026-9c02-4626-b4ad-b905f99f763a}" } ```
            {
                "name": "get_usersselected_userssh_keyskey_id",
                "table_name": "ssh_account_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{selected_user}/ssh-keys/{key_id}",
                    "params": {
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the webhook resource or subject types on which webhooks can be registered.  Each resource/subject type contains an `events` link that returns the paginated list of specific events each individual subject type can emit.  This endpoint is publicly accessible and does not require authentication or scopes.  Example:  ``` $ curl https://api.bitbucket.org/2.0/hook_events  {     "repository": {         "links": {             "events": {                 "href": "https://api.bitbucket.org/2.0/hook_events/repository"             }         }     },     "workspace": {         "links": {             "events": {                 "href": "https://api.bitbucket.org/2.0/hook_events/workspace"             }         }     } } ```
            {
                "name": "get_hook_events",
                "table_name": "subject_types",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/hook_events",
                },
            },
            # Returns the tags in the repository.  By default, results will be in the order the underlying source control system returns them and identical to the ordering one sees when running "$ git tag --list". Note that this follows simple lexical ordering of the ref names.  This can be undesirable as it does apply any natural sorting semantics, meaning for instance that tags are sorted ["v10", "v11", "v9"] instead of ["v9", "v10", "v11"].  Sorting can be changed using the ?sort= query parameter. When using ?sort=name to explicitly sort on ref name, Bitbucket will apply natural sorting and interpret numerical values as numbers instead of strings.
            {
                "name": "get_repositoriesworkspacerepo_slugrefstags",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/refs/tags",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified tag.  ``` $ curl -s https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8 -G | jq . {   "name": "3.8",   "links": {     "commits": {       "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commits/3.8"     },     "self": {       "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/refs/tags/3.8"     },     "html": {       "href": "https://bitbucket.org/seanfarley/hg/commits/tag/3.8"     }   },   "tagger": {     "raw": "Matt Mackall <mpm@selenic.com>",     "type": "author",     "user": {       "username": "mpmselenic",       "nickname": "mpmselenic",       "display_name": "Matt Mackall",       "type": "user",       "uuid": "{a4934530-db4c-419c-a478-9ab4964c2ee7}",       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/users/mpmselenic"         },         "html": {           "href": "https://bitbucket.org/mpmselenic/"         },         "avatar": {           "href": "https://bitbucket.org/account/mpmselenic/avatar/32/"         }       }     }   },   "date": "2016-05-01T18:52:25+00:00",   "message": "Added tag 3.8 for changeset f85de28eae32",   "type": "tag",   "target": {     "hash": "f85de28eae32e7d3064b1a1321309071bbaaa069",     "repository": {       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg"         },         "html": {           "href": "https://bitbucket.org/seanfarley/hg"         },         "avatar": {           "href": "https://bitbucket.org/seanfarley/hg/avatar/32/"         }       },       "type": "repository",       "name": "hg",       "full_name": "seanfarley/hg",       "uuid": "{c75687fb-e99d-4579-9087-190dbd406d30}"     },     "links": {       "self": {         "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069"       },       "comments": {         "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069/comments"       },       "patch": {         "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/patch/f85de28eae32e7d3064b1a1321309071bbaaa069"       },       "html": {         "href": "https://bitbucket.org/seanfarley/hg/commits/f85de28eae32e7d3064b1a1321309071bbaaa069"       },       "diff": {         "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/diff/f85de28eae32e7d3064b1a1321309071bbaaa069"       },       "approve": {         "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069/approve"       },       "statuses": {         "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/f85de28eae32e7d3064b1a1321309071bbaaa069/statuses"       }     },     "author": {       "raw": "Sean Farley <sean@farley.io>",       "type": "author",       "user": {         "username": "seanfarley",         "nickname": "seanfarley",         "display_name": "Sean Farley",         "type": "user",         "uuid": "{a295f8a8-5876-4d43-89b5-3ad8c6c3c51d}",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/users/seanfarley"           },           "html": {             "href": "https://bitbucket.org/seanfarley/"           },           "avatar": {             "href": "https://bitbucket.org/account/seanfarley/avatar/32/"           }         }       }     },     "parents": [       {         "hash": "9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2",         "type": "commit",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/seanfarley/hg/commit/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2"           },           "html": {             "href": "https://bitbucket.org/seanfarley/hg/commits/9a98d0e5b07fc60887f9d3d34d9ac7d536f470d2"           }         }       }     ],     "date": "2016-05-01T04:21:17+00:00",     "message": "debian: alphabetize build deps",     "type": "commit"   } } ```
            {
                "name": "get_repositoriesworkspacerepo_slugrefstagsname",
                "table_name": "tag",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/refs/tags/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugrefstags",
                            "field": "name",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # When merging a pull request takes too long, the client receives a task ID along with a 202 status code. The task ID can be used in a call to this endpoint to check the status of a merge task.  ``` curl -X GET https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/<task_id> ```  If the merge task is not yet finished, a PENDING status will be returned.  ``` HTTP/2 200 {     "task_status": "PENDING",     "links": {         "self": {             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/<task_id>"         }     } } ```  If the merge was successful, a SUCCESS status will be returned.  ``` HTTP/2 200 {     "task_status": "SUCCESS",     "links": {         "self": {             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bitbucket/pullrequests/2286/merge/task-status/<task_id>"         }     },     "merge_result": <the merged pull request object> } ```  If the merge task failed, an error will be returned.  ``` {     "type": "error",     "error": {         "message": "<error message>"     } } ```
            {
                "name": "get_repositoriesworkspacerepo_slugpullrequestspull_request_idmergetask_statustask_id",
                "table_name": "task_statu",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pullrequests/{pull_request_id}/merge/task-status/{task_id}",
                    "params": {
                        "task_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugpullrequests",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pull_request_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_pipeline_test_report_test_cases",
                "table_name": "test_case",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "step_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_pipeline_test_report_test_case_reasons",
                "table_name": "test_case_reason",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports/test_cases/{test_case_uuid}/test_case_reasons",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "step_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "test_case_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "get_pipeline_test_reports",
                "table_name": "test_report",
                "endpoint": {
                    "path": "/repositories/{workspace}/{repo_slug}/pipelines/{pipeline_uuid}/steps/{step_uuid}/test_reports",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pipeline_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "step_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This endpoint redirects the client to the directory listing of the root directory on the main branch.  This is equivalent to directly hitting [/2.0/repositories/{username}/{repo_slug}/src/{commit}/{path}](src/%7Bcommit%7D/%7Bpath%7D) without having to know the name or SHA1 of the repo's main branch.  To create new commits, [POST to this endpoint](#post)
            {
                "name": "get_repositoriesworkspacerepo_slugsrc",
                "table_name": "treeentry",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/src",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This endpoints is used to retrieve the contents of a single file, or the contents of a directory at a specified revision.  #### Raw file contents  When `path` points to a file, this endpoint returns the raw contents. The response's Content-Type is derived from the filename extension (not from the contents). The file contents are not processed and no character encoding/recoding is performed and as a result no character encoding is included as part of the Content-Type.  The `Content-Disposition` header will be "attachment" to prevent browsers from running executable files.  If the file is managed by LFS, then a 301 redirect pointing to Atlassian's media services platform is returned.  The response includes an ETag that is based on the contents of the file and its attributes. This means that an empty `__init__.py` always returns the same ETag, regardless on the directory it lives in, or the commit it is on.  #### File meta data  When the request for a file path includes the query parameter `?format=meta`, instead of returning the file's raw contents, Bitbucket instead returns the JSON object describing the file's properties:  ```javascript $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests/__init__.py?format=meta {   "links": {     "self": {       "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py"     },     "meta": {       "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format=meta"     }   },   "path": "tests/__init__.py",   "commit": {     "type": "commit",     "hash": "eefd5ef5d3df01aed629f650959d6706d54cd335",     "links": {       "self": {         "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335"       },       "html": {         "href": "https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335"       }     }   },   "attributes": [],   "type": "commit_file",   "size": 0 } ```  File objects contain an `attributes` element that contains a list of possible modifiers. Currently defined values are:  * `link` -- indicates that the entry is a symbolic link. The contents     of the file represent the path the link points to. * `executable` -- indicates that the file has the executable bit set. * `subrepository` -- indicates that the entry points to a submodule or     subrepo. The contents of the file is the SHA1 of the repository     pointed to. * `binary` -- indicates whether Bitbucket thinks the file is binary.  This endpoint can provide an alternative to how a HEAD request can be used to check for the existence of a file, or a file's size without incurring the overhead of receiving its full contents.   #### Directory listings  When `path` points to a directory instead of a file, the response is a paginated list of directory and file objects in the same order as the underlying SCM system would return them.  For example:  ```javascript $ curl https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef/tests {   "pagelen": 10,   "values": [     {       "path": "tests/test_project",       "type": "commit_directory",       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/"         },         "meta": {           "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format=meta"         }       },       "commit": {         "type": "commit",         "hash": "eefd5ef5d3df01aed629f650959d6706d54cd335",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335"           },           "html": {             "href": "https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335"           }         }       }     },     {       "links": {         "self": {           "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py"         },         "meta": {           "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/__init__.py?format=meta"         }       },       "path": "tests/__init__.py",       "commit": {         "type": "commit",         "hash": "eefd5ef5d3df01aed629f650959d6706d54cd335",         "links": {           "self": {             "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/commit/eefd5ef5d3df01aed629f650959d6706d54cd335"           },           "html": {             "href": "https://bitbucket.org/atlassian/bbql/commits/eefd5ef5d3df01aed629f650959d6706d54cd335"           }         }       },       "attributes": [],       "type": "commit_file",       "size": 0     }   ],   "page": 1,   "size": 2 } ```  When listing the contents of the repo's root directory, the use of a trailing slash at the end of the URL is required.  The response by default is not recursive, meaning that only the direct contents of a path are returned. The response does not recurse down into subdirectories. In order to "walk" the entire directory tree, the client can either parse each response and follow the `self` links of each `commit_directory` object, or can specify a `max_depth` to recurse to.  The max_depth parameter will do a breadth-first search to return the contents of the subdirectories up to the depth specified. Breadth-first search was chosen as it leads to the least amount of file system operations for git. If the `max_depth` parameter is specified to be too large, the call will time out and return a 555.  Each returned object is either a `commit_file`, or a `commit_directory`, both of which contain a `path` element. This path is the absolute path from the root of the repository. Each object also contains a `commit` object which embeds the commit the file is on. Note that this is merely the commit that was used in the URL. It is *not* the commit that last modified the file.  Directory objects have 2 representations. Their `self` link returns the paginated contents of the directory. The `meta` link on the other hand returns the actual `directory` object itself, e.g.:  ```javascript {   "path": "tests/test_project",   "type": "commit_directory",   "links": {     "self": {       "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/"     },     "meta": {       "href": "https://api.bitbucket.org/2.0/repositories/atlassian/bbql/src/eefd5ef5d3df01aed629f650959d6706d54cd335/tests/test_project/?format=meta"     }   },   "commit": { ... } } ```  #### Querying, filtering and sorting  Like most API endpoints, this API supports the Bitbucket querying/filtering syntax and so you could filter a directory listing to only include entries that match certain criteria. For instance, to list all binary files over 1kb use the expression:  `size > 1024 and attributes = "binary"`  which after urlencoding yields the query string:  `?q=size%3E1024+and+attributes%3D%22binary%22`  To change the ordering of the response, use the `?sort` parameter:  `.../src/eefd5ef/?sort=-size`  See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.
            {
                "name": "get_repositoriesworkspacerepo_slugsrccommitpath",
                "table_name": "treeentry",
                "primary_key": "path",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/src/{commit}/{path}",
                    "params": {
                        "path": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugsrc",
                            "field": "path",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified default reviewer.  Example: ``` $ curl https://api.bitbucket.org/2.0/.../default-reviewers/%7Bf0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6%7D {     "display_name": "Davis Lee",     "type": "user",     "uuid": "{f0e0e8e9-66c1-4b85-a784-44a9eb9ef1a6}" } ```
            {
                "name": "get_workspacesworkspaceprojectsproject_keydefault_reviewersselected_user",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}/projects/{project_key}/default-reviewers/{selected_user}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "selected_user": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a list of all [linker](/cloud/bitbucket/modules/linker/) values for the specified linker of the authenticated application.  A linker value lets applications supply values to modify its regular expression.  The base regular expression must use a Bitbucket-specific match group `(?K)` which will be translated to `([\w\-]+)`. A value must match this pattern.  [Read more about linker values](/cloud/bitbucket/modules/linker/#usingthebitbucketapitosupplyvalues)
            {
                "name": "get_addonlinkerslinker_keyvalues",
                "table_name": "value",
                "endpoint": {
                    "path": "/addon/linkers/{linker_key}/values",
                    "params": {
                        "linker_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get a single [linker](/cloud/bitbucket/modules/linker/) value of the authenticated application.
            {
                "name": "get_addonlinkerslinker_keyvaluesvalue_id",
                "table_name": "value",
                "endpoint": {
                    "path": "/addon/linkers/{linker_key}/values/{value_id}",
                    "params": {
                        "linker_key": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "value_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the versions that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.
            {
                "name": "get_repositoriesworkspacerepo_slugversions",
                "table_name": "version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/versions",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the specified issue tracker version object.
            {
                "name": "get_repositoriesworkspacerepo_slugversionsversion_id",
                "table_name": "version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/versions/{version_id}",
                    "params": {
                        "version_id": {
                            "type": "resolve",
                            "resource": "get_repositoriesworkspacerepo_slugversions",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Used to check if the current user is watching a specific snippet.  Returns 204 (No Content) if the user is watching the snippet and 404 if not.  Hitting this endpoint anonymously always returns a 404.
            {
                "name": "get_snippetsworkspaceencoded_idwatch",
                "table_name": "watch",
                "endpoint": {
                    "path": "/snippets/{workspace}/{encoded_id}/watch",
                    "params": {
                        "encoded_id": {
                            "type": "resolve",
                            "resource": "get_snippetsworkspace",
                            "field": "id",
                        },
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of webhooks installed on this repository.
            {
                "name": "get_repositoriesworkspacerepo_slughooks",
                "table_name": "webhook_subscription",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/repositories/{workspace}/{repo_slug}/hooks",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the webhook with the specified id installed on the specified repository.
            {
                "name": "get_repositoriesworkspacerepo_slughooksuid",
                "table_name": "webhook_subscription",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories/{workspace}/{repo_slug}/hooks/{uid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "uid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a paginated list of webhooks installed on this workspace.
            {
                "name": "get_workspacesworkspacehooks",
                "table_name": "webhook_subscription",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/hooks",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the webhook with the specified id installed on the given workspace.
            {
                "name": "get_workspacesworkspacehooksuid",
                "table_name": "webhook_subscription",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}/hooks/{uid}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "uid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of workspaces accessible by the authenticated user.  Example:  ``` $ curl https://api.bitbucket.org/2.0/workspaces  {   "pagelen": 10,   "page": 1,   "size": 1,   "values": [     {         "uuid": "{a15fb181-db1f-48f7-b41f-e1eff06929d6}",         "links": {             "owners": {                 "href": "https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members?q=permission%3D%22owner%22"             },             "self": {                 "href": "https://api.bitbucket.org/2.0/workspaces/bbworkspace1"             },             "repositories": {                 "href": "https://api.bitbucket.org/2.0/repositories/bbworkspace1"             },             "snippets": {                 "href": "https://api.bitbucket.org/2.0/snippets/bbworkspace1"             },             "html": {                 "href": "https://bitbucket.org/bbworkspace1/"             },             "avatar": {                 "href": "https://bitbucket.org/workspaces/bbworkspace1/avatar/?ts=1543465801"             },             "members": {                 "href": "https://api.bitbucket.org/2.0/workspaces/bbworkspace1/members"             },             "projects": {                 "href": "https://api.bitbucket.org/2.0/workspaces/bbworkspace1/projects"             }         },         "created_on": "2018-11-14T19:15:05.058566+00:00",         "type": "workspace",         "slug": "bbworkspace1",         "is_private": true,         "name": "Atlassian Bitbucket"     }   ] } ```  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by workspace or permission by adding the following query string parameters:  * `q=slug="bbworkspace1"` or `q=is_private=true` * `sort=created_on`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.  **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information, see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**
            {
                "name": "get_workspaces",
                "table_name": "workspace",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces",
                },
            },
            # Returns the requested workspace.
            {
                "name": "get_workspacesworkspace",
                "table_name": "workspace",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns an object for each workspace the caller is a member of, and their effective role - the highest level of privilege the caller has. If a user is a member of multiple groups with distinct roles, only the highest level is returned.  Permissions can be:  * `owner` * `collaborator` * `member`  **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information, see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**  Example:  ``` $ curl https://api.bitbucket.org/2.0/user/permissions/workspaces  {   "pagelen": 10,   "page": 1,   "size": 1,   "values": [     {       "type": "workspace_membership",       "permission": "owner",       "last_accessed": "2019-03-07T12:35:02.900024+00:00",       "added_on": "2018-10-11T17:42:02.961424+00:00",       "user": {         "type": "user",         "uuid": "{470c176d-3574-44ea-bb41-89e8638bcca4}",         "nickname": "evzijst",         "display_name": "Erik van Zijst",       },       "workspace": {         "type": "workspace",         "uuid": "{a15fb181-db1f-48f7-b41f-e1eff06929d6}",         "slug": "bbworkspace1",         "name": "Atlassian Bitbucket",       }     }   ] } ```  Results may be further [filtered or sorted](/cloud/bitbucket/rest/intro/#filtering) by workspace or permission by adding the following query string parameters:  * `q=workspace.slug="bbworkspace1"` or `q=permission="owner"` * `sort=workspace.slug`  Note that the query parameter values need to be URL escaped so that `=` would become `%3D`.
            {
                "name": "get_userpermissionsworkspaces",
                "table_name": "workspace_membership",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/user/permissions/workspaces",
                },
            },
            # Returns all members of the requested workspace.
            {
                "name": "get_workspacesworkspacemembers",
                "table_name": "workspace_membership",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/members",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the workspace membership, which includes a `User` object for the member and a `Workspace` object for the requested workspace.
            {
                "name": "get_workspacesworkspacemembersmember",
                "table_name": "workspace_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/workspaces/{workspace}/members/{member}",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "member": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the list of members in a workspace and their permission levels. Permission can be: * `owner` * `collaborator` * `member`  **The `collaborator` role is being removed from the Bitbucket Cloud API. For more information, see the [deprecation announcement](/cloud/bitbucket/deprecation-notice-collaborator-role/).**  Example:  ``` $ curl -X https://api.bitbucket.org/2.0/workspaces/bbworkspace1/permissions  {     "pagelen": 10,     "values": [         {             "permission": "owner",             "type": "workspace_membership",             "user": {                 "type": "user",                 "uuid": "{470c176d-3574-44ea-bb41-89e8638bcca4}",                 "display_name": "Erik van Zijst",             },             "workspace": {                 "type": "workspace",                 "uuid": "{a15fb181-db1f-48f7-b41f-e1eff06929d6}",                 "slug": "bbworkspace1",                 "name": "Atlassian Bitbucket",             }         },         {             "permission": "member",             "type": "workspace_membership",             "user": {                 "type": "user",                 "nickname": "seanaty",                 "display_name": "Sean Conaty",                 "uuid": "{504c3b62-8120-4f0c-a7bc-87800b9d6f70}"             },             "workspace": {                 "type": "workspace",                 "uuid": "{a15fb181-db1f-48f7-b41f-e1eff06929d6}",                 "slug": "bbworkspace1",                 "name": "Atlassian Bitbucket",             }         }     ],     "page": 1,     "size": 2 } ```  Results may be further [filtered](/cloud/bitbucket/rest/intro/#filtering) by permission by adding the following query string parameters:  * `q=permission="owner"`
            {
                "name": "get_workspacesworkspacepermissions",
                "table_name": "workspace_membership",
                "endpoint": {
                    "data_selector": "values",
                    "path": "/workspaces/{workspace}/permissions",
                    "params": {
                        "workspace": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
