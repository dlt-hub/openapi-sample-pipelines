# digital_ocean pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/digital_ocean.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /v2/1-clicks_ 
  *resource*: one_clicks_list  
  *description*: To list all available 1-Click applications, send a GET request to `/v2/1-clicks`. The `type` may be provided as query paramater in order to restrict results to a certain type of 1-Click, for example: `/v2/1-clicks?type=droplet`. Current supported types are `kubernetes` and `droplet`.  The response will be a JSON object with a key called `1_clicks`. This will be set to an array of 1-Click application data, each of which will contain the the slug and type for the 1-Click. 
* _GET /v2/account_ 
  *resource*: account_get  
  *description*: To show information about the current user account, send a GET request to `/v2/account`.
* _GET /v2/actions_ 
  *resource*: actions_list  
  *description*: This will be the entire list of actions taken on your account, so it will be quite large. As with any large collection returned by the API, the results will be paginated with only 20 on each page by default.
* _GET /v2/actions/{action_id}_ 
  *resource*: actions_get  
  *description*: To retrieve a specific action object, send a GET request to `/v2/actions/$ACTION_ID`.
* _GET /v2/droplets/{droplet_id}/actions_ 
  *resource*: droplet_actions_list  
  *description*: To retrieve a list of all actions that have been executed for a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/actions`.  The results will be returned as a JSON object with an `actions` key. This will be set to an array filled with `action` objects containing the standard `action` attributes. 
* _GET /v2/droplets/{droplet_id}/actions/{action_id}_ 
  *resource*: droplet_actions_get  
  *description*: To retrieve a Droplet action, send a GET request to `/v2/droplets/$DROPLET_ID/actions/$ACTION_ID`.  The response will be a JSON object with a key called `action`. The value will be a Droplet action object. 
* _GET /v2/floating_ips/{floating_ip}/actions_ 
  *resource*: floating_i_ps_action_list  
  *description*: To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`.
* _GET /v2/floating_ips/{floating_ip}/actions/{action_id}_ 
  *resource*: floating_i_ps_action_get  
  *description*: To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`.
* _GET /v2/images/{image_id}/actions_ 
  *resource*: image_actions_list  
  *description*: To retrieve all actions that have been executed on an image, send a GET request to `/v2/images/$IMAGE_ID/actions`.
* _GET /v2/images/{image_id}/actions/{action_id}_ 
  *resource*: image_actions_get  
  *description*: To retrieve the status of an image action, send a GET request to `/v2/images/$IMAGE_ID/actions/$IMAGE_ACTION_ID`.
* _GET /v2/reserved_ips/{reserved_ip}/actions_ 
  *resource*: reserved_i_ps_actions_list  
  *description*: To retrieve all actions that have been executed on a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions`.
* _GET /v2/reserved_ips/{reserved_ip}/actions/{action_id}_ 
  *resource*: reserved_i_ps_actions_get  
  *description*: To retrieve the status of a reserved IP action, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions/$ACTION_ID`.
* _GET /v2/volumes/{volume_id}/actions_ 
  *resource*: volume_actions_list  
  *description*: To retrieve all actions that have been executed on a volume, send a GET request to `/v2/volumes/$VOLUME_ID/actions`.  
* _GET /v2/volumes/{volume_id}/actions/{action_id}_ 
  *resource*: volume_actions_get  
  *description*: To retrieve the status of a volume action, send a GET request to `/v2/volumes/$VOLUME_ID/actions/$ACTION_ID`.  
* _GET /v2/apps/{app_id}/alerts_ 
  *resource*: apps_list_alerts  
  *description*: List alerts associated to the app and any components. This includes configuration information about the alerts including emails, slack webhooks, and triggering events or conditions.
* _GET /v2/monitoring/alerts_ 
  *resource*: monitoring_list_alert_policy  
  *description*: Returns all alert policies that are configured for the given account. To List all alert policies, send a GET request to `/v2/monitoring/alerts`.
* _GET /v2/monitoring/alerts/{alert_uuid}_ 
  *resource*: monitoring_get_alert_policy  
  *description*: To retrieve a given alert policy, send a GET request to `/v2/monitoring/alerts/{alert_uuid}`
* _GET /v2/uptime/checks/{check_id}/alerts_ 
  *resource*: uptime_check_alerts_list  
  *description*: To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`.
* _GET /v2/uptime/checks/{check_id}/alerts/{alert_id}_ 
  *resource*: uptime_alert_get  
  *description*: To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`.
* _GET /v2/apps/{app_id}/deployments_ 
  *resource*: apps_list_deployments  
  *description*: List all deployments of an app.
* _GET /v2/apps/{app_id}/deployments/{deployment_id}_ 
  *resource*: apps_get_deployment  
  *description*: Retrieve information about an app deployment.
* _GET /v2/apps_ 
  *resource*: apps_list  
  *description*: List all apps on your account. Information about the current active deployment as well as any in progress ones will also be included for each app.
* _GET /v2/apps/{id}_ 
  *resource*: apps_get  
  *description*: Retrieve details about an existing app by either its ID or name. To retrieve an app by its name, do not include an ID in the request path. Information about the current active deployment as well as any in progress ones will also be included in the response.
* _GET /v2/databases/{database_cluster_uuid}/backups_ 
  *resource*: databases_list_backups  
  *description*: To list all of the available backups of a PostgreSQL or MySQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/backups`. **Note**: Backups are not supported for Redis clusters. The result will be a JSON object with a `backups key`. This will be set to an array of backup objects, each of which will contain the size of the backup and the timestamp at which it was created.
* _GET /v2/droplets/{droplet_id}/backups_ 
  *resource*: droplets_list_backups  
  *description*: To retrieve any backups associated with a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/backups`.  You will get back a JSON object that has a `backups` key. This will be set to an array of backup objects, each of which contain the standard Droplet backup attributes. 
* _GET /v2/customers/my/balance_ 
  *resource*: balance_get  
  *description*: To retrieve the balances on a customer's account, send a GET request to `/v2/customers/my/balance`.
* _GET /v2/monitoring/metrics/droplet/bandwidth_ 
  *resource*: monitoring_get_droplet_bandwidth_metrics  
  *description*: To retrieve bandwidth metrics for a given Droplet, send a GET request to `/v2/monitoring/metrics/droplet/bandwidth`. Use the `interface` query parameter to specify if the results should be for the `private` or `public` interface. Use the `direction` query parameter to specify if the results should be for `inbound` or `outbound` traffic.
* _GET /v2/apps/{app_id}/metrics/bandwidth_daily_ 
  *resource*: apps_get_metrics_bandwidth_daily  
  *description*: Retrieve daily bandwidth usage metrics for a single app.
* _GET /v2/customers/my/billing_history_ 
  *resource*: billing_history_list  
  *description*: To retrieve a list of all billing history entries, send a GET request to `/v2/customers/my/billing_history`.
* _GET /v2/databases/{database_cluster_uuid}/ca_ 
  *resource*: databases_get_ca  
  *description*: To retrieve the public certificate used to secure the connection to the database cluster send a GET request to `/v2/databases/$DATABASE_ID/ca`.  The response will be a JSON object with a `ca` key. This will be set to an object containing the base64 encoding of the public key certificate. 
* _GET /v2/certificates_ 
  *resource*: certificates_list  
  *description*: To list all of the certificates available on your account, send a GET request to `/v2/certificates`.
* _GET /v2/certificates/{certificate_id}_ 
  *resource*: certificates_get  
  *description*: To show information about an existing certificate, send a GET request to `/v2/certificates/$CERTIFICATE_ID`.
* _GET /v2/uptime/checks_ 
  *resource*: uptime_checks_list  
  *description*: To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`.
* _GET /v2/uptime/checks/{check_id}_ 
  *resource*: uptime_check_get  
  *description*: To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`.
* _GET /v2/kubernetes/clusters_ 
  *resource*: kubernetes_list_clusters  
  *description*: To list all of the Kubernetes clusters on your account, send a GET request to `/v2/kubernetes/clusters`. 
* _GET /v2/kubernetes/clusters/{cluster_id}_ 
  *resource*: kubernetes_get_cluster  
  *description*: To show information about an existing Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID`. 
* _GET /v2/kubernetes/clusters/{cluster_id}/clusterlint_ 
  *resource*: kubernetes_get_cluster_lint_results  
  *description*: To request clusterlint diagnostics for your cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/clusterlint`. If the `run_id` query parameter is provided, then the diagnostics for the specific run is fetched. By default, the latest results are shown.  To find out how to address clusterlint feedback, please refer to [the clusterlint check documentation](https://github.com/digitalocean/clusterlint/blob/master/checks.md). 
* _GET /v2/databases/{database_cluster_uuid}/config_ 
  *resource*: databases_get_config  
  *description*: Shows configuration parameters for an existing database cluster by sending a GET request to `/v2/databases/$DATABASE_ID/config`. The response is a JSON object with a `config` key, which is set to an object containing any database configuration parameters. 
* _GET /v2/monitoring/metrics/droplet/cpu_ 
  *resource*: monitoring_get_droplet_cpu_metrics  
  *description*: To retrieve CPU metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/cpu`.
* _GET /v2/kubernetes/clusters/{cluster_id}/credentials_ 
  *resource*: kubernetes_get_credentials  
  *description*: This endpoint returns a JSON object . It can be used to programmatically construct Kubernetes clients which cannot parse kubeconfig files.  The resulting JSON object contains token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)".  To retrieve credentials for accessing a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/credentials`.  Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication. 
* _GET /v2/customers/my/invoices/{invoice_uuid}/csv_ 
  *resource*: invoices_get_csv_by_uuid  
  *description*: To retrieve a CSV for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/csv`.
* _GET /v2/databases_ 
  *resource*: databases_list_clusters  
  *description*: To list all of the database clusters available on your account, send a GET request to `/v2/databases`. To limit the results to database clusters with a specific tag, include the `tag_name` query parameter set to the name of the tag. For example, `/v2/databases?tag_name=$TAG_NAME`. The result will be a JSON object with a `databases` key. This will be set to an array of database objects, each of which will contain the standard database attributes. The embedded `connection` and `private_connection` objects will contain the information needed to access the database cluster: The embedded `maintenance_window` object will contain information about any scheduled maintenance for the database cluster.
* _GET /v2/databases/{database_cluster_uuid}_ 
  *resource*: databases_get_cluster  
  *description*: To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID`. The response will be a JSON object with a database key. This will be set to an object containing the standard database cluster attributes. The embedded connection and private_connection objects will contain the information needed to access the database cluster. The embedded maintenance_window object will contain information about any scheduled maintenance for the database cluster.
* _GET /v2/databases/{database_cluster_uuid}/dbs_ 
  *resource*: databases_list  
  *description*: To list all of the databases in a clusters, send a GET request to `/v2/databases/$DATABASE_ID/dbs`.  The result will be a JSON object with a `dbs` key. This will be set to an array of database objects, each of which will contain the standard database attributes.  Note: Database management is not supported for Redis clusters. 
* _GET /v2/databases/{database_cluster_uuid}/dbs/{database_name}_ 
  *resource*: databases_get  
  *description*: To show information about an existing database cluster, send a GET request to `/v2/databases/$DATABASE_ID/dbs/$DB_NAME`.  Note: Database management is not supported for Redis clusters.  The response will be a JSON object with a `db` key. This will be set to an object containing the standard database attributes. 
* _GET /v2/projects/default_ 
  *resource*: projects_get_default  
  *description*: To get your default project, send a GET request to `/v2/projects/default`.
* _GET /v2/droplets/{droplet_id}/destroy_with_associated_resources_ 
  *resource*: droplets_list_associated_resources  
  *description*: To list the associated billable resources that can be destroyed along with a Droplet, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources` endpoint.  The response will be a JSON object containing `snapshots`, `volumes`, and `volume_snapshots` keys. Each will be set to an array of objects containing information about the associated resources. 
* _GET /v2/kubernetes/clusters/{cluster_id}/destroy_with_associated_resources_ 
  *resource*: kubernetes_list_associated_resources  
  *description*: To list the associated billable resources that can be destroyed along with a cluster, send a GET request to the `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/destroy_with_associated_resources` endpoint.
* _GET /v2/registry/{registry_name}/{repository_name}/digests_ 
  *resource*: registry_list_repository_manifests  
  *description*: To list all manifests in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/digests`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list manifests for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/digests`. 
* _GET /v2/registry/docker-credentials_ 
  *resource*: registry_get_docker_credentials  
  *description*: In order to access your container registry with the Docker client or from a Kubernetes cluster, you will need to configure authentication. The necessary JSON configuration can be retrieved by sending a GET request to `/v2/registry/docker-credentials`.  The response will be in the format of a Docker `config.json` file. To use the config in your Kubernetes cluster, create a Secret with:      kubectl create secret generic docr \       --from-file=.dockerconfigjson=config.json \       --type=kubernetes.io/dockerconfigjson  By default, the returned credentials have read-only access to your registry and cannot be used to push images. This is appropriate for most Kubernetes clusters. To retrieve read/write credentials, suitable for use with the Docker client or in a CI system, read_write may be provided as query parameter. For example: `/v2/registry/docker-credentials?read_write=true`  By default, the returned credentials will not expire. To retrieve credentials with an expiry set, expiry_seconds may be provided as a query parameter. For example: `/v2/registry/docker-credentials?expiry_seconds=3600` will return credentials that expire after one hour. 
* _GET /v2/domains_ 
  *resource*: domains_list  
  *description*: To retrieve a list of all of the domains in your account, send a GET request to `/v2/domains`.
* _GET /v2/domains/{domain_name}_ 
  *resource*: domains_get  
  *description*: To get details about a specific domain, send a GET request to `/v2/domains/$DOMAIN_NAME`.
* _GET /v2/droplets_ 
  *resource*: droplets_list  
  *description*: To list all Droplets in your account, send a GET request to `/v2/droplets`.  The response body will be a JSON object with a key of `droplets`. This will be set to an array containing objects each representing a Droplet. These will contain the standard Droplet attributes.  ### Filtering Results by Tag  It's possible to request filtered results by including certain query parameters. To only list Droplets assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/droplets?tag_name=$TAG_NAME`. 
* _GET /v2/droplets/{droplet_id}_ 
  *resource*: droplets_get  
  *description*: To show information about an individual Droplet, send a GET request to `/v2/droplets/$DROPLET_ID`. 
* _GET /v2/reports/droplet_neighbors_ids_ 
  *resource*: droplets_list_neighbors_ids  
  *description*: To retrieve a list of all Droplets that are co-located on the same physical hardware, send a GET request to `/v2/reports/droplet_neighbors_ids`.  The results will be returned as a JSON object with a key of `neighbor_ids`. This will be set to an array of arrays. Each array will contain a set of Droplet IDs for Droplets that share a physical server. An empty array indicates that all Droplets associated with your account are located on separate physical hardware. 
* _GET /v2/cdn/endpoints_ 
  *resource*: cdn_list_endpoints  
  *description*: To list all of the CDN endpoints available on your account, send a GET request to `/v2/cdn/endpoints`.
* _GET /v2/cdn/endpoints/{cdn_id}_ 
  *resource*: cdn_get_endpoint  
  *description*: To show information about an existing CDN endpoint, send a GET request to `/v2/cdn/endpoints/$ENDPOINT_ID`.
* _GET /v2/databases/{database_cluster_uuid}/eviction_policy_ 
  *resource*: databases_get_eviction_policy  
  *description*: To retrieve the configured eviction policy for an existing Redis cluster, send a GET request to `/v2/databases/$DATABASE_ID/eviction_policy`. The response will be a JSON object with an `eviction_policy` key. This will be set to a string representing the eviction policy.
* _GET /v2/monitoring/metrics/droplet/filesystem_free_ 
  *resource*: monitoring_get_droplet_filesystem_free_metrics  
  *description*: To retrieve filesystem free metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_free`.
* _GET /v2/monitoring/metrics/droplet/filesystem_size_ 
  *resource*: monitoring_get_droplet_filesystem_size_metrics  
  *description*: To retrieve filesystem size metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/filesystem_size`.
* _GET /v2/databases/{database_cluster_uuid}/firewall_ 
  *resource*: databases_list_firewall_rules  
  *description*: To list all of a database cluster's firewall rules (known as "trusted sources" in the control panel), send a GET request to `/v2/databases/$DATABASE_ID/firewall`. The result will be a JSON object with a `rules` key.
* _GET /v2/droplets/{droplet_id}/firewalls_ 
  *resource*: droplets_list_firewalls  
  *description*: To retrieve a list of all firewalls available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/firewalls`  The response will be a JSON object that has a key called `firewalls`. This will be set to an array of `firewall` objects, each of which contain the standard `firewall` attributes. 
* _GET /v2/firewalls_ 
  *resource*: firewalls_list  
  *description*: To list all of the firewalls available on your account, send a GET request to `/v2/firewalls`.
* _GET /v2/firewalls/{firewall_id}_ 
  *resource*: firewalls_get  
  *description*: To show information about an existing firewall, send a GET request to `/v2/firewalls/$FIREWALL_ID`.
* _GET /v2/floating_ips_ 
  *resource*: floating_i_ps_list  
  *description*: To list all of the floating IPs available on your account, send a GET request to `/v2/floating_ips`.
* _GET /v2/floating_ips/{floating_ip}_ 
  *resource*: floating_i_ps_get  
  *description*: To show information about a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP_ADDR`.
* _GET /v2/registry/{registry_name}/garbage-collection_ 
  *resource*: registry_get_garbage_collection  
  *description*: To get information about the currently-active garbage collection for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collection`.
* _GET /v2/registry/{registry_name}/garbage-collections_ 
  *resource*: registry_list_garbage_collections  
  *description*: To get information about past garbage collections for a registry, send a GET request to `/v2/registry/$REGISTRY_NAME/garbage-collections`.
* _GET /v2/apps/regions_ 
  *resource*: apps_list_regions  
  *description*: List all regions supported by App Platform.
* _GET /v2/images_ 
  *resource*: images_list  
  *description*: To list all of the images available on your account, send a GET request to /v2/images.  ## Filtering Results -----  It's possible to request filtered results by including certain query parameters.  **Image Type**  Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter.  > Important: The `type` query parameter does not directly relate to the `type` attribute.  To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`.  To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`.  **User Images**  To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`.  **Tags**  To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`. 
* _GET /v2/images/{image_id}_ 
  *resource*: images_get  
  *description*: To retrieve information about an image, send a `GET` request to `/v2/images/$IDENTIFIER`. 
* _GET /v2/apps/tiers/instance_sizes_ 
  *resource*: apps_list_instance_sizes  
  *description*: List all instance sizes for `service`, `worker`, and `job` components.
* _GET /v2/apps/tiers/instance_sizes/{slug}_ 
  *resource*: apps_get_instance_size  
  *description*: Retrieve information about a specific instance size for `service`, `worker`, and `job` components.
* _GET /v2/customers/my/invoices_ 
  *resource*: invoices_list  
  *description*: To retrieve a list of all invoices, send a GET request to `/v2/customers/my/invoices`.
* _GET /v2/customers/my/invoices/{invoice_uuid}_ 
  *resource*: invoices_get_by_uuid  
  *description*: To retrieve the invoice items for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID`.
* _GET /v2/droplets/{droplet_id}/kernels_ 
  *resource*: droplets_list_kernels  
  *description*: To retrieve a list of all kernels available to a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/kernels`  The response will be a JSON object that has a key called `kernels`. This will be set to an array of `kernel` objects, each of which contain the standard `kernel` attributes. 
* _GET /v2/account/keys_ 
  *resource*: ssh_keys_list  
  *description*: To list all of the keys in your account, send a GET request to `/v2/account/keys`. The response will be a JSON object with a key set to `ssh_keys`. The value of this will be an array of ssh_key objects, each of which contains the standard ssh_key attributes.
* _GET /v2/account/keys/{ssh_key_identifier}_ 
  *resource*: ssh_keys_get  
  *description*: To get information about a key, send a GET request to `/v2/account/keys/$KEY_ID` or `/v2/account/keys/$KEY_FINGERPRINT`. The response will be a JSON object with the key `ssh_key` and value an ssh_key object which contains the standard ssh_key attributes.
* _GET /v2/kubernetes/clusters/{cluster_id}/kubeconfig_ 
  *resource*: kubernetes_get_kubeconfig  
  *description*: This endpoint returns a kubeconfig file in YAML format. It can be used to connect to and administer the cluster using the Kubernetes command line tool, `kubectl`, or other programs supporting kubeconfig files (e.g., client libraries).  The resulting kubeconfig file uses token-based authentication for clusters supporting it, and certificate-based authentication otherwise. For a list of supported versions and more information, see "[How to Connect to a DigitalOcean Kubernetes Cluster with kubectl](https://www.digitalocean.com/docs/kubernetes/how-to/connect-with-kubectl/)".  To retrieve a kubeconfig file for use with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig`.  Clusters supporting token-based authentication may define an expiration by passing a duration in seconds as a query parameter to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/kubeconfig?expiry_seconds=$DURATION_IN_SECONDS`. If not set or 0, then the token will have a 7 day expiry. The query parameter has no impact in certificate-based authentication. 
* _GET /v2/monitoring/metrics/droplet/load_1_ 
  *resource*: monitoring_get_droplet_load_1_metrics  
  *description*: To retrieve 1 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_1`.
* _GET /v2/monitoring/metrics/droplet/load_15_ 
  *resource*: monitoring_get_droplet_load_15_metrics  
  *description*: To retrieve 15 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_15`.
* _GET /v2/monitoring/metrics/droplet/load_5_ 
  *resource*: monitoring_get_droplet_load_5_metrics  
  *description*: To retrieve 5 minute load average metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/load_5`.
* _GET /v2/load_balancers_ 
  *resource*: load_balancers_list  
  *description*: To list all of the load balancer instances on your account, send a GET request to `/v2/load_balancers`. 
* _GET /v2/load_balancers/{lb_id}_ 
  *resource*: load_balancers_get  
  *description*: To show information about a load balancer instance, send a GET request to `/v2/load_balancers/$LOAD_BALANCER_ID`. 
* _GET /v2/apps/{app_id}/components/{component_name}/logs_ 
  *resource*: apps_get_logs_active_deployment  
  *description*: Retrieve the logs of the active deployment if one exists. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. Note log_type=BUILD logs will return logs associated with the current active deployment (being served). To view build logs associated with in-progress build, the query must explicitly reference the deployment id.
* _GET /v2/apps/{app_id}/deployments/{deployment_id}/components/{component_name}/logs_ 
  *resource*: apps_get_logs  
  *description*: Retrieve the logs of a past, in-progress, or active deployment. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.
* _GET /v2/apps/{app_id}/deployments/{deployment_id}/logs_ 
  *resource*: apps_get_logs_aggregate  
  *description*: Retrieve the logs of a past, in-progress, or active deployment. If a component name is specified, the logs will be limited to only that component. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment.
* _GET /v2/apps/{app_id}/logs_ 
  *resource*: apps_get_logs_active_deployment_aggregate  
  *description*: Retrieve the logs of the active deployment if one exists. The response will include links to either real-time logs of an in-progress or active deployment or archived logs of a past deployment. Note log_type=BUILD logs will return logs associated with the current active deployment (being served). To view build logs associated with in-progress build, the query must explicitly reference the deployment id.
* _GET /v2/vpcs/{vpc_id}/members_ 
  *resource*: vpcs_list_members  
  *description*: To list all of the resources that are members of a VPC, send a GET request to `/v2/vpcs/$VPC_ID/members`.  To only list resources of a specific type that are members of the VPC, included a `resource_type` query parameter. For example, to only list Droplets in the VPC, send a GET request to `/v2/vpcs/$VPC_ID/members?resource_type=droplet`. 
* _GET /v2/monitoring/metrics/droplet/memory_available_ 
  *resource*: monitoring_get_droplet_memory_available_metrics  
  *description*: To retrieve available memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_available`.
* _GET /v2/monitoring/metrics/droplet/memory_cached_ 
  *resource*: monitoring_get_droplet_memory_cached_metrics  
  *description*: To retrieve cached memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_cached`.
* _GET /v2/monitoring/metrics/droplet/memory_free_ 
  *resource*: monitoring_get_droplet_memory_free_metrics  
  *description*: To retrieve free memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_free`.
* _GET /v2/monitoring/metrics/droplet/memory_total_ 
  *resource*: monitoring_get_droplet_memory_total_metrics  
  *description*: To retrieve total memory metrics for a given droplet, send a GET request to `/v2/monitoring/metrics/droplet/memory_total`.
* _GET /v2/functions/namespaces_ 
  *resource*: functions_list_namespaces  
  *description*: Returns a list of namespaces associated with the current user. To get all namespaces, send a GET request to `/v2/functions/namespaces`.
* _GET /v2/functions/namespaces/{namespace_id}_ 
  *resource*: functions_get_namespace  
  *description*: Gets the namespace details for the given namespace UUID. To get namespace details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID` with no parameters.
* _GET /v2/droplets/{droplet_id}/neighbors_ 
  *resource*: droplets_list_neighbors  
  *description*: To retrieve a list of any "neighbors" (i.e. Droplets that are co-located on the same physical hardware) for a specific Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/neighbors`.  The results will be returned as a JSON object with a key of `droplets`. This will be set to an array containing objects representing any other Droplets that share the same physical hardware. An empty array indicates that the Droplet is not co-located any other Droplets associated with your account. 
* _GET /v2/kubernetes/clusters/{cluster_id}/node_pools_ 
  *resource*: kubernetes_list_node_pools  
  *description*: To list all of the node pools in a Kubernetes clusters, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools`. 
* _GET /v2/kubernetes/clusters/{cluster_id}/node_pools/{node_pool_id}_ 
  *resource*: kubernetes_get_node_pool  
  *description*: To show information about a specific node pool in a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/node_pools/$NODE_POOL_ID`. 
* _GET /v2/databases/{database_cluster_uuid}/online-migration_ 
  *resource*: databases_get_migration_status  
  *description*: To retrieve the status of the most recent online migration, send a GET request to `/v2/databases/$DATABASE_ID/online-migration`. 
* _GET /v2/databases/options_ 
  *resource*: databases_list_options  
  *description*: To list all of the options available for the offered database engines, send a GET request to `/v2/databases/options`. The result will be a JSON object with an `options` key.
* _GET /v2/kubernetes/options_ 
  *resource*: kubernetes_list_options  
  *description*: To list the versions of Kubernetes available for use, the regions that support Kubernetes, and the available node sizes, send a GET request to `/v2/kubernetes/options`.
* _GET /v2/registry/options_ 
  *resource*: registry_get_options  
  *description*: This endpoint serves to provide additional information as to which option values are available when creating a container registry. There are multiple subscription tiers available for container registry. Each tier allows a different number of image repositories to be created in your registry, and has a different amount of storage and transfer included. There are multiple regions available for container registry and controls where your data is stored. To list the available options, send a GET request to `/v2/registry/options`.
* _GET /v2/customers/my/invoices/{invoice_uuid}/pdf_ 
  *resource*: invoices_get_pdf_by_uuid  
  *description*: To retrieve a PDF for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/pdf`.
* _GET /v2/databases/{database_cluster_uuid}/pools_ 
  *resource*: databases_list_connection_pools  
  *description*: To list all of the connection pools available to a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools`. The result will be a JSON object with a `pools` key. This will be set to an array of connection pool objects.
* _GET /v2/databases/{database_cluster_uuid}/pools/{pool_name}_ 
  *resource*: databases_get_connection_pool  
  *description*: To show information about an existing connection pool for a PostgreSQL database cluster, send a GET request to `/v2/databases/$DATABASE_ID/pools/$POOL_NAME`. The response will be a JSON object with a `pool` key.
* _GET /v2/projects_ 
  *resource*: projects_list  
  *description*: To list all your projects, send a GET request to `/v2/projects`.
* _GET /v2/projects/{project_id}_ 
  *resource*: projects_get  
  *description*: To get a project, send a GET request to `/v2/projects/$PROJECT_ID`.
* _GET /v2/domains/{domain_name}/records_ 
  *resource*: domains_list_records  
  *description*: To get a listing of all records configured for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records`. The list of records returned can be filtered by using the `name` and `type` query parameters. For example, to only include A records for a domain, send a GET request to `/v2/domains/$DOMAIN_NAME/records?type=A`. `name` must be a fully qualified record name. For example, to only include records matching `sub.example.com`, send a GET request to `/v2/domains/$DOMAIN_NAME/records?name=sub.example.com`. Both name and type may be used together.  
* _GET /v2/domains/{domain_name}/records/{domain_record_id}_ 
  *resource*: domains_get_record  
  *description*: To retrieve a specific domain record, send a GET request to `/v2/domains/$DOMAIN_NAME/records/$RECORD_ID`.
* _GET /v2/regions_ 
  *resource*: regions_list  
  *description*: To list all of the regions that are available, send a GET request to `/v2/regions`. The response will be a JSON object with a key called `regions`. The value of this will be an array of `region` objects, each of which will contain the standard region attributes.
* _GET /v2/registry_ 
  *resource*: registry_get  
  *description*: To get information about your container registry, send a GET request to `/v2/registry`.
* _GET /v2/databases/{database_cluster_uuid}/replicas_ 
  *resource*: databases_list_replicas  
  *description*: To list all of the read-only replicas associated with a database cluster, send a GET request to `/v2/databases/$DATABASE_ID/replicas`.  **Note**: Read-only replicas are not supported for Redis clusters.  The result will be a JSON object with a `replicas` key. This will be set to an array of database replica objects, each of which will contain the standard database replica attributes.
* _GET /v2/databases/{database_cluster_uuid}/replicas/{replica_name}_ 
  *resource*: databases_get_replica  
  *description*: To show information about an existing database replica, send a GET request to `/v2/databases/$DATABASE_ID/replicas/$REPLICA_NAME`.  **Note**: Read-only replicas are not supported for Redis clusters.  The response will be a JSON object with a `replica key`. This will be set to an object containing the standard database replica attributes.
* _GET /v2/registry/{registry_name}/repositoriesV2_ 
  *resource*: registry_list_repositories_v2  
  *description*: To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositoriesV2`.
* _GET /v2/registry/{registry_name}/repositories_ 
  *resource*: registry_list_repositories  
  *description*: This endpoint has been deprecated in favor of the _List All Container Registry Repositories [V2]_ endpoint.  To list all repositories in your container registry, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories`. 
* _GET /v2/reserved_ips_ 
  *resource*: reserved_i_ps_list  
  *description*: To list all of the reserved IPs available on your account, send a GET request to `/v2/reserved_ips`.
* _GET /v2/reserved_ips/{reserved_ip}_ 
  *resource*: reserved_i_ps_get  
  *description*: To show information about a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP_ADDR`.
* _GET /v2/projects/default/resources_ 
  *resource*: projects_list_resources_default  
  *description*: To list all your resources in your default project, send a GET request to `/v2/projects/default/resources`.
* _GET /v2/projects/{project_id}/resources_ 
  *resource*: projects_list_resources  
  *description*: To list all your resources in a project, send a GET request to `/v2/projects/$PROJECT_ID/resources`.
* _GET /v2/sizes_ 
  *resource*: sizes_list  
  *description*: To list all of available Droplet sizes, send a GET request to `/v2/sizes`. The response will be a JSON object with a key called `sizes`. The value of this will be an array of `size` objects each of which contain the standard size attributes.
* _GET /v2/droplets/{droplet_id}/snapshots_ 
  *resource*: droplets_list_snapshots  
  *description*: To retrieve the snapshots that have been created from a Droplet, send a GET request to `/v2/droplets/$DROPLET_ID/snapshots`.  You will get back a JSON object that has a `snapshots` key. This will be set to an array of snapshot objects, each of which contain the standard Droplet snapshot attributes. 
* _GET /v2/snapshots_ 
  *resource*: snapshots_list  
  *description*: To list all of the snapshots available on your account, send a GET request to `/v2/snapshots`.  The response will be a JSON object with a key called `snapshots`. This will be set to an array of `snapshot` objects, each of which will contain the standard snapshot attributes.  ### Filtering Results by Resource Type  It's possible to request filtered results by including certain query parameters.  #### List Droplet Snapshots  To retrieve only snapshots based on Droplets, include the `resource_type` query parameter set to `droplet`. For example, `/v2/snapshots?resource_type=droplet`.  #### List Volume Snapshots  To retrieve only snapshots based on volumes, include the `resource_type` query parameter set to `volume`. For example, `/v2/snapshots?resource_type=volume`. 
* _GET /v2/snapshots/{snapshot_id}_ 
  *resource*: snapshots_get  
  *description*: To retrieve information about a snapshot, send a GET request to `/v2/snapshots/$SNAPSHOT_ID`.  The response will be a JSON object with a key called `snapshot`. The value of this will be an snapshot object containing the standard snapshot attributes. 
* _GET /v2/volumes/snapshots/{snapshot_id}_ 
  *resource*: volume_snapshots_get_by_id  
  *description*: To retrieve the details of a snapshot that has been created from a volume, send a GET request to `/v2/volumes/snapshots/$SNAPSHOT_ID`.  
* _GET /v2/volumes/{volume_id}/snapshots_ 
  *resource*: volume_snapshots_list  
  *description*: To retrieve the snapshots that have been created from a volume, send a GET request to `/v2/volumes/$VOLUME_ID/snapshots`.  
* _GET /v2/databases/{database_cluster_uuid}/sql_mode_ 
  *resource*: databases_get_sql_mode  
  *description*: To retrieve the configured SQL modes for an existing MySQL cluster, send a GET request to `/v2/databases/$DATABASE_ID/sql_mode`. The response will be a JSON object with a `sql_mode` key. This will be set to a string representing the configured SQL modes.
* _GET /v2/uptime/checks/{check_id}/state_ 
  *resource*: uptime_check_state_get  
  *description*: To show information about an existing check's state, send a GET request to `/v2/uptime/checks/$CHECK_ID/state`.
* _GET /v2/droplets/{droplet_id}/destroy_with_associated_resources/status_ 
  *resource*: droplets_get_destroy_associated_resources_status  
  *description*: To check on the status of a request to destroy a Droplet with its associated resources, send a GET request to the `/v2/droplets/$DROPLET_ID/destroy_with_associated_resources/status` endpoint. 
* _GET /v2/registry/subscription_ 
  *resource*: registry_get_subscription  
  *description*: A subscription is automatically created when you configure your container registry. To get information about your subscription, send a GET request to `/v2/registry/subscription`.
* _GET /v2/customers/my/invoices/{invoice_uuid}/summary_ 
  *resource*: invoices_get_summary_by_uuid  
  *description*: To retrieve a summary for an invoice, send a GET request to `/v2/customers/my/invoices/$INVOICE_UUID/summary`.
* _GET /v2/registry/{registry_name}/{repository_name}/tags_ 
  *resource*: registry_list_repository_tags  
  *description*: To list all tags in your container registry repository, send a GET request to `/v2/registry/$REGISTRY_NAME/repositories/$REPOSITORY_NAME/tags`.  Note that if your repository name contains `/` characters, it must be URL-encoded in the request URL. For example, to list tags for `registry.digitalocean.com/example/my/repo`, the path would be `/v2/registry/example/repositories/my%2Frepo/tags`. 
* _GET /v2/tags_ 
  *resource*: tags_list  
  *description*: To list all of your tags, you can send a GET request to `/v2/tags`.
* _GET /v2/tags/{tag_id}_ 
  *resource*: tags_get  
  *description*: To retrieve an individual tag, you can send a `GET` request to `/v2/tags/$TAG_NAME`.
* _GET /v2/apps/tiers_ 
  *resource*: apps_list_tiers  
  *description*: List all app tiers.
* _GET /v2/apps/tiers/{slug}_ 
  *resource*: apps_get_tier  
  *description*: Retrieve information about a specific app tier.
* _GET /v2/functions/namespaces/{namespace_id}/triggers_ 
  *resource*: functions_list_triggers  
  *description*: Returns a list of triggers associated with the current user and namespace. To get all triggers, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers`.
* _GET /v2/functions/namespaces/{namespace_id}/triggers/{trigger_name}_ 
  *resource*: functions_get_trigger  
  *description*: Gets the trigger details. To get the trigger details, send a GET request to `/v2/functions/namespaces/$NAMESPACE_ID/triggers/$TRIGGER_NAME`.
* _GET /v2/kubernetes/clusters/{cluster_id}/upgrades_ 
  *resource*: kubernetes_get_available_upgrades  
  *description*: To determine whether a cluster can be upgraded, and the versions to which it can be upgraded, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/upgrades`. 
* _GET /v2/databases/{database_cluster_uuid}/users_ 
  *resource*: databases_list_users  
  *description*: To list all of the users for your database cluster, send a GET request to `/v2/databases/$DATABASE_ID/users`.  Note: User management is not supported for Redis clusters.  The result will be a JSON object with a `users` key. This will be set to an array of database user objects, each of which will contain the standard database user attributes.  For MySQL clusters, additional options will be contained in the mysql_settings object. 
* _GET /v2/databases/{database_cluster_uuid}/users/{username}_ 
  *resource*: databases_get_user  
  *description*: To show information about an existing database user, send a GET request to `/v2/databases/$DATABASE_ID/users/$USERNAME`.  Note: User management is not supported for Redis clusters.  The response will be a JSON object with a `user` key. This will be set to an object containing the standard database user attributes.  For MySQL clusters, additional options will be contained in the mysql_settings object. 
* _GET /v2/kubernetes/clusters/{cluster_id}/user_ 
  *resource*: kubernetes_get_cluster_user  
  *description*: To show information the user associated with a Kubernetes cluster, send a GET request to `/v2/kubernetes/clusters/$K8S_CLUSTER_ID/user`. 
* _GET /v2/volumes_ 
  *resource*: volumes_list  
  *description*: To list all of the block storage volumes available on your account, send a GET request to `/v2/volumes`. ## Filtering Results ### By Region The `region` may be provided as query parameter in order to restrict results to volumes available in a specific region. For example: `/v2/volumes?region=nyc1` ### By Name It is also possible to list volumes on your account that match a specified name. To do so, send a GET request with the volume's name as a query parameter to `/v2/volumes?name=$VOLUME_NAME`. **Note:** You can only create one volume per region with the same name. ### By Name and Region It is also possible to retrieve information about a block storage volume by name. To do so, send a GET request with the volume's name and the region slug for the region it is located in as query parameters to `/v2/volumes?name=$VOLUME_NAME&region=nyc1`.   
* _GET /v2/volumes/{volume_id}_ 
  *resource*: volumes_get  
  *description*: To show information about a block storage volume, send a GET request to `/v2/volumes/$VOLUME_ID`.  
* _GET /v2/vpcs_ 
  *resource*: vpcs_list  
  *description*: To list all of the VPCs on your account, send a GET request to `/v2/vpcs`.
* _GET /v2/vpcs/{vpc_id}_ 
  *resource*: vpcs_get  
  *description*: To show information about an existing VPC, send a GET request to `/v2/vpcs/$VPC_ID`.
