from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="digital_ocean_source", max_table_nesting=2)
def digital_ocean_source(
    token: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "bearer",
                "token": token,
            },
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "meta.total",
            },
        },
        "resources": [
            # To list all available 1-Click applications, send a GET request to `/v2/1-clicks`. The `type` may be provided as query paramater in order to restrict results to a certain type of 1-Click, for example: `/v2/1-clicks?type=droplet`. Current supported types are `kubernetes` and `droplet`.  The response will be a JSON object with a key called `1_clicks`. This will be set to an array of 1-Click application data, each of which will contain the the slug and type for the 1-Click.
            {
                "name": "one_clicks_list",
                "table_name": "1_click",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/1-clicks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To show information about the current user account, send a GET request to `/v2/account`.
            {
                "name": "account_get",
                "table_name": "account",
                "endpoint": {
                    "data_selector": "account",
                    "path": "/v2/account",
                },
            },
            # This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default.
            {
                "name": "actions_list",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions",
                    "path": "/v2/actions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`.
            {
                "name": "actions_get",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "action",
                    "path": "/v2/actions/{action_id}",
                    "params": {
                        "action_id": {
                            "type": "resolve",
                            "resource": "actions_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To retrieve a list of all actions that have been executed for a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/actions`.  The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with `action` objects containing the standard `action` attributes.
            {
                "name": "droplet_actions_list",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions",
                    "path": "/v2/droplets/{droplet_id}/actions",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve a Droplet action, send a GET request to `/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.  The response will be a JSON object with a key called `action`. The value will be a Droplet action object.
            {
                "name": "droplet_actions_get",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "action",
                    "path": "/v2/droplets/{droplet_id}/actions/{action_id}",
                    "params": {
                        "action_id": {
                            "type": "resolve",
                            "resource": "droplet_actions_list",
                            "field": "id",
                        },
                        "droplet_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`.
            {
                "name": "floating_i_ps_action_list",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions",
                    "path": "/v2/floating_ips/{floating_ip}/actions",
                    "params": {
                        "floating_ip": {
                            "type": "resolve",
                            "resource": "floating_i_ps_list",
                            "field": "project_id",
                        },
                    },
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "links.pages.next",
                    },
                },
            },
            # To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`.
            {
                "name": "floating_i_ps_action_get",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "action",
                    "path": "/v2/floating_ips/{floating_ip}/actions/{action_id}",
                    "params": {
                        "action_id": {
                            "type": "resolve",
                            "resource": "floating_i_ps_action_list",
                            "field": "id",
                        },
                        "floating_ip": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve all actions that have been executed on an image, send a GET request to `/v2/images/$IMAGE_ID/actions`.
            {
                "name": "image_actions_list",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions",
                    "path": "/v2/images/{image_id}/actions",
                    "params": {
                        "image_id": {
                            "type": "resolve",
                            "resource": "images_list",
                            "field": "id",
                        },
                    },
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "links.pages.next",
                    },
                },
            },
            # To retrieve the status of an image action, send a GET request to `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`.
            {
                "name": "image_actions_get",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/images/{image_id}/actions/{action_id}",
                    "params": {
                        "action_id": {
                            "type": "resolve",
                            "resource": "image_actions_list",
                            "field": "id",
                        },
                        "image_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve all actions that have been executed on a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions`.
            {
                "name": "reserved_i_ps_actions_list",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions",
                    "path": "/v2/reserved_ips/{reserved_ip}/actions",
                    "params": {
                        "reserved_ip": {
                            "type": "resolve",
                            "resource": "reserved_i_ps_list",
                            "field": "project_id",
                        },
                    },
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "links.pages.next",
                    },
                },
            },
            # To retrieve the status of a reserved IP action, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions/$ACTION_ID`.
            {
                "name": "reserved_i_ps_actions_get",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "action",
                    "path": "/v2/reserved_ips/{reserved_ip}/actions/{action_id}",
                    "params": {
                        "action_id": {
                            "type": "resolve",
                            "resource": "reserved_i_ps_actions_list",
                            "field": "id",
                        },
                        "reserved_ip": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`.
            {
                "name": "volume_actions_list",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions",
                    "path": "/v2/volumes/{volume_id}/actions",
                    "params": {
                        "volume_id": {
                            "type": "resolve",
                            "resource": "volumes_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve the status of a volume action, send a GET request to `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.
            {
                "name": "volume_actions_get",
                "table_name": "action",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "action",
                    "path": "/v2/volumes/{volume_id}/actions/{action_id}",
                    "params": {
                        "action_id": {
                            "type": "resolve",
                            "resource": "volume_actions_list",
                            "field": "id",
                        },
                        "volume_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions.
            {
                "name": "apps_list_alerts",
                "table_name": "alert",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "alerts",
                    "path": "/v2/apps/{app_id}/alerts",
                    "params": {
                        "app_id": {
                            "type": "resolve",
                            "resource": "apps_list",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`.
            {
                "name": "monitoring_list_alert_policy",
                "table_name": "alert",
                "endpoint": {
                    "data_selector": "policies",
                    "path": "/v2/monitoring/alerts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/{alert_uuid}`
            {
                "name": "monitoring_get_alert_policy",
                "table_name": "alert",
                "endpoint": {
                    "data_selector": "policy",
                    "path": "/v2/monitoring/alerts/{alert_uuid}",
                    "params": {
                        "alert_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`.
            {
                "name": "uptime_check_alerts_list",
                "table_name": "alert",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "alerts",
                    "path": "/v2/uptime/checks/{check_id}/alerts",
                    "params": {
                        "check_id": {
                            "type": "resolve",
                            "resource": "uptime_checks_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`.
            {
                "name": "uptime_alert_get",
                "table_name": "alert",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "alert",
                    "path": "/v2/uptime/checks/{check_id}/alerts/{alert_id}",
                    "params": {
                        "alert_id": {
                            "type": "resolve",
                            "resource": "uptime_check_alerts_list",
                            "field": "id",
                        },
                        "check_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all deployments of an app.
            {
                "name": "apps_list_deployments",
                "table_name": "an_app_deployment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "deployments",
                    "path": "/v2/apps/{app_id}/deployments",
                    "params": {
                        "app_id": {
                            "type": "resolve",
                            "resource": "apps_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # Retrieve information about an app deployment.
            {
                "name": "apps_get_deployment",
                "table_name": "an_app_deployment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "deployment",
                    "path": "/v2/apps/{app_id}/deployments/{deployment_id}",
                    "params": {
                        "deployment_id": {
                            "type": "resolve",
                            "resource": "apps_list_deployments",
                            "field": "id",
                        },
                        "app_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app.
            {
                "name": "apps_list",
                "table_name": "app",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "apps",
                    "path": "/v2/apps",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "with_projects": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response.
            {
                "name": "apps_get",
                "table_name": "app",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "app",
                    "path": "/v2/apps/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "apps_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To list all of the available backups of a PostgreSQL or MySQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/backups`. **Note**: Backups are not supported for Redis clusters. The result will be a JSON object with a `backups key`. This will be set to an array of backup objects, each of which will contain the size of the backup and the timestamp at which it was created.
            {
                "name": "databases_list_backups",
                "table_name": "backup",
                "endpoint": {
                    "data_selector": "backups",
                    "path": "/v2/databases/{database_cluster_uuid}/backups",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve any backups associated with a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/backups`.  You will get back a JSON object that has a `backups` key. This will be set to an array of backup objects, each of which contain the standard Droplet backup attributes.
            {
                "name": "droplets_list_backups",
                "table_name": "backup",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "backups",
                    "path": "/v2/droplets/{droplet_id}/backups",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve the balances on a customer's account, send a GET request to `/v2/customers/my/balance`.
            {
                "name": "balance_get",
                "table_name": "balance",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/customers/my/balance",
                },
            },
            # To retrieve bandwidth metrics for a given Droplet, send a GET request to `/v2/monitoring/metrics/droplet/bandwidth`. Use the `interface` query parameter to specify if the results should be for the `private` or `public` interface. Use the `direction` query parameter to specify if the results should be for `inbound` or `outbound` traffic.
            {
                "name": "monitoring_get_droplet_bandwidth_metrics",
                "table_name": "bandwidth",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/bandwidth",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "interface": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "direction": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Retrieve daily bandwidth usage metrics for a single app.
            {
                "name": "apps_get_metrics_bandwidth_daily",
                "table_name": "bandwidth_daily",
                "primary_key": "app_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "app_bandwidth_usage",
                    "path": "/v2/apps/{app_id}/metrics/bandwidth_daily",
                    "params": {
                        "app_id": {
                            "type": "resolve",
                            "resource": "apps_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "date": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To retrieve a list of all billing history entries, send a GET request to `/v2/customers/my/billing_history`.
            {
                "name": "billing_history_list",
                "table_name": "billing_history",
                "endpoint": {
                    "data_selector": "billing_history",
                    "path": "/v2/customers/my/billing_history",
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "links.pages.next",
                    },
                },
            },
            # To retrieve the public certificate used to secure the connection to the database cluster send a GET request to `/v2/databases/$DATABASE_ID/ca`.  The response will be a JSON object with a `ca` key. This will be set to an object containing the base64 encoding of the public key certificate.
            {
                "name": "databases_get_ca",
                "table_name": "ca",
                "endpoint": {
                    "data_selector": "ca",
                    "path": "/v2/databases/{database_cluster_uuid}/ca",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the certificates available on your account, send a GET request to `/v2/certificates`.
            {
                "name": "certificates_list",
                "table_name": "certificate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "certificates",
                    "path": "/v2/certificates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing certificate, send a GET request to `/v2/certificates/$CERTIFICATE_ID`.
            {
                "name": "certificates_get",
                "table_name": "certificate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "certificate",
                    "path": "/v2/certificates/{certificate_id}",
                    "params": {
                        "certificate_id": {
                            "type": "resolve",
                            "resource": "certificates_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`.
            {
                "name": "uptime_checks_list",
                "table_name": "check",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "checks",
                    "path": "/v2/uptime/checks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`.
            {
                "name": "uptime_check_get",
                "table_name": "check",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "check",
                    "path": "/v2/uptime/checks/{check_id}",
                    "params": {
                        "check_id": {
                            "type": "resolve",
                            "resource": "uptime_checks_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the Kubernetes clusters on your account, send a GET request to `/v2/kubernetes/clusters`.
            {
                "name": "kubernetes_list_clusters",
                "table_name": "cluster",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kubernetes_clusters",
                    "path": "/v2/kubernetes/clusters",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`.
            {
                "name": "kubernetes_get_cluster",
                "table_name": "cluster",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kubernetes_cluster",
                    "path": "/v2/kubernetes/clusters/{cluster_id}",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                    },
                },
            },
            # To request clusterlint diagnostics for your cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. If the `run_id` query parameter is provided, then the diagnostics for the specific run is fetched. By default, the latest results are shown.  To find out how to address clusterlint feedback, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md).
            {
                "name": "kubernetes_get_cluster_lint_results",
                "table_name": "clusterlint",
                "endpoint": {
                    "data_selector": "diagnostics",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/clusterlint",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "run_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Shows configuration parameters for an existing database cluster by sending a GET request to `/v2/databases/$DATABASE_ID/config`. The response is a JSON object with a `config` key, which is set to an object containing any database configuration parameters.
            {
                "name": "databases_get_config",
                "table_name": "config",
                "endpoint": {
                    "data_selector": "config.pgbouncer.ignore_startup_parameters",
                    "path": "/v2/databases/{database_cluster_uuid}/config",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve CPU metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/cpu`.
            {
                "name": "monitoring_get_droplet_cpu_metrics",
                "table_name": "cpu",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/cpu",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # This endpoint returns a JSON object . It can be used to programmatically construct Kubernetes clients which cannot parse kubeconfig files.  The resulting JSON object contains token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)".  To retrieve credentials for accessing a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials`.  Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication.
            {
                "name": "kubernetes_get_credentials",
                "table_name": "credential",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/credentials",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expiry_seconds": "0",
                    },
                },
            },
            # To retrieve a CSV for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/csv`.
            {
                "name": "invoices_get_csv_by_uuid",
                "table_name": "csv",
                "endpoint": {
                    "path": "/v2/customers/my/invoices/{invoice_uuid}/csv",
                    "params": {
                        "invoice_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`. The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster: The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster.
            {
                "name": "databases_list_clusters",
                "table_name": "databasis",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases",
                    "params": {
                        # the parameters below can optionally be configured
                        # "tag_name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID`. The response will be a JSON object with a database key. This will be set to an object containing the standard database cluster attributes. The embedded connection and private_connection objects will contain the information needed to access the database cluster. The embedded maintenance_window object will contain information about any scheduled maintenance for the database cluster.
            {
                "name": "databases_get_cluster",
                "table_name": "databasis",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "database",
                    "path": "/v2/databases/{database_cluster_uuid}",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the databases in a clusters, send a GET request to `/v2/databases/$DATABASE_ID/dbs`.  The result will be a JSON object with a `dbs` key. This will be set to an array of database objects, each of which will contain the standard database attributes.  Note: Database management is not supported for Redis clusters.
            {
                "name": "databases_list",
                "table_name": "db",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/dbs",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.  Note: Database management is not supported for Redis clusters.  The response will be a JSON object with a `db` key. This will be set to an object containing the standard database attributes.
            {
                "name": "databases_get",
                "table_name": "db",
                "endpoint": {
                    "data_selector": "db",
                    "path": "/v2/databases/{database_cluster_uuid}/dbs/{database_name}",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "database_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To get your default project, send a GET request to `/v2/projects/default`.
            {
                "name": "projects_get_default",
                "table_name": "default",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "project",
                    "path": "/v2/projects/default",
                },
            },
            # To list the associated billable resources that can be destroyed along with a Droplet, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint.  The response will be a JSON object containing `snapshots`, `volumes`, and `volume_snapshots` keys. Each will be set to an array of objects containing information about the associated resources.
            {
                "name": "droplets_list_associated_resources",
                "table_name": "destroy_with_associated_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "floating_ips",
                    "path": "/v2/droplets/{droplet_id}/destroy_with_associated_resources",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To list the associated billable resources that can be destroyed along with a cluster, send a GET request to the `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources` endpoint.
            {
                "name": "kubernetes_list_associated_resources",
                "table_name": "destroy_with_associated_resource",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "load_balancers",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all manifests in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/digests`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list manifests for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/digests`.
            {
                "name": "registry_list_repository_manifests",
                "table_name": "digest",
                "endpoint": {
                    "data_selector": "manifests",
                    "path": "/v2/registry/{registry_name}/{repository_name}/digests",
                    "params": {
                        "registry_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repository_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # In order to access your container registry with the Docker client or from a Kubernetes cluster, you will need to configure authentication. The necessary JSON configuration can be retrieved by sending a GET request to `/v2/registry/docker-credentials`.  The response will be in the format of a Docker `config.json` file. To use the config in your Kubernetes cluster, create a Secret with:      kubectl create secret generic docr \       --from-file=.dockerconfigjson=config.json \       --type=kubernetes.io/dockerconfigjson  By default, the returned credentials have read-only access to your registry and cannot be used to push images. This is appropriate for most Kubernetes clusters. To retrieve read/write credentials, suitable for use with the Docker client or in a CI system, read_write may be provided as query parameter. For example: `/v2/registry/docker-credentials?read_write=true`  By default, the returned credentials will not expire. To retrieve credentials with an expiry set, expiry_seconds may be provided as a query parameter. For example: `/v2/registry/docker-credentials?expiry_seconds=3600` will return credentials that expire after one hour.
            {
                "name": "registry_get_docker_credentials",
                "table_name": "docker_credential",
                "endpoint": {
                    "data_selector": "auths.registry.digitalocean.com",
                    "path": "/v2/registry/docker-credentials",
                    "params": {
                        # the parameters below can optionally be configured
                        # "expiry_seconds": "0",
                        # "read_write": "false",
                    },
                },
            },
            # To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`.
            {
                "name": "domains_list",
                "table_name": "domain",
                "endpoint": {
                    "data_selector": "domains",
                    "path": "/v2/domains",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`.
            {
                "name": "domains_get",
                "table_name": "domain",
                "endpoint": {
                    "data_selector": "domain",
                    "path": "/v2/domains/{domain_name}",
                    "params": {
                        "domain_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all Droplets in your account, send a GET request to `/v2/droplets`.  The response body will be a JSON object with a key of `droplets`. This will be set to an array containing objects each representing a Droplet. These will contain the standard Droplet attributes.  ### Filtering Results by Tag  It's possible to request filtered results by including certain query parameters. To only list Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/droplets?tag_name=$TAG_NAME`.
            {
                "name": "droplets_list",
                "table_name": "droplet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "droplets",
                    "path": "/v2/droplets",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "tag_name": "OPTIONAL_CONFIG",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To show information about an individual Droplet, send a GET request to `/v2/droplets/$DROPLET_ID`.
            {
                "name": "droplets_get",
                "table_name": "droplet",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "droplet",
                    "path": "/v2/droplets/{droplet_id}",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To retrieve a list of all Droplets that are co-located on the same physical hardware, send a GET request to `/v2/reports/droplet_neighbors_ids`.  The results will be returned as a JSON object with a key of `neighbor_ids`. This will be set to an array of arrays. Each array will contain a set of Droplet IDs for Droplets that share a physical server. An empty array indicates that all Droplets associated with your account are located on separate physical hardware.
            {
                "name": "droplets_list_neighbors_ids",
                "table_name": "droplet_neighbors_id",
                "endpoint": {
                    "data_selector": "neighbor_ids",
                    "path": "/v2/reports/droplet_neighbors_ids",
                },
            },
            # To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`.
            {
                "name": "cdn_list_endpoints",
                "table_name": "endpoint",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "endpoints",
                    "path": "/v2/cdn/endpoints",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing CDN endpoint, send a GET request to `/v2/cdn/endpoints/$ENDPOINT_ID`.
            {
                "name": "cdn_get_endpoint",
                "table_name": "endpoint",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "endpoint",
                    "path": "/v2/cdn/endpoints/{cdn_id}",
                    "params": {
                        "cdn_id": {
                            "type": "resolve",
                            "resource": "cdn_list_endpoints",
                            "field": "id",
                        },
                    },
                },
            },
            # To retrieve the configured eviction policy for an existing Redis cluster, send a GET request to `/v2/databases/$DATABASE_ID/eviction_policy`. The response will be a JSON object with an `eviction_policy` key. This will be set to a string representing the eviction policy.
            {
                "name": "databases_get_eviction_policy",
                "table_name": "eviction_policy",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/eviction_policy",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve filesystem free metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_free`.
            {
                "name": "monitoring_get_droplet_filesystem_free_metrics",
                "table_name": "filesystem_free",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/filesystem_free",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To retrieve filesystem size metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_size`.
            {
                "name": "monitoring_get_droplet_filesystem_size_metrics",
                "table_name": "filesystem_size",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/filesystem_size",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To list all of a database cluster's firewall rules (known as "trusted sources" in the control panel), send a GET request to `/v2/databases/$DATABASE_ID/firewall`. The result will be a JSON object with a `rules` key.
            {
                "name": "databases_list_firewall_rules",
                "table_name": "firewall",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/firewall",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve a list of all firewalls available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/firewalls`  The response will be a JSON object that has a key called `firewalls`. This will be set to an array of `firewall` objects, each of which contain the standard `firewall` attributes.
            {
                "name": "droplets_list_firewalls",
                "table_name": "firewall",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "firewalls",
                    "path": "/v2/droplets/{droplet_id}/firewalls",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`.
            {
                "name": "firewalls_list",
                "table_name": "firewall",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "firewalls",
                    "path": "/v2/firewalls",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing firewall, send a GET request to `/v2/firewalls/$FIREWALL_ID`.
            {
                "name": "firewalls_get",
                "table_name": "firewall",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "firewall",
                    "path": "/v2/firewalls/{firewall_id}",
                    "params": {
                        "firewall_id": {
                            "type": "resolve",
                            "resource": "firewalls_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`.
            {
                "name": "floating_i_ps_list",
                "table_name": "floating_ip",
                "primary_key": "project_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "floating_ips",
                    "path": "/v2/floating_ips",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`.
            {
                "name": "floating_i_ps_get",
                "table_name": "floating_ip",
                "primary_key": "project_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "floating_ip",
                    "path": "/v2/floating_ips/{floating_ip}",
                    "params": {
                        "floating_ip": {
                            "type": "resolve",
                            "resource": "floating_i_ps_list",
                            "field": "project_id",
                        },
                    },
                },
            },
            # To get information about the currently-active garbage collection for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collection`.
            {
                "name": "registry_get_garbage_collection",
                "table_name": "garbage_collection",
                "primary_key": "registry_name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "garbage_collection",
                    "path": "/v2/registry/{registry_name}/garbage-collection",
                    "params": {
                        "registry_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`.
            {
                "name": "registry_list_garbage_collections",
                "table_name": "garbage_collection",
                "primary_key": "registry_name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "garbage_collections",
                    "path": "/v2/registry/{registry_name}/garbage-collections",
                    "params": {
                        "registry_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # List all regions supported by App Platform.
            {
                "name": "apps_list_regions",
                "table_name": "geographical_information_about_an_app_origin",
                "endpoint": {
                    "data_selector": "regions",
                    "path": "/v2/apps/regions",
                },
            },
            # To list all of the images available on your account, send a GET request to /v2/images.  ## Filtering Results -----  It's possible to request filtered results by including certain query parameters.  **Image Type**  Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter.  > Important: The `type` query parameter does not directly relate to the `type` attribute.  To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`.  To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`.  **User Images**  To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`.  **Tags**  To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`.
            {
                "name": "images_list",
                "table_name": "image",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "images",
                    "path": "/v2/images",
                    "params": {
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "private": "OPTIONAL_CONFIG",
                        # "tag_name": "OPTIONAL_CONFIG",
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve information about an image, send a `GET` request to `/v2/images/$IDENTIFIER`.
            {
                "name": "images_get",
                "table_name": "image",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "image",
                    "path": "/v2/images/{image_id}",
                    "params": {
                        "image_id": {
                            "type": "resolve",
                            "resource": "images_list",
                            "field": "id",
                        },
                    },
                },
            },
            # List all instance sizes for `service`, `worker`, and `job` components.
            {
                "name": "apps_list_instance_sizes",
                "table_name": "instance_size",
                "endpoint": {
                    "data_selector": "instance_sizes",
                    "path": "/v2/apps/tiers/instance_sizes",
                },
            },
            # Retrieve information about a specific instance size for `service`, `worker`, and `job` components.
            {
                "name": "apps_get_instance_size",
                "table_name": "instance_size",
                "primary_key": "slug",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "instance_size",
                    "path": "/v2/apps/tiers/instance_sizes/{slug}",
                    "params": {
                        "slug": {
                            "type": "resolve",
                            "resource": "apps_list_instance_sizes",
                            "field": "slug",
                        },
                    },
                },
            },
            # To retrieve a list of all invoices, send a GET request to `/v2/customers/my/invoices`.
            {
                "name": "invoices_list",
                "table_name": "invoice",
                "endpoint": {
                    "data_selector": "invoices",
                    "path": "/v2/customers/my/invoices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve the invoice items for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID`.
            {
                "name": "invoices_get_by_uuid",
                "table_name": "invoice",
                "endpoint": {
                    "data_selector": "invoice_items",
                    "path": "/v2/customers/my/invoices/{invoice_uuid}",
                    "params": {
                        "invoice_uuid": {
                            "type": "resolve",
                            "resource": "invoices_list",
                            "field": "invoice_uuid",
                        },
                    },
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "links.pages.next",
                    },
                },
            },
            # To retrieve a list of all kernels available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/kernels`  The response will be a JSON object that has a key called `kernels`. This will be set to an array of `kernel` objects, each of which contain the standard `kernel` attributes.
            {
                "name": "droplets_list_kernels",
                "table_name": "kernel",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "kernels",
                    "path": "/v2/droplets/{droplet_id}/kernels",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To list all of the keys in your account, send a GET request to `/v2/account/keys`. The response will be a JSON object with a key set to `ssh_keys`. The value of this will be an array of ssh_key objects, each of which contains the standard ssh_key attributes.
            {
                "name": "ssh_keys_list",
                "table_name": "key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "ssh_keys",
                    "path": "/v2/account/keys",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`. The response will be a JSON object with the key `ssh_key` and value an ssh_key object which contains the standard ssh_key attributes.
            {
                "name": "ssh_keys_get",
                "table_name": "key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "ssh_key",
                    "path": "/v2/account/keys/{ssh_key_identifier}",
                    "params": {
                        "ssh_key_identifier": {
                            "type": "resolve",
                            "resource": "ssh_keys_list",
                            "field": "id",
                        },
                    },
                },
            },
            # This endpoint returns a kubeconfig file in YAML format. It can be used to connect to and administer the cluster using the Kubernetes command line tool, `kubectl`, or other programs supporting kubeconfig files (e.g., client libraries).  The resulting kubeconfig file uses token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)".  To retrieve a kubeconfig file for use with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig`.  Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication.
            {
                "name": "kubernetes_get_kubeconfig",
                "table_name": "kubeconfig",
                "endpoint": {
                    "path": "/v2/kubernetes/clusters/{cluster_id}/kubeconfig",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "expiry_seconds": "0",
                    },
                },
            },
            # To retrieve 1 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_1`.
            {
                "name": "monitoring_get_droplet_load_1_metrics",
                "table_name": "load_1",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/load_1",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To retrieve 15 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_15`.
            {
                "name": "monitoring_get_droplet_load_15_metrics",
                "table_name": "load_15",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/load_15",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To retrieve 5 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_5`.
            {
                "name": "monitoring_get_droplet_load_5_metrics",
                "table_name": "load_5",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/load_5",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To list all of the load balancer instances on your account, send a GET request to `/v2/load_balancers`.
            {
                "name": "load_balancers_list",
                "table_name": "load_balancer",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "load_balancers",
                    "path": "/v2/load_balancers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about a load balancer instance, send a GET request to `/v2/load_balancers/$LOAD_BALANCER_ID`.
            {
                "name": "load_balancers_get",
                "table_name": "load_balancer",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "load_balancer",
                    "path": "/v2/load_balancers/{lb_id}",
                    "params": {
                        "lb_id": {
                            "type": "resolve",
                            "resource": "load_balancers_list",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieve the logs of the active deployment if one exists. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. Note log_type=BUILD logs will return logs associated with the current active deployment (being served). To view build logs associated with in-progress build, the query must explicitly reference the deployment id.
            {
                "name": "apps_get_logs_active_deployment",
                "table_name": "log",
                "endpoint": {
                    "data_selector": "historic_urls",
                    "path": "/v2/apps/{app_id}/components/{component_name}/logs",
                    "params": {
                        "component_name": {
                            "type": "resolve",
                            "resource": "apps_list",
                            "field": "id",
                        },
                        "app_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "type": "UNSPECIFIED",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "follow": "OPTIONAL_CONFIG",
                        # "pod_connection_timeout": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve the logs of a past, in-progress, or active deployment. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.
            {
                "name": "apps_get_logs",
                "table_name": "log",
                "endpoint": {
                    "data_selector": "historic_urls",
                    "path": "/v2/apps/{app_id}/deployments/{deployment_id}/components/{component_name}/logs",
                    "params": {
                        "component_name": {
                            "type": "resolve",
                            "resource": "apps_list_deployments",
                            "field": "id",
                        },
                        "app_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "deployment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "type": "UNSPECIFIED",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "follow": "OPTIONAL_CONFIG",
                        # "pod_connection_timeout": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.
            {
                "name": "apps_get_logs_aggregate",
                "table_name": "log",
                "endpoint": {
                    "data_selector": "historic_urls",
                    "path": "/v2/apps/{app_id}/deployments/{deployment_id}/logs",
                    "params": {
                        "deployment_id": {
                            "type": "resolve",
                            "resource": "apps_list_deployments",
                            "field": "id",
                        },
                        "app_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "type": "UNSPECIFIED",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "follow": "OPTIONAL_CONFIG",
                        # "pod_connection_timeout": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve the logs of the active deployment if one exists. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. Note log_type=BUILD logs will return logs associated with the current active deployment (being served). To view build logs associated with in-progress build, the query must explicitly reference the deployment id.
            {
                "name": "apps_get_logs_active_deployment_aggregate",
                "table_name": "log",
                "endpoint": {
                    "data_selector": "historic_urls",
                    "path": "/v2/apps/{app_id}/logs",
                    "params": {
                        "app_id": {
                            "type": "resolve",
                            "resource": "apps_list",
                            "field": "id",
                        },
                        "type": "UNSPECIFIED",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "follow": "OPTIONAL_CONFIG",
                        # "pod_connection_timeout": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To list all of the resources that are members of a VPC, send a GET request to `/v2/vpcs/$VPC_ID/members`.  To only list resources of a specific type that are members of the VPC, included a `resource_type` query parameter. For example, to only list Droplets in the VPC, send a GET request to `/v2/vpcs/$VPC_ID/members?resource_type=droplet`.
            {
                "name": "vpcs_list_members",
                "table_name": "member",
                "endpoint": {
                    "data_selector": "members",
                    "path": "/v2/vpcs/{vpc_id}/members",
                    "params": {
                        "vpc_id": {
                            "type": "resolve",
                            "resource": "vpcs_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "resource_type": "OPTIONAL_CONFIG",
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve available memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_available`.
            {
                "name": "monitoring_get_droplet_memory_available_metrics",
                "table_name": "memory_available",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/memory_available",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To retrieve cached memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_cached`.
            {
                "name": "monitoring_get_droplet_memory_cached_metrics",
                "table_name": "memory_cached",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/memory_cached",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To retrieve free memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_free`.
            {
                "name": "monitoring_get_droplet_memory_free_metrics",
                "table_name": "memory_free",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/memory_free",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # To retrieve total memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_total`.
            {
                "name": "monitoring_get_droplet_memory_total_metrics",
                "table_name": "memory_total",
                "endpoint": {
                    "data_selector": "data.result",
                    "path": "/v2/monitoring/metrics/droplet/memory_total",
                    "params": {
                        "host_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "end": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Returns a list of namespaces associated with the current user. To get all namespaces, send a GET request to `/v2/functions/namespaces`.
            {
                "name": "functions_list_namespaces",
                "table_name": "namespace",
                "endpoint": {
                    "data_selector": "namespaces",
                    "path": "/v2/functions/namespaces",
                },
            },
            # Gets the namespace details for the given namespace UUID. To get namespace details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID` with no parameters.
            {
                "name": "functions_get_namespace",
                "table_name": "namespace",
                "endpoint": {
                    "data_selector": "namespace",
                    "path": "/v2/functions/namespaces/{namespace_id}",
                    "params": {
                        "namespace_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve a list of any "neighbors" (i.e. Droplets that are co-located on the same physical hardware) for a specific Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/neighbors`.  The results will be returned as a JSON object with a key of `droplets`. This will be set to an array containing objects representing any other Droplets that share the same physical hardware. An empty array indicates that the Droplet is not co-located any other Droplets associated with your account.
            {
                "name": "droplets_list_neighbors",
                "table_name": "neighbor",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "droplets",
                    "path": "/v2/droplets/{droplet_id}/neighbors",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the node pools in a Kubernetes clusters, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`.
            {
                "name": "kubernetes_list_node_pools",
                "table_name": "node_pool",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/node_pools",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                    },
                },
            },
            # To show information about a specific node pool in a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`.
            {
                "name": "kubernetes_get_node_pool",
                "table_name": "node_pool",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "node_pool",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}",
                    "params": {
                        "node_pool_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                        "cluster_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To retrieve the status of the most recent online migration, send a GET request to `/v2/databases/$DATABASE_ID/online-migration`.
            {
                "name": "databases_get_migration_status",
                "table_name": "online_migration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/online-migration",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the options available for the offered database engines, send a GET request to `/v2/databases/options`. The result will be a JSON object with an `options` key.
            {
                "name": "databases_list_options",
                "table_name": "option",
                "endpoint": {
                    "data_selector": "version_availability.mongodb",
                    "path": "/v2/databases/options",
                },
            },
            # To list the versions of Kubernetes available for use, the regions that support Kubernetes, and the available node sizes, send a GET request to `/v2/kubernetes/options`.
            {
                "name": "kubernetes_list_options",
                "table_name": "option",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/kubernetes/options",
                },
            },
            # This endpoint serves to provide additional information as to which option values are available when creating a container registry. There are multiple subscription tiers available for container registry. Each tier allows a different number of image repositories to be created in your registry, and has a different amount of storage and transfer included. There are multiple regions available for container registry and controls where your data is stored. To list the available options, send a GET request to `/v2/registry/options`.
            {
                "name": "registry_get_options",
                "table_name": "option",
                "endpoint": {
                    "data_selector": "options.available_regions",
                    "path": "/v2/registry/options",
                },
            },
            # To retrieve a PDF for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/pdf`.
            {
                "name": "invoices_get_pdf_by_uuid",
                "table_name": "pdf",
                "endpoint": {
                    "path": "/v2/customers/my/invoices/{invoice_uuid}/pdf",
                    "params": {
                        "invoice_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`. The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects.
            {
                "name": "databases_list_connection_pools",
                "table_name": "pool",
                "endpoint": {
                    "data_selector": "pools",
                    "path": "/v2/databases/{database_cluster_uuid}/pools",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To show information about an existing connection pool for a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. The response will be a JSON object with a `pool` key.
            {
                "name": "databases_get_connection_pool",
                "table_name": "pool",
                "endpoint": {
                    "data_selector": "pool",
                    "path": "/v2/databases/{database_cluster_uuid}/pools/{pool_name}",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pool_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all your projects, send a GET request to `/v2/projects`.
            {
                "name": "projects_list",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "projects",
                    "path": "/v2/projects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To get a project, send a GET request to `/v2/projects/$PROJECT_ID`.
            {
                "name": "projects_get",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "project",
                    "path": "/v2/projects/{project_id}",
                    "params": {
                        "project_id": {
                            "type": "resolve",
                            "resource": "projects_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`. The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together.
            {
                "name": "domains_list_records",
                "table_name": "record",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "domain_records",
                    "path": "/v2/domains/{domain_name}/records",
                    "params": {
                        "domain_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "name": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve a specific domain record, send a GET request to `/v2/domains/$DOMAIN_NAME/records/$RECORD_ID`.
            {
                "name": "domains_get_record",
                "table_name": "record",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "domain_record",
                    "path": "/v2/domains/{domain_name}/records/{domain_record_id}",
                    "params": {
                        "domain_record_id": {
                            "type": "resolve",
                            "resource": "domains_list_records",
                            "field": "id",
                        },
                        "domain_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all of the regions that are available, send a GET request to `/v2/regions`. The response will be a JSON object with a key called `regions`. The value of this will be an array of `region` objects, each of which will contain the standard region attributes.
            {
                "name": "regions_list",
                "table_name": "region",
                "endpoint": {
                    "data_selector": "regions",
                    "path": "/v2/regions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To get information about your container registry, send a GET request to `/v2/registry`.
            {
                "name": "registry_get",
                "table_name": "registry",
                "endpoint": {
                    "data_selector": "registry",
                    "path": "/v2/registry",
                },
            },
            # To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`.  **Note**: Read-only replicas are not supported for Redis clusters.  The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes.
            {
                "name": "databases_list_replicas",
                "table_name": "replica",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/replicas",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To show information about an existing database replica, send a GET request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`.  **Note**: Read-only replicas are not supported for Redis clusters.  The response will be a JSON object with a `replica key`. This will be set to an object containing the standard database replica attributes.
            {
                "name": "databases_get_replica",
                "table_name": "replica",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "replica",
                    "path": "/v2/databases/{database_cluster_uuid}/replicas/{replica_name}",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "replica_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositoriesV2`.
            {
                "name": "registry_list_repositories_v2",
                "table_name": "repositories_v2",
                "primary_key": "registry_name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/v2/registry/{registry_name}/repositoriesV2",
                    "params": {
                        "registry_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "page_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This endpoint has been deprecated in favor of the _List All Container Registry Repositories [V2]_ endpoint.  To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories`.
            {
                "name": "registry_list_repositories",
                "table_name": "repository",
                "primary_key": "registry_name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/v2/registry/{registry_name}/repositories",
                    "params": {
                        "registry_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To list all of the reserved IPs available on your account, send a GET request to `/v2/reserved_ips`.
            {
                "name": "reserved_i_ps_list",
                "table_name": "reserved_ip",
                "primary_key": "project_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "reserved_ips",
                    "path": "/v2/reserved_ips",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP_ADDR`.
            {
                "name": "reserved_i_ps_get",
                "table_name": "reserved_ip",
                "primary_key": "project_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "reserved_ip",
                    "path": "/v2/reserved_ips/{reserved_ip}",
                    "params": {
                        "reserved_ip": {
                            "type": "resolve",
                            "resource": "reserved_i_ps_list",
                            "field": "project_id",
                        },
                    },
                },
            },
            # To list all your resources in your default project, send a GET request to `/v2/projects/default/resources`.
            {
                "name": "projects_list_resources_default",
                "table_name": "resource",
                "endpoint": {
                    "data_selector": "resources",
                    "path": "/v2/projects/default/resources",
                    "paginator": {
                        "type": "json_response",
                        "next_url_path": "links.pages.next",
                    },
                },
            },
            # To list all your resources in a project, send a GET request to `/v2/projects/$PROJECT_ID/resources`.
            {
                "name": "projects_list_resources",
                "table_name": "resource",
                "endpoint": {
                    "data_selector": "resources",
                    "path": "/v2/projects/{project_id}/resources",
                    "params": {
                        "project_id": {
                            "type": "resolve",
                            "resource": "projects_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To list all of available Droplet sizes, send a GET request to `/v2/sizes`. The response will be a JSON object with a key called `sizes`. The value of this will be an array of `size` objects each of which contain the standard size attributes.
            {
                "name": "sizes_list",
                "table_name": "size",
                "endpoint": {
                    "data_selector": "sizes",
                    "path": "/v2/sizes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve the snapshots that have been created from a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/snapshots`.  You will get back a JSON object that has a `snapshots` key. This will be set to an array of snapshot objects, each of which contain the standard Droplet snapshot attributes.
            {
                "name": "droplets_list_snapshots",
                "table_name": "snapshot",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "snapshots",
                    "path": "/v2/droplets/{droplet_id}/snapshots",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To list all of the snapshots available on your account, send a GET request to `/v2/snapshots`.  The response will be a JSON object with a key called `snapshots`. This will be set to an array of `snapshot` objects, each of which will contain the standard snapshot attributes.  ### Filtering Results by Resource Type  It's possible to request filtered results by including certain query parameters.  #### List Droplet Snapshots  To retrieve only snapshots based on Droplets, include the `resource_type` query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.  #### List Volume Snapshots  To retrieve only snapshots based on volumes, include the `resource_type` query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`.
            {
                "name": "snapshots_list",
                "table_name": "snapshot",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "snapshots",
                    "path": "/v2/snapshots",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                        # "resource_type": "OPTIONAL_CONFIG",
                    },
                },
            },
            # To retrieve information about a snapshot, send a GET request to `/v2/snapshots/$SNAPSHOT_ID`.  The response will be a JSON object with a key called `snapshot`. The value of this will be an snapshot object containing the standard snapshot attributes.
            {
                "name": "snapshots_get",
                "table_name": "snapshot",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "snapshot",
                    "path": "/v2/snapshots/{snapshot_id}",
                    "params": {
                        "snapshot_id": {
                            "type": "resolve",
                            "resource": "snapshots_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To retrieve the details of a snapshot that has been created from a volume, send a GET request to `/v2/volumes/snapshots/$SNAPSHOT_ID`.
            {
                "name": "volume_snapshots_get_by_id",
                "table_name": "snapshot",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "snapshot",
                    "path": "/v2/volumes/snapshots/{snapshot_id}",
                    "params": {
                        "snapshot_id": {
                            "type": "resolve",
                            "resource": "volumes_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`.
            {
                "name": "volume_snapshots_list",
                "table_name": "snapshot",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "snapshots",
                    "path": "/v2/volumes/{volume_id}/snapshots",
                    "params": {
                        "volume_id": {
                            "type": "resolve",
                            "resource": "volumes_list",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve the configured SQL modes for an existing MySQL cluster, send a GET request to `/v2/databases/$DATABASE_ID/sql_mode`. The response will be a JSON object with a `sql_mode` key. This will be set to a string representing the configured SQL modes.
            {
                "name": "databases_get_sql_mode",
                "table_name": "sql_mode",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/sql_mode",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To show information about an existing check's state, send a GET request to `/v2/uptime/checks/$CHECK_ID/state`.
            {
                "name": "uptime_check_state_get",
                "table_name": "state",
                "endpoint": {
                    "data_selector": "state",
                    "path": "/v2/uptime/checks/{check_id}/state",
                    "params": {
                        "check_id": {
                            "type": "resolve",
                            "resource": "uptime_checks_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To check on the status of a request to destroy a Droplet with its associated resources, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint.
            {
                "name": "droplets_get_destroy_associated_resources_status",
                "table_name": "statu",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "resources.floating_ips",
                    "path": "/v2/droplets/{droplet_id}/destroy_with_associated_resources/status",
                    "params": {
                        "droplet_id": {
                            "type": "resolve",
                            "resource": "droplets_list_associated_resources",
                            "field": "id",
                        },
                    },
                },
            },
            # A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`.
            {
                "name": "registry_get_subscription",
                "table_name": "subscription",
                "endpoint": {
                    "data_selector": "subscription",
                    "path": "/v2/registry/subscription",
                },
            },
            # To retrieve a summary for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/summary`.
            {
                "name": "invoices_get_summary_by_uuid",
                "table_name": "summary",
                "endpoint": {
                    "data_selector": "product_charges.items",
                    "path": "/v2/customers/my/invoices/{invoice_uuid}/summary",
                    "params": {
                        "invoice_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To list all tags in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list tags for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags`.
            {
                "name": "registry_list_repository_tags",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/v2/registry/{registry_name}/{repository_name}/tags",
                    "params": {
                        "registry_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repository_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To list all of your tags, you can send a GET request to `/v2/tags`.
            {
                "name": "tags_list",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "tags",
                    "path": "/v2/tags",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To retrieve an individual tag, you can send a `GET` request to `/v2/tags/$TAG_NAME`.
            {
                "name": "tags_get",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "tag",
                    "path": "/v2/tags/{tag_id}",
                    "params": {
                        "tag_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all app tiers.
            {
                "name": "apps_list_tiers",
                "table_name": "tier",
                "endpoint": {
                    "data_selector": "tiers",
                    "path": "/v2/apps/tiers",
                },
            },
            # Retrieve information about a specific app tier.
            {
                "name": "apps_get_tier",
                "table_name": "tier",
                "primary_key": "slug",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tier",
                    "path": "/v2/apps/tiers/{slug}",
                    "params": {
                        "slug": {
                            "type": "resolve",
                            "resource": "apps_list_tiers",
                            "field": "slug",
                        },
                    },
                },
            },
            # Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`.
            {
                "name": "functions_list_triggers",
                "table_name": "trigger",
                "endpoint": {
                    "data_selector": "triggers",
                    "path": "/v2/functions/namespaces/{namespace_id}/triggers",
                    "params": {
                        "namespace_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`.
            {
                "name": "functions_get_trigger",
                "table_name": "trigger",
                "endpoint": {
                    "data_selector": "trigger",
                    "path": "/v2/functions/namespaces/{namespace_id}/triggers/{trigger_name}",
                    "params": {
                        "namespace_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trigger_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To determine whether a cluster can be upgraded, and the versions to which it can be upgraded, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`.
            {
                "name": "kubernetes_get_available_upgrades",
                "table_name": "upgrade",
                "endpoint": {
                    "data_selector": "available_upgrade_versions",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/upgrades",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the users for your database cluster, send a GET request to `/v2/databases/$DATABASE_ID/users`.  Note: User management is not supported for Redis clusters.  The result will be a JSON object with a `users` key. This will be set to an array of database user objects, each of which will contain the standard database user attributes.  For MySQL clusters, additional options will be contained in the mysql_settings object.
            {
                "name": "databases_list_users",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v2/databases/{database_cluster_uuid}/users",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To show information about an existing database user, send a GET request to `/v2/databases/$DATABASE_ID/users/$USERNAME`.  Note: User management is not supported for Redis clusters.  The response will be a JSON object with a `user` key. This will be set to an object containing the standard database user attributes.  For MySQL clusters, additional options will be contained in the mysql_settings object.
            {
                "name": "databases_get_user",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "user",
                    "path": "/v2/databases/{database_cluster_uuid}/users/{username}",
                    "params": {
                        "database_cluster_uuid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To show information the user associated with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/user`.
            {
                "name": "kubernetes_get_cluster_user",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "kubernetes_cluster_user.groups",
                    "path": "/v2/kubernetes/clusters/{cluster_id}/user",
                    "params": {
                        "cluster_id": {
                            "type": "resolve",
                            "resource": "kubernetes_list_clusters",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`. ## Filtering Results ### By Region The `region` may be provided as query parameter in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1` ### By Name It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per region with the same name. ### By Name and Region It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.
            {
                "name": "volumes_list",
                "table_name": "volume",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "volumes",
                    "path": "/v2/volumes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "name": "OPTIONAL_CONFIG",
                        # "region": "OPTIONAL_CONFIG",
                        # "per_page": "20",
                    },
                },
            },
            # To show information about a block storage volume, send a GET request to `/v2/volumes/$VOLUME_ID`.
            {
                "name": "volumes_get",
                "table_name": "volume",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "volume",
                    "path": "/v2/volumes/{volume_id}",
                    "params": {
                        "volume_id": {
                            "type": "resolve",
                            "resource": "volumes_list",
                            "field": "id",
                        },
                    },
                },
            },
            # To list all of the VPCs on your account, send a GET request to `/v2/vpcs`.
            {
                "name": "vpcs_list",
                "table_name": "vpc",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "vpcs",
                    "path": "/v2/vpcs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "20",
                    },
                },
            },
            # To show information about an existing VPC, send a GET request to `/v2/vpcs/$VPC_ID`.
            {
                "name": "vpcs_get",
                "table_name": "vpc",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "vpc",
                    "path": "/v2/vpcs/{vpc_id}",
                    "params": {
                        "vpc_id": {
                            "type": "resolve",
                            "resource": "vpcs_list",
                            "field": "id",
                        },
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
