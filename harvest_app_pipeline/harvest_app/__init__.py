from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="harvest_app_source", max_table_nesting=2)
def harvest_app_source(
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
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # Returns a list of billable rates for the user identified by USER_ID. The billable rates are returned sorted by start_date, with the oldest starting billable rates appearing first.  The response contains an object with a billable_rates property that contains an array of up to per_page billable rates. Each entry in the array is a separate billable rate object. If no more billable rates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your billable rates.
            {
                "name": "list_billable_rates_for_specific_user",
                "table_name": "billable_rate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "billable_rates",
                    "path": "/users/{userId}/billable_rates",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "list_users",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the billable rate with the given ID. Returns a billable rate object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_billable_rate",
                "table_name": "billable_rate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{userId}/billable_rates/{billableRateId}",
                    "params": {
                        "billableRateId": {
                            "type": "resolve",
                            "resource": "list_billable_rates_for_specific_user",
                            "field": "id",
                        },
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of your clients. The clients are returned sorted by creation date, with the most recently created clients appearing first.  The response contains an object with a clients property that contains an array of up to per_page clients. Each entry in the array is a separate client object. If no more clients are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your clients.
            {
                "name": "list_clients",
                "table_name": "client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "clients",
                    "path": "/clients",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the client with the given ID. Returns a client object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_client",
                "table_name": "client",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/clients/{clientId}",
                    "params": {
                        "clientId": {
                            "type": "resolve",
                            "resource": "list_clients",
                            "field": "id",
                        },
                    },
                },
            },
            # Retrieves the company for the currently authenticated user. Returns a company object and a 200 OK response code.
            {
                "name": "retrieve_company",
                "table_name": "company",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/company",
                },
            },
            # Returns a list of your contacts. The contacts are returned sorted by creation date, with the most recently created contacts appearing first.  The response contains an object with a contacts property that contains an array of up to per_page contacts. Each entry in the array is a separate contact object. If no more contacts are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your contacts.
            {
                "name": "list_contacts",
                "table_name": "contact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "contacts",
                    "path": "/contacts",
                    "params": {
                        # the parameters below can optionally be configured
                        # "client_id": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the contact with the given ID. Returns a contact object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_contact",
                "table_name": "contact",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/contacts/{contactId}",
                    "params": {
                        "contactId": {
                            "type": "resolve",
                            "resource": "list_contacts",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of cost rates for the user identified by USER_ID. The cost rates are returned sorted by start_date, with the oldest starting cost rates appearing first.  The response contains an object with a cost_rates property that contains an array of up to per_page cost rates. Each entry in the array is a separate cost rate object. If no more cost rates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your cost rates.
            {
                "name": "list_cost_rates_for_specific_user",
                "table_name": "cost_rate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "cost_rates",
                    "path": "/users/{userId}/cost_rates",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "list_users",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the cost rate with the given ID. Returns a cost rate object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_cost_rate",
                "table_name": "cost_rate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{userId}/cost_rates/{costRateId}",
                    "params": {
                        "costRateId": {
                            "type": "resolve",
                            "resource": "list_cost_rates_for_specific_user",
                            "field": "id",
                        },
                        "userId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of your estimates. The estimates are returned sorted by issue date, with the most recently issued estimates appearing first.  The response contains an object with a estimates property that contains an array of up to per_page estimates. Each entry in the array is a separate estimate object. If no more estimates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your estimates.
            {
                "name": "list_estimates",
                "table_name": "estimate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "estimates",
                    "path": "/estimates",
                    "params": {
                        # the parameters below can optionally be configured
                        # "client_id": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "to": "OPTIONAL_CONFIG",
                        # "state": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the estimate with the given ID. Returns an estimate object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_estimate",
                "table_name": "estimate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/estimates/{estimateId}",
                    "params": {
                        "estimateId": {
                            "type": "resolve",
                            "resource": "list_estimates",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of your estimate item categories. The estimate item categories are returned sorted by creation date, with the most recently created estimate item categories appearing first.  The response contains an object with a estimate_item_categories property that contains an array of up to per_page estimate item categories. Each entry in the array is a separate estimate item category object. If no more estimate item categories are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your estimate item categories.
            {
                "name": "list_estimate_item_categories",
                "table_name": "estimate_item_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "estimate_item_categories",
                    "path": "/estimate_item_categories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the estimate item category with the given ID. Returns an estimate item category object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_estimate_item_category",
                "table_name": "estimate_item_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/estimate_item_categories/{estimateItemCategoryId}",
                    "params": {
                        "estimateItemCategoryId": {
                            "type": "resolve",
                            "resource": "list_estimate_item_categories",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of messages associated with a given estimate. The estimate messages are returned sorted by creation date, with the most recently created messages appearing first.  The response contains an object with an estimate_messages property that contains an array of up to per_page messages. Each entry in the array is a separate message object. If no more messages are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your messages.
            {
                "name": "list_messages_for_estimate",
                "table_name": "estimate_message",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "estimate_messages",
                    "path": "/estimates/{estimateId}/messages",
                    "params": {
                        "estimateId": {
                            "type": "resolve",
                            "resource": "list_estimates",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of your expenses. If accessing this endpoint as an Administrator, all expenses in the account will be returned. If accessing this endpoint as a Manager, all expenses for assigned teammates and managed projects will be returned. The expenses are returned sorted by the spent_at date, with the most recent expenses appearing first.  The response contains an object with a expenses property that contains an array of up to per_page expenses. Each entry in the array is a separate expense object. If no more expenses are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your expenses.
            {
                "name": "list_expenses",
                "table_name": "expense",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "expenses",
                    "path": "/expenses",
                    "params": {
                        # the parameters below can optionally be configured
                        # "user_id": "OPTIONAL_CONFIG",
                        # "client_id": "OPTIONAL_CONFIG",
                        # "project_id": "OPTIONAL_CONFIG",
                        # "is_billed": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "to": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the expense with the given ID. Returns an expense object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_expense",
                "table_name": "expense",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/expenses/{expenseId}",
                    "params": {
                        "expenseId": {
                            "type": "resolve",
                            "resource": "list_expenses",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of your expense categories. The expense categories are returned sorted by creation date, with the most recently created expense categories appearing first.  The response contains an object with a expense_categories property that contains an array of up to per_page expense categories. Each entry in the array is a separate expense category object. If no more expense categories are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your expense categories.
            {
                "name": "list_expense_categories",
                "table_name": "expense_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "expense_categories",
                    "path": "/expense_categories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the expense category with the given ID. Returns an expense category object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_expense_category",
                "table_name": "expense_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/expense_categories/{expenseCategoryId}",
                    "params": {
                        "expenseCategoryId": {
                            "type": "resolve",
                            "resource": "list_expense_categories",
                            "field": "id",
                        },
                    },
                },
            },
            {
                "name": "expense_categories_report",
                "table_name": "expense_reports_result",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/expenses/categories",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "clients_expenses_report",
                "table_name": "expense_reports_result",
                "primary_key": "client_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/expenses/clients",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "projects_expenses_report",
                "table_name": "expense_reports_result",
                "primary_key": "project_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/expenses/projects",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "team_expenses_report",
                "table_name": "expense_reports_result",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/expenses/team",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of your invoices. The invoices are returned sorted by issue date, with the most recently issued invoices appearing first.  The response contains an object with a invoices property that contains an array of up to per_page invoices. Each entry in the array is a separate invoice object. If no more invoices are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your invoices.
            {
                "name": "list_invoices",
                "table_name": "invoice",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "invoices",
                    "path": "/invoices",
                    "params": {
                        # the parameters below can optionally be configured
                        # "client_id": "OPTIONAL_CONFIG",
                        # "project_id": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "to": "OPTIONAL_CONFIG",
                        # "state": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the invoice with the given ID. Returns an invoice object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_invoice",
                "table_name": "invoice",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/invoices/{invoiceId}",
                    "params": {
                        "invoiceId": {
                            "type": "resolve",
                            "resource": "list_invoices",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of your invoice item categories. The invoice item categories are returned sorted by creation date, with the most recently created invoice item categories appearing first.  The response contains an object with a invoice_item_categories property that contains an array of up to per_page invoice item categories. Each entry in the array is a separate invoice item category object. If no more invoice item categories are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your invoice item categories.
            {
                "name": "list_invoice_item_categories",
                "table_name": "invoice_item_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "invoice_item_categories",
                    "path": "/invoice_item_categories",
                    "params": {
                        # the parameters below can optionally be configured
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the invoice item category with the given ID. Returns an invoice item category object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_invoice_item_category",
                "table_name": "invoice_item_category",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/invoice_item_categories/{invoiceItemCategoryId}",
                    "params": {
                        "invoiceItemCategoryId": {
                            "type": "resolve",
                            "resource": "list_invoice_item_categories",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of messages associated with a given invoice. The invoice messages are returned sorted by creation date, with the most recently created messages appearing first.  The response contains an object with an invoice_messages property that contains an array of up to per_page messages. Each entry in the array is a separate message object. If no more messages are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your messages.
            {
                "name": "list_messages_for_invoice",
                "table_name": "invoice_message",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "invoice_messages",
                    "path": "/invoices/{invoiceId}/messages",
                    "params": {
                        "invoiceId": {
                            "type": "resolve",
                            "resource": "list_invoices",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns the subject and body text as configured in Harvest of an invoice message for a specific invoice and a 200 OK response code if the call succeeded. Does not create the invoice message. If no parameters are passed, will return the subject and body of a general invoice message for the specific invoice.
            {
                "name": "retrieve_invoice_message_subject_and_body_for_specific_invoice",
                "table_name": "invoice_message_subject_and_body",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/invoices/{invoiceId}/messages/new",
                    "params": {
                        "invoiceId": {
                            "type": "resolve",
                            "resource": "list_messages_for_invoice",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "thank_you": "OPTIONAL_CONFIG",
                        # "reminder": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of payments associate with a given invoice. The payments are returned sorted by creation date, with the most recently created payments appearing first.  The response contains an object with an invoice_payments property that contains an array of up to per_page payments. Each entry in the array is a separate payment object. If no more payments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your payments.
            {
                "name": "list_payments_for_invoice",
                "table_name": "invoice_payment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "invoice_payments",
                    "path": "/invoices/{invoiceId}/payments",
                    "params": {
                        "invoiceId": {
                            "type": "resolve",
                            "resource": "list_invoices",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the currently authenticated user. Returns a user object and a 200 OK response code.
            {
                "name": "retrieve_the_currently_authenticated_user",
                "table_name": "me",
                "endpoint": {
                    "data_selector": "roles",
                    "path": "/users/me",
                },
            },
            # Returns a list of your projects. The projects are returned sorted by creation date, with the most recently created projects appearing first.  The response contains an object with a projects property that contains an array of up to per_page projects. Each entry in the array is a separate project object. If no more projects are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your projects.
            {
                "name": "list_projects",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "projects",
                    "path": "/projects",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "client_id": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the project with the given ID. Returns a project object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_project",
                "table_name": "project",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "list_projects",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of your active project assignments for the currently authenticated user. The project assignments are returned sorted by creation date, with the most recently created project assignments appearing first.  The response contains an object with a project_assignments property that contains an array of up to per_page project assignments. Each entry in the array is a separate project assignment object. If no more project assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your project assignments.
            {
                "name": "list_active_project_assignments_for_the_currently_authenticated_user",
                "table_name": "project_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "project_assignments",
                    "path": "/users/me/project_assignments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of active project assignments for the user identified by USER_ID. The project assignments are returned sorted by creation date, with the most recently created project assignments appearing first.  The response contains an object with a project_assignments property that contains an array of up to per_page project assignments. Each entry in the array is a separate project assignment object. If no more project assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your project assignments.
            {
                "name": "list_active_project_assignments",
                "table_name": "project_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "project_assignments",
                    "path": "/users/{userId}/project_assignments",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "list_users",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # The response contains an object with a results property that contains an array of up to per_page results. Each entry in the array is a separate result object. If no more results are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your results.
            {
                "name": "project_budget_report",
                "table_name": "project_budget_report_result",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/project_budget",
                    "params": {
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                        # "is_active": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of roles in the account. The roles are returned sorted by creation date, with the most recently created roles appearing first.  The response contains an object with a roles property that contains an array of up to per_page roles. Each entry in the array is a separate role object. If no more roles are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your roles.
            {
                "name": "list_roles",
                "table_name": "role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "roles",
                    "path": "/roles",
                    "params": {
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the role with the given ID. Returns a role object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_role",
                "table_name": "role",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/roles/{roleId}",
                    "params": {
                        "roleId": {
                            "type": "resolve",
                            "resource": "list_roles",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of your tasks. The tasks are returned sorted by creation date, with the most recently created tasks appearing first.  The response contains an object with a tasks property that contains an array of up to per_page tasks. Each entry in the array is a separate task object. If no more tasks are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your tasks.
            {
                "name": "list_tasks",
                "table_name": "task",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "tasks",
                    "path": "/tasks",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the task with the given ID. Returns a task object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_task",
                "table_name": "task",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/tasks/{taskId}",
                    "params": {
                        "taskId": {
                            "type": "resolve",
                            "resource": "list_tasks",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of your task assignments for the project identified by PROJECT_ID. The task assignments are returned sorted by creation date, with the most recently created task assignments appearing first.  The response contains an object with a task_assignments property that contains an array of up to per_page task assignments. Each entry in the array is a separate task assignment object. If no more task assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your task assignments.
            {
                "name": "list_task_assignments_for_specific_project",
                "table_name": "task_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "task_assignments",
                    "path": "/projects/{projectId}/task_assignments",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "list_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the task assignment with the given ID. Returns a task assignment object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_task_assignment",
                "table_name": "task_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/task_assignments/{taskAssignmentId}",
                    "params": {
                        "taskAssignmentId": {
                            "type": "resolve",
                            "resource": "list_task_assignments_for_specific_project",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of your task assignments. The task assignments are returned sorted by creation date, with the most recently created task assignments appearing first.  The response contains an object with a task_assignments property that contains an array of up to per_page task assignments. Each entry in the array is a separate task assignment object. If no more task assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your task assignments.
            {
                "name": "list_task_assignments",
                "table_name": "task_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "task_assignments",
                    "path": "/task_assignments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of assigned teammates for the user identified by USER_ID. The USER_ID must belong to a user that is a Manager, if not, a 422 Unprocessable Entity status code will be returned.  The response contains an object with a teammates property that contains an array of up to per_page teammates. Each entry in the array is a separate teammate object. If no more teammates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your teammates.
            {
                "name": "list_assigned_teammates_for_specific_user",
                "table_name": "teammate",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "teammates",
                    "path": "/users/{userId}/teammates",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "list_users",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of time entries. The time entries are returned sorted by spent_date date. At this time, the sort option can’t be customized.  The response contains an object with a time_entries property that contains an array of up to per_page time entries. Each entry in the array is a separate time entry object. If no more time entries are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your time entries.
            {
                "name": "list_time_entries",
                "table_name": "time_entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "time_entries",
                    "path": "/time_entries",
                    "params": {
                        # the parameters below can optionally be configured
                        # "user_id": "OPTIONAL_CONFIG",
                        # "client_id": "OPTIONAL_CONFIG",
                        # "project_id": "OPTIONAL_CONFIG",
                        # "task_id": "OPTIONAL_CONFIG",
                        # "external_reference_id": "OPTIONAL_CONFIG",
                        # "is_billed": "OPTIONAL_CONFIG",
                        # "is_running": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "to": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the time entry with the given ID. Returns a time entry object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_time_entry",
                "table_name": "time_entry",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/time_entries/{timeEntryId}",
                    "params": {
                        "timeEntryId": {
                            "type": "resolve",
                            "resource": "list_time_entries",
                            "field": "id",
                        },
                    },
                },
            },
            {
                "name": "clients_time_report",
                "table_name": "time_reports_result",
                "primary_key": "client_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/time/clients",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "include_fixed_fee": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "projects_time_report",
                "table_name": "time_reports_result",
                "primary_key": "project_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/time/projects",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "include_fixed_fee": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "tasks_report",
                "table_name": "time_reports_result",
                "primary_key": "task_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/time/tasks",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "include_fixed_fee": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "team_time_report",
                "table_name": "time_reports_result",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/time/team",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "include_fixed_fee": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # The response contains an object with a results property that contains an array of up to per_page results. Each entry in the array is a separate result object. If no more results are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your results.  Note: Each request requires both the from and to parameters to be supplied in the URL’s query string. The timeframe supplied cannot exceed 1 year (365 days).
            {
                "name": "uninvoiced_report",
                "table_name": "uninvoiced_report_result",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/reports/uninvoiced",
                    "params": {
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "to": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of your users. The users are returned sorted by creation date, with the most recently created users appearing first.  The response contains an object with a users property that contains an array of up to per_page users. Each entry in the array is a separate user object. If no more users are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your users.
            {
                "name": "list_users",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "users",
                    "path": "/users",
                    "params": {
                        # the parameters below can optionally be configured
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the user with the given ID. Returns a user object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_user",
                "table_name": "user",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/users/{userId}",
                    "params": {
                        "userId": {
                            "type": "resolve",
                            "resource": "list_users",
                            "field": "id",
                        },
                    },
                },
            },
            # Returns a list of user assignments for the project identified by PROJECT_ID. The user assignments are returned sorted by creation date, with the most recently created user assignments appearing first.  The response contains an object with a user_assignments property that contains an array of up to per_page user assignments. Each entry in the array is a separate user assignment object. If no more user assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your user assignments.
            {
                "name": "list_user_assignments_for_specific_project",
                "table_name": "user_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "user_assignments",
                    "path": "/projects/{projectId}/user_assignments",
                    "params": {
                        "projectId": {
                            "type": "resolve",
                            "resource": "list_projects",
                            "field": "id",
                        },
                        # the parameters below can optionally be configured
                        # "user_id": "OPTIONAL_CONFIG",
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieves the user assignment with the given ID. Returns a user assignment object and a 200 OK response code if a valid identifier was provided.
            {
                "name": "retrieve_user_assignment",
                "table_name": "user_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/projects/{projectId}/user_assignments/{userAssignmentId}",
                    "params": {
                        "userAssignmentId": {
                            "type": "resolve",
                            "resource": "list_user_assignments_for_specific_project",
                            "field": "id",
                        },
                        "projectId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Returns a list of your projects user assignments, active and archived. The user assignments are returned sorted by creation date, with the most recently created user assignments appearing first.  The response contains an object with a user_assignments property that contains an array of up to per_page user assignments. Each entry in the array is a separate user assignment object. If no more user assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your user assignments.
            {
                "name": "list_user_assignments",
                "table_name": "user_assignment",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "user_assignments",
                    "path": "/user_assignments",
                    "params": {
                        # the parameters below can optionally be configured
                        # "user_id": "OPTIONAL_CONFIG",
                        # "is_active": "OPTIONAL_CONFIG",
                        # "updated_since": "OPTIONAL_CONFIG",
                        # "cursor": "OPTIONAL_CONFIG",
                        # "per_page": "OPTIONAL_CONFIG",
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
