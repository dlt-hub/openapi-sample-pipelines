# google_sheets pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Public/google_sheets.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /v4/spreadsheets/{spreadsheetId}/developerMetadata/{metadataId}_ 
  *resource*: v_4_spreadsheets_developer_metadata  
  *description*: Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and the developer metadata's unique metadataId.
* _GET /v4/spreadsheets/{spreadsheetId}_ 
  *resource*: v4_spreadsheets  
  *description*: Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default, data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice, retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet data, use the ranges URL parameter. Ranges are specified using [A1 notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example, `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the spreadsheet that intersect the requested ranges.
* _GET /v4/spreadsheets/{spreadsheetId}/values/{range}_ 
  *resource*: v4_spreadsheets_values  
  *description*: Returns a range of values from a spreadsheet. The caller must specify the spreadsheet ID and a range.
* _GET /v4/spreadsheets/{spreadsheetId}/values:batchGet_ 
  *resource*: v_4_spreadsheets_valuesbatch_get  
  *description*: Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID and one or more ranges.
