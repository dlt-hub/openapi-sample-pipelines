# visible_thread pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/visible_thread.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /dictionaries_ 
  *resource*: get_dictionaries  
  *description*: Get your list of dictionaries
* _GET /documents_ 
  *resource*: get_documents  
  *description*: Get your list of documents
* _GET /documents/{docId}_ 
  *resource*: get_doc_by_id  
  *description*: Get data from a previously submitted document identified by ***docId***
* _GET /searches_ 
  *resource*: get_searches  
  *description*: Get your list of searches
* _GET /searches/{docId}/{dictionaryId}_ 
  *resource*: get_search_results  
  *description*: Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** & **urlId**
* _GET /webscans/{scanId}/webUrls/{urlId}_ 
  *resource*: get_scan_url_by_id  
  *description*: Get detailed results for a scan/url (readability, long sentence and passive language instances), identified by **scanId** & **urlId**
* _GET /webscans_ 
  *resource*: get_webscans  
  *description*: Get your list of scans
* _GET /webscans/{scanId}_ 
  *resource*: get_scan_by_id  
  *description*: Get data from a previously run scan, identified by **scanId**
