# circleci pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/circleci.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /project/{username}/{project}/{build_num}/artifacts_ 
  *resource*: get_projectusernameprojectbuild_numartifacts  
  *description*: List the artifacts produced by a given build. 
* _GET /project/{username}/{project}_ 
  *resource*: get_projectusernameproject  
  *description*: Build summary for each of the last 30 builds for a single git repo. 
* _GET /recent-builds_ 
  *resource*: get_recent_builds  
  *description*: Build summary for each of the last 30 recent builds, ordered by build_num. 
* _GET /project/{username}/{project}/{build_num}_ 
  *resource*: get_projectusernameprojectbuild_num  
  *description*: Full details for a single build. The response includes all of the fields from the build summary. This is also the payload for the [notification webhooks](/docs/configuration/#notify), in which case this object is the value to a key named 'payload'. 
* _GET /project/{username}/{project}/envvar_ 
  *resource*: get_projectusernameprojectenvvar  
  *description*: Lists the environment variables for :project 
* _GET /project/{username}/{project}/envvar/{name}_ 
  *resource*: get_projectusernameprojectenvvarname  
  *description*: Gets the hidden value of environment variable :name 
* _GET /project/{username}/{project}/checkout-key_ 
  *resource*: get_projectusernameprojectcheckout_key  
  *description*: Lists checkout keys. 
* _GET /project/{username}/{project}/checkout-key/{fingerprint}_ 
  *resource*: get_projectusernameprojectcheckout_keyfingerprint  
  *description*: Get a checkout key. 
* _GET /me_ 
  *resource*: get_me  
  *description*: Provides information about the signed in user. 
* _GET /projects_ 
  *resource*: get_projects  
  *description*: List of all the projects you're following on CircleCI, with build information organized by branch. 
* _GET /project/{username}/{project}/{build_num}/tests_ 
  *resource*: get_projectusernameprojectbuild_numtests  
  *description*: Provides test metadata for a build Note: [Learn how to set up your builds to collect test metadata](https://circleci.com/docs/test-metadata/) 
