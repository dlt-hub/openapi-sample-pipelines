# crypt_api pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/crypt_api.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi


## Available resources
* _GET /{ticker}/convert/_ 
  *resource*: convert  
  *description*: This method allows for seamless conversion of prices between FIAT currencies and cryptocurrencies, as well as between different cryptocurrencies. **Note:**   * Prices are fetched every 5 minutes from CoinMarketCap.
* _GET /{ticker}/create/_ 
  *resource*: create  
  *description*: This method is used to generate a new address to give your clients, where they can send payments.  **Please make sure when sending a transaction you <a href="https://cryptapi.io/cryptocurrencies/" target="_blank">consult the minimum transfer value</a> for the crypto/token you wish to use. If the value you send is bellow our minimums, CryptAPI will ignore the transaction.**  Before delving into the documentation, why not check if the <a href="https://cryptapi.io/libraries/" target="_blank">libraries</a> already have the functionality you need? It could save you time and effort in the long run!  **Notice:** The length of this request can't surpass the ```8192``` characters! 
* _GET /info/_ 
  *resource*: cryptapi_info  
  *description*: Endpoint that provides information regarding CryptAPI Service (e.g supported blockchains, cryptocurrencies and tokens). 
* _GET /{ticker}/estimate/_ 
  *resource*: estimate  
  *description*: <br/> This method allows you to estimate blockchain fees to process a transaction.  **Notes:**   * This is an **estimation** only, and might change significantly when the transaction is processed. CryptAPI   is not responsible if blockchain fees when forwarding the funds differ from this estimation.   * These not include CryptAPI's fees. 
* _GET /{ticker}/info/_ 
  *resource*: info  
  *description*: This endpoint is used to fetch information of the cryptocurrency/token you provided in the <a href="#operation/info!in=path&path=ticker&t=request"><code>ticker</code></a> parameter. 
* _GET /{ticker}/logs/_ 
  *resource*: log_items  
  *description*: <br/> This method provides valuable information and callbacks for addresses that are created through the <a href="#operation/create"><code>create</code></a> endpoint.  It allows users to retrieve a list of callbacks made at the specified <a href="#operation/logs!c=200&path=callbacks&t=response"><code>callbacks</code></a> parameter, allows to track payment activity and troubleshoot any issues that may arise. 
* _GET /{ticker}/qrcode/_ 
  *resource*: qrcode  
  *description*: This method generates a base64-encoded QR Code image for payments. 
