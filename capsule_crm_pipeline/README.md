# capsule_crm pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/capsule_crm.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /api/v2/kases_ 
  *resource*: list_cases  
  *description*: https://developer.capsulecrm.com/v2/operations/Case#listCases
* _GET /api/v2/kases/search_ 
  *resource*: search_cases  
  *description*: https://developer.capsulecrm.com/v2/operations/Case#searchCases
* _GET /api/v2/kases/{caseId}_ 
  *resource*: show_case  
  *description*: https://developer.capsulecrm.com/v2/operations/Case#showCase
* _GET /api/v2/parties/{partyId}/kases_ 
  *resource*: list_cases_by_party  
  *description*: https://developer.capsulecrm.com/v2/operations/Case#listCasesByParty
* _GET /api/v2/opportunities_ 
  *resource*: list_opportunities  
  *description*: https://developer.capsulecrm.com/v2/operations/Opportunity#listOpportunities
* _GET /api/v2/opportunities/search_ 
  *resource*: search_opportunities  
  *description*: https://developer.capsulecrm.com/v2/operations/Opportunity#searchOpportunities
* _GET /api/v2/opportunities/{opportunityId}_ 
  *resource*: show_opportunity  
  *description*: https://developer.capsulecrm.com/v2/operations/Opportunity#showOpportunity
* _GET /api/v2/parties/{partyId}/opportunities_ 
  *resource*: list_opportunities_by_party  
  *description*: https://developer.capsulecrm.com/v2/operations/Opportunity#listOpportunitiesByParty
* _GET /api/v2/parties_ 
  *resource*: list_parties  
  *description*: https://developer.capsulecrm.com/v2/operations/Party#listParties
* _GET /api/v2/parties/search_ 
  *resource*: search_parties  
  *description*: https://developer.capsulecrm.com/v2/operations/Party#searchParties
* _GET /api/v2/parties/{partyId}_ 
  *resource*: show_party  
  *description*: https://developer.capsulecrm.com/v2/operations/Party#showParty
* _GET /api/v2/tasks_ 
  *resource*: list_tasks  
  *description*: https://developer.capsulecrm.com/v2/operations/Task#listTasks
