from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="clubhouse_api_source", max_table_nesting=2)
def clubhouse_api_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            {
                "name": "check_for_update",
                "table_name": "check_for_update",
                "endpoint": {
                    "path": "/check_for_update",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_testflight": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_actionable_notification",
                "table_name": "get_actionable_notification",
                "endpoint": {
                    "path": "/get_actionable_notifications",
                },
            },
            {
                "name": "get_all_topic",
                "table_name": "get_all_topic",
                "endpoint": {
                    "path": "/get_all_topics",
                },
            },
            {
                "name": "get_channel",
                "table_name": "get_channel",
                "endpoint": {
                    "path": "/get_channels",
                },
            },
            {
                "name": "get_event",
                "table_name": "get_event",
                "endpoint": {
                    "path": "/get_events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_filtered": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_notification",
                "table_name": "get_notification",
                "endpoint": {
                    "path": "/get_notifications",
                    "params": {
                        # the parameters below can optionally be configured
                        # "page_size": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_setting",
                "table_name": "get_setting",
                "endpoint": {
                    "path": "/get_settings",
                },
            },
            {
                "name": "get_suggested_follows_all",
                "table_name": "get_suggested_follows_all",
                "endpoint": {
                    "path": "/get_suggested_follows_all",
                    "params": {
                        # the parameters below can optionally be configured
                        # "in_onboarding": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_users_for_topic",
                "table_name": "get_users_for_topic",
                "endpoint": {
                    "path": "/get_users_for_topic",
                    "params": {
                        # the parameters below can optionally be configured
                        # "topic_id": "OPTIONAL_CONFIG",
                        # "page_size": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_welcome_channel",
                "table_name": "get_welcome_channel",
                "endpoint": {
                    "path": "/get_welcome_channel",
                },
            },
        ],
    }

    return rest_api_source(source_config)
