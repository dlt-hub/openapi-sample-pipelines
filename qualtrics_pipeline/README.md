# qualtrics pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/qualtrics.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /distributions_ 
  *resource*: distribution  
  *description*: Gets all distributions for a given survey
* _GET /eventsubscriptions/{SubscriptionId}_ 
  *resource*: event_subscriptions_response  
  *description*: Get event subscriptions
* _GET /distributions/{DistributionId}/links_ 
  *resource*: link  
  *description*: Retrieves all the individual links for a given distribution
* _GET /survey-definitions/{SurveyId}_ 
  *resource*: survey_response  
  *description*: Gets a single Qualtrics survey speficied by its ID
