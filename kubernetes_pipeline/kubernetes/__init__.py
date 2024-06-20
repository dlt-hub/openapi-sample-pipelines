from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="kubernetes_source", max_table_nesting=2)
def kubernetes_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # get service account issuer OpenID configuration, also known as the 'OIDC discovery doc'
            {
                "name": "get_service_account_issuer_open_id_configuration",
                "table_name": "",
                "endpoint": {
                    "path": "/.well-known/openid-configuration/",
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_admissionregistration_api_group",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_admissionregistration_v1api_resources",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind MutatingWebhookConfiguration
            {
                "name": "list_admissionregistration_v1_mutating_webhook_configuration",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/mutatingwebhookconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified MutatingWebhookConfiguration
            {
                "name": "read_admissionregistration_v1_mutating_webhook_configuration",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/mutatingwebhookconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingAdmissionPolicy
            {
                "name": "list_admissionregistration_v1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingAdmissionPolicy
            {
                "name": "read_admissionregistration_v1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ValidatingAdmissionPolicy
            {
                "name": "read_admissionregistration_v1_validating_admission_policy_status",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicies/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingAdmissionPolicyBinding
            {
                "name": "list_admissionregistration_v1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingAdmissionPolicyBinding
            {
                "name": "read_admissionregistration_v1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingadmissionpolicybindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingWebhookConfiguration
            {
                "name": "list_admissionregistration_v1_validating_webhook_configuration",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingWebhookConfiguration
            {
                "name": "read_admissionregistration_v1_validating_webhook_configuration",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/validatingwebhookconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_mutating_webhook_configuration_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/mutatingwebhookconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind MutatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_mutating_webhook_configuration",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/mutatingwebhookconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_validating_admission_policy_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_validating_admission_policy_binding_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/validatingadmissionpolicybindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_validating_webhook_configuration_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingWebhookConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_validating_webhook_configuration",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1/watch/validatingwebhookconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_admissionregistration_v1_alpha_1api_resources",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingAdmissionPolicy
            {
                "name": "list_admissionregistration_v1_alpha_1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingAdmissionPolicy
            {
                "name": "read_admissionregistration_v1_alpha_1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ValidatingAdmissionPolicy
            {
                "name": "read_admissionregistration_v1_alpha_1_validating_admission_policy_status",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicies/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingAdmissionPolicyBinding
            {
                "name": "list_admissionregistration_v1_alpha_1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicybindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingAdmissionPolicyBinding
            {
                "name": "read_admissionregistration_v1_alpha_1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/validatingadmissionpolicybindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_alpha_1_validating_admission_policy_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_alpha_1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_alpha_1_validating_admission_policy_binding_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicybindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_alpha_1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1alpha1/watch/validatingadmissionpolicybindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_admissionregistration_v1_beta_1api_resources",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingAdmissionPolicy
            {
                "name": "list_admissionregistration_v1_beta_1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingAdmissionPolicy
            {
                "name": "read_admissionregistration_v1_beta_1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ValidatingAdmissionPolicy
            {
                "name": "read_admissionregistration_v1_beta_1_validating_admission_policy_status",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ValidatingAdmissionPolicyBinding
            {
                "name": "list_admissionregistration_v1_beta_1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicybindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ValidatingAdmissionPolicyBinding
            {
                "name": "read_admissionregistration_v1_beta_1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/validatingadmissionpolicybindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_beta_1_validating_admission_policy_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingAdmissionPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_beta_1_validating_admission_policy",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_admissionregistration_v1_beta_1_validating_admission_policy_binding_list",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicybindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ValidatingAdmissionPolicyBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_admissionregistration_v1_beta_1_validating_admission_policy_binding",
                "table_name": "admissionregistration",
                "endpoint": {
                    "path": "/apis/admissionregistration.k8s.io/v1beta1/watch/validatingadmissionpolicybindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available API versions
            {
                "name": "get_api_versions",
                "table_name": "api",
                "endpoint": {
                    "path": "/apis/",
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_apiextensions_api_group",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_apiextensions_v1api_resources",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CustomResourceDefinition
            {
                "name": "list_apiextensions_v1_custom_resource_definition",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/v1/customresourcedefinitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified CustomResourceDefinition
            {
                "name": "read_apiextensions_v1_custom_resource_definition",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified CustomResourceDefinition
            {
                "name": "read_apiextensions_v1_custom_resource_definition_status",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/v1/customresourcedefinitions/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apiextensions_v1_custom_resource_definition_list",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind CustomResourceDefinition. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apiextensions_v1_custom_resource_definition",
                "table_name": "apiextension",
                "endpoint": {
                    "path": "/apis/apiextensions.k8s.io/v1/watch/customresourcedefinitions/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_apiregistration_api_group",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_apiregistration_v1api_resources",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind APIService
            {
                "name": "list_apiregistration_v1api_service",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/v1/apiservices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified APIService
            {
                "name": "read_apiregistration_v1api_service",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/v1/apiservices/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified APIService
            {
                "name": "read_apiregistration_v1api_service_status",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/v1/apiservices/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of APIService. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apiregistration_v1api_service_list",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/v1/watch/apiservices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind APIService. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apiregistration_v1api_service",
                "table_name": "apiregistration",
                "endpoint": {
                    "path": "/apis/apiregistration.k8s.io/v1/watch/apiservices/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_apps_api_group",
                "table_name": "app",
                "endpoint": {
                    "path": "/apis/apps/",
                    "paginator": "auto",
                },
            },
            # get available API versions
            {
                "name": "get_core_api_versions",
                "table_name": "apus",
                "endpoint": {
                    "path": "/api/",
                    "paginator": "auto",
                },
            },
            # connect GET requests to attach of Pod
            {
                "name": "connect_core_v1_get_namespaced_pod_attach",
                "table_name": "attach",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/attach",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "container": "OPTIONAL_CONFIG",
                        # "stderr": "OPTIONAL_CONFIG",
                        # "stdin": "OPTIONAL_CONFIG",
                        # "stdout": "OPTIONAL_CONFIG",
                        # "tty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_authentication_api_group",
                "table_name": "authentication",
                "endpoint": {
                    "path": "/apis/authentication.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_authentication_v1api_resources",
                "table_name": "authentication",
                "endpoint": {
                    "path": "/apis/authentication.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_authentication_v1_alpha_1api_resources",
                "table_name": "authentication",
                "endpoint": {
                    "path": "/apis/authentication.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_authentication_v1_beta_1api_resources",
                "table_name": "authentication",
                "endpoint": {
                    "path": "/apis/authentication.k8s.io/v1beta1/",
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_authorization_api_group",
                "table_name": "authorization",
                "endpoint": {
                    "path": "/apis/authorization.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_authorization_v1api_resources",
                "table_name": "authorization",
                "endpoint": {
                    "path": "/apis/authorization.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_autoscaling_api_group",
                "table_name": "autoscaling",
                "endpoint": {
                    "path": "/apis/autoscaling/",
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_batch_api_group",
                "table_name": "batch",
                "endpoint": {
                    "path": "/apis/batch/",
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_certificates_api_group",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_certificates_v1api_resources",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CertificateSigningRequest
            {
                "name": "list_certificates_v1_certificate_signing_request",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/certificatesigningrequests",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified CertificateSigningRequest
            {
                "name": "read_certificates_v1_certificate_signing_request",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read approval of the specified CertificateSigningRequest
            {
                "name": "read_certificates_v1_certificate_signing_request_approval",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/approval",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified CertificateSigningRequest
            {
                "name": "read_certificates_v1_certificate_signing_request_status",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/certificatesigningrequests/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_certificates_v1_certificate_signing_request_list",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/watch/certificatesigningrequests",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind CertificateSigningRequest. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_certificates_v1_certificate_signing_request",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1/watch/certificatesigningrequests/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_certificates_v1_alpha_1api_resources",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ClusterTrustBundle
            {
                "name": "list_certificates_v1_alpha_1_cluster_trust_bundle",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1alpha1/clustertrustbundles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ClusterTrustBundle
            {
                "name": "read_certificates_v1_alpha_1_cluster_trust_bundle",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1alpha1/clustertrustbundles/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ClusterTrustBundle. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_certificates_v1_alpha_1_cluster_trust_bundle_list",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1alpha1/watch/clustertrustbundles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ClusterTrustBundle. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_certificates_v1_alpha_1_cluster_trust_bundle",
                "table_name": "certificate",
                "endpoint": {
                    "path": "/apis/certificates.k8s.io/v1alpha1/watch/clustertrustbundles/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list objects of kind ComponentStatus
            {
                "name": "list_core_v1_component_status",
                "table_name": "componentstatus",
                "endpoint": {
                    "path": "/api/v1/componentstatuses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ComponentStatus
            {
                "name": "read_core_v1_component_status",
                "table_name": "componentstatus",
                "endpoint": {
                    "path": "/api/v1/componentstatuses/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ConfigMap
            {
                "name": "list_core_v1_config_map_for_all_namespaces",
                "table_name": "configmap",
                "endpoint": {
                    "path": "/api/v1/configmaps",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ConfigMap
            {
                "name": "list_core_v1_namespaced_config_map",
                "table_name": "configmap",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/configmaps",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ConfigMap
            {
                "name": "read_core_v1_namespaced_config_map",
                "table_name": "configmap",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/configmaps/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_config_map_list_for_all_namespaces",
                "table_name": "configmap",
                "endpoint": {
                    "path": "/api/v1/watch/configmaps",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ConfigMap. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_config_map_list",
                "table_name": "configmap",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/configmaps",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ConfigMap. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_config_map",
                "table_name": "configmap",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/configmaps/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ControllerRevision
            {
                "name": "list_apps_v1_controller_revision_for_all_namespaces",
                "table_name": "controllerrevision",
                "endpoint": {
                    "path": "/apis/apps/v1/controllerrevisions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ControllerRevision
            {
                "name": "list_apps_v1_namespaced_controller_revision",
                "table_name": "controllerrevision",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/controllerrevisions",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ControllerRevision
            {
                "name": "read_apps_v1_namespaced_controller_revision",
                "table_name": "controllerrevision",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/controllerrevisions/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ControllerRevision. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_controller_revision_list_for_all_namespaces",
                "table_name": "controllerrevision",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/controllerrevisions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ControllerRevision. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_namespaced_controller_revision_list",
                "table_name": "controllerrevision",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/controllerrevisions",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ControllerRevision. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apps_v1_namespaced_controller_revision",
                "table_name": "controllerrevision",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/controllerrevisions/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_coordination_api_group",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_coordination_v1api_resources",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Lease
            {
                "name": "list_coordination_v1_lease_for_all_namespaces",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/leases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Lease
            {
                "name": "list_coordination_v1_namespaced_lease",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/namespaces/{namespace}/leases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Lease
            {
                "name": "read_coordination_v1_namespaced_lease",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/namespaces/{namespace}/leases/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Lease. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_coordination_v1_lease_list_for_all_namespaces",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/watch/leases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Lease. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_coordination_v1_namespaced_lease_list",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/watch/namespaces/{namespace}/leases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Lease. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_coordination_v1_namespaced_lease",
                "table_name": "coordination",
                "endpoint": {
                    "path": "/apis/coordination.k8s.io/v1/watch/namespaces/{namespace}/leases/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CronJob
            {
                "name": "list_batch_v1_cron_job_for_all_namespaces",
                "table_name": "cronjob",
                "endpoint": {
                    "path": "/apis/batch/v1/cronjobs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CronJob
            {
                "name": "list_batch_v1_namespaced_cron_job",
                "table_name": "cronjob",
                "endpoint": {
                    "path": "/apis/batch/v1/namespaces/{namespace}/cronjobs",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified CronJob
            {
                "name": "read_batch_v1_namespaced_cron_job",
                "table_name": "cronjob",
                "endpoint": {
                    "path": "/apis/batch/v1/namespaces/{namespace}/cronjobs/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_batch_v1_cron_job_list_for_all_namespaces",
                "table_name": "cronjob",
                "endpoint": {
                    "path": "/apis/batch/v1/watch/cronjobs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CronJob. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_batch_v1_namespaced_cron_job_list",
                "table_name": "cronjob",
                "endpoint": {
                    "path": "/apis/batch/v1/watch/namespaces/{namespace}/cronjobs",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind CronJob. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_batch_v1_namespaced_cron_job",
                "table_name": "cronjob",
                "endpoint": {
                    "path": "/apis/batch/v1/watch/namespaces/{namespace}/cronjobs/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind DaemonSet
            {
                "name": "list_apps_v1_daemon_set_for_all_namespaces",
                "table_name": "daemonset",
                "endpoint": {
                    "path": "/apis/apps/v1/daemonsets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind DaemonSet
            {
                "name": "list_apps_v1_namespaced_daemon_set",
                "table_name": "daemonset",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/daemonsets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified DaemonSet
            {
                "name": "read_apps_v1_namespaced_daemon_set",
                "table_name": "daemonset",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/daemonsets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_daemon_set_list_for_all_namespaces",
                "table_name": "daemonset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/daemonsets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of DaemonSet. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_namespaced_daemon_set_list",
                "table_name": "daemonset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/daemonsets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind DaemonSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apps_v1_namespaced_daemon_set",
                "table_name": "daemonset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/daemonsets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Deployment
            {
                "name": "list_apps_v1_deployment_for_all_namespaces",
                "table_name": "deployment",
                "endpoint": {
                    "path": "/apis/apps/v1/deployments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Deployment
            {
                "name": "list_apps_v1_namespaced_deployment",
                "table_name": "deployment",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/deployments",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Deployment
            {
                "name": "read_apps_v1_namespaced_deployment",
                "table_name": "deployment",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/deployments/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_deployment_list_for_all_namespaces",
                "table_name": "deployment",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/deployments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Deployment. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_namespaced_deployment_list",
                "table_name": "deployment",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/deployments",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Deployment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apps_v1_namespaced_deployment",
                "table_name": "deployment",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/deployments/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_discovery_api_group",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_discovery_v1api_resources",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind EndpointSlice
            {
                "name": "list_discovery_v1_endpoint_slice_for_all_namespaces",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/endpointslices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind EndpointSlice
            {
                "name": "list_discovery_v1_namespaced_endpoint_slice",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/namespaces/{namespace}/endpointslices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified EndpointSlice
            {
                "name": "read_discovery_v1_namespaced_endpoint_slice",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/namespaces/{namespace}/endpointslices/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of EndpointSlice. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_discovery_v1_endpoint_slice_list_for_all_namespaces",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/watch/endpointslices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of EndpointSlice. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_discovery_v1_namespaced_endpoint_slice_list",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/watch/namespaces/{namespace}/endpointslices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind EndpointSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_discovery_v1_namespaced_endpoint_slice",
                "table_name": "discovery",
                "endpoint": {
                    "path": "/apis/discovery.k8s.io/v1/watch/namespaces/{namespace}/endpointslices/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Endpoints
            {
                "name": "list_core_v1_endpoints_for_all_namespaces",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/api/v1/endpoints",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Endpoints
            {
                "name": "list_core_v1_namespaced_endpoints",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/endpoints",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Endpoints
            {
                "name": "read_core_v1_namespaced_endpoints",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/endpoints/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_endpoints_list_for_all_namespaces",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/api/v1/watch/endpoints",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Endpoints. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_endpoints_list",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/endpoints",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Endpoints. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_endpoints",
                "table_name": "endpoint",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/endpoints/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read ephemeralcontainers of the specified Pod
            {
                "name": "read_core_v1_namespaced_pod_ephemeralcontainers",
                "table_name": "ephemeralcontainer",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/ephemeralcontainers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Event
            {
                "name": "list_core_v1_event_for_all_namespaces",
                "table_name": "event",
                "endpoint": {
                    "path": "/api/v1/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Event
            {
                "name": "list_core_v1_namespaced_event",
                "table_name": "event",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/events",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Event
            {
                "name": "read_core_v1_namespaced_event",
                "table_name": "event",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/events/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_event_list_for_all_namespaces",
                "table_name": "event",
                "endpoint": {
                    "path": "/api/v1/watch/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_event_list",
                "table_name": "event",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/events",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_event",
                "table_name": "event",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/events/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_events_api_group",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_events_v1api_resources",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Event
            {
                "name": "list_events_v1_event_for_all_namespaces",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Event
            {
                "name": "list_events_v1_namespaced_event",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/namespaces/{namespace}/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Event
            {
                "name": "read_events_v1_namespaced_event",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/namespaces/{namespace}/events/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_events_v1_event_list_for_all_namespaces",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/watch/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Event. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_events_v1_namespaced_event_list",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/watch/namespaces/{namespace}/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Event. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_events_v1_namespaced_event",
                "table_name": "event",
                "endpoint": {
                    "path": "/apis/events.k8s.io/v1/watch/namespaces/{namespace}/events/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to exec of Pod
            {
                "name": "connect_core_v1_get_namespaced_pod_exec",
                "table_name": "exec",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/exec",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "command": "OPTIONAL_CONFIG",
                        # "container": "OPTIONAL_CONFIG",
                        # "stderr": "OPTIONAL_CONFIG",
                        # "stdin": "OPTIONAL_CONFIG",
                        # "stdout": "OPTIONAL_CONFIG",
                        # "tty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_flowcontrol_apiserver_api_group",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_flowcontrol_apiserver_v1api_resources",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind FlowSchema
            {
                "name": "list_flowcontrol_apiserver_v1_flow_schema",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/flowschemas",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified FlowSchema
            {
                "name": "read_flowcontrol_apiserver_v1_flow_schema",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified FlowSchema
            {
                "name": "read_flowcontrol_apiserver_v1_flow_schema_status",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/flowschemas/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PriorityLevelConfiguration
            {
                "name": "list_flowcontrol_apiserver_v1_priority_level_configuration",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PriorityLevelConfiguration
            {
                "name": "read_flowcontrol_apiserver_v1_priority_level_configuration",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified PriorityLevelConfiguration
            {
                "name": "read_flowcontrol_apiserver_v1_priority_level_configuration_status",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/prioritylevelconfigurations/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of FlowSchema. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_flowcontrol_apiserver_v1_flow_schema_list",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind FlowSchema. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_flowcontrol_apiserver_v1_flow_schema",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/watch/flowschemas/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_flowcontrol_apiserver_v1_priority_level_configuration_list",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_flowcontrol_apiserver_v1_priority_level_configuration",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1/watch/prioritylevelconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_flowcontrol_apiserver_v1_beta_3api_resources",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind FlowSchema
            {
                "name": "list_flowcontrol_apiserver_v1_beta_3_flow_schema",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/flowschemas",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified FlowSchema
            {
                "name": "read_flowcontrol_apiserver_v1_beta_3_flow_schema",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/flowschemas/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified FlowSchema
            {
                "name": "read_flowcontrol_apiserver_v1_beta_3_flow_schema_status",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/flowschemas/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PriorityLevelConfiguration
            {
                "name": "list_flowcontrol_apiserver_v1_beta_3_priority_level_configuration",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/prioritylevelconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PriorityLevelConfiguration
            {
                "name": "read_flowcontrol_apiserver_v1_beta_3_priority_level_configuration",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/prioritylevelconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified PriorityLevelConfiguration
            {
                "name": "read_flowcontrol_apiserver_v1_beta_3_priority_level_configuration_status",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/prioritylevelconfigurations/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of FlowSchema. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_flowcontrol_apiserver_v1_beta_3_flow_schema_list",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/flowschemas",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind FlowSchema. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_flowcontrol_apiserver_v1_beta_3_flow_schema",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/flowschemas/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_flowcontrol_apiserver_v1_beta_3_priority_level_configuration_list",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/prioritylevelconfigurations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PriorityLevelConfiguration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_flowcontrol_apiserver_v1_beta_3_priority_level_configuration",
                "table_name": "flowcontrol",
                "endpoint": {
                    "path": "/apis/flowcontrol.apiserver.k8s.io/v1beta3/watch/prioritylevelconfigurations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind HorizontalPodAutoscaler
            {
                "name": "list_autoscaling_v1_horizontal_pod_autoscaler_for_all_namespaces",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/horizontalpodautoscalers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind HorizontalPodAutoscaler
            {
                "name": "list_autoscaling_v1_namespaced_horizontal_pod_autoscaler",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified HorizontalPodAutoscaler
            {
                "name": "read_autoscaling_v1_namespaced_horizontal_pod_autoscaler",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_autoscaling_v1_horizontal_pod_autoscaler_list_for_all_namespaces",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/watch/horizontalpodautoscalers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler_list",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_autoscaling_v1_namespaced_horizontal_pod_autoscaler",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind HorizontalPodAutoscaler
            {
                "name": "list_autoscaling_v2_horizontal_pod_autoscaler_for_all_namespaces",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/horizontalpodautoscalers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind HorizontalPodAutoscaler
            {
                "name": "list_autoscaling_v2_namespaced_horizontal_pod_autoscaler",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified HorizontalPodAutoscaler
            {
                "name": "read_autoscaling_v2_namespaced_horizontal_pod_autoscaler",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_autoscaling_v2_horizontal_pod_autoscaler_list_for_all_namespaces",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/watch/horizontalpodautoscalers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_autoscaling_v2_namespaced_horizontal_pod_autoscaler_list",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind HorizontalPodAutoscaler. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_autoscaling_v2_namespaced_horizontal_pod_autoscaler",
                "table_name": "horizontalpodautoscaler",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/watch/namespaces/{namespace}/horizontalpodautoscalers/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_internal_apiserver_api_group",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_internal_apiserver_v1_alpha_1api_resources",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind StorageVersion
            {
                "name": "list_internal_apiserver_v1_alpha_1_storage_version",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/v1alpha1/storageversions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified StorageVersion
            {
                "name": "read_internal_apiserver_v1_alpha_1_storage_version",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/v1alpha1/storageversions/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified StorageVersion
            {
                "name": "read_internal_apiserver_v1_alpha_1_storage_version_status",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/v1alpha1/storageversions/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of StorageVersion. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_internal_apiserver_v1_alpha_1_storage_version_list",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/v1alpha1/watch/storageversions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind StorageVersion. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_internal_apiserver_v1_alpha_1_storage_version",
                "table_name": "internal",
                "endpoint": {
                    "path": "/apis/internal.apiserver.k8s.io/v1alpha1/watch/storageversions/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Job
            {
                "name": "list_batch_v1_job_for_all_namespaces",
                "table_name": "job",
                "endpoint": {
                    "path": "/apis/batch/v1/jobs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Job
            {
                "name": "list_batch_v1_namespaced_job",
                "table_name": "job",
                "endpoint": {
                    "path": "/apis/batch/v1/namespaces/{namespace}/jobs",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Job
            {
                "name": "read_batch_v1_namespaced_job",
                "table_name": "job",
                "endpoint": {
                    "path": "/apis/batch/v1/namespaces/{namespace}/jobs/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_batch_v1_job_list_for_all_namespaces",
                "table_name": "job",
                "endpoint": {
                    "path": "/apis/batch/v1/watch/jobs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Job. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_batch_v1_namespaced_job_list",
                "table_name": "job",
                "endpoint": {
                    "path": "/apis/batch/v1/watch/namespaces/{namespace}/jobs",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Job. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_batch_v1_namespaced_job",
                "table_name": "job",
                "endpoint": {
                    "path": "/apis/batch/v1/watch/namespaces/{namespace}/jobs/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get service account issuer OpenID JSON Web Key Set (contains public token verification keys)
            {
                "name": "get_service_account_issuer_open_id_keyset",
                "table_name": "jwk",
                "endpoint": {
                    "path": "/openid/v1/jwks/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind LimitRange
            {
                "name": "list_core_v1_limit_range_for_all_namespaces",
                "table_name": "limitrange",
                "endpoint": {
                    "path": "/api/v1/limitranges",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind LimitRange
            {
                "name": "list_core_v1_namespaced_limit_range",
                "table_name": "limitrange",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/limitranges",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified LimitRange
            {
                "name": "read_core_v1_namespaced_limit_range",
                "table_name": "limitrange",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/limitranges/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_limit_range_list_for_all_namespaces",
                "table_name": "limitrange",
                "endpoint": {
                    "path": "/api/v1/watch/limitranges",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of LimitRange. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_limit_range_list",
                "table_name": "limitrange",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/limitranges",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind LimitRange. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_limit_range",
                "table_name": "limitrange",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/limitranges/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read log of the specified Pod
            {
                "name": "read_core_v1_namespaced_pod_log",
                "table_name": "log",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/log",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "container": "OPTIONAL_CONFIG",
                        # "follow": "OPTIONAL_CONFIG",
                        # "insecureSkipTLSVerifyBackend": "OPTIONAL_CONFIG",
                        # "limitBytes": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "previous": "OPTIONAL_CONFIG",
                        # "sinceSeconds": "OPTIONAL_CONFIG",
                        # "tailLines": "OPTIONAL_CONFIG",
                        # "timestamps": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "log_file_list_handler",
                "table_name": "log",
                "endpoint": {
                    "path": "/logs/",
                    "paginator": "auto",
                },
            },
            {
                "name": "log_file_handler",
                "table_name": "log",
                "endpoint": {
                    "path": "/logs/{logpath}",
                    "params": {
                        "logpath": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Namespace
            {
                "name": "list_core_v1_namespace",
                "table_name": "namespace",
                "endpoint": {
                    "path": "/api/v1/namespaces",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Namespace
            {
                "name": "read_core_v1_namespace",
                "table_name": "namespace",
                "endpoint": {
                    "path": "/api/v1/namespaces/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Namespace. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespace_list",
                "table_name": "namespace",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Namespace. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespace",
                "table_name": "namespace",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_networking_api_group",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_networking_v1api_resources",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind IngressClass
            {
                "name": "list_networking_v1_ingress_class",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/ingressclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified IngressClass
            {
                "name": "read_networking_v1_ingress_class",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/ingressclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Ingress
            {
                "name": "list_networking_v1_ingress_for_all_namespaces",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/ingresses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Ingress
            {
                "name": "list_networking_v1_namespaced_ingress",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Ingress
            {
                "name": "read_networking_v1_namespaced_ingress",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Ingress
            {
                "name": "read_networking_v1_namespaced_ingress_status",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/namespaces/{namespace}/ingresses/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind NetworkPolicy
            {
                "name": "list_networking_v1_namespaced_network_policy",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified NetworkPolicy
            {
                "name": "read_networking_v1_namespaced_network_policy",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/namespaces/{namespace}/networkpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind NetworkPolicy
            {
                "name": "list_networking_v1_network_policy_for_all_namespaces",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/networkpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of IngressClass. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_ingress_class_list",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/ingressclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind IngressClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_networking_v1_ingress_class",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/ingressclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Ingress. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_ingress_list_for_all_namespaces",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/ingresses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Ingress. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_namespaced_ingress_list",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/ingresses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Ingress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_networking_v1_namespaced_ingress",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/ingresses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_namespaced_network_policy_list",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_networking_v1_namespaced_network_policy",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/namespaces/{namespace}/networkpolicies/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of NetworkPolicy. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_network_policy_list_for_all_namespaces",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1/watch/networkpolicies",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_networking_v1_alpha_1api_resources",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind IPAddress
            {
                "name": "list_networking_v1_alpha_1ip_address",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/ipaddresses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified IPAddress
            {
                "name": "read_networking_v1_alpha_1ip_address",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/ipaddresses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ServiceCIDR
            {
                "name": "list_networking_v1_alpha_1_service_cidr",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/servicecidrs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ServiceCIDR
            {
                "name": "read_networking_v1_alpha_1_service_cidr",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/servicecidrs/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ServiceCIDR
            {
                "name": "read_networking_v1_alpha_1_service_cidr_status",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/servicecidrs/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of IPAddress. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_alpha_1ip_address_list",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/watch/ipaddresses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind IPAddress. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_networking_v1_alpha_1ip_address",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/watch/ipaddresses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_networking_v1_alpha_1_service_cidr_list",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/watch/servicecidrs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ServiceCIDR. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_networking_v1_alpha_1_service_cidr",
                "table_name": "networking",
                "endpoint": {
                    "path": "/apis/networking.k8s.io/v1alpha1/watch/servicecidrs/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Node
            {
                "name": "list_core_v1_node",
                "table_name": "node",
                "endpoint": {
                    "path": "/api/v1/nodes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Node
            {
                "name": "read_core_v1_node",
                "table_name": "node",
                "endpoint": {
                    "path": "/api/v1/nodes/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Node. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_node_list",
                "table_name": "node",
                "endpoint": {
                    "path": "/api/v1/watch/nodes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Node. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_node",
                "table_name": "node",
                "endpoint": {
                    "path": "/api/v1/watch/nodes/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_node_api_group",
                "table_name": "node",
                "endpoint": {
                    "path": "/apis/node.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_node_v1api_resources",
                "table_name": "node",
                "endpoint": {
                    "path": "/apis/node.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind RuntimeClass
            {
                "name": "list_node_v1_runtime_class",
                "table_name": "node",
                "endpoint": {
                    "path": "/apis/node.k8s.io/v1/runtimeclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified RuntimeClass
            {
                "name": "read_node_v1_runtime_class",
                "table_name": "node",
                "endpoint": {
                    "path": "/apis/node.k8s.io/v1/runtimeclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_node_v1_runtime_class_list",
                "table_name": "node",
                "endpoint": {
                    "path": "/apis/node.k8s.io/v1/watch/runtimeclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind RuntimeClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_node_v1_runtime_class",
                "table_name": "node",
                "endpoint": {
                    "path": "/apis/node.k8s.io/v1/watch/runtimeclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PersistentVolume
            {
                "name": "list_core_v1_persistent_volume",
                "table_name": "persistentvolume",
                "endpoint": {
                    "path": "/api/v1/persistentvolumes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PersistentVolume
            {
                "name": "read_core_v1_persistent_volume",
                "table_name": "persistentvolume",
                "endpoint": {
                    "path": "/api/v1/persistentvolumes/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_persistent_volume_list",
                "table_name": "persistentvolume",
                "endpoint": {
                    "path": "/api/v1/watch/persistentvolumes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PersistentVolume. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_persistent_volume",
                "table_name": "persistentvolume",
                "endpoint": {
                    "path": "/api/v1/watch/persistentvolumes/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PersistentVolumeClaim
            {
                "name": "list_core_v1_namespaced_persistent_volume_claim",
                "table_name": "persistentvolumeclaim",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/persistentvolumeclaims",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PersistentVolumeClaim
            {
                "name": "read_core_v1_namespaced_persistent_volume_claim",
                "table_name": "persistentvolumeclaim",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PersistentVolumeClaim
            {
                "name": "list_core_v1_persistent_volume_claim_for_all_namespaces",
                "table_name": "persistentvolumeclaim",
                "endpoint": {
                    "path": "/api/v1/persistentvolumeclaims",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_persistent_volume_claim_list",
                "table_name": "persistentvolumeclaim",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_persistent_volume_claim",
                "table_name": "persistentvolumeclaim",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/persistentvolumeclaims/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PersistentVolumeClaim. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_persistent_volume_claim_list_for_all_namespaces",
                "table_name": "persistentvolumeclaim",
                "endpoint": {
                    "path": "/api/v1/watch/persistentvolumeclaims",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Pod
            {
                "name": "list_core_v1_namespaced_pod",
                "table_name": "pod",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Pod
            {
                "name": "read_core_v1_namespaced_pod",
                "table_name": "pod",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Pod
            {
                "name": "list_core_v1_pod_for_all_namespaces",
                "table_name": "pod",
                "endpoint": {
                    "path": "/api/v1/pods",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_pod_list",
                "table_name": "pod",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/pods",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Pod. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_pod",
                "table_name": "pod",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/pods/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Pod. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_pod_list_for_all_namespaces",
                "table_name": "pod",
                "endpoint": {
                    "path": "/api/v1/watch/pods",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PodDisruptionBudget
            {
                "name": "list_policy_v1_namespaced_pod_disruption_budget",
                "table_name": "poddisruptionbudget",
                "endpoint": {
                    "path": "/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PodDisruptionBudget
            {
                "name": "read_policy_v1_namespaced_pod_disruption_budget",
                "table_name": "poddisruptionbudget",
                "endpoint": {
                    "path": "/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PodDisruptionBudget
            {
                "name": "list_policy_v1_pod_disruption_budget_for_all_namespaces",
                "table_name": "poddisruptionbudget",
                "endpoint": {
                    "path": "/apis/policy/v1/poddisruptionbudgets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_policy_v1_namespaced_pod_disruption_budget_list",
                "table_name": "poddisruptionbudget",
                "endpoint": {
                    "path": "/apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_policy_v1_namespaced_pod_disruption_budget",
                "table_name": "poddisruptionbudget",
                "endpoint": {
                    "path": "/apis/policy/v1/watch/namespaces/{namespace}/poddisruptionbudgets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PodDisruptionBudget. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_policy_v1_pod_disruption_budget_list_for_all_namespaces",
                "table_name": "poddisruptionbudget",
                "endpoint": {
                    "path": "/apis/policy/v1/watch/poddisruptionbudgets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PodTemplate
            {
                "name": "list_core_v1_namespaced_pod_template",
                "table_name": "podtemplate",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/podtemplates",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PodTemplate
            {
                "name": "read_core_v1_namespaced_pod_template",
                "table_name": "podtemplate",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/podtemplates/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PodTemplate
            {
                "name": "list_core_v1_pod_template_for_all_namespaces",
                "table_name": "podtemplate",
                "endpoint": {
                    "path": "/api/v1/podtemplates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_pod_template_list",
                "table_name": "podtemplate",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/podtemplates",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PodTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_pod_template",
                "table_name": "podtemplate",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/podtemplates/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PodTemplate. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_pod_template_list_for_all_namespaces",
                "table_name": "podtemplate",
                "endpoint": {
                    "path": "/api/v1/watch/podtemplates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_policy_api_group",
                "table_name": "policy",
                "endpoint": {
                    "path": "/apis/policy/",
                    "paginator": "auto",
                },
            },
            # connect GET requests to portforward of Pod
            {
                "name": "connect_core_v1_get_namespaced_pod_portforward",
                "table_name": "portforward",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/portforward",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ports": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to proxy of Pod
            {
                "name": "connect_core_v1_get_namespaced_pod_proxy",
                "table_name": "proxy",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/proxy",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to proxy of Pod
            {
                "name": "connect_core_v1_get_namespaced_pod_proxy_with_path",
                "table_name": "proxy",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/proxy/{path}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to proxy of Service
            {
                "name": "connect_core_v1_get_namespaced_service_proxy",
                "table_name": "proxy",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/services/{name}/proxy",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to proxy of Service
            {
                "name": "connect_core_v1_get_namespaced_service_proxy_with_path",
                "table_name": "proxy",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to proxy of Node
            {
                "name": "connect_core_v1_get_node_proxy",
                "table_name": "proxy",
                "endpoint": {
                    "path": "/api/v1/nodes/{name}/proxy",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # connect GET requests to proxy of Node
            {
                "name": "connect_core_v1_get_node_proxy_with_path",
                "table_name": "proxy",
                "endpoint": {
                    "path": "/api/v1/nodes/{name}/proxy/{path}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "path": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_rbac_authorization_api_group",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_rbac_authorization_v1api_resources",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ClusterRoleBinding
            {
                "name": "list_rbac_authorization_v1_cluster_role_binding",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/clusterrolebindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ClusterRoleBinding
            {
                "name": "read_rbac_authorization_v1_cluster_role_binding",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/clusterrolebindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ClusterRole
            {
                "name": "list_rbac_authorization_v1_cluster_role",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/clusterroles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ClusterRole
            {
                "name": "read_rbac_authorization_v1_cluster_role",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/clusterroles/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind RoleBinding
            {
                "name": "list_rbac_authorization_v1_namespaced_role_binding",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified RoleBinding
            {
                "name": "read_rbac_authorization_v1_namespaced_role_binding",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/rolebindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Role
            {
                "name": "list_rbac_authorization_v1_namespaced_role",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Role
            {
                "name": "read_rbac_authorization_v1_namespaced_role",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/namespaces/{namespace}/roles/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind RoleBinding
            {
                "name": "list_rbac_authorization_v1_role_binding_for_all_namespaces",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/rolebindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Role
            {
                "name": "list_rbac_authorization_v1_role_for_all_namespaces",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/roles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_rbac_authorization_v1_cluster_role_binding_list",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ClusterRoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_rbac_authorization_v1_cluster_role_binding",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/clusterrolebindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ClusterRole. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_rbac_authorization_v1_cluster_role_list",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/clusterroles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ClusterRole. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_rbac_authorization_v1_cluster_role",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/clusterroles/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_rbac_authorization_v1_namespaced_role_binding_list",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind RoleBinding. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_rbac_authorization_v1_namespaced_role_binding",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/rolebindings/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_rbac_authorization_v1_namespaced_role_list",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Role. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_rbac_authorization_v1_namespaced_role",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/namespaces/{namespace}/roles/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of RoleBinding. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_rbac_authorization_v1_role_binding_list_for_all_namespaces",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/rolebindings",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Role. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_rbac_authorization_v1_role_list_for_all_namespaces",
                "table_name": "rbac",
                "endpoint": {
                    "path": "/apis/rbac.authorization.k8s.io/v1/watch/roles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ReplicaSet
            {
                "name": "list_apps_v1_namespaced_replica_set",
                "table_name": "replicaset",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/replicasets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ReplicaSet
            {
                "name": "read_apps_v1_namespaced_replica_set",
                "table_name": "replicaset",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/replicasets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ReplicaSet
            {
                "name": "list_apps_v1_replica_set_for_all_namespaces",
                "table_name": "replicaset",
                "endpoint": {
                    "path": "/apis/apps/v1/replicasets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_namespaced_replica_set_list",
                "table_name": "replicaset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/replicasets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apps_v1_namespaced_replica_set",
                "table_name": "replicaset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/replicasets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ReplicaSet. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_replica_set_list_for_all_namespaces",
                "table_name": "replicaset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/replicasets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ReplicationController
            {
                "name": "list_core_v1_namespaced_replication_controller",
                "table_name": "replicationcontroller",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/replicationcontrollers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ReplicationController
            {
                "name": "read_core_v1_namespaced_replication_controller",
                "table_name": "replicationcontroller",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/replicationcontrollers/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ReplicationController
            {
                "name": "list_core_v1_replication_controller_for_all_namespaces",
                "table_name": "replicationcontroller",
                "endpoint": {
                    "path": "/api/v1/replicationcontrollers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_replication_controller_list",
                "table_name": "replicationcontroller",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/replicationcontrollers",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ReplicationController. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_replication_controller",
                "table_name": "replicationcontroller",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/replicationcontrollers/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ReplicationController. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_replication_controller_list_for_all_namespaces",
                "table_name": "replicationcontroller",
                "endpoint": {
                    "path": "/api/v1/watch/replicationcontrollers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_resource_api_group",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_resource_v1_alpha_2api_resources",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PodSchedulingContext
            {
                "name": "list_resource_v1_alpha_2_namespaced_pod_scheduling_context",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/podschedulingcontexts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PodSchedulingContext
            {
                "name": "read_resource_v1_alpha_2_namespaced_pod_scheduling_context",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/podschedulingcontexts/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified PodSchedulingContext
            {
                "name": "read_resource_v1_alpha_2_namespaced_pod_scheduling_context_status",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/podschedulingcontexts/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClaimParameters
            {
                "name": "list_resource_v1_alpha_2_namespaced_resource_claim_parameters",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceClaimParameters
            {
                "name": "read_resource_v1_alpha_2_namespaced_resource_claim_parameters",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimparameters/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClaim
            {
                "name": "list_resource_v1_alpha_2_namespaced_resource_claim",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaims",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceClaim
            {
                "name": "read_resource_v1_alpha_2_namespaced_resource_claim",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaims/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ResourceClaim
            {
                "name": "read_resource_v1_alpha_2_namespaced_resource_claim_status",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaims/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClaimTemplate
            {
                "name": "list_resource_v1_alpha_2_namespaced_resource_claim_template",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimtemplates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceClaimTemplate
            {
                "name": "read_resource_v1_alpha_2_namespaced_resource_claim_template",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclaimtemplates/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClassParameters
            {
                "name": "list_resource_v1_alpha_2_namespaced_resource_class_parameters",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclassparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceClassParameters
            {
                "name": "read_resource_v1_alpha_2_namespaced_resource_class_parameters",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/namespaces/{namespace}/resourceclassparameters/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PodSchedulingContext
            {
                "name": "list_resource_v1_alpha_2_pod_scheduling_context_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/podschedulingcontexts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClaimParameters
            {
                "name": "list_resource_v1_alpha_2_resource_claim_parameters_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceclaimparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClaim
            {
                "name": "list_resource_v1_alpha_2_resource_claim_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceclaims",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClaimTemplate
            {
                "name": "list_resource_v1_alpha_2_resource_claim_template_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceclaimtemplates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClass
            {
                "name": "list_resource_v1_alpha_2_resource_class",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceClass
            {
                "name": "read_resource_v1_alpha_2_resource_class",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceClassParameters
            {
                "name": "list_resource_v1_alpha_2_resource_class_parameters_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceclassparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceSlice
            {
                "name": "list_resource_v1_alpha_2_resource_slice",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceslices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceSlice
            {
                "name": "read_resource_v1_alpha_2_resource_slice",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/resourceslices/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PodSchedulingContext. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_pod_scheduling_context_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/podschedulingcontexts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PodSchedulingContext. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_pod_scheduling_context",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/podschedulingcontexts/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClaimParameters. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_claim_parameters_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceClaimParameters. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_claim_parameters",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimparameters/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_claim_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaims",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_claim",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaims/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_claim_template_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimtemplates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_claim_template",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclaimtemplates/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClassParameters. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_class_parameters_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclassparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceClassParameters. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_namespaced_resource_class_parameters",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/namespaces/{namespace}/resourceclassparameters/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PodSchedulingContext. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_pod_scheduling_context_list_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/podschedulingcontexts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClaimParameters. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_resource_claim_parameters_list_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceclaimparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClaim. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_resource_claim_list_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceclaims",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClaimTemplate. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_resource_claim_template_list_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceclaimtemplates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClass. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_resource_class_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_resource_class",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceClassParameters. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_resource_class_parameters_list_for_all_namespaces",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceclassparameters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_resource_v1_alpha_2_resource_slice_list",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceslices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceSlice. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_resource_v1_alpha_2_resource_slice",
                "table_name": "resource",
                "endpoint": {
                    "path": "/apis/resource.k8s.io/v1alpha2/watch/resourceslices/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceQuota
            {
                "name": "list_core_v1_namespaced_resource_quota",
                "table_name": "resourcequota",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/resourcequotas",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ResourceQuota
            {
                "name": "read_core_v1_namespaced_resource_quota",
                "table_name": "resourcequota",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/resourcequotas/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ResourceQuota
            {
                "name": "list_core_v1_resource_quota_for_all_namespaces",
                "table_name": "resourcequota",
                "endpoint": {
                    "path": "/api/v1/resourcequotas",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_resource_quota_list",
                "table_name": "resourcequota",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/resourcequotas",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_resource_quota",
                "table_name": "resourcequota",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/resourcequotas/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ResourceQuota. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_resource_quota_list_for_all_namespaces",
                "table_name": "resourcequota",
                "endpoint": {
                    "path": "/api/v1/watch/resourcequotas",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read scale of the specified ReplicationController
            {
                "name": "read_core_v1_namespaced_replication_controller_scale",
                "table_name": "scale",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read scale of the specified Deployment
            {
                "name": "read_apps_v1_namespaced_deployment_scale",
                "table_name": "scale",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/deployments/{name}/scale",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read scale of the specified ReplicaSet
            {
                "name": "read_apps_v1_namespaced_replica_set_scale",
                "table_name": "scale",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/replicasets/{name}/scale",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read scale of the specified StatefulSet
            {
                "name": "read_apps_v1_namespaced_stateful_set_scale",
                "table_name": "scale",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/scale",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_scheduling_api_group",
                "table_name": "scheduling",
                "endpoint": {
                    "path": "/apis/scheduling.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_scheduling_v1api_resources",
                "table_name": "scheduling",
                "endpoint": {
                    "path": "/apis/scheduling.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind PriorityClass
            {
                "name": "list_scheduling_v1_priority_class",
                "table_name": "scheduling",
                "endpoint": {
                    "path": "/apis/scheduling.k8s.io/v1/priorityclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified PriorityClass
            {
                "name": "read_scheduling_v1_priority_class",
                "table_name": "scheduling",
                "endpoint": {
                    "path": "/apis/scheduling.k8s.io/v1/priorityclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of PriorityClass. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_scheduling_v1_priority_class_list",
                "table_name": "scheduling",
                "endpoint": {
                    "path": "/apis/scheduling.k8s.io/v1/watch/priorityclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind PriorityClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_scheduling_v1_priority_class",
                "table_name": "scheduling",
                "endpoint": {
                    "path": "/apis/scheduling.k8s.io/v1/watch/priorityclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Secret
            {
                "name": "list_core_v1_namespaced_secret",
                "table_name": "secret",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/secrets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Secret
            {
                "name": "read_core_v1_namespaced_secret",
                "table_name": "secret",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/secrets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Secret
            {
                "name": "list_core_v1_secret_for_all_namespaces",
                "table_name": "secret",
                "endpoint": {
                    "path": "/api/v1/secrets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_secret_list",
                "table_name": "secret",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/secrets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Secret. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_secret",
                "table_name": "secret",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/secrets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Secret. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_secret_list_for_all_namespaces",
                "table_name": "secret",
                "endpoint": {
                    "path": "/api/v1/watch/secrets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Service
            {
                "name": "list_core_v1_namespaced_service",
                "table_name": "service",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/services",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified Service
            {
                "name": "read_core_v1_namespaced_service",
                "table_name": "service",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/services/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind Service
            {
                "name": "list_core_v1_service_for_all_namespaces",
                "table_name": "service",
                "endpoint": {
                    "path": "/api/v1/services",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_service_list",
                "table_name": "service",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/services",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind Service. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_service",
                "table_name": "service",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/services/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of Service. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_service_list_for_all_namespaces",
                "table_name": "service",
                "endpoint": {
                    "path": "/api/v1/watch/services",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ServiceAccount
            {
                "name": "list_core_v1_namespaced_service_account",
                "table_name": "serviceaccount",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/serviceaccounts",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified ServiceAccount
            {
                "name": "read_core_v1_namespaced_service_account",
                "table_name": "serviceaccount",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/serviceaccounts/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind ServiceAccount
            {
                "name": "list_core_v1_service_account_for_all_namespaces",
                "table_name": "serviceaccount",
                "endpoint": {
                    "path": "/api/v1/serviceaccounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_namespaced_service_account_list",
                "table_name": "serviceaccount",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/serviceaccounts",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_core_v1_namespaced_service_account",
                "table_name": "serviceaccount",
                "endpoint": {
                    "path": "/api/v1/watch/namespaces/{namespace}/serviceaccounts/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of ServiceAccount. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_core_v1_service_account_list_for_all_namespaces",
                "table_name": "serviceaccount",
                "endpoint": {
                    "path": "/api/v1/watch/serviceaccounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind StatefulSet
            {
                "name": "list_apps_v1_namespaced_stateful_set",
                "table_name": "statefulset",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/statefulsets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified StatefulSet
            {
                "name": "read_apps_v1_namespaced_stateful_set",
                "table_name": "statefulset",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind StatefulSet
            {
                "name": "list_apps_v1_stateful_set_for_all_namespaces",
                "table_name": "statefulset",
                "endpoint": {
                    "path": "/apis/apps/v1/statefulsets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_namespaced_stateful_set_list",
                "table_name": "statefulset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/statefulsets",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind StatefulSet. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_apps_v1_namespaced_stateful_set",
                "table_name": "statefulset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/namespaces/{namespace}/statefulsets/{name}",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of StatefulSet. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_apps_v1_stateful_set_list_for_all_namespaces",
                "table_name": "statefulset",
                "endpoint": {
                    "path": "/apis/apps/v1/watch/statefulsets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified PersistentVolumeClaim
            {
                "name": "read_core_v1_namespaced_persistent_volume_claim_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/persistentvolumeclaims/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Pod
            {
                "name": "read_core_v1_namespaced_pod_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/pods/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ReplicationController
            {
                "name": "read_core_v1_namespaced_replication_controller_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ResourceQuota
            {
                "name": "read_core_v1_namespaced_resource_quota_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/resourcequotas/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Service
            {
                "name": "read_core_v1_namespaced_service_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/namespaces/{namespace}/services/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Namespace
            {
                "name": "read_core_v1_namespace_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/namespaces/{name}/status",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Node
            {
                "name": "read_core_v1_node_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/nodes/{name}/status",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified PersistentVolume
            {
                "name": "read_core_v1_persistent_volume_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/api/v1/persistentvolumes/{name}/status",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified DaemonSet
            {
                "name": "read_apps_v1_namespaced_daemon_set_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/daemonsets/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Deployment
            {
                "name": "read_apps_v1_namespaced_deployment_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/deployments/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified ReplicaSet
            {
                "name": "read_apps_v1_namespaced_replica_set_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/replicasets/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified StatefulSet
            {
                "name": "read_apps_v1_namespaced_stateful_set_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/apps/v1/namespaces/{namespace}/statefulsets/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified HorizontalPodAutoscaler
            {
                "name": "read_autoscaling_v1_namespaced_horizontal_pod_autoscaler_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/namespaces/{namespace}/horizontalpodautoscalers/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified HorizontalPodAutoscaler
            {
                "name": "read_autoscaling_v2_namespaced_horizontal_pod_autoscaler_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/namespaces/{namespace}/horizontalpodautoscalers/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified CronJob
            {
                "name": "read_batch_v1_namespaced_cron_job_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/batch/v1/namespaces/{namespace}/cronjobs/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified Job
            {
                "name": "read_batch_v1_namespaced_job_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/batch/v1/namespaces/{namespace}/jobs/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified PodDisruptionBudget
            {
                "name": "read_policy_v1_namespaced_pod_disruption_budget_status",
                "table_name": "statu",
                "endpoint": {
                    "path": "/apis/policy/v1/namespaces/{namespace}/poddisruptionbudgets/{name}/status",
                    "params": {
                        "namespace": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_storage_api_group",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_storage_v1api_resources",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CSIDriver
            {
                "name": "list_storage_v1csi_driver",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/csidrivers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified CSIDriver
            {
                "name": "read_storage_v1csi_driver",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/csidrivers/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CSINode
            {
                "name": "list_storage_v1csi_node",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/csinodes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified CSINode
            {
                "name": "read_storage_v1csi_node",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/csinodes/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CSIStorageCapacity
            {
                "name": "list_storage_v1csi_storage_capacity_for_all_namespaces",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/csistoragecapacities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind CSIStorageCapacity
            {
                "name": "list_storage_v1_namespaced_csi_storage_capacity",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified CSIStorageCapacity
            {
                "name": "read_storage_v1_namespaced_csi_storage_capacity",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/namespaces/{namespace}/csistoragecapacities/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind StorageClass
            {
                "name": "list_storage_v1_storage_class",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/storageclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified StorageClass
            {
                "name": "read_storage_v1_storage_class",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/storageclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind VolumeAttachment
            {
                "name": "list_storage_v1_volume_attachment",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/volumeattachments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified VolumeAttachment
            {
                "name": "read_storage_v1_volume_attachment",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/volumeattachments/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified VolumeAttachment
            {
                "name": "read_storage_v1_volume_attachment_status",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/volumeattachments/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CSIDriver. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1csi_driver_list",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/csidrivers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind CSIDriver. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storage_v1csi_driver",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/csidrivers/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CSINode. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1csi_node_list",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/csinodes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind CSINode. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storage_v1csi_node",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/csinodes/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1csi_storage_capacity_list_for_all_namespaces",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/csistoragecapacities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1_namespaced_csi_storage_capacity_list",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind CSIStorageCapacity. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storage_v1_namespaced_csi_storage_capacity",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/namespaces/{namespace}/csistoragecapacities/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of StorageClass. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1_storage_class_list",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/storageclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind StorageClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storage_v1_storage_class",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/storageclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1_volume_attachment_list",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/volumeattachments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind VolumeAttachment. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storage_v1_volume_attachment",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1/watch/volumeattachments/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_storage_v1_alpha_1api_resources",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind VolumeAttributesClass
            {
                "name": "list_storage_v1_alpha_1_volume_attributes_class",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1alpha1/volumeattributesclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified VolumeAttributesClass
            {
                "name": "read_storage_v1_alpha_1_volume_attributes_class",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1alpha1/volumeattributesclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storage_v1_alpha_1_volume_attributes_class_list",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1alpha1/watch/volumeattributesclasses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind VolumeAttributesClass. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storage_v1_alpha_1_volume_attributes_class",
                "table_name": "storage",
                "endpoint": {
                    "path": "/apis/storage.k8s.io/v1alpha1/watch/volumeattributesclasses/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get information of a group
            {
                "name": "get_storagemigration_api_group",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_storagemigration_v1_alpha_1api_resources",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/v1alpha1/",
                    "paginator": "auto",
                },
            },
            # list or watch objects of kind StorageVersionMigration
            {
                "name": "list_storagemigration_v1_alpha_1_storage_version_migration",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read the specified StorageVersionMigration
            {
                "name": "read_storagemigration_v1_alpha_1_storage_version_migration",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # read status of the specified StorageVersionMigration
            {
                "name": "read_storagemigration_v1_alpha_1_storage_version_migration_status",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/v1alpha1/storageversionmigrations/{name}/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pretty": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch individual changes to a list of StorageVersionMigration. deprecated: use the 'watch' parameter with a list operation instead.
            {
                "name": "watch_storagemigration_v1_alpha_1_storage_version_migration_list",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/v1alpha1/watch/storageversionmigrations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # watch changes to an object of kind StorageVersionMigration. deprecated: use the 'watch' parameter with a list operation instead, filtered to a single item with the 'fieldSelector' parameter.
            {
                "name": "watch_storagemigration_v1_alpha_1_storage_version_migration",
                "table_name": "storagemigration",
                "endpoint": {
                    "path": "/apis/storagemigration.k8s.io/v1alpha1/watch/storageversionmigrations/{name}",
                    "params": {
                        # the parameters below can optionally be configured
                        # "allowWatchBookmarks": "OPTIONAL_CONFIG",
                        # "continue": "OPTIONAL_CONFIG",
                        # "fieldSelector": "OPTIONAL_CONFIG",
                        # "labelSelector": "OPTIONAL_CONFIG",
                        # "limit": "OPTIONAL_CONFIG",
                        # "pretty": "OPTIONAL_CONFIG",
                        # "resourceVersion": "OPTIONAL_CONFIG",
                        # "resourceVersionMatch": "OPTIONAL_CONFIG",
                        # "sendInitialEvents": "OPTIONAL_CONFIG",
                        # "timeoutSeconds": "OPTIONAL_CONFIG",
                        # "watch": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_core_v1api_resources",
                "table_name": "v1",
                "endpoint": {
                    "path": "/api/v1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_apps_v1api_resources",
                "table_name": "v1",
                "endpoint": {
                    "path": "/apis/apps/v1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_autoscaling_v1api_resources",
                "table_name": "v1",
                "endpoint": {
                    "path": "/apis/autoscaling/v1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_batch_v1api_resources",
                "table_name": "v1",
                "endpoint": {
                    "path": "/apis/batch/v1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_policy_v1api_resources",
                "table_name": "v1",
                "endpoint": {
                    "path": "/apis/policy/v1/",
                    "paginator": "auto",
                },
            },
            # get available resources
            {
                "name": "get_autoscaling_v2api_resources",
                "table_name": "v2",
                "endpoint": {
                    "path": "/apis/autoscaling/v2/",
                    "paginator": "auto",
                },
            },
            # get the code version
            {
                "name": "get_code_version",
                "table_name": "version",
                "endpoint": {
                    "path": "/version/",
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
