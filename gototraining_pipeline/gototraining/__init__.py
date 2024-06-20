from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="gototraining_source", max_table_nesting=2)
def gototraining_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # This call retrieves a list of registrants from a specific completed training session. The response includes the registrants' email addresses, and if they attended, it includes the duration of each period of their attendance in minutes, and the times at which they joined and left. If a registrant does not attend, they appear at the bottom of the listing with timeInSession = 0.
            {
                "name": "get_attendance_details",
                "table_name": "attendee",
                "endpoint": {
                    "path": "/reports/organizers/{organizerKey}/sessions/{sessionKey}/attendees",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "sessionKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # A request for a direct URL to the admin portal for a specific training. The request identifies the organizer and the training; the response provides a link the organizer can use to manage or launch the training in the admin portal. The training organizer will be required to log in. You can schedule and manage the training (e.g., add tests, polls and training materials) from the URL provided in the response.
            {
                "name": "get_manage_training_url",
                "table_name": "manage_url",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings/{trainingKey}/manageUrl",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # DEPRECATED: Please use the Admin API call 'Get all users' instead. For details see https://goto-developer.logmein.com/get-all-users.
            {
                "name": "get_all_organisers",
                "table_name": "organizer",
                "endpoint": {
                    "path": "/accounts/{accountKey}/organizers",
                    "params": {
                        "accountKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves organizer details for a specific training. This is only applicable to multi-user accounts with sharing enabled (co-organizers).
            {
                "name": "get_organisers_for_training",
                "table_name": "organizer",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings/{trainingKey}/organizers",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This call retrieves information on all online recordings for a given training. If there are none, it returns an empty list.
            {
                "name": "get_recordings_for_training",
                "table_name": "recording",
                "endpoint": {
                    "path": "/trainings/{trainingKey}/recordings",
                    "params": {
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This call provides the download for the given recording by returning a 302 redirect to the original file.
            {
                "name": "get_recording_download_by_id",
                "table_name": "recording",
                "endpoint": {
                    "path": "/trainings/{trainingKey}/recordings/{recordingId}",
                    "params": {
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "recordingId": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details on all registrants for a specific training. Registrants can be:<br>WAITING - registrant registered and is awaiting approval (where organizer has required approval)<br>APPROVED - registrant registered and is approved<br>DENIED - registrant registered and was not approved.<br><br>IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.
            {
                "name": "get_registrants",
                "table_name": "registrant",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings/{trainingKey}/registrants",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves details for specific registrant in a specific training. Registrants can be:<br>WAITING - registrant registered and is awaiting approval (where organizer has required approval)<br>APPROVED - registrant registered and is approved<br>DENIED - registrant registered and was not approved.<br><br>IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.
            {
                "name": "get_registrant",
                "table_name": "registrant",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings/{trainingKey}/registrants/{registrantKey}",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "registrantKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start. A login of the organizer is not required.
            {
                "name": "start_training",
                "table_name": "start",
                "endpoint": {
                    "path": "/trainings/{trainingKey}/start",
                    "params": {
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start after the organizer logs in with its credentials.
            {
                "name": "get_start_url",
                "table_name": "start_url",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings/{trainingKey}/startUrl",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This call retrieves information on all scheduled trainings for a given organizer. The trainings are returned in the order in which they were created. Completed trainings are not included; ongoing trainings with past sessions are included along with the past sessions. If the organizer does not have any scheduled trainings, the response will be empty.
            {
                "name": "get_all_trainings",
                "table_name": "training",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Uses the organizer key and training key to retrieve information on a scheduled training.
            {
                "name": "get_training",
                "table_name": "training",
                "endpoint": {
                    "path": "/organizers/{organizerKey}/trainings/{trainingKey}",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # This call returns session details for a given training. A session is a completed training event. Each training may contain one or more sessions.
            {
                "name": "get_session_details_for_training",
                "table_name": "training",
                "endpoint": {
                    "path": "/reports/organizers/{organizerKey}/trainings/{trainingKey}",
                    "params": {
                        "organizerKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "trainingKey": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
