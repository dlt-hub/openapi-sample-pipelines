# aviation_api pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/aviation_api.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /charts/afd_ 
  *resource*: afd  
  *description*: Search for AFD by ICAO or FAA identifier
* _GET /airports_ 
  *resource*: airport  
  *description*: Search for an airport by its ICAO or FAA identifier
* _GET /charts/changes_ 
  *resource*: change  
  *description*: Search for charts by ICAO or FAA identifier or chart name
* _GET /charts_ 
  *resource*: chart  
  *description*: Search for charts by ICAO or FAA identifier with optional grouping
* _GET /vatsim/controllers_ 
  *resource*: controller  
  *description*: Search for all the at a specified facility on VATSIM
* _GET /weather/metar_ 
  *resource*: metar  
  *description*: Search for an airport's METAR
* _GET /vatsim/pilots_ 
  *resource*: pilot  
  *description*: Search for all the arrivals and/or departures into an airport on VATSIM
* _GET /preferred-routes_ 
  *resource*: preferred_route  
  *description*: Get all of the preferred routes with no search parameters
* _GET /preferred-routes/search_ 
  *resource*: search  
  *description*: Search for preferred routes by various parameters. At least one search criteria is required, although a combination of any can be used
* _GET /weather/taf_ 
  *resource*: taf  
  *description*: Search for an airport's TAF
