from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="google_sheets_source", max_table_nesting=2)
def google_sheets_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and the developer metadata's unique metadataId.
            {
                "name": "v_4_spreadsheets_developer_metadata",
                "table_name": "developer_metadata",
                "primary_key": "metadataId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v4/spreadsheets/{spreadsheetId}/developerMetadata/{metadataId}",
                    "params": {
                        "spreadsheetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "metadataId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet data, use the ranges URL parameter. Ranges are specified using [A1 notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example, `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the spreadsheet that intersect the requested ranges.
            {
                "name": "v4_spreadsheets",
                "table_name": "spreadsheet",
                "primary_key": "spreadsheetId",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v4/spreadsheets/{spreadsheetId}",
                    "params": {
                        "spreadsheetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "includeGridData": "OPTIONAL_CONFIG",
                        # "ranges": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns a range of values from a spreadsheet. The caller must specify the spreadsheet ID and a range.
            {
                "name": "v4_spreadsheets_values",
                "table_name": "value_range",
                "primary_key": "range",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v4/spreadsheets/{spreadsheetId}/values/{range}",
                    "params": {
                        "spreadsheetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "range": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "dateTimeRenderOption": "OPTIONAL_CONFIG",
                        # "majorDimension": "OPTIONAL_CONFIG",
                        # "valueRenderOption": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges.
            {
                "name": "v_4_spreadsheets_valuesbatch_get",
                "table_name": "value_range",
                "endpoint": {
                    "data_selector": "valueRanges",
                    "path": "/v4/spreadsheets/{spreadsheetId}/values:batchGet",
                    "params": {
                        "spreadsheetId": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "$.xgafv": "OPTIONAL_CONFIG",
                        # "access_token": "OPTIONAL_CONFIG",
                        # "alt": "OPTIONAL_CONFIG",
                        # "callback": "OPTIONAL_CONFIG",
                        # "fields": "OPTIONAL_CONFIG",
                        # "key": "OPTIONAL_CONFIG",
                        # "oauth_token": "OPTIONAL_CONFIG",
                        # "prettyPrint": "OPTIONAL_CONFIG",
                        # "quotaUser": "OPTIONAL_CONFIG",
                        # "upload_protocol": "OPTIONAL_CONFIG",
                        # "uploadType": "OPTIONAL_CONFIG",
                        # "dateTimeRenderOption": "OPTIONAL_CONFIG",
                        # "majorDimension": "OPTIONAL_CONFIG",
                        # "ranges": "OPTIONAL_CONFIG",
                        # "valueRenderOption": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
