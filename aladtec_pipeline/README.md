# aladtec pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/aladtec.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['token'] in your 
secrets.toml.

## Available resources
* _GET /accrual-banks_ 
  *resource*: accrual_bank  
  *description*: Returns a list of all accrual banks.
* _GET /availability_ 
  *resource*: availability  
  *description*: Returns Member Availability for the requested date/time range.
* _GET /accrual-banks/balances_ 
  *resource*: balance  
  *description*: Returns the number of hours in each specified accrual bank for a list of provided members.
* _GET /time-clock-time/clocked-in-members_ 
  *resource*: clocked_in_member  
  *description*: Members clocked in at the time of the request.
* _GET /configuration_ 
  *resource*: configuration  
  *description*: Returns a list of configuration settings.
* _GET /members/custom-attributes_ 
  *resource*: custom_attribute  
  *description*: Returns all customer created Member Database attribute definitions.
* _GET /members/employee-types_ 
  *resource*: employee_type  
  *description*: Returns all employee types. These can be customized per Aladtec system. Examples: part time, full time, volunteer.
* _GET /events_ 
  *resource*: event  
  *description*: Events for requested date/time range.
* _GET /extra-hours_ 
  *resource*: extra_hour  
  *description*: Returns extra hours ranges for a specified period of time in the past.
* _GET /time-clock/kiosks_ 
  *resource*: kiosk  
  *description*: Returns a list of unique, active Kiosks used to clock in and out.
* _GET /members_ 
  *resource*: member  
  *description*: Returns members and the members' associated Member Database attributes. Attributes must be accessible through the API or the value will be null. Contact Aladtec Support (support@aladtec.com, 888.749.5550) to make attributes accessible through the API.
* _GET /scheduled-time/members-scheduled-now_ 
  *resource*: members_scheduled_now  
  *description*: Schedule and position for each member scheduled at the time of the request.
* _GET /scheduled-time/notes_ 
  *resource*: note  
  *description*: Returns Schedule Notes grouped by calendar date. Up to one year can be retrieved in a single request.
* _GET /scheduled-time/open-time_ 
  *resource*: open_time  
  *description*: Returns time ranges where no member is scheduled. Typically used for finding shifts needing coverage. Up to one month can be retrieved in a single request.
* _GET /time-clock/paycodes_ 
  *resource*: paycode  
  *description*: Returns a list of unique, active Paycodes which can be applied to time clock time.
* _GET /reports/payroll_ 
  *resource*: payroll  
  *description*: Runs the Payroll Report export.  <strong>Pagination is required</strong> to export all records within the requested range. 
* _GET /schedules/position-qualifications_ 
  *resource*: position_qualification  
  *description*: Returns a list of unique position qualifications.
* _GET /schedules_ 
  *resource*: schedule  
  *description*: Schedule configuration defined in an Aladtec system. Data is sorted by the order defined on the Setup -> Schedules page.
* _GET /scheduled-time_ 
  *resource*: scheduled_time  
  *description*: Returns scheduled time ranges for a specified period of time
* _GET /shift-labels_ 
  *resource*: shift_label  
  *description*: Shift Labels for requested date range.
* _GET /time-clock-time_ 
  *resource*: time_clock_time  
  *description*: Time Clock records for the requested date/time range. If a member is clocked in at the time of the request, the time clock record will be excluded.
* _GET /time-off_ 
  *resource*: time_off  
  *description*: Approved and pending Time Off ranges for the requested date/time range. Note: By default, only approved Time Off ranges are included in the response. 
* _GET /time-types_ 
  *resource*: time_type  
  *description*: Returns a list of unique Time Types which can be applied to scheduled time.
* _GET /time-off/types_ 
  *resource*: type  
  *description*: Returns all active Time Off Types.
* _GET /work-groups_ 
  *resource*: work_group  
  *description*: Returns all work groups. Work groups are used for putting members into groups if they follow the same schedule and work limit rules. Work groups can be customized per Aladtec system.
