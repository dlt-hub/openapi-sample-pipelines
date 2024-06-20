from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="kpack_source", max_table_nesting=2)
def kpack_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # list or watch builders
            {
                "name": "list_all_builders",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/builders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch builds
            {
                "name": "list_all_builds",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/builds",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch cluster scoped clusterbuilders
            {
                "name": "list_all_clusterbuilders",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterbuilders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a cluster scoped ClusterBuilder
            {
                "name": "get_cluster_builder",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterbuilders/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified cluster scoped ClusterBuilder
            {
                "name": "get_cluster_builder_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterbuilders/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch cluster scoped clusterstacks
            {
                "name": "list_all_clusterstacks",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterstacks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a cluster scoped ClusterStack
            {
                "name": "get_cluster_stack",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterstacks/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified cluster scoped ClusterStack
            {
                "name": "get_cluster_stack_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterstacks/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch cluster scoped clusterstores
            {
                "name": "list_all_clusterstores",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterstores",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a cluster scoped ClusterStore
            {
                "name": "get_cluster_store",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterstores/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified cluster scoped ClusterStore
            {
                "name": "get_cluster_store_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/clusterstores/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch images
            {
                "name": "list_all_images",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/images",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch namespace scoped builders
            {
                "name": "list_namespaced_builders",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/builders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a namespace scoped custom object
            {
                "name": "get_builder",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/builders/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified namespace scoped Builder
            {
                "name": "get_builder_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/builders/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch namespace scoped builds
            {
                "name": "list_namespaced_builds",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/builds",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a namespace scoped custom object
            {
                "name": "get_build",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/builds/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified namespace scoped Build
            {
                "name": "get_build_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/builds/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch namespace scoped images
            {
                "name": "list_namespaced_images",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/images",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a namespace scoped custom object
            {
                "name": "get_image",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/images/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified namespace scoped Image
            {
                "name": "get_image_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/images/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch namespace scoped sourceresolvers
            {
                "name": "list_namespaced_sourceresolvers",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/sourceresolvers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a namespace scoped custom object
            {
                "name": "get_source_resolver",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/sourceresolvers/{name}",
                    "paginator": "auto",
                },
            },
            # read status of the specified namespace scoped SourceResolver
            {
                "name": "get_source_resolver_status",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/namespaces/{namespace}/sourceresolvers/{name}/status",
                    "paginator": "auto",
                },
            },
            # list or watch sourceresolvers
            {
                "name": "list_all_sourceresolvers",
                "table_name": "kpack",
                "endpoint": {
                    "path": "/apis/kpack.io/v1alpha1/sourceresolvers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
