from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="kafka_source", max_table_nesting=2)
def kafka_source(
    api_key: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "api_key",
                "api_key": api_key,
                "name": "Authorization",
                "location": "header",
            },
        },
        "resources": [
            #              <p>Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.</p>
            {
                "name": "cluster",
                "table_name": "cluster",
                "primary_key": "ClusterArn",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "ClusterInfo",
                    "path": "/api/v2/clusters/{clusterArn}",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.</p>
            {
                "name": "cluster_info",
                "table_name": "cluster_info",
                "primary_key": "ClusterArn",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "ClusterInfo",
                    "path": "/v1/clusters/{clusterArn}",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a description of the cluster operation specified by the ARN.</p>
            {
                "name": "cluster_operation_info",
                "table_name": "cluster_operation_info",
                "endpoint": {
                    "data_selector": "ClusterOperationInfo",
                    "path": "/v1/operations/{clusterOperationArn}",
                    "params": {
                        "clusterOperationArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a description of the cluster operation specified by the ARN.</p>
            {
                "name": "cluster_operation_v2",
                "table_name": "cluster_operation_v2",
                "endpoint": {
                    "data_selector": "ClusterOperationInfo",
                    "path": "/api/v2/operations/{clusterOperationArn}",
                    "params": {
                        "clusterOperationArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a description of this MSK configuration.</p>
            {
                "name": "describe_configuration_response",
                "table_name": "describe_configuration_response",
                "primary_key": "Arn",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/configurations/{arn}",
                    "params": {
                        "arn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a description of this revision of the configuration.</p>
            {
                "name": "describe_configuration_revision_response",
                "table_name": "describe_configuration_revision_response",
                "primary_key": "Revision",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/configurations/{arn}/revisions/{revision}",
                    "params": {
                        "arn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "revision": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a description of this MSK VPC connection.</p>
            {
                "name": "describe_vpc_connection_response",
                "table_name": "describe_vpc_connection_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/vpc-connection/{arn}",
                    "params": {
                        "arn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>A list of brokers that a client application can use to bootstrap.</p>
            {
                "name": "get_bootstrap_brokers_response",
                "table_name": "get_bootstrap_brokers_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/clusters/{clusterArn}/bootstrap-brokers",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Get the MSK cluster policy specified by the Amazon Resource Name (ARN) in the request.</p>
            {
                "name": "get_cluster_policy_response",
                "table_name": "get_cluster_policy_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/clusters/{clusterArn}/policy",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the VPC connections in this Region.</p>
            {
                "name": "list_of_client_vpc_connection",
                "table_name": "list_of_client_vpc_connection",
                "endpoint": {
                    "data_selector": "ClientVpcConnections",
                    "path": "/v1/clusters/{clusterArn}/client-vpc-connections",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the MSK clusters in the current Region.</p>
            {
                "name": "list_of_cluster",
                "table_name": "list_of_cluster",
                "endpoint": {
                    "data_selector": "ClusterInfoList",
                    "path": "/api/v2/clusters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "clusterNameFilter": "OPTIONAL_CONFIG",
                        # "clusterTypeFilter": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the MSK clusters in the current Region.</p>
            {
                "name": "list_of_cluster_info",
                "table_name": "list_of_cluster_info",
                "endpoint": {
                    "data_selector": "ClusterInfoList",
                    "path": "/v1/clusters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "clusterNameFilter": "OPTIONAL_CONFIG",
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the operations that have been performed on the specified MSK cluster.</p>
            {
                "name": "list_of_cluster_operation_info",
                "table_name": "list_of_cluster_operation_info",
                "endpoint": {
                    "data_selector": "ClusterOperationInfoList",
                    "path": "/v1/clusters/{clusterArn}/operations",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the operations that have been performed on the specified MSK cluster.</p>
            {
                "name": "list_of_cluster_operation_v2_summary",
                "table_name": "list_of_cluster_operation_v2_summary",
                "endpoint": {
                    "data_selector": "ClusterOperationInfoList",
                    "path": "/api/v2/clusters/{clusterArn}/operations",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Gets the Apache Kafka versions to which you can update the MSK cluster.</p>
            {
                "name": "list_of_compatible_kafka_version",
                "table_name": "list_of_compatible_kafka_version",
                "endpoint": {
                    "data_selector": "CompatibleKafkaVersions",
                    "path": "/v1/compatible-kafka-versions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "clusterArn": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the MSK configurations in this Region.</p>
            {
                "name": "list_of_configuration",
                "table_name": "list_of_configuration",
                "endpoint": {
                    "data_selector": "Configurations",
                    "path": "/v1/configurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the MSK configurations in this Region.</p>
            {
                "name": "list_of_configuration_revision",
                "table_name": "list_of_configuration_revision",
                "endpoint": {
                    "data_selector": "Revisions",
                    "path": "/v1/configurations/{arn}/revisions",
                    "params": {
                        "arn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of Apache Kafka versions.</p>
            {
                "name": "list_of_kafka_version",
                "table_name": "list_of_kafka_version",
                "endpoint": {
                    "data_selector": "KafkaVersions",
                    "path": "/v1/kafka-versions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of the broker nodes in the cluster.</p>
            {
                "name": "list_of_node_info",
                "table_name": "list_of_node_info",
                "endpoint": {
                    "data_selector": "NodeInfoList",
                    "path": "/v1/clusters/{clusterArn}/nodes",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of the Scram Secrets associated with an Amazon MSK cluster.</p>
            {
                "name": "list_of_string",
                "table_name": "list_of_string",
                "endpoint": {
                    "data_selector": "SecretArnList",
                    "path": "/v1/clusters/{clusterArn}/scram-secrets",
                    "params": {
                        "clusterArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of all the VPC connections in this Region.</p>
            {
                "name": "list_of_vpc_connection",
                "table_name": "list_of_vpc_connection",
                "endpoint": {
                    "data_selector": "VpcConnections",
                    "path": "/v1/vpc-connections",
                    "params": {
                        # the parameters below can optionally be configured
                        # "maxResults": "OPTIONAL_CONFIG",
                        # "nextToken": "OPTIONAL_CONFIG",
                        # "MaxResults": "OPTIONAL_CONFIG",
                        # "NextToken": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            #              <p>Returns a list of the tags associated with the specified resource.</p>
            {
                "name": "map_of_string",
                "table_name": "map_of_string",
                "endpoint": {
                    "data_selector": "Tags",
                    "path": "/v1/tags/{resourceArn}",
                    "params": {
                        "resourceArn": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
