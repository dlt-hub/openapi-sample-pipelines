from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="nftport_source", max_table_nesting=2)
def nftport_source(
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
                "name": "Authorization",
                "location": "header",
            },
            "paginator": {
                "type": "page_number",
                "page_param": "page_number",
                "total_path": "total",
            },
        },
        "resources": [
            {
                "name": "",
                "table_name": "",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/",
                },
            },
            # Returns a list of contracts (i.e. collections) based on `type` of ownership:  1. `owns_contract_nfts`- the given account (wallet) address owns at least one NFT.  2. `owns_contracts`- the given account (wallet) address is the owner of the contract.  #### Useful for: * Showing the user a list of contracts in which they own NFTs. * Showing the user a list of contracts owned by them. * Checking if a user owns an NFT in a specific collections and then unlocking some experience for them, i.e. token-gating. (You are still responsible for validating that the user owns the wallet.)  #### Related: * For a quick start, see the [List of sample addresses](../docs/About/SampleAddresses.md) to copy. * To get a list of all NFTs owned by this account, see [Retrieve NFTs owned by account](../1.json/paths/~1v0~1accounts~1{account_address}/get). * To get extra detailed information on the returned NFTs, see [Retrieve NFT details](../1.json/paths/~1v0~1nfts~1{contract_address}~1{token_id}/get).
            {
                "name": "account_contracts_response",
                "table_name": "account_contracts_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/accounts/contracts/{account_address}",
                    "params": {
                        "account_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "type": "owns_contract_nfts",
                        # "page_size": "20",
                        # "continuation": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns NFTs owned by a given account (i.e. wallet) address. Can also return each NFT metadata with  ```include```  parameter.  #### Useful for: * For checking if a user owns a specific NFT and then unlocking specific activity. * Adding NFT portfolio section to your apps.  #### Related: * For a quick start, see the [List of sample addresses](../docs/About/SampleAddresses.md) to copy. * To get all NFTs per contract, see [Retrieve contract NFTs](../1.json/paths/~1v0~1nfts~1{contract_address}/get). * To get extra detailed information on the returned NFTs, see [Retrieve NFT details](../1.json/paths/~1v0~1nfts~1{contract_address}~1{token_id}/get).
            {
                "name": "account_nfts_response",
                "table_name": "account_nfts_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/accounts/{account_address}",
                    "params": {
                        "account_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "page_size": "50",
                        # "continuation": "OPTIONAL_CONFIG",
                        # "include": "['metadata']",
                        # "exclude": "OPTIONAL_CONFIG",
                        # "contract_address": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Retrieve in-depth sales statistics about a contract from OpenSea. Includes statistics such as floor price, total volume, sales, etc. Updated with 1-hour interval.  #### Useful for: * Analysis and ranking of NFT collections. * Tracking NFT collections by sales, etc.  #### Related: * For a quick start, see the [List of sample addresses](../docs/About/SampleAddresses.md) to copy. * To query transactions from a contract, see [Retrieve transactions by contract](../1.json/paths/~1v0~1transactions~1nfts~1{contract_address}/get). * To get all NFTs of a contract, see [Retrieve contract NFTs](../1.json/paths/~1v0~1nfts~1{contract_address}/get).
            {
                "name": "collection_stats_response",
                "table_name": "collection_stats_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/transactions/stats/{contract_address}",
                    "params": {
                        "contract_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                    },
                },
            },
            # Returns all NFTs for a given contract address. Can be set to ```include``` the NFT ```metadata```, ```file_information```, ```rarity```, ```last_sale_price``` or ```all``` which returns extra information. Ethereum, Polygon and Goerli are supported.  #### Useful for: * Importing all NFTs from a given contract to your application.  #### Related: * For a quick start, see the [List of sample addresses](../docs/About/SampleAddresses.md) to copy. * To get detailed information on the returned NFTs, see [Retrieve NFT details](../1.json/paths/~1v0~1nfts~1{contract_address}~1{token_id}/get). * To get NFTs that a given account owns, see [Retrieve NFTs owned by an account](../1.json/paths/~1v0~1accounts~1{account_address}/get).
            {
                "name": "contract_nft",
                "table_name": "contract_nft",
                "primary_key": "contract_address",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "nfts",
                    "path": "/v0/nfts/{contract_address}",
                    "params": {
                        "contract_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "page_size": "50",
                        # "include": "['metadata']",
                        # "refresh_metadata": "false",
                    },
                },
            },
            # Returns the details of a batch minted NFTs for ERC1155 contracts. You need to provide  ```transaction_hash```  which is returned from [Batch customizable minting](../3.json/paths/~1v0~1mints~1customizable~1batch/post). Minting is not instantaneous because blockchains take time to verify transactions. Thus, you can poll this endpoint every 5 seconds until you get a response.  #### Useful for: * Confirming that NFT minting was successful and the NFTs are on chain.  #### Related: * For batch customizable minting, see [Batch customizable minting](../3.json/paths/~1v0~1mints~1customizable~1batch/post).
            {
                "name": "get_batch_minted_nft_response",
                "table_name": "get_batch_minted_nft_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/mints/batch/{transaction_hash}",
                    "params": {
                        "transaction_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "polygon",
                    },
                },
            },
            # Returns the details of a contract that has previously been deployed with [Deploy a contract for NFT products](../3.json/paths/~1v0~1contracts/post) or [Deploy an NFT collection contract](../3.json/paths/~1v0~1contracts~1collections/post). Supply the ```transaction_hash``` to check if the contract is on chain and to get the ```contract_address```. For NFT product contracts, you can use the returned ```contract_address``` in [Customizable Minting](../3.json/paths/~1v0~1mints~1customizable/post).  As blockchains can take a few seconds up to a few minutes to sync, this endpoint can be polled until the ```contract_address``` is returned.  #### Useful for: * Deploying your own contracts so you can build custom products or collections easily.  #### Related: * If you want to get data about NFT contracts which you haven't deployed using NFTPort, see [Retrieve contract NFTs](../1.json/paths/~1v0~1nfts~1{contract_address}/get). * If you want to learn how to use the [customizable minting](../3.json/paths/~1v0~1mints~1customizable/post), see [Customizable Minting Quickstart](docs/minting/Minting-Quickstart.md#customizable-minting).
            {
                "name": "get_deployed_contract_response",
                "table_name": "get_deployed_contract_response",
                "primary_key": "transaction_hash",
                "write_disposition": "merge",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/contracts/{transaction_hash}",
                    "params": {
                        "transaction_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "polygon",
                    },
                },
            },
            # Returns the details of a minted NFT. You need to provide  ```transaction_hash```  which is returned from [Easy minting w/URL](../3.json/paths/~1v0~1mints~1easy~1urls/post), [Easy minting w/file upload](../3.json/paths/~1v0~1mints~1easy~1files/post) or [Customizable minting](../3.json/paths/~1v0~1mints~1customizable/post). Minting is not instantaneous because blockchains take time to verify transactions. Thus, you can poll this endpoint every 5 seconds until you get a response.  #### Useful for: * Confirming that NFT minting was successful and the NFT is on chain.  #### Related: * For easy minting, see [Easy minting w/URL](../3.json/paths/~1v0~1mints~1easy~1urls/post) or [Easy minting w/file upload](../3.json/paths/~1v0~1mints~1easy~1files/post). * For customizable minting, see [Customizable minting](../3.json/paths/~1v0~1mints~1customizable/post). * If you wish to list all your previously minted NFTs, see [List all your minted NFTs](../3.json/paths/~1v0~1me~1mints/get). * To see all your previous IPFS uploads, see [List all your IPFS uploads](../3.json/paths/~1v0~1me~1storage/get).
            {
                "name": "get_minted_nft_response",
                "table_name": "get_minted_nft_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/mints/{transaction_hash}",
                    "params": {
                        "transaction_hash": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "polygon",
                    },
                },
            },
            # Returns the ABI for a contract you’ve previously deployed with  [Deploy a contract for NFT products](../3.json/paths/~1v0~1contracts/post) or [Deploy a contract for NFT collections](../3.json/paths/~1v0~1contracts~1collections/post).  #### Useful for: * Retrieving your contract ABI, for direct on-chain contract calls.  #### Related: * To see all the contracts you've previously deployed, see [List all your deployed contracts](../3.json/paths/~1v0~1me~1contracts/get). * If you want to learn how to use the [customizable minting](../3.json/paths/~1v0~1mints~1customizable/post), see [Customizable Minting Quickstart](docs/minting/Minting-Quickstart.md#customizable-minting).
            {
                "name": "get_user_profile_contracts_ab_is_response",
                "table_name": "get_user_profile_contracts_ab_is_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/me/contracts/abis/{contract_address}",
                    "params": {
                        "contract_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "polygon",
                    },
                },
            },
            # Retrieve your NFTPort settings to check your usage and limits. #### Useful for: * Checking your minting and contract deployment usage and limits. * Checking your NFT Data rate limits  #### Related: * You can access the same information on your [NFTPort dashboard](https://dashboard.nftport.xyz). * To see your minted NFTs, see [List all your minted NFTs](../3.json/paths/~1v0~1me~1mints/get). * To see your deployed contracts, see [List all your deployed contracts](../3.json/paths/~1v0~1me~1contracts/get).
            {
                "name": "get_user_profile_settings_response",
                "table_name": "get_user_profile_settings_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/me/settings",
                },
            },
            # Returns details for a given NFT. These include ```metadata_url```, ```metadata``` such as name, description, attributes, etc., ```file_url```, ```cached_file_url``` and ```mint_date```. Ethereum, Polygon and Goerli are supported.  #### Useful for: * For easily getting all the necessary information about a given NFT.  #### Related: * For a quick start, see the [List of sample addresses and token IDs](../docs/About/SampleAddresses.md) to copy. * To get all NFTs per contract, see [Retrieve contract NFTs](../1.json/paths/~1v0~1nfts~1{contract_address}/get). * To get NFTs that a given account owns, see [Retrieve NFTs owned by an account](../1.json/paths/~1v0~1accounts~1{account_address}/get).
            {
                "name": "nft_details_response",
                "table_name": "nft_details_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/nfts/{contract_address}/{token_id}",
                    "params": {
                        "token_id": {
                            "type": "resolve",
                            "resource": "contract_nft",
                            "field": "token_id",
                        },
                        "contract_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "refresh_metadata": "false",
                        # "include": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of all data uploaded to IPFS by you. This includes files, metadata and directories uploaded to IPFS.  **Note: Only lists IPFS uploads created after 2022-03-21T12:10:00 UTC.**  #### Useful for: * Retrieving your uploaded data to IPFS.  #### Related: * To see all the NFTs you've previously minted, see [List all your minted NFTs](../3.json/paths/~1v0~1me~1mints/get).
            {
                "name": "storage",
                "table_name": "storage",
                "endpoint": {
                    "data_selector": "storage",
                    "path": "/v0/me/storage",
                    "params": {
                        "type": "FILL_ME_IN",  # TODO: fill in required query parameter
                        # the parameters below can optionally be configured
                        # "page_size": "50",
                        # "start_date": "OPTIONAL_CONFIG",
                        # "end_date": "OPTIONAL_CONFIG",
                    },
                    "paginator": {
                        "type": "page_number",
                        "page_param": "page_number",
                        "total_path": "",
                        "maximum_page": 20,
                    },
                },
            },
            # Returns all on-chain transactions (Contract specific/OS Seaport/LooksRare/X2Y2/Rarible/CryptoPunks) as well as Seaport listings for the specified account (i.e. wallet) address. Can be set to `include` transactions such as `mint`, `burn`, `transfer_from`, `transfer_to`, `buy`, `sell`, `list` or `all` which includes all transactions. Ethereum and Polygon mainnet is supported.  #### Useful for: * Tracking all transactions made by an account. * Building analytics and monitoring solutions.  #### Related: * For a quick start, see the [List of sample addresses](../docs/About/SampleAddresses.md) to copy. * To query transactions from a contract, see [Retrieve transactions by contract](../1.json/paths/~1v0~1transactions~1nfts~1{contract_address}/get). * To query transactions for an NFT, see [Retrieve transactions by NFT](../1.json/paths/~1v0~1transactions~1nfts~1{contract_address}~1{token_id}/get).
            {
                "name": "transactions_by_account_response",
                "table_name": "transactions_by_account_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/transactions/accounts/{account_address}",
                    "params": {
                        "account_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "page_size": "20",
                        # "type": "['all']",
                        # "continuation": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns all on-chain transactions (Contract specific/OS Seaport/LooksRare/X2Y2/Rarible/CryptoPunks) as well as Seaport listings for the specified contract. Can be set to `include` transactions such as `transfer`, `burn`, `mint`, `sale` and `list`, or `all` which includes all transactions. Ethereum and Polygon mainnet is supported.  #### Useful for: * Tracking all transactions of all NFT tokens in a contract. * Building analytics and monitoring solutions.  #### Related: * For a quick start, see the [List of sample addresses](../docs/About/SampleAddresses.md) to copy. * To query sales statistics of an NFT collection, see [Retrieve contract sales statistics](../1.json/paths/~1v0~1transactions~1stats~1{contract_address}/get). * To query transactions for an NFT, see [Retrieve transactions by NFT](../1.json/paths/~1v0~1transactions~1nfts~1{contract_address}~1{token_id}/get). * To query transactions from an account, see [Retrieve transactions by account](../1.json/paths/~1v0~1transactions~1accounts~1{account_address}/get).
            {
                "name": "transactions_by_contract_response",
                "table_name": "transactions_by_contract_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/transactions/nfts/{contract_address}",
                    "params": {
                        "contract_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "page_size": "20",
                        # "type": "['all']",
                        # "continuation": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns all on-chain transactions (Contract specific/OS Seaport/LooksRare/X2Y2/Rarible/CryptoPunks) as well as Seaport listings for the specified NFT token. Can be set to `include` transactions such as `transfer`, `burn`, `mint`, `sale` and `list`, or `all` which includes all transactions. Ethereum and Polygon mainnet is supported.  #### Useful for: * Tracking all transactions of an NFT token. * Building analytics and monitoring solutions.  #### Related: * For a quick start, see the [List of sample addresses and token IDs](../docs/About/SampleAddresses.md) to copy. * To query transactions from a contract, see [Retrieve transactions by contract](../1.json/paths/~1v0~1transactions~1nfts~1{contract_address}/get). * To query transactions from an account, see [Retrieve transactions by account](../1.json/paths/~1v0~1transactions~1accounts~1{account_address}/get).
            {
                "name": "transactions_by_token_response",
                "table_name": "transactions_by_token_response",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v0/transactions/nfts/{contract_address}/{token_id}",
                    "params": {
                        "contract_address": "FILL_ME_IN",  # TODO: fill in required path parameter
                        "token_id": "FILL_ME_IN",  # TODO: fill in required path parameter
                        # the parameters below can optionally be configured
                        # "chain": "ethereum",
                        # "page_size": "20",
                        # "type": "['all']",
                        # "continuation": "OPTIONAL_CONFIG",
                    },
                },
            },
            # Returns a list of all the NFTs you’ve previously minted with [Easy minting w/URL](../3.json/paths/~1v0~1mints~1easy~1urls/post), [Easy minting w/file upload](../3.json/paths/~1v0~1mints~1easy~1files/post) or [Customizable minting](../3.json/paths/~1v0~1mints~1customizable/post).  For recently minted NFTs, it may take a few minutes until they appear in this response.  #### Useful for: * Retrieving your NFT minting history.  #### Related: * To see all the contracts you've previously deployed, see [List all your deployed contracts](../3.json/paths/~1v0~1me~1contracts/get). * To see all your previous IPFS uploads, see [List all your IPFS uploads](../3.json/paths/~1v0~1me~1storage/get).
            {
                "name": "user_minted_nft_response",
                "table_name": "user_minted_nft_response",
                "endpoint": {
                    "data_selector": "minted_nfts",
                    "path": "/v0/me/mints",
                    "params": {
                        # the parameters below can optionally be configured
                        # "chain": "OPTIONAL_CONFIG",
                        # "page_size": "50",
                    },
                },
            },
            # Returns a list of all the collection contracts you’ve previously deployed. It can also return merkle proofs of all the whitelisted addresses with `include` set to `merkle_proofs`. These proofs can be used during presale/whitelisted minting. A Merkle proof is a series of hashes which can be combined with the Merkle tree root and and the node (address) it was generated for, to verify that the node is contained in the Merkle tree without having access to the entire tree.  #### Useful for: * Retrieving collection-specific contract details. * Retrieving your collection contract creation history. * Getting merkle proofs of whitelisted addresses.
            {
                "name": "user_profile_contract_collections_details",
                "table_name": "user_profile_contract_collections_details",
                "endpoint": {
                    "data_selector": "contracts",
                    "path": "/v0/me/contracts/collections",
                    "params": {
                        # the parameters below can optionally be configured
                        # "chain": "polygon",
                        # "include": "['default']",
                    },
                },
            },
            # Returns a list of all the contracts you’ve previously deployed with [Deploy a contract for NFT products](../3.json/paths/~1v0~1contracts/post).  #### Useful for: * Retrieving your contract creation history.  #### Related: * To see all the NFTs you've previously minted, see [List all your minted NFTs](../3.json/paths/~1v0~1me~1mints/get). * To see all your previous IPFS uploads, see [List all your IPFS uploads](../3.json/paths/~1v0~1me~1storage/get).
            {
                "name": "user_profile_contract_details",
                "table_name": "user_profile_contract_details",
                "endpoint": {
                    "data_selector": "contracts",
                    "path": "/v0/me/contracts",
                },
            },
        ],
    }

    return rest_api_source(source_config)
