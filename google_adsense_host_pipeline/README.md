# google_adsense_host pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/google_adsense_host.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /accounts_ 
  *resource*: adsensehost_accounts_list  
  *description*: List hosted accounts associated with this AdSense account by ad client id.
* _GET /accounts/{accountId}_ 
  *resource*: adsensehost_accounts_get  
  *description*: Get information about the selected associated AdSense account.
* _GET /accounts/{accountId}/adclients_ 
  *resource*: adsensehost_accounts_adclients_list  
  *description*: List all hosted ad clients in the specified hosted account.
* _GET /accounts/{accountId}/adclients/{adClientId}_ 
  *resource*: adsensehost_accounts_adclients_get  
  *description*: Get information about one of the ad clients in the specified publisher's AdSense account.
* _GET /adclients_ 
  *resource*: adsensehost_adclients_list  
  *description*: List all host ad clients in this AdSense account.
* _GET /adclients/{adClientId}_ 
  *resource*: adsensehost_adclients_get  
  *description*: Get information about one of the ad clients in the Host AdSense account.
* _GET /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}/adcode_ 
  *resource*: adsensehost_accounts_adunits_get_ad_code  
  *description*: Get ad code for the specified ad unit, attaching the specified host custom channels.
* _GET /accounts/{accountId}/adclients/{adClientId}/adunits_ 
  *resource*: adsensehost_accounts_adunits_list  
  *description*: List all ad units in the specified publisher's AdSense account.
* _GET /accounts/{accountId}/adclients/{adClientId}/adunits/{adUnitId}_ 
  *resource*: adsensehost_accounts_adunits_get  
  *description*: Get the specified host ad unit in this AdSense account.
* _GET /adclients/{adClientId}/customchannels_ 
  *resource*: adsensehost_customchannels_list  
  *description*: List all host custom channels in this AdSense account.
* _GET /adclients/{adClientId}/customchannels/{customChannelId}_ 
  *resource*: adsensehost_customchannels_get  
  *description*: Get a specific custom channel from the host AdSense account.
* _GET /accounts/{accountId}/reports_ 
  *resource*: adsensehost_accounts_reports_generate  
  *description*: Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.
* _GET /reports_ 
  *resource*: adsensehost_reports_generate  
  *description*: Generate an AdSense report based on the report request sent in the query parameters. Returns the result as JSON; to retrieve output in CSV format specify "alt=csv" as a query parameter.
* _GET /associationsessions/start_ 
  *resource*: adsensehost_associationsessions_start  
  *description*: Create an association session for initiating an association with an AdSense user.
* _GET /adclients/{adClientId}/urlchannels_ 
  *resource*: adsensehost_urlchannels_list  
  *description*: List all host URL channels in the host AdSense account.
* _GET /associationsessions/verify_ 
  *resource*: adsensehost_associationsessions_verify  
  *description*: Verify an association session after the association callback returns from AdSense signup.
