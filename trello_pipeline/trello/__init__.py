from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="trello_source", max_table_nesting=2)
def trello_source(
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
                "name": "key",
                "location": "query",
            },
            "paginator": {
                "type": "page_number",
                "page_param": "page",
                "total_path": "",
                "maximum_page": 20,
            },
        },
        "resources": [
            {
                "name": "get_actions_by_id_action",
                "table_name": "action",
                "endpoint": {
                    "path": "/actions/{idAction}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "display": "OPTIONAL_CONFIG",
                        # "entities": "OPTIONAL_CONFIG",
                        # "fields": "all",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_actions_by_id_action_by_field",
                "table_name": "action",
                "endpoint": {
                    "path": "/actions/{idAction}/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_actions_by_id_board",
                "table_name": "action",
                "endpoint": {
                    "path": "/boards/{idBoard}/actions",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "entities": "OPTIONAL_CONFIG",
                        # "display": "OPTIONAL_CONFIG",
                        # "filter": "all",
                        # "fields": "all",
                        # "limit": "50",
                        # "format": "list",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "idModels": "OPTIONAL_CONFIG",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_cards_actions_by_id_card",
                "table_name": "action",
                "endpoint": {
                    "path": "/cards/{idCard}/actions",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "entities": "OPTIONAL_CONFIG",
                        # "display": "OPTIONAL_CONFIG",
                        # "filter": "commentCard and updateCard:idList",
                        # "fields": "all",
                        # "limit": "50",
                        # "format": "list",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "idModels": "OPTIONAL_CONFIG",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_lists_actions_by_id_list",
                "table_name": "action",
                "endpoint": {
                    "path": "/lists/{idList}/actions",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "entities": "OPTIONAL_CONFIG",
                        # "display": "OPTIONAL_CONFIG",
                        # "filter": "all",
                        # "fields": "all",
                        # "limit": "50",
                        # "format": "list",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "idModels": "OPTIONAL_CONFIG",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_members_actions_by_id_member",
                "table_name": "action",
                "endpoint": {
                    "path": "/members/{idMember}/actions",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "entities": "OPTIONAL_CONFIG",
                        # "display": "OPTIONAL_CONFIG",
                        # "filter": "all",
                        # "fields": "all",
                        # "limit": "50",
                        # "format": "list",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "idModels": "OPTIONAL_CONFIG",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_organizations_actions_by_id_org",
                "table_name": "action",
                "endpoint": {
                    "path": "/organizations/{idOrg}/actions",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "entities": "OPTIONAL_CONFIG",
                        # "display": "OPTIONAL_CONFIG",
                        # "filter": "all",
                        # "fields": "all",
                        # "limit": "50",
                        # "format": "list",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "idModels": "OPTIONAL_CONFIG",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_cards_attachments_by_id_card",
                "table_name": "attachment",
                "endpoint": {
                    "path": "/cards/{idCard}/attachments",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                        # "filter": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_cards_attachments_by_id_card_by_id_attachment",
                "table_name": "attachment",
                "endpoint": {
                    "path": "/cards/{idCard}/attachments/{idAttachment}",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idAttachment": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_batch",
                "table_name": "batch",
                "endpoint": {
                    "path": "/batch",
                    "params": {
                        "urls": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_board_by_id_action",
                "table_name": "board",
                "endpoint": {
                    "path": "/actions/{idAction}/board",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_board_by_id_action_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/actions/{idAction}/board/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_by_id_board",
                "table_name": "board",
                "endpoint": {
                    "path": "/boards/{idBoard}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_display": "OPTIONAL_CONFIG",
                        # "actions_format": "list",
                        # "actions_since": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "action_fields": "all",
                        # "action_member": "OPTIONAL_CONFIG",
                        # "action_member_fields": "avatarHash, fullName, initials and username",
                        # "action_memberCreator": "OPTIONAL_CONFIG",
                        # "action_memberCreator_fields": "avatarHash, fullName, initials and username",
                        # "cards": "none",
                        # "card_fields": "all",
                        # "card_attachments": "OPTIONAL_CONFIG",
                        # "card_attachment_fields": "all",
                        # "card_checklists": "none",
                        # "card_stickers": "OPTIONAL_CONFIG",
                        # "boardStars": "none",
                        # "labels": "none",
                        # "label_fields": "all",
                        # "labels_limit": "50",
                        # "lists": "none",
                        # "list_fields": "all",
                        # "memberships": "none",
                        # "memberships_member": "OPTIONAL_CONFIG",
                        # "memberships_member_fields": "fullName and username",
                        # "members": "none",
                        # "member_fields": "avatarHash, initials, fullName, username and confirmed",
                        # "membersInvited": "none",
                        # "membersInvited_fields": "avatarHash, initials, fullName and username",
                        # "checklists": "none",
                        # "checklist_fields": "all",
                        # "organization": "OPTIONAL_CONFIG",
                        # "organization_fields": "name and displayName",
                        # "organization_memberships": "none",
                        # "myPrefs": "OPTIONAL_CONFIG",
                        # "fields": "name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames",
                    },
                },
            },
            {
                "name": "get_boards_by_id_board_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/boards/{idBoard}/{field}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_cards_board_by_id_card",
                "table_name": "board",
                "endpoint": {
                    "path": "/cards/{idCard}/board",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_cards_board_by_id_card_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/cards/{idCard}/board/{field}",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_checklists_board_by_id_checklist",
                "table_name": "board",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/board",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_checklists_board_by_id_checklist_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/board/{field}",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_labels_board_by_id_label",
                "table_name": "board",
                "endpoint": {
                    "path": "/labels/{idLabel}/board",
                    "params": {
                        "idLabel": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_labels_board_by_id_label_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/labels/{idLabel}/board/{field}",
                    "params": {
                        "idLabel": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_lists_board_by_id_list",
                "table_name": "board",
                "endpoint": {
                    "path": "/lists/{idList}/board",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_lists_board_by_id_list_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/lists/{idList}/board/{field}",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_boards_by_id_member",
                "table_name": "board",
                "endpoint": {
                    "path": "/members/{idMember}/boards",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "fields": "all",
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "actions_format": "list",
                        # "actions_since": "OPTIONAL_CONFIG",
                        # "action_fields": "all",
                        # "memberships": "none",
                        # "organization": "OPTIONAL_CONFIG",
                        # "organization_fields": "name and displayName",
                        # "lists": "none",
                    },
                },
            },
            {
                "name": "get_members_boards_by_id_member_by_filter",
                "table_name": "board",
                "endpoint": {
                    "path": "/members/{idMember}/boards/{filter}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_board_by_id_notification",
                "table_name": "board",
                "endpoint": {
                    "path": "/notifications/{idNotification}/board",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_notifications_board_by_id_notification_by_field",
                "table_name": "board",
                "endpoint": {
                    "path": "/notifications/{idNotification}/board/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_organizations_boards_by_id_org",
                "table_name": "board",
                "endpoint": {
                    "path": "/organizations/{idOrg}/boards",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "fields": "all",
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "actions_format": "list",
                        # "actions_since": "OPTIONAL_CONFIG",
                        # "action_fields": "all",
                        # "memberships": "none",
                        # "organization": "OPTIONAL_CONFIG",
                        # "organization_fields": "name and displayName",
                        # "lists": "none",
                    },
                },
            },
            {
                "name": "get_organizations_boards_by_id_org_by_filter",
                "table_name": "board",
                "endpoint": {
                    "path": "/organizations/{idOrg}/boards/{filter}",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_board_backgrounds_by_id_member",
                "table_name": "board_background",
                "endpoint": {
                    "path": "/members/{idMember}/boardBackgrounds",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                    },
                },
            },
            {
                "name": "get_members_board_backgrounds_by_id_member_by_id_board_background",
                "table_name": "board_background",
                "endpoint": {
                    "path": "/members/{idMember}/boardBackgrounds/{idBoardBackground}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idBoardBackground": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_board_stars_by_id_board",
                "table_name": "board_star",
                "endpoint": {
                    "path": "/boards/{idBoard}/boardStars",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "mine",
                    },
                },
            },
            {
                "name": "get_members_board_stars_by_id_member",
                "table_name": "board_star",
                "endpoint": {
                    "path": "/members/{idMember}/boardStars",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_board_stars_by_id_member_by_id_board_star",
                "table_name": "board_star",
                "endpoint": {
                    "path": "/members/{idMember}/boardStars/{idBoardStar}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idBoardStar": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_boards_invited_by_id_member",
                "table_name": "boards_invited",
                "endpoint": {
                    "path": "/members/{idMember}/boardsInvited",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_members_boards_invited_by_id_member_by_field",
                "table_name": "boards_invited",
                "endpoint": {
                    "path": "/members/{idMember}/boardsInvited/{field}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_card_by_id_action",
                "table_name": "card",
                "endpoint": {
                    "path": "/actions/{idAction}/card",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_card_by_id_action_by_field",
                "table_name": "card",
                "endpoint": {
                    "path": "/actions/{idAction}/card/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_cards_by_id_board",
                "table_name": "card",
                "endpoint": {
                    "path": "/boards/{idBoard}/cards",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "stickers": "OPTIONAL_CONFIG",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "limit": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "filter": "visible",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_cards_by_id_board_by_filter",
                "table_name": "card",
                "endpoint": {
                    "path": "/boards/{idBoard}/cards/{filter}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_cards_by_id_board_by_id_card",
                "table_name": "card",
                "endpoint": {
                    "path": "/boards/{idBoard}/cards/{idCard}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_display": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "action_fields": "all",
                        # "action_memberCreator_fields": "avatarHash, fullName, initials and username",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, initials, fullName and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checkItemState_fields": "all",
                        # "labels": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "checklist_fields": "all",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_members_cards_by_id_board_by_id_member",
                "table_name": "card",
                "endpoint": {
                    "path": "/boards/{idBoard}/members/{idMember}/cards",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "board": "OPTIONAL_CONFIG",
                        # "board_fields": "name, desc, closed, idOrganization, pinned, url and prefs",
                        # "list": "OPTIONAL_CONFIG",
                        # "list_fields": "all",
                        # "filter": "visible",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_cards_by_id_card",
                "table_name": "card",
                "endpoint": {
                    "path": "/cards/{idCard}",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_display": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "action_fields": "all",
                        # "action_memberCreator_fields": "avatarHash, fullName, initials and username",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "membersVoted": "OPTIONAL_CONFIG",
                        # "memberVoted_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checkItemState_fields": "all",
                        # "checklists": "none",
                        # "checklist_fields": "all",
                        # "board": "OPTIONAL_CONFIG",
                        # "board_fields": "name, desc, descData, closed, idOrganization, pinned, url and prefs",
                        # "list": "OPTIONAL_CONFIG",
                        # "list_fields": "all",
                        # "stickers": "OPTIONAL_CONFIG",
                        # "sticker_fields": "all",
                        # "fields": "badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl and url",
                    },
                },
            },
            {
                "name": "get_cards_by_id_card_by_field",
                "table_name": "card",
                "endpoint": {
                    "path": "/cards/{idCard}/{field}",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_checklists_cards_by_id_checklist",
                "table_name": "card",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/cards",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "stickers": "OPTIONAL_CONFIG",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "limit": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "filter": "open",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_checklists_cards_by_id_checklist_by_filter",
                "table_name": "card",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/cards/{filter}",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_lists_cards_by_id_list",
                "table_name": "card",
                "endpoint": {
                    "path": "/lists/{idList}/cards",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "stickers": "OPTIONAL_CONFIG",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "limit": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "filter": "open",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_lists_cards_by_id_list_by_filter",
                "table_name": "card",
                "endpoint": {
                    "path": "/lists/{idList}/cards/{filter}",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_cards_by_id_member",
                "table_name": "card",
                "endpoint": {
                    "path": "/members/{idMember}/cards",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "stickers": "OPTIONAL_CONFIG",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "limit": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "before": "OPTIONAL_CONFIG",
                        # "filter": "visible",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_members_cards_by_id_member_by_filter",
                "table_name": "card",
                "endpoint": {
                    "path": "/members/{idMember}/cards/{filter}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_card_by_id_notification",
                "table_name": "card",
                "endpoint": {
                    "path": "/notifications/{idNotification}/card",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_notifications_card_by_id_notification_by_field",
                "table_name": "card",
                "endpoint": {
                    "path": "/notifications/{idNotification}/card/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_organizations_members_cards_by_id_org_by_id_member",
                "table_name": "card",
                "endpoint": {
                    "path": "/organizations/{idOrg}/members/{idMember}/cards",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "attachments": "OPTIONAL_CONFIG",
                        # "attachment_fields": "all",
                        # "members": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                        # "checkItemStates": "OPTIONAL_CONFIG",
                        # "checklists": "none",
                        # "board": "OPTIONAL_CONFIG",
                        # "board_fields": "name, desc, closed, idOrganization, pinned, url and prefs",
                        # "list": "OPTIONAL_CONFIG",
                        # "list_fields": "all",
                        # "filter": "visible",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_checklists_check_items_by_id_checklist",
                "table_name": "check_item",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/checkItems",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "fields": "name, nameData, pos and state",
                    },
                },
            },
            {
                "name": "get_checklists_check_items_by_id_checklist_by_id_check_item",
                "table_name": "check_item",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/checkItems/{idCheckItem}",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idCheckItem": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "name, nameData, pos and state",
                    },
                },
            },
            {
                "name": "get_cards_check_item_states_by_id_card",
                "table_name": "check_item_state",
                "endpoint": {
                    "path": "/cards/{idCard}/checkItemStates",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_checklists_by_id_board",
                "table_name": "checklist",
                "endpoint": {
                    "path": "/boards/{idBoard}/checklists",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cards": "none",
                        # "card_fields": "all",
                        # "checkItems": "all",
                        # "checkItem_fields": "name, nameData, pos and state",
                        # "filter": "all",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_cards_checklists_by_id_card",
                "table_name": "checklist",
                "endpoint": {
                    "path": "/cards/{idCard}/checklists",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cards": "none",
                        # "card_fields": "all",
                        # "checkItems": "all",
                        # "checkItem_fields": "name, nameData, pos and state",
                        # "filter": "all",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_checklists_by_id_checklist",
                "table_name": "checklist",
                "endpoint": {
                    "path": "/checklists/{idChecklist}",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cards": "none",
                        # "card_fields": "all",
                        # "checkItems": "all",
                        # "checkItem_fields": "name, nameData, pos and state",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_checklists_by_id_checklist_by_field",
                "table_name": "checklist",
                "endpoint": {
                    "path": "/checklists/{idChecklist}/{field}",
                    "params": {
                        "idChecklist": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_custom_board_backgrounds_by_id_member",
                "table_name": "custom_board_background",
                "endpoint": {
                    "path": "/members/{idMember}/customBoardBackgrounds",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                    },
                },
            },
            {
                "name": "get_members_custom_board_backgrounds_by_id_member_by_id_board_background",
                "table_name": "custom_board_background",
                "endpoint": {
                    "path": "/members/{idMember}/customBoardBackgrounds/{idBoardBackground}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idBoardBackground": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            # This gets the list of all of the user’s uploaded emoji
            {
                "name": "get_members_custom_emoji_by_id_member",
                "table_name": "custom_emoji",
                "endpoint": {
                    "path": "/members/{idMember}/customEmoji",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                    },
                },
            },
            {
                "name": "get_members_custom_emoji_by_id_member_by_id_custom_emoji",
                "table_name": "custom_emoji",
                "endpoint": {
                    "path": "/members/{idMember}/customEmoji/{idCustomEmoji}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idCustomEmoji": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            # This gets a list of all of the user’s uploaded stickers
            {
                "name": "get_members_custom_stickers_by_id_member",
                "table_name": "custom_sticker",
                "endpoint": {
                    "path": "/members/{idMember}/customStickers",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                    },
                },
            },
            {
                "name": "get_members_custom_stickers_by_id_member_by_id_custom_sticker",
                "table_name": "custom_sticker",
                "endpoint": {
                    "path": "/members/{idMember}/customStickers/{idCustomSticker}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idCustomSticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_deltas_by_id_board",
                "table_name": "delta",
                "endpoint": {
                    "path": "/boards/{idBoard}/deltas",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "tags": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "ixLastUpdate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_deltas_by_id_member",
                "table_name": "delta",
                "endpoint": {
                    "path": "/members/{idMember}/deltas",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "tags": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "ixLastUpdate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_organizations_deltas_by_id_org",
                "table_name": "delta",
                "endpoint": {
                    "path": "/organizations/{idOrg}/deltas",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "tags": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "ixLastUpdate": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_display_by_id_action",
                "table_name": "display",
                "endpoint": {
                    "path": "/actions/{idAction}/display",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_display_by_id_notification",
                "table_name": "display",
                "endpoint": {
                    "path": "/notifications/{idNotification}/display",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_entities_by_id_action",
                "table_name": "entity",
                "endpoint": {
                    "path": "/actions/{idAction}/entities",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_entities_by_id_notification",
                "table_name": "entity",
                "endpoint": {
                    "path": "/notifications/{idNotification}/entities",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_labels_by_id_board",
                "table_name": "label",
                "endpoint": {
                    "path": "/boards/{idBoard}/labels",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                        # "limit": "50",
                    },
                },
            },
            {
                "name": "get_boards_labels_by_id_board_by_id_label",
                "table_name": "label",
                "endpoint": {
                    "path": "/boards/{idBoard}/labels/{idLabel}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idLabel": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_labels_by_id_label",
                "table_name": "label",
                "endpoint": {
                    "path": "/labels/{idLabel}",
                    "params": {
                        "idLabel": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_list_by_id_action",
                "table_name": "list",
                "endpoint": {
                    "path": "/actions/{idAction}/list",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_list_by_id_action_by_field",
                "table_name": "list",
                "endpoint": {
                    "path": "/actions/{idAction}/list/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_lists_by_id_board",
                "table_name": "list",
                "endpoint": {
                    "path": "/boards/{idBoard}/lists",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cards": "none",
                        # "card_fields": "all",
                        # "filter": "open",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_lists_by_id_board_by_filter",
                "table_name": "list",
                "endpoint": {
                    "path": "/boards/{idBoard}/lists/{filter}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_cards_list_by_id_card",
                "table_name": "list",
                "endpoint": {
                    "path": "/cards/{idCard}/list",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_cards_list_by_id_card_by_field",
                "table_name": "list",
                "endpoint": {
                    "path": "/cards/{idCard}/list/{field}",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_lists_by_id_list",
                "table_name": "list",
                "endpoint": {
                    "path": "/lists/{idList}",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "cards": "none",
                        # "card_fields": "all",
                        # "board": "OPTIONAL_CONFIG",
                        # "board_fields": "name, desc, descData, closed, idOrganization, pinned, url and prefs",
                        # "fields": "name, closed, idBoard and pos",
                    },
                },
            },
            {
                "name": "get_lists_by_id_list_by_field",
                "table_name": "list",
                "endpoint": {
                    "path": "/lists/{idList}/{field}",
                    "params": {
                        "idList": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_list_by_id_notification",
                "table_name": "list",
                "endpoint": {
                    "path": "/notifications/{idNotification}/list",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_notifications_list_by_id_notification_by_field",
                "table_name": "list",
                "endpoint": {
                    "path": "/notifications/{idNotification}/list/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_member_by_id_action",
                "table_name": "member",
                "endpoint": {
                    "path": "/actions/{idAction}/member",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_member_by_id_action_by_field",
                "table_name": "member",
                "endpoint": {
                    "path": "/actions/{idAction}/member/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_members_by_id_board",
                "table_name": "member",
                "endpoint": {
                    "path": "/boards/{idBoard}/members",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "fields": "fullName and username",
                        # "activity": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_boards_members_by_id_board_by_filter",
                "table_name": "member",
                "endpoint": {
                    "path": "/boards/{idBoard}/members/{filter}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_cards_members_by_id_card",
                "table_name": "member",
                "endpoint": {
                    "path": "/cards/{idCard}/members",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            # If you specify 'me' as the username, this call will respond as if you had supplied the username associated with the supplied token
            {
                "name": "get_members_by_id_member",
                "table_name": "member",
                "endpoint": {
                    "path": "/members/{idMember}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_display": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "action_fields": "all",
                        # "action_since": "OPTIONAL_CONFIG",
                        # "action_before": "OPTIONAL_CONFIG",
                        # "cards": "none",
                        # "card_fields": "all",
                        # "card_members": "OPTIONAL_CONFIG",
                        # "card_member_fields": "avatarHash, fullName, initials and username",
                        # "card_attachments": "OPTIONAL_CONFIG",
                        # "card_attachment_fields": "url and previews",
                        # "card_stickers": "OPTIONAL_CONFIG",
                        # "boards": "OPTIONAL_CONFIG",
                        # "board_fields": "name, closed, idOrganization and pinned",
                        # "board_actions": "OPTIONAL_CONFIG",
                        # "board_actions_entities": "OPTIONAL_CONFIG",
                        # "board_actions_display": "OPTIONAL_CONFIG",
                        # "board_actions_format": "list",
                        # "board_actions_since": "OPTIONAL_CONFIG",
                        # "board_actions_limit": "50",
                        # "board_action_fields": "all",
                        # "board_lists": "none",
                        # "board_memberships": "none",
                        # "board_organization": "OPTIONAL_CONFIG",
                        # "board_organization_fields": "name and displayName",
                        # "boardsInvited": "OPTIONAL_CONFIG",
                        # "boardsInvited_fields": "name, closed, idOrganization and pinned",
                        # "boardStars": "OPTIONAL_CONFIG",
                        # "savedSearches": "OPTIONAL_CONFIG",
                        # "organizations": "none",
                        # "organization_fields": "all",
                        # "organization_paid_account": "OPTIONAL_CONFIG",
                        # "organizationsInvited": "none",
                        # "organizationsInvited_fields": "all",
                        # "notifications": "OPTIONAL_CONFIG",
                        # "notifications_entities": "OPTIONAL_CONFIG",
                        # "notifications_display": "OPTIONAL_CONFIG",
                        # "notifications_limit": "50",
                        # "notification_fields": "all",
                        # "notification_memberCreator": "OPTIONAL_CONFIG",
                        # "notification_memberCreator_fields": "avatarHash, fullName, initials and username",
                        # "notification_before": "OPTIONAL_CONFIG",
                        # "notification_since": "OPTIONAL_CONFIG",
                        # "tokens": "none",
                        # "paid_account": "OPTIONAL_CONFIG",
                        # "boardBackgrounds": "none",
                        # "customBoardBackgrounds": "none",
                        # "customStickers": "none",
                        # "customEmoji": "none",
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_members_by_id_member_by_field",
                "table_name": "member",
                "endpoint": {
                    "path": "/members/{idMember}/{field}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_member_by_id_notification",
                "table_name": "member",
                "endpoint": {
                    "path": "/notifications/{idNotification}/member",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_notifications_member_by_id_notification_by_field",
                "table_name": "member",
                "endpoint": {
                    "path": "/notifications/{idNotification}/member/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_organizations_members_by_id_org",
                "table_name": "member",
                "endpoint": {
                    "path": "/organizations/{idOrg}/members",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "fields": "fullName and username",
                        # "activity": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_organizations_members_by_id_org_by_filter",
                "table_name": "member",
                "endpoint": {
                    "path": "/organizations/{idOrg}/members/{filter}",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_search_members",
                "table_name": "member",
                "endpoint": {
                    "path": "/search/members",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "limit": "8",
                        # "idBoard": "OPTIONAL_CONFIG",
                        # "idOrganization": "OPTIONAL_CONFIG",
                        # "onlyOrgMembers": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_tokens_member_by_token",
                "table_name": "member",
                "endpoint": {
                    "path": "/tokens/{token}/member",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_tokens_member_by_token_by_field",
                "table_name": "member",
                "endpoint": {
                    "path": "/tokens/{token}/member/{field}",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_member_creator_by_id_action",
                "table_name": "member_creator",
                "endpoint": {
                    "path": "/actions/{idAction}/memberCreator",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_member_creator_by_id_action_by_field",
                "table_name": "member_creator",
                "endpoint": {
                    "path": "/actions/{idAction}/memberCreator/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_member_creator_by_id_notification",
                "table_name": "member_creator",
                "endpoint": {
                    "path": "/notifications/{idNotification}/memberCreator",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_notifications_member_creator_by_id_notification_by_field",
                "table_name": "member_creator",
                "endpoint": {
                    "path": "/notifications/{idNotification}/memberCreator/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_members_invited_by_id_board",
                "table_name": "members_invited",
                "endpoint": {
                    "path": "/boards/{idBoard}/membersInvited",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_members_invited_by_id_board_by_field",
                "table_name": "members_invited",
                "endpoint": {
                    "path": "/boards/{idBoard}/membersInvited/{field}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_organizations_members_invited_by_id_org",
                "table_name": "members_invited",
                "endpoint": {
                    "path": "/organizations/{idOrg}/membersInvited",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_organizations_members_invited_by_id_org_by_field",
                "table_name": "members_invited",
                "endpoint": {
                    "path": "/organizations/{idOrg}/membersInvited/{field}",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_cards_members_voted_by_id_card",
                "table_name": "members_voted",
                "endpoint": {
                    "path": "/cards/{idCard}/membersVoted",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_boards_memberships_by_id_board",
                "table_name": "membership",
                "endpoint": {
                    "path": "/boards/{idBoard}/memberships",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "fullName and username",
                    },
                },
            },
            {
                "name": "get_boards_memberships_by_id_board_by_id_membership",
                "table_name": "membership",
                "endpoint": {
                    "path": "/boards/{idBoard}/memberships/{idMembership}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idMembership": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "fullName and username",
                    },
                },
            },
            {
                "name": "get_organizations_memberships_by_id_org",
                "table_name": "membership",
                "endpoint": {
                    "path": "/organizations/{idOrg}/memberships",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "fullName and username",
                    },
                },
            },
            {
                "name": "get_organizations_memberships_by_id_org_by_id_membership",
                "table_name": "membership",
                "endpoint": {
                    "path": "/organizations/{idOrg}/memberships/{idMembership}",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idMembership": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "fullName and username",
                    },
                },
            },
            {
                "name": "get_boards_my_prefs_by_id_board",
                "table_name": "my_pref",
                "endpoint": {
                    "path": "/boards/{idBoard}/myPrefs",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            # You can only read the notifications for the member associated with the supplied token
            {
                "name": "get_members_notifications_by_id_member",
                "table_name": "notification",
                "endpoint": {
                    "path": "/members/{idMember}/notifications",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "entities": "OPTIONAL_CONFIG",
                        # "display": "OPTIONAL_CONFIG",
                        # "filter": "all",
                        # "read_filter": "all",
                        # "fields": "all",
                        # "limit": "50",
                        # "before": "OPTIONAL_CONFIG",
                        # "since": "OPTIONAL_CONFIG",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_members_notifications_by_id_member_by_filter",
                "table_name": "notification",
                "endpoint": {
                    "path": "/members/{idMember}/notifications/{filter}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_by_id_notification",
                "table_name": "notification",
                "endpoint": {
                    "path": "/notifications/{idNotification}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "display": "OPTIONAL_CONFIG",
                        # "entities": "OPTIONAL_CONFIG",
                        # "fields": "all",
                        # "memberCreator": "OPTIONAL_CONFIG",
                        # "memberCreator_fields": "avatarHash, fullName, initials and username",
                        # "board": "OPTIONAL_CONFIG",
                        # "board_fields": "name",
                        # "list": "OPTIONAL_CONFIG",
                        # "card": "OPTIONAL_CONFIG",
                        # "card_fields": "name",
                        # "organization": "OPTIONAL_CONFIG",
                        # "organization_fields": "displayName",
                        # "member": "OPTIONAL_CONFIG",
                        # "member_fields": "avatarHash, fullName, initials and username",
                    },
                },
            },
            {
                "name": "get_notifications_by_id_notification_by_field",
                "table_name": "notification",
                "endpoint": {
                    "path": "/notifications/{idNotification}/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_actions_organization_by_id_action",
                "table_name": "organization",
                "endpoint": {
                    "path": "/actions/{idAction}/organization",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_actions_organization_by_id_action_by_field",
                "table_name": "organization",
                "endpoint": {
                    "path": "/actions/{idAction}/organization/{field}",
                    "params": {
                        "idAction": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_boards_organization_by_id_board",
                "table_name": "organization",
                "endpoint": {
                    "path": "/boards/{idBoard}/organization",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_boards_organization_by_id_board_by_field",
                "table_name": "organization",
                "endpoint": {
                    "path": "/boards/{idBoard}/organization/{field}",
                    "params": {
                        "idBoard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_organizations_by_id_member",
                "table_name": "organization",
                "endpoint": {
                    "path": "/members/{idMember}/organizations",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                        # "fields": "all",
                        # "paid_account": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_members_organizations_by_id_member_by_filter",
                "table_name": "organization",
                "endpoint": {
                    "path": "/members/{idMember}/organizations/{filter}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "filter": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_notifications_organization_by_id_notification",
                "table_name": "organization",
                "endpoint": {
                    "path": "/notifications/{idNotification}/organization",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_notifications_organization_by_id_notification_by_field",
                "table_name": "organization",
                "endpoint": {
                    "path": "/notifications/{idNotification}/organization/{field}",
                    "params": {
                        "idNotification": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_organizations_by_id_org",
                "table_name": "organization",
                "endpoint": {
                    "path": "/organizations/{idOrg}",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "actions": "OPTIONAL_CONFIG",
                        # "actions_entities": "OPTIONAL_CONFIG",
                        # "actions_display": "OPTIONAL_CONFIG",
                        # "actions_limit": "50",
                        # "action_fields": "all",
                        # "memberships": "none",
                        # "memberships_member": "OPTIONAL_CONFIG",
                        # "memberships_member_fields": "fullName and username",
                        # "members": "none",
                        # "member_fields": "avatarHash, fullName, initials, username and confirmed",
                        # "member_activity": "OPTIONAL_CONFIG",
                        # "membersInvited": "none",
                        # "membersInvited_fields": "avatarHash, initials, fullName and username",
                        # "boards": "none",
                        # "board_fields": "all",
                        # "board_actions": "OPTIONAL_CONFIG",
                        # "board_actions_entities": "OPTIONAL_CONFIG",
                        # "board_actions_display": "OPTIONAL_CONFIG",
                        # "board_actions_format": "list",
                        # "board_actions_since": "OPTIONAL_CONFIG",
                        # "board_actions_limit": "50",
                        # "board_action_fields": "all",
                        # "board_lists": "none",
                        # "paid_account": "OPTIONAL_CONFIG",
                        # "fields": "name, displayName, desc, descData, url, website, logoHash, products and powerUps",
                    },
                },
            },
            {
                "name": "get_organizations_by_id_org_by_field",
                "table_name": "organization",
                "endpoint": {
                    "path": "/organizations/{idOrg}/{field}",
                    "params": {
                        "idOrg": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_organizations_invited_by_id_member",
                "table_name": "organizations_invited",
                "endpoint": {
                    "path": "/members/{idMember}/organizationsInvited",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_members_organizations_invited_by_id_member_by_field",
                "table_name": "organizations_invited",
                "endpoint": {
                    "path": "/members/{idMember}/organizationsInvited/{field}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_saved_searches_by_id_member",
                "table_name": "saved_search",
                "endpoint": {
                    "path": "/members/{idMember}/savedSearches",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_members_saved_searches_by_id_member_by_id_saved_search",
                "table_name": "saved_search",
                "endpoint": {
                    "path": "/members/{idMember}/savedSearches/{idSavedSearch}",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idSavedSearch": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/search",
                    "params": {
                        "query": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "idOrganizations": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "idBoards": "mine",
                        # "idCards": "OPTIONAL_CONFIG",
                        # "modelTypes": "all",
                        # "board_fields": "name and idOrganization",
                        # "boards_limit": "10",
                        # "card_fields": "all",
                        # "cards_limit": "10",
                        # "cards_page": "0",
                        # "card_board": "OPTIONAL_CONFIG",
                        # "card_list": "OPTIONAL_CONFIG",
                        # "card_members": "OPTIONAL_CONFIG",
                        # "card_stickers": "OPTIONAL_CONFIG",
                        # "card_attachments": "OPTIONAL_CONFIG",
                        # "organization_fields": "name and displayName",
                        # "organizations_limit": "10",
                        # "member_fields": "avatarHash, fullName, initials, username and confirmed",
                        # "members_limit": "10",
                        # "partial": "OPTIONAL_CONFIG",
                    },
                },
            },
            # This is the route for WebSocket requests.  See the socket API reference for a description of WebSocket usage.
            {
                "name": "get_sessions_socket",
                "table_name": "socket",
                "endpoint": {
                    "path": "/sessions/socket",
                    "params": {
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_cards_stickers_by_id_card",
                "table_name": "sticker",
                "endpoint": {
                    "path": "/cards/{idCard}/stickers",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_cards_stickers_by_id_card_by_id_sticker",
                "table_name": "sticker",
                "endpoint": {
                    "path": "/cards/{idCard}/stickers/{idSticker}",
                    "params": {
                        "idCard": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idSticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                    },
                },
            },
            {
                "name": "get_members_tokens_by_id_member",
                "table_name": "token",
                "endpoint": {
                    "path": "/members/{idMember}/tokens",
                    "params": {
                        "idMember": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "filter": "all",
                    },
                },
            },
            {
                "name": "get_tokens_by_token",
                "table_name": "token",
                "endpoint": {
                    "path": "/tokens/{token}",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "fields": "all",
                        # "webhooks": "OPTIONAL_CONFIG",
                    },
                },
            },
            {
                "name": "get_tokens_by_token_by_field",
                "table_name": "token",
                "endpoint": {
                    "path": "/tokens/{token}/{field}",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_types_by_id",
                "table_name": "type",
                "endpoint": {
                    "path": "/types/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_tokens_webhooks_by_token",
                "table_name": "webhook",
                "endpoint": {
                    "path": "/tokens/{token}/webhooks",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_tokens_webhooks_by_token_by_id_webhook",
                "table_name": "webhook",
                "endpoint": {
                    "path": "/tokens/{token}/webhooks/{idWebhook}",
                    "params": {
                        "token": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "idWebhook": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_webhooks_by_id_webhook",
                "table_name": "webhook",
                "endpoint": {
                    "path": "/webhooks/{idWebhook}",
                    "params": {
                        "idWebhook": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
            {
                "name": "get_webhooks_by_id_webhook_by_field",
                "table_name": "webhook",
                "endpoint": {
                    "path": "/webhooks/{idWebhook}/{field}",
                    "params": {
                        "idWebhook": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "field": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "key": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "token": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                },
            },
        ],
    }

    return rest_api_source(source_config)
