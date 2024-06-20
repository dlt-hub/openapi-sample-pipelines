# trello pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/trello.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /actions/{idAction}_ 
  *resource*: get_actions_by_id_action  
* _GET /actions/{idAction}/{field}_ 
  *resource*: get_actions_by_id_action_by_field  
* _GET /boards/{idBoard}/actions_ 
  *resource*: get_boards_actions_by_id_board  
* _GET /cards/{idCard}/actions_ 
  *resource*: get_cards_actions_by_id_card  
* _GET /lists/{idList}/actions_ 
  *resource*: get_lists_actions_by_id_list  
* _GET /members/{idMember}/actions_ 
  *resource*: get_members_actions_by_id_member  
* _GET /organizations/{idOrg}/actions_ 
  *resource*: get_organizations_actions_by_id_org  
* _GET /cards/{idCard}/attachments_ 
  *resource*: get_cards_attachments_by_id_card  
* _GET /cards/{idCard}/attachments/{idAttachment}_ 
  *resource*: get_cards_attachments_by_id_card_by_id_attachment  
* _GET /batch_ 
  *resource*: get_batch  
* _GET /actions/{idAction}/board_ 
  *resource*: get_actions_board_by_id_action  
* _GET /actions/{idAction}/board/{field}_ 
  *resource*: get_actions_board_by_id_action_by_field  
* _GET /boards/{idBoard}_ 
  *resource*: get_boards_by_id_board  
* _GET /boards/{idBoard}/{field}_ 
  *resource*: get_boards_by_id_board_by_field  
* _GET /cards/{idCard}/board_ 
  *resource*: get_cards_board_by_id_card  
* _GET /cards/{idCard}/board/{field}_ 
  *resource*: get_cards_board_by_id_card_by_field  
* _GET /checklists/{idChecklist}/board_ 
  *resource*: get_checklists_board_by_id_checklist  
* _GET /checklists/{idChecklist}/board/{field}_ 
  *resource*: get_checklists_board_by_id_checklist_by_field  
* _GET /labels/{idLabel}/board_ 
  *resource*: get_labels_board_by_id_label  
* _GET /labels/{idLabel}/board/{field}_ 
  *resource*: get_labels_board_by_id_label_by_field  
* _GET /lists/{idList}/board_ 
  *resource*: get_lists_board_by_id_list  
* _GET /lists/{idList}/board/{field}_ 
  *resource*: get_lists_board_by_id_list_by_field  
* _GET /members/{idMember}/boards_ 
  *resource*: get_members_boards_by_id_member  
* _GET /members/{idMember}/boards/{filter}_ 
  *resource*: get_members_boards_by_id_member_by_filter  
* _GET /notifications/{idNotification}/board_ 
  *resource*: get_notifications_board_by_id_notification  
* _GET /notifications/{idNotification}/board/{field}_ 
  *resource*: get_notifications_board_by_id_notification_by_field  
* _GET /organizations/{idOrg}/boards_ 
  *resource*: get_organizations_boards_by_id_org  
* _GET /organizations/{idOrg}/boards/{filter}_ 
  *resource*: get_organizations_boards_by_id_org_by_filter  
* _GET /members/{idMember}/boardBackgrounds_ 
  *resource*: get_members_board_backgrounds_by_id_member  
* _GET /members/{idMember}/boardBackgrounds/{idBoardBackground}_ 
  *resource*: get_members_board_backgrounds_by_id_member_by_id_board_background  
* _GET /boards/{idBoard}/boardStars_ 
  *resource*: get_boards_board_stars_by_id_board  
* _GET /members/{idMember}/boardStars_ 
  *resource*: get_members_board_stars_by_id_member  
* _GET /members/{idMember}/boardStars/{idBoardStar}_ 
  *resource*: get_members_board_stars_by_id_member_by_id_board_star  
* _GET /members/{idMember}/boardsInvited_ 
  *resource*: get_members_boards_invited_by_id_member  
* _GET /members/{idMember}/boardsInvited/{field}_ 
  *resource*: get_members_boards_invited_by_id_member_by_field  
* _GET /actions/{idAction}/card_ 
  *resource*: get_actions_card_by_id_action  
* _GET /actions/{idAction}/card/{field}_ 
  *resource*: get_actions_card_by_id_action_by_field  
* _GET /boards/{idBoard}/cards_ 
  *resource*: get_boards_cards_by_id_board  
* _GET /boards/{idBoard}/cards/{filter}_ 
  *resource*: get_boards_cards_by_id_board_by_filter  
* _GET /boards/{idBoard}/cards/{idCard}_ 
  *resource*: get_boards_cards_by_id_board_by_id_card  
* _GET /boards/{idBoard}/members/{idMember}/cards_ 
  *resource*: get_boards_members_cards_by_id_board_by_id_member  
* _GET /cards/{idCard}_ 
  *resource*: get_cards_by_id_card  
* _GET /cards/{idCard}/{field}_ 
  *resource*: get_cards_by_id_card_by_field  
* _GET /checklists/{idChecklist}/cards_ 
  *resource*: get_checklists_cards_by_id_checklist  
* _GET /checklists/{idChecklist}/cards/{filter}_ 
  *resource*: get_checklists_cards_by_id_checklist_by_filter  
* _GET /lists/{idList}/cards_ 
  *resource*: get_lists_cards_by_id_list  
* _GET /lists/{idList}/cards/{filter}_ 
  *resource*: get_lists_cards_by_id_list_by_filter  
* _GET /members/{idMember}/cards_ 
  *resource*: get_members_cards_by_id_member  
* _GET /members/{idMember}/cards/{filter}_ 
  *resource*: get_members_cards_by_id_member_by_filter  
* _GET /notifications/{idNotification}/card_ 
  *resource*: get_notifications_card_by_id_notification  
* _GET /notifications/{idNotification}/card/{field}_ 
  *resource*: get_notifications_card_by_id_notification_by_field  
* _GET /organizations/{idOrg}/members/{idMember}/cards_ 
  *resource*: get_organizations_members_cards_by_id_org_by_id_member  
* _GET /checklists/{idChecklist}/checkItems_ 
  *resource*: get_checklists_check_items_by_id_checklist  
* _GET /checklists/{idChecklist}/checkItems/{idCheckItem}_ 
  *resource*: get_checklists_check_items_by_id_checklist_by_id_check_item  
* _GET /cards/{idCard}/checkItemStates_ 
  *resource*: get_cards_check_item_states_by_id_card  
* _GET /boards/{idBoard}/checklists_ 
  *resource*: get_boards_checklists_by_id_board  
* _GET /cards/{idCard}/checklists_ 
  *resource*: get_cards_checklists_by_id_card  
* _GET /checklists/{idChecklist}_ 
  *resource*: get_checklists_by_id_checklist  
* _GET /checklists/{idChecklist}/{field}_ 
  *resource*: get_checklists_by_id_checklist_by_field  
* _GET /members/{idMember}/customBoardBackgrounds_ 
  *resource*: get_members_custom_board_backgrounds_by_id_member  
* _GET /members/{idMember}/customBoardBackgrounds/{idBoardBackground}_ 
  *resource*: get_members_custom_board_backgrounds_by_id_member_by_id_board_background  
* _GET /members/{idMember}/customEmoji_ 
  *resource*: get_members_custom_emoji_by_id_member  
  *description*: This gets the list of all of the user’s uploaded emoji
* _GET /members/{idMember}/customEmoji/{idCustomEmoji}_ 
  *resource*: get_members_custom_emoji_by_id_member_by_id_custom_emoji  
* _GET /members/{idMember}/customStickers_ 
  *resource*: get_members_custom_stickers_by_id_member  
  *description*: This gets a list of all of the user’s uploaded stickers
* _GET /members/{idMember}/customStickers/{idCustomSticker}_ 
  *resource*: get_members_custom_stickers_by_id_member_by_id_custom_sticker  
* _GET /boards/{idBoard}/deltas_ 
  *resource*: get_boards_deltas_by_id_board  
* _GET /members/{idMember}/deltas_ 
  *resource*: get_members_deltas_by_id_member  
* _GET /organizations/{idOrg}/deltas_ 
  *resource*: get_organizations_deltas_by_id_org  
* _GET /actions/{idAction}/display_ 
  *resource*: get_actions_display_by_id_action  
* _GET /notifications/{idNotification}/display_ 
  *resource*: get_notifications_display_by_id_notification  
* _GET /actions/{idAction}/entities_ 
  *resource*: get_actions_entities_by_id_action  
* _GET /notifications/{idNotification}/entities_ 
  *resource*: get_notifications_entities_by_id_notification  
* _GET /boards/{idBoard}/labels_ 
  *resource*: get_boards_labels_by_id_board  
* _GET /boards/{idBoard}/labels/{idLabel}_ 
  *resource*: get_boards_labels_by_id_board_by_id_label  
* _GET /labels/{idLabel}_ 
  *resource*: get_labels_by_id_label  
* _GET /actions/{idAction}/list_ 
  *resource*: get_actions_list_by_id_action  
* _GET /actions/{idAction}/list/{field}_ 
  *resource*: get_actions_list_by_id_action_by_field  
* _GET /boards/{idBoard}/lists_ 
  *resource*: get_boards_lists_by_id_board  
* _GET /boards/{idBoard}/lists/{filter}_ 
  *resource*: get_boards_lists_by_id_board_by_filter  
* _GET /cards/{idCard}/list_ 
  *resource*: get_cards_list_by_id_card  
* _GET /cards/{idCard}/list/{field}_ 
  *resource*: get_cards_list_by_id_card_by_field  
* _GET /lists/{idList}_ 
  *resource*: get_lists_by_id_list  
* _GET /lists/{idList}/{field}_ 
  *resource*: get_lists_by_id_list_by_field  
* _GET /notifications/{idNotification}/list_ 
  *resource*: get_notifications_list_by_id_notification  
* _GET /notifications/{idNotification}/list/{field}_ 
  *resource*: get_notifications_list_by_id_notification_by_field  
* _GET /actions/{idAction}/member_ 
  *resource*: get_actions_member_by_id_action  
* _GET /actions/{idAction}/member/{field}_ 
  *resource*: get_actions_member_by_id_action_by_field  
* _GET /boards/{idBoard}/members_ 
  *resource*: get_boards_members_by_id_board  
* _GET /boards/{idBoard}/members/{filter}_ 
  *resource*: get_boards_members_by_id_board_by_filter  
* _GET /cards/{idCard}/members_ 
  *resource*: get_cards_members_by_id_card  
* _GET /members/{idMember}_ 
  *resource*: get_members_by_id_member  
  *description*: If you specify 'me' as the username, this call will respond as if you had supplied the username associated with the supplied token
* _GET /members/{idMember}/{field}_ 
  *resource*: get_members_by_id_member_by_field  
* _GET /notifications/{idNotification}/member_ 
  *resource*: get_notifications_member_by_id_notification  
* _GET /notifications/{idNotification}/member/{field}_ 
  *resource*: get_notifications_member_by_id_notification_by_field  
* _GET /organizations/{idOrg}/members_ 
  *resource*: get_organizations_members_by_id_org  
* _GET /organizations/{idOrg}/members/{filter}_ 
  *resource*: get_organizations_members_by_id_org_by_filter  
* _GET /search/members_ 
  *resource*: get_search_members  
* _GET /tokens/{token}/member_ 
  *resource*: get_tokens_member_by_token  
* _GET /tokens/{token}/member/{field}_ 
  *resource*: get_tokens_member_by_token_by_field  
* _GET /actions/{idAction}/memberCreator_ 
  *resource*: get_actions_member_creator_by_id_action  
* _GET /actions/{idAction}/memberCreator/{field}_ 
  *resource*: get_actions_member_creator_by_id_action_by_field  
* _GET /notifications/{idNotification}/memberCreator_ 
  *resource*: get_notifications_member_creator_by_id_notification  
* _GET /notifications/{idNotification}/memberCreator/{field}_ 
  *resource*: get_notifications_member_creator_by_id_notification_by_field  
* _GET /boards/{idBoard}/membersInvited_ 
  *resource*: get_boards_members_invited_by_id_board  
* _GET /boards/{idBoard}/membersInvited/{field}_ 
  *resource*: get_boards_members_invited_by_id_board_by_field  
* _GET /organizations/{idOrg}/membersInvited_ 
  *resource*: get_organizations_members_invited_by_id_org  
* _GET /organizations/{idOrg}/membersInvited/{field}_ 
  *resource*: get_organizations_members_invited_by_id_org_by_field  
* _GET /cards/{idCard}/membersVoted_ 
  *resource*: get_cards_members_voted_by_id_card  
* _GET /boards/{idBoard}/memberships_ 
  *resource*: get_boards_memberships_by_id_board  
* _GET /boards/{idBoard}/memberships/{idMembership}_ 
  *resource*: get_boards_memberships_by_id_board_by_id_membership  
* _GET /organizations/{idOrg}/memberships_ 
  *resource*: get_organizations_memberships_by_id_org  
* _GET /organizations/{idOrg}/memberships/{idMembership}_ 
  *resource*: get_organizations_memberships_by_id_org_by_id_membership  
* _GET /boards/{idBoard}/myPrefs_ 
  *resource*: get_boards_my_prefs_by_id_board  
* _GET /members/{idMember}/notifications_ 
  *resource*: get_members_notifications_by_id_member  
  *description*: You can only read the notifications for the member associated with the supplied token
* _GET /members/{idMember}/notifications/{filter}_ 
  *resource*: get_members_notifications_by_id_member_by_filter  
* _GET /notifications/{idNotification}_ 
  *resource*: get_notifications_by_id_notification  
* _GET /notifications/{idNotification}/{field}_ 
  *resource*: get_notifications_by_id_notification_by_field  
* _GET /actions/{idAction}/organization_ 
  *resource*: get_actions_organization_by_id_action  
* _GET /actions/{idAction}/organization/{field}_ 
  *resource*: get_actions_organization_by_id_action_by_field  
* _GET /boards/{idBoard}/organization_ 
  *resource*: get_boards_organization_by_id_board  
* _GET /boards/{idBoard}/organization/{field}_ 
  *resource*: get_boards_organization_by_id_board_by_field  
* _GET /members/{idMember}/organizations_ 
  *resource*: get_members_organizations_by_id_member  
* _GET /members/{idMember}/organizations/{filter}_ 
  *resource*: get_members_organizations_by_id_member_by_filter  
* _GET /notifications/{idNotification}/organization_ 
  *resource*: get_notifications_organization_by_id_notification  
* _GET /notifications/{idNotification}/organization/{field}_ 
  *resource*: get_notifications_organization_by_id_notification_by_field  
* _GET /organizations/{idOrg}_ 
  *resource*: get_organizations_by_id_org  
* _GET /organizations/{idOrg}/{field}_ 
  *resource*: get_organizations_by_id_org_by_field  
* _GET /members/{idMember}/organizationsInvited_ 
  *resource*: get_members_organizations_invited_by_id_member  
* _GET /members/{idMember}/organizationsInvited/{field}_ 
  *resource*: get_members_organizations_invited_by_id_member_by_field  
* _GET /members/{idMember}/savedSearches_ 
  *resource*: get_members_saved_searches_by_id_member  
* _GET /members/{idMember}/savedSearches/{idSavedSearch}_ 
  *resource*: get_members_saved_searches_by_id_member_by_id_saved_search  
* _GET /search_ 
  *resource*: get_search  
* _GET /sessions/socket_ 
  *resource*: get_sessions_socket  
  *description*: This is the route for WebSocket requests.  See the socket API reference for a description of WebSocket usage.
* _GET /cards/{idCard}/stickers_ 
  *resource*: get_cards_stickers_by_id_card  
* _GET /cards/{idCard}/stickers/{idSticker}_ 
  *resource*: get_cards_stickers_by_id_card_by_id_sticker  
* _GET /members/{idMember}/tokens_ 
  *resource*: get_members_tokens_by_id_member  
* _GET /tokens/{token}_ 
  *resource*: get_tokens_by_token  
* _GET /tokens/{token}/{field}_ 
  *resource*: get_tokens_by_token_by_field  
* _GET /types/{id}_ 
  *resource*: get_types_by_id  
* _GET /tokens/{token}/webhooks_ 
  *resource*: get_tokens_webhooks_by_token  
* _GET /tokens/{token}/webhooks/{idWebhook}_ 
  *resource*: get_tokens_webhooks_by_token_by_id_webhook  
* _GET /webhooks/{idWebhook}_ 
  *resource*: get_webhooks_by_id_webhook  
* _GET /webhooks/{idWebhook}/{field}_ 
  *resource*: get_webhooks_by_id_webhook_by_field  
