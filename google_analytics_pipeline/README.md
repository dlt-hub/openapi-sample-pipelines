# google_analytics pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/google_analytics.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /management/accounts_ 
  *resource*: analytics_management_accounts_list  
  *description*: Lists all accounts to which the user has access.
* _GET /management/accountSummaries_ 
  *resource*: analytics_management_account_summaries_list  
  *description*: Lists account summaries (lightweight tree comprised of accounts/properties/profiles) to which the user has access.
* _GET /metadata/{reportType}/columns_ 
  *resource*: analytics_metadata_columns_list  
  *description*: Lists all columns for a report type
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources_ 
  *resource*: analytics_management_custom_data_sources_list  
  *description*: List custom data sources to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions_ 
  *resource*: analytics_management_custom_dimensions_list  
  *description*: Lists custom dimensions to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customDimensions/{customDimensionId}_ 
  *resource*: analytics_management_custom_dimensions_get  
  *description*: Get a custom dimension to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics_ 
  *resource*: analytics_management_custom_metrics_list  
  *description*: Lists custom metrics to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customMetrics/{customMetricId}_ 
  *resource*: analytics_management_custom_metrics_get  
  *description*: Get a custom metric to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks_ 
  *resource*: analytics_management_web_property_ad_words_links_list  
  *description*: Lists webProperty-Google Ads links for a given web property.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/entityAdWordsLinks/{webPropertyAdWordsLinkId}_ 
  *resource*: analytics_management_web_property_ad_words_links_get  
  *description*: Returns a web property-Google Ads link to which the user has access.
* _GET /management/accounts/{accountId}/entityUserLinks_ 
  *resource*: analytics_management_account_user_links_list  
  *description*: Lists account-user links for a given account.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/entityUserLinks_ 
  *resource*: analytics_management_webproperty_user_links_list  
  *description*: Lists webProperty-user links for a given web property.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/entityUserLinks_ 
  *resource*: analytics_management_profile_user_links_list  
  *description*: Lists profile-user links for a given view (profile).
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments_ 
  *resource*: analytics_management_experiments_list  
  *description*: Lists experiments to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/experiments/{experimentId}_ 
  *resource*: analytics_management_experiments_get  
  *description*: Returns an experiment to which the user has access.
* _GET /management/accounts/{accountId}/filters_ 
  *resource*: analytics_management_filters_list  
  *description*: Lists all filters for an account
* _GET /management/accounts/{accountId}/filters/{filterId}_ 
  *resource*: analytics_management_filters_get  
  *description*: Returns filters to which the user has access.
* _GET /data/ga_ 
  *resource*: analytics_data_ga_get  
  *description*: Returns Analytics data for a view (profile).
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals_ 
  *resource*: analytics_management_goals_list  
  *description*: Lists goals to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/goals/{goalId}_ 
  *resource*: analytics_management_goals_get  
  *description*: Gets a goal to which the user has access.
* _GET /data/mcf_ 
  *resource*: analytics_data_mcf_get  
  *description*: Returns Analytics Multi-Channel Funnels data for a view (profile).
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles_ 
  *resource*: analytics_management_profiles_list  
  *description*: Lists views (profiles) to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}_ 
  *resource*: analytics_management_profiles_get  
  *description*: Gets a view (profile) to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks_ 
  *resource*: analytics_management_profile_filter_links_list  
  *description*: Lists all profile filter links for a profile.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/profileFilterLinks/{linkId}_ 
  *resource*: analytics_management_profile_filter_links_get  
  *description*: Returns a single profile filter link.
* _GET /data/realtime_ 
  *resource*: analytics_data_realtime_get  
  *description*: Returns real time data for a view (profile).
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences_ 
  *resource*: analytics_management_remarketing_audience_list  
  *description*: Lists remarketing audiences to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/remarketingAudiences/{remarketingAudienceId}_ 
  *resource*: analytics_management_remarketing_audience_get  
  *description*: Gets a remarketing audience to which the user has access.
* _GET /management/segments_ 
  *resource*: analytics_management_segments_list  
  *description*: Lists segments to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports_ 
  *resource*: analytics_management_unsampled_reports_list  
  *description*: Lists unsampled reports to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/profiles/{profileId}/unsampledReports/{unsampledReportId}_ 
  *resource*: analytics_management_unsampled_reports_get  
  *description*: Returns a single unsampled report.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads_ 
  *resource*: analytics_management_uploads_list  
  *description*: List uploads to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}/customDataSources/{customDataSourceId}/uploads/{uploadId}_ 
  *resource*: analytics_management_uploads_get  
  *description*: List uploads to which the user has access.
* _GET /management/accounts/{accountId}/webproperties_ 
  *resource*: analytics_management_webproperties_list  
  *description*: Lists web properties to which the user has access.
* _GET /management/accounts/{accountId}/webproperties/{webPropertyId}_ 
  *resource*: analytics_management_webproperties_get  
  *description*: Gets a web property to which the user has access.
