# kpack pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/kpack.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /apis/kpack.io/v1alpha1/builders_ 
  *resource*: list_all_builders  
  *description*: list or watch builders
* _GET /apis/kpack.io/v1alpha1/builds_ 
  *resource*: list_all_builds  
  *description*: list or watch builds
* _GET /apis/kpack.io/v1alpha1/clusterbuilders_ 
  *resource*: list_all_clusterbuilders  
  *description*: list or watch cluster scoped clusterbuilders
* _GET /apis/kpack.io/v1alpha1/clusterbuilders/{name}_ 
  *resource*: get_cluster_builder  
  *description*: Returns a cluster scoped ClusterBuilder
* _GET /apis/kpack.io/v1alpha1/clusterbuilders/{name}/status_ 
  *resource*: get_cluster_builder_status  
  *description*: read status of the specified cluster scoped ClusterBuilder
* _GET /apis/kpack.io/v1alpha1/clusterstacks_ 
  *resource*: list_all_clusterstacks  
  *description*: list or watch cluster scoped clusterstacks
* _GET /apis/kpack.io/v1alpha1/clusterstacks/{name}_ 
  *resource*: get_cluster_stack  
  *description*: Returns a cluster scoped ClusterStack
* _GET /apis/kpack.io/v1alpha1/clusterstacks/{name}/status_ 
  *resource*: get_cluster_stack_status  
  *description*: read status of the specified cluster scoped ClusterStack
* _GET /apis/kpack.io/v1alpha1/clusterstores_ 
  *resource*: list_all_clusterstores  
  *description*: list or watch cluster scoped clusterstores
* _GET /apis/kpack.io/v1alpha1/clusterstores/{name}_ 
  *resource*: get_cluster_store  
  *description*: Returns a cluster scoped ClusterStore
* _GET /apis/kpack.io/v1alpha1/clusterstores/{name}/status_ 
  *resource*: get_cluster_store_status  
  *description*: read status of the specified cluster scoped ClusterStore
* _GET /apis/kpack.io/v1alpha1/images_ 
  *resource*: list_all_images  
  *description*: list or watch images
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/builders_ 
  *resource*: list_namespaced_builders  
  *description*: list or watch namespace scoped builders
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/builders/{name}_ 
  *resource*: get_builder  
  *description*: Returns a namespace scoped custom object
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/builders/{name}/status_ 
  *resource*: get_builder_status  
  *description*: read status of the specified namespace scoped Builder
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/builds_ 
  *resource*: list_namespaced_builds  
  *description*: list or watch namespace scoped builds
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/builds/{name}_ 
  *resource*: get_build  
  *description*: Returns a namespace scoped custom object
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/builds/{name}/status_ 
  *resource*: get_build_status  
  *description*: read status of the specified namespace scoped Build
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/images_ 
  *resource*: list_namespaced_images  
  *description*: list or watch namespace scoped images
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/images/{name}_ 
  *resource*: get_image  
  *description*: Returns a namespace scoped custom object
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/images/{name}/status_ 
  *resource*: get_image_status  
  *description*: read status of the specified namespace scoped Image
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/sourceresolvers_ 
  *resource*: list_namespaced_sourceresolvers  
  *description*: list or watch namespace scoped sourceresolvers
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/sourceresolvers/{name}_ 
  *resource*: get_source_resolver  
  *description*: Returns a namespace scoped custom object
* _GET /apis/kpack.io/v1alpha1/namespaces/{namespace}/sourceresolvers/{name}/status_ 
  *resource*: get_source_resolver_status  
  *description*: read status of the specified namespace scoped SourceResolver
* _GET /apis/kpack.io/v1alpha1/sourceresolvers_ 
  *resource*: list_all_sourceresolvers  
  *description*: list or watch sourceresolvers
