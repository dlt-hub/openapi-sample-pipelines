from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="circleci_source", max_table_nesting=2)
def circleci_source(
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
                "name": "circle-token",
                "location": "query",
            },
            "paginator": {
                "type": "offset",
                "limit": 100,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            # List the artifacts produced by a given build.
            {
                "name": "get_projectusernameprojectbuild_numartifacts",
                "table_name": "artifact",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}/{build_num}/artifacts",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "build_num": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Build summary for each of the last 30 builds for a single git repo.
            {
                "name": "get_projectusernameproject",
                "table_name": "build",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Build summary for each of the last 30 recent builds, ordered by build_num.
            {
                "name": "get_recent_builds",
                "table_name": "build",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/recent-builds",
                },
            },
            # Full details for a single build. The response includes all of the fields from the build summary. This is also the payload for the [notification webhooks](/docs/configuration/#notify), in which case this object is the value to a key named 'payload'.
            {
                "name": "get_projectusernameprojectbuild_num",
                "table_name": "build_detail",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}/{build_num}",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "build_num": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the environment variables for :project
            {
                "name": "get_projectusernameprojectenvvar",
                "table_name": "envvar",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}/envvar",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the hidden value of environment variable :name
            {
                "name": "get_projectusernameprojectenvvarname",
                "table_name": "envvar",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}/envvar/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "get_projectusernameprojectenvvar",
                            "field": "name",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists checkout keys.
            {
                "name": "get_projectusernameprojectcheckout_key",
                "table_name": "key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}/checkout-key",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get a checkout key.
            {
                "name": "get_projectusernameprojectcheckout_keyfingerprint",
                "table_name": "key",
                "primary_key": "fingerprint",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/project/{username}/{project}/checkout-key/{fingerprint}",
                    "params": {
                        "fingerprint": {
                            "type": "resolve",
                            "resource": "get_projectusernameprojectcheckout_key",
                            "field": "fingerprint",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Provides information about the signed in user.
            {
                "name": "get_me",
                "table_name": "me",
                "endpoint": {
                    "data_selector": "all_emails",
                    "path": "/me",
                },
            },
            # List of all the projects you're following on CircleCI, with build information organized by branch.
            {
                "name": "get_projects",
                "table_name": "project",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects",
                },
            },
            # Provides test metadata for a build Note: [Learn how to set up your builds to collect test metadata](https://circleci.com/docs/test-metadata/)
            {
                "name": "get_projectusernameprojectbuild_numtests",
                "table_name": "test",
                "endpoint": {
                    "data_selector": "tests",
                    "path": "/project/{username}/{project}/{build_num}/tests",
                    "params": {
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "project": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "build_num": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
