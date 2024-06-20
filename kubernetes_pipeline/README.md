# kubernetes pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/kubernetes.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /.well-known/openid-configuration/_ 
  *resource*: get_service_account_issuer_open_id_configuration  
  *description*: get service account issuer OpenID configuration, also known as the 'OIDC discovery doc'
* _GET /apis/admissionregistration.k8s.io/_ 
  *resource*: get_admissionregistration_api_group  
  *description*: get information of a group
* _GET /apis/admissionregistration.k8s.io/v1/_ 
  *resource*: get_admissionregistration_v1api_resources  
  *description*: get available resources
* _GET /apis/admissionregistration.k8s.io/v1/mutatingwebhookconfigurations_ 
  *resource*: list_admissionregistration_v1_mutating_webhook_configuration  
  *description*: list or watch objects of kind MutatingWebhookConfiguration
* _GET /apis/admissionregistration.k8s.io/v1/mutatingwebhookconfigurations/{name}_ 
  *resource*: read_admissionregistration_v1_mutating_webhook_configuration  
  *description*: read the specified MutatingWebhookConfiguration
* _GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies_ 
  *resource*: list_admissionregistration_v1_validating_admission_policy  
  *description*: list or watch objects of kind ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}_ 
  *resource*: read_admissionregistration_v1_validating_admission_policy  
  *description*: read the specified ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status_ 
  *resource*: read_admissionregistration_v1_validating_admission_policy_status  
  *description*: read status of the specified ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings_ 
  *resource*: list_admissionregistration_v1_validating_admission_policy_binding  
  *description*: list or watch objects of kind ValidatingAdmissionPolicyBinding
* _GET /apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings/{name}_ 
  *resource*: read_admissionregistration_v1_validating_admission_policy_binding  
  *description*: read the specified ValidatingAdmissionPolicyBinding
* _GET /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations_ 
  *resource*: list_admissionregistration_v1_validating_webhook_configuration  
  *description*: list or watch objects of kind ValidatingWebhookConfiguration
* _GET /apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}_ 
  *resource*: read_admissionregistration_v1_validating_webhook_configuration  
  *description*: read the specified ValidatingWebhookConfiguration
* _GET /apis/admissionregistration.k8s.io/v1/watch/mutatingwebhookconfigurations_ 
  *resource*: watch_admissionregistration_v1_mutating_webhook_configuration_list  
  *description*: watch individual changes to a list of MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1/watch/mutatingwebhookconfigurations/{name}_ 
  *resource*: watch_admissionregistration_v1_mutating_webhook_configuration  
  *description*: watch changes to an object of kind MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies_ 
  *resource*: watch_admissionregistration_v1_validating_admission_policy_list  
  *description*: watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}_ 
  *resource*: watch_admissionregistration_v1_validating_admission_policy  
  *description*: watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings_ 
  *resource*: watch_admissionregistration_v1_validating_admission_policy_binding_list  
  *description*: watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings/{name}_ 
  *resource*: watch_admissionregistration_v1_validating_admission_policy_binding  
  *description*: watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations_ 
  *resource*: watch_admissionregistration_v1_validating_webhook_configuration_list  
  *description*: watch individual changes to a list of ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations/{name}_ 
  *resource*: watch_admissionregistration_v1_validating_webhook_configuration  
  *description*: watch changes to an object of kind ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1alpha1/_ 
  *resource*: get_admissionregistration_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicies_ 
  *resource*: list_admissionregistration_v1_alpha_1_validating_admission_policy  
  *description*: list or watch objects of kind ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicies/{name}_ 
  *resource*: read_admissionregistration_v1_alpha_1_validating_admission_policy  
  *description*: read the specified ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicies/{name}/status_ 
  *resource*: read_admissionregistration_v1_alpha_1_validating_admission_policy_status  
  *description*: read status of the specified ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicybindings_ 
  *resource*: list_admissionregistration_v1_alpha_1_validating_admission_policy_binding  
  *description*: list or watch objects of kind ValidatingAdmissionPolicyBinding
* _GET /apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicybindings/{name}_ 
  *resource*: read_admissionregistration_v1_alpha_1_validating_admission_policy_binding  
  *description*: read the specified ValidatingAdmissionPolicyBinding
* _GET /apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicies_ 
  *resource*: watch_admissionregistration_v1_alpha_1_validating_admission_policy_list  
  *description*: watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicies/{name}_ 
  *resource*: watch_admissionregistration_v1_alpha_1_validating_admission_policy  
  *description*: watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicybindings_ 
  *resource*: watch_admissionregistration_v1_alpha_1_validating_admission_policy_binding_list  
  *description*: watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicybindings/{name}_ 
  *resource*: watch_admissionregistration_v1_alpha_1_validating_admission_policy_binding  
  *description*: watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1beta1/_ 
  *resource*: get_admissionregistration_v1_beta_1api_resources  
  *description*: get available resources
* _GET /apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies_ 
  *resource*: list_admissionregistration_v1_beta_1_validating_admission_policy  
  *description*: list or watch objects of kind ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies/{name}_ 
  *resource*: read_admissionregistration_v1_beta_1_validating_admission_policy  
  *description*: read the specified ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies/{name}/status_ 
  *resource*: read_admissionregistration_v1_beta_1_validating_admission_policy_status  
  *description*: read status of the specified ValidatingAdmissionPolicy
* _GET /apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicybindings_ 
  *resource*: list_admissionregistration_v1_beta_1_validating_admission_policy_binding  
  *description*: list or watch objects of kind ValidatingAdmissionPolicyBinding
* _GET /apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicybindings/{name}_ 
  *resource*: read_admissionregistration_v1_beta_1_validating_admission_policy_binding  
  *description*: read the specified ValidatingAdmissionPolicyBinding
* _GET /apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicies_ 
  *resource*: watch_admissionregistration_v1_beta_1_validating_admission_policy_list  
  *description*: watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicies/{name}_ 
  *resource*: watch_admissionregistration_v1_beta_1_validating_admission_policy  
  *description*: watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicybindings_ 
  *resource*: watch_admissionregistration_v1_beta_1_validating_admission_policy_binding_list  
  *description*: watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicybindings/{name}_ 
  *resource*: watch_admissionregistration_v1_beta_1_validating_admission_policy_binding  
  *description*: watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/_ 
  *resource*: get_api_versions  
  *description*: get available API versions
* _GET /apis/apiextensions.k8s.io/_ 
  *resource*: get_apiextensions_api_group  
  *description*: get information of a group
* _GET /apis/apiextensions.k8s.io/v1/_ 
  *resource*: get_apiextensions_v1api_resources  
  *description*: get available resources
* _GET /apis/apiextensions.k8s.io/v1/customresourcedefinitions_ 
  *resource*: list_apiextensions_v1_custom_resource_definition  
  *description*: list or watch objects of kind CustomResourceDefinition
* _GET /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}_ 
  *resource*: read_apiextensions_v1_custom_resource_definition  
  *description*: read the specified CustomResourceDefinition
* _GET /apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status_ 
  *resource*: read_apiextensions_v1_custom_resource_definition_status  
  *description*: read status of the specified CustomResourceDefinition
* _GET /apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions_ 
  *resource*: watch_apiextensions_v1_custom_resource_definition_list  
  *description*: watch individual changes to a list of CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions/{name}_ 
  *resource*: watch_apiextensions_v1_custom_resource_definition  
  *description*: watch changes to an object of kind CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apiregistration.k8s.io/_ 
  *resource*: get_apiregistration_api_group  
  *description*: get information of a group
* _GET /apis/apiregistration.k8s.io/v1/_ 
  *resource*: get_apiregistration_v1api_resources  
  *description*: get available resources
* _GET /apis/apiregistration.k8s.io/v1/apiservices_ 
  *resource*: list_apiregistration_v1api_service  
  *description*: list or watch objects of kind APIService
* _GET /apis/apiregistration.k8s.io/v1/apiservices/{name}_ 
  *resource*: read_apiregistration_v1api_service  
  *description*: read the specified APIService
* _GET /apis/apiregistration.k8s.io/v1/apiservices/{name}/status_ 
  *resource*: read_apiregistration_v1api_service_status  
  *description*: read status of the specified APIService
* _GET /apis/apiregistration.k8s.io/v1/watch/apiservices_ 
  *resource*: watch_apiregistration_v1api_service_list  
  *description*: watch individual changes to a list of APIService. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apiregistration.k8s.io/v1/watch/apiservices/{name}_ 
  *resource*: watch_apiregistration_v1api_service  
  *description*: watch changes to an object of kind APIService. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apps/_ 
  *resource*: get_apps_api_group  
  *description*: get information of a group
* _GET /api/_ 
  *resource*: get_core_api_versions  
  *description*: get available API versions
* _GET /api/v1/namespaces/{namespace}/pods/{name}/attach_ 
  *resource*: connect_core_v1_get_namespaced_pod_attach  
  *description*: connect GET requests to attach of Pod
* _GET /apis/authentication.k8s.io/_ 
  *resource*: get_authentication_api_group  
  *description*: get information of a group
* _GET /apis/authentication.k8s.io/v1/_ 
  *resource*: get_authentication_v1api_resources  
  *description*: get available resources
* _GET /apis/authentication.k8s.io/v1alpha1/_ 
  *resource*: get_authentication_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/authentication.k8s.io/v1beta1/_ 
  *resource*: get_authentication_v1_beta_1api_resources  
  *description*: get available resources
* _GET /apis/authorization.k8s.io/_ 
  *resource*: get_authorization_api_group  
  *description*: get information of a group
* _GET /apis/authorization.k8s.io/v1/_ 
  *resource*: get_authorization_v1api_resources  
  *description*: get available resources
* _GET /apis/autoscaling/_ 
  *resource*: get_autoscaling_api_group  
  *description*: get information of a group
* _GET /apis/batch/_ 
  *resource*: get_batch_api_group  
  *description*: get information of a group
* _GET /apis/certificates.k8s.io/_ 
  *resource*: get_certificates_api_group  
  *description*: get information of a group
* _GET /apis/certificates.k8s.io/v1/_ 
  *resource*: get_certificates_v1api_resources  
  *description*: get available resources
* _GET /apis/certificates.k8s.io/v1/certificatesigningrequests_ 
  *resource*: list_certificates_v1_certificate_signing_request  
  *description*: list or watch objects of kind CertificateSigningRequest
* _GET /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}_ 
  *resource*: read_certificates_v1_certificate_signing_request  
  *description*: read the specified CertificateSigningRequest
* _GET /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/approval_ 
  *resource*: read_certificates_v1_certificate_signing_request_approval  
  *description*: read approval of the specified CertificateSigningRequest
* _GET /apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/status_ 
  *resource*: read_certificates_v1_certificate_signing_request_status  
  *description*: read status of the specified CertificateSigningRequest
* _GET /apis/certificates.k8s.io/v1/watch/certificatesigningrequests_ 
  *resource*: watch_certificates_v1_certificate_signing_request_list  
  *description*: watch individual changes to a list of CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/certificates.k8s.io/v1/watch/certificatesigningrequests/{name}_ 
  *resource*: watch_certificates_v1_certificate_signing_request  
  *description*: watch changes to an object of kind CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/certificates.k8s.io/v1alpha1/_ 
  *resource*: get_certificates_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/certificates.k8s.io/v1alpha1/clustertrustbundles_ 
  *resource*: list_certificates_v1_alpha_1_cluster_trust_bundle  
  *description*: list or watch objects of kind ClusterTrustBundle
* _GET /apis/certificates.k8s.io/v1alpha1/clustertrustbundles/{name}_ 
  *resource*: read_certificates_v1_alpha_1_cluster_trust_bundle  
  *description*: read the specified ClusterTrustBundle
* _GET /apis/certificates.k8s.io/v1alpha1/watch/clustertrustbundles_ 
  *resource*: watch_certificates_v1_alpha_1_cluster_trust_bundle_list  
  *description*: watch individual changes to a list of ClusterTrustBundle. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/certificates.k8s.io/v1alpha1/watch/clustertrustbundles/{name}_ 
  *resource*: watch_certificates_v1_alpha_1_cluster_trust_bundle  
  *description*: watch changes to an object of kind ClusterTrustBundle. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/componentstatuses_ 
  *resource*: list_core_v1_component_status  
  *description*: list objects of kind ComponentStatus
* _GET /api/v1/componentstatuses/{name}_ 
  *resource*: read_core_v1_component_status  
  *description*: read the specified ComponentStatus
* _GET /api/v1/configmaps_ 
  *resource*: list_core_v1_config_map_for_all_namespaces  
  *description*: list or watch objects of kind ConfigMap
* _GET /api/v1/namespaces/{namespace}/configmaps_ 
  *resource*: list_core_v1_namespaced_config_map  
  *description*: list or watch objects of kind ConfigMap
* _GET /api/v1/namespaces/{namespace}/configmaps/{name}_ 
  *resource*: read_core_v1_namespaced_config_map  
  *description*: read the specified ConfigMap
* _GET /api/v1/watch/configmaps_ 
  *resource*: watch_core_v1_config_map_list_for_all_namespaces  
  *description*: watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/configmaps_ 
  *resource*: watch_core_v1_namespaced_config_map_list  
  *description*: watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/configmaps/{name}_ 
  *resource*: watch_core_v1_namespaced_config_map  
  *description*: watch changes to an object of kind ConfigMap. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apps/v1/controllerrevisions_ 
  *resource*: list_apps_v1_controller_revision_for_all_namespaces  
  *description*: list or watch objects of kind ControllerRevision
* _GET /apis/apps/v1/namespaces/{namespace}/controllerrevisions_ 
  *resource*: list_apps_v1_namespaced_controller_revision  
  *description*: list or watch objects of kind ControllerRevision
* _GET /apis/apps/v1/namespaces/{namespace}/controllerrevisions/{name}_ 
  *resource*: read_apps_v1_namespaced_controller_revision  
  *description*: read the specified ControllerRevision
* _GET /apis/apps/v1/watch/controllerrevisions_ 
  *resource*: watch_apps_v1_controller_revision_list_for_all_namespaces  
  *description*: watch individual changes to a list of ControllerRevision. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/controllerrevisions_ 
  *resource*: watch_apps_v1_namespaced_controller_revision_list  
  *description*: watch individual changes to a list of ControllerRevision. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/controllerrevisions/{name}_ 
  *resource*: watch_apps_v1_namespaced_controller_revision  
  *description*: watch changes to an object of kind ControllerRevision. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/coordination.k8s.io/_ 
  *resource*: get_coordination_api_group  
  *description*: get information of a group
* _GET /apis/coordination.k8s.io/v1/_ 
  *resource*: get_coordination_v1api_resources  
  *description*: get available resources
* _GET /apis/coordination.k8s.io/v1/leases_ 
  *resource*: list_coordination_v1_lease_for_all_namespaces  
  *description*: list or watch objects of kind Lease
* _GET /apis/coordination.k8s.io/v1/namespaces/{namespace}/leases_ 
  *resource*: list_coordination_v1_namespaced_lease  
  *description*: list or watch objects of kind Lease
* _GET /apis/coordination.k8s.io/v1/namespaces/{namespace}/leases/{name}_ 
  *resource*: read_coordination_v1_namespaced_lease  
  *description*: read the specified Lease
* _GET /apis/coordination.k8s.io/v1/watch/leases_ 
  *resource*: watch_coordination_v1_lease_list_for_all_namespaces  
  *description*: watch individual changes to a list of Lease. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/coordination.k8s.io/v1/watch/namespaces/{namespace}/leases_ 
  *resource*: watch_coordination_v1_namespaced_lease_list  
  *description*: watch individual changes to a list of Lease. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/coordination.k8s.io/v1/watch/namespaces/{namespace}/leases/{name}_ 
  *resource*: watch_coordination_v1_namespaced_lease  
  *description*: watch changes to an object of kind Lease. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/batch/v1/cronjobs_ 
  *resource*: list_batch_v1_cron_job_for_all_namespaces  
  *description*: list or watch objects of kind CronJob
* _GET /apis/batch/v1/namespaces/{namespace}/cronjobs_ 
  *resource*: list_batch_v1_namespaced_cron_job  
  *description*: list or watch objects of kind CronJob
* _GET /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}_ 
  *resource*: read_batch_v1_namespaced_cron_job  
  *description*: read the specified CronJob
* _GET /apis/batch/v1/watch/cronjobs_ 
  *resource*: watch_batch_v1_cron_job_list_for_all_namespaces  
  *description*: watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/batch/v1/watch/namespaces/{namespace}/cronjobs_ 
  *resource*: watch_batch_v1_namespaced_cron_job_list  
  *description*: watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/batch/v1/watch/namespaces/{namespace}/cronjobs/{name}_ 
  *resource*: watch_batch_v1_namespaced_cron_job  
  *description*: watch changes to an object of kind CronJob. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apps/v1/daemonsets_ 
  *resource*: list_apps_v1_daemon_set_for_all_namespaces  
  *description*: list or watch objects of kind DaemonSet
* _GET /apis/apps/v1/namespaces/{namespace}/daemonsets_ 
  *resource*: list_apps_v1_namespaced_daemon_set  
  *description*: list or watch objects of kind DaemonSet
* _GET /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}_ 
  *resource*: read_apps_v1_namespaced_daemon_set  
  *description*: read the specified DaemonSet
* _GET /apis/apps/v1/watch/daemonsets_ 
  *resource*: watch_apps_v1_daemon_set_list_for_all_namespaces  
  *description*: watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/daemonsets_ 
  *resource*: watch_apps_v1_namespaced_daemon_set_list  
  *description*: watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/daemonsets/{name}_ 
  *resource*: watch_apps_v1_namespaced_daemon_set  
  *description*: watch changes to an object of kind DaemonSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apps/v1/deployments_ 
  *resource*: list_apps_v1_deployment_for_all_namespaces  
  *description*: list or watch objects of kind Deployment
* _GET /apis/apps/v1/namespaces/{namespace}/deployments_ 
  *resource*: list_apps_v1_namespaced_deployment  
  *description*: list or watch objects of kind Deployment
* _GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}_ 
  *resource*: read_apps_v1_namespaced_deployment  
  *description*: read the specified Deployment
* _GET /apis/apps/v1/watch/deployments_ 
  *resource*: watch_apps_v1_deployment_list_for_all_namespaces  
  *description*: watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/deployments_ 
  *resource*: watch_apps_v1_namespaced_deployment_list  
  *description*: watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}_ 
  *resource*: watch_apps_v1_namespaced_deployment  
  *description*: watch changes to an object of kind Deployment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/discovery.k8s.io/_ 
  *resource*: get_discovery_api_group  
  *description*: get information of a group
* _GET /apis/discovery.k8s.io/v1/_ 
  *resource*: get_discovery_v1api_resources  
  *description*: get available resources
* _GET /apis/discovery.k8s.io/v1/endpointslices_ 
  *resource*: list_discovery_v1_endpoint_slice_for_all_namespaces  
  *description*: list or watch objects of kind EndpointSlice
* _GET /apis/discovery.k8s.io/v1/namespaces/{namespace}/endpointslices_ 
  *resource*: list_discovery_v1_namespaced_endpoint_slice  
  *description*: list or watch objects of kind EndpointSlice
* _GET /apis/discovery.k8s.io/v1/namespaces/{namespace}/endpointslices/{name}_ 
  *resource*: read_discovery_v1_namespaced_endpoint_slice  
  *description*: read the specified EndpointSlice
* _GET /apis/discovery.k8s.io/v1/watch/endpointslices_ 
  *resource*: watch_discovery_v1_endpoint_slice_list_for_all_namespaces  
  *description*: watch individual changes to a list of EndpointSlice. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/discovery.k8s.io/v1/watch/namespaces/{namespace}/endpointslices_ 
  *resource*: watch_discovery_v1_namespaced_endpoint_slice_list  
  *description*: watch individual changes to a list of EndpointSlice. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/discovery.k8s.io/v1/watch/namespaces/{namespace}/endpointslices/{name}_ 
  *resource*: watch_discovery_v1_namespaced_endpoint_slice  
  *description*: watch changes to an object of kind EndpointSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/endpoints_ 
  *resource*: list_core_v1_endpoints_for_all_namespaces  
  *description*: list or watch objects of kind Endpoints
* _GET /api/v1/namespaces/{namespace}/endpoints_ 
  *resource*: list_core_v1_namespaced_endpoints  
  *description*: list or watch objects of kind Endpoints
* _GET /api/v1/namespaces/{namespace}/endpoints/{name}_ 
  *resource*: read_core_v1_namespaced_endpoints  
  *description*: read the specified Endpoints
* _GET /api/v1/watch/endpoints_ 
  *resource*: watch_core_v1_endpoints_list_for_all_namespaces  
  *description*: watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/endpoints_ 
  *resource*: watch_core_v1_namespaced_endpoints_list  
  *description*: watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/endpoints/{name}_ 
  *resource*: watch_core_v1_namespaced_endpoints  
  *description*: watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers_ 
  *resource*: read_core_v1_namespaced_pod_ephemeralcontainers  
  *description*: read ephemeralcontainers of the specified Pod
* _GET /api/v1/events_ 
  *resource*: list_core_v1_event_for_all_namespaces  
  *description*: list or watch objects of kind Event
* _GET /api/v1/namespaces/{namespace}/events_ 
  *resource*: list_core_v1_namespaced_event  
  *description*: list or watch objects of kind Event
* _GET /api/v1/namespaces/{namespace}/events/{name}_ 
  *resource*: read_core_v1_namespaced_event  
  *description*: read the specified Event
* _GET /api/v1/watch/events_ 
  *resource*: watch_core_v1_event_list_for_all_namespaces  
  *description*: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/events_ 
  *resource*: watch_core_v1_namespaced_event_list  
  *description*: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/events/{name}_ 
  *resource*: watch_core_v1_namespaced_event  
  *description*: watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/events.k8s.io/_ 
  *resource*: get_events_api_group  
  *description*: get information of a group
* _GET /apis/events.k8s.io/v1/_ 
  *resource*: get_events_v1api_resources  
  *description*: get available resources
* _GET /apis/events.k8s.io/v1/events_ 
  *resource*: list_events_v1_event_for_all_namespaces  
  *description*: list or watch objects of kind Event
* _GET /apis/events.k8s.io/v1/namespaces/{namespace}/events_ 
  *resource*: list_events_v1_namespaced_event  
  *description*: list or watch objects of kind Event
* _GET /apis/events.k8s.io/v1/namespaces/{namespace}/events/{name}_ 
  *resource*: read_events_v1_namespaced_event  
  *description*: read the specified Event
* _GET /apis/events.k8s.io/v1/watch/events_ 
  *resource*: watch_events_v1_event_list_for_all_namespaces  
  *description*: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/events.k8s.io/v1/watch/namespaces/{namespace}/events_ 
  *resource*: watch_events_v1_namespaced_event_list  
  *description*: watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/events.k8s.io/v1/watch/namespaces/{namespace}/events/{name}_ 
  *resource*: watch_events_v1_namespaced_event  
  *description*: watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/namespaces/{namespace}/pods/{name}/exec_ 
  *resource*: connect_core_v1_get_namespaced_pod_exec  
  *description*: connect GET requests to exec of Pod
* _GET /apis/flowcontrol.apiserver.k8s.io/_ 
  *resource*: get_flowcontrol_apiserver_api_group  
  *description*: get information of a group
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/_ 
  *resource*: get_flowcontrol_apiserver_v1api_resources  
  *description*: get available resources
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas_ 
  *resource*: list_flowcontrol_apiserver_v1_flow_schema  
  *description*: list or watch objects of kind FlowSchema
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}_ 
  *resource*: read_flowcontrol_apiserver_v1_flow_schema  
  *description*: read the specified FlowSchema
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status_ 
  *resource*: read_flowcontrol_apiserver_v1_flow_schema_status  
  *description*: read status of the specified FlowSchema
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations_ 
  *resource*: list_flowcontrol_apiserver_v1_priority_level_configuration  
  *description*: list or watch objects of kind PriorityLevelConfiguration
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}_ 
  *resource*: read_flowcontrol_apiserver_v1_priority_level_configuration  
  *description*: read the specified PriorityLevelConfiguration
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status_ 
  *resource*: read_flowcontrol_apiserver_v1_priority_level_configuration_status  
  *description*: read status of the specified PriorityLevelConfiguration
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas_ 
  *resource*: watch_flowcontrol_apiserver_v1_flow_schema_list  
  *description*: watch individual changes to a list of FlowSchema. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas/{name}_ 
  *resource*: watch_flowcontrol_apiserver_v1_flow_schema  
  *description*: watch changes to an object of kind FlowSchema. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations_ 
  *resource*: watch_flowcontrol_apiserver_v1_priority_level_configuration_list  
  *description*: watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations/{name}_ 
  *resource*: watch_flowcontrol_apiserver_v1_priority_level_configuration  
  *description*: watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/_ 
  *resource*: get_flowcontrol_apiserver_v1_beta_3api_resources  
  *description*: get available resources
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/flowschemas_ 
  *resource*: list_flowcontrol_apiserver_v1_beta_3_flow_schema  
  *description*: list or watch objects of kind FlowSchema
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/flowschemas/{name}_ 
  *resource*: read_flowcontrol_apiserver_v1_beta_3_flow_schema  
  *description*: read the specified FlowSchema
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/flowschemas/{name}/status_ 
  *resource*: read_flowcontrol_apiserver_v1_beta_3_flow_schema_status  
  *description*: read status of the specified FlowSchema
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/prioritylevelconfigurations_ 
  *resource*: list_flowcontrol_apiserver_v1_beta_3_priority_level_configuration  
  *description*: list or watch objects of kind PriorityLevelConfiguration
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/prioritylevelconfigurations/{name}_ 
  *resource*: read_flowcontrol_apiserver_v1_beta_3_priority_level_configuration  
  *description*: read the specified PriorityLevelConfiguration
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/prioritylevelconfigurations/{name}/status_ 
  *resource*: read_flowcontrol_apiserver_v1_beta_3_priority_level_configuration_status  
  *description*: read status of the specified PriorityLevelConfiguration
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/flowschemas_ 
  *resource*: watch_flowcontrol_apiserver_v1_beta_3_flow_schema_list  
  *description*: watch individual changes to a list of FlowSchema. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/flowschemas/{name}_ 
  *resource*: watch_flowcontrol_apiserver_v1_beta_3_flow_schema  
  *description*: watch changes to an object of kind FlowSchema. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/prioritylevelconfigurations_ 
  *resource*: watch_flowcontrol_apiserver_v1_beta_3_priority_level_configuration_list  
  *description*: watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/prioritylevelconfigurations/{name}_ 
  *resource*: watch_flowcontrol_apiserver_v1_beta_3_priority_level_configuration  
  *description*: watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/autoscaling/v1/horizontalpodautoscalers_ 
  *resource*: list_autoscaling_v1_horizontal_pod_autoscaler_for_all_namespaces  
  *description*: list or watch objects of kind HorizontalPodAutoscaler
* _GET /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers_ 
  *resource*: list_autoscaling_v1_namespaced_horizontal_pod_autoscaler  
  *description*: list or watch objects of kind HorizontalPodAutoscaler
* _GET /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}_ 
  *resource*: read_autoscaling_v1_namespaced_horizontal_pod_autoscaler  
  *description*: read the specified HorizontalPodAutoscaler
* _GET /apis/autoscaling/v1/watch/horizontalpodautoscalers_ 
  *resource*: watch_autoscaling_v1_horizontal_pod_autoscaler_list_for_all_namespaces  
  *description*: watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers_ 
  *resource*: watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler_list  
  *description*: watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}_ 
  *resource*: watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler  
  *description*: watch changes to an object of kind HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/autoscaling/v2/horizontalpodautoscalers_ 
  *resource*: list_autoscaling_v2_horizontal_pod_autoscaler_for_all_namespaces  
  *description*: list or watch objects of kind HorizontalPodAutoscaler
* _GET /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers_ 
  *resource*: list_autoscaling_v2_namespaced_horizontal_pod_autoscaler  
  *description*: list or watch objects of kind HorizontalPodAutoscaler
* _GET /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}_ 
  *resource*: read_autoscaling_v2_namespaced_horizontal_pod_autoscaler  
  *description*: read the specified HorizontalPodAutoscaler
* _GET /apis/autoscaling/v2/watch/horizontalpodautoscalers_ 
  *resource*: watch_autoscaling_v2_horizontal_pod_autoscaler_list_for_all_namespaces  
  *description*: watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers_ 
  *resource*: watch_autoscaling_v2_namespaced_horizontal_pod_autoscaler_list  
  *description*: watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}_ 
  *resource*: watch_autoscaling_v2_namespaced_horizontal_pod_autoscaler  
  *description*: watch changes to an object of kind HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/internal.apiserver.k8s.io/_ 
  *resource*: get_internal_apiserver_api_group  
  *description*: get information of a group
* _GET /apis/internal.apiserver.k8s.io/v1alpha1/_ 
  *resource*: get_internal_apiserver_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/internal.apiserver.k8s.io/v1alpha1/storageversions_ 
  *resource*: list_internal_apiserver_v1_alpha_1_storage_version  
  *description*: list or watch objects of kind StorageVersion
* _GET /apis/internal.apiserver.k8s.io/v1alpha1/storageversions/{name}_ 
  *resource*: read_internal_apiserver_v1_alpha_1_storage_version  
  *description*: read the specified StorageVersion
* _GET /apis/internal.apiserver.k8s.io/v1alpha1/storageversions/{name}/status_ 
  *resource*: read_internal_apiserver_v1_alpha_1_storage_version_status  
  *description*: read status of the specified StorageVersion
* _GET /apis/internal.apiserver.k8s.io/v1alpha1/watch/storageversions_ 
  *resource*: watch_internal_apiserver_v1_alpha_1_storage_version_list  
  *description*: watch individual changes to a list of StorageVersion. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/internal.apiserver.k8s.io/v1alpha1/watch/storageversions/{name}_ 
  *resource*: watch_internal_apiserver_v1_alpha_1_storage_version  
  *description*: watch changes to an object of kind StorageVersion. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/batch/v1/jobs_ 
  *resource*: list_batch_v1_job_for_all_namespaces  
  *description*: list or watch objects of kind Job
* _GET /apis/batch/v1/namespaces/{namespace}/jobs_ 
  *resource*: list_batch_v1_namespaced_job  
  *description*: list or watch objects of kind Job
* _GET /apis/batch/v1/namespaces/{namespace}/jobs/{name}_ 
  *resource*: read_batch_v1_namespaced_job  
  *description*: read the specified Job
* _GET /apis/batch/v1/watch/jobs_ 
  *resource*: watch_batch_v1_job_list_for_all_namespaces  
  *description*: watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/batch/v1/watch/namespaces/{namespace}/jobs_ 
  *resource*: watch_batch_v1_namespaced_job_list  
  *description*: watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/batch/v1/watch/namespaces/{namespace}/jobs/{name}_ 
  *resource*: watch_batch_v1_namespaced_job  
  *description*: watch changes to an object of kind Job. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /openid/v1/jwks/_ 
  *resource*: get_service_account_issuer_open_id_keyset  
  *description*: get service account issuer OpenID JSON Web Key Set (contains public token verification keys)
* _GET /api/v1/limitranges_ 
  *resource*: list_core_v1_limit_range_for_all_namespaces  
  *description*: list or watch objects of kind LimitRange
* _GET /api/v1/namespaces/{namespace}/limitranges_ 
  *resource*: list_core_v1_namespaced_limit_range  
  *description*: list or watch objects of kind LimitRange
* _GET /api/v1/namespaces/{namespace}/limitranges/{name}_ 
  *resource*: read_core_v1_namespaced_limit_range  
  *description*: read the specified LimitRange
* _GET /api/v1/watch/limitranges_ 
  *resource*: watch_core_v1_limit_range_list_for_all_namespaces  
  *description*: watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/limitranges_ 
  *resource*: watch_core_v1_namespaced_limit_range_list  
  *description*: watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/limitranges/{name}_ 
  *resource*: watch_core_v1_namespaced_limit_range  
  *description*: watch changes to an object of kind LimitRange. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/namespaces/{namespace}/pods/{name}/log_ 
  *resource*: read_core_v1_namespaced_pod_log  
  *description*: read log of the specified Pod
* _GET /logs/_ 
  *resource*: log_file_list_handler  
* _GET /logs/{logpath}_ 
  *resource*: log_file_handler  
* _GET /api/v1/namespaces_ 
  *resource*: list_core_v1_namespace  
  *description*: list or watch objects of kind Namespace
* _GET /api/v1/namespaces/{name}_ 
  *resource*: read_core_v1_namespace  
  *description*: read the specified Namespace
* _GET /api/v1/watch/namespaces_ 
  *resource*: watch_core_v1_namespace_list  
  *description*: watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{name}_ 
  *resource*: watch_core_v1_namespace  
  *description*: watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/networking.k8s.io/_ 
  *resource*: get_networking_api_group  
  *description*: get information of a group
* _GET /apis/networking.k8s.io/v1/_ 
  *resource*: get_networking_v1api_resources  
  *description*: get available resources
* _GET /apis/networking.k8s.io/v1/ingressclasses_ 
  *resource*: list_networking_v1_ingress_class  
  *description*: list or watch objects of kind IngressClass
* _GET /apis/networking.k8s.io/v1/ingressclasses/{name}_ 
  *resource*: read_networking_v1_ingress_class  
  *description*: read the specified IngressClass
* _GET /apis/networking.k8s.io/v1/ingresses_ 
  *resource*: list_networking_v1_ingress_for_all_namespaces  
  *description*: list or watch objects of kind Ingress
* _GET /apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses_ 
  *resource*: list_networking_v1_namespaced_ingress  
  *description*: list or watch objects of kind Ingress
* _GET /apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses/{name}_ 
  *resource*: read_networking_v1_namespaced_ingress  
  *description*: read the specified Ingress
* _GET /apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses/{name}/status_ 
  *resource*: read_networking_v1_namespaced_ingress_status  
  *description*: read status of the specified Ingress
* _GET /apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies_ 
  *resource*: list_networking_v1_namespaced_network_policy  
  *description*: list or watch objects of kind NetworkPolicy
* _GET /apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}_ 
  *resource*: read_networking_v1_namespaced_network_policy  
  *description*: read the specified NetworkPolicy
* _GET /apis/networking.k8s.io/v1/networkpolicies_ 
  *resource*: list_networking_v1_network_policy_for_all_namespaces  
  *description*: list or watch objects of kind NetworkPolicy
* _GET /apis/networking.k8s.io/v1/watch/ingressclasses_ 
  *resource*: watch_networking_v1_ingress_class_list  
  *description*: watch individual changes to a list of IngressClass. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1/watch/ingressclasses/{name}_ 
  *resource*: watch_networking_v1_ingress_class  
  *description*: watch changes to an object of kind IngressClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/networking.k8s.io/v1/watch/ingresses_ 
  *resource*: watch_networking_v1_ingress_list_for_all_namespaces  
  *description*: watch individual changes to a list of Ingress. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1/watch/namespaces/{namespace}/ingresses_ 
  *resource*: watch_networking_v1_namespaced_ingress_list  
  *description*: watch individual changes to a list of Ingress. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1/watch/namespaces/{namespace}/ingresses/{name}_ 
  *resource*: watch_networking_v1_namespaced_ingress  
  *description*: watch changes to an object of kind Ingress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies_ 
  *resource*: watch_networking_v1_namespaced_network_policy_list  
  *description*: watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies/{name}_ 
  *resource*: watch_networking_v1_namespaced_network_policy  
  *description*: watch changes to an object of kind NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/networking.k8s.io/v1/watch/networkpolicies_ 
  *resource*: watch_networking_v1_network_policy_list_for_all_namespaces  
  *description*: watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1alpha1/_ 
  *resource*: get_networking_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/networking.k8s.io/v1alpha1/ipaddresses_ 
  *resource*: list_networking_v1_alpha_1ip_address  
  *description*: list or watch objects of kind IPAddress
* _GET /apis/networking.k8s.io/v1alpha1/ipaddresses/{name}_ 
  *resource*: read_networking_v1_alpha_1ip_address  
  *description*: read the specified IPAddress
* _GET /apis/networking.k8s.io/v1alpha1/servicecidrs_ 
  *resource*: list_networking_v1_alpha_1_service_cidr  
  *description*: list or watch objects of kind ServiceCIDR
* _GET /apis/networking.k8s.io/v1alpha1/servicecidrs/{name}_ 
  *resource*: read_networking_v1_alpha_1_service_cidr  
  *description*: read the specified ServiceCIDR
* _GET /apis/networking.k8s.io/v1alpha1/servicecidrs/{name}/status_ 
  *resource*: read_networking_v1_alpha_1_service_cidr_status  
  *description*: read status of the specified ServiceCIDR
* _GET /apis/networking.k8s.io/v1alpha1/watch/ipaddresses_ 
  *resource*: watch_networking_v1_alpha_1ip_address_list  
  *description*: watch individual changes to a list of IPAddress. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1alpha1/watch/ipaddresses/{name}_ 
  *resource*: watch_networking_v1_alpha_1ip_address  
  *description*: watch changes to an object of kind IPAddress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/networking.k8s.io/v1alpha1/watch/servicecidrs_ 
  *resource*: watch_networking_v1_alpha_1_service_cidr_list  
  *description*: watch individual changes to a list of ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/networking.k8s.io/v1alpha1/watch/servicecidrs/{name}_ 
  *resource*: watch_networking_v1_alpha_1_service_cidr  
  *description*: watch changes to an object of kind ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/nodes_ 
  *resource*: list_core_v1_node  
  *description*: list or watch objects of kind Node
* _GET /api/v1/nodes/{name}_ 
  *resource*: read_core_v1_node  
  *description*: read the specified Node
* _GET /api/v1/watch/nodes_ 
  *resource*: watch_core_v1_node_list  
  *description*: watch individual changes to a list of Node. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/nodes/{name}_ 
  *resource*: watch_core_v1_node  
  *description*: watch changes to an object of kind Node. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/node.k8s.io/_ 
  *resource*: get_node_api_group  
  *description*: get information of a group
* _GET /apis/node.k8s.io/v1/_ 
  *resource*: get_node_v1api_resources  
  *description*: get available resources
* _GET /apis/node.k8s.io/v1/runtimeclasses_ 
  *resource*: list_node_v1_runtime_class  
  *description*: list or watch objects of kind RuntimeClass
* _GET /apis/node.k8s.io/v1/runtimeclasses/{name}_ 
  *resource*: read_node_v1_runtime_class  
  *description*: read the specified RuntimeClass
* _GET /apis/node.k8s.io/v1/watch/runtimeclasses_ 
  *resource*: watch_node_v1_runtime_class_list  
  *description*: watch individual changes to a list of RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/node.k8s.io/v1/watch/runtimeclasses/{name}_ 
  *resource*: watch_node_v1_runtime_class  
  *description*: watch changes to an object of kind RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/persistentvolumes_ 
  *resource*: list_core_v1_persistent_volume  
  *description*: list or watch objects of kind PersistentVolume
* _GET /api/v1/persistentvolumes/{name}_ 
  *resource*: read_core_v1_persistent_volume  
  *description*: read the specified PersistentVolume
* _GET /api/v1/watch/persistentvolumes_ 
  *resource*: watch_core_v1_persistent_volume_list  
  *description*: watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/persistentvolumes/{name}_ 
  *resource*: watch_core_v1_persistent_volume  
  *description*: watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/namespaces/{namespace}/persistentvolumeclaims_ 
  *resource*: list_core_v1_namespaced_persistent_volume_claim  
  *description*: list or watch objects of kind PersistentVolumeClaim
* _GET /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}_ 
  *resource*: read_core_v1_namespaced_persistent_volume_claim  
  *description*: read the specified PersistentVolumeClaim
* _GET /api/v1/persistentvolumeclaims_ 
  *resource*: list_core_v1_persistent_volume_claim_for_all_namespaces  
  *description*: list or watch objects of kind PersistentVolumeClaim
* _GET /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims_ 
  *resource*: watch_core_v1_namespaced_persistent_volume_claim_list  
  *description*: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}_ 
  *resource*: watch_core_v1_namespaced_persistent_volume_claim  
  *description*: watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/persistentvolumeclaims_ 
  *resource*: watch_core_v1_persistent_volume_claim_list_for_all_namespaces  
  *description*: watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/pods_ 
  *resource*: list_core_v1_namespaced_pod  
  *description*: list or watch objects of kind Pod
* _GET /api/v1/namespaces/{namespace}/pods/{name}_ 
  *resource*: read_core_v1_namespaced_pod  
  *description*: read the specified Pod
* _GET /api/v1/pods_ 
  *resource*: list_core_v1_pod_for_all_namespaces  
  *description*: list or watch objects of kind Pod
* _GET /api/v1/watch/namespaces/{namespace}/pods_ 
  *resource*: watch_core_v1_namespaced_pod_list  
  *description*: watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/pods/{name}_ 
  *resource*: watch_core_v1_namespaced_pod  
  *description*: watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/pods_ 
  *resource*: watch_core_v1_pod_list_for_all_namespaces  
  *description*: watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets_ 
  *resource*: list_policy_v1_namespaced_pod_disruption_budget  
  *description*: list or watch objects of kind PodDisruptionBudget
* _GET /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}_ 
  *resource*: read_policy_v1_namespaced_pod_disruption_budget  
  *description*: read the specified PodDisruptionBudget
* _GET /apis/policy/v1/poddisruptionbudgets_ 
  *resource*: list_policy_v1_pod_disruption_budget_for_all_namespaces  
  *description*: list or watch objects of kind PodDisruptionBudget
* _GET /apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets_ 
  *resource*: watch_policy_v1_namespaced_pod_disruption_budget_list  
  *description*: watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets/{name}_ 
  *resource*: watch_policy_v1_namespaced_pod_disruption_budget  
  *description*: watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/policy/v1/watch/poddisruptionbudgets_ 
  *resource*: watch_policy_v1_pod_disruption_budget_list_for_all_namespaces  
  *description*: watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/podtemplates_ 
  *resource*: list_core_v1_namespaced_pod_template  
  *description*: list or watch objects of kind PodTemplate
* _GET /api/v1/namespaces/{namespace}/podtemplates/{name}_ 
  *resource*: read_core_v1_namespaced_pod_template  
  *description*: read the specified PodTemplate
* _GET /api/v1/podtemplates_ 
  *resource*: list_core_v1_pod_template_for_all_namespaces  
  *description*: list or watch objects of kind PodTemplate
* _GET /api/v1/watch/namespaces/{namespace}/podtemplates_ 
  *resource*: watch_core_v1_namespaced_pod_template_list  
  *description*: watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/podtemplates/{name}_ 
  *resource*: watch_core_v1_namespaced_pod_template  
  *description*: watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/podtemplates_ 
  *resource*: watch_core_v1_pod_template_list_for_all_namespaces  
  *description*: watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/policy/_ 
  *resource*: get_policy_api_group  
  *description*: get information of a group
* _GET /api/v1/namespaces/{namespace}/pods/{name}/portforward_ 
  *resource*: connect_core_v1_get_namespaced_pod_portforward  
  *description*: connect GET requests to portforward of Pod
* _GET /api/v1/namespaces/{namespace}/pods/{name}/proxy_ 
  *resource*: connect_core_v1_get_namespaced_pod_proxy  
  *description*: connect GET requests to proxy of Pod
* _GET /api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}_ 
  *resource*: connect_core_v1_get_namespaced_pod_proxy_with_path  
  *description*: connect GET requests to proxy of Pod
* _GET /api/v1/namespaces/{namespace}/services/{name}/proxy_ 
  *resource*: connect_core_v1_get_namespaced_service_proxy  
  *description*: connect GET requests to proxy of Service
* _GET /api/v1/namespaces/{namespace}/services/{name}/proxy/{path}_ 
  *resource*: connect_core_v1_get_namespaced_service_proxy_with_path  
  *description*: connect GET requests to proxy of Service
* _GET /api/v1/nodes/{name}/proxy_ 
  *resource*: connect_core_v1_get_node_proxy  
  *description*: connect GET requests to proxy of Node
* _GET /api/v1/nodes/{name}/proxy/{path}_ 
  *resource*: connect_core_v1_get_node_proxy_with_path  
  *description*: connect GET requests to proxy of Node
* _GET /apis/rbac.authorization.k8s.io/_ 
  *resource*: get_rbac_authorization_api_group  
  *description*: get information of a group
* _GET /apis/rbac.authorization.k8s.io/v1/_ 
  *resource*: get_rbac_authorization_v1api_resources  
  *description*: get available resources
* _GET /apis/rbac.authorization.k8s.io/v1/clusterrolebindings_ 
  *resource*: list_rbac_authorization_v1_cluster_role_binding  
  *description*: list or watch objects of kind ClusterRoleBinding
* _GET /apis/rbac.authorization.k8s.io/v1/clusterrolebindings/{name}_ 
  *resource*: read_rbac_authorization_v1_cluster_role_binding  
  *description*: read the specified ClusterRoleBinding
* _GET /apis/rbac.authorization.k8s.io/v1/clusterroles_ 
  *resource*: list_rbac_authorization_v1_cluster_role  
  *description*: list or watch objects of kind ClusterRole
* _GET /apis/rbac.authorization.k8s.io/v1/clusterroles/{name}_ 
  *resource*: read_rbac_authorization_v1_cluster_role  
  *description*: read the specified ClusterRole
* _GET /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings_ 
  *resource*: list_rbac_authorization_v1_namespaced_role_binding  
  *description*: list or watch objects of kind RoleBinding
* _GET /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings/{name}_ 
  *resource*: read_rbac_authorization_v1_namespaced_role_binding  
  *description*: read the specified RoleBinding
* _GET /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles_ 
  *resource*: list_rbac_authorization_v1_namespaced_role  
  *description*: list or watch objects of kind Role
* _GET /apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles/{name}_ 
  *resource*: read_rbac_authorization_v1_namespaced_role  
  *description*: read the specified Role
* _GET /apis/rbac.authorization.k8s.io/v1/rolebindings_ 
  *resource*: list_rbac_authorization_v1_role_binding_for_all_namespaces  
  *description*: list or watch objects of kind RoleBinding
* _GET /apis/rbac.authorization.k8s.io/v1/roles_ 
  *resource*: list_rbac_authorization_v1_role_for_all_namespaces  
  *description*: list or watch objects of kind Role
* _GET /apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings_ 
  *resource*: watch_rbac_authorization_v1_cluster_role_binding_list  
  *description*: watch individual changes to a list of ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings/{name}_ 
  *resource*: watch_rbac_authorization_v1_cluster_role_binding  
  *description*: watch changes to an object of kind ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/clusterroles_ 
  *resource*: watch_rbac_authorization_v1_cluster_role_list  
  *description*: watch individual changes to a list of ClusterRole. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/clusterroles/{name}_ 
  *resource*: watch_rbac_authorization_v1_cluster_role  
  *description*: watch changes to an object of kind ClusterRole. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings_ 
  *resource*: watch_rbac_authorization_v1_namespaced_role_binding_list  
  *description*: watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings/{name}_ 
  *resource*: watch_rbac_authorization_v1_namespaced_role_binding  
  *description*: watch changes to an object of kind RoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles_ 
  *resource*: watch_rbac_authorization_v1_namespaced_role_list  
  *description*: watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles/{name}_ 
  *resource*: watch_rbac_authorization_v1_namespaced_role  
  *description*: watch changes to an object of kind Role. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/rolebindings_ 
  *resource*: watch_rbac_authorization_v1_role_binding_list_for_all_namespaces  
  *description*: watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/rbac.authorization.k8s.io/v1/watch/roles_ 
  *resource*: watch_rbac_authorization_v1_role_list_for_all_namespaces  
  *description*: watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/namespaces/{namespace}/replicasets_ 
  *resource*: list_apps_v1_namespaced_replica_set  
  *description*: list or watch objects of kind ReplicaSet
* _GET /apis/apps/v1/namespaces/{namespace}/replicasets/{name}_ 
  *resource*: read_apps_v1_namespaced_replica_set  
  *description*: read the specified ReplicaSet
* _GET /apis/apps/v1/replicasets_ 
  *resource*: list_apps_v1_replica_set_for_all_namespaces  
  *description*: list or watch objects of kind ReplicaSet
* _GET /apis/apps/v1/watch/namespaces/{namespace}/replicasets_ 
  *resource*: watch_apps_v1_namespaced_replica_set_list  
  *description*: watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/replicasets/{name}_ 
  *resource*: watch_apps_v1_namespaced_replica_set  
  *description*: watch changes to an object of kind ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apps/v1/watch/replicasets_ 
  *resource*: watch_apps_v1_replica_set_list_for_all_namespaces  
  *description*: watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/replicationcontrollers_ 
  *resource*: list_core_v1_namespaced_replication_controller  
  *description*: list or watch objects of kind ReplicationController
* _GET /api/v1/namespaces/{namespace}/replicationcontrollers/{name}_ 
  *resource*: read_core_v1_namespaced_replication_controller  
  *description*: read the specified ReplicationController
* _GET /api/v1/replicationcontrollers_ 
  *resource*: list_core_v1_replication_controller_for_all_namespaces  
  *description*: list or watch objects of kind ReplicationController
* _GET /api/v1/watch/namespaces/{namespace}/replicationcontrollers_ 
  *resource*: watch_core_v1_namespaced_replication_controller_list  
  *description*: watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/replicationcontrollers/{name}_ 
  *resource*: watch_core_v1_namespaced_replication_controller  
  *description*: watch changes to an object of kind ReplicationController. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/replicationcontrollers_ 
  *resource*: watch_core_v1_replication_controller_list_for_all_namespaces  
  *description*: watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/_ 
  *resource*: get_resource_api_group  
  *description*: get information of a group
* _GET /apis/resource.k8s.io/v1alpha2/_ 
  *resource*: get_resource_v1_alpha_2api_resources  
  *description*: get available resources
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/podschedulingcontexts_ 
  *resource*: list_resource_v1_alpha_2_namespaced_pod_scheduling_context  
  *description*: list or watch objects of kind PodSchedulingContext
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/podschedulingcontexts/{name}_ 
  *resource*: read_resource_v1_alpha_2_namespaced_pod_scheduling_context  
  *description*: read the specified PodSchedulingContext
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/podschedulingcontexts/{name}/status_ 
  *resource*: read_resource_v1_alpha_2_namespaced_pod_scheduling_context_status  
  *description*: read status of the specified PodSchedulingContext
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimparameters_ 
  *resource*: list_resource_v1_alpha_2_namespaced_resource_claim_parameters  
  *description*: list or watch objects of kind ResourceClaimParameters
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimparameters/{name}_ 
  *resource*: read_resource_v1_alpha_2_namespaced_resource_claim_parameters  
  *description*: read the specified ResourceClaimParameters
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaims_ 
  *resource*: list_resource_v1_alpha_2_namespaced_resource_claim  
  *description*: list or watch objects of kind ResourceClaim
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaims/{name}_ 
  *resource*: read_resource_v1_alpha_2_namespaced_resource_claim  
  *description*: read the specified ResourceClaim
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaims/{name}/status_ 
  *resource*: read_resource_v1_alpha_2_namespaced_resource_claim_status  
  *description*: read status of the specified ResourceClaim
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimtemplates_ 
  *resource*: list_resource_v1_alpha_2_namespaced_resource_claim_template  
  *description*: list or watch objects of kind ResourceClaimTemplate
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimtemplates/{name}_ 
  *resource*: read_resource_v1_alpha_2_namespaced_resource_claim_template  
  *description*: read the specified ResourceClaimTemplate
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclassparameters_ 
  *resource*: list_resource_v1_alpha_2_namespaced_resource_class_parameters  
  *description*: list or watch objects of kind ResourceClassParameters
* _GET /apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclassparameters/{name}_ 
  *resource*: read_resource_v1_alpha_2_namespaced_resource_class_parameters  
  *description*: read the specified ResourceClassParameters
* _GET /apis/resource.k8s.io/v1alpha2/podschedulingcontexts_ 
  *resource*: list_resource_v1_alpha_2_pod_scheduling_context_for_all_namespaces  
  *description*: list or watch objects of kind PodSchedulingContext
* _GET /apis/resource.k8s.io/v1alpha2/resourceclaimparameters_ 
  *resource*: list_resource_v1_alpha_2_resource_claim_parameters_for_all_namespaces  
  *description*: list or watch objects of kind ResourceClaimParameters
* _GET /apis/resource.k8s.io/v1alpha2/resourceclaims_ 
  *resource*: list_resource_v1_alpha_2_resource_claim_for_all_namespaces  
  *description*: list or watch objects of kind ResourceClaim
* _GET /apis/resource.k8s.io/v1alpha2/resourceclaimtemplates_ 
  *resource*: list_resource_v1_alpha_2_resource_claim_template_for_all_namespaces  
  *description*: list or watch objects of kind ResourceClaimTemplate
* _GET /apis/resource.k8s.io/v1alpha2/resourceclasses_ 
  *resource*: list_resource_v1_alpha_2_resource_class  
  *description*: list or watch objects of kind ResourceClass
* _GET /apis/resource.k8s.io/v1alpha2/resourceclasses/{name}_ 
  *resource*: read_resource_v1_alpha_2_resource_class  
  *description*: read the specified ResourceClass
* _GET /apis/resource.k8s.io/v1alpha2/resourceclassparameters_ 
  *resource*: list_resource_v1_alpha_2_resource_class_parameters_for_all_namespaces  
  *description*: list or watch objects of kind ResourceClassParameters
* _GET /apis/resource.k8s.io/v1alpha2/resourceslices_ 
  *resource*: list_resource_v1_alpha_2_resource_slice  
  *description*: list or watch objects of kind ResourceSlice
* _GET /apis/resource.k8s.io/v1alpha2/resourceslices/{name}_ 
  *resource*: read_resource_v1_alpha_2_resource_slice  
  *description*: read the specified ResourceSlice
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/podschedulingcontexts_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_pod_scheduling_context_list  
  *description*: watch individual changes to a list of PodSchedulingContext. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/podschedulingcontexts/{name}_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_pod_scheduling_context  
  *description*: watch changes to an object of kind PodSchedulingContext. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimparameters_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_claim_parameters_list  
  *description*: watch individual changes to a list of ResourceClaimParameters. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimparameters/{name}_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_claim_parameters  
  *description*: watch changes to an object of kind ResourceClaimParameters. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaims_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_claim_list  
  *description*: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaims/{name}_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_claim  
  *description*: watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimtemplates_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_claim_template_list  
  *description*: watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimtemplates/{name}_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_claim_template  
  *description*: watch changes to an object of kind ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclassparameters_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_class_parameters_list  
  *description*: watch individual changes to a list of ResourceClassParameters. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclassparameters/{name}_ 
  *resource*: watch_resource_v1_alpha_2_namespaced_resource_class_parameters  
  *description*: watch changes to an object of kind ResourceClassParameters. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/resource.k8s.io/v1alpha2/watch/podschedulingcontexts_ 
  *resource*: watch_resource_v1_alpha_2_pod_scheduling_context_list_for_all_namespaces  
  *description*: watch individual changes to a list of PodSchedulingContext. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceclaimparameters_ 
  *resource*: watch_resource_v1_alpha_2_resource_claim_parameters_list_for_all_namespaces  
  *description*: watch individual changes to a list of ResourceClaimParameters. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceclaims_ 
  *resource*: watch_resource_v1_alpha_2_resource_claim_list_for_all_namespaces  
  *description*: watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceclaimtemplates_ 
  *resource*: watch_resource_v1_alpha_2_resource_claim_template_list_for_all_namespaces  
  *description*: watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceclasses_ 
  *resource*: watch_resource_v1_alpha_2_resource_class_list  
  *description*: watch individual changes to a list of ResourceClass. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceclasses/{name}_ 
  *resource*: watch_resource_v1_alpha_2_resource_class  
  *description*: watch changes to an object of kind ResourceClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceclassparameters_ 
  *resource*: watch_resource_v1_alpha_2_resource_class_parameters_list_for_all_namespaces  
  *description*: watch individual changes to a list of ResourceClassParameters. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceslices_ 
  *resource*: watch_resource_v1_alpha_2_resource_slice_list  
  *description*: watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/resource.k8s.io/v1alpha2/watch/resourceslices/{name}_ 
  *resource*: watch_resource_v1_alpha_2_resource_slice  
  *description*: watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/namespaces/{namespace}/resourcequotas_ 
  *resource*: list_core_v1_namespaced_resource_quota  
  *description*: list or watch objects of kind ResourceQuota
* _GET /api/v1/namespaces/{namespace}/resourcequotas/{name}_ 
  *resource*: read_core_v1_namespaced_resource_quota  
  *description*: read the specified ResourceQuota
* _GET /api/v1/resourcequotas_ 
  *resource*: list_core_v1_resource_quota_for_all_namespaces  
  *description*: list or watch objects of kind ResourceQuota
* _GET /api/v1/watch/namespaces/{namespace}/resourcequotas_ 
  *resource*: watch_core_v1_namespaced_resource_quota_list  
  *description*: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/resourcequotas/{name}_ 
  *resource*: watch_core_v1_namespaced_resource_quota  
  *description*: watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/resourcequotas_ 
  *resource*: watch_core_v1_resource_quota_list_for_all_namespaces  
  *description*: watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale_ 
  *resource*: read_core_v1_namespaced_replication_controller_scale  
  *description*: read scale of the specified ReplicationController
* _GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale_ 
  *resource*: read_apps_v1_namespaced_deployment_scale  
  *description*: read scale of the specified Deployment
* _GET /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale_ 
  *resource*: read_apps_v1_namespaced_replica_set_scale  
  *description*: read scale of the specified ReplicaSet
* _GET /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/scale_ 
  *resource*: read_apps_v1_namespaced_stateful_set_scale  
  *description*: read scale of the specified StatefulSet
* _GET /apis/scheduling.k8s.io/_ 
  *resource*: get_scheduling_api_group  
  *description*: get information of a group
* _GET /apis/scheduling.k8s.io/v1/_ 
  *resource*: get_scheduling_v1api_resources  
  *description*: get available resources
* _GET /apis/scheduling.k8s.io/v1/priorityclasses_ 
  *resource*: list_scheduling_v1_priority_class  
  *description*: list or watch objects of kind PriorityClass
* _GET /apis/scheduling.k8s.io/v1/priorityclasses/{name}_ 
  *resource*: read_scheduling_v1_priority_class  
  *description*: read the specified PriorityClass
* _GET /apis/scheduling.k8s.io/v1/watch/priorityclasses_ 
  *resource*: watch_scheduling_v1_priority_class_list  
  *description*: watch individual changes to a list of PriorityClass. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/scheduling.k8s.io/v1/watch/priorityclasses/{name}_ 
  *resource*: watch_scheduling_v1_priority_class  
  *description*: watch changes to an object of kind PriorityClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/namespaces/{namespace}/secrets_ 
  *resource*: list_core_v1_namespaced_secret  
  *description*: list or watch objects of kind Secret
* _GET /api/v1/namespaces/{namespace}/secrets/{name}_ 
  *resource*: read_core_v1_namespaced_secret  
  *description*: read the specified Secret
* _GET /api/v1/secrets_ 
  *resource*: list_core_v1_secret_for_all_namespaces  
  *description*: list or watch objects of kind Secret
* _GET /api/v1/watch/namespaces/{namespace}/secrets_ 
  *resource*: watch_core_v1_namespaced_secret_list  
  *description*: watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/secrets/{name}_ 
  *resource*: watch_core_v1_namespaced_secret  
  *description*: watch changes to an object of kind Secret. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/secrets_ 
  *resource*: watch_core_v1_secret_list_for_all_namespaces  
  *description*: watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/services_ 
  *resource*: list_core_v1_namespaced_service  
  *description*: list or watch objects of kind Service
* _GET /api/v1/namespaces/{namespace}/services/{name}_ 
  *resource*: read_core_v1_namespaced_service  
  *description*: read the specified Service
* _GET /api/v1/services_ 
  *resource*: list_core_v1_service_for_all_namespaces  
  *description*: list or watch objects of kind Service
* _GET /api/v1/watch/namespaces/{namespace}/services_ 
  *resource*: watch_core_v1_namespaced_service_list  
  *description*: watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/services/{name}_ 
  *resource*: watch_core_v1_namespaced_service  
  *description*: watch changes to an object of kind Service. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/services_ 
  *resource*: watch_core_v1_service_list_for_all_namespaces  
  *description*: watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/serviceaccounts_ 
  *resource*: list_core_v1_namespaced_service_account  
  *description*: list or watch objects of kind ServiceAccount
* _GET /api/v1/namespaces/{namespace}/serviceaccounts/{name}_ 
  *resource*: read_core_v1_namespaced_service_account  
  *description*: read the specified ServiceAccount
* _GET /api/v1/serviceaccounts_ 
  *resource*: list_core_v1_service_account_for_all_namespaces  
  *description*: list or watch objects of kind ServiceAccount
* _GET /api/v1/watch/namespaces/{namespace}/serviceaccounts_ 
  *resource*: watch_core_v1_namespaced_service_account_list  
  *description*: watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/watch/namespaces/{namespace}/serviceaccounts/{name}_ 
  *resource*: watch_core_v1_namespaced_service_account  
  *description*: watch changes to an object of kind ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/watch/serviceaccounts_ 
  *resource*: watch_core_v1_service_account_list_for_all_namespaces  
  *description*: watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/namespaces/{namespace}/statefulsets_ 
  *resource*: list_apps_v1_namespaced_stateful_set  
  *description*: list or watch objects of kind StatefulSet
* _GET /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}_ 
  *resource*: read_apps_v1_namespaced_stateful_set  
  *description*: read the specified StatefulSet
* _GET /apis/apps/v1/statefulsets_ 
  *resource*: list_apps_v1_stateful_set_for_all_namespaces  
  *description*: list or watch objects of kind StatefulSet
* _GET /apis/apps/v1/watch/namespaces/{namespace}/statefulsets_ 
  *resource*: watch_apps_v1_namespaced_stateful_set_list  
  *description*: watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/apps/v1/watch/namespaces/{namespace}/statefulsets/{name}_ 
  *resource*: watch_apps_v1_namespaced_stateful_set  
  *description*: watch changes to an object of kind StatefulSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/apps/v1/watch/statefulsets_ 
  *resource*: watch_apps_v1_stateful_set_list_for_all_namespaces  
  *description*: watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status_ 
  *resource*: read_core_v1_namespaced_persistent_volume_claim_status  
  *description*: read status of the specified PersistentVolumeClaim
* _GET /api/v1/namespaces/{namespace}/pods/{name}/status_ 
  *resource*: read_core_v1_namespaced_pod_status  
  *description*: read status of the specified Pod
* _GET /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status_ 
  *resource*: read_core_v1_namespaced_replication_controller_status  
  *description*: read status of the specified ReplicationController
* _GET /api/v1/namespaces/{namespace}/resourcequotas/{name}/status_ 
  *resource*: read_core_v1_namespaced_resource_quota_status  
  *description*: read status of the specified ResourceQuota
* _GET /api/v1/namespaces/{namespace}/services/{name}/status_ 
  *resource*: read_core_v1_namespaced_service_status  
  *description*: read status of the specified Service
* _GET /api/v1/namespaces/{name}/status_ 
  *resource*: read_core_v1_namespace_status  
  *description*: read status of the specified Namespace
* _GET /api/v1/nodes/{name}/status_ 
  *resource*: read_core_v1_node_status  
  *description*: read status of the specified Node
* _GET /api/v1/persistentvolumes/{name}/status_ 
  *resource*: read_core_v1_persistent_volume_status  
  *description*: read status of the specified PersistentVolume
* _GET /apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status_ 
  *resource*: read_apps_v1_namespaced_daemon_set_status  
  *description*: read status of the specified DaemonSet
* _GET /apis/apps/v1/namespaces/{namespace}/deployments/{name}/status_ 
  *resource*: read_apps_v1_namespaced_deployment_status  
  *description*: read status of the specified Deployment
* _GET /apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status_ 
  *resource*: read_apps_v1_namespaced_replica_set_status  
  *description*: read status of the specified ReplicaSet
* _GET /apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/status_ 
  *resource*: read_apps_v1_namespaced_stateful_set_status  
  *description*: read status of the specified StatefulSet
* _GET /apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status_ 
  *resource*: read_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status  
  *description*: read status of the specified HorizontalPodAutoscaler
* _GET /apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status_ 
  *resource*: read_autoscaling_v2_namespaced_horizontal_pod_autoscaler_status  
  *description*: read status of the specified HorizontalPodAutoscaler
* _GET /apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status_ 
  *resource*: read_batch_v1_namespaced_cron_job_status  
  *description*: read status of the specified CronJob
* _GET /apis/batch/v1/namespaces/{namespace}/jobs/{name}/status_ 
  *resource*: read_batch_v1_namespaced_job_status  
  *description*: read status of the specified Job
* _GET /apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}/status_ 
  *resource*: read_policy_v1_namespaced_pod_disruption_budget_status  
  *description*: read status of the specified PodDisruptionBudget
* _GET /apis/storage.k8s.io/_ 
  *resource*: get_storage_api_group  
  *description*: get information of a group
* _GET /apis/storage.k8s.io/v1/_ 
  *resource*: get_storage_v1api_resources  
  *description*: get available resources
* _GET /apis/storage.k8s.io/v1/csidrivers_ 
  *resource*: list_storage_v1csi_driver  
  *description*: list or watch objects of kind CSIDriver
* _GET /apis/storage.k8s.io/v1/csidrivers/{name}_ 
  *resource*: read_storage_v1csi_driver  
  *description*: read the specified CSIDriver
* _GET /apis/storage.k8s.io/v1/csinodes_ 
  *resource*: list_storage_v1csi_node  
  *description*: list or watch objects of kind CSINode
* _GET /apis/storage.k8s.io/v1/csinodes/{name}_ 
  *resource*: read_storage_v1csi_node  
  *description*: read the specified CSINode
* _GET /apis/storage.k8s.io/v1/csistoragecapacities_ 
  *resource*: list_storage_v1csi_storage_capacity_for_all_namespaces  
  *description*: list or watch objects of kind CSIStorageCapacity
* _GET /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities_ 
  *resource*: list_storage_v1_namespaced_csi_storage_capacity  
  *description*: list or watch objects of kind CSIStorageCapacity
* _GET /apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name}_ 
  *resource*: read_storage_v1_namespaced_csi_storage_capacity  
  *description*: read the specified CSIStorageCapacity
* _GET /apis/storage.k8s.io/v1/storageclasses_ 
  *resource*: list_storage_v1_storage_class  
  *description*: list or watch objects of kind StorageClass
* _GET /apis/storage.k8s.io/v1/storageclasses/{name}_ 
  *resource*: read_storage_v1_storage_class  
  *description*: read the specified StorageClass
* _GET /apis/storage.k8s.io/v1/volumeattachments_ 
  *resource*: list_storage_v1_volume_attachment  
  *description*: list or watch objects of kind VolumeAttachment
* _GET /apis/storage.k8s.io/v1/volumeattachments/{name}_ 
  *resource*: read_storage_v1_volume_attachment  
  *description*: read the specified VolumeAttachment
* _GET /apis/storage.k8s.io/v1/volumeattachments/{name}/status_ 
  *resource*: read_storage_v1_volume_attachment_status  
  *description*: read status of the specified VolumeAttachment
* _GET /apis/storage.k8s.io/v1/watch/csidrivers_ 
  *resource*: watch_storage_v1csi_driver_list  
  *description*: watch individual changes to a list of CSIDriver. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1/watch/csidrivers/{name}_ 
  *resource*: watch_storage_v1csi_driver  
  *description*: watch changes to an object of kind CSIDriver. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/storage.k8s.io/v1/watch/csinodes_ 
  *resource*: watch_storage_v1csi_node_list  
  *description*: watch individual changes to a list of CSINode. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1/watch/csinodes/{name}_ 
  *resource*: watch_storage_v1csi_node  
  *description*: watch changes to an object of kind CSINode. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/storage.k8s.io/v1/watch/csistoragecapacities_ 
  *resource*: watch_storage_v1csi_storage_capacity_list_for_all_namespaces  
  *description*: watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities_ 
  *resource*: watch_storage_v1_namespaced_csi_storage_capacity_list  
  *description*: watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities/{name}_ 
  *resource*: watch_storage_v1_namespaced_csi_storage_capacity  
  *description*: watch changes to an object of kind CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/storage.k8s.io/v1/watch/storageclasses_ 
  *resource*: watch_storage_v1_storage_class_list  
  *description*: watch individual changes to a list of StorageClass. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1/watch/storageclasses/{name}_ 
  *resource*: watch_storage_v1_storage_class  
  *description*: watch changes to an object of kind StorageClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/storage.k8s.io/v1/watch/volumeattachments_ 
  *resource*: watch_storage_v1_volume_attachment_list  
  *description*: watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1/watch/volumeattachments/{name}_ 
  *resource*: watch_storage_v1_volume_attachment  
  *description*: watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/storage.k8s.io/v1alpha1/_ 
  *resource*: get_storage_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/storage.k8s.io/v1alpha1/volumeattributesclasses_ 
  *resource*: list_storage_v1_alpha_1_volume_attributes_class  
  *description*: list or watch objects of kind VolumeAttributesClass
* _GET /apis/storage.k8s.io/v1alpha1/volumeattributesclasses/{name}_ 
  *resource*: read_storage_v1_alpha_1_volume_attributes_class  
  *description*: read the specified VolumeAttributesClass
* _GET /apis/storage.k8s.io/v1alpha1/watch/volumeattributesclasses_ 
  *resource*: watch_storage_v1_alpha_1_volume_attributes_class_list  
  *description*: watch individual changes to a list of VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storage.k8s.io/v1alpha1/watch/volumeattributesclasses/{name}_ 
  *resource*: watch_storage_v1_alpha_1_volume_attributes_class  
  *description*: watch changes to an object of kind VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /apis/storagemigration.k8s.io/_ 
  *resource*: get_storagemigration_api_group  
  *description*: get information of a group
* _GET /apis/storagemigration.k8s.io/v1alpha1/_ 
  *resource*: get_storagemigration_v1_alpha_1api_resources  
  *description*: get available resources
* _GET /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations_ 
  *resource*: list_storagemigration_v1_alpha_1_storage_version_migration  
  *description*: list or watch objects of kind StorageVersionMigration
* _GET /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}_ 
  *resource*: read_storagemigration_v1_alpha_1_storage_version_migration  
  *description*: read the specified StorageVersionMigration
* _GET /apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}/status_ 
  *resource*: read_storagemigration_v1_alpha_1_storage_version_migration_status  
  *description*: read status of the specified StorageVersionMigration
* _GET /apis/storagemigration.k8s.io/v1alpha1/watch/storageversionmigrations_ 
  *resource*: watch_storagemigration_v1_alpha_1_storage_version_migration_list  
  *description*: watch individual changes to a list of StorageVersionMigration. deprecated: use the 'watch' parameter with a list operation instead.
* _GET /apis/storagemigration.k8s.io/v1alpha1/watch/storageversionmigrations/{name}_ 
  *resource*: watch_storagemigration_v1_alpha_1_storage_version_migration  
  *description*: watch changes to an object of kind StorageVersionMigration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
* _GET /api/v1/_ 
  *resource*: get_core_v1api_resources  
  *description*: get available resources
* _GET /apis/apps/v1/_ 
  *resource*: get_apps_v1api_resources  
  *description*: get available resources
* _GET /apis/autoscaling/v1/_ 
  *resource*: get_autoscaling_v1api_resources  
  *description*: get available resources
* _GET /apis/batch/v1/_ 
  *resource*: get_batch_v1api_resources  
  *description*: get available resources
* _GET /apis/policy/v1/_ 
  *resource*: get_policy_v1api_resources  
  *description*: get available resources
* _GET /apis/autoscaling/v2/_ 
  *resource*: get_autoscaling_v2api_resources  
  *description*: get available resources
* _GET /version/_ 
  *resource*: get_code_version  
  *description*: get the code version
