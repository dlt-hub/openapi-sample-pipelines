# twilio pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/twilio.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses http authentication. Please fill in the required variables ['username', 'password'] in your 
secrets.toml.

## Available resources
* _GET /2010-04-01/Accounts.json_ 
  *resource*: list_account  
  *description*: Retrieves a collection of Accounts belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{Sid}.json_ 
  *resource*: fetch_account  
  *description*: Fetch the account specified by the provided Account Sid
* _GET /2010-04-01/Accounts/{AccountSid}/Addresses.json_ 
  *resource*: list_address  
  *description*: An Address instance resource represents your or your customer's physical location within a country. Around the world, some local authorities require the name and address of the user to be on file with Twilio to purchase and own a phone number.
* _GET /2010-04-01/Accounts/{AccountSid}/Addresses/{Sid}.json_ 
  *resource*: fetch_address  
  *description*: An Address instance resource represents your or your customer's physical location within a country. Around the world, some local authorities require the name and address of the user to be on file with Twilio to purchase and own a phone number.
* _GET /2010-04-01/Accounts/{AccountSid}/Addresses/{AddressSid}/DependentPhoneNumbers.json_ 
  *resource*: list_dependent_phone_number  
  *description*: Phone numbers dependent on an Address resource
* _GET /2010-04-01/Accounts/{AccountSid}/Applications.json_ 
  *resource*: list_application  
  *description*: Retrieve a list of applications representing an application within the requesting account
* _GET /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json_ 
  *resource*: fetch_application  
  *description*: Fetch the application specified by the provided sid
* _GET /2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps/{ConnectAppSid}.json_ 
  *resource*: fetch_authorized_connect_app  
  *description*: Fetch an instance of an authorized-connect-app
* _GET /2010-04-01/Accounts/{AccountSid}/AuthorizedConnectApps.json_ 
  *resource*: list_authorized_connect_app  
  *description*: Retrieve a list of authorized-connect-apps belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers.json_ 
  *resource*: list_available_phone_number_country  
  *description*: Country codes with available phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}.json_ 
  *resource*: fetch_available_phone_number_country  
  *description*: Country codes with available phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Local.json_ 
  *resource*: list_available_phone_number_local  
  *description*: Available local phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/MachineToMachine.json_ 
  *resource*: list_available_phone_number_machine_to_machine  
  *description*: Available machine-to-machine phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Mobile.json_ 
  *resource*: list_available_phone_number_mobile  
  *description*: Available mobile phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/National.json_ 
  *resource*: list_available_phone_number_national  
  *description*: Available national phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/SharedCost.json_ 
  *resource*: list_available_phone_number_shared_cost  
  *description*: Available shared cost numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/TollFree.json_ 
  *resource*: list_available_phone_number_toll_free  
  *description*: Available toll free phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Voip.json_ 
  *resource*: list_available_phone_number_voip  
  *description*: Available VoIP phone numbers
* _GET /2010-04-01/Accounts/{AccountSid}/Balance.json_ 
  *resource*: fetch_balance  
  *description*: Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately. Child accounts do not contain balance information
* _GET /2010-04-01/Accounts/{AccountSid}/Calls.json_ 
  *resource*: list_call  
  *description*: Retrieves a collection of calls made to and from your account
* _GET /2010-04-01/Accounts/{AccountSid}/Calls/{Sid}.json_ 
  *resource*: fetch_call  
  *description*: Fetch the call specified by the provided Call SID
* _GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Events.json_ 
  *resource*: list_call_event  
  *description*: Retrieve a list of all events for a call.
* _GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications.json_ 
  *resource*: list_call_notification  
  *description*: Error notifications for calls
* _GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications/{Sid}.json_ 
  *resource*: fetch_call_notification  
  *description*: Error notifications for calls
* _GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings.json_ 
  *resource*: list_call_recording  
  *description*: Retrieve a list of recordings belonging to the call used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Recordings/{Sid}.json_ 
  *resource*: fetch_call_recording  
  *description*: Fetch an instance of a recording for a call
* _GET /2010-04-01/Accounts/{AccountSid}/Conferences/{Sid}.json_ 
  *resource*: fetch_conference  
  *description*: Fetch an instance of a conference
* _GET /2010-04-01/Accounts/{AccountSid}/Conferences.json_ 
  *resource*: list_conference  
  *description*: Retrieve a list of conferences belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings/{Sid}.json_ 
  *resource*: fetch_conference_recording  
  *description*: Fetch an instance of a recording for a call
* _GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Recordings.json_ 
  *resource*: list_conference_recording  
  *description*: Retrieve a list of recordings belonging to the call used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants/{CallSid}.json_ 
  *resource*: fetch_participant  
  *description*: Fetch an instance of a participant
* _GET /2010-04-01/Accounts/{AccountSid}/Conferences/{ConferenceSid}/Participants.json_ 
  *resource*: list_participant  
  *description*: Retrieve a list of participants belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/ConnectApps/{Sid}.json_ 
  *resource*: fetch_connect_app  
  *description*: Fetch an instance of a connect-app
* _GET /2010-04-01/Accounts/{AccountSid}/ConnectApps.json_ 
  *resource*: list_connect_app  
  *description*: Retrieve a list of connect-apps belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{Sid}.json_ 
  *resource*: fetch_incoming_phone_number  
  *description*: Fetch an incoming-phone-number belonging to the account used to make the request.
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers.json_ 
  *resource*: list_incoming_phone_number  
  *description*: Retrieve a list of incoming-phone-numbers belonging to the account used to make the request.
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{Sid}.json_ 
  *resource*: fetch_incoming_phone_number_assigned_add_on  
  *description*: Fetch an instance of an Add-on installation currently assigned to this Number.
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns.json_ 
  *resource*: list_incoming_phone_number_assigned_add_on  
  *description*: Retrieve a list of Add-on installations currently assigned to this Number.
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions/{Sid}.json_ 
  *resource*: fetch_incoming_phone_number_assigned_add_on_extension  
  *description*: Fetch an instance of an Extension for the Assigned Add-on.
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/{ResourceSid}/AssignedAddOns/{AssignedAddOnSid}/Extensions.json_ 
  *resource*: list_incoming_phone_number_assigned_add_on_extension  
  *description*: Retrieve a list of Extensions for the Assigned Add-on.
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Local.json_ 
  *resource*: list_incoming_phone_number_local  
  *description*: Incoming local phone numbers on a Twilio account/project
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Mobile.json_ 
  *resource*: list_incoming_phone_number_mobile  
  *description*: Incoming mobile phone numbers on a Twilio account/project
* _GET /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/TollFree.json_ 
  *resource*: list_incoming_phone_number_toll_free  
  *description*: Incoming toll free phone numbers on a Twilio account/project
* _GET /2010-04-01/Accounts/{AccountSid}/Keys/{Sid}.json_ 
  *resource*: fetch_key  
  *description*: API keys
* _GET /2010-04-01/Accounts/{AccountSid}/Keys.json_ 
  *resource*: list_key  
  *description*: API keys
* _GET /2010-04-01/Accounts/{AccountSid}/Messages.json_ 
  *resource*: list_message  
  *description*: Retrieve a list of Message resources associated with a Twilio Account
* _GET /2010-04-01/Accounts/{AccountSid}/Messages/{Sid}.json_ 
  *resource*: fetch_message  
  *description*: Fetch a specific Message
* _GET /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media/{Sid}.json_ 
  *resource*: fetch_media  
  *description*: Fetch a single Media resource associated with a specific Message resource
* _GET /2010-04-01/Accounts/{AccountSid}/Messages/{MessageSid}/Media.json_ 
  *resource*: list_media  
  *description*: Read a list of Media resources associated with a specific Message resource
* _GET /2010-04-01/Accounts/{AccountSid}/Notifications.json_ 
  *resource*: list_notification  
  *description*: Retrieve a list of notifications belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json_ 
  *resource*: fetch_notification  
  *description*: Fetch a notification belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds/{Sid}.json_ 
  *resource*: fetch_outgoing_caller_id  
  *description*: Fetch an outgoing-caller-id belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/OutgoingCallerIds.json_ 
  *resource*: list_outgoing_caller_id  
  *description*: Retrieve a list of outgoing-caller-ids belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Queues/{Sid}.json_ 
  *resource*: fetch_queue  
  *description*: Fetch an instance of a queue identified by the QueueSid
* _GET /2010-04-01/Accounts/{AccountSid}/Queues.json_ 
  *resource*: list_queue  
  *description*: Retrieve a list of queues belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members/{CallSid}.json_ 
  *resource*: fetch_member  
  *description*: Fetch a specific member from the queue
* _GET /2010-04-01/Accounts/{AccountSid}/Queues/{QueueSid}/Members.json_ 
  *resource*: list_member  
  *description*: Retrieve the members of the queue
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{Sid}.json_ 
  *resource*: fetch_recording  
  *description*: Fetch an instance of a recording
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings.json_ 
  *resource*: list_recording  
  *description*: Retrieve a list of recordings belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{Sid}.json_ 
  *resource*: fetch_recording_add_on_result  
  *description*: Fetch an instance of an AddOnResult
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults.json_ 
  *resource*: list_recording_add_on_result  
  *description*: Retrieve a list of results belonging to the recording
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads/{Sid}.json_ 
  *resource*: fetch_recording_add_on_result_payload  
  *description*: Fetch an instance of a result payload
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{ReferenceSid}/AddOnResults/{AddOnResultSid}/Payloads.json_ 
  *resource*: list_recording_add_on_result_payload  
  *description*: Retrieve a list of payloads belonging to the AddOnResult
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions/{Sid}.json_ 
  *resource*: fetch_recording_transcription  
  *description*: References to text transcriptions of call recordings
* _GET /2010-04-01/Accounts/{AccountSid}/Recordings/{RecordingSid}/Transcriptions.json_ 
  *resource*: list_recording_transcription  
  *description*: References to text transcriptions of call recordings
* _GET /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json_ 
  *resource*: fetch_short_code  
  *description*: Fetch an instance of a short code
* _GET /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json_ 
  *resource*: list_short_code  
  *description*: Retrieve a list of short-codes belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/SigningKeys.json_ 
  *resource*: list_signing_key  
  *description*: Create a new signing key
* _GET /2010-04-01/Accounts/{AccountSid}/SigningKeys/{Sid}.json_ 
  *resource*: fetch_signing_key  
  *description*: TODO: Resource-level docs
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists.json_ 
  *resource*: list_sip_credential_list  
  *description*: Get All Credential Lists
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{Sid}.json_ 
  *resource*: fetch_sip_credential_list  
  *description*: Get a Credential List
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials.json_ 
  *resource*: list_sip_credential  
  *description*: Retrieve a list of credentials.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/CredentialLists/{CredentialListSid}/Credentials/{Sid}.json_ 
  *resource*: fetch_sip_credential  
  *description*: Fetch a single credential.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json_ 
  *resource*: list_sip_domain  
  *description*: Retrieve a list of domains belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json_ 
  *resource*: fetch_sip_domain  
  *description*: Fetch an instance of a Domain
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings.json_ 
  *resource*: list_sip_auth_calls_credential_list_mapping  
  *description*: Retrieve a list of credential list mappings belonging to the domain used in the request
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/CredentialListMappings/{Sid}.json_ 
  *resource*: fetch_sip_auth_calls_credential_list_mapping  
  *description*: Fetch a specific instance of a credential list mapping
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings.json_ 
  *resource*: list_sip_auth_calls_ip_access_control_list_mapping  
  *description*: Retrieve a list of IP Access Control List mappings belonging to the domain used in the request
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Calls/IpAccessControlListMappings/{Sid}.json_ 
  *resource*: fetch_sip_auth_calls_ip_access_control_list_mapping  
  *description*: Fetch a specific instance of an IP Access Control List mapping
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings.json_ 
  *resource*: list_sip_auth_registrations_credential_list_mapping  
  *description*: Retrieve a list of credential list mappings belonging to the domain used in the request
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/Auth/Registrations/CredentialListMappings/{Sid}.json_ 
  *resource*: fetch_sip_auth_registrations_credential_list_mapping  
  *description*: Fetch a specific instance of a credential list mapping
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings.json_ 
  *resource*: list_sip_credential_list_mapping  
  *description*: Read multiple CredentialListMapping resources from an account.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/CredentialListMappings/{Sid}.json_ 
  *resource*: fetch_sip_credential_list_mapping  
  *description*: Fetch a single CredentialListMapping resource from an account.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings/{Sid}.json_ 
  *resource*: fetch_sip_ip_access_control_list_mapping  
  *description*: Fetch an IpAccessControlListMapping resource.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{DomainSid}/IpAccessControlListMappings.json_ 
  *resource*: list_sip_ip_access_control_list_mapping  
  *description*: Retrieve a list of IpAccessControlListMapping resources.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists.json_ 
  *resource*: list_sip_ip_access_control_list  
  *description*: Retrieve a list of IpAccessControlLists that belong to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{Sid}.json_ 
  *resource*: fetch_sip_ip_access_control_list  
  *description*: Fetch a specific instance of an IpAccessControlList
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses.json_ 
  *resource*: list_sip_ip_address  
  *description*: Read multiple IpAddress resources.
* _GET /2010-04-01/Accounts/{AccountSid}/SIP/IpAccessControlLists/{IpAccessControlListSid}/IpAddresses/{Sid}.json_ 
  *resource*: fetch_sip_ip_address  
  *description*: Read one IpAddress resource.
* _GET /2010-04-01/Accounts/{AccountSid}/Transcriptions/{Sid}.json_ 
  *resource*: fetch_transcription  
  *description*: Fetch an instance of a Transcription
* _GET /2010-04-01/Accounts/{AccountSid}/Transcriptions.json_ 
  *resource*: list_transcription  
  *description*: Retrieve a list of transcriptions belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records.json_ 
  *resource*: list_usage_record  
  *description*: Retrieve a list of usage-records belonging to the account used to make the request
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/AllTime.json_ 
  *resource*: list_usage_record_all_time  
  *description*: Usage records for all time
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/Daily.json_ 
  *resource*: list_usage_record_daily  
  *description*: Usage records summarized by day
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/LastMonth.json_ 
  *resource*: list_usage_record_last_month  
  *description*: Usage records for last month
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/Monthly.json_ 
  *resource*: list_usage_record_monthly  
  *description*: Usage records summarized by month
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/ThisMonth.json_ 
  *resource*: list_usage_record_this_month  
  *description*: Usage records for this month
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/Today.json_ 
  *resource*: list_usage_record_today  
  *description*: Usage records for today
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/Yearly.json_ 
  *resource*: list_usage_record_yearly  
  *description*: Usage records summarized by year
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Records/Yesterday.json_ 
  *resource*: list_usage_record_yesterday  
  *description*: Usage records for yesterday
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json_ 
  *resource*: fetch_usage_trigger  
  *description*: Fetch and instance of a usage-trigger
* _GET /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json_ 
  *resource*: list_usage_trigger  
  *description*: Retrieve a list of usage-triggers belonging to the account used to make the request
* _GET /healthcheck_ 
  *resource*: fetch_health_check  
  *description*: API HealthCheck
