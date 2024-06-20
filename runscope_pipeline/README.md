# runscope pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/runscope.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /account_ 
  *resource*: get_account  
  *description*: Information about the authorized account.
* _GET /teams/{teamId}/agents_ 
  *resource*: get_teamsteam_idagents  
  *description*: List currently connected agents associated with a given team.
* _GET /buckets_ 
  *resource*: get_buckets  
* _GET /buckets/{bucketKey}_ 
  *resource*: get_bucketsbucket_key  
* _GET /buckets/{bucketKey}/environments_ 
  *resource*: get_bucketsbucket_keyenvironments  
* _GET /buckets/{bucketKey}/tests/{testId}/environments_ 
  *resource*: get_bucketsbucket_keyteststest_idenvironments  
* _GET /buckets/{bucketKey}/errors_ 
  *resource*: get_bucketsbucket_keyerrors  
* _GET /teams/{teamId}/integrations_ 
  *resource*: get_teamsteam_idintegrations  
  *description*: Returns a list of integrations configured for the team.
* _GET /buckets/{bucketKey}/messages_ 
  *resource*: get_bucketsbucket_keymessages  
* _GET /buckets/{bucketKey}/messages/{messageId}_ 
  *resource*: get_bucketsbucket_keymessagesmessage_id  
* _GET /buckets/{bucketKey}/tests/{testId}/metrics_ 
  *resource*: get_bucketsbucket_keyteststest_idmetrics  
* _GET /teams/{teamId}/people_ 
  *resource*: get_teamsteam_idpeople  
  *description*: List people and integrations associated with a given team.
* _GET /buckets/{bucketKey}/tests/{testId}/steps_ 
  *resource*: get_bucketsbucket_keyteststest_idsteps  
* _GET /buckets/{bucketKey}/tests_ 
  *resource*: get_bucketsbucket_keytests  
* _GET /buckets/{bucketKey}/tests/{testId}_ 
  *resource*: get_bucketsbucket_keyteststest_id  
