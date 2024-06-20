from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="coinbase_source", max_table_nesting=2)
def coinbase_source(
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
                "name": "CB-ACCESS-API-KEY",
                "location": "header",
            },
        },
        "resources": [
            # Returns a list of supported networks and network information for a specific asset.
            {
                "name": "get_asset_networks",
                "table_name": "asset_network_v_1",
                "primary_key": "asset_uuid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/assets/{asset}/networks",
                    "params": {
                        "asset": {
                            "type": "resolve",
                            "resource": "get_assets",
                            "field": "asset_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of all supported assets.
            {
                "name": "get_assets",
                "table_name": "asset_v_1",
                "primary_key": "asset_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/assets",
                    "paginator": "auto",
                },
            },
            # Retrieves information for a specific asset.
            {
                "name": "get_asset",
                "table_name": "asset_v_1",
                "primary_key": "asset_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/assets/{asset}",
                    "params": {
                        "asset": {
                            "type": "resolve",
                            "resource": "get_assets",
                            "field": "asset_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a list of aggregated candles data for a given instrument, granularity and time range
            {
                "name": "get_instrument_candles",
                "table_name": "candle",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/instruments/{instrument}/candles",
                    "params": {
                        "instrument": {
                            "type": "resolve",
                            "resource": "get_instruments",
                            "field": "instrument_id",
                        },
                        "granularity": "FILL_ME_IN",  # TODO: fill in required query parameter
                        "start": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "end": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the trading volumes for each instrument separated by day.
            {
                "name": "get_instrument_volumes_daily",
                "table_name": "daily",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/instruments/volumes/daily",
                    "params": {
                        "instruments": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "result_limit": "OPTIONAL_CONFIG",
                        # "result_offset": "OPTIONAL_CONFIG",
                        # "time_from": "OPTIONAL_CONFIG",
                        # "show_other": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Return all the fee rate tiers.
            {
                "name": "get_fee_rate_tiers",
                "table_name": "fee_rate_tier_v_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/fee-rate-tiers",
                    "paginator": "auto",
                },
            },
            # Retrieves the historical funding rates for a specific instrument.
            {
                "name": "get_instrument_funding",
                "table_name": "instrument_funding_v_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/instruments/{instrument}/funding",
                    "params": {
                        "instrument": {
                            "type": "resolve",
                            "resource": "get_instruments",
                            "field": "instrument_id",
                        },
                        # the parameters below can optionally be configured
                        # "result_limit": "OPTIONAL_CONFIG",
                        # "result_offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the current quote for a specific instrument.
            {
                "name": "get_instrument_quote",
                "table_name": "instrument_quote_v_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/instruments/{instrument}/quote",
                    "params": {
                        "instrument": {
                            "type": "resolve",
                            "resource": "get_instruments",
                            "field": "instrument_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all of the instruments available for trading.
            {
                "name": "get_instruments",
                "table_name": "instrument_v_1",
                "primary_key": "instrument_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/instruments",
                    "paginator": "auto",
                },
            },
            # Retrieves market information for a specific instrument.
            {
                "name": "get_instrument",
                "table_name": "instrument_v_1",
                "primary_key": "instrument_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/instruments/{instrument}",
                    "params": {
                        "instrument": {
                            "type": "resolve",
                            "resource": "get_instruments",
                            "field": "instrument_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns a list of active orders resting on the order book matching the requested criteria. Does not return any rejected, cancelled, or fully filled orders as they are not active.
            {
                "name": "get_orders",
                "table_name": "order_result_v_1",
                "primary_key": "order_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/orders",
                    "params": {
                        # the parameters below can optionally be configured
                        # "portfolio": "OPTIONAL_CONFIG",
                        # "instrument": "OPTIONAL_CONFIG",
                        # "instrument_type": "OPTIONAL_CONFIG",
                        # "client_order_id": "OPTIONAL_CONFIG",
                        # "event_type": "OPTIONAL_CONFIG",
                        # "ref_datetime": "OPTIONAL_CONFIG",
                        # "result_limit": "OPTIONAL_CONFIG",
                        # "result_offset": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves a single order. The order retrieved can be either active or inactive.
            {
                "name": "get_order",
                "table_name": "order_result_v_1",
                "primary_key": "order_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/orders/{id}",
                    "params": {
                        "id": {
                            "type": "resolve",
                            "resource": "get_orders",
                            "field": "order_id",
                        },
                        "portfolio": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the summary, positions, and balances of a portfolio.
            {
                "name": "get_portfolio_detail",
                "table_name": "portfolio_balance_v_1",
                "primary_key": "asset_uuid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "balances",
                    "path": "/api/v1/portfolios/{portfolio}/detail",
                    "params": {
                        "portfolio": {
                            "type": "resolve",
                            "resource": "get_portfolios",
                            "field": "portfolio_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all of the balances for a given portfolio.
            {
                "name": "get_portfolio_balances",
                "table_name": "portfolio_balance_v_1",
                "primary_key": "asset_uuid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/{portfolio}/balances",
                    "params": {
                        "portfolio": {
                            "type": "resolve",
                            "resource": "get_portfolios",
                            "field": "portfolio_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the balance for a given portfolio and asset.
            {
                "name": "get_portfolio_balance",
                "table_name": "portfolio_balance_v_1",
                "primary_key": "asset_uuid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/{portfolio}/balances/{asset}",
                    "params": {
                        "asset": {
                            "type": "resolve",
                            "resource": "get_portfolio_balances",
                            "field": "asset_uuid",
                        },
                        "portfolio": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the Perpetual Future and Spot fee rate tiers for the user.
            {
                "name": "get_portfolios_fee_rates",
                "table_name": "portfolio_fee_rate_v_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/fee-rates",
                    "paginator": "auto",
                },
            },
            # Returns fills for specified portfolios or fills for all portfolios if none are provided.
            {
                "name": "get_multi_portfolio_fills",
                "table_name": "portfolio_fill_v_1",
                "primary_key": "fill_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/portfolios/fills",
                    "params": {
                        # the parameters below can optionally be configured
                        # "portfolios": "OPTIONAL_CONFIG",
                        # "order_id": "OPTIONAL_CONFIG",
                        # "client_order_id": "OPTIONAL_CONFIG",
                        # "ref_datetime": "OPTIONAL_CONFIG",
                        # "result_limit": "OPTIONAL_CONFIG",
                        # "result_offset": "OPTIONAL_CONFIG",
                        # "time_from": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all of the fills for a given portfolio.
            {
                "name": "get_portfolio_fills",
                "table_name": "portfolio_fill_v_1",
                "primary_key": "fill_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/portfolios/{portfolio}/fills",
                    "params": {
                        "portfolio": {
                            "type": "resolve",
                            "resource": "get_portfolios",
                            "field": "portfolio_id",
                        },
                        # the parameters below can optionally be configured
                        # "order_id": "OPTIONAL_CONFIG",
                        # "client_order_id": "OPTIONAL_CONFIG",
                        # "ref_datetime": "OPTIONAL_CONFIG",
                        # "result_limit": "OPTIONAL_CONFIG",
                        # "result_offset": "OPTIONAL_CONFIG",
                        # "time_from": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Returns all of the positions for a given portfolio.
            {
                "name": "get_portfolio_positions",
                "table_name": "portfolio_position_v_1",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/{portfolio}/positions",
                    "params": {
                        "portfolio": {
                            "type": "resolve",
                            "resource": "get_portfolios",
                            "field": "portfolio_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the position for a given portfolio and symbol.
            {
                "name": "get_portfolio_position",
                "table_name": "portfolio_position_v_1",
                "primary_key": "id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/{portfolio}/positions/{instrument}",
                    "params": {
                        "instrument": {
                            "type": "resolve",
                            "resource": "get_portfolio_positions",
                            "field": "id",
                        },
                        "portfolio": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieves the high level overview of a portfolio.
            {
                "name": "get_portfolio_summary",
                "table_name": "portfolio_summary_v_1",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/{portfolio}/summary",
                    "params": {
                        "portfolio": {
                            "type": "resolve",
                            "resource": "get_portfolios",
                            "field": "portfolio_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            # Returns all of the user's portfolios.
            {
                "name": "get_portfolios",
                "table_name": "portfolio_v_1",
                "primary_key": "portfolio_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios",
                    "paginator": "auto",
                },
            },
            # Returns the user's specified portfolio.
            {
                "name": "get_portfolio",
                "table_name": "portfolio_v_1",
                "primary_key": "portfolio_id",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/portfolios/{portfolio}",
                    "params": {
                        "portfolio": {
                            "type": "resolve",
                            "resource": "get_portfolios",
                            "field": "portfolio_id",
                        },
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_transfers",
                "table_name": "transfer_v_1",
                "primary_key": "transfer_uuid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "results",
                    "path": "/api/v1/transfers",
                    "params": {
                        # the parameters below can optionally be configured
                        # "portfolio [DEPRECATED]": "OPTIONAL_CONFIG",
                        # "portfolios": "OPTIONAL_CONFIG",
                        # "time_from": "OPTIONAL_CONFIG",
                        # "time_to": "OPTIONAL_CONFIG",
                        # "result_limit": "OPTIONAL_CONFIG",
                        # "result_offset": "OPTIONAL_CONFIG",
                        # "status": "OPTIONAL_CONFIG",
                        # "type": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_transfer",
                "table_name": "transfer_v_1",
                "primary_key": "transfer_uuid",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/api/v1/transfers/{transfer_uuid}",
                    "params": {
                        "transfer_uuid": {
                            "type": "resolve",
                            "resource": "get_transfers",
                            "field": "transfer_uuid",
                        },
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
