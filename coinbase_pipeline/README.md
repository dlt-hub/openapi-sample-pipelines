# coinbase pipeline

Created with [dlt-init-openapi](https://github.com/dlt-hub/dlt-init-openapi) v. 0.1.0

Generated from downloaded spec at `https://raw.githubusercontent.com/dlt-hub/openapi-specs/main/open_api_specs/Business/coinbase.yaml`
## Learn more at

* https://dlthub.com
* https://github.com/dlt-hub/dlt
* https://github.com/dlt-hub/dlt-init-openapi

## Credentials
This API uses apiKey authentication. Please fill in the required variables ['api_key'] in your 
secrets.toml.

## Available resources
* _GET /api/v1/assets/{asset}/networks_ 
  *resource*: get_asset_networks  
  *description*: Returns a list of supported networks and network information for a specific asset.
* _GET /api/v1/assets_ 
  *resource*: get_assets  
  *description*: Returns a list of all supported assets.
* _GET /api/v1/assets/{asset}_ 
  *resource*: get_asset  
  *description*: Retrieves information for a specific asset.
* _GET /api/v1/instruments/{instrument}/candles_ 
  *resource*: get_instrument_candles  
  *description*: Retrieves a list of aggregated candles data for a given instrument, granularity and time range
* _GET /api/v1/instruments/volumes/daily_ 
  *resource*: get_instrument_volumes_daily  
  *description*: Retrieves the trading volumes for each instrument separated by day.
* _GET /api/v1/fee-rate-tiers_ 
  *resource*: get_fee_rate_tiers  
  *description*: Return all the fee rate tiers.
* _GET /api/v1/instruments/{instrument}/funding_ 
  *resource*: get_instrument_funding  
  *description*: Retrieves the historical funding rates for a specific instrument.
* _GET /api/v1/instruments/{instrument}/quote_ 
  *resource*: get_instrument_quote  
  *description*: Retrieves the current quote for a specific instrument.
* _GET /api/v1/instruments_ 
  *resource*: get_instruments  
  *description*: Returns all of the instruments available for trading.
* _GET /api/v1/instruments/{instrument}_ 
  *resource*: get_instrument  
  *description*: Retrieves market information for a specific instrument.
* _GET /api/v1/orders_ 
  *resource*: get_orders  
  *description*: Returns a list of active orders resting on the order book matching the requested criteria. Does not return any rejected, cancelled, or fully filled orders as they are not active.
* _GET /api/v1/orders/{id}_ 
  *resource*: get_order  
  *description*: Retrieves a single order. The order retrieved can be either active or inactive.
* _GET /api/v1/portfolios/{portfolio}/detail_ 
  *resource*: get_portfolio_detail  
  *description*: Retrieves the summary, positions, and balances of a portfolio.
* _GET /api/v1/portfolios/{portfolio}/balances_ 
  *resource*: get_portfolio_balances  
  *description*: Returns all of the balances for a given portfolio.
* _GET /api/v1/portfolios/{portfolio}/balances/{asset}_ 
  *resource*: get_portfolio_balance  
  *description*: Retrieves the balance for a given portfolio and asset.
* _GET /api/v1/portfolios/fee-rates_ 
  *resource*: get_portfolios_fee_rates  
  *description*: Retrieves the Perpetual Future and Spot fee rate tiers for the user.
* _GET /api/v1/portfolios/fills_ 
  *resource*: get_multi_portfolio_fills  
  *description*: Returns fills for specified portfolios or fills for all portfolios if none are provided.
* _GET /api/v1/portfolios/{portfolio}/fills_ 
  *resource*: get_portfolio_fills  
  *description*: Returns all of the fills for a given portfolio.
* _GET /api/v1/portfolios/{portfolio}/positions_ 
  *resource*: get_portfolio_positions  
  *description*: Returns all of the positions for a given portfolio.
* _GET /api/v1/portfolios/{portfolio}/positions/{instrument}_ 
  *resource*: get_portfolio_position  
  *description*: Retrieves the position for a given portfolio and symbol.
* _GET /api/v1/portfolios/{portfolio}/summary_ 
  *resource*: get_portfolio_summary  
  *description*: Retrieves the high level overview of a portfolio.
* _GET /api/v1/portfolios_ 
  *resource*: get_portfolios  
  *description*: Returns all of the user's portfolios.
* _GET /api/v1/portfolios/{portfolio}_ 
  *resource*: get_portfolio  
  *description*: Returns the user's specified portfolio.
* _GET /api/v1/transfers_ 
  *resource*: get_transfers  
* _GET /api/v1/transfers/{transfer_uuid}_ 
  *resource*: get_transfer  
