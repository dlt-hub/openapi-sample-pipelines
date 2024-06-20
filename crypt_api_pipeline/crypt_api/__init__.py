from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="crypt_api_source", max_table_nesting=2)
def crypt_api_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # This method allows for seamless conversion of prices between FIAT currencies and cryptocurrencies, as well as between different cryptocurrencies. **Note:**   * Prices are fetched every 5 minutes from CoinMarketCap.
            {
                "name": "convert",
                "table_name": "convert",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/{ticker}/convert/",
                    "params": {
                        "ticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "value": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "from": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # This method is used to generate a new address to give your clients, where they can send payments.  **Please make sure when sending a transaction you <a href="https://cryptapi.io/cryptocurrencies/" target="_blank">consult the minimum transfer value</a> for the crypto/token you wish to use. If the value you send is bellow our minimums, CryptAPI will ignore the transaction.**  Before delving into the documentation, why not check if the <a href="https://cryptapi.io/libraries/" target="_blank">libraries</a> already have the functionality you need? It could save you time and effort in the long run!  **Notice:** The length of this request can't surpass the ```8192``` characters!
            {
                "name": "create",
                "table_name": "create",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/{ticker}/create/",
                    "params": {
                        "ticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "callback": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "address": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "pending": "0",
                        # "confirmations": "1",
                        # "email": "OPTIONAL_CONFIG",
                        # "post": "0",
                        # "json": "0",
                        # "priority": "default",
                        # "multi_token": "0",
                        # "multi_chain": "0",
                        # "convert": "0",
                    },
                    "paginator": "auto",
                },
            },
            # Endpoint that provides information regarding CryptAPI Service (e.g supported blockchains, cryptocurrencies and tokens).
            {
                "name": "cryptapi_info",
                "table_name": "cryptapi_info",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/info/",
                    "params": {
                        # the parameters below can optionally be configured
                        # "prices": "0",
                    },
                    "paginator": "auto",
                },
            },
            # <br/> This method allows you to estimate blockchain fees to process a transaction.  **Notes:**   * This is an **estimation** only, and might change significantly when the transaction is processed. CryptAPI   is not responsible if blockchain fees when forwarding the funds differ from this estimation.   * These not include CryptAPI's fees.
            {
                "name": "estimate",
                "table_name": "estimate",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/{ticker}/estimate/",
                    "params": {
                        "ticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "addresses": "1",
                        # "priority": "default",
                    },
                    "paginator": "auto",
                },
            },
            # This endpoint is used to fetch information of the cryptocurrency/token you provided in the <a href="#operation/info!in=path&path=ticker&t=request"><code>ticker</code></a> parameter.
            {
                "name": "info",
                "table_name": "info",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/{ticker}/info/",
                    "params": {
                        "ticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "prices": "1",
                    },
                    "paginator": "auto",
                },
            },
            # <br/> This method provides valuable information and callbacks for addresses that are created through the <a href="#operation/create"><code>create</code></a> endpoint.  It allows users to retrieve a list of callbacks made at the specified <a href="#operation/logs!c=200&path=callbacks&t=response"><code>callbacks</code></a> parameter, allows to track payment activity and troubleshoot any issues that may arise.
            {
                "name": "log_items",
                "table_name": "log_items",
                "endpoint": {
                    "data_selector": "callbacks",
                    "path": "/{ticker}/logs/",
                    "params": {
                        "ticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "callback": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # This method generates a base64-encoded QR Code image for payments.
            {
                "name": "qrcode",
                "table_name": "qrcode",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/{ticker}/qrcode/",
                    "params": {
                        "ticker": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "address": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "value": "OPTIONAL_CONFIG",
                        # "size": "512",
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
