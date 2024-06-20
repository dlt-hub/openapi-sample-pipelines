from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="runscope_source", max_table_nesting=2)
def runscope_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Information about the authorized account.
            {
                "name": "get_account",
                "table_name": "account",
                "endpoint": {
                    "path": "/account",
                    "paginator": "auto",
                },
            },
            # List currently connected agents associated with a given team.
            {
                "name": "get_teamsteam_idagents",
                "table_name": "agent",
                "endpoint": {
                    "path": "/teams/{teamId}/agents",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_buckets",
                "table_name": "bucket",
                "endpoint": {
                    "path": "/buckets",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_key",
                "table_name": "bucket",
                "endpoint": {
                    "path": "/buckets/{bucketKey}",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keyenvironments",
                "table_name": "environment",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/environments",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keyteststest_idenvironments",
                "table_name": "environment",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/tests/{testId}/environments",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "testId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keyerrors",
                "table_name": "error",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/errors",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of integrations configured for the team.
            {
                "name": "get_teamsteam_idintegrations",
                "table_name": "integration",
                "endpoint": {
                    "path": "/teams/{teamId}/integrations",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keymessages",
                "table_name": "message",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/messages",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "count": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keymessagesmessage_id",
                "table_name": "message",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/messages/{messageId}",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "messageId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keyteststest_idmetrics",
                "table_name": "metric",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/tests/{testId}/metrics",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "testId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # List people and integrations associated with a given team.
            {
                "name": "get_teamsteam_idpeople",
                "table_name": "person",
                "endpoint": {
                    "path": "/teams/{teamId}/people",
                    "params": {
                        "teamId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keyteststest_idsteps",
                "table_name": "step",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/tests/{testId}/steps",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "testId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keytests",
                "table_name": "test",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/tests",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bucketsbucket_keyteststest_id",
                "table_name": "test",
                "endpoint": {
                    "path": "/buckets/{bucketKey}/tests/{testId}",
                    "params": {
                        "bucketKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "testId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
