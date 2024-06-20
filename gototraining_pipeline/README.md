# gototraining pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/gototraining.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /reports/organizers/{organizerKey}/sessions/{sessionKey}/attendees_ 
  *resource*: get_attendance_details  
  *description*: This call retrieves a list of registrants from a specific completed training session. The response includes the registrants' email addresses, and if they attended, it includes the duration of each period of their attendance in minutes, and the times at which they joined and left. If a registrant does not attend, they appear at the bottom of the listing with timeInSession = 0.
* _GET /organizers/{organizerKey}/trainings/{trainingKey}/manageUrl_ 
  *resource*: get_manage_training_url  
  *description*: A request for a direct URL to the admin portal for a specific training. The request identifies the organizer and the training; the response provides a link the organizer can use to manage or launch the training in the admin portal. The training organizer will be required to log in. You can schedule and manage the training (e.g., add tests, polls and training materials) from the URL provided in the response.
* _GET /accounts/{accountKey}/organizers_ 
  *resource*: get_all_organisers  
  *description*: DEPRECATED: Please use the Admin API call 'Get all users' instead. For details see https://goto-developer.logmein.com/get-all-users.
* _GET /organizers/{organizerKey}/trainings/{trainingKey}/organizers_ 
  *resource*: get_organisers_for_training  
  *description*: Retrieves organizer details for a specific training. This is only applicable to multi-user accounts with sharing enabled (co-organizers).
* _GET /trainings/{trainingKey}/recordings_ 
  *resource*: get_recordings_for_training  
  *description*: This call retrieves information on all online recordings for a given training. If there are none, it returns an empty list.
* _GET /trainings/{trainingKey}/recordings/{recordingId}_ 
  *resource*: get_recording_download_by_id  
  *description*: This call provides the download for the given recording by returning a 302 redirect to the original file.
* _GET /organizers/{organizerKey}/trainings/{trainingKey}/registrants_ 
  *resource*: get_registrants  
  *description*: Retrieves details on all registrants for a specific training. Registrants can be:<br>WAITING - registrant registered and is awaiting approval (where organizer has required approval)<br>APPROVED - registrant registered and is approved<br>DENIED - registrant registered and was not approved.<br><br>IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.
* _GET /organizers/{organizerKey}/trainings/{trainingKey}/registrants/{registrantKey}_ 
  *resource*: get_registrant  
  *description*: Retrieves details for specific registrant in a specific training. Registrants can be:<br>WAITING - registrant registered and is awaiting approval (where organizer has required approval)<br>APPROVED - registrant registered and is approved<br>DENIED - registrant registered and was not approved.<br><br>IMPORTANT: The registrant data caches are typically updated immediately and the data will be returned in the response. However, the update can take as long as two hours.
* _GET /trainings/{trainingKey}/start_ 
  *resource*: start_training  
  *description*: Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start. A login of the organizer is not required.
* _GET /organizers/{organizerKey}/trainings/{trainingKey}/startUrl_ 
  *resource*: get_start_url  
  *description*: Returns a URL that can be used to start a training. When this URL is opened in a web browser, the GoToTraining client will be downloaded and launched and the training will start after the organizer logs in with its credentials.
* _GET /organizers/{organizerKey}/trainings_ 
  *resource*: get_all_trainings  
  *description*: This call retrieves information on all scheduled trainings for a given organizer. The trainings are returned in the order in which they were created. Completed trainings are not included; ongoing trainings with past sessions are included along with the past sessions. If the organizer does not have any scheduled trainings, the response will be empty.
* _GET /organizers/{organizerKey}/trainings/{trainingKey}_ 
  *resource*: get_training  
  *description*: Uses the organizer key and training key to retrieve information on a scheduled training.
* _GET /reports/organizers/{organizerKey}/trainings/{trainingKey}_ 
  *resource*: get_session_details_for_training  
  *description*: This call returns session details for a given training. A session is a completed training event. Each training may contain one or more sessions.
