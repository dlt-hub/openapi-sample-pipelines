# google_ads pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/google_ads.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /v2/accounts_ 
  *resource*: v2_accounts  
  *description*: Lists all accounts available to this user.
* _GET /v2/{parent}:listChildAccounts_ 
  *resource*: v_2_parentlist_child_accounts  
  *description*: Lists all accounts directly managed by the given AdSense account.
* _GET /v2/{name}/adBlockingRecoveryTag_ 
  *resource*: v_2_ad_blocking_recovery_tag  
  *description*: Gets the ad blocking recovery tag of an account.
* _GET /v2/{parent}/adclients_ 
  *resource*: v2_adclients  
  *description*: Lists all the ad clients available in an account.
* _GET /v2/{parent}/adunits_ 
  *resource*: v2_adunits  
  *description*: Lists all ad units under a specified account and ad client.
* _GET /v2/{parent}:listLinkedAdUnits_ 
  *resource*: v_2_parentlist_linked_ad_units  
  *description*: Lists all the ad units available for a custom channel.
* _GET /v2/{name}/adcode_ 
  *resource*: v2_adcode  
  *description*: Gets the ad unit code for a given ad unit. For more information, see [About the AdSense code](https://support.google.com/adsense/answer/9274634) and [Where to place the ad code in your HTML](https://support.google.com/adsense/answer/9190028).
* _GET /v2/{parent}/alerts_ 
  *resource*: v2_alerts  
  *description*: Lists all the alerts available in an account.
* _GET /v2/{parent}/customchannels_ 
  *resource*: v2_customchannels  
  *description*: Lists all the custom channels available in an ad client.
* _GET /v2/{parent}:listLinkedCustomChannels_ 
  *resource*: v_2_parentlist_linked_custom_channels  
  *description*: Lists all the custom channels available for an ad unit.
* _GET /v2/{account}/reports:generate_ 
  *resource*: v2_reportsgenerate  
  *description*: Generates an ad hoc report.
* _GET /v2/{name}/saved:generate_ 
  *resource*: v2_savedgenerate  
  *description*: Generates a saved report.
* _GET /v2/{parent}/payments_ 
  *resource*: v2_payments  
  *description*: Lists all the payments available for an account.
* _GET /v2/{account}/reports:generateCsv_ 
  *resource*: v_2_reportsgenerate_csv  
  *description*: Generates a csv formatted ad hoc report.
* _GET /v2/{name}/saved_ 
  *resource*: v2_saved  
  *description*: Gets the saved report from the given resource name.
* _GET /v2/{parent}/reports/saved_ 
  *resource*: v2_reports_saved  
  *description*: Lists saved reports.
* _GET /v2/{name}/saved:generateCsv_ 
  *resource*: v_2_savedgenerate_csv  
  *description*: Generates a csv formatted saved report.
* _GET /v2/{name}_ 
  *resource*: v2  
  *description*: Gets information about the selected site.
* _GET /v2/{parent}/sites_ 
  *resource*: v2_sites  
  *description*: Lists all the sites available in an account.
* _GET /v2/{parent}/urlchannels_ 
  *resource*: v2_urlchannels  
  *description*: Lists active url channels.
