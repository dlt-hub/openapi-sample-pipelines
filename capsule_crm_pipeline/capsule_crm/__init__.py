from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="capsule_crm_source", max_table_nesting=2)
def capsule_crm_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # https://developer.capsulecrm.com/v2/operations/Case#listCases
            {
                "name": "list_cases",
                "table_name": "case",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kases",
                    "path": "/api/v2/kases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Case#searchCases
            {
                "name": "search_cases",
                "table_name": "case",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kases",
                    "path": "/api/v2/kases/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Case#showCase
            {
                "name": "show_case",
                "table_name": "case",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kase",
                    "path": "/api/v2/kases/{caseId}",
                    "params": {
                        "caseId": {
                            "type": "resolve",
                            "resource": "list_cases",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Case#listCasesByParty
            {
                "name": "list_cases_by_party",
                "table_name": "case",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kases",
                    "path": "/api/v2/parties/{partyId}/kases",
                    "params": {
                        "partyId": {
                            "type": "resolve",
                            "resource": "list_parties",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Opportunity#listOpportunities
            {
                "name": "list_opportunities",
                "table_name": "opportunity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "opportunities",
                    "path": "/api/v2/opportunities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Opportunity#searchOpportunities
            {
                "name": "search_opportunities",
                "table_name": "opportunity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "opportunities",
                    "path": "/api/v2/opportunities/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Opportunity#showOpportunity
            {
                "name": "show_opportunity",
                "table_name": "opportunity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "opportunity",
                    "path": "/api/v2/opportunities/{opportunityId}",
                    "params": {
                        "opportunityId": {
                            "type": "resolve",
                            "resource": "list_opportunities",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Opportunity#listOpportunitiesByParty
            {
                "name": "list_opportunities_by_party",
                "table_name": "opportunity",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "opportunities",
                    "path": "/api/v2/parties/{partyId}/opportunities",
                    "params": {
                        "partyId": {
                            "type": "resolve",
                            "resource": "list_parties",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Party#listParties
            {
                "name": "list_parties",
                "table_name": "party",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "parties",
                    "path": "/api/v2/parties",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Party#searchParties
            {
                "name": "search_parties",
                "table_name": "party",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "parties",
                    "path": "/api/v2/parties/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Party#showParty
            {
                "name": "show_party",
                "table_name": "party",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "party",
                    "path": "/api/v2/parties/{partyId}",
                    "params": {
                        "partyId": {
                            "type": "resolve",
                            "resource": "list_parties",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "embed": "OPTIONAL_CONFIG",
                    },
                },
            },
            # https://developer.capsulecrm.com/v2/operations/Task#listTasks
            {
                "name": "list_tasks",
                "table_name": "task",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tasks",
                    "path": "/api/v2/tasks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "perPage": "OPTIONAL_CONFIG",
                        # "embed": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
