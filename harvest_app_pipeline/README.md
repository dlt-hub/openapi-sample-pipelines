# harvest_app pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/harvest_app.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /users/{userId}/billable_rates_ 
  *resource*: list_billable_rates_for_specific_user  
  *description*: Returns a list of billable rates for the user identified by USER_ID. The billable rates are returned sorted by start_date, with the oldest starting billable rates appearing first.  The response contains an object with a billable_rates property that contains an array of up to per_page billable rates. Each entry in the array is a separate billable rate object. If no more billable rates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your billable rates.
* _GET /users/{userId}/billable_rates/{billableRateId}_ 
  *resource*: retrieve_billable_rate  
  *description*: Retrieves the billable rate with the given ID. Returns a billable rate object and a 200 OK response code if a valid identifier was provided.
* _GET /clients_ 
  *resource*: list_clients  
  *description*: Returns a list of your clients. The clients are returned sorted by creation date, with the most recently created clients appearing first.  The response contains an object with a clients property that contains an array of up to per_page clients. Each entry in the array is a separate client object. If no more clients are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your clients.
* _GET /clients/{clientId}_ 
  *resource*: retrieve_client  
  *description*: Retrieves the client with the given ID. Returns a client object and a 200 OK response code if a valid identifier was provided.
* _GET /company_ 
  *resource*: retrieve_company  
  *description*: Retrieves the company for the currently authenticated user. Returns a company object and a 200 OK response code.
* _GET /contacts_ 
  *resource*: list_contacts  
  *description*: Returns a list of your contacts. The contacts are returned sorted by creation date, with the most recently created contacts appearing first.  The response contains an object with a contacts property that contains an array of up to per_page contacts. Each entry in the array is a separate contact object. If no more contacts are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your contacts.
* _GET /contacts/{contactId}_ 
  *resource*: retrieve_contact  
  *description*: Retrieves the contact with the given ID. Returns a contact object and a 200 OK response code if a valid identifier was provided.
* _GET /users/{userId}/cost_rates_ 
  *resource*: list_cost_rates_for_specific_user  
  *description*: Returns a list of cost rates for the user identified by USER_ID. The cost rates are returned sorted by start_date, with the oldest starting cost rates appearing first.  The response contains an object with a cost_rates property that contains an array of up to per_page cost rates. Each entry in the array is a separate cost rate object. If no more cost rates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your cost rates.
* _GET /users/{userId}/cost_rates/{costRateId}_ 
  *resource*: retrieve_cost_rate  
  *description*: Retrieves the cost rate with the given ID. Returns a cost rate object and a 200 OK response code if a valid identifier was provided.
* _GET /estimates_ 
  *resource*: list_estimates  
  *description*: Returns a list of your estimates. The estimates are returned sorted by issue date, with the most recently issued estimates appearing first.  The response contains an object with a estimates property that contains an array of up to per_page estimates. Each entry in the array is a separate estimate object. If no more estimates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your estimates.
* _GET /estimates/{estimateId}_ 
  *resource*: retrieve_estimate  
  *description*: Retrieves the estimate with the given ID. Returns an estimate object and a 200 OK response code if a valid identifier was provided.
* _GET /estimate_item_categories_ 
  *resource*: list_estimate_item_categories  
  *description*: Returns a list of your estimate item categories. The estimate item categories are returned sorted by creation date, with the most recently created estimate item categories appearing first.  The response contains an object with a estimate_item_categories property that contains an array of up to per_page estimate item categories. Each entry in the array is a separate estimate item category object. If no more estimate item categories are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your estimate item categories.
* _GET /estimate_item_categories/{estimateItemCategoryId}_ 
  *resource*: retrieve_estimate_item_category  
  *description*: Retrieves the estimate item category with the given ID. Returns an estimate item category object and a 200 OK response code if a valid identifier was provided.
* _GET /estimates/{estimateId}/messages_ 
  *resource*: list_messages_for_estimate  
  *description*: Returns a list of messages associated with a given estimate. The estimate messages are returned sorted by creation date, with the most recently created messages appearing first.  The response contains an object with an estimate_messages property that contains an array of up to per_page messages. Each entry in the array is a separate message object. If no more messages are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your messages.
* _GET /expenses_ 
  *resource*: list_expenses  
  *description*: Returns a list of your expenses. If accessing this endpoint as an Administrator, all expenses in the account will be returned. If accessing this endpoint as a Manager, all expenses for assigned teammates and managed projects will be returned. The expenses are returned sorted by the spent_at date, with the most recent expenses appearing first.  The response contains an object with a expenses property that contains an array of up to per_page expenses. Each entry in the array is a separate expense object. If no more expenses are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your expenses.
* _GET /expenses/{expenseId}_ 
  *resource*: retrieve_expense  
  *description*: Retrieves the expense with the given ID. Returns an expense object and a 200 OK response code if a valid identifier was provided.
* _GET /expense_categories_ 
  *resource*: list_expense_categories  
  *description*: Returns a list of your expense categories. The expense categories are returned sorted by creation date, with the most recently created expense categories appearing first.  The response contains an object with a expense_categories property that contains an array of up to per_page expense categories. Each entry in the array is a separate expense category object. If no more expense categories are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your expense categories.
* _GET /expense_categories/{expenseCategoryId}_ 
  *resource*: retrieve_expense_category  
  *description*: Retrieves the expense category with the given ID. Returns an expense category object and a 200 OK response code if a valid identifier was provided.
* _GET /reports/expenses/categories_ 
  *resource*: expense_categories_report  
* _GET /reports/expenses/clients_ 
  *resource*: clients_expenses_report  
* _GET /reports/expenses/projects_ 
  *resource*: projects_expenses_report  
* _GET /reports/expenses/team_ 
  *resource*: team_expenses_report  
* _GET /invoices_ 
  *resource*: list_invoices  
  *description*: Returns a list of your invoices. The invoices are returned sorted by issue date, with the most recently issued invoices appearing first.  The response contains an object with a invoices property that contains an array of up to per_page invoices. Each entry in the array is a separate invoice object. If no more invoices are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your invoices.
* _GET /invoices/{invoiceId}_ 
  *resource*: retrieve_invoice  
  *description*: Retrieves the invoice with the given ID. Returns an invoice object and a 200 OK response code if a valid identifier was provided.
* _GET /invoice_item_categories_ 
  *resource*: list_invoice_item_categories  
  *description*: Returns a list of your invoice item categories. The invoice item categories are returned sorted by creation date, with the most recently created invoice item categories appearing first.  The response contains an object with a invoice_item_categories property that contains an array of up to per_page invoice item categories. Each entry in the array is a separate invoice item category object. If no more invoice item categories are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your invoice item categories.
* _GET /invoice_item_categories/{invoiceItemCategoryId}_ 
  *resource*: retrieve_invoice_item_category  
  *description*: Retrieves the invoice item category with the given ID. Returns an invoice item category object and a 200 OK response code if a valid identifier was provided.
* _GET /invoices/{invoiceId}/messages_ 
  *resource*: list_messages_for_invoice  
  *description*: Returns a list of messages associated with a given invoice. The invoice messages are returned sorted by creation date, with the most recently created messages appearing first.  The response contains an object with an invoice_messages property that contains an array of up to per_page messages. Each entry in the array is a separate message object. If no more messages are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your messages.
* _GET /invoices/{invoiceId}/messages/new_ 
  *resource*: retrieve_invoice_message_subject_and_body_for_specific_invoice  
  *description*: Returns the subject and body text as configured in Harvest of an invoice message for a specific invoice and a 200 OK response code if the call succeeded. Does not create the invoice message. If no parameters are passed, will return the subject and body of a general invoice message for the specific invoice.
* _GET /invoices/{invoiceId}/payments_ 
  *resource*: list_payments_for_invoice  
  *description*: Returns a list of payments associate with a given invoice. The payments are returned sorted by creation date, with the most recently created payments appearing first.  The response contains an object with an invoice_payments property that contains an array of up to per_page payments. Each entry in the array is a separate payment object. If no more payments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your payments.
* _GET /users/me_ 
  *resource*: retrieve_the_currently_authenticated_user  
  *description*: Retrieves the currently authenticated user. Returns a user object and a 200 OK response code.
* _GET /projects_ 
  *resource*: list_projects  
  *description*: Returns a list of your projects. The projects are returned sorted by creation date, with the most recently created projects appearing first.  The response contains an object with a projects property that contains an array of up to per_page projects. Each entry in the array is a separate project object. If no more projects are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your projects.
* _GET /projects/{projectId}_ 
  *resource*: retrieve_project  
  *description*: Retrieves the project with the given ID. Returns a project object and a 200 OK response code if a valid identifier was provided.
* _GET /users/me/project_assignments_ 
  *resource*: list_active_project_assignments_for_the_currently_authenticated_user  
  *description*: Returns a list of your active project assignments for the currently authenticated user. The project assignments are returned sorted by creation date, with the most recently created project assignments appearing first.  The response contains an object with a project_assignments property that contains an array of up to per_page project assignments. Each entry in the array is a separate project assignment object. If no more project assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your project assignments.
* _GET /users/{userId}/project_assignments_ 
  *resource*: list_active_project_assignments  
  *description*: Returns a list of active project assignments for the user identified by USER_ID. The project assignments are returned sorted by creation date, with the most recently created project assignments appearing first.  The response contains an object with a project_assignments property that contains an array of up to per_page project assignments. Each entry in the array is a separate project assignment object. If no more project assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your project assignments.
* _GET /reports/project_budget_ 
  *resource*: project_budget_report  
  *description*: The response contains an object with a results property that contains an array of up to per_page results. Each entry in the array is a separate result object. If no more results are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your results.
* _GET /roles_ 
  *resource*: list_roles  
  *description*: Returns a list of roles in the account. The roles are returned sorted by creation date, with the most recently created roles appearing first.  The response contains an object with a roles property that contains an array of up to per_page roles. Each entry in the array is a separate role object. If no more roles are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your roles.
* _GET /roles/{roleId}_ 
  *resource*: retrieve_role  
  *description*: Retrieves the role with the given ID. Returns a role object and a 200 OK response code if a valid identifier was provided.
* _GET /tasks_ 
  *resource*: list_tasks  
  *description*: Returns a list of your tasks. The tasks are returned sorted by creation date, with the most recently created tasks appearing first.  The response contains an object with a tasks property that contains an array of up to per_page tasks. Each entry in the array is a separate task object. If no more tasks are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your tasks.
* _GET /tasks/{taskId}_ 
  *resource*: retrieve_task  
  *description*: Retrieves the task with the given ID. Returns a task object and a 200 OK response code if a valid identifier was provided.
* _GET /projects/{projectId}/task_assignments_ 
  *resource*: list_task_assignments_for_specific_project  
  *description*: Returns a list of your task assignments for the project identified by PROJECT_ID. The task assignments are returned sorted by creation date, with the most recently created task assignments appearing first.  The response contains an object with a task_assignments property that contains an array of up to per_page task assignments. Each entry in the array is a separate task assignment object. If no more task assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your task assignments.
* _GET /projects/{projectId}/task_assignments/{taskAssignmentId}_ 
  *resource*: retrieve_task_assignment  
  *description*: Retrieves the task assignment with the given ID. Returns a task assignment object and a 200 OK response code if a valid identifier was provided.
* _GET /task_assignments_ 
  *resource*: list_task_assignments  
  *description*: Returns a list of your task assignments. The task assignments are returned sorted by creation date, with the most recently created task assignments appearing first.  The response contains an object with a task_assignments property that contains an array of up to per_page task assignments. Each entry in the array is a separate task assignment object. If no more task assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your task assignments.
* _GET /users/{userId}/teammates_ 
  *resource*: list_assigned_teammates_for_specific_user  
  *description*: Returns a list of assigned teammates for the user identified by USER_ID. The USER_ID must belong to a user that is a Manager, if not, a 422 Unprocessable Entity status code will be returned.  The response contains an object with a teammates property that contains an array of up to per_page teammates. Each entry in the array is a separate teammate object. If no more teammates are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your teammates.
* _GET /time_entries_ 
  *resource*: list_time_entries  
  *description*: Returns a list of time entries. The time entries are returned sorted by spent_date date. At this time, the sort option can’t be customized.  The response contains an object with a time_entries property that contains an array of up to per_page time entries. Each entry in the array is a separate time entry object. If no more time entries are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your time entries.
* _GET /time_entries/{timeEntryId}_ 
  *resource*: retrieve_time_entry  
  *description*: Retrieves the time entry with the given ID. Returns a time entry object and a 200 OK response code if a valid identifier was provided.
* _GET /reports/time/clients_ 
  *resource*: clients_time_report  
* _GET /reports/time/projects_ 
  *resource*: projects_time_report  
* _GET /reports/time/tasks_ 
  *resource*: tasks_report  
* _GET /reports/time/team_ 
  *resource*: team_time_report  
* _GET /reports/uninvoiced_ 
  *resource*: uninvoiced_report  
  *description*: The response contains an object with a results property that contains an array of up to per_page results. Each entry in the array is a separate result object. If no more results are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your results.  Note: Each request requires both the from and to parameters to be supplied in the URL’s query string. The timeframe supplied cannot exceed 1 year (365 days).
* _GET /users_ 
  *resource*: list_users  
  *description*: Returns a list of your users. The users are returned sorted by creation date, with the most recently created users appearing first.  The response contains an object with a users property that contains an array of up to per_page users. Each entry in the array is a separate user object. If no more users are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your users.
* _GET /users/{userId}_ 
  *resource*: retrieve_user  
  *description*: Retrieves the user with the given ID. Returns a user object and a 200 OK response code if a valid identifier was provided.
* _GET /projects/{projectId}/user_assignments_ 
  *resource*: list_user_assignments_for_specific_project  
  *description*: Returns a list of user assignments for the project identified by PROJECT_ID. The user assignments are returned sorted by creation date, with the most recently created user assignments appearing first.  The response contains an object with a user_assignments property that contains an array of up to per_page user assignments. Each entry in the array is a separate user assignment object. If no more user assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your user assignments.
* _GET /projects/{projectId}/user_assignments/{userAssignmentId}_ 
  *resource*: retrieve_user_assignment  
  *description*: Retrieves the user assignment with the given ID. Returns a user assignment object and a 200 OK response code if a valid identifier was provided.
* _GET /user_assignments_ 
  *resource*: list_user_assignments  
  *description*: Returns a list of your projects user assignments, active and archived. The user assignments are returned sorted by creation date, with the most recently created user assignments appearing first.  The response contains an object with a user_assignments property that contains an array of up to per_page user assignments. Each entry in the array is a separate user assignment object. If no more user assignments are available, the resulting array will be empty. Several additional pagination properties are included in the response to simplify paginating your user assignments.
