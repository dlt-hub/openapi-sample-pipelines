# kafka pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/kafka.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /api/v2/clusters/{clusterArn}_ 
  *resource*: cluster  
  *description*:              <p>Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.</p>          
* _GET /v1/clusters/{clusterArn}_ 
  *resource*: cluster_info  
  *description*:              <p>Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.</p>          
* _GET /v1/operations/{clusterOperationArn}_ 
  *resource*: cluster_operation_info  
  *description*:              <p>Returns a description of the cluster operation specified by the ARN.</p>          
* _GET /api/v2/operations/{clusterOperationArn}_ 
  *resource*: cluster_operation_v2  
  *description*:              <p>Returns a description of the cluster operation specified by the ARN.</p> 
* _GET /v1/configurations/{arn}_ 
  *resource*: describe_configuration_response  
  *description*:              <p>Returns a description of this MSK configuration.</p>          
* _GET /v1/configurations/{arn}/revisions/{revision}_ 
  *resource*: describe_configuration_revision_response  
  *description*:              <p>Returns a description of this revision of the configuration.</p>          
* _GET /v1/vpc-connection/{arn}_ 
  *resource*: describe_vpc_connection_response  
  *description*:              <p>Returns a description of this MSK VPC connection.</p>          
* _GET /v1/clusters/{clusterArn}/bootstrap-brokers_ 
  *resource*: get_bootstrap_brokers_response  
  *description*:              <p>A list of brokers that a client application can use to bootstrap.</p>          
* _GET /v1/clusters/{clusterArn}/policy_ 
  *resource*: get_cluster_policy_response  
  *description*:              <p>Get the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.</p>          
* _GET /v1/clusters/{clusterArn}/client-vpc-connections_ 
  *resource*: list_of_client_vpc_connection  
  *description*:              <p>Returns a list of all the VPC connections in this Region.</p>          
* _GET /api/v2/clusters_ 
  *resource*: list_of_cluster  
  *description*:              <p>Returns a list of all the MSK clusters in the current Region.</p>          
* _GET /v1/clusters_ 
  *resource*: list_of_cluster_info  
  *description*:              <p>Returns a list of all the MSK clusters in the current Region.</p>          
* _GET /v1/clusters/{clusterArn}/operations_ 
  *resource*: list_of_cluster_operation_info  
  *description*:              <p>Returns a list of all the operations that have been performed on the specified MSK cluster.</p>          
* _GET /api/v2/clusters/{clusterArn}/operations_ 
  *resource*: list_of_cluster_operation_v2_summary  
  *description*:              <p>Returns a list of all the operations that have been performed on the specified MSK cluster.</p>          
* _GET /v1/compatible-kafka-versions_ 
  *resource*: list_of_compatible_kafka_version  
  *description*:              <p>Gets the Apache Kafka versions to which you can update the MSK cluster.</p>          
* _GET /v1/configurations_ 
  *resource*: list_of_configuration  
  *description*:              <p>Returns a list of all the MSK configurations in this Region.</p>          
* _GET /v1/configurations/{arn}/revisions_ 
  *resource*: list_of_configuration_revision  
  *description*:              <p>Returns a list of all the MSK configurations in this Region.</p>          
* _GET /v1/kafka-versions_ 
  *resource*: list_of_kafka_version  
  *description*:              <p>Returns a list of Apache Kafka versions.</p>          
* _GET /v1/clusters/{clusterArn}/nodes_ 
  *resource*: list_of_node_info  
  *description*:              <p>Returns a list of the broker nodes in the cluster.</p>          
* _GET /v1/clusters/{clusterArn}/scram-secrets_ 
  *resource*: list_of_string  
  *description*:              <p>Returns a list of the Scram Secrets associated with an Amazon MSK cluster.</p>          
* _GET /v1/vpc-connections_ 
  *resource*: list_of_vpc_connection  
  *description*:              <p>Returns a list of all the VPC connections in this Region.</p>          
* _GET /v1/tags/{resourceArn}_ 
  *resource*: map_of_string  
  *description*:              <p>Returns a list of the tags associated with the specified resource.</p>          
