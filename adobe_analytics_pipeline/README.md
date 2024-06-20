# adobe_analytics pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/adobe_analytics.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /calculatedmetrics_ 
  *resource*: find_calculated_metrics  
  *description*: A calculated metric response will always include these default items: *id, name, description, rsid, owner, polarity, precision, type*  Other attributes can be optionally requested through the 'expansion' field:  * *modified*: Date that the metric was last modified (ISO 8601) * *definition*: Calculated metric definition as JSON object * *compatibility*: Products that the metric is compatible with * *reportSuiteName*: Also return the friendly Report Suite name for the RSID * *tags*: Gives all existing tags associated with the calculated metric  For more information about calculated metrics go [here](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/calculatedmetrics.md)  
* _GET /calculatedmetrics/{id}_ 
  *resource*: find_one_calculated_metric  
  *description*: A calculated metric response will always include these default items: *id, name, description, rsid, owner, polarity, precision, type*  Other attributes can be optionally requested through the 'expansion' field:  * *modified*: Date that the metric was last modified (ISO 8601) * *definition*: Calculated metric definition as JSON object * *compatibility*: Products that the metric is compatible with * *reportSuiteName*: Also return the friendly Report Suite name for the RSID * *tags*: Gives all existing tags associated with the calculated metric  For more information about calculated metrics go [here](https://github.com/AdobeDocs/analytics-2.0-apis/blob/master/calculatedmetrics.md)  
* _GET /dateranges/{dateRangeId}_ 
  *resource*: get_date_range  
* _GET /dimensions_ 
  *resource*: dimensions_get_dimensions  
* _GET /dimensions/{dimensionId}_ 
  *resource*: dimensions_get_dimension  
* _GET /metrics/{id}_ 
  *resource*: get_metric  
* _GET /segments/{id}_ 
  *resource*: segments_get_segment  
* _GET /users_ 
  *resource*: find_all_users  
  *description*: Retrieves a list of all users for the company designated by the auth token.
* _GET /users/me_ 
  *resource*: get_current_user  
* _GET /metrics_ 
  *resource*: get_metrics  
  *description*: This returns the metrics list primarily for the Analytics product. The platform identity API Returns a list of all possible metrics for the supported systems.
* _GET /collections/suites_ 
  *resource*: get_collections  
  *description*: Returns all report suite types in a single collection.
* _GET /collections/suites/{rsid}_ 
  *resource*: find_one  
  *description*: Returns all report suite types in a single collection.
* _GET /dateranges_ 
  *resource*: get_date_ranges  
  *description*: This API allows users to store commonly used date ranges so that they can be reused throughout the product.
* _GET /segments_ 
  *resource*: segments_get_segments  
* _GET /auditlogs/usage_ 
  *resource*: get_usage_logs  
  *description*: This API returns the usage and access logs for a given date range within a 3 month period. This API authenticates with an IMS user token.
