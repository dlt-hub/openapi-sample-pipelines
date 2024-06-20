from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="github_source", max_table_nesting=2)
def github_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # Lists repositories and their GitHub Actions cache usage for an organization. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  OAuth tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_usage_by_repo_for_org",
                "table_name": "actions_cache_usage_by_repository",
                "endpoint": {
                    "data_selector": "repository_cache_usages",
                    "path": "/orgs/{org}/actions/cache/usage-by-repository",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets GitHub Actions cache usage for a repository. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_usage",
                "table_name": "actions_cache_usage_by_repository",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/cache/usage",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the total GitHub Actions cache usage for an enterprise. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  OAuth tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_usage_for_enterprise",
                "table_name": "actions_cache_usage_org_enterprise",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/cache/usage",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the total GitHub Actions cache usage for an organization. The data fetched using this API is refreshed approximately every 5 minutes, so values returned from this endpoint may take at least 5 minutes to get updated.  OAuth tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_usage_for_org",
                "table_name": "actions_cache_usage_org_enterprise",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/cache/usage",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the GitHub Actions cache usage policy for an enterprise.  OAuth tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_usage_policy_for_enterprise",
                "table_name": "actions_cache_usage_policy_enterprise",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/cache/usage-policy",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets GitHub Actions cache usage policy for a repository.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_usage_policy",
                "table_name": "actions_cache_usage_policy_for_repository",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/cache/usage-policy",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the GitHub Actions permissions policy for organizations and allowed actions in an enterprise.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminget_github_actions_permissions_enterprise",
                "table_name": "actions_enterprise_permissions",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/permissions",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an enterprise, as well as whether GitHub Actions can submit approving pull request reviews. For more information, see "[Enforcing a policy for workflow permissions in your enterprise](https://docs.github.com/enterprise-server@3.9/admin/policies/enforcing-policies-for-your-enterprise/enforcing-policies-for-github-actions-in-your-enterprise#enforcing-a-policy-for-workflow-permissions-in-your-enterprise)."  OAuth tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "actionsget_github_actions_default_workflow_permissions_enterprise",
                "table_name": "actions_get_default_workflow_permissions",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/permissions/workflow",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in an organization, as well as whether GitHub Actions can submit approving pull request reviews. For more information, see "[Setting the permissions of the GITHUB_TOKEN for your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization#setting-the-permissions-of-the-github_token-for-your-organization)."  OAuth tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "actionsget_github_actions_default_workflow_permissions_organization",
                "table_name": "actions_get_default_workflow_permissions",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/permissions/workflow",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the default workflow permissions granted to the `GITHUB_TOKEN` when running workflows in a repository, as well as if GitHub Actions can submit approving pull request reviews. For more information, see "[Setting the permissions of the GITHUB_TOKEN for your repository](https://docs.github.com/enterprise-server@3.9/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#setting-the-permissions-of-the-github_token-for-your-repository)."  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_github_actions_default_workflow_permissions_repository",
                "table_name": "actions_get_default_workflow_permissions",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/permissions/workflow",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the GitHub Actions permissions policy for repositories and allowed actions in an organization.  You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
            {
                "name": "actionsget_github_actions_permissions_organization",
                "table_name": "actions_organization_permissions",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/permissions",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  The authenticated user must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_org_public_key",
                "table_name": "actions_public_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/secrets/public-key",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_repo_public_key",
                "table_name": "actions_public_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/secrets/public-key",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get the public key for an environment, which you need to encrypt environment secrets. You need to encrypt a secret before you can create or update secrets.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_environment_public_key",
                "table_name": "actions_public_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/secrets/public-key",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "environment_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the GitHub Actions permissions policy for a repository, including whether GitHub Actions is enabled and the actions allowed to run in the repository.  You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API.
            {
                "name": "actionsget_github_actions_permissions_repository",
                "table_name": "actions_repository_permissions",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/permissions",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all organization secrets shared with a repository without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_repo_organization_secrets",
                "table_name": "actions_secret",
                "endpoint": {
                    "data_selector": "secrets",
                    "path": "/repos/{owner}/{repo}/actions/organization-secrets",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all secrets available in a repository without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_repo_secrets",
                "table_name": "actions_secret",
                "endpoint": {
                    "data_selector": "secrets",
                    "path": "/repos/{owner}/{repo}/actions/secrets",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single repository secret without revealing its encrypted value.  The authenticated user must have collaborator access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_repo_secret",
                "table_name": "actions_secret",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/secrets/{secret_name}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all secrets available in an environment without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_environment_secrets",
                "table_name": "actions_secret",
                "endpoint": {
                    "data_selector": "secrets",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/secrets",
                    "params": {
                        "environment_name": {
                            "type": "resolve",
                            "resource": "reposget_all_environments",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single environment secret without revealing its encrypted value.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_environment_secret",
                "table_name": "actions_secret",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/secrets/{secret_name}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "environment_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all organization variables shared with a repository.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_repo_organization_variables",
                "table_name": "actions_variable",
                "endpoint": {
                    "data_selector": "variables",
                    "path": "/repos/{owner}/{repo}/actions/organization-variables",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "10",
                    },
                },
            },
            # Lists all repository variables.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_repo_variables",
                "table_name": "actions_variable",
                "endpoint": {
                    "data_selector": "variables",
                    "path": "/repos/{owner}/{repo}/actions/variables",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "10",
                    },
                },
            },
            # Gets a specific variable in a repository.  The authenticated user must have collaborator access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_repo_variable",
                "table_name": "actions_variable",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/variables/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "actionslist_repo_variables",
                            "field": "name",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all environment variables.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_environment_variables",
                "table_name": "actions_variable",
                "endpoint": {
                    "data_selector": "variables",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/variables",
                    "params": {
                        "environment_name": {
                            "type": "resolve",
                            "resource": "reposget_all_environments",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "10",
                    },
                },
            },
            # Gets a specific variable in an environment.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_environment_variable",
                "table_name": "actions_variable",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/variables/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "actionslist_environment_variables",
                            "field": "name",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "environment_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the level of access that workflows outside of the repository have to actions and reusable workflows in the repository. This endpoint only applies to internal and private repositories. For more information, see "[Allowing access to components in a private repository](https://docs.github.com/enterprise-server@3.9/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-a-private-repository)" and "[Allowing access to components in an internal repository](https://docs.github.com/enterprise-server@3.9/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#allowing-access-to-components-in-an-internal-repository)."  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_workflow_access_to_repository",
                "table_name": "actions_workflow_access_to_repository",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/permissions/access",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the GitHub Advanced Security active committers for an enterprise per repository.  Each distinct user login across all repositories is counted as a single Advanced Security seat, so the `total_advanced_security_committers` is not the sum of active_users for each repository.  The total number of repositories with committer information is tracked by the `total_count` field.
            {
                "name": "billingget_github_advanced_security_billing_ghe",
                "table_name": "advanced_security_active_committers_repository",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/enterprises/{enterprise}/settings/billing/advanced-security",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets the GitHub Advanced Security active committers for an organization per repository.  Each distinct user login across all repositories is counted as a single Advanced Security seat, so the `total_advanced_security_committers` is not the sum of advanced_security_committers for each repository.  If this organization defers to an enterprise for billing, the `total_advanced_security_committers` returned from the organization API may include some users that are in more than one organization, so they will only consume a single Advanced Security seat at the enterprise level.  The total number of repositories with committer information is tracked by the `total_count` field.
            {
                "name": "billingget_github_advanced_security_billing_org",
                "table_name": "advanced_security_active_committers_repository",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/orgs/{org}/settings/billing/advanced-security",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets the current message and expiration date of the global announcement banner in your enterprise.
            {
                "name": "enterprise_adminget_announcement",
                "table_name": "announcement",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/announcement",
                },
            },
            # Gets the announcement banner currently set for the organization. Only returns the announcement banner set at the organization level. Organization members may also see an enterprise-level announcement banner. To get an announcement banner displayed at the enterprise level, use the enterprise-level endpoint.
            {
                "name": "announcement_bannersget_announcement_banner_for_org",
                "table_name": "announcement_banner",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/announcement",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the GitHub App associated with the authentication credentials used. To see how many app installations are associated with this GitHub App, see the `installations_count` in the response. For more details about your app's installations, see the "[List installations for the authenticated app](https://docs.github.com/enterprise-server@3.9/rest/apps/apps#list-installations-for-the-authenticated-app)" endpoint.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_authenticated",
                "table_name": "app",
                "endpoint": {
                    "data_selector": "events",
                    "path": "/app",
                },
            },
            # **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations/), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.9/developers/apps/authorizing-oauth-apps#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).  You can use this API to list the set of OAuth applications that have been granted access to your account. Unlike the [list your authorizations](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations#list-your-authorizations) API, this API does not manage individual tokens. This API will return one entry for each OAuth application that has been granted access to your account, regardless of the number of tokens an application has generated for your user. The list of OAuth applications returned matches what is shown on [the application authorizations settings screen within GitHub](https://github.com/settings/applications#authorized). The `scopes` returned are the union of scopes authorized for the application. For example, if an application has one token with `repo` scope and another token with `user` scope, the grant will return `["repo", "user"]`.
            {
                "name": "oauth_authorizationslist_grants",
                "table_name": "application_grant",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/applications/grants",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "client_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.9/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
            {
                "name": "oauth_authorizationsget_grant",
                "table_name": "application_grant",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/applications/grants/{grant_id}",
                    "params": {
                        "grant_id": {
                            "type": "resolve",
                            "resource": "oauth_authorizationslist_grants",
                            "field": "id",
                        },
                    },
                },
            },
            # Fetches the URL to a migration archive.
            {
                "name": "migrationsdownload_archive_for_org",
                "table_name": "archive",
                "endpoint": {
                    "path": "/orgs/{org}/migrations/{migration_id}/archive",
                    "params": {
                        "migration_id": {
                            "type": "resolve",
                            "resource": "migrationslist_for_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetches the URL to download the migration archive as a `tar.gz` file. Depending on the resources your repository uses, the migration archive can contain JSON files with data for these objects:  *   attachments *   bases *   commit\_comments *   issue\_comments *   issue\_events *   issues *   milestones *   organizations *   projects *   protected\_branches *   pull\_request\_reviews *   pull\_requests *   releases *   repositories *   review\_comments *   schema *   users  The archive will also contain an `attachments` directory that includes all attachment files uploaded to GitHub.com and a `repositories` directory that contains the repository's Git data.
            {
                "name": "migrationsget_archive_for_authenticated_user",
                "table_name": "archive",
                "endpoint": {
                    "path": "/user/migrations/{migration_id}/archive",
                    "params": {
                        "migration_id": {
                            "type": "resolve",
                            "resource": "migrationslist_for_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists all artifacts for a repository.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionslist_artifacts_for_repo",
                "table_name": "artifact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "artifacts",
                    "path": "/repos/{owner}/{repo}/actions/artifacts",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a specific artifact for a workflow run.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_artifact",
                "table_name": "artifact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}",
                    "params": {
                        "artifact_id": {
                            "type": "resolve",
                            "resource": "actionslist_artifacts_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a redirect URL to download an archive for a repository. This URL expires after 1 minute. Look for `Location:` in the response header to find the URL for the download. The `:archive_format` must be `zip`.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsdownload_artifact",
                "table_name": "artifact",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/actions/artifacts/{artifact_id}/{archive_format}",
                    "params": {
                        "archive_format": {
                            "type": "resolve",
                            "resource": "actionslist_artifacts_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "artifact_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists artifacts for a workflow run.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionslist_workflow_run_artifacts",
                "table_name": "artifact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "artifacts",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/artifacts",
                    "params": {
                        "run_id": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Checks if a user has permission to be assigned to an issue in this repository.  If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.  Otherwise a `404` status code is returned.
            {
                "name": "issuescheck_user_can_be_assigned",
                "table_name": "assignee",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/assignees/{assignee}",
                    "params": {
                        "assignee": {
                            "type": "resolve",
                            "resource": "issueslist_assignees",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Checks if a user has permission to be assigned to a specific issue.  If the `assignee` can be assigned to this issue, a `204` status code with no content is returned.  Otherwise a `404` status code is returned.
            {
                "name": "issuescheck_user_can_be_assigned_to_issue",
                "table_name": "assignee",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}/assignees/{assignee}",
                    "params": {
                        "assignee": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "assignee",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "issue_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the audit log for an enterprise.  The authenticated user must be an enterprise admin to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminget_audit_log",
                "table_name": "audit_log_event",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/audit-log",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "phrase": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Gets the audit log for an organization. For more information, see "[Reviewing the audit log for your organization](https://docs.github.com/enterprise-server@3.9/github/setting-up-and-managing-organizations-and-teams/reviewing-the-audit-log-for-your-organization)."  By default, the response includes up to 30 events from the past three months. Use the `phrase` parameter to filter results and retrieve older events. For example, use the `phrase` parameter with the `created` qualifier to filter events based on when the events occurred. For more information, see "[Reviewing the audit log for your organization](https://docs.github.com/enterprise-server@3.9/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/reviewing-the-audit-log-for-your-organization#searching-the-audit-log)."  Use pagination to retrieve fewer or more than 30 events. For more information, see "[Using pagination in the REST API](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api)."  The authenticated user must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:audit_log` scope to use this endpoint.
            {
                "name": "orgsget_audit_log",
                "table_name": "audit_log_event",
                "primary_key": "org",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/audit-log",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "phrase": "OPTIONAL_CONFIG",
                        # "include": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "order": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists personal access tokens for all users, including admin users.
            {
                "name": "enterprise_adminlist_personal_access_tokens",
                "table_name": "authorization",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/tokens",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.9/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
            {
                "name": "oauth_authorizationslist_authorizations",
                "table_name": "authorization",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/authorizations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "client_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Deprecation Notice:** GitHub Enterprise Server will discontinue the [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations), which is used by integrations to create personal access tokens and OAuth tokens, and you must now create these tokens using our [web application flow](https://docs.github.com/enterprise-server@3.9/apps/building-oauth-apps/authorizing-oauth-apps/#web-application-flow). The [OAuth Authorizations API](https://docs.github.com/enterprise-server@3.9/rest/oauth-authorizations/oauth-authorizations) will be removed on November, 13, 2020. For more information, including scheduled brownouts, see the [blog post](https://developer.github.com/changes/2020-02-14-deprecating-oauth-auth-endpoint/).
            {
                "name": "oauth_authorizationsget_authorization",
                "table_name": "authorization",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/authorizations/{authorization_id}",
                    "params": {
                        "authorization_id": {
                            "type": "resolve",
                            "resource": "oauth_authorizationslist_authorizations",
                            "field": "id",
                        },
                    },
                },
            },
            # Gets all autolinks that are configured for a repository.  Information about autolinks are only available to repository administrators.
            {
                "name": "reposlist_autolinks",
                "table_name": "autolink",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/autolinks",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This returns a single autolink reference by ID that was configured for the given repository.  Information about autolinks are only available to repository administrators.
            {
                "name": "reposget_autolink",
                "table_name": "autolink",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/autolinks/{autolink_id}",
                    "params": {
                        "autolink_id": {
                            "type": "resolve",
                            "resource": "reposlist_autolinks",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the authenticated user's gists or if called anonymously, this endpoint returns all public gists:
            {
                "name": "gistslist",
                "table_name": "base_gist",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List public gists sorted by most recently updated to least recently updated.  Note: With [pagination](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api), you can fetch up to 3000 gists. For example, you can fetch 100 pages with 30 gists per page or 30 pages with 100 gists per page.
            {
                "name": "gistslist_public",
                "table_name": "base_gist",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/public",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the authenticated user's starred gists:
            {
                "name": "gistslist_starred",
                "table_name": "base_gist",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/starred",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists public gists for the specified user:
            {
                "name": "gistslist_for_user",
                "table_name": "base_gist",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/gists",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # The `content` in the response will always be Base64 encoded.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw blob data. - **`application/vnd.github+json`**: Returns a JSON representation of the blob with `content` as a base64 encoded string. This is the default if no media type is specified.  **Note** This endpoint supports blobs up to 100 megabytes in size.
            {
                "name": "gitget_blob",
                "table_name": "blob",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/git/blobs/{file_sha}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "file_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Returns all branches where the given commit SHA is the HEAD, or latest commit for the branch.
            {
                "name": "reposlist_branches_for_head_commit",
                "table_name": "branch_short",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "reposget_branch",
                "table_name": "branch_with_protection",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the GitHub Actions caches for a repository.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_actions_cache_list",
                "table_name": "cach",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "actions_caches",
                    "path": "/repos/{owner}/{repo}/actions/caches",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "ref": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "sort": "last_accessed_at",
                        # "direction": "desc",
                    },
                },
            },
            # Lists the status of each repository cache replica.
            {
                "name": "reposlist_cache_info",
                "table_name": "cach",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/replicas/caches",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists annotations for a check run using the annotation `id`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.
            {
                "name": "checkslist_annotations",
                "table_name": "check_annotation",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "check_run_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single check run using its `id`.  **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.
            {
                "name": "checksget",
                "table_name": "check_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/check-runs/{check_run_id}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "check_run_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists check runs for a check suite using its `id`.  **Note:** The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.
            {
                "name": "checkslist_for_suite",
                "table_name": "check_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "check_runs",
                    "path": "/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "check_suite_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "check_name": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "filter": "latest",
                        # "per_page": "30",
                    },
                },
            },
            # Lists check runs for a commit ref. The `ref` can be a SHA, branch name, or a tag name.  **Note:** The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array.  If there are more than 1000 check suites on a single git reference, this endpoint will limit check runs to the 1000 most recent check suites. To iterate over all possible check runs, use the [List check suites for a Git reference](https://docs.github.com/enterprise-server@3.9/rest/reference/checks#list-check-suites-for-a-git-reference) endpoint and provide the `check_suite_id` parameter to the [List check runs in a check suite](https://docs.github.com/enterprise-server@3.9/rest/reference/checks#list-check-runs-in-a-check-suite) endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.
            {
                "name": "checkslist_for_ref",
                "table_name": "check_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "check_runs",
                    "path": "/repos/{owner}/{repo}/commits/{ref}/check-runs",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "check_name": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "filter": "latest",
                        # "per_page": "30",
                        # "app_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a single check suite using its `id`.  **Note:** The Checks API only looks for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.
            {
                "name": "checksget_suite",
                "table_name": "check_suite",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/check-suites/{check_suite_id}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "check_suite_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists check suites for a commit `ref`. The `ref` can be a SHA, branch name, or a tag name.  **Note:** The endpoints to manage checks only look for pushes in the repository where the check suite or check run were created. Pushes to a branch in a forked repository are not detected and return an empty `pull_requests` array and a `null` value for `head_branch`.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint on a private repository.
            {
                "name": "checkslist_suites_for_ref",
                "table_name": "check_suite",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "check_suites",
                    "path": "/repos/{owner}/{repo}/commits/{ref}/check-suites",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "app_id": "OPTIONAL_CONFIG",
                        # "check_name": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Returns a weekly aggregate of the number of additions and deletions pushed to a repository.
            {
                "name": "reposget_code_frequency_stats",
                "table_name": "code_frequency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/stats/code_frequency",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Each array contains the day number, hour number, and number of commits:  *   `0-6`: Sunday - Saturday *   `0-23`: Hour of day *   Number of commits  For example, `[2, 14, 25]` indicates that there were 25 total commits, during the 2:00pm hour on Tuesdays. All times are based on the time zone of individual commits.
            {
                "name": "reposget_punch_card_stats",
                "table_name": "code_frequency_stat",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/stats/punch_card",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns array of all GitHub's codes of conduct.
            {
                "name": "codes_of_conductget_all_codes_of_conduct",
                "table_name": "code_of_conduct",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/codes_of_conduct",
                },
            },
            # Returns information about the specified GitHub code of conduct.
            {
                "name": "codes_of_conductget_conduct_code",
                "table_name": "code_of_conduct",
                "primary_key": "key",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/codes_of_conduct/{key}",
                    "params": {
                        "key": {
                            "type": "resolve",
                            "resource": "codes_of_conductget_all_codes_of_conduct",
                            "field": "key",
                        },
                    },
                },
            },
            # Gets a single code scanning alert.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanningget_alert",
                "table_name": "code_scanning_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "alert_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all instances of the specified code scanning alert.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanninglist_alert_instances",
                "table_name": "code_scanning_alert_instance",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/code-scanning/alerts/{alert_number}/instances",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "alert_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "ref": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists code scanning alerts.  The response includes a `most_recent_instance` object. This provides details of the most recent instance of this alert for the default branch (or for the specified Git reference if you used `ref` in the request).  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanninglist_alerts_for_repo",
                "table_name": "code_scanning_alert_items",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/code-scanning/alerts",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "tool_name": "OPTIONAL_CONFIG",
                        # "tool_guid": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "ref": "OPTIONAL_CONFIG",
                        # "direction": "desc",
                        # "sort": "created",
                        # "state": "OPTIONAL_CONFIG",
                        # "severity": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists the details of all code scanning analyses for a repository, starting with the most recent. The response is paginated and you can use the `page` and `per_page` parameters to list the analyses you're interested in. By default 30 analyses are listed per page.  The `rules_count` field in the response give the number of rules that were run in the analysis. For very old analyses this data is not available, and `0` is returned in this field.  **Deprecation notice**: The `tool_name` field is deprecated and will, in future, not be included in the response for this endpoint. The example response reflects this change. The tool name can now be found inside the `tool` field.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanninglist_recent_analyses",
                "table_name": "code_scanning_analysis",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/code-scanning/analyses",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "tool_name": "OPTIONAL_CONFIG",
                        # "tool_guid": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "ref": "OPTIONAL_CONFIG",
                        # "sarif_id": "OPTIONAL_CONFIG",
                        # "direction": "desc",
                        # "sort": "created",
                    },
                },
            },
            # Gets a specified code scanning analysis for a repository.  The default JSON response contains fields that describe the analysis. This includes the Git reference and commit SHA to which the analysis relates, the datetime of the analysis, the name of the code scanning tool, and the number of alerts.  The `rules_count` field in the default response give the number of rules that were run in the analysis. For very old analyses this data is not available, and `0` is returned in this field.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/sarif+json`**: Instead of returning a summary of the analysis, this endpoint returns a subset of the analysis data that was uploaded. The data is formatted as [SARIF version 2.1.0](https://docs.oasis-open.org/sarif/sarif/v2.1.0/cs01/sarif-v2.1.0-cs01.html). It also returns additional data such as the `github/alertNumber` and `github/alertUrl` properties.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanningget_analysis",
                "table_name": "code_scanning_analysis",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/code-scanning/analyses/{analysis_id}",
                    "params": {
                        "analysis_id": {
                            "type": "resolve",
                            "resource": "code_scanninglist_recent_analyses",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists code scanning alerts for the default branch for all eligible repositories in an enterprise. Eligible repositories are repositories that are owned by organizations that you own or for which you are a security manager. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."  The authenticated user must be a member of the enterprise to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `security_events` or `repo` scope to use this endpoint.
            {
                "name": "code_scanninglist_alerts_for_enterprise",
                "table_name": "code_scanning_organization_alert_items",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/code-scanning/alerts",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "tool_name": "OPTIONAL_CONFIG",
                        # "tool_guid": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "direction": "desc",
                        # "state": "OPTIONAL_CONFIG",
                        # "sort": "created",
                    },
                },
            },
            # Lists code scanning alerts for the default branch for all eligible repositories in an organization. Eligible repositories are repositories that are owned by organizations that you own or for which you are a security manager. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."  The authenticated user must be an owner or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `security_events` or `repo`s cope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanninglist_alerts_for_org",
                "table_name": "code_scanning_organization_alert_items",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/code-scanning/alerts",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "tool_name": "OPTIONAL_CONFIG",
                        # "tool_guid": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "direction": "desc",
                        # "state": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "severity": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets information about a SARIF upload, including the status and the URL of the analysis that was uploaded so that you can retrieve details of the analysis. For more information, see "[Get a code scanning analysis for a repository](/rest/code-scanning/code-scanning#get-a-code-scanning-analysis-for-a-repository)." OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanningget_sarif",
                "table_name": "code_scanning_sarifs_status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/code-scanning/sarifs/{sarif_id}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "sarif_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Searches for query terms inside of a file. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api).  When searching for code, you can get text match metadata for the file **content** and file **path** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you want to find the definition of the `addClass` function inside [jQuery](https://github.com/jquery/jquery) repository, your query would look something like this:  `q=addClass+in:file+language:js+repo:jquery/jquery`  This query searches for the keyword `addClass` within a file's contents. The query limits the search to files where the language is JavaScript in the `jquery/jquery` repository.  Considerations for code search:  Due to the complexity of searching code, there are a few restrictions on how searches are performed:  *   Only the _default branch_ is considered. In most cases, this will be the `master` branch. *   Only files smaller than 384 KB are searchable. *   You must always include at least one search term when searching source code. For example, searching for [`language:go`](https://github.com/search?utf8=%E2%9C%93&q=language%3Ago&type=Code) is not valid, while [`amazing language:go`](https://github.com/search?utf8=%E2%9C%93&q=amazing+language%3Ago&type=Code) is.
            {
                "name": "searchcode",
                "table_name": "code_search_result_item",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/code",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "order": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. Organization members with write, maintain, or admin privileges on the organization-owned repository can use this endpoint.  Team members will include the members of child teams.  The authenticated user must have push access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:org` and `repo` scopes to use this endpoint.
            {
                "name": "reposlist_collaborators",
                "table_name": "collaborator",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/collaborators",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "affiliation": "all",
                        # "permission": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.  Team members will include the members of child teams.  The authenticated user must have push access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:org` and `repo` scopes to use this endpoint.
            {
                "name": "reposcheck_collaborator",
                "table_name": "collaborator",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/collaborators/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "reposlist_collaborators",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |
            {
                "name": "reposlist_commits",
                "table_name": "commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/commits",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sha": "OPTIONAL_CONFIG",
                        # "path": "OPTIONAL_CONFIG",
                        # "author": "OPTIONAL_CONFIG",
                        # "committer": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "until": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "[*].stats.total",
                    },
                },
            },
            # Returns the contents of a single commit reference. You must have `read` access for the repository to use this endpoint.  **Note:** If there are more than 300 files in the commit diff and the default JSON media type is requested, the response will include pagination link headers for the remaining files, up to a limit of 3000 files. Each page contains the static commit information, and the only changes are to the file listing.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)." Pagination query parameters are not supported for these media types.  - **`application/vnd.github.diff`**: Returns the diff of the commit. Larger diffs may time out and return a 5xx status code. - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs with binary data will have no `patch` property. Larger diffs may time out and return a 5xx status code. - **`application/vnd.github.sha`**: Returns the commit's SHA-1 hash. You can use this endpoint to check if a remote reference's SHA-1 hash is the same as your local reference's SHA-1 hash by providing the local SHA-1 reference as the ETag.  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |
            {
                "name": "reposget_commit",
                "table_name": "commit",
                "endpoint": {
                    "data_selector": "parents",
                    "path": "/repos/{owner}/{repo}/commits/{ref}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "stats.total",
                    },
                },
            },
            # Compares two commits against one another. You can compare refs (branches or tags) and commit SHAs in the same repository, or you can compare refs and commit SHAs that exist in different repositories within the same repository network, including fork branches. For more information about how to view a repository's network, see "[Understanding connections between repositories](https://docs.github.com/enterprise-server@3.9/repositories/viewing-activity-and-data-for-your-repository/understanding-connections-between-repositories)."  This endpoint is equivalent to running the `git log BASE..HEAD` command, but it returns commits in a different order. The `git log BASE..HEAD` command returns commits in reverse chronological order, whereas the API returns commits in chronological order.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.diff`**: Returns the diff of the commit. - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs with binary data will have no `patch` property.  The API response includes details about the files that were changed between the two commits. This includes the status of the change (if a file was added, removed, modified, or renamed), and details of the change itself. For example, files with a `renamed` status have a `previous_filename` field showing the previous filename of the file, and files with a `modified` status have a `patch` field showing the changes made to the file.  When calling this endpoint without any paging parameter (`per_page` or `page`), the returned list is limited to 250 commits, and the last commit in the list is the most recent of the entire comparison.  **Working with large comparisons**  To process a response with a large number of commits, use a query parameter (`per_page` or `page`) to paginate the results. When using pagination:  - The list of changed files is only shown on the first page of results, but it includes all changed files for the entire comparison. - The results are returned in chronological order, but the last commit in the returned list may not be the most recent one in the entire set if there are more pages of results.  For more information on working with pagination, see "[Using pagination in the REST API](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api)."  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The `verification` object includes the following fields:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |
            {
                "name": "reposcompare_commits",
                "table_name": "commit",
                "endpoint": {
                    "data_selector": "commits",
                    "path": "/repos/{owner}/{repo}/compare/{basehead}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "basehead": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "base_commit.stats.total",
                    },
                },
            },
            # Lists a maximum of 250 commits for a pull request. To receive a complete commit list for pull requests with more than 250 commits, use the [List commits](https://docs.github.com/enterprise-server@3.9/rest/commits/commits#list-commits) endpoint.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist_commits",
                "table_name": "commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/commits",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "[*].stats.total",
                    },
                },
            },
            # Returns the last year of commit activity grouped by week. The `days` array is a group of commits per day, starting on `Sunday`.
            {
                "name": "reposget_commit_activity_stats",
                "table_name": "commit_activity",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/stats/commit_activity",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the commit comments for a specified repository. Comments are ordered by ascending ID.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "reposlist_commit_comments_for_repo",
                "table_name": "commit_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/comments",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specified commit comment.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "reposget_commit_comment",
                "table_name": "commit_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "reposlist_commit_comments_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the comments for a specified commit.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "reposlist_comments_for_commit",
                "table_name": "commit_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/commits/{commit_sha}/comments",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Find commits via various criteria on the default branch (usually `main`). This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api).  When searching for commits, you can get text match metadata for the **message** field when you provide the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you want to find commits related to CSS in the [octocat/Spoon-Knife](https://github.com/octocat/Spoon-Knife) repository. Your query would look something like this:  `q=repo:octocat/Spoon-Knife+css`
            {
                "name": "searchcommits",
                "table_name": "commit_search_result_item",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/commits",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "order": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Gets the diff of the dependency changes between two commits of a repository, based on the changes to the dependency manifests made in those commits.
            {
                "name": "dependency_graphdiff_range",
                "table_name": "compare",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/dependency-graph/compare/{basehead}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "basehead": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This endpoint allows you to check the status of the most recent configuration process:  Note that you may need to wait several seconds after you start a process before you can check its status.  The different statuses are:  | Status        | Description                       | | ------------- | --------------------------------- | | `PENDING`     | The job has not started yet       | | `CONFIGURING` | The job is running                | | `DONE`        | The job has finished correctly    | | `FAILED`      | The job has finished unexpectedly |
            {
                "name": "enterprise_adminget_configuration_status",
                "table_name": "configcheck",
                "endpoint": {
                    "data_selector": "progress",
                    "path": "/setup/api/configcheck",
                },
            },
            # Gets the contents of a file or directory in a repository. Specify the file path or directory with the `path` parameter. If you omit the `path` parameter, you will receive the contents of the repository's root directory.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw file contents for files and symlinks. - **`application/vnd.github.html+json`**: Returns the file contents in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup). - **`application/vnd.github.object+json`**: Returns the contents in a consistent object format regardless of the content type. For example, instead of an array of objects for a directory, the response will be an object with an `entries` attribute containing the array of objects.  If the content is a directory, the response will be an array of objects, one object for each item in the directory. When listing the contents of a directory, submodules have their "type" specified as "file". Logically, the value _should_ be "submodule". This behavior exists [for backwards compatibility purposes](https://git.io/v1YCW). In the next major version of the API, the type will be returned as "submodule".  If the content is a symlink and the symlink's target is a normal file in the repository, then the API responds with the content of the file. Otherwise, the API responds with an object describing the symlink itself.  If the content is a submodule, the `submodule_git_url` field identifies the location of the submodule repository, and the `sha` identifies a specific commit within the submodule repository. Git uses the given URL when cloning the submodule repository, and checks out the submodule at that specific commit. If the submodule repository is not hosted on github.com, the Git URLs (`git_url` and `_links["git"]`) and the github.com URLs (`html_url` and `_links["html"]`) will have null values.  **Notes**:  - To get a repository's contents recursively, you can [recursively get the tree](https://docs.github.com/enterprise-server@3.9/rest/git/trees#get-a-tree). - This API has an upper limit of 1,000 files for a directory. If you need to retrieve more files, use the [Git Trees API](https://docs.github.com/enterprise-server@3.9/rest/git/trees#get-a-tree). - Download URLs expire and are meant to be used just once. To ensure the download URL does not expire, please use the contents API to obtain a fresh download URL for each download. - If the requested file's size is:   - 1 MB or smaller: All features of this endpoint are supported.   - Between 1-100 MB: Only the `raw` or `object` custom media types are supported. Both will work as normal, except that when using the `object` media type, the `content` field will be an empty string and the `encoding` field will be `"none"`. To get the contents of these larger files, use the `raw` media type.   - Greater than 100 MB: This endpoint is not supported.
            {
                "name": "reposget_content",
                "table_name": "content",
                "primary_key": "path",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/contents/{path}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "path": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ref": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets the preferred README for a repository.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is the default if you do not specify a media type. - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup).
            {
                "name": "reposget_readme",
                "table_name": "content_file",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/readme",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ref": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets the README from a repository directory.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw file contents. This is the default if you do not specify a media type. - **`application/vnd.github.html+json`**: Returns the README in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup).
            {
                "name": "reposget_readme_in_directory",
                "table_name": "content_file",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/readme/{dir}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "dir": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ref": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
            {
                "name": "reposget_all_status_check_contexts",
                "table_name": "context",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks/contexts",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists contributors to the specified repository and sorts them by the number of commits per contributor in descending order. This endpoint may return information that is a few hours old because the GitHub REST API caches contributor data to improve performance.  GitHub identifies contributors by author email address. This endpoint groups contribution counts by GitHub user, which includes all associated email addresses. To improve performance, only the first 500 author email addresses in the repository link to GitHub users. The rest will appear as anonymous contributors without associated GitHub user information.
            {
                "name": "reposlist_contributors",
                "table_name": "contributor",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/contributors",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "anon": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            #  Returns the `total` number of commits authored by the contributor. In addition, the response includes a Weekly Hash (`weeks` array) with the following information:  *   `w` - Start of the week, given as a [Unix timestamp](https://en.wikipedia.org/wiki/Unix_time). *   `a` - Number of additions *   `d` - Number of deletions *   `c` - Number of commits
            {
                "name": "reposget_contributors_stats",
                "table_name": "contributor_activity",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/stats/contributors",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a code scanning default setup configuration.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with private or public repositories, or the `public_repo` scope to use this endpoint with only public repositories.
            {
                "name": "code_scanningget_default_setup",
                "table_name": "default_setup",
                "endpoint": {
                    "data_selector": "languages",
                    "path": "/repos/{owner}/{repo}/code-scanning/default-setup",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "dependabotlist_alerts_for_repo",
                "table_name": "dependabot_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/dependabot/alerts",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "severity": "OPTIONAL_CONFIG",
                        # "ecosystem": "OPTIONAL_CONFIG",
                        # "package": "OPTIONAL_CONFIG",
                        # "manifest": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "per_page": "30",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "first": "30",
                        # "last": "OPTIONAL_CONFIG",
                    },
                },
            },
            # OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "dependabotget_alert",
                "table_name": "dependabot_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/dependabot/alerts/{alert_number}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "alert_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists Dependabot alerts for repositories that are owned by the specified enterprise.  The authenticated user must be a member of the enterprise to use this endpoint.  Alerts are only returned for organizations in the enterprise for which you are an organization owner or a security manager. For more information about security managers, see "[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint.
            {
                "name": "dependabotlist_alerts_for_enterprise",
                "table_name": "dependabot_alert_with_repository",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/dependabot/alerts",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "severity": "OPTIONAL_CONFIG",
                        # "ecosystem": "OPTIONAL_CONFIG",
                        # "package": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "first": "30",
                        # "last": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists Dependabot alerts for an organization.  The authenticated user must be an owner or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "dependabotlist_alerts_for_org",
                "table_name": "dependabot_alert_with_repository",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/dependabot/alerts",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "severity": "OPTIONAL_CONFIG",
                        # "ecosystem": "OPTIONAL_CONFIG",
                        # "package": "OPTIONAL_CONFIG",
                        # "scope": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                        # "first": "30",
                        # "last": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "dependabotget_org_public_key",
                "table_name": "dependabot_public_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/dependabot/secrets/public-key",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets your public key, which you need to encrypt secrets. You need to encrypt a secret before you can create or update secrets. Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint if the repository is private.
            {
                "name": "dependabotget_repo_public_key",
                "table_name": "dependabot_public_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/dependabot/secrets/public-key",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all secrets available in a repository without revealing their encrypted values.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "dependabotlist_repo_secrets",
                "table_name": "dependabot_secret",
                "endpoint": {
                    "data_selector": "secrets",
                    "path": "/repos/{owner}/{repo}/dependabot/secrets",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single repository secret without revealing its encrypted value.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "dependabotget_repo_secret",
                "table_name": "dependabot_secret",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/dependabot/secrets/{secret_name}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "reposlist_deploy_keys",
                "table_name": "deploy_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/keys",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "reposget_deploy_key",
                "table_name": "deploy_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/keys/{key_id}",
                    "params": {
                        "key_id": {
                            "type": "resolve",
                            "resource": "reposlist_deploy_keys",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Simple filtering of deployments is available via query parameters:
            {
                "name": "reposlist_deployments",
                "table_name": "deployment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/deployments",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sha": "none",
                        # "ref": "none",
                        # "task": "none",
                        # "environment": "none",
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "reposget_deployment",
                "table_name": "deployment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/deployments/{deployment_id}",
                    "params": {
                        "deployment_id": {
                            "type": "resolve",
                            "resource": "reposlist_deployments",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the deployment branch policies for an environment.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "reposlist_deployment_branch_policies",
                "table_name": "deployment_branch_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "branch_policies",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies",
                    "params": {
                        "environment_name": {
                            "type": "resolve",
                            "resource": "reposget_all_environments",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a deployment branch policy for an environment.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "reposget_deployment_branch_policy",
                "table_name": "deployment_branch_policy",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}/deployment-branch-policies/{branch_policy_id}",
                    "params": {
                        "branch_policy_id": {
                            "type": "resolve",
                            "resource": "reposlist_deployment_branch_policies",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "environment_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Users with pull access can view deployment statuses for a deployment:
            {
                "name": "reposlist_deployment_statuses",
                "table_name": "deployment_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses",
                    "params": {
                        "deployment_id": {
                            "type": "resolve",
                            "resource": "reposlist_deployments",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Users with pull access can view a deployment status for a deployment:
            {
                "name": "reposget_deployment_status",
                "table_name": "deployment_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/deployments/{deployment_id}/statuses/{status_id}",
                    "params": {
                        "status_id": {
                            "type": "resolve",
                            "resource": "reposlist_deployment_statuses",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "deployment_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the files in a specified pull request.  **Note:** Responses include a maximum of 3000 files. The paginated response returns 30 files per page by default.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist_files",
                "table_name": "diff_entry",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/files",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all of your email addresses, and specifies which one is visible to the public.  OAuth app tokens and personal access tokens (classic) need the `user:email` scope to use this endpoint.
            {
                "name": "userslist_emails_for_authenticated_user",
                "table_name": "email",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/emails",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists your publicly visible email address, which you can set with the [Set primary email visibility for the authenticated user](https://docs.github.com/enterprise-server@3.9/rest/users/emails#set-primary-email-visibility-for-the-authenticated-user) endpoint.  OAuth app tokens and personal access tokens (classic) need the `user:email` scope to use this endpoint.
            {
                "name": "userslist_public_emails_for_authenticated_user",
                "table_name": "email",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/public_emails",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all the emojis available to use on GitHub Enterprise Server.
            {
                "name": "emojisget",
                "table_name": "emoji",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/emojis",
                },
            },
            {
                "name": "enterprise_adminget_comment_stats",
                "table_name": "enterprise_comment_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/comments",
                },
            },
            {
                "name": "enterprise_adminget_gist_stats",
                "table_name": "enterprise_gist_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/gists",
                },
            },
            {
                "name": "enterprise_adminget_hooks_stats",
                "table_name": "enterprise_hook_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/hooks",
                },
            },
            {
                "name": "enterprise_adminget_issue_stats",
                "table_name": "enterprise_issue_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/issues",
                },
            },
            {
                "name": "enterprise_adminget_milestone_stats",
                "table_name": "enterprise_milestone_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/milestones",
                },
            },
            {
                "name": "enterprise_adminget_org_stats",
                "table_name": "enterprise_organization_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/orgs",
                },
            },
            {
                "name": "enterprise_adminget_all_stats",
                "table_name": "enterprise_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/all",
                },
            },
            {
                "name": "enterprise_adminget_pages_stats",
                "table_name": "enterprise_page_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/pages",
                },
            },
            {
                "name": "enterprise_adminget_pull_request_stats",
                "table_name": "enterprise_pull_request_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/pulls",
                },
            },
            {
                "name": "enterprise_adminget_repo_stats",
                "table_name": "enterprise_repository_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/repos",
                },
            },
            # Gets code security and analysis settings for the specified enterprise.  The authenticated user must be an administrator of the enterprise in order to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "secret_scanningget_security_analysis_settings_for_enterprise",
                "table_name": "enterprise_security_analysis_settings",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/code_security_and_analysis",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "enterprise_adminget_user_stats",
                "table_name": "enterprise_user_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/stats/users",
                },
            },
            # Lists the environments for a repository.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "reposget_all_environments",
                "table_name": "environment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "environments",
                    "path": "/repos/{owner}/{repo}/environments",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Note:** To get information about name patterns that branches must match in order to deploy to this environment, see "[Get a deployment branch policy](/rest/deployments/branch-policies#get-a-deployment-branch-policy)."  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "reposget_environment",
                "table_name": "environment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/environments/{environment_name}",
                    "params": {
                        "environment_name": {
                            "type": "resolve",
                            "resource": "reposget_all_environments",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionsget_reviews_for_run",
                "table_name": "environment_approvals",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/approvals",
                    "params": {
                        "run_id": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List any syntax errors that are detected in the CODEOWNERS file.  For more information about the correct CODEOWNERS syntax, see "[About code owners](https://docs.github.com/enterprise-server@3.9/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)."
            {
                "name": "reposcodeowners_errors",
                "table_name": "error",
                "endpoint": {
                    "data_selector": "errors",
                    "path": "/repos/{owner}/{repo}/codeowners/errors",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "ref": "OPTIONAL_CONFIG",
                    },
                },
            },
            # We delay the public events feed by five minutes, which means the most recent event returned by the public events API actually occurred at least five minutes ago.
            {
                "name": "activitylist_public_events",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/events",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "activitylist_public_events_for_repo_network",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/networks/{owner}/{repo}/events",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "activitylist_public_org_events",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/events",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Note**: This API is not built to serve real-time use cases. Depending on the time of day, event latency can be anywhere from 30s to 6h.
            {
                "name": "activitylist_repo_events",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/events",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # If you are authenticated as the given user, you will see your private events. Otherwise, you'll only see public events.
            {
                "name": "activitylist_events_for_authenticated_user",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/events",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # This is the user's organization dashboard. You must be authenticated as the user to view this.
            {
                "name": "activitylist_org_events_for_authenticated_user",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/events/orgs/{org}",
                    "params": {
                        "org": {
                            "type": "resolve",
                            "resource": "activitylist_events_for_authenticated_user",
                            "field": "org",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "activitylist_public_events_for_user",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/events/public",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "activitylist_events_for_authenticated_user",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # These are events that you've received by watching repositories and following users. If you are authenticated as the given user, you will see private events. Otherwise, you'll only see public events.
            {
                "name": "activitylist_received_events_for_user",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/received_events",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "activitylist_received_public_events_for_user",
                "table_name": "event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/received_events/public",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "activitylist_received_events_for_user",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Displays information about the specific group's usage.  Provides a list of the group's external members as well as a list of teams that this group is connected to.  You can manage team membership with your identity provider using Enterprise Managed Users for GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products)" in the GitHub Help documentation.
            {
                "name": "teamsexternal_idp_group_info_for_org",
                "table_name": "external_group",
                "primary_key": "group_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/external-group/{group_id}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists external groups available in an organization. You can query the groups using the `display_name` parameter, only groups with a `group_name` containing the text provided in the `display_name` parameter will be returned.  You can also limit your page results using the `per_page` parameter. GitHub Enterprise Server generates a url-encoded `page` token using a cursor value for where the next page begins. For more information on cursor pagination, see "[Offset and Cursor Pagination explained](https://dev.to/jackmarchant/offset-and-cursor-pagination-explained-b89)."  You can manage team membership with your identity provider using Enterprise Managed Users for GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products)" in the GitHub Help documentation.
            {
                "name": "teamslist_external_idp_groups_for_org",
                "table_name": "external_group",
                "endpoint": {
                    "data_selector": "groups",
                    "path": "/orgs/{org}/external-groups",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "display_name": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists a connection between a team and an external group.  You can manage team membership with your identity provider using Enterprise Managed Users for GitHub Enterprise Cloud. For more information, see "[GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products)" in the GitHub Help documentation.
            {
                "name": "teamslist_linked_external_idp_groups_to_team_for_org",
                "table_name": "external_group",
                "endpoint": {
                    "data_selector": "groups",
                    "path": "/orgs/{org}/teams/{team_slug}/external-groups",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the feeds available to the authenticated user. The response provides a URL for each feed. You can then get a specific feed by sending a request to one of the feed URLs.  *   **Timeline**: The GitHub Enterprise Server global public timeline *   **User**: The public timeline for any user, using `uri_template`. For more information, see "[Hypermedia](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)." *   **Current user public**: The public timeline for the authenticated user *   **Current user**: The private timeline for the authenticated user *   **Current user actor**: The private timeline for activity created by the authenticated user *   **Current user organizations**: The private timeline for the organizations the authenticated user is a member of. *   **Security advisories**: A collection of public announcements that provide information about security-related vulnerabilities in software on GitHub Enterprise Server.  By default, timeline resources are returned in JSON. You can specify the `application/atom+xml` type in the `Accept` header to return timeline resources in Atom format. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  **Note**: Private feeds are only returned when [authenticating via Basic Auth](https://docs.github.com/enterprise-server@3.9/rest/overview/other-authentication-methods#basic-authentication) since current feed URIs use the older, non revocable auth tokens.
            {
                "name": "activityget_feeds",
                "table_name": "feed",
                "endpoint": {
                    "data_selector": "current_user_organization_urls",
                    "path": "/feeds",
                },
            },
            {
                "name": "userscheck_person_is_followed_by_authenticated",
                "table_name": "following",
                "endpoint": {
                    "path": "/user/following/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist_followed_by_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            {
                "name": "userscheck_following_for_user",
                "table_name": "following",
                "endpoint": {
                    "path": "/users/{username}/following/{target_user}",
                    "params": {
                        "target_user": {
                            "type": "resolve",
                            "resource": "userslist_following_for_user",
                            "field": "id",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # The `parent` and `source` objects are present when the repository is a fork. `parent` is the repository this repository was forked from, `source` is the ultimate source for the network.  **Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."
            {
                "name": "reposget",
                "table_name": "full_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the comments on a gist.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.
            {
                "name": "gistslist_comments",
                "table_name": "gist_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/{gist_id}/comments",
                    "params": {
                        "gist_id": {
                            "type": "resolve",
                            "resource": "gistslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a comment on a gist.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.
            {
                "name": "gistsget_comment",
                "table_name": "gist_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/{gist_id}/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "gistslist_comments",
                            "field": "id",
                        },
                        "gist_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "gistslist_commits",
                "table_name": "gist_commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/{gist_id}/commits",
                    "params": {
                        "gist_id": {
                            "type": "resolve",
                            "resource": "gistslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "[*].change_status.total",
                    },
                },
            },
            # Gets a specified gist.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.
            {
                "name": "gistsget",
                "table_name": "gist_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/{gist_id}",
                    "params": {
                        "gist_id": {
                            "type": "resolve",
                            "resource": "gistslist",
                            "field": "id",
                        },
                    },
                },
            },
            {
                "name": "gistslist_forks",
                "table_name": "gist_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/{gist_id}/forks",
                    "params": {
                        "gist_id": {
                            "type": "resolve",
                            "resource": "gistslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page",
                        "total_path": "[*].history.[*].change_status.total",
                    },
                },
            },
            # Gets a specified gist revision.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown. This is the default if you do not pass any specific media type. - **`application/vnd.github.base64+json`**: Returns the base64-encoded contents. This can be useful if your gist contains any invalid UTF-8 sequences.
            {
                "name": "gistsget_revision",
                "table_name": "gist_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gists/{gist_id}/{sha}",
                    "params": {
                        "sha": {
                            "type": "resolve",
                            "resource": "gistslist",
                            "field": "id",
                        },
                        "gist_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a Git [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).  To get the contents of a commit, see "[Get a commit](/rest/commits/commits#get-a-commit)."  **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in the table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |
            {
                "name": "gitget_commit",
                "table_name": "git_commit",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/git/commits/{commit_sha}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns an array of references from your Git database that match the supplied name. The `:ref` in the URL must be formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags. If the `:ref` doesn't exist in the repository, but existing refs start with `:ref`, they will be returned as an array.  When you use this endpoint without providing a `:ref`, it will return an array of all the references from your Git database, including notes and stashes if they exist on the server. Anything in the namespace is returned, not just `heads` and `tags`.  **Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".  If you request matching references for a branch named `feature` but the branch `feature` doesn't exist, the response can still include other matching head refs that start with the word `feature`, such as `featureA` and `featureB`.
            {
                "name": "gitlist_matching_refs",
                "table_name": "git_ref",
                "primary_key": "ref",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/git/matching-refs/{ref}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a single reference from your Git database. The `:ref` in the URL must be formatted as `heads/<branch name>` for branches and `tags/<tag name>` for tags. If the `:ref` doesn't match an existing ref, a `404` is returned.  **Note:** You need to explicitly [request a pull request](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#get-a-pull-request) to trigger a test merge commit, which checks the mergeability of pull requests. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".
            {
                "name": "gitget_ref",
                "table_name": "git_ref",
                "primary_key": "ref",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/git/ref/{ref}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Signature verification object**  The response will include a `verification` object that describes the result of verifying the commit's signature. The following fields are included in the `verification` object:  | Name | Type | Description | | ---- | ---- | ----------- | | `verified` | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified. | | `reason` | `string` | The reason for verified value. Possible values and their meanings are enumerated in table below. | | `signature` | `string` | The signature that was extracted from the commit. | | `payload` | `string` | The value that was signed. |  These are the possible values for `reason` in the `verification` object:  | Value | Description | | ----- | ----------- | | `expired_key` | The key that made the signature is expired. | | `not_signing_key` | The "signing" flag is not among the usage flags in the GPG key that made the signature. | | `gpgverify_error` | There was an error communicating with the signature verification service. | | `gpgverify_unavailable` | The signature verification service is currently unavailable. | | `unsigned` | The object does not include a signature. | | `unknown_signature_type` | A non-PGP signature was found in the commit. | | `no_user` | No user was associated with the `committer` email address in the commit. | | `unverified_email` | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. | | `bad_email` | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature. | | `unknown_key` | The key that made the signature has not been registered with any user's account. | | `malformed_signature` | There was an error parsing the signature. | | `invalid` | The signature could not be cryptographically verified using the key whose key-id was found in the signature. | | `valid` | None of the above errors applied, so the signature is considered to be verified. |
            {
                "name": "gitget_tag",
                "table_name": "git_tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/git/tags/{tag_sha}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "tag_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a single tree using the SHA1 value or ref name for that tree.  If `truncated` is `true` in the response then the number of items in the `tree` array exceeded our maximum limit. If you need to fetch more items, use the non-recursive method of fetching trees, and fetch one sub-tree at a time.   **Note**: The limit for the `tree` array is 100,000 entries with a maximum size of 7 MB when using the `recursive` parameter.
            {
                "name": "gitget_tree",
                "table_name": "git_tree",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/git/trees/{tree_sha}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "tree_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "recursive": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the content of a gitignore template.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw .gitignore contents.
            {
                "name": "gitignoreget_template",
                "table_name": "gitignore_template",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gitignore/templates/{name}",
                    "params": {
                        "name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "enterprise_adminlist_global_webhooks",
                "table_name": "global_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/hooks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "enterprise_adminget_global_webhook",
                "table_name": "global_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/hooks/{hook_id}",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_global_webhooks",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists the current user's GPG keys.  OAuth app tokens and personal access tokens (classic) need the `read:gpg_key` scope to use this endpoint.
            {
                "name": "userslist_gpg_keys_for_authenticated_user",
                "table_name": "gpg_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/gpg_keys",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # View extended details for a single GPG key.  OAuth app tokens and personal access tokens (classic) need the `read:gpg_key` scope to use this endpoint.
            {
                "name": "usersget_gpg_key_for_authenticated_user",
                "table_name": "gpg_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/gpg_keys/{gpg_key_id}",
                    "params": {
                        "gpg_key_id": {
                            "type": "resolve",
                            "resource": "userslist_gpg_keys_for_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists the GPG keys for a user. This information is accessible by anyone.
            {
                "name": "userslist_gpg_keys_for_user",
                "table_name": "gpg_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/gpg_keys",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Note:** The SCIM API endpoints for enterprise accounts are currently in *private* beta and are subject to change.  Lists provisioned SCIM groups in an enterprise.  You can improve query search time by using the `excludedAttributes` query parameter with a value of `members` to exclude members from the response.
            {
                "name": "enterprise_adminlist_provisioned_groups_enterprise",
                "table_name": "group",
                "endpoint": {
                    "data_selector": "schemas",
                    "path": "/scim/v2/enterprises/{enterprise}/Groups",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "excludedAttributes": "OPTIONAL_CONFIG",
                        # "startIndex": "1",
                        # "count": "30",
                    },
                },
            },
            # Lists webhooks for a repository. `last response` may return null if there have not been any deliveries within 30 days.
            {
                "name": "reposlist_webhooks",
                "table_name": "hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/hooks",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Returns a webhook configured in a repository. To get only the webhook `config` properties, see "[Get a webhook configuration for a repository](/rest/webhooks/repo-config#get-a-webhook-configuration-for-a-repository)."
            {
                "name": "reposget_webhook",
                "table_name": "hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/hooks/{hook_id}",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "reposlist_webhooks",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a delivery for the webhook configured for a GitHub App.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_webhook_delivery",
                "table_name": "hook_delivery",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/app/hook/deliveries/{delivery_id}",
                    "params": {
                        "delivery_id": {
                            "type": "resolve",
                            "resource": "appslist_webhook_deliveries",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a delivery for a webhook configured in an organization.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.
            {
                "name": "orgsget_webhook_delivery",
                "table_name": "hook_delivery",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/hooks/{hook_id}/deliveries/{delivery_id}",
                    "params": {
                        "delivery_id": {
                            "type": "resolve",
                            "resource": "orgslist_webhook_deliveries",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "hook_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a delivery for a webhook configured in a repository.
            {
                "name": "reposget_webhook_delivery",
                "table_name": "hook_delivery",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}",
                    "params": {
                        "delivery_id": {
                            "type": "resolve",
                            "resource": "reposlist_webhook_deliveries",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "hook_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of webhook deliveries for the webhook configured for a GitHub App.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appslist_webhook_deliveries",
                "table_name": "hook_delivery_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/app/hook/deliveries",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "redelivery": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of webhook deliveries for a webhook configured in an organization.  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.
            {
                "name": "orgslist_webhook_deliveries",
                "table_name": "hook_delivery_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/hooks/{hook_id}/deliveries",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "orgslist_webhooks",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "redelivery": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of webhook deliveries for a webhook configured in a repository.
            {
                "name": "reposlist_webhook_deliveries",
                "table_name": "hook_delivery_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/hooks/{hook_id}/deliveries",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "reposlist_webhooks",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "redelivery": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Provides hovercard information. You can find out more about someone in relation to their pull requests, issues, repositories, and organizations.    The `subject_type` and `subject_id` parameters provide context for the person's hovercard, which returns more information than without the parameters. For example, if you wanted to find out more about `octocat` who owns the `Spoon-Knife` repository, you would use a `subject_type` value of `repository` and a `subject_id` value of `1300192` (the ID of the `Spoon-Knife` repository).  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "usersget_context_for_user",
                "table_name": "hovercard",
                "endpoint": {
                    "data_selector": "contexts",
                    "path": "/users/{username}/hovercard",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "subject_type": "OPTIONAL_CONFIG",
                        # "subject_id": "OPTIONAL_CONFIG",
                    },
                },
            },
            # The permissions the installation has are included under the `permissions` key.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appslist_installations",
                "table_name": "installation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/app/installations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "since": "OPTIONAL_CONFIG",
                        # "outdated": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Enables an authenticated GitHub App to find an installation's information using the installation id.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_installation",
                "table_name": "installation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/app/installations/{installation_id}",
                    "params": {
                        "installation_id": {
                            "type": "resolve",
                            "resource": "appslist_installations",
                            "field": "id",
                        },
                    },
                },
            },
            # Enables an authenticated GitHub App to find the organization's installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_org_installation",
                "table_name": "installation",
                "endpoint": {
                    "data_selector": "events",
                    "path": "/orgs/{org}/installation",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all GitHub Apps in an organization. The installation count includes all GitHub Apps installed on repositories in the organization.  The authenticated user must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:read` scope to use this endpoint.
            {
                "name": "orgslist_app_installations",
                "table_name": "installation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "installations",
                    "path": "/orgs/{org}/installations",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Enables an authenticated GitHub App to find the repository's installation information. The installation's account type will be either an organization or a user account, depending which account the repository belongs to.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_repo_installation",
                "table_name": "installation",
                "endpoint": {
                    "data_selector": "events",
                    "path": "/repos/{owner}/{repo}/installation",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists installations of your GitHub App that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  You can find the permissions for the installation under the `permissions` key.
            {
                "name": "appslist_installations_for_authenticated_user",
                "table_name": "installation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "installations",
                    "path": "/user/installations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Enables an authenticated GitHub App to find the user’s installation information.  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_user_installation",
                "table_name": "installation",
                "endpoint": {
                    "data_selector": "events",
                    "path": "/users/{username}/installation",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                    },
                },
            },
            # **Note**: The `:app_slug` is just the URL-friendly name of your GitHub App. You can find this on the settings page for your GitHub App (e.g., `https://github.com/settings/apps/:app_slug`).
            {
                "name": "appsget_by_slug",
                "table_name": "integration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/apps/{app_slug}",
                    "params": {
                        "app_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the GitHub Apps that have push access to this branch. Only GitHub Apps that are installed on the repository and that have been granted write access to the repository contents can be added as authorized actors on a protected branch.
            {
                "name": "reposget_apps_with_access_to_protected_branch",
                "table_name": "integration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
                    "params": {
                        "branch": {
                            "type": "resolve",
                            "resource": "reposget_access_restrictions",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all the pending installation requests for the authenticated GitHub App.
            {
                "name": "appslist_installation_requests_for_authenticated_app",
                "table_name": "integration_installation_request",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/app/installation-requests",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List issues assigned to the authenticated user across all visible repositories including owned repositories, member repositories, and organization repositories. You can use the `filter` query parameter to fetch issues that are not necessarily assigned to you.  **Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#list-pull-requests)" endpoint.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issueslist",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/issues",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "assigned",
                        # "state": "open",
                        # "labels": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "since": "OPTIONAL_CONFIG",
                        # "collab": "OPTIONAL_CONFIG",
                        # "orgs": "OPTIONAL_CONFIG",
                        # "owned": "OPTIONAL_CONFIG",
                        # "pulls": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List issues in an organization assigned to the authenticated user.  **Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#list-pull-requests)" endpoint.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issueslist_for_org",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/issues",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "assigned",
                        # "state": "open",
                        # "labels": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List issues in a repository. Only open issues will be listed.  **Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#list-pull-requests)" endpoint.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issueslist_for_repo",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "milestone": "OPTIONAL_CONFIG",
                        # "state": "open",
                        # "assignee": "OPTIONAL_CONFIG",
                        # "creator": "OPTIONAL_CONFIG",
                        # "mentioned": "OPTIONAL_CONFIG",
                        # "labels": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # The API returns a [`301 Moved Permanently` status](https://docs.github.com/enterprise-server@3.9/rest/guides/best-practices-for-using-the-rest-api#follow-redirects) if the issue was [transferred](https://docs.github.com/enterprise-server@3.9/articles/transferring-an-issue-to-another-repository/) to another repository. If the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API returns a `404 Not Found` status. If the issue was deleted from a repository where the authenticated user has read access, the API returns a `410 Gone` status. To receive webhook events for transferred and deleted issues, subscribe to the [`issues`](https://docs.github.com/enterprise-server@3.9/webhooks/event-payloads/#issues) webhook.  **Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#list-pull-requests)" endpoint.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issuesget",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}",
                    "params": {
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List issues across owned and member repositories assigned to the authenticated user.  **Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull request id, use the "[List pull requests](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#list-pull-requests)" endpoint.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issueslist_for_authenticated_user",
                "table_name": "issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/issues",
                    "params": {
                        # the parameters below can optionally be configured
                        # "filter": "assigned",
                        # "state": "open",
                        # "labels": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # You can use the REST API to list comments on issues and pull requests for a repository. Every pull request is an issue, but not every issue is a pull request.  By default, issue comments are ordered by ascending ID.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issueslist_comments_for_repo",
                "table_name": "issue_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/comments",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sort": "created",
                        # "direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # You can use the REST API to get comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issuesget_comment",
                "table_name": "issue_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "issueslist_comments_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # You can use the REST API to list comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.  Issue comments are ordered by ascending ID.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "issueslist_comments",
                "table_name": "issue_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}/comments",
                    "params": {
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists events for a repository.
            {
                "name": "issueslist_events_for_repo",
                "table_name": "issue_event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/events",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single event by the event id.
            {
                "name": "issuesget_event",
                "table_name": "issue_event",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/events/{event_id}",
                    "params": {
                        "event_id": {
                            "type": "resolve",
                            "resource": "issueslist_events_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all events for an issue.
            {
                "name": "issueslist_events",
                "table_name": "issue_event_for_issue",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}/events",
                    "params": {
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Find issues by state and keyword. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api).  When searching for issues, you can get text match metadata for the issue **title**, issue **body**, and issue **comment body** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you want to find the oldest unresolved Python bugs on Windows. Your query might look something like this.  `q=windows+label:bug+language:python+state:open&sort=created&order=asc`  This query searches for the keyword `windows`, within any open issue that is labeled as `bug`. The search runs across repositories whose primary language is Python. The results are sorted by creation date in ascending order, which means the oldest issues appear first in the search results.  **Note:** For requests made by GitHub Apps with a user access token, you can't retrieve a combination of issues and pull requests in a single query. Requests that don't include the `is:issue` or `is:pull-request` qualifier will receive an HTTP `422 Unprocessable Entity` response. To get results for both issues and pull requests, you must send separate queries for issues and pull requests. For more information about the `is` qualifier, see "[Searching only issues or pull requests](https://docs.github.com/enterprise-server@3.9/github/searching-for-information-on-github/searching-issues-and-pull-requests#search-only-issues-or-pull-requests)."
            {
                "name": "searchissues_and_pull_requests",
                "table_name": "issue_search_result_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/issues",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "order": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific job in a workflow run.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_job_for_workflow_run",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/jobs/{job_id}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "job_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists jobs for a specific workflow run attempt. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint  with a private repository.
            {
                "name": "actionslist_jobs_for_workflow_run_attempt",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "jobs",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/jobs",
                    "params": {
                        "attempt_number": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "run_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists jobs for a workflow run. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionslist_jobs_for_workflow_run",
                "table_name": "job",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "jobs",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/jobs",
                    "params": {
                        "run_id": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "latest",
                        # "per_page": "30",
                    },
                },
            },
            # Lists the public SSH keys for the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `read:public_key` scope to use this endpoint.
            {
                "name": "userslist_public_ssh_keys_for_authenticated_user",
                "table_name": "key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/keys",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # View extended details for a single public SSH key.  OAuth app tokens and personal access tokens (classic) need the `read:public_key` scope to use this endpoint.
            {
                "name": "usersget_public_ssh_key_for_authenticated_user",
                "table_name": "key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/keys/{key_id}",
                    "params": {
                        "key_id": {
                            "type": "resolve",
                            "resource": "userslist_public_ssh_keys_for_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists the _verified_ public SSH keys for a user. This is accessible by anyone.
            {
                "name": "userslist_public_keys_for_user",
                "table_name": "key_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/keys",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all labels for an issue.
            {
                "name": "issueslist_labels_on_issue",
                "table_name": "label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}/labels",
                    "params": {
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all labels for a repository.
            {
                "name": "issueslist_labels_for_repo",
                "table_name": "label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/labels",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a label using the given name.
            {
                "name": "issuesget_label",
                "table_name": "label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/labels/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "issueslist_labels_for_repo",
                            "field": "name",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists labels for issues in a milestone.
            {
                "name": "issueslist_labels_for_milestone",
                "table_name": "label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/milestones/{milestone_number}/labels",
                    "params": {
                        "milestone_number": {
                            "type": "resolve",
                            "resource": "issueslist_milestones",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Find labels in a repository with names or descriptions that match search keywords. Returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api).  When searching for labels, you can get text match metadata for the label **name** and **description** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you want to find labels in the `linguist` repository that match `bug`, `defect`, or `enhancement`. Your query might look like this:  `q=bug+defect+enhancement&repository_id=64778136`  The labels that best match the query appear first in the search results.
            {
                "name": "searchlabels",
                "table_name": "label_search_result_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/labels",
                    "params": {
                        "repository_id": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "order": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Lists languages for the specified repository. The value shown for each language is the number of bytes of code written in that language.
            {
                "name": "reposlist_languages",
                "table_name": "language",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/languages",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets information about a specific license. For more information, see "[Licensing a repository ](https://docs.github.com/enterprise-server@3.9/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)."
            {
                "name": "licensesget",
                "table_name": "license",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/licenses/{license}",
                    "params": {
                        "license": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # This method returns the contents of the repository's license file, if one is detected.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw contents of the license. - **`application/vnd.github.html+json`**: Returns the license contents in HTML. Markup languages are rendered to HTML using GitHub's open-source [Markup library](https://github.com/github/markup).
            {
                "name": "licensesget_for_repo",
                "table_name": "license_content",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/license",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "enterprise_adminget_license_information",
                "table_name": "license_info",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprise/settings/license",
                },
            },
            # Lists the most commonly used licenses on GitHub. For more information, see "[Licensing a repository ](https://docs.github.com/enterprise-server@3.9/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)."
            {
                "name": "licensesget_all_commonly_used",
                "table_name": "license_simple",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/licenses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "featured": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a redirect URL to download a plain text file of logs for a workflow job. This link expires after 1 minute. Look for `Location:` in the response header to find the URL for the download.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsdownload_job_logs_for_workflow_run",
                "table_name": "log",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/actions/jobs/{job_id}/logs",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "job_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a redirect URL to download an archive of log files for a specific workflow run attempt. This link expires after 1 minute. Look for `Location:` in the response header to find the URL for the download.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsdownload_workflow_run_attempt_logs",
                "table_name": "log",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}/logs",
                    "params": {
                        "attempt_number": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "run_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a redirect URL to download an archive of log files for a workflow run. This link expires after 1 minute. Look for `Location:` in the response header to find the URL for the download.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsdownload_workflow_run_logs",
                "table_name": "log",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/logs",
                    "params": {
                        "run_id": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Check your installation's maintenance status:
            {
                "name": "enterprise_adminget_maintenance_status",
                "table_name": "maintenance",
                "endpoint": {
                    "data_selector": "connection_services",
                    "path": "/setup/api/maintenance",
                },
            },
            # Check if a user is, publicly or privately, a member of the organization.
            {
                "name": "orgscheck_membership_for_user",
                "table_name": "member",
                "endpoint": {
                    "path": "/orgs/{org}/members/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "orgslist_members",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # The "Get team member" endpoint (described below) is deprecated.  We recommend using the [Get team membership for a user](https://docs.github.com/enterprise-server@3.9/rest/teams/members#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.  To list members in a team, the team must be visible to the authenticated user.
            {
                "name": "teamsget_member_legacy",
                "table_name": "member",
                "endpoint": {
                    "path": "/teams/{team_id}/members/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "teamslist_members_legacy",
                            "field": "id",
                        },
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Checks if a pull request has been merged into the base branch. The HTTP status of the response indicates whether or not the pull request has been merged; the response body is empty.
            {
                "name": "pullscheck_if_merged",
                "table_name": "merge",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/merge",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "metaget",
                "table_name": "metum",
                "endpoint": {
                    "data_selector": "packages",
                    "path": "/meta",
                },
            },
            # Lists the most recent migrations, including both exports (which can be started through the REST API) and imports (which cannot be started using the REST API).  A list of `repositories` is only returned for export migrations.
            {
                "name": "migrationslist_for_org",
                "table_name": "migration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/migrations",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "exclude": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetches the status of a migration.  The `state` of a migration can be one of the following values:  *   `pending`, which means the migration hasn't started yet. *   `exporting`, which means the migration is in progress. *   `exported`, which means the migration finished successfully. *   `failed`, which means the migration failed.
            {
                "name": "migrationsget_status_for_org",
                "table_name": "migration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/migrations/{migration_id}",
                    "params": {
                        "migration_id": {
                            "type": "resolve",
                            "resource": "migrationslist_for_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "exclude": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists all migrations a user has started.
            {
                "name": "migrationslist_for_authenticated_user",
                "table_name": "migration",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/migrations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists milestones for a repository.
            {
                "name": "issueslist_milestones",
                "table_name": "milestone",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/milestones",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "open",
                        # "sort": "due_on",
                        # "direction": "asc",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a milestone using the given milestone number.
            {
                "name": "issuesget_milestone",
                "table_name": "milestone",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/milestones/{milestone_number}",
                    "params": {
                        "milestone_number": {
                            "type": "resolve",
                            "resource": "issueslist_milestones",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the repositories with access to a self-hosted runner group configured in an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "actionslist_repo_access_to_self_hosted_runner_group_in_org",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/orgs/{org}/actions/runner-groups/{runner_group_id}/repositories",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "runner_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_selected_repos_for_org_secret",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/orgs/{org}/actions/secrets/{secret_name}/repositories",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all repositories that can access an organization variable that is available to selected repositories.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_selected_repos_for_org_variable",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/orgs/{org}/actions/variables/{name}/repositories",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "actionslist_org_variables",
                            "field": "name",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all repositories that have been selected when the `visibility` for repository access to a secret is set to `selected`.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "dependabotlist_selected_repos_for_org_secret",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/orgs/{org}/dependabot/secrets/{secret_name}/repositories",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List all the repositories for this organization migration.
            {
                "name": "migrationslist_repos_for_org",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/migrations/{migration_id}/repositories",
                    "params": {
                        "migration_id": {
                            "type": "resolve",
                            "resource": "migrationslist_for_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists repositories for the specified organization.  **Note:** In order to see the `security_and_analysis` block for a repository you must have admin permissions for the repository or be an owner or security manager for the organization that owns the repository. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."
            {
                "name": "reposlist_for_org",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/repos",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "type": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists a team's repositories visible to the authenticated user.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos`.
            {
                "name": "teamslist_repos_in_org",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/repos",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "reposlist_forks",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/forks",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sort": "newest",
                        # "per_page": "30",
                    },
                },
            },
            # Lists all public repositories in the order that they were created.  Note: - For GitHub Enterprise Server, this endpoint will only list repositories available to all users on the enterprise. - Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of repositories.
            {
                "name": "reposlist_public",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repositories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "visibility": "public",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List team repositories](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#list-team-repositories) endpoint.
            {
                "name": "teamslist_repos_legacy",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/repos",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all the repositories for this user migration.
            {
                "name": "migrationslist_repos_for_authenticated_user",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/migrations/{migration_id}/repositories",
                    "params": {
                        "migration_id": {
                            "type": "resolve",
                            "resource": "migrationslist_for_authenticated_user",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists repositories the authenticated user is watching.
            {
                "name": "activitylist_watched_repos_for_authenticated_user",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/subscriptions",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists public repositories for the specified user.
            {
                "name": "reposlist_for_user",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/repos",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "type": "owner",
                        # "sort": "full_name",
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists repositories a user is watching.
            {
                "name": "activitylist_repos_watched_by_user",
                "table_name": "minimal_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/subscriptions",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Get node metadata for all configured nodes in the current cluster. For more information, see "[About clustering](https://docs.github.com/enterprise-server@3.9/admin/enterprise-management/configuring-clustering/about-clustering)."
            {
                "name": "enterprise_adminget_config_nodes",
                "table_name": "node",
                "endpoint": {
                    "data_selector": "nodes",
                    "path": "/manage/v1/config/nodes",
                    "params": {
                        # the parameters below can optionally be configured
                        # "uuid": "OPTIONAL_CONFIG",
                        # "cluster_roles": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get the octocat as ASCII art
            {
                "name": "metaget_octocat",
                "table_name": "octocat",
                "endpoint": {
                    "path": "/octocat",
                    "params": {
                        # the parameters below can optionally be configured
                        # "s": "OPTIONAL_CONFIG",
                    },
                },
            },
            # You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.
            {
                "name": "orgslist_webhooks",
                "table_name": "org_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/hooks",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Returns a webhook configured in an organization. To get only the webhook `config` properties, see "[Get a webhook configuration for an organization](/rest/orgs/webhooks#get-a-webhook-configuration-for-an-organization).  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.
            {
                "name": "orgsget_webhook",
                "table_name": "org_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/hooks/{hook_id}",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "orgslist_webhooks",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # In order to get a user's membership with an organization, the authenticated user must be an organization member. The `state` parameter in the response can be used to identify the user's membership status.
            {
                "name": "orgsget_membership_for_user",
                "table_name": "org_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/memberships/{username}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all of the authenticated user's organization memberships.
            {
                "name": "orgslist_memberships_for_authenticated_user",
                "table_name": "org_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/memberships/orgs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # If the authenticated user is an active or pending member of the organization, this endpoint will return the user's membership. If the authenticated user is not affiliated with the organization, a `404` is returned. This endpoint will return a `403` if the request is made by a GitHub App that is blocked by the organization.
            {
                "name": "orgsget_membership_for_authenticated_user",
                "table_name": "org_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/memberships/orgs/{org}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all pre-receive hooks that are enabled or testing for this organization as well as any disabled hooks that can be configured at the organization level. Globally disabled pre-receive hooks that do not allow downstream configuration are not listed.
            {
                "name": "enterprise_adminlist_pre_receive_hooks_for_org",
                "table_name": "org_pre_receive_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/pre-receive-hooks",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "direction": "desc",
                        # "sort": "created",
                    },
                },
            },
            {
                "name": "enterprise_adminget_pre_receive_hook_for_org",
                "table_name": "org_pre_receive_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/pre-receive-hooks/{pre_receive_hook_id}",
                    "params": {
                        "pre_receive_hook_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_pre_receive_hooks_for_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all secrets available in an organization without revealing their encrypted values.  Authenticated users must have collaborator access to a repository to create, update, or read secrets.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_org_secrets",
                "table_name": "organization_actions_secret",
                "endpoint": {
                    "data_selector": "secrets",
                    "path": "/orgs/{org}/actions/secrets",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single organization secret without revealing its encrypted value.  The authenticated user must have collaborator access to a repository to create, update, or read secrets  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_org_secret",
                "table_name": "organization_actions_secret",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/secrets/{secret_name}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all organization variables.  Authenticated users must have collaborator access to a repository to create, update, or read variables.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_org_variables",
                "table_name": "organization_actions_variable",
                "endpoint": {
                    "data_selector": "variables",
                    "path": "/orgs/{org}/actions/variables",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "10",
                    },
                },
            },
            # Gets a specific variable in an organization.  The authenticated user must have collaborator access to a repository to create, update, or read variables.  OAuth tokens and personal access tokens (classic) need the`admin:org` scope to use this endpoint. If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_org_variable",
                "table_name": "organization_actions_variable",
                "primary_key": "name",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/variables/{name}",
                    "params": {
                        "name": {
                            "type": "resolve",
                            "resource": "actionslist_org_variables",
                            "field": "name",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note**: This operation is deprecated and will be removed in the future. Use the "[List custom repository roles](https://docs.github.com/enterprise-server@3.9/rest/orgs/custom-roles#list-custom-repository-roles-in-an-organization)" endpoint instead.  List the custom repository roles available in this organization. For more information on custom repository roles, see "[About custom repository roles](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-repository-roles)."  The authenticated user must be administrator of the organization or of a repository of the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` or `repo` scope to use this endpoint.
            {
                "name": "orgslist_custom_roles",
                "table_name": "organization_custom_repository_role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_roles",
                    "path": "/organizations/{organization_id}/custom_roles",
                    "params": {
                        "organization_id": {
                            "type": "resolve",
                            "resource": "orgslist",
                            "field": "id",
                        },
                    },
                },
            },
            # List the custom repository roles available in this organization. For more information on custom repository roles, see "[About custom repository roles](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-repository-roles)."  The authenticated user must be an administrator of the organization or of a repository of the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` or `repo` scope to use this endpoint.
            {
                "name": "orgslist_custom_repo_roles",
                "table_name": "organization_custom_repository_role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "custom_roles",
                    "path": "/orgs/{org}/custom-repository-roles",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a custom repository role that is available to all repositories owned by the organization. For more information on custom repository roles, see "[About custom repository roles](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-repository-roles)."  The authenticated user must be an administrator of the organization or of a repository of the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` or `repo` scope to use this endpoint.
            {
                "name": "orgsget_custom_repo_role",
                "table_name": "organization_custom_repository_role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/custom-repository-roles/{role_id}",
                    "params": {
                        "role_id": {
                            "type": "resolve",
                            "resource": "orgslist_custom_repo_roles",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all secrets available in an organization without revealing their encrypted values.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "dependabotlist_org_secrets",
                "table_name": "organization_dependabot_secret",
                "endpoint": {
                    "data_selector": "secrets",
                    "path": "/orgs/{org}/dependabot/secrets",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a single organization secret without revealing its encrypted value.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "dependabotget_org_secret",
                "table_name": "organization_dependabot_secret",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/dependabot/secrets/{secret_name}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "secret_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets information about an organization.  When the value of `two_factor_requirement_enabled` is `true`, the organization requires all members, billing managers, and outside collaborators to enable [two-factor authentication](https://docs.github.com/enterprise-server@3.9/articles/securing-your-account-with-two-factor-authentication-2fa/).  To see the full details about an organization, the authenticated user must be an organization owner.  The values returned by this endpoint are set by the "Update an organization" endpoint. If your organization set a default security configuration (beta), the following values retrieved from the "Update an organization" endpoint have been overwritten by that configuration:  - advanced_security_enabled_for_new_repositories - dependabot_alerts_enabled_for_new_repositories - dependabot_security_updates_enabled_for_new_repositories - dependency_graph_enabled_for_new_repositories - secret_scanning_enabled_for_new_repositories - secret_scanning_push_protection_enabled_for_new_repositories  For more information on security configurations, see "[Enabling security features at scale](https://docs.github.com/enterprise-server@3.9/code-security/securing-your-organization/introduction-to-securing-your-organization-at-scale/about-enabling-security-features-at-scale)."  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to see the full details about an organization.  To see information about an organization's GitHub Enterprise Server plan, GitHub Apps need the `Organization plan` permission.
            {
                "name": "orgsget",
                "table_name": "organization_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists secret scanning alerts for eligible repositories in an enterprise, from newest to oldest. To use this endpoint, you must be a member of the enterprise, and you must use an access token with the `repo` scope or `security_events` scope. Alerts are only returned for organizations in the enterprise for which you are an organization owner or a [security manager](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization).
            {
                "name": "secret_scanninglist_alerts_for_enterprise",
                "table_name": "organization_secret_scanning_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/secret-scanning/alerts",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "secret_type": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "per_page": "30",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists secret scanning alerts for eligible repositories in an organization, from newest to oldest.  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "secret_scanninglist_alerts_for_org",
                "table_name": "organization_secret_scanning_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/secret-scanning/alerts",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "secret_type": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "per_page": "30",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists the organizations that are selected to have GitHub Actions enabled in an enterprise. To use this endpoint, the enterprise permission policy for `enabled_organizations` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_selected_organizations_enabled_github_actions_enterprise",
                "table_name": "organization_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "organizations",
                    "path": "/enterprises/{enterprise}/actions/permissions/organizations",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists the organizations with access to a self-hosted runner group.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_org_access_to_self_hosted_runner_group_in_enterprise",
                "table_name": "organization_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "organizations",
                    "path": "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/organizations",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "runner_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all organizations, in the order that they were created.  **Note:** Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of organizations.
            {
                "name": "orgslist",
                "table_name": "organization_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/organizations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List organizations for the authenticated user.  For OAuth app tokens and personal access tokens (classic), this endpoint only lists organizations that your authorization allows you to operate on in some way (e.g., you can list teams with `read:org` scope, you can publicize your organization membership with `user` scope, etc.). Therefore, this API requires at least `user` or `read:org` scope for OAuth app tokens and personal access tokens (classic). Requests with insufficient scope will receive a `403 Forbidden` response.
            {
                "name": "orgslist_for_authenticated_user",
                "table_name": "organization_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/orgs",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List [public organization memberships](https://docs.github.com/enterprise-server@3.9/articles/publicizing-or-concealing-organization-membership) for the specified user.  This method only lists _public_ memberships, regardless of authentication. If you need to fetch all of the organization memberships (public and private) for the authenticated user, use the [List organizations for the authenticated user](https://docs.github.com/enterprise-server@3.9/rest/orgs/orgs#list-organizations-for-the-authenticated-user) API instead.
            {
                "name": "orgslist_for_user",
                "table_name": "organization_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/orgs",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all packages that are in a specific organization, are readable by the requesting user, and that encountered a conflict during a Docker migration.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint.
            {
                "name": "packageslist_docker_migration_conflicting_packages_for_organization",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/docker/conflicts",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists packages in an organization readable by the user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packageslist_packages_for_organization",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/packages",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "visibility": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific package in an organization.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_package_for_organization",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/packages/{package_type}/{package_name}",
                    "params": {
                        "package_name": {
                            "type": "resolve",
                            "resource": "packageslist_packages_for_organization",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all packages that are owned by the authenticated user within the user's namespace, and that encountered a conflict during a Docker migration.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint.
            {
                "name": "packageslist_docker_migration_conflicting_packages_for_authenticated_user",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/docker/conflicts",
                },
            },
            # Lists packages owned by the authenticated user within the user's namespace.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packageslist_packages_for_authenticated_user",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/packages",
                    "params": {
                        "package_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "visibility": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific package for a package owned by the authenticated user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_package_for_authenticated_user",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/packages/{package_type}/{package_name}",
                    "params": {
                        "package_name": {
                            "type": "resolve",
                            "resource": "packageslist_packages_for_authenticated_user",
                            "field": "id",
                        },
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all packages that are in a specific user's namespace, that the requesting user has access to, and that encountered a conflict during Docker migration.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint.
            {
                "name": "packageslist_docker_migration_conflicting_packages_for_user",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/docker/conflicts",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists all packages in a user's namespace for which the requesting user has access.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packageslist_packages_for_user",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/packages",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        "package_type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "visibility": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific package metadata for a public package owned by a user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_package_for_user",
                "table_name": "package",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/packages/{package_type}/{package_name}",
                    "params": {
                        "package_name": {
                            "type": "resolve",
                            "resource": "packageslist_packages_for_user",
                            "field": "id",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists package versions for a package owned by an organization.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint if the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_all_package_versions_for_package_owned_by_org",
                "table_name": "package_version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/packages/{package_type}/{package_name}/versions",
                    "params": {
                        "package_name": {
                            "type": "resolve",
                            "resource": "packageslist_packages_for_organization",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "state": "active",
                    },
                },
            },
            # Gets a specific package version in an organization.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_package_version_for_organization",
                "table_name": "package_version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/packages/{package_type}/{package_name}/versions/{package_version_id}",
                    "params": {
                        "package_version_id": {
                            "type": "resolve",
                            "resource": "packagesget_all_package_versions_for_package_owned_by_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists package versions for a package owned by the authenticated user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_all_package_versions_for_package_owned_by_authenticated_user",
                "table_name": "package_version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/packages/{package_type}/{package_name}/versions",
                    "params": {
                        "package_name": {
                            "type": "resolve",
                            "resource": "packageslist_packages_for_authenticated_user",
                            "field": "id",
                        },
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "state": "active",
                    },
                },
            },
            # Gets a specific package version for a package owned by the authenticated user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_package_version_for_authenticated_user",
                "table_name": "package_version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/packages/{package_type}/{package_name}/versions/{package_version_id}",
                    "params": {
                        "package_version_id": {
                            "type": "resolve",
                            "resource": "packagesget_all_package_versions_for_package_owned_by_authenticated_user",
                            "field": "id",
                        },
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists package versions for a public package owned by a specified user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_all_package_versions_for_package_owned_by_user",
                "table_name": "package_version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/packages/{package_type}/{package_name}/versions",
                    "params": {
                        "package_name": {
                            "type": "resolve",
                            "resource": "packageslist_packages_for_user",
                            "field": "id",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a specific package version for a public package owned by a specified user.  OAuth app tokens and personal access tokens (classic) need the `read:packages` scope to use this endpoint. If the `package_type` belongs to a GitHub Packages registry that only supports repository-scoped permissions, the `repo` scope is also required. For the list of these registries, see "[About permissions for GitHub Packages](https://docs.github.com/enterprise-server@3.9/packages/learn-github-packages/about-permissions-for-github-packages#permissions-for-repository-scoped-packages)."
            {
                "name": "packagesget_package_version_for_user",
                "table_name": "package_version",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/packages/{package_type}/{package_name}/versions/{package_version_id}",
                    "params": {
                        "package_version_id": {
                            "type": "resolve",
                            "resource": "packagesget_all_package_versions_for_package_owned_by_user",
                            "field": "id",
                        },
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_type": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "package_name": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets information about a GitHub Enterprise Server Pages site.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "reposget_pages",
                "table_name": "page",
                "endpoint": {
                    "data_selector": "https_certificate.domains",
                    "path": "/repos/{owner}/{repo}/pages",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists builts of a GitHub Enterprise Server Pages site.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "reposlist_pages_builds",
                "table_name": "page_build",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pages/builds",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets information about the single most recent build of a GitHub Enterprise Server Pages site.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "reposget_latest_pages_build",
                "table_name": "page_build",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pages/builds/latest",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets information about a GitHub Enterprise Server Pages build.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "reposget_pages_build",
                "table_name": "page_build",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pages/builds/{build_id}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "build_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the total commit counts for the `owner` and total commit counts in `all`. `all` is everyone combined, including the `owner` in the last 52 weeks. If you'd like to get the commit counts for non-owners, you can subtract `owner` from `all`.  The array order is oldest week (index 0) to most recent week.  The most recent week is seven days ago at UTC midnight to today at UTC midnight.
            {
                "name": "reposget_participation_stats",
                "table_name": "participation",
                "endpoint": {
                    "data_selector": "all",
                    "path": "/repos/{owner}/{repo}/stats/participation",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get all deployment environments for a workflow run that are waiting for protection rules to pass.  Anyone with read access to the repository can use this endpoint.  If the repository is private, OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_pending_deployments_for_run",
                "table_name": "pending_deployment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/pending_deployments",
                    "params": {
                        "run_id": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "enterprise_adminlist_pre_receive_environments",
                "table_name": "pre_receive_environment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/pre-receive-environments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "direction": "desc",
                        # "sort": "created",
                    },
                },
            },
            {
                "name": "enterprise_adminget_pre_receive_environment",
                "table_name": "pre_receive_environment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/pre-receive-environments/{pre_receive_environment_id}",
                    "params": {
                        "pre_receive_environment_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_pre_receive_environments",
                            "field": "id",
                        },
                    },
                },
            },
            # In addition to seeing the download status at the "[Get a pre-receive environment](#get-a-pre-receive-environment)" endpoint, there is also this separate endpoint for just the download status.
            {
                "name": "enterprise_adminget_download_status_for_pre_receive_environment",
                "table_name": "pre_receive_environment_download_status",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/pre-receive-environments/{pre_receive_environment_id}/downloads/latest",
                    "params": {
                        "pre_receive_environment_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_pre_receive_environments",
                            "field": "id",
                        },
                    },
                },
            },
            {
                "name": "enterprise_adminlist_pre_receive_hooks",
                "table_name": "pre_receive_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/pre-receive-hooks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "direction": "desc",
                        # "sort": "created",
                    },
                },
            },
            {
                "name": "enterprise_adminget_pre_receive_hook",
                "table_name": "pre_receive_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/pre-receive-hooks/{pre_receive_hook_id}",
                    "params": {
                        "pre_receive_hook_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_pre_receive_hooks",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists the projects in an organization. Returns a `404 Not Found` status if projects are disabled in the organization. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
            {
                "name": "projectslist_for_org",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/projects",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "open",
                        # "per_page": "30",
                    },
                },
            },
            # Gets a project by its `id`. Returns a `404 Not Found` status if projects are disabled. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
            {
                "name": "projectsget",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{project_id}",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the projects in a repository. Returns a `404 Not Found` status if projects are disabled in the repository. If you do not have sufficient privileges to perform this action, a `401 Unauthorized` or `410 Gone` status is returned.
            {
                "name": "projectslist_for_repo",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/projects",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "open",
                        # "per_page": "30",
                    },
                },
            },
            # Lists projects for a user.
            {
                "name": "projectslist_for_user",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/projects",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "state": "open",
                        # "per_page": "30",
                    },
                },
            },
            # Gets information about a project card.
            {
                "name": "projectsget_card",
                "table_name": "project_card",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/columns/cards/{card_id}",
                    "params": {
                        "card_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the project cards in a project.
            {
                "name": "projectslist_cards",
                "table_name": "project_card",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/columns/{column_id}/cards",
                    "params": {
                        "column_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "archived_state": "not_archived",
                        # "per_page": "30",
                    },
                },
            },
            # Returns the collaborator's permission level for an organization project. Possible values for the `permission` key: `admin`, `write`, `read`, `none`. You must be an organization owner or a project `admin` to review a user's permission level.
            {
                "name": "projectsget_permission_for_user",
                "table_name": "project_collaborator_permission",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{project_id}/collaborators/{username}/permission",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "projectslist_collaborators",
                            "field": "id",
                        },
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets information about a project column.
            {
                "name": "projectsget_column",
                "table_name": "project_column",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/columns/{column_id}",
                    "params": {
                        "column_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the project columns in a project.
            {
                "name": "projectslist_columns",
                "table_name": "project_column",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{project_id}/columns",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
            {
                "name": "reposget_admin_branch_protection",
                "table_name": "protected_branch_admin_enforced",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  When authenticated with admin or owner permissions to the repository, you can use this endpoint to check whether a branch requires signed commits. An enabled status of `true` indicates you must sign commits on this branch. For more information, see [Signing commits with GPG](https://docs.github.com/enterprise-server@3.9/articles/signing-commits-with-gpg) in GitHub Help.  **Note**: You must enable branch protection to require signed commits.
            {
                "name": "reposget_commit_signature_protection",
                "table_name": "protected_branch_admin_enforced",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
            {
                "name": "reposget_branch_protection",
                "table_name": "protection",
                "endpoint": {
                    "data_selector": "required_status_checks.contexts",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "enterprise_adminlist_public_keys",
                "table_name": "public_key_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/admin/keys",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "direction": "desc",
                        # "sort": "created",
                        # "since": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Check if the provided user is a public member of the organization.
            {
                "name": "orgscheck_public_membership_for_user",
                "table_name": "public_member",
                "endpoint": {
                    "path": "/orgs/{org}/public_members/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "orgslist_public_members",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists details of a pull request by providing its number.  When you get, [create](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls/#create-a-pull-request), or [edit](https://docs.github.com/enterprise-server@3.9/rest/pulls/pulls#update-a-pull-request) a pull request, GitHub Enterprise Server creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the `mergeable` key. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".  The value of the `mergeable` attribute can be `true`, `false`, or `null`. If the value is `null`, then GitHub Enterprise Server has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-`null` value for the `mergeable` attribute in the response. If `mergeable` is `true`, then `merge_commit_sha` will be the SHA of the _test_ merge commit.  The value of the `merge_commit_sha` attribute changes depending on the state of the pull request. Before merging a pull request, the `merge_commit_sha` attribute holds the SHA of the _test_ merge commit. After merging a pull request, the `merge_commit_sha` attribute changes depending on how you merged the pull request:  *   If merged as a [merge commit](https://docs.github.com/enterprise-server@3.9/articles/about-merge-methods-on-github/), `merge_commit_sha` represents the SHA of the merge commit. *   If merged via a [squash](https://docs.github.com/enterprise-server@3.9/articles/about-merge-methods-on-github/#squashing-your-merge-commits), `merge_commit_sha` represents the SHA of the squashed commit on the base branch. *   If [rebased](https://docs.github.com/enterprise-server@3.9/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), `merge_commit_sha` represents the commit that the base branch was updated to.  Pass the appropriate [media type](https://docs.github.com/enterprise-server@3.9/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`. - **`application/vnd.github.diff`**: For more information, see "[git-diff](https://git-scm.com/docs/git-diff)" in the Git documentation. If a diff is corrupt, contact us through the [GitHub Support portal](https://support.github.com/). Include the repository name and pull request ID in your message.
            {
                "name": "pullsget",
                "table_name": "pull_request",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all reviews for a specified pull request. The list of reviews returns in chronological order.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist_reviews",
                "table_name": "pull_request_review",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/reviews",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Retrieves a pull request review by its ID.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullsget_review",
                "table_name": "pull_request_review",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}",
                    "params": {
                        "review_id": {
                            "type": "resolve",
                            "resource": "pullslist_reviews",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pull_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist_review_comments_for_repo",
                "table_name": "pull_request_review_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/comments",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Provides details for a specified review comment.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullsget_review_comment",
                "table_name": "pull_request_review_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/comments/{comment_id}",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "pullslist_review_comments_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all review comments for a specified pull request. By default, review comments are in ascending order by ID.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist_review_comments",
                "table_name": "pull_request_review_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/comments",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "sort": "created",
                        # "direction": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists the merged pull request that introduced the commit to the repository. If the commit is not present in the default branch, will only return open pull requests associated with the commit.  To list the open or merged pull requests associated with a branch, you can set the `commit_sha` parameter to the branch name.
            {
                "name": "reposlist_pull_requests_associated_with_commit",
                "table_name": "pull_request_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "commit_sha": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists pull requests in a specified repository.  Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist",
                "table_name": "pull_request_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "open",
                        # "head": "OPTIONAL_CONFIG",
                        # "base": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # **Note:** Accessing this endpoint does not count against your REST API rate limit.  Some categories of endpoints have custom rate limits that are separate from the rate limit governing the other REST API endpoints. For this reason, the API response categorizes your rate limit. Under `resources`, you'll see objects relating to different categories: * The `core` object provides your rate limit status for all non-search-related resources in the REST API. * The `search` object provides your rate limit status for the REST API for searching (excluding code searches). For more information, see "[Search](https://docs.github.com/enterprise-server@3.9/rest/search/search)." * The `code_search` object provides your rate limit status for the REST API for searching code. For more information, see "[Search code](https://docs.github.com/enterprise-server@3.9/rest/search/search#search-code)." * The `graphql` object provides your rate limit status for the GraphQL API. For more information, see "[Resource limitations](https://docs.github.com/enterprise-server@3.9/graphql/overview/resource-limitations#rate-limit)." * The `integration_manifest` object provides your rate limit status for the `POST /app-manifests/{code}/conversions` operation. For more information, see "[Creating a GitHub App from a manifest](https://docs.github.com/enterprise-server@3.9/apps/creating-github-apps/setting-up-a-github-app/creating-a-github-app-from-a-manifest#3-you-exchange-the-temporary-code-to-retrieve-the-app-configuration)." * The `dependency_snapshots` object provides your rate limit status for submitting snapshots to the dependency graph. For more information, see "[Dependency graph](https://docs.github.com/enterprise-server@3.9/rest/dependency-graph)." * The `code_scanning_upload` object provides your rate limit status for uploading SARIF results to code scanning. For more information, see "[Uploading a SARIF file to GitHub](https://docs.github.com/enterprise-server@3.9/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)." * The `actions_runner_registration` object provides your rate limit status for registering self-hosted runners in GitHub Actions. For more information, see "[Self-hosted runners](https://docs.github.com/enterprise-server@3.9/rest/actions/self-hosted-runners)." * The `source_import` object is no longer in use for any API endpoints, and it will be removed in the next API version. For more information about API versions, see "[API Versions](https://docs.github.com/enterprise-server@3.9/rest/overview/api-versions)."  **Note:** The `rate` object is deprecated. If you're writing new API client code or updating existing code, you should use the `core` object instead of the `rate` object. The `core` object contains the same information that is present in the `rate` object.
            {
                "name": "rate_limitget",
                "table_name": "rate_limit_overview",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/rate_limit",
                },
            },
            # List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@3.9/rest/teams/discussion-comments#get-a-discussion-comment).  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/comments/:comment_number/reactions`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "reactionslist_for_team_discussion_comment_in_org",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}/reactions",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the reactions to a [team discussion](https://docs.github.com/enterprise-server@3.9/rest/teams/discussions#get-a-discussion).  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/:org_id/team/:team_id/discussions/:discussion_number/reactions`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "reactionslist_for_team_discussion_in_org",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/reactions",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the reactions to a [commit comment](https://docs.github.com/enterprise-server@3.9/rest/commits/comments#get-a-commit-comment).
            {
                "name": "reactionslist_for_commit_comment",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/comments/{comment_id}/reactions",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "reposlist_commit_comments_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the reactions to an [issue comment](https://docs.github.com/enterprise-server@3.9/rest/issues/comments#get-an-issue-comment).
            {
                "name": "reactionslist_for_issue_comment",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "issueslist_comments_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the reactions to an [issue](https://docs.github.com/enterprise-server@3.9/rest/issues/issues#get-an-issue).
            {
                "name": "reactionslist_for_issue",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}/reactions",
                    "params": {
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the reactions to a [pull request review comment](https://docs.github.com/enterprise-server@3.9/rest/pulls/comments#get-a-review-comment-for-a-pull-request).
            {
                "name": "reactionslist_for_pull_request_review_comment",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions",
                    "params": {
                        "comment_id": {
                            "type": "resolve",
                            "resource": "pullslist_review_comments_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # List the reactions to a [release](https://docs.github.com/enterprise-server@3.9/rest/releases/releases#get-a-release).
            {
                "name": "reactionslist_for_release",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/releases/{release_id}/reactions",
                    "params": {
                        "release_id": {
                            "type": "resolve",
                            "resource": "reposlist_releases",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion comment`](https://docs.github.com/enterprise-server@3.9/rest/reactions/reactions#list-reactions-for-a-team-discussion-comment) endpoint.  List the reactions to a [team discussion comment](https://docs.github.com/enterprise-server@3.9/rest/teams/discussion-comments#get-a-discussion-comment).  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "reactionslist_for_team_discussion_comment_legacy",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}/reactions",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List reactions for a team discussion`](https://docs.github.com/enterprise-server@3.9/rest/reactions/reactions#list-reactions-for-a-team-discussion) endpoint.  List the reactions to a [team discussion](https://docs.github.com/enterprise-server@3.9/rest/teams/discussions#get-a-discussion).  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "reactionslist_for_team_discussion_legacy",
                "table_name": "reaction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/discussions/{discussion_number}/reactions",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "content": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # This returns a list of releases, which does not include regular Git tags that have not been associated with a release. To get a list of Git tags, use the [Repository Tags API](https://docs.github.com/enterprise-server@3.9/rest/repos/repos#list-repository-tags).  Information about published releases are available to everyone. Only users with push access will receive listings for draft releases.
            {
                "name": "reposlist_releases",
                "table_name": "release",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/releases",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Get a published release with the specified tag.
            {
                "name": "reposget_release_by_tag",
                "table_name": "release",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/releases/tags/{tag}",
                    "params": {
                        "tag": {
                            "type": "resolve",
                            "resource": "reposlist_releases",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a public release with the specified release ID.  **Note:** This returns an `upload_url` key corresponding to the endpoint for uploading release assets. This key is a hypermedia resource. For more information, see "[Getting started with the REST API](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)."
            {
                "name": "reposget_release",
                "table_name": "release",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/releases/{release_id}",
                    "params": {
                        "release_id": {
                            "type": "resolve",
                            "resource": "reposlist_releases",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # To download the asset's binary content, set the `Accept` header of the request to [`application/octet-stream`](https://docs.github.com/enterprise-server@3.9/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a `200` or `302` response.
            {
                "name": "reposget_release_asset",
                "table_name": "release_asset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/releases/assets/{asset_id}",
                    "params": {
                        "asset_id": {
                            "type": "resolve",
                            "resource": "reposlist_releases",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # View the latest published full release for the repository.  The latest release is the most recent non-prerelease, non-draft release, sorted by the `created_at` attribute. The `created_at` attribute is the date of the commit used for the release, and not the date when the release was drafted or published.
            {
                "name": "reposget_latest_release",
                "table_name": "release_asset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "assets",
                    "path": "/repos/{owner}/{repo}/releases/latest",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "reposlist_releases",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "reposlist_release_assets",
                "table_name": "release_asset",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/releases/{release_id}/assets",
                    "params": {
                        "release_id": {
                            "type": "resolve",
                            "resource": "reposlist_releases",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Find repositories via various criteria. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api).  When searching for repositories, you can get text match metadata for the **name** and **description** fields when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you want to search for popular Tetris repositories written in assembly code, your query might look like this:  `q=tetris+language:assembly&sort=stars&order=desc`  This query searches for repositories with the word `tetris` in the name, the description, or the README. The results are limited to repositories where the primary language is assembly. The results are sorted by stars in descending order, so that the most popular repositories appear first in the search results.
            {
                "name": "searchrepos",
                "table_name": "repo_search_result_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/repositories",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "order": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # List repositories that an app installation can access.
            {
                "name": "appslist_repos_accessible_to_installation",
                "table_name": "repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/installation/repositories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists the selected repositories that are enabled for GitHub Actions in an organization. To use this endpoint, the organization permission policy for `enabled_repositories` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization)."  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "actionslist_selected_repositories_enabled_github_actions_organization",
                "table_name": "repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/orgs/{org}/actions/permissions/repositories",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access for an installation.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.  The access the user has to each repository is included in the hash under the `permissions` key.
            {
                "name": "appslist_installation_repos_for_authenticated_user",
                "table_name": "repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "repositories",
                    "path": "/user/installations/{installation_id}/repositories",
                    "params": {
                        "installation_id": {
                            "type": "resolve",
                            "resource": "appslist_installations_for_authenticated_user",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists repositories that the authenticated user has explicit permission (`:read`, `:write`, or `:admin`) to access.  The authenticated user has explicit permission to access repositories they own, repositories where they are a collaborator, and repositories that they can access through an organization membership.
            {
                "name": "reposlist_for_authenticated_user",
                "table_name": "repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/repos",
                    "params": {
                        # the parameters below can optionally be configured
                        # "visibility": "all",
                        # "affiliation": "owner,collaborator,organization_member",
                        # "type": "all",
                        # "sort": "full_name",
                        # "direction": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Lists repositories the authenticated user has starred.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.star+json`**: Includes a timestamp of when the star was created.
            {
                "name": "activitylist_repos_starred_by_authenticated_user",
                "table_name": "repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/starred",
                    "params": {
                        # the parameters below can optionally be configured
                        # "sort": "created",
                        # "direction": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Checks the repository permission of a collaborator. The possible repository permissions are `admin`, `write`, `read`, and `none`.  *Note*: The `permission` attribute provides the legacy base roles of `admin`, `write`, `read`, and `none`, where the `maintain` role is mapped to `write` and the `triage` role is mapped to `read`. To determine the role assigned to the collaborator, see the `role_name` attribute, which will provide the full role name, including custom roles. The `permissions` hash can also be used to determine which base level of access the collaborator has to the repository.
            {
                "name": "reposget_collaborator_permission_level",
                "table_name": "repository_collaborator_permission",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/collaborators/{username}/permission",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "reposlist_collaborators",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the fine-grained permissions that can be used in custom repository roles for an organization. For more information, see "[About custom repository roles](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/about-custom-repository-roles)."  The authenticated user must be an administrator of the organization or of a repository of the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` or `repo` scope to use this endpoint.
            {
                "name": "orgslist_repo_fine_grained_permissions",
                "table_name": "repository_fine_grained_permission",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/repository-fine-grained-permissions",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # When authenticating as a user with admin rights to a repository, this endpoint will list all currently open repository invitations.
            {
                "name": "reposlist_invitations",
                "table_name": "repository_invitation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/invitations",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # When authenticating as a user, this endpoint will list all currently open repository invitations for that user.
            {
                "name": "reposlist_invitations_for_authenticated_user",
                "table_name": "repository_invitation",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/repository_invitations",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List all pre-receive hooks that are enabled or testing for this repository as well as any disabled hooks that are allowed to be enabled at the repository level. Pre-receive hooks that are disabled at a higher level and are not configurable will not be listed.
            {
                "name": "enterprise_adminlist_pre_receive_hooks_for_repo",
                "table_name": "repository_pre_receive_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pre-receive-hooks",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "direction": "desc",
                        # "sort": "created",
                    },
                },
            },
            {
                "name": "enterprise_adminget_pre_receive_hook_for_repo",
                "table_name": "repository_pre_receive_hook",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pre-receive-hooks/{pre_receive_hook_id}",
                    "params": {
                        "pre_receive_hook_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_pre_receive_hooks_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets information about whether the authenticated user is subscribed to the repository.
            {
                "name": "activityget_repo_subscription",
                "table_name": "repository_subscription",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/subscription",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
            {
                "name": "reposget_status_checks_protection",
                "table_name": "required_status_check",
                "endpoint": {
                    "data_selector": "contexts",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists who has access to this protected branch.  **Note**: Users, apps, and teams `restrictions` are only available for organization-owned repositories.
            {
                "name": "reposget_access_restrictions",
                "table_name": "restriction",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "users",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists comments for a specific pull request review.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github-commitcomment.raw+json`**: Returns the raw markdown body. Response will include `body`. This is the default if you do not pass any specific media type. - **`application/vnd.github-commitcomment.text+json`**: Returns a text only representation of the markdown body. Response will include `body_text`. - **`application/vnd.github-commitcomment.html+json`**: Returns HTML rendered from the body's markdown. Response will include `body_html`. - **`application/vnd.github-commitcomment.full+json`**: Returns raw, text, and HTML representations. Response will include `body`, `body_text`, and `body_html`.
            {
                "name": "pullslist_comments_for_review",
                "table_name": "review_comment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/reviews/{review_id}/comments",
                    "params": {
                        "review_id": {
                            "type": "resolve",
                            "resource": "pullslist_reviews",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "pull_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Get Hypermedia links to resources accessible in GitHub's REST API
            {
                "name": "metaroot",
                "table_name": "root",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/",
                },
            },
            # Lists the self-hosted runners that are in a specific enterprise group.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_self_hosted_runners_in_group_for_enterprise",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "runners",
                    "path": "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}/runners",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "runner_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all self-hosted runners configured for an enterprise.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_self_hosted_runners_for_enterprise",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "runners",
                    "path": "/enterprises/{enterprise}/actions/runners",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific self-hosted runner configured in an enterprise.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminget_self_hosted_runner_for_enterprise",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/runners/{runner_id}",
                    "params": {
                        "runner_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_self_hosted_runners_for_enterprise",
                            "field": "id",
                        },
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists self-hosted runners that are in a specific organization group.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "actionslist_self_hosted_runners_in_group_for_org",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "runners",
                    "path": "/orgs/{org}/actions/runner-groups/{runner_group_id}/runners",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "runner_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all self-hosted runners configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_self_hosted_runners_for_org",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "runners",
                    "path": "/orgs/{org}/actions/runners",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific self-hosted runner configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionsget_self_hosted_runner_for_org",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/runners/{runner_id}",
                    "params": {
                        "runner_id": {
                            "type": "resolve",
                            "resource": "actionslist_self_hosted_runners_for_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all self-hosted runners configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_self_hosted_runners_for_repo",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "runners",
                    "path": "/repos/{owner}/{repo}/actions/runners",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific self-hosted runner configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_self_hosted_runner_for_repo",
                "table_name": "runner",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/runners/{runner_id}",
                    "params": {
                        "runner_id": {
                            "type": "resolve",
                            "resource": "actionslist_self_hosted_runners_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists binaries for the runner application that you can download and run.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_runner_applications_for_enterprise",
                "table_name": "runner_application",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/runners/downloads",
                    "params": {
                        "enterprise": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_self_hosted_runners_for_enterprise",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists binaries for the runner application that you can download and run.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.  If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_runner_applications_for_org",
                "table_name": "runner_application",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/runners/downloads",
                    "params": {
                        "org": {
                            "type": "resolve",
                            "resource": "actionslist_self_hosted_runners_for_org",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists binaries for the runner application that you can download and run.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_runner_applications_for_repo",
                "table_name": "runner_application",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/runners/downloads",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "actionslist_self_hosted_runners_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all self-hosted runner groups for an enterprise.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_self_hosted_runner_groups_for_enterprise",
                "table_name": "runner_groups_enterprise",
                "endpoint": {
                    "data_selector": "runner_groups",
                    "path": "/enterprises/{enterprise}/actions/runner-groups",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "visible_to_organization": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a specific self-hosted runner group for an enterprise.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminget_self_hosted_runner_group_for_enterprise",
                "table_name": "runner_groups_enterprise",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/enterprises/{enterprise}/actions/runner-groups/{runner_group_id}",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "runner_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all self-hosted runner groups configured in an organization and inherited from an enterprise.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "actionslist_self_hosted_runner_groups_for_org",
                "table_name": "runner_groups_org",
                "endpoint": {
                    "data_selector": "runner_groups",
                    "path": "/orgs/{org}/actions/runner-groups",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                        # "visible_to_repository": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a specific self-hosted runner group for an organization.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint.
            {
                "name": "actionsget_self_hosted_runner_group_for_org",
                "table_name": "runner_groups_org",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/actions/runner-groups/{runner_group_id}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "runner_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all labels for a self-hosted runner configured in an enterprise.  OAuth app tokens and personal access tokens (classic) need the `manage_runners:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminlist_labels_for_self_hosted_runner_for_enterprise",
                "table_name": "runner_label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "labels",
                    "path": "/enterprises/{enterprise}/actions/runners/{runner_id}/labels",
                    "params": {
                        "runner_id": {
                            "type": "resolve",
                            "resource": "enterprise_adminlist_self_hosted_runners_for_enterprise",
                            "field": "id",
                        },
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all labels for a self-hosted runner configured in an organization.  Authenticated users must have admin access to the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `admin:org` scope to use this endpoint. If the repository is private, the `repo` scope is also required.
            {
                "name": "actionslist_labels_for_self_hosted_runner_for_org",
                "table_name": "runner_label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "labels",
                    "path": "/orgs/{org}/actions/runners/{runner_id}/labels",
                    "params": {
                        "runner_id": {
                            "type": "resolve",
                            "resource": "actionslist_self_hosted_runners_for_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all labels for a self-hosted runner configured in a repository.  Authenticated users must have admin access to the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionslist_labels_for_self_hosted_runner_for_repo",
                "table_name": "runner_label",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "labels",
                    "path": "/repos/{owner}/{repo}/actions/runners/{runner_id}/labels",
                    "params": {
                        "runner_id": {
                            "type": "resolve",
                            "resource": "actionslist_self_hosted_runners_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Exports the software bill of materials (SBOM) for a repository in SPDX JSON format.
            {
                "name": "dependency_graphexport_sbom",
                "table_name": "sbom",
                "endpoint": {
                    "data_selector": "sbom.documentDescribes",
                    "path": "/repos/{owner}/{repo}/dependency-graph/sbom",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note:** The SCIM API endpoints for enterprise accounts are currently in *private* beta and are subject to change.  Gets information about a SCIM group.
            {
                "name": "enterprise_adminget_provisioning_information_for_enterprise_group",
                "table_name": "scim_enterprise_group_response",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/scim/v2/enterprises/{enterprise}/Groups/{scim_group_id}",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "scim_group_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "excludedAttributes": "OPTIONAL_CONFIG",
                    },
                },
            },
            # **Note:** The SCIM API endpoints for enterprise accounts are currently in *private* beta and are subject to change.  Gets information about a SCIM user.
            {
                "name": "enterprise_adminget_provisioning_information_for_enterprise_user",
                "table_name": "scim_enterprise_user_response",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/scim/v2/enterprises/{enterprise}/Users/{scim_user_id}",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "scim_user_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists secret scanning alerts for an eligible repository, from newest to oldest.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "secret_scanninglist_alerts_for_repo",
                "table_name": "secret_scanning_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/secret-scanning/alerts",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "state": "OPTIONAL_CONFIG",
                        # "secret_type": "OPTIONAL_CONFIG",
                        # "resolution": "OPTIONAL_CONFIG",
                        # "sort": "created",
                        # "direction": "desc",
                        # "per_page": "30",
                        # "before": "OPTIONAL_CONFIG",
                        # "after": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a single secret scanning alert detected in an eligible repository.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "secret_scanningget_alert",
                "table_name": "secret_scanning_alert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "alert_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all locations for a given secret scanning alert for an eligible repository.  The authenticated user must be an administrator for the repository or for the organization that owns the repository to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` or `security_events` scope to use this endpoint. If this endpoint is only used with public repositories, the token can use the `public_repo` scope instead.
            {
                "name": "secret_scanninglist_locations_for_alert",
                "table_name": "secret_scanning_location",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/secret-scanning/alerts/{alert_number}/locations",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "alert_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets the selected actions that are allowed in an enterprise. To use this endpoint, the enterprise permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an enterprise](#set-github-actions-permissions-for-an-enterprise)."  OAuth app tokens and personal access tokens (classic) need the `admin:enterprise` scope to use this endpoint.
            {
                "name": "enterprise_adminget_allowed_actions_enterprise",
                "table_name": "selected_action",
                "endpoint": {
                    "data_selector": "patterns_allowed",
                    "path": "/enterprises/{enterprise}/actions/permissions/selected-actions",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the selected actions that are allowed in an organization. To use this endpoint, the organization permission policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for an organization](#set-github-actions-permissions-for-an-organization).""  You must authenticate using an access token with the `admin:org` scope to use this endpoint. GitHub Apps must have the `administration` organization permission to use this API.
            {
                "name": "actionsget_allowed_actions_organization",
                "table_name": "selected_action",
                "endpoint": {
                    "data_selector": "patterns_allowed",
                    "path": "/orgs/{org}/actions/permissions/selected-actions",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the settings for selected actions that are allowed in a repository. To use this endpoint, the repository policy for `allowed_actions` must be configured to `selected`. For more information, see "[Set GitHub Actions permissions for a repository](#set-github-actions-permissions-for-a-repository)."  You must authenticate using an access token with the `repo` scope to use this endpoint. GitHub Apps must have the `administration` repository permission to use this API.
            {
                "name": "actionsget_allowed_actions_repository",
                "table_name": "selected_action",
                "endpoint": {
                    "data_selector": "patterns_allowed",
                    "path": "/repos/{owner}/{repo}/actions/permissions/selected-actions",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the settings for your instance. To change settings, see the [Set settings endpoint](https://docs.github.com/enterprise-server@3.9/rest/enterprise-admin/management-console#set-settings).  **Note:** You cannot retrieve the management console password with the Enterprise administration API.
            {
                "name": "enterprise_adminget_settings",
                "table_name": "setting",
                "endpoint": {
                    "data_selector": "run_list",
                    "path": "/setup/api/settings",
                },
            },
            {
                "name": "reposlist_branches",
                "table_name": "short_branch",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "protected": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Users with pull access in a repository can access a combined view of commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.   Additionally, a combined `state` is returned. The `state` is one of:  *   **failure** if any of the contexts report as `error` or `failure` *   **pending** if there are no statuses or a context is `pending` *   **success** if the latest status for all contexts is `success`
            {
                "name": "reposget_combined_status_for_ref",
                "table_name": "simple_commit_status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "statuses",
                    "path": "/repos/{owner}/{repo}/commits/{ref}/status",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List all users who are members of an organization. If the authenticated user is also a member of this organization then both concealed and public members will be returned.
            {
                "name": "orgslist_members",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/members",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "role": "all",
                        # "per_page": "30",
                    },
                },
            },
            # List all users who are outside collaborators of an organization.
            {
                "name": "orgslist_outside_collaborators",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/outside_collaborators",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "per_page": "30",
                    },
                },
            },
            # Members of an organization can choose to have their membership publicized or not.
            {
                "name": "orgslist_public_members",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/public_members",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Team members will include the members of child teams.  To list members in a team, the team must be visible to the authenticated user.
            {
                "name": "teamslist_members_in_org",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/members",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "role": "all",
                        # "per_page": "30",
                    },
                },
            },
            # Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project `admin` to list collaborators.
            {
                "name": "projectslist_collaborators",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{project_id}/collaborators",
                    "params": {
                        "project_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "affiliation": "all",
                        # "per_page": "30",
                    },
                },
            },
            # Lists the [available assignees](https://docs.github.com/enterprise-server@3.9/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository.
            {
                "name": "issueslist_assignees",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/assignees",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.
            {
                "name": "reposget_pull_request_review_protection",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "dismissal_restrictions.users",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "branch": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the people who have push access to this branch.
            {
                "name": "reposget_users_with_access_to_protected_branch",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users",
                    "params": {
                        "branch": {
                            "type": "resolve",
                            "resource": "reposget_access_restrictions",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the users or teams whose review is requested for a pull request. Once a requested reviewer submits a review, they are no longer considered a requested reviewer. Their review will instead be returned by the [List reviews for a pull request](https://docs.github.com/enterprise-server@3.9/rest/pulls/reviews#list-reviews-for-a-pull-request) operation.
            {
                "name": "pullslist_requested_reviewers",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "users",
                    "path": "/repos/{owner}/{repo}/pulls/{pull_number}/requested_reviewers",
                    "params": {
                        "pull_number": {
                            "type": "resolve",
                            "resource": "pullslist",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the people watching the specified repository.
            {
                "name": "activitylist_watchers_for_repo",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/subscribers",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team members`](https://docs.github.com/enterprise-server@3.9/rest/teams/members#list-team-members) endpoint.  Team members will include the members of child teams.
            {
                "name": "teamslist_members_legacy",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/members",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "role": "all",
                        # "per_page": "30",
                    },
                },
            },
            # Lists the people following the authenticated user.
            {
                "name": "userslist_followers_for_authenticated_user",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/followers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists the people who the authenticated user follows.
            {
                "name": "userslist_followed_by_authenticated_user",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/following",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all users, in the order that they signed up on GitHub Enterprise Server. This list includes personal user accounts and organization accounts.  Note: Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api#using-link-headers) to get the URL for the next page of users.
            {
                "name": "userslist",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "since": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # Lists the people following the specified user.
            {
                "name": "userslist_followers_for_user",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/followers",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists the people who the specified user follows.
            {
                "name": "userslist_following_for_user",
                "table_name": "simple_user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/following",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists all of your social accounts.
            {
                "name": "userslist_social_accounts_for_authenticated_user",
                "table_name": "social_account",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/social_accounts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists social media accounts for a user. This endpoint is accessible by anyone.
            {
                "name": "userslist_social_accounts_for_user",
                "table_name": "social_account",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/social_accounts",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "enterprise_adminget_all_authorized_ssh_keys",
                "table_name": "ssh_key",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/setup/api/settings/authorized-keys",
                },
            },
            # Lists the SSH signing keys for the authenticated user's GitHub account.  OAuth app tokens and personal access tokens (classic) need the `read:ssh_signing_key` scope to use this endpoint.
            {
                "name": "userslist_ssh_signing_keys_for_authenticated_user",
                "table_name": "ssh_signing_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/ssh_signing_keys",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets extended details for an SSH signing key.  OAuth app tokens and personal access tokens (classic) need the `read:ssh_signing_key` scope to use this endpoint.
            {
                "name": "usersget_ssh_signing_key_for_authenticated_user",
                "table_name": "ssh_signing_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/ssh_signing_keys/{ssh_signing_key_id}",
                    "params": {
                        "ssh_signing_key_id": {
                            "type": "resolve",
                            "resource": "userslist_ssh_signing_keys_for_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists the SSH signing keys for a user. This operation is accessible by anyone.
            {
                "name": "userslist_ssh_signing_keys_for_user",
                "table_name": "ssh_signing_key",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/ssh_signing_keys",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "gistscheck_is_starred",
                "table_name": "star",
                "endpoint": {
                    "path": "/gists/{gist_id}/star",
                    "params": {
                        "gist_id": {
                            "type": "resolve",
                            "resource": "gistslist",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists the people that have starred the repository.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.star+json`**: Includes a timestamp of when the star was created.
            {
                "name": "activitylist_stargazers_for_repo",
                "table_name": "stargazer",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/stargazers",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Whether the authenticated user has starred the repository.
            {
                "name": "activitycheck_repo_is_starred_by_authenticated_user",
                "table_name": "starred",
                "endpoint": {
                    "path": "/user/starred/{owner}/{repo}",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "activitylist_repos_starred_by_authenticated_user",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists repositories a user has starred.  This endpoint supports the following custom media types. For more information, see "[Media types](https://docs.github.com/enterprise-server@3.9/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."  - **`application/vnd.github.star+json`**: Includes a timestamp of when the star was created.
            {
                "name": "activitylist_repos_starred_by_user",
                "table_name": "starred",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}/starred",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "sort": "created",
                        # "direction": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Gets the status of all services running on each replica node. This endpoint may take several seconds to reply.
            {
                "name": "enterprise_adminget_replication_status",
                "table_name": "statu",
                "endpoint": {
                    "data_selector": "nodes",
                    "path": "/manage/v1/replication/status",
                    "params": {
                        # the parameters below can optionally be configured
                        # "uuid": "OPTIONAL_CONFIG",
                        # "cluster_roles": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.  This resource is also available via a legacy route: `GET /repos/:owner/:repo/statuses/:ref`.
            {
                "name": "reposlist_commit_statuses_for_ref",
                "table_name": "status",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/commits/{ref}/statuses",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets the customization template for an OpenID Connect (OIDC) subject claim.  OAuth app tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.
            {
                "name": "oidcget_oidc_custom_sub_template_for_org",
                "table_name": "sub",
                "endpoint": {
                    "data_selector": "include_claim_keys",
                    "path": "/orgs/{org}/actions/oidc/customization/sub",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets the customization template for an OpenID Connect (OIDC) subject claim.  OAuth tokens and personal access tokens (classic) need the `repo` scope to use this endpoint.
            {
                "name": "actionsget_custom_oidc_sub_claim_for_repo",
                "table_name": "sub",
                "endpoint": {
                    "data_selector": "include_claim_keys",
                    "path": "/repos/{owner}/{repo}/actions/oidc/customization/sub",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            {
                "name": "reposlist_tags",
                "table_name": "tag",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/tags",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # This returns the tag protection states of a repository.  This information is only available to repository administrators.
            {
                "name": "reposlist_tag_protection",
                "table_name": "tag_protection",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/tags/protection",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a redirect URL to download a tar archive for a repository. If you omit `:ref`, the repository’s default branch (usually `main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the `Location` header to make a second `GET` request. **Note**: For private repositories, these links are temporary and expire after five minutes.
            {
                "name": "reposdownload_tarball_archive",
                "table_name": "tarball",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/tarball/{ref}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all teams in an organization that are visible to the authenticated user.
            {
                "name": "teamslist",
                "table_name": "team",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Lists the child teams of the team specified by `{team_slug}`.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/teams`.
            {
                "name": "teamslist_child_in_org",
                "table_name": "team",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/teams",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Protected branches are available in public repositories with GitHub Free and GitHub Free for organizations, and in public and private repositories with GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server. For more information, see [GitHub's products](https://docs.github.com/enterprise-server@3.9/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.  Lists the teams who have push access to this branch. The list includes child teams.
            {
                "name": "reposget_teams_with_access_to_protected_branch",
                "table_name": "team",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams",
                    "params": {
                        "branch": {
                            "type": "resolve",
                            "resource": "reposget_access_restrictions",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the teams that have access to the specified repository and that are also visible to the authenticated user.  For a public repository, a team is listed only if that team added the public repository explicitly.  OAuth app tokens and personal access tokens (classic) need the `public_repo` or `repo` scope to use this endpoint with a public repository, and `repo` scope to use this endpoint with a private repository.
            {
                "name": "reposlist_teams",
                "table_name": "team",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/teams",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List child teams`](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#list-child-teams) endpoint.
            {
                "name": "teamslist_child_legacy",
                "table_name": "team",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/teams",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # List all discussions on a team's page.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamslist_discussions_in_org",
                "table_name": "team_discussion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/discussions",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "desc",
                        # "per_page": "30",
                        # "pinned": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a specific discussion on a team's page.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamsget_discussion_in_org",
                "table_name": "team_discussion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List discussions`](https://docs.github.com/enterprise-server@3.9/rest/teams/discussions#list-discussions) endpoint.  List all discussions on a team's page.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamslist_discussions_legacy",
                "table_name": "team_discussion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/discussions",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion](https://docs.github.com/enterprise-server@3.9/rest/teams/discussions#get-a-discussion) endpoint.  Get a specific discussion on a team's page.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamsget_discussion_legacy",
                "table_name": "team_discussion",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/discussions/{discussion_number}",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all comments on a team discussion.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamslist_discussion_comments_in_org",
                "table_name": "team_discussion_comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Get a specific comment on a team discussion.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/discussions/{discussion_number}/comments/{comment_number}`.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamsget_discussion_comment_in_org",
                "table_name": "team_discussion_comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/discussions/{discussion_number}/comments/{comment_number}",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [List discussion comments](https://docs.github.com/enterprise-server@3.9/rest/teams/discussion-comments#list-discussion-comments) endpoint.  List all comments on a team discussion.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamslist_discussion_comments_legacy",
                "table_name": "team_discussion_comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/discussions/{discussion_number}/comments",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "direction": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get a discussion comment](https://docs.github.com/enterprise-server@3.9/rest/teams/discussion-comments#get-a-discussion-comment) endpoint.  Get a specific comment on a team discussion.  OAuth app tokens and personal access tokens (classic) need the `read:discussion` scope to use this endpoint.
            {
                "name": "teamsget_discussion_comment_legacy",
                "table_name": "team_discussion_comment",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/discussions/{discussion_number}/comments/{comment_number}",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "discussion_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "comment_number": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Gets a team using the team's `slug`. To create the `slug`, GitHub Enterprise Server replaces special characters in the `name` string, changes all words to lowercase, and replaces spaces with a `-` separator. For example, `"My TEam Näme"` would become `my-team-name`.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}`.
            {
                "name": "teamsget_by_name",
                "table_name": "team_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the [Get a team by name](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#get-a-team-by-name) endpoint.
            {
                "name": "teamsget_legacy",
                "table_name": "team_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all of the teams across all of the organizations to which the authenticated user belongs.  OAuth app tokens and personal access tokens (classic) need the `user`, `repo`, or `read:org` scope to use this endpoint.  When using a fine-grained personal access token, the resource owner of the token must be a single organization, and the response will only include the teams from that organization.
            {
                "name": "teamslist_for_authenticated_user",
                "table_name": "team_full",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user/teams",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Team members will include the members of child teams.  To get a user's membership with a team, the team must be visible to the authenticated user.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/memberships/{username}`.  **Note:** The response contains the `state` of the membership and the member's `role`.  The `role` for organization owners is set to `maintainer`. For more information about `maintainer` roles, see [Create a team](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#create-a-team).
            {
                "name": "teamsget_membership_for_user_in_org",
                "table_name": "team_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/memberships/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Get team membership for a user](https://docs.github.com/enterprise-server@3.9/rest/teams/members#get-team-membership-for-a-user) endpoint.  Team members will include the members of child teams.  To get a user's membership with a team, the team must be visible to the authenticated user.  **Note:** The response contains the `state` of the membership and the member's `role`.  The `role` for organization owners is set to `maintainer`. For more information about `maintainer` roles, see [Create a team](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#create-a-team).
            {
                "name": "teamsget_membership_for_user_legacy",
                "table_name": "team_membership",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/memberships/{username}",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "username": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the organization projects for a team.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects`.
            {
                "name": "teamslist_projects_in_org",
                "table_name": "team_project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/projects",
                    "params": {
                        "team_slug": {
                            "type": "resolve",
                            "resource": "teamslist",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/projects/{project_id}`.
            {
                "name": "teamscheck_permissions_for_project_in_org",
                "table_name": "team_project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/projects/{project_id}",
                    "params": {
                        "project_id": {
                            "type": "resolve",
                            "resource": "teamslist_projects_in_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team projects`](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#list-team-projects) endpoint.  Lists the organization projects for a team.
            {
                "name": "teamslist_projects_legacy",
                "table_name": "team_project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/projects",
                    "params": {
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a project](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#check-team-permissions-for-a-project) endpoint.  Checks whether a team has `read`, `write`, or `admin` permissions for an organization project. The response includes projects inherited from a parent team.
            {
                "name": "teamscheck_permissions_for_project_legacy",
                "table_name": "team_project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/projects/{project_id}",
                    "params": {
                        "project_id": {
                            "type": "resolve",
                            "resource": "teamslist_projects_legacy",
                            "field": "id",
                        },
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull` permission for a repository. Repositories inherited through a parent team will also be checked.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@3.9/rest/overview/media-types/) via the `application/vnd.github.v3.repository+json` accept header.  If a team doesn't have permission for the repository, you will receive a `404 Not Found` response status.  If the repository is private, you must have at least `read` permission for that repository, and your token must have the `repo` or `admin:org` scope. Otherwise, you will receive a `404 Not Found` response status.  **Note:** You can also specify a team by `org_id` and `team_id` using the route `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.
            {
                "name": "teamscheck_permissions_for_repo_in_org",
                "table_name": "team_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "teamslist_repos_in_org",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "team_slug": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # **Note**: Repositories inherited through a parent team will also be checked.  **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [Check team permissions for a repository](https://docs.github.com/enterprise-server@3.9/rest/teams/teams#check-team-permissions-for-a-repository) endpoint.  You can also get information about the specified repository, including what permissions the team grants on it, by passing the following custom [media type](https://docs.github.com/enterprise-server@3.9/rest/overview/media-types/) via the `Accept` header:
            {
                "name": "teamscheck_permissions_for_repo_legacy",
                "table_name": "team_repository",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/teams/{team_id}/repos/{owner}/{repo}",
                    "params": {
                        "repo": {
                            "type": "resolve",
                            "resource": "teamslist_repos_legacy",
                            "field": "id",
                        },
                        "team_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists teams that are security managers for an organization. For more information, see "[Managing security managers in your organization](https://docs.github.com/enterprise-server@3.9/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."  The authenticated user must be an administrator or security manager for the organization to use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `read:org` scope to use this endpoint.
            {
                "name": "orgslist_security_manager_teams",
                "table_name": "team_simple",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/security-managers",
                    "params": {
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # List all templates available to pass as an option when [creating a repository](https://docs.github.com/enterprise-server@3.9/rest/repos/repos#create-a-repository-for-the-authenticated-user).
            {
                "name": "gitignoreget_all_templates",
                "table_name": "template",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/gitignore/templates",
                },
            },
            # List all notifications for the current user, sorted by most recently updated.
            {
                "name": "activitylist_notifications_for_authenticated_user",
                "table_name": "thread",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/notifications",
                    "params": {
                        # the parameters below can optionally be configured
                        # "all": "false",
                        # "participating": "false",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "per_page": "50",
                    },
                },
            },
            # Gets information about a notification thread.
            {
                "name": "activityget_thread",
                "table_name": "thread",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/notifications/threads/{thread_id}",
                    "params": {
                        "thread_id": {
                            "type": "resolve",
                            "resource": "activitylist_notifications_for_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            # Lists all notifications for the current user in the specified repository.
            {
                "name": "activitylist_repo_notifications_for_authenticated_user",
                "table_name": "thread",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/notifications",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "all": "false",
                        # "participating": "false",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                    },
                },
            },
            # This checks to see if the current user is subscribed to a thread. You can also [get a repository subscription](https://docs.github.com/enterprise-server@3.9/rest/activity/watching#get-a-repository-subscription).  Note that subscriptions are only generated if a user is participating in a conversation--for example, they've replied to the thread, were **@mentioned**, or manually subscribe to a thread.
            {
                "name": "activityget_thread_subscription_for_authenticated_user",
                "table_name": "thread_subscription",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/notifications/threads/{thread_id}/subscription",
                    "params": {
                        "thread_id": {
                            "type": "resolve",
                            "resource": "activitylist_notifications_for_authenticated_user",
                            "field": "id",
                        },
                    },
                },
            },
            # List all timeline events for an issue.
            {
                "name": "issueslist_events_for_timeline",
                "table_name": "timeline_issue_events",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/issues/{issue_number}/timeline",
                    "params": {
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issueslist_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            {
                "name": "reposget_all_topics",
                "table_name": "topic",
                "endpoint": {
                    "data_selector": "names",
                    "path": "/repos/{owner}/{repo}/topics",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Find topics via various criteria. Results are sorted by best match. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api). See "[Searching topics](https://docs.github.com/enterprise-server@3.9/articles/searching-topics/)" for a detailed list of qualifiers.  When searching for topics, you can get text match metadata for the topic's **short\_description**, **description**, **name**, or **display\_name** field when you pass the `text-match` media type. For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you want to search for topics related to Ruby that are featured on https://github.com/topics. Your query might look like this:  `q=ruby+is:featured`  This query searches for topics with the keyword `ruby` and limits the results to find only topics that are featured. The topics that are the best match for the query appear first in the search results.
            {
                "name": "searchtopics",
                "table_name": "topic_search_result_item",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/topics",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # **Note:** The SCIM API endpoints for enterprise accounts are currently in *private* beta and are subject to change.  Lists provisioned SCIM enterprise members.  When a user with a SCIM-provisioned external identity is removed from an enterprise through a `patch` with `active` flag set to `false`, the account's metadata is preserved to allow the user to re-join the enterprise in the future. However, the user's account will be suspended and the user will not be able to sign-in. In order to permanently suspend the users account with no ability to re-join the enterprise in the future, use the `delete` request. Users that were not permanently deleted will be visible in the returned results.
            {
                "name": "enterprise_adminlist_provisioned_identities_enterprise",
                "table_name": "user",
                "endpoint": {
                    "data_selector": "schemas",
                    "path": "/scim/v2/enterprises/{enterprise}/Users",
                    "params": {
                        "enterprise": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "filter": "OPTIONAL_CONFIG",
                        # "startIndex": "1",
                        # "count": "30",
                    },
                },
            },
            # OAuth app tokens and personal access tokens (classic) need the `user` scope in order for the response to include private profile information.
            {
                "name": "usersget_authenticated",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/user",
                },
            },
            # Provides publicly available information about someone with a GitHub account.  The `email` key in the following response is the publicly visible email address from your GitHub Enterprise Server [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for `email`, then it will have a value of `null`. You only see publicly visible email addresses when authenticated with GitHub Enterprise Server. For more information, see [Authentication](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-rest-api#authentication).  The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see "[Emails API](https://docs.github.com/enterprise-server@3.9/rest/users/emails)".
            {
                "name": "usersget_by_username",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{username}",
                    "params": {
                        "username": {
                            "type": "resolve",
                            "resource": "userslist",
                            "field": "id",
                        },
                    },
                },
            },
            # Find users via various criteria. This method returns up to 100 results [per page](https://docs.github.com/enterprise-server@3.9/rest/guides/using-pagination-in-the-rest-api).  When searching for users, you can get text match metadata for the issue **login**, public **email**, and **name** fields when you pass the `text-match` media type. For more details about highlighting search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata). For more details about how to receive highlighted search results, see [Text match metadata](https://docs.github.com/enterprise-server@3.9/rest/search/search#text-match-metadata).  For example, if you're looking for a list of popular users, you might try this query:  `q=tom+repos:%3E42+followers:%3E1000`  This query searches for users with the name `tom`. The results are restricted to users with more than 42 repositories and over 1,000 followers.  This endpoint does not accept authentication and will only include publicly visible users. As an alternative, you can use the GraphQL API. The GraphQL API requires authentication and will return private users, including Enterprise Managed Users (EMUs), that you are authorized to view. For more information, see "[GraphQL Queries](https://docs.github.com/enterprise-server@3.9/graphql/reference/queries#search)."
            {
                "name": "searchusers",
                "table_name": "user_search_result_item",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "items",
                    "path": "/search/users",
                    "params": {
                        "q": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "sort": "OPTIONAL_CONFIG",
                        # "order": "desc",
                        # "per_page": "30",
                    },
                },
            },
            # Gets the GitHub Enterprise Server release versions that are currently installed on all available nodes. For more information, see "[GitHub Enterprise Server releases](https://docs.github.com/enterprise-server@3.9/admin/all-releases)."
            {
                "name": "enterprise_adminget_version",
                "table_name": "version",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/manage/v1/version",
                    "params": {
                        # the parameters below can optionally be configured
                        # "uuid": "OPTIONAL_CONFIG",
                        # "cluster_roles": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Shows whether dependency alerts are enabled or disabled for a repository. The authenticated user must have admin read access to the repository. For more information, see "[About security alerts for vulnerable dependencies](https://docs.github.com/enterprise-server@3.9/articles/about-security-alerts-for-vulnerable-dependencies)".
            {
                "name": "reposcheck_vulnerability_alerts",
                "table_name": "vulnerability_alert",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/vulnerability-alerts",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the webhook configuration for a GitHub App. For more information about configuring a webhook for your app, see "[Creating a GitHub App](/developers/apps/creating-a-github-app)."  You must use a [JWT](https://docs.github.com/enterprise-server@3.9/apps/building-github-apps/authenticating-with-github-apps/#authenticating-as-a-github-app) to access this endpoint.
            {
                "name": "appsget_webhook_config_for_app",
                "table_name": "webhook_config",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/app/hook/config",
                },
            },
            # Returns the webhook configuration for an organization. To get more information about the webhook, including the `active` state and `events`, use "[Get an organization webhook ](/rest/orgs/webhooks#get-an-organization-webhook)."  You must be an organization owner to use this endpoint.  OAuth app tokens and personal access tokens (classic) need `admin:org_hook` scope. OAuth apps cannot list, view, or edit webhooks that they did not create and users cannot list, view, or edit webhooks that were created by OAuth apps.
            {
                "name": "orgsget_webhook_config_for_org",
                "table_name": "webhook_config",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/orgs/{org}/hooks/{hook_id}/config",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "orgslist_webhooks",
                            "field": "id",
                        },
                        "org": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns the webhook configuration for a repository. To get more information about the webhook, including the `active` state and `events`, use "[Get a repository webhook](/rest/webhooks/repos#get-a-repository-webhook)."  OAuth app tokens and personal access tokens (classic) need the `read:repo_hook` or `repo` scope to use this endpoint.
            {
                "name": "reposget_webhook_config_for_repo",
                "table_name": "webhook_config",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/hooks/{hook_id}/config",
                    "params": {
                        "hook_id": {
                            "type": "resolve",
                            "resource": "reposlist_webhooks",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists the workflows in a repository.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionslist_repo_workflows",
                "table_name": "workflow",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "workflows",
                    "path": "/repos/{owner}/{repo}/actions/workflows",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "per_page": "30",
                    },
                },
            },
            # Gets a specific workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionsget_workflow",
                "table_name": "workflow",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/workflows/{workflow_id}",
                    "params": {
                        "workflow_id": {
                            "type": "resolve",
                            "resource": "actionslist_repo_workflows",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Lists all workflow runs for a repository. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.  This API will return up to 1,000 results for each search when using the following parameters: `actor`, `branch`, `check_suite_id`, `created`, `event`, `head_sha`, `status`.
            {
                "name": "actionslist_workflow_runs_for_repo",
                "table_name": "workflow_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "workflow_runs",
                    "path": "/repos/{owner}/{repo}/actions/runs",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "actor": "OPTIONAL_CONFIG",
                        # "branch": "OPTIONAL_CONFIG",
                        # "event": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "created": "OPTIONAL_CONFIG",
                        # "exclude_pull_requests": "false",
                        # "check_suite_id": "OPTIONAL_CONFIG",
                        # "head_sha": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Gets a specific workflow run.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionsget_workflow_run",
                "table_name": "workflow_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}",
                    "params": {
                        "run_id": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "exclude_pull_requests": "false",
                    },
                },
            },
            # Gets a specific workflow run attempt.  Anyone with read access to the repository can use this endpoint.  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionsget_workflow_run_attempt",
                "table_name": "workflow_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/repos/{owner}/{repo}/actions/runs/{run_id}/attempts/{attempt_number}",
                    "params": {
                        "attempt_number": {
                            "type": "resolve",
                            "resource": "actionslist_workflow_runs_for_repo",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "run_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "exclude_pull_requests": "false",
                    },
                },
            },
            # List all workflow runs for a workflow. You can replace `workflow_id` with the workflow file name. For example, you could use `main.yaml`. You can use parameters to narrow the list of results. For more information about using parameters, see [Parameters](https://docs.github.com/enterprise-server@3.9/rest/guides/getting-started-with-the-rest-api#parameters).  Anyone with read access to the repository can use this endpoint  OAuth app tokens and personal access tokens (classic) need the `repo` scope to use this endpoint with a private repository.
            {
                "name": "actionslist_workflow_runs",
                "table_name": "workflow_run",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "workflow_runs",
                    "path": "/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs",
                    "params": {
                        "workflow_id": {
                            "type": "resolve",
                            "resource": "actionslist_repo_workflows",
                            "field": "id",
                        },
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "actor": "OPTIONAL_CONFIG",
                        # "branch": "OPTIONAL_CONFIG",
                        # "event": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "per_page": "30",
                        # "created": "OPTIONAL_CONFIG",
                        # "exclude_pull_requests": "false",
                        # "check_suite_id": "OPTIONAL_CONFIG",
                        # "head_sha": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a random sentence from the Zen of GitHub
            {
                "name": "metaget_zen",
                "table_name": "zen",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/zen",
                },
            },
            # Gets a redirect URL to download a zip archive for a repository. If you omit `:ref`, the repository’s default branch (usually `main`) will be used. Please make sure your HTTP framework is configured to follow redirects or you will need to use the `Location` header to make a second `GET` request.  **Note**: For private repositories, these links are temporary and expire after five minutes. If the repository is empty, you will receive a 404 when you follow the redirect.
            {
                "name": "reposdownload_zipball_archive",
                "table_name": "zipball",
                "endpoint": {
                    "path": "/repos/{owner}/{repo}/zipball/{ref}",
                    "params": {
                        "owner": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "repo": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ref": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
