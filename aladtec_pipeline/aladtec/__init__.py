from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="aladtec_source", max_table_nesting=2)
def aladtec_source(
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
                "type": "offset",
                "limit": 100,
                "offset_param": "offset",
                "limit_param": "limit",
                "total_path": "",
                "maximum_offset": 20,
            },
        },
        "resources": [
            # Returns a list of all accrual banks.
            {
                "name": "accrual_bank",
                "table_name": "accrual_bank",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/accrual-banks",
                },
            },
            # Returns Member Availability for the requested date/time range.
            {
                "name": "availability",
                "table_name": "availability",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/availability",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Returns the number of hours in each specified accrual bank for a list of provided members.
            {
                "name": "balance",
                "table_name": "balance",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/accrual-banks/balances",
                    "params": {
                        "member_ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "accrual_bank_ids": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Members clocked in at the time of the request.
            {
                "name": "clocked_in_member",
                "table_name": "clocked_in_member",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-clock-time/clocked-in-members",
                },
            },
            # Returns a list of configuration settings.
            {
                "name": "configuration",
                "table_name": "configuration",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/configuration",
                },
            },
            # Returns all customer created Member Database attribute definitions.
            {
                "name": "custom_attribute",
                "table_name": "custom_attribute",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/members/custom-attributes",
                },
            },
            # Returns all employee types. These can be customized per Aladtec system. Examples: part time, full time, volunteer.
            {
                "name": "employee_type",
                "table_name": "employee_type",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/members/employee-types",
                },
            },
            # Events for requested date/time range.
            {
                "name": "event",
                "table_name": "event",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/events",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "daily_split_time": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns extra hours ranges for a specified period of time in the past.
            {
                "name": "extra_hour",
                "table_name": "extra_hour",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/extra-hours",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "schedule_ids": "OPTIONAL_CONFIG",
                        # "member_ids": "OPTIONAL_CONFIG",
                        # "position_qualification_ids": "OPTIONAL_CONFIG",
                        # "time_type_ids": "OPTIONAL_CONFIG",
                        # "statuses": "approved",
                        # "daily_split_time": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of unique, active Kiosks used to clock in and out.
            {
                "name": "kiosk",
                "table_name": "kiosk",
                "primary_key": "kiosk_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-clock/kiosks",
                },
            },
            # Returns members and the members' associated Member Database attributes. Attributes must be accessible through the API or the value will be null. Contact Aladtec Support (support@aladtec.com, 888.749.5550) to make attributes accessible through the API.
            {
                "name": "member",
                "table_name": "member",
                "primary_key": "member_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/members",
                    "params": {
                        # the parameters below can optionally be configured
                        # "member_ids": "OPTIONAL_CONFIG",
                        # "include_inactive": "false",
                        # "attribute_ids": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Schedule and position for each member scheduled at the time of the request.
            {
                "name": "members_scheduled_now",
                "table_name": "members_scheduled_now",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/scheduled-time/members-scheduled-now",
                    "params": {
                        # the parameters below can optionally be configured
                        # "schedule_ids": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns Schedule Notes grouped by calendar date. Up to one year can be retrieved in a single request.
            {
                "name": "note",
                "table_name": "note",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/scheduled-time/notes",
                    "params": {
                        "range_start_date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "schedule_ids": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns time ranges where no member is scheduled. Typically used for finding shifts needing coverage. Up to one month can be retrieved in a single request.
            {
                "name": "open_time",
                "table_name": "open_time",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/scheduled-time/open-time",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "schedule_ids": "OPTIONAL_CONFIG",
                        # "position_ids": "OPTIONAL_CONFIG",
                        # "include_only_shift_time": "true",
                        # "daily_split_time": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of unique, active Paycodes which can be applied to time clock time.
            {
                "name": "paycode",
                "table_name": "paycode",
                "primary_key": "paycode_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-clock/paycodes",
                },
            },
            # Runs the Payroll Report export.  <strong>Pagination is required</strong> to export all records within the requested range.
            {
                "name": "payroll",
                "table_name": "payroll",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/reports/payroll",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "member_ids": "OPTIONAL_CONFIG",
                        # "time_categories": "OPTIONAL_CONFIG",
                        # "next_token": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of unique position qualifications.
            {
                "name": "position_qualification",
                "table_name": "position_qualification",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/schedules/position-qualifications",
                },
            },
            # Schedule configuration defined in an Aladtec system. Data is sorted by the order defined on the Setup -> Schedules page.
            {
                "name": "schedule",
                "table_name": "schedule",
                "primary_key": "schedule_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/schedules",
                    "params": {
                        # the parameters below can optionally be configured
                        # "include_archived": "false",
                    },
                },
            },
            # Returns scheduled time ranges for a specified period of time
            {
                "name": "scheduled_time",
                "table_name": "scheduled_time",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/scheduled-time",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "schedule_ids": "OPTIONAL_CONFIG",
                        # "member_ids": "OPTIONAL_CONFIG",
                        # "position_ids": "OPTIONAL_CONFIG",
                        # "time_type_ids": "OPTIONAL_CONFIG",
                        # "daily_split_time": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Shift Labels for requested date range.
            {
                "name": "shift_label",
                "table_name": "shift_label",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/shift-labels",
                    "params": {
                        "range_start_date": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_date": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Time Clock records for the requested date/time range. If a member is clocked in at the time of the request, the time clock record will be excluded.
            {
                "name": "time_clock_time",
                "table_name": "time_clock_time",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-clock-time",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # Approved and pending Time Off ranges for the requested date/time range. Note: By default, only approved Time Off ranges are included in the response.
            {
                "name": "time_off",
                "table_name": "time_off",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-off",
                    "params": {
                        "range_start_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "range_stop_datetime": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "statuses": "approved",
                        # "daily_split_time": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of unique Time Types which can be applied to scheduled time.
            {
                "name": "time_type",
                "table_name": "time_type",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-types",
                },
            },
            # Returns all active Time Off Types.
            {
                "name": "type",
                "table_name": "type",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/time-off/types",
                },
            },
            # Returns all work groups. Work groups are used for putting members into groups if they follow the same schedule and work limit rules. Work groups can be customized per Aladtec system.
            {
                "name": "work_group",
                "table_name": "work_group",
                "endpoint": {
                    "data_selector": "data",
                    "path": "/work-groups",
                },
            },
        ],
    }

    return rest_api_source(source_config)
