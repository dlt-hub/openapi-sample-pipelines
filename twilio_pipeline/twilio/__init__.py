from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="twilio_source", max_table_nesting=2)
def twilio_source(
    username: str = dlt.secrets.value,
    password: str = dlt.secrets.value,
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "auth": {
                "type": "http_basic",
                "username": username,
                "password": password,
            },
            "paginator": {
                "type": "page_number",
                "page_param": "Page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            # Retrieves a collection of Accounts belonging to the account used to make the request
            {
                "name": "list_account",
                "table_name": "api_v2010_account",
                "endpoint": {
                    "data_selector": "accounts",
                    "path": "/2010-04-01/Accounts.json",
                    "params": {
                        # the parameters below can optionally be configured
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "Status": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch the account specified by the provided Account Sid
            {
                "name": "fetch_account",
                "table_name": "api_v2010_account",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_account",
                            "field": "sid",
                        },
                    },
                },
            },
            # An Address instance resource represents your or your customer's physical location within a country. Around the world, some local authorities require the name and address of the user to be on file with Twilio to purchase and own a phone number.
            {
                "name": "list_address",
                "table_name": "api_v2010_account_address",
                "endpoint": {
                    "data_selector": "addresses",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Addresses.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "CustomerName": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "IsoCountry": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # An Address instance resource represents your or your customer's physical location within a country. Around the world, some local authorities require the name and address of the user to be on file with Twilio to purchase and own a phone number.
            {
                "name": "fetch_address",
                "table_name": "api_v2010_account_address",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_address",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Phone numbers dependent on an Address resource
            {
                "name": "list_dependent_phone_number",
                "table_name": "api_v2010_account_address_dependent_phone_number",
                "endpoint": {
                    "data_selector": "dependent_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "AddressSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of applications representing an application within the requesting account
            {
                "name": "list_application",
                "table_name": "api_v2010_account_application",
                "endpoint": {
                    "data_selector": "applications",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Applications.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch the application specified by the provided sid
            {
                "name": "fetch_application",
                "table_name": "api_v2010_account_application",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_application",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetch an instance of an authorized-connect-app
            {
                "name": "fetch_authorized_connect_app",
                "table_name": "api_v2010_account_authorized_connect_app",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps/{ConnectAppSid}.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ConnectAppSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of authorized-connect-apps belonging to the account used to make the request
            {
                "name": "list_authorized_connect_app",
                "table_name": "api_v2010_account_authorized_connect_app",
                "endpoint": {
                    "data_selector": "authorized_connect_apps",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Country codes with available phone numbers
            {
                "name": "list_available_phone_number_country",
                "table_name": "api_v2010_account_available_phone_number_country",
                "endpoint": {
                    "data_selector": "countries",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Country codes with available phone numbers
            {
                "name": "fetch_available_phone_number_country",
                "table_name": "api_v2010_account_available_phone_number_country",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Available local phone numbers
            {
                "name": "list_available_phone_number_local",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_local",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Local.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Available machine-to-machine phone numbers
            {
                "name": "list_available_phone_number_machine_to_machine",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_machine_to_machine",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/MachineToMachine.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Available mobile phone numbers
            {
                "name": "list_available_phone_number_mobile",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_mobile",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Mobile.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Available national phone numbers
            {
                "name": "list_available_phone_number_national",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_national",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/National.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Available shared cost numbers
            {
                "name": "list_available_phone_number_shared_cost",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_shared_cost",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/SharedCost.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Available toll free phone numbers
            {
                "name": "list_available_phone_number_toll_free",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_toll_free",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/TollFree.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Available VoIP phone numbers
            {
                "name": "list_available_phone_number_voip",
                "table_name": "api_v2010_account_available_phone_number_country_available_phone_number_voip",
                "endpoint": {
                    "data_selector": "available_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Voip.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CountryCode": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "AreaCode": "OPTIONAL_CONFIG",
                        # "Contains": "OPTIONAL_CONFIG",
                        # "SmsEnabled": "OPTIONAL_CONFIG",
                        # "MmsEnabled": "OPTIONAL_CONFIG",
                        # "VoiceEnabled": "OPTIONAL_CONFIG",
                        # "ExcludeAllAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeLocalAddressRequired": "OPTIONAL_CONFIG",
                        # "ExcludeForeignAddressRequired": "OPTIONAL_CONFIG",
                        # "Beta": "OPTIONAL_CONFIG",
                        # "NearNumber": "OPTIONAL_CONFIG",
                        # "NearLatLong": "OPTIONAL_CONFIG",
                        # "Distance": "OPTIONAL_CONFIG",
                        # "InPostalCode": "OPTIONAL_CONFIG",
                        # "InRegion": "OPTIONAL_CONFIG",
                        # "InRateCenter": "OPTIONAL_CONFIG",
                        # "InLata": "OPTIONAL_CONFIG",
                        # "InLocality": "OPTIONAL_CONFIG",
                        # "FaxEnabled": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately. Child accounts do not contain balance information
            {
                "name": "fetch_balance",
                "table_name": "api_v2010_account_balance",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Balance.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieves a collection of calls made to and from your account
            {
                "name": "list_call",
                "table_name": "api_v2010_account_call",
                "endpoint": {
                    "data_selector": "calls",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "To": "OPTIONAL_CONFIG",
                        # "From": "OPTIONAL_CONFIG",
                        # "ParentCallSid": "OPTIONAL_CONFIG",
                        # "Status": "OPTIONAL_CONFIG",
                        # "StartTime": "OPTIONAL_CONFIG",
                        # "StartTime<": "OPTIONAL_CONFIG",
                        # "StartTime>": "OPTIONAL_CONFIG",
                        # "EndTime": "OPTIONAL_CONFIG",
                        # "EndTime<": "OPTIONAL_CONFIG",
                        # "EndTime>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch the call specified by the provided Call SID
            {
                "name": "fetch_call",
                "table_name": "api_v2010_account_call",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_call",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of all events for a call.
            {
                "name": "list_call_event",
                "table_name": "api_v2010_account_call_call_event",
                "endpoint": {
                    "data_selector": "events",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Events.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Error notifications for calls
            {
                "name": "list_call_notification",
                "table_name": "api_v2010_account_call_call_notification",
                "endpoint": {
                    "data_selector": "notifications",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Log": "OPTIONAL_CONFIG",
                        # "MessageDate": "OPTIONAL_CONFIG",
                        # "MessageDate<": "OPTIONAL_CONFIG",
                        # "MessageDate>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Error notifications for calls
            {
                "name": "fetch_call_notification",
                "table_name": "api_v2010_account_call_call_notification_instance",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_call_notification",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of recordings belonging to the call used to make the request
            {
                "name": "list_call_recording",
                "table_name": "api_v2010_account_call_call_recording",
                "endpoint": {
                    "data_selector": "recordings",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "DateCreated": "OPTIONAL_CONFIG",
                        # "DateCreated<": "OPTIONAL_CONFIG",
                        # "DateCreated>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a recording for a call
            {
                "name": "fetch_call_recording",
                "table_name": "api_v2010_account_call_call_recording",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_call_recording",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetch an instance of a conference
            {
                "name": "fetch_conference",
                "table_name": "api_v2010_account_conference",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_conference",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of conferences belonging to the account used to make the request
            {
                "name": "list_conference",
                "table_name": "api_v2010_account_conference",
                "endpoint": {
                    "data_selector": "conferences",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Conferences.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "DateCreated": "OPTIONAL_CONFIG",
                        # "DateCreated<": "OPTIONAL_CONFIG",
                        # "DateCreated>": "OPTIONAL_CONFIG",
                        # "DateUpdated": "OPTIONAL_CONFIG",
                        # "DateUpdated<": "OPTIONAL_CONFIG",
                        # "DateUpdated>": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "Status": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a recording for a call
            {
                "name": "fetch_conference_recording",
                "table_name": "api_v2010_account_conference_conference_recording",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_conference_recording",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ConferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of recordings belonging to the call used to make the request
            {
                "name": "list_conference_recording",
                "table_name": "api_v2010_account_conference_conference_recording",
                "endpoint": {
                    "data_selector": "recordings",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ConferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "DateCreated": "OPTIONAL_CONFIG",
                        # "DateCreated<": "OPTIONAL_CONFIG",
                        # "DateCreated>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a participant
            {
                "name": "fetch_participant",
                "table_name": "api_v2010_account_conference_participant",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ConferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of participants belonging to the account used to make the request
            {
                "name": "list_participant",
                "table_name": "api_v2010_account_conference_participant",
                "endpoint": {
                    "data_selector": "participants",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ConferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Muted": "OPTIONAL_CONFIG",
                        # "Hold": "OPTIONAL_CONFIG",
                        # "Coaching": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a connect-app
            {
                "name": "fetch_connect_app",
                "table_name": "api_v2010_account_connect_app",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_connect_app",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of connect-apps belonging to the account used to make the request
            {
                "name": "list_connect_app",
                "table_name": "api_v2010_account_connect_app",
                "endpoint": {
                    "data_selector": "connect_apps",
                    "path": "/2010-04-01/Accounts/{AccountSid}/ConnectApps.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an incoming-phone-number belonging to the account used to make the request.
            {
                "name": "fetch_incoming_phone_number",
                "table_name": "api_v2010_account_incoming_phone_number",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_incoming_phone_number",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.
            {
                "name": "list_incoming_phone_number",
                "table_name": "api_v2010_account_incoming_phone_number",
                "endpoint": {
                    "data_selector": "incoming_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Beta": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "PhoneNumber": "OPTIONAL_CONFIG",
                        # "Origin": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of an Add-on installation currently assigned to this Number.
            {
                "name": "fetch_incoming_phone_number_assigned_add_on",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_incoming_phone_number_assigned_add_on",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ResourceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of Add-on installations currently assigned to this Number.
            {
                "name": "list_incoming_phone_number_assigned_add_on",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on",
                "endpoint": {
                    "data_selector": "assigned_add_ons",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ResourceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of an Extension for the Assigned Add-on.
            {
                "name": "fetch_incoming_phone_number_assigned_add_on_extension",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on_incoming_phone_number_assigned_add_on_extension",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_incoming_phone_number_assigned_add_on_extension",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ResourceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "AssignedAddOnSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of Extensions for the Assigned Add-on.
            {
                "name": "list_incoming_phone_number_assigned_add_on_extension",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_assigned_add_on_incoming_phone_number_assigned_add_on_extension",
                "endpoint": {
                    "data_selector": "extensions",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ResourceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "AssignedAddOnSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Incoming local phone numbers on a Twilio account/project
            {
                "name": "list_incoming_phone_number_local",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_local",
                "endpoint": {
                    "data_selector": "incoming_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Beta": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "PhoneNumber": "OPTIONAL_CONFIG",
                        # "Origin": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Incoming mobile phone numbers on a Twilio account/project
            {
                "name": "list_incoming_phone_number_mobile",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_mobile",
                "endpoint": {
                    "data_selector": "incoming_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Mobile.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Beta": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "PhoneNumber": "OPTIONAL_CONFIG",
                        # "Origin": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Incoming toll free phone numbers on a Twilio account/project
            {
                "name": "list_incoming_phone_number_toll_free",
                "table_name": "api_v2010_account_incoming_phone_number_incoming_phone_number_toll_free",
                "endpoint": {
                    "data_selector": "incoming_phone_numbers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/TollFree.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Beta": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "PhoneNumber": "OPTIONAL_CONFIG",
                        # "Origin": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # API keys
            {
                "name": "fetch_key",
                "table_name": "api_v2010_account_key",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Keys/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_key",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # API keys
            {
                "name": "list_key",
                "table_name": "api_v2010_account_key",
                "endpoint": {
                    "data_selector": "keys",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Keys.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of Message resources associated with a Twilio Account
            {
                "name": "list_message",
                "table_name": "api_v2010_account_message",
                "endpoint": {
                    "data_selector": "messages",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Messages.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "To": "OPTIONAL_CONFIG",
                        # "From": "OPTIONAL_CONFIG",
                        # "DateSent": "OPTIONAL_CONFIG",
                        # "DateSent<": "OPTIONAL_CONFIG",
                        # "DateSent>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a specific Message
            {
                "name": "fetch_message",
                "table_name": "api_v2010_account_message",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_message",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetch a single Media resource associated with a specific Message resource
            {
                "name": "fetch_media",
                "table_name": "api_v2010_account_message_media",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_media",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "MessageSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Read a list of Media resources associated with a specific Message resource
            {
                "name": "list_media",
                "table_name": "api_v2010_account_message_media",
                "endpoint": {
                    "data_selector": "media_list",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "MessageSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "DateCreated": "OPTIONAL_CONFIG",
                        # "DateCreated<": "OPTIONAL_CONFIG",
                        # "DateCreated>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of notifications belonging to the account used to make the request
            {
                "name": "list_notification",
                "table_name": "api_v2010_account_notification",
                "endpoint": {
                    "data_selector": "notifications",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Notifications.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Log": "OPTIONAL_CONFIG",
                        # "MessageDate": "OPTIONAL_CONFIG",
                        # "MessageDate<": "OPTIONAL_CONFIG",
                        # "MessageDate>": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a notification belonging to the account used to make the request
            {
                "name": "fetch_notification",
                "table_name": "api_v2010_account_notification_instance",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_notification",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetch an outgoing-caller-id belonging to the account used to make the request
            {
                "name": "fetch_outgoing_caller_id",
                "table_name": "api_v2010_account_outgoing_caller_id",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_outgoing_caller_id",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of outgoing-caller-ids belonging to the account used to make the request
            {
                "name": "list_outgoing_caller_id",
                "table_name": "api_v2010_account_outgoing_caller_id",
                "endpoint": {
                    "data_selector": "outgoing_caller_ids",
                    "path": "/2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PhoneNumber": "OPTIONAL_CONFIG",
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a queue identified by the QueueSid
            {
                "name": "fetch_queue",
                "table_name": "api_v2010_account_queue",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_queue",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of queues belonging to the account used to make the request
            {
                "name": "list_queue",
                "table_name": "api_v2010_account_queue",
                "endpoint": {
                    "data_selector": "queues",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Queues.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a specific member from the queue
            {
                "name": "fetch_member",
                "table_name": "api_v2010_account_queue_member",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "QueueSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CallSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve the members of the queue
            {
                "name": "list_member",
                "table_name": "api_v2010_account_queue_member",
                "endpoint": {
                    "data_selector": "queue_members",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "QueueSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a recording
            {
                "name": "fetch_recording",
                "table_name": "api_v2010_account_recording",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_recording",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "IncludeSoftDeleted": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of recordings belonging to the account used to make the request
            {
                "name": "list_recording",
                "table_name": "api_v2010_account_recording",
                "endpoint": {
                    "data_selector": "recordings",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "DateCreated": "OPTIONAL_CONFIG",
                        # "DateCreated<": "OPTIONAL_CONFIG",
                        # "DateCreated>": "OPTIONAL_CONFIG",
                        # "CallSid": "OPTIONAL_CONFIG",
                        # "ConferenceSid": "OPTIONAL_CONFIG",
                        # "IncludeSoftDeleted": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of an AddOnResult
            {
                "name": "fetch_recording_add_on_result",
                "table_name": "api_v2010_account_recording_recording_add_on_result",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_recording_add_on_result",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ReferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of results belonging to the recording
            {
                "name": "list_recording_add_on_result",
                "table_name": "api_v2010_account_recording_recording_add_on_result",
                "endpoint": {
                    "data_selector": "add_on_results",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ReferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a result payload
            {
                "name": "fetch_recording_add_on_result_payload",
                "table_name": "api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_recording_add_on_result_payload",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ReferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "AddOnResultSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of payloads belonging to the AddOnResult
            {
                "name": "list_recording_add_on_result_payload",
                "table_name": "api_v2010_account_recording_recording_add_on_result_recording_add_on_result_payload",
                "endpoint": {
                    "data_selector": "payloads",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "ReferenceSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "AddOnResultSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # References to text transcriptions of call recordings
            {
                "name": "fetch_recording_transcription",
                "table_name": "api_v2010_account_recording_recording_transcription",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_recording_transcription",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "RecordingSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # References to text transcriptions of call recordings
            {
                "name": "list_recording_transcription",
                "table_name": "api_v2010_account_recording_recording_transcription",
                "endpoint": {
                    "data_selector": "transcriptions",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "RecordingSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a short code
            {
                "name": "fetch_short_code",
                "table_name": "api_v2010_account_short_code",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_short_code",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of short-codes belonging to the account used to make the request
            {
                "name": "list_short_code",
                "table_name": "api_v2010_account_short_code",
                "endpoint": {
                    "data_selector": "short_codes",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "FriendlyName": "OPTIONAL_CONFIG",
                        # "ShortCode": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Create a new signing key
            {
                "name": "list_signing_key",
                "table_name": "api_v2010_account_signing_key",
                "endpoint": {
                    "data_selector": "signing_keys",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SigningKeys.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # TODO: Resource-level docs
            {
                "name": "fetch_signing_key",
                "table_name": "api_v2010_account_signing_key",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_signing_key",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Get All Credential Lists
            {
                "name": "list_sip_credential_list",
                "table_name": "api_v2010_account_sip_sip_credential_list",
                "endpoint": {
                    "data_selector": "credential_lists",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Get a Credential List
            {
                "name": "fetch_sip_credential_list",
                "table_name": "api_v2010_account_sip_sip_credential_list",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_credential_list",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of credentials.
            {
                "name": "list_sip_credential",
                "table_name": "api_v2010_account_sip_sip_credential_list_sip_credential",
                "endpoint": {
                    "data_selector": "credentials",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CredentialListSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a single credential.
            {
                "name": "fetch_sip_credential",
                "table_name": "api_v2010_account_sip_sip_credential_list_sip_credential",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_credential",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "CredentialListSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of domains belonging to the account used to make the request
            {
                "name": "list_sip_domain",
                "table_name": "api_v2010_account_sip_sip_domain",
                "endpoint": {
                    "data_selector": "domains",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch an instance of a Domain
            {
                "name": "fetch_sip_domain",
                "table_name": "api_v2010_account_sip_sip_domain",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_domain",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of credential list mappings belonging to the domain used in the request
            {
                "name": "list_sip_auth_calls_credential_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_credential_list_mapping",
                "endpoint": {
                    "data_selector": "contents",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a specific instance of a credential list mapping
            {
                "name": "fetch_sip_auth_calls_credential_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_credential_list_mapping",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_auth_calls_credential_list_mapping",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of IP Access Control List mappings belonging to the domain used in the request
            {
                "name": "list_sip_auth_calls_ip_access_control_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_ip_access_control_list_mapping",
                "endpoint": {
                    "data_selector": "contents",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a specific instance of an IP Access Control List mapping
            {
                "name": "fetch_sip_auth_calls_ip_access_control_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_auth_sip_auth_calls_sip_auth_calls_ip_access_control_list_mapping",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_auth_calls_ip_access_control_list_mapping",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of credential list mappings belonging to the domain used in the request
            {
                "name": "list_sip_auth_registrations_credential_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_auth_sip_auth_registrations_sip_auth_registrations_credential_list_mapping",
                "endpoint": {
                    "data_selector": "contents",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a specific instance of a credential list mapping
            {
                "name": "fetch_sip_auth_registrations_credential_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_auth_sip_auth_registrations_sip_auth_registrations_credential_list_mapping",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_auth_registrations_credential_list_mapping",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Read multiple CredentialListMapping resources from an account.
            {
                "name": "list_sip_credential_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_credential_list_mapping",
                "endpoint": {
                    "data_selector": "credential_list_mappings",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a single CredentialListMapping resource from an account.
            {
                "name": "fetch_sip_credential_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_credential_list_mapping",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_credential_list_mapping",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetch an IpAccessControlListMapping resource.
            {
                "name": "fetch_sip_ip_access_control_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_ip_access_control_list_mapping",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_ip_access_control_list_mapping",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of IpAccessControlListMapping resources.
            {
                "name": "list_sip_ip_access_control_list_mapping",
                "table_name": "api_v2010_account_sip_sip_domain_sip_ip_access_control_list_mapping",
                "endpoint": {
                    "data_selector": "ip_access_control_list_mappings",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "DomainSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of IpAccessControlLists that belong to the account used to make the request
            {
                "name": "list_sip_ip_access_control_list",
                "table_name": "api_v2010_account_sip_sip_ip_access_control_list",
                "endpoint": {
                    "data_selector": "ip_access_control_lists",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch a specific instance of an IpAccessControlList
            {
                "name": "fetch_sip_ip_access_control_list",
                "table_name": "api_v2010_account_sip_sip_ip_access_control_list",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_ip_access_control_list",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Read multiple IpAddress resources.
            {
                "name": "list_sip_ip_address",
                "table_name": "api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address",
                "endpoint": {
                    "data_selector": "ip_addresses",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "IpAccessControlListSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Read one IpAddress resource.
            {
                "name": "fetch_sip_ip_address",
                "table_name": "api_v2010_account_sip_sip_ip_access_control_list_sip_ip_address",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_sip_ip_address",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "IpAccessControlListSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Fetch an instance of a Transcription
            {
                "name": "fetch_transcription",
                "table_name": "api_v2010_account_transcription",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_transcription",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of transcriptions belonging to the account used to make the request
            {
                "name": "list_transcription",
                "table_name": "api_v2010_account_transcription",
                "endpoint": {
                    "data_selector": "transcriptions",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Transcriptions.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve a list of usage-records belonging to the account used to make the request
            {
                "name": "list_usage_record",
                "table_name": "api_v2010_account_usage_usage_record",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records for all time
            {
                "name": "list_usage_record_all_time",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_all_time",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/AllTime.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records summarized by day
            {
                "name": "list_usage_record_daily",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_daily",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/Daily.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records for last month
            {
                "name": "list_usage_record_last_month",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_last_month",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/LastMonth.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records summarized by month
            {
                "name": "list_usage_record_monthly",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_monthly",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/Monthly.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records for this month
            {
                "name": "list_usage_record_this_month",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_this_month",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/ThisMonth.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records for today
            {
                "name": "list_usage_record_today",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_today",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/Today.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records summarized by year
            {
                "name": "list_usage_record_yearly",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_yearly",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/Yearly.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Usage records for yesterday
            {
                "name": "list_usage_record_yesterday",
                "table_name": "api_v2010_account_usage_usage_record_usage_record_yesterday",
                "endpoint": {
                    "data_selector": "usage_records",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Records/Yesterday.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Category": "OPTIONAL_CONFIG",
                        # "StartDate": "OPTIONAL_CONFIG",
                        # "EndDate": "OPTIONAL_CONFIG",
                        # "IncludeSubaccounts": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Fetch and instance of a usage-trigger
            {
                "name": "fetch_usage_trigger",
                "table_name": "api_v2010_account_usage_usage_trigger",
                "primary_key": "sid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json",
                    "params": {
                        "Sid": {
                            "type": "resolve",
                            "resource": "list_usage_trigger",
                            "field": "sid",
                        },
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                },
            },
            # Retrieve a list of usage-triggers belonging to the account used to make the request
            {
                "name": "list_usage_trigger",
                "table_name": "api_v2010_account_usage_usage_trigger",
                "endpoint": {
                    "data_selector": "usage_triggers",
                    "path": "/2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json",
                    "params": {
                        "AccountSid": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "Recurring": "OPTIONAL_CONFIG",
                        # "TriggerBy": "OPTIONAL_CONFIG",
                        # "UsageCategory": "OPTIONAL_CONFIG",
                        # "PageSize": "OPTIONAL_CONFIG",
                        # "PageToken": "OPTIONAL_CONFIG",
                    },
                },
            },
            # API HealthCheck
            {
                "name": "fetch_health_check",
                "table_name": "healthcheck",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/healthcheck",
                },
            },
        ],
    }

    return rest_api_source(source_config)
