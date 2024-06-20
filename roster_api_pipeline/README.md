# roster_api pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/roster_api.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /contact_ 
  *resource*: contact  
  *description*: Gets a contact's information by contactId, email or phone.               <b>Header requires</b>: "Authorization Bearer {accessToken}"
* _GET /get-request_ 
  *resource*: get_request  
  *description*: Gets the delayed processing results of a previous request that exceeded the wait limit. When a request in the API exceeds the wait limit, a RequestId will be provided in the API response. This RequestId can be used here to retrieve the json response of the associated endpoint that was called previously where processing exceeded the wait limit. This endpoint is typically only needed when using this API for real-time social data collection when a new contact is added to the system.  <b>Header requires</b>: "Authorization Bearer {accessToken}"  <b>Response Statuses</b>:  - <b>COMPLETED</b>: request completed successfully<br /> - <b>NEW</b>: request created<br /> - <b>IN_PROGRESS</b>: request is being processed. Try again in a few seconds.<br /> - <b>PROCESSING_LIMIT_EXCEEDED</b>: processing took too long and was terminated.<br /> - <b>ERROR</b>: error occurred during processing<br />
* _GET /program_ 
  *resource*: program  
  *description*: Returns a list of active programs.              <b>Header requires</b>: "Authorization Bearer {accessToken}"
