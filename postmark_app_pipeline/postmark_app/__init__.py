from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="postmark_app_source", max_table_nesting=2)
def postmark_app_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "get_bounces",
                "table_name": "bounce",
                "endpoint": {
                    "path": "/bounces",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "inactive": "OPTIONAL_CONFIG",
                        # "emailFilter": "OPTIONAL_CONFIG",
                        # "messageID": "OPTIONAL_CONFIG",
                        # "tag": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_single_bounce",
                "table_name": "bounce",
                "endpoint": {
                    "path": "/bounces/{bounceid}",
                    "params": {
                        "bounceid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bounce_counts",
                "table_name": "bounce",
                "endpoint": {
                    "path": "/stats/outbound/bounces",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_click_counts_by_browser_family",
                "table_name": "browserfamily",
                "endpoint": {
                    "path": "/stats/outbound/clicks/browserfamilies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "search_clicks_for_outbound_messages",
                "table_name": "click",
                "endpoint": {
                    "path": "/messages/outbound/clicks",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "recipient": "OPTIONAL_CONFIG",
                        # "tag": "OPTIONAL_CONFIG",
                        # "client_name": "OPTIONAL_CONFIG",
                        # "client_company": "OPTIONAL_CONFIG",
                        # "client_family": "OPTIONAL_CONFIG",
                        # "os_name": "OPTIONAL_CONFIG",
                        # "os_family": "OPTIONAL_CONFIG",
                        # "os_company": "OPTIONAL_CONFIG",
                        # "platform": "OPTIONAL_CONFIG",
                        # "country": "OPTIONAL_CONFIG",
                        # "region": "OPTIONAL_CONFIG",
                        # "city": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_clicks_for_single_outbound_message",
                "table_name": "click",
                "endpoint": {
                    "path": "/messages/outbound/clicks/{messageid}",
                    "params": {
                        "messageid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_click_counts",
                "table_name": "click",
                "endpoint": {
                    "path": "/stats/outbound/clicks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_delivery_stats",
                "table_name": "deliverystat",
                "endpoint": {
                    "path": "/deliverystats",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_inbound_message_details",
                "table_name": "detail",
                "endpoint": {
                    "path": "/messages/inbound/{messageid}/details",
                    "params": {
                        "messageid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_message_details",
                "table_name": "detail",
                "endpoint": {
                    "path": "/messages/outbound/{messageid}/details",
                    "params": {
                        "messageid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_bouncesbounceiddump",
                "table_name": "dump",
                "endpoint": {
                    "path": "/bounces/{bounceid}/dump",
                    "params": {
                        "bounceid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_message_dump",
                "table_name": "dump",
                "endpoint": {
                    "path": "/messages/outbound/{messageid}/dump",
                    "params": {
                        "messageid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_open_counts_by_email_client",
                "table_name": "emailclient",
                "endpoint": {
                    "path": "/stats/outbound/opens/emailclients",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "search_inbound_messages",
                "table_name": "inbound",
                "endpoint": {
                    "path": "/messages/inbound",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "recipient": "OPTIONAL_CONFIG",
                        # "fromemail": "OPTIONAL_CONFIG",
                        # "subject": "OPTIONAL_CONFIG",
                        # "mailboxhash": "OPTIONAL_CONFIG",
                        # "tag": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "list_inbound_rules",
                "table_name": "inboundrule",
                "endpoint": {
                    "path": "/triggers/inboundrules",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_click_counts_by_location",
                "table_name": "location",
                "endpoint": {
                    "path": "/stats/outbound/clicks/location",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "search_opens_for_outbound_messages",
                "table_name": "open",
                "endpoint": {
                    "path": "/messages/outbound/opens",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "recipient": "OPTIONAL_CONFIG",
                        # "tag": "OPTIONAL_CONFIG",
                        # "client_name": "OPTIONAL_CONFIG",
                        # "client_company": "OPTIONAL_CONFIG",
                        # "client_family": "OPTIONAL_CONFIG",
                        # "os_name": "OPTIONAL_CONFIG",
                        # "os_family": "OPTIONAL_CONFIG",
                        # "os_company": "OPTIONAL_CONFIG",
                        # "platform": "OPTIONAL_CONFIG",
                        # "country": "OPTIONAL_CONFIG",
                        # "region": "OPTIONAL_CONFIG",
                        # "city": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_opens_for_single_outbound_message",
                "table_name": "open",
                "endpoint": {
                    "path": "/messages/outbound/opens/{messageid}",
                    "params": {
                        "messageid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_open_counts",
                "table_name": "open",
                "endpoint": {
                    "path": "/stats/outbound/opens",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "search_outbound_messages",
                "table_name": "outbound",
                "endpoint": {
                    "path": "/messages/outbound",
                    "params": {
                        "count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "recipient": "OPTIONAL_CONFIG",
                        # "fromemail": "OPTIONAL_CONFIG",
                        # "tag": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_overview_statistics",
                "table_name": "outbound",
                "endpoint": {
                    "path": "/stats/outbound",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_click_counts_by_platform",
                "table_name": "platform",
                "endpoint": {
                    "path": "/stats/outbound/clicks/platforms",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_outbound_open_counts_by_platform",
                "table_name": "platform",
                "endpoint": {
                    "path": "/stats/outbound/opens/platforms",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sent_counts",
                "table_name": "send",
                "endpoint": {
                    "path": "/stats/outbound/sends",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_current_server_configuration",
                "table_name": "server",
                "endpoint": {
                    "path": "/server",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_spam_complaints",
                "table_name": "spam",
                "endpoint": {
                    "path": "/stats/outbound/spam",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "list_templates",
                "table_name": "template",
                "endpoint": {
                    "path": "/templates",
                    "params": {
                        "Count": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "Offset": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_single_template",
                "table_name": "template",
                "endpoint": {
                    "path": "/templates/{templateIdOrAlias}",
                    "params": {
                        "templateIdOrAlias": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_tracked_email_counts",
                "table_name": "tracked",
                "endpoint": {
                    "path": "/stats/outbound/tracked",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag": "OPTIONAL_CONFIG",
                        # "fromdate": "OPTIONAL_CONFIG",
                        # "todate": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
