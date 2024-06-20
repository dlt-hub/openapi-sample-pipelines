# mercedes_benz_traffic_signs pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/mercedes_benz_traffic_signs.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /geojson_ 
  *resource*: geojson  
  *description*: This endpoint returns the uuid of the GeoJSON object and the GeoJSON object itself that is predefined for the user. The object is used to restrict the area of data retrieval. The response does not incorporate any geolocation filters.
* _GET /trafficsigns_ 
  *resource*: trafficsign  
  *description*: This endpoint returns a set of traffic signs restricted to the predefined area of the user. The traffic signs data is returned in a paged response. If there are no traffic signs in the defined area, an empty list is returned. Note that missing fields in individual traffic sign data are returned as `null` values. To additionally limit the returned data, a bounding box can be defined as geolocation filter. The bounding box is defined by two points, each represented by a longitude and a latitude coordinate. The first point is defined by the longitudePoint1 and latitudePoint1 query parameters. The second point is defined by the longitudePoint2 and latitudePoint2 query parameters. All four query parameters are optional, but if one of them is provided, all four must be provided to define a bounding box as geolocation filter.
