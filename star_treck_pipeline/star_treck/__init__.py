from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="star_treck_source", max_table_nesting=2)
def star_treck_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            # Pagination over animals
            {
                "name": "v1_rest_animal_search",
                "table_name": "animal_base",
                "endpoint": {
                    "data_selector": "animals",
                    "path": "/v1/rest/animal/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single animal
            {
                "name": "v1_rest_animal",
                "table_name": "animal_full",
                "endpoint": {
                    "data_selector": "animal",
                    "path": "/v1/rest/animal",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single astronomical object
            {
                "name": "v_1_rest_astronomical_object",
                "table_name": "astronomical_object_base",
                "endpoint": {
                    "data_selector": "astronomicalObject.astronomicalObjects",
                    "path": "/v1/rest/astronomicalObject",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over astronomical objects
            {
                "name": "v_1_rest_astronomical_object_search",
                "table_name": "astronomical_object_base",
                "endpoint": {
                    "data_selector": "astronomicalObjects",
                    "path": "/v1/rest/astronomicalObject/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single astronomical object (V2)
            {
                "name": "v_2_rest_astronomical_object",
                "table_name": "astronomical_object_v2_base",
                "endpoint": {
                    "data_selector": "astronomicalObject.astronomicalObjects",
                    "path": "/v2/rest/astronomicalObject",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over astronomical objects (V2)
            {
                "name": "v_2_rest_astronomical_object_search",
                "table_name": "astronomical_object_v2_base",
                "endpoint": {
                    "data_selector": "astronomicalObjects",
                    "path": "/v2/rest/astronomicalObject/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over books
            {
                "name": "v1_rest_book_search",
                "table_name": "book_base",
                "endpoint": {
                    "data_selector": "books",
                    "path": "/v1/rest/book/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over book collections
            {
                "name": "v_1_rest_book_collection_search",
                "table_name": "book_collection_base",
                "endpoint": {
                    "data_selector": "bookCollections",
                    "path": "/v1/rest/bookCollection/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single book
            {
                "name": "v1_rest_book",
                "table_name": "book_series_base",
                "endpoint": {
                    "data_selector": "book.bookSeries",
                    "path": "/v1/rest/book",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single book (V2)
            {
                "name": "v2_rest_book",
                "table_name": "book_series_base",
                "endpoint": {
                    "data_selector": "book.bookSeries",
                    "path": "/v2/rest/book",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single book collection
            {
                "name": "v_1_rest_book_collection",
                "table_name": "book_series_base",
                "endpoint": {
                    "data_selector": "bookCollection.bookSeries",
                    "path": "/v1/rest/bookCollection",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single book series
            {
                "name": "v_1_rest_book_series",
                "table_name": "book_series_base",
                "endpoint": {
                    "data_selector": "bookSeries.parentSeries",
                    "path": "/v1/rest/bookSeries",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over book series
            {
                "name": "v_1_rest_book_series_search",
                "table_name": "book_series_base",
                "endpoint": {
                    "data_selector": "bookSeries",
                    "path": "/v1/rest/bookSeries/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over books (V2)
            {
                "name": "v2_rest_book_search",
                "table_name": "book_v2_base",
                "endpoint": {
                    "data_selector": "books",
                    "path": "/v2/rest/book/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over characters
            {
                "name": "v1_rest_character_search",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "characters",
                    "path": "/v1/rest/character/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single occupation
            {
                "name": "v1_rest_occupation",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "occupation.characters",
                    "path": "/v1/rest/occupation",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single occupation (V2)
            {
                "name": "v2_rest_occupation",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "occupation.characters",
                    "path": "/v2/rest/occupation",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single organization
            {
                "name": "v1_rest_organization",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "organization.characters",
                    "path": "/v1/rest/organization",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single species
            {
                "name": "v1_rest_species",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "species.characters",
                    "path": "/v1/rest/species",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single species (V2)
            {
                "name": "v2_rest_species",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "species.characters",
                    "path": "/v2/rest/species",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single title
            {
                "name": "v1_rest_title",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "title.characters",
                    "path": "/v1/rest/title",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single title (V2)
            {
                "name": "v2_rest_title",
                "table_name": "character_base",
                "endpoint": {
                    "data_selector": "title.characters",
                    "path": "/v2/rest/title",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over comic collections
            {
                "name": "v_1_rest_comic_collection_search",
                "table_name": "comic_collection_base",
                "endpoint": {
                    "data_selector": "comicCollections",
                    "path": "/v1/rest/comicCollection/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single comics
            {
                "name": "v1_rest_comics",
                "table_name": "comic_series_base",
                "endpoint": {
                    "data_selector": "comics.comicSeries",
                    "path": "/v1/rest/comics",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single comic collection
            {
                "name": "v_1_rest_comic_collection",
                "table_name": "comic_series_base",
                "endpoint": {
                    "data_selector": "comicCollection.comicSeries",
                    "path": "/v1/rest/comicCollection",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single comic collection (V2)
            {
                "name": "v_2_rest_comic_collection",
                "table_name": "comic_series_base",
                "endpoint": {
                    "data_selector": "comicCollection.comicSeries",
                    "path": "/v2/rest/comicCollection",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single comic series
            {
                "name": "v_1_rest_comic_series",
                "table_name": "comic_series_base",
                "endpoint": {
                    "data_selector": "comicSeries.parentSeries",
                    "path": "/v1/rest/comicSeries",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over comic series
            {
                "name": "v_1_rest_comic_series_search",
                "table_name": "comic_series_base",
                "endpoint": {
                    "data_selector": "comicSeries",
                    "path": "/v1/rest/comicSeries/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single comic strip
            {
                "name": "v_1_rest_comic_strip",
                "table_name": "comic_series_base",
                "endpoint": {
                    "data_selector": "comicStrip.comicSeries",
                    "path": "/v1/rest/comicStrip",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over comic strips
            {
                "name": "v_1_rest_comic_strip_search",
                "table_name": "comic_strip_base",
                "endpoint": {
                    "data_selector": "comicStrips",
                    "path": "/v1/rest/comicStrip/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over comics
            {
                "name": "v1_rest_comics_search",
                "table_name": "comics_base",
                "endpoint": {
                    "data_selector": "comics",
                    "path": "/v1/rest/comics/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over companies
            {
                "name": "v1_rest_company_search",
                "table_name": "company_base",
                "endpoint": {
                    "data_selector": "companies",
                    "path": "/v1/rest/company/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single magazine series
            {
                "name": "v_1_rest_magazine_series",
                "table_name": "company_base",
                "endpoint": {
                    "data_selector": "magazineSeries.publishers",
                    "path": "/v1/rest/magazineSeries",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single soundtrack
            {
                "name": "v1_rest_soundtrack",
                "table_name": "company_base",
                "endpoint": {
                    "data_selector": "soundtrack.labels",
                    "path": "/v1/rest/soundtrack",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single trading card set
            {
                "name": "v_1_rest_trading_card_set",
                "table_name": "company_base",
                "endpoint": {
                    "data_selector": "tradingCardSet.manufacturers",
                    "path": "/v1/rest/tradingCardSet",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single video game
            {
                "name": "v_1_rest_video_game",
                "table_name": "company_base",
                "endpoint": {
                    "data_selector": "videoGame.publishers",
                    "path": "/v1/rest/videoGame",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single company
            {
                "name": "v1_rest_company",
                "table_name": "company_full",
                "endpoint": {
                    "data_selector": "company",
                    "path": "/v1/rest/company",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over companies (V2)
            {
                "name": "v2_rest_company_search",
                "table_name": "company_v2_base",
                "endpoint": {
                    "data_selector": "companies",
                    "path": "/v2/rest/company/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single company (V2)
            {
                "name": "v2_rest_company",
                "table_name": "company_v2_full",
                "endpoint": {
                    "data_selector": "company",
                    "path": "/v2/rest/company",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over conflicts
            {
                "name": "v1_rest_conflict_search",
                "table_name": "conflict_base",
                "endpoint": {
                    "data_selector": "conflicts",
                    "path": "/v1/rest/conflict/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a data version
            {
                "name": "v_1_rest_common_data_version",
                "table_name": "data_version",
                "endpoint": {
                    "data_selector": "$",
                    "path": "/v1/rest/common/dataVersion",
                    "paginator": "auto",
                },
            },
            # Pagination over elements
            {
                "name": "v1_rest_element_search",
                "table_name": "element_base",
                "endpoint": {
                    "data_selector": "elements",
                    "path": "/v1/rest/element/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single element
            {
                "name": "v1_rest_element",
                "table_name": "element_full",
                "endpoint": {
                    "data_selector": "element",
                    "path": "/v1/rest/element",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over elements (V2)
            {
                "name": "v2_rest_element_search",
                "table_name": "element_v2_base",
                "endpoint": {
                    "data_selector": "elements",
                    "path": "/v2/rest/element/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single element (V2)
            {
                "name": "v2_rest_element",
                "table_name": "element_v2_full",
                "endpoint": {
                    "data_selector": "element",
                    "path": "/v2/rest/element",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over episodes
            {
                "name": "v1_rest_episode_search",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "episodes",
                    "path": "/v1/rest/episode/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single performer
            {
                "name": "v1_rest_performer",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "performer.episodesPerformances",
                    "path": "/v1/rest/performer",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single performer (V2)
            {
                "name": "v2_rest_performer",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "performer.episodesPerformances",
                    "path": "/v2/rest/performer",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single season
            {
                "name": "v1_rest_season",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "season.episodes",
                    "path": "/v1/rest/season",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single series
            {
                "name": "v1_rest_series",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "series.episodes",
                    "path": "/v1/rest/series",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single staff member
            {
                "name": "v1_rest_staff",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "staff.writtenEpisodes",
                    "path": "/v1/rest/staff",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single staff member (V2)
            {
                "name": "v2_rest_staff",
                "table_name": "episode_base",
                "endpoint": {
                    "data_selector": "staff.writtenEpisodes",
                    "path": "/v2/rest/staff",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over foods
            {
                "name": "v1_rest_food_search",
                "table_name": "food_base",
                "endpoint": {
                    "data_selector": "foods",
                    "path": "/v1/rest/food/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single food
            {
                "name": "v1_rest_food",
                "table_name": "food_full",
                "endpoint": {
                    "data_selector": "food",
                    "path": "/v1/rest/food",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over literature
            {
                "name": "v1_rest_literature_search",
                "table_name": "literature_base",
                "endpoint": {
                    "data_selector": "literature",
                    "path": "/v1/rest/literature/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single literature
            {
                "name": "v1_rest_literature",
                "table_name": "literature_full",
                "endpoint": {
                    "data_selector": "literature",
                    "path": "/v1/rest/literature",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single conflict
            {
                "name": "v1_rest_conflict",
                "table_name": "location_base",
                "endpoint": {
                    "data_selector": "conflict.locations",
                    "path": "/v1/rest/conflict",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single conflict (V2)
            {
                "name": "v2_rest_conflict",
                "table_name": "location_base",
                "endpoint": {
                    "data_selector": "conflict.locations",
                    "path": "/v2/rest/conflict",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over locations
            {
                "name": "v1_rest_location_search",
                "table_name": "location_base",
                "endpoint": {
                    "data_selector": "locations",
                    "path": "/v1/rest/location/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single location
            {
                "name": "v1_rest_location",
                "table_name": "location_full",
                "endpoint": {
                    "data_selector": "location",
                    "path": "/v1/rest/location",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over locations (V2)
            {
                "name": "v2_rest_location_search",
                "table_name": "location_v2_base",
                "endpoint": {
                    "data_selector": "locations",
                    "path": "/v2/rest/location/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single location (V2)
            {
                "name": "v2_rest_location",
                "table_name": "location_v2_full",
                "endpoint": {
                    "data_selector": "location",
                    "path": "/v2/rest/location",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over magazines
            {
                "name": "v1_rest_magazine_search",
                "table_name": "magazine_base",
                "endpoint": {
                    "data_selector": "magazines",
                    "path": "/v1/rest/magazine/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single magazine
            {
                "name": "v1_rest_magazine",
                "table_name": "magazine_series_base",
                "endpoint": {
                    "data_selector": "magazine.magazineSeries",
                    "path": "/v1/rest/magazine",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over magazine series
            {
                "name": "v_1_rest_magazine_series_search",
                "table_name": "magazine_series_base",
                "endpoint": {
                    "data_selector": "magazineSeries",
                    "path": "/v1/rest/magazineSeries/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over materials
            {
                "name": "v1_rest_material_search",
                "table_name": "material_base",
                "endpoint": {
                    "data_selector": "materials",
                    "path": "/v1/rest/material/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single material
            {
                "name": "v1_rest_material",
                "table_name": "material_full",
                "endpoint": {
                    "data_selector": "material",
                    "path": "/v1/rest/material",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over medical conditions
            {
                "name": "v_1_rest_medical_condition_search",
                "table_name": "medical_condition_base",
                "endpoint": {
                    "data_selector": "medicalConditions",
                    "path": "/v1/rest/medicalCondition/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single medical condition
            {
                "name": "v_1_rest_medical_condition",
                "table_name": "medical_condition_full",
                "endpoint": {
                    "data_selector": "medicalCondition",
                    "path": "/v1/rest/medicalCondition",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over movies
            {
                "name": "v1_rest_movie_search",
                "table_name": "movie_base",
                "endpoint": {
                    "data_selector": "movies",
                    "path": "/v1/rest/movie/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over occupations
            {
                "name": "v1_rest_occupation_search",
                "table_name": "occupation_base",
                "endpoint": {
                    "data_selector": "occupations",
                    "path": "/v1/rest/occupation/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over occupations (V2)
            {
                "name": "v2_rest_occupation_search",
                "table_name": "occupation_v2_base",
                "endpoint": {
                    "data_selector": "occupations",
                    "path": "/v2/rest/occupation/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over organizations
            {
                "name": "v1_rest_organization_search",
                "table_name": "organization_base",
                "endpoint": {
                    "data_selector": "organizations",
                    "path": "/v1/rest/organization/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single spacecraft class (V2)
            {
                "name": "v_2_rest_spacecraft_class",
                "table_name": "organization_base",
                "endpoint": {
                    "data_selector": "spacecraftClass.owners",
                    "path": "/v2/rest/spacecraftClass",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single spacecraft class (V3)
            {
                "name": "v_3_rest_spacecraft_class",
                "table_name": "organization_base",
                "endpoint": {
                    "data_selector": "spacecraftClass.owners",
                    "path": "/v3/rest/spacecraftClass",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single character
            {
                "name": "v1_rest_character",
                "table_name": "performer_base",
                "endpoint": {
                    "data_selector": "character.performers",
                    "path": "/v1/rest/character",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over performers
            {
                "name": "v1_rest_performer_search",
                "table_name": "performer_base",
                "endpoint": {
                    "data_selector": "performers",
                    "path": "/v1/rest/performer/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over performers (V2)
            {
                "name": "v2_rest_performer_search",
                "table_name": "performer_v2_base",
                "endpoint": {
                    "data_selector": "performers",
                    "path": "/v2/rest/performer/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single video release
            {
                "name": "v_1_rest_video_release",
                "table_name": "reference",
                "endpoint": {
                    "data_selector": "videoRelease.references",
                    "path": "/v1/rest/videoRelease",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over seasons
            {
                "name": "v1_rest_season_search",
                "table_name": "season_base",
                "endpoint": {
                    "data_selector": "seasons",
                    "path": "/v1/rest/season/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over series
            {
                "name": "v1_rest_series_search",
                "table_name": "series_base",
                "endpoint": {
                    "data_selector": "series",
                    "path": "/v1/rest/series/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single video release (V2)
            {
                "name": "v_2_rest_video_release",
                "table_name": "series_base",
                "endpoint": {
                    "data_selector": "videoRelease.series",
                    "path": "/v2/rest/videoRelease",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over soundtracks
            {
                "name": "v1_rest_soundtrack_search",
                "table_name": "soundtrack_base",
                "endpoint": {
                    "data_selector": "soundtracks",
                    "path": "/v1/rest/soundtrack/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over spacecrafts
            {
                "name": "v1_rest_spacecraft_search",
                "table_name": "spacecraft_base",
                "endpoint": {
                    "data_selector": "spacecrafts",
                    "path": "/v1/rest/spacecraft/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over spacecraft classes
            {
                "name": "v_1_rest_spacecraft_class_search",
                "table_name": "spacecraft_class_base",
                "endpoint": {
                    "data_selector": "spacecraftClasses",
                    "path": "/v1/rest/spacecraftClass/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over spacecraft classes (V2)
            {
                "name": "v_2_rest_spacecraft_class_search",
                "table_name": "spacecraft_class_v2_base",
                "endpoint": {
                    "data_selector": "spacecraftClasses",
                    "path": "/v2/rest/spacecraftClass/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single spacecraft
            {
                "name": "v1_rest_spacecraft",
                "table_name": "spacecraft_type",
                "endpoint": {
                    "data_selector": "spacecraft.spacecraftTypes",
                    "path": "/v1/rest/spacecraft",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single spacecraft (V2)
            {
                "name": "v2_rest_spacecraft",
                "table_name": "spacecraft_type",
                "endpoint": {
                    "data_selector": "spacecraft.spacecraftTypes",
                    "path": "/v2/rest/spacecraft",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single spacecraft class
            {
                "name": "v_1_rest_spacecraft_class",
                "table_name": "spacecraft_type",
                "endpoint": {
                    "data_selector": "spacecraftClass.spacecraftTypes",
                    "path": "/v1/rest/spacecraftClass",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over spacecrafts (V2)
            {
                "name": "v2_rest_spacecraft_search",
                "table_name": "spacecraft_v2_base",
                "endpoint": {
                    "data_selector": "spacecrafts",
                    "path": "/v2/rest/spacecraft/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over species
            {
                "name": "v1_rest_species_search",
                "table_name": "species_base",
                "endpoint": {
                    "data_selector": "species",
                    "path": "/v1/rest/species/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over species (V2)
            {
                "name": "v2_rest_species_search",
                "table_name": "species_v2_base",
                "endpoint": {
                    "data_selector": "species",
                    "path": "/v2/rest/species/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single episode
            {
                "name": "v1_rest_episode",
                "table_name": "staff_base",
                "endpoint": {
                    "data_selector": "episode.writers",
                    "path": "/v1/rest/episode",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single movie
            {
                "name": "v1_rest_movie",
                "table_name": "staff_base",
                "endpoint": {
                    "data_selector": "movie.writers",
                    "path": "/v1/rest/movie",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over staff members
            {
                "name": "v1_rest_staff_search",
                "table_name": "staff_base",
                "endpoint": {
                    "data_selector": "staff",
                    "path": "/v1/rest/staff/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over staff members (V2)
            {
                "name": "v2_rest_staff_search",
                "table_name": "staff_v2_base",
                "endpoint": {
                    "data_selector": "staff",
                    "path": "/v2/rest/staff/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over technology pieces
            {
                "name": "v1_rest_technology_search",
                "table_name": "technology_base",
                "endpoint": {
                    "data_selector": "technology",
                    "path": "/v1/rest/technology/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single technology piece
            {
                "name": "v1_rest_technology",
                "table_name": "technology_full",
                "endpoint": {
                    "data_selector": "technology",
                    "path": "/v1/rest/technology",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over technology pieces (V2)
            {
                "name": "v2_rest_technology_search",
                "table_name": "technology_v2_base",
                "endpoint": {
                    "data_selector": "technology",
                    "path": "/v2/rest/technology/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single technology piece (V2)
            {
                "name": "v2_rest_technology",
                "table_name": "technology_v2_full",
                "endpoint": {
                    "data_selector": "technology",
                    "path": "/v2/rest/technology",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over titles
            {
                "name": "v1_rest_title_search",
                "table_name": "title_base",
                "endpoint": {
                    "data_selector": "titles",
                    "path": "/v1/rest/title/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over titles (V2)
            {
                "name": "v2_rest_title_search",
                "table_name": "title_v2_base",
                "endpoint": {
                    "data_selector": "titles",
                    "path": "/v2/rest/title/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over trading cards
            {
                "name": "v_1_rest_trading_card_search",
                "table_name": "trading_card_base",
                "endpoint": {
                    "data_selector": "tradingCards",
                    "path": "/v1/rest/tradingCard/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single trading card deck
            {
                "name": "v_1_rest_trading_card_deck",
                "table_name": "trading_card_base",
                "endpoint": {
                    "data_selector": "tradingCardDeck.tradingCards",
                    "path": "/v1/rest/tradingCardDeck",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over trading card decks
            {
                "name": "v_1_rest_trading_card_deck_search",
                "table_name": "trading_card_deck_base",
                "endpoint": {
                    "data_selector": "tradingCardDecks",
                    "path": "/v1/rest/tradingCardDeck/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single trading card
            {
                "name": "v_1_rest_trading_card",
                "table_name": "trading_card_full",
                "endpoint": {
                    "data_selector": "tradingCard",
                    "path": "/v1/rest/tradingCard",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over trading card sets
            {
                "name": "v_1_rest_trading_card_set_search",
                "table_name": "trading_card_set_base",
                "endpoint": {
                    "data_selector": "tradingCardSets",
                    "path": "/v1/rest/tradingCardSet/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over video games
            {
                "name": "v_1_rest_video_game_search",
                "table_name": "video_game_base",
                "endpoint": {
                    "data_selector": "videoGames",
                    "path": "/v1/rest/videoGame/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over video releases
            {
                "name": "v_1_rest_video_release_search",
                "table_name": "video_release_base",
                "endpoint": {
                    "data_selector": "videoReleases",
                    "path": "/v1/rest/videoRelease/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over video releases (V2)
            {
                "name": "v_2_rest_video_release_search",
                "table_name": "video_release_base",
                "endpoint": {
                    "data_selector": "videoReleases",
                    "path": "/v2/rest/videoRelease/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over weapons
            {
                "name": "v1_rest_weapon_search",
                "table_name": "weapon_base",
                "endpoint": {
                    "data_selector": "weapons",
                    "path": "/v1/rest/weapon/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single weapon
            {
                "name": "v1_rest_weapon",
                "table_name": "weapon_full",
                "endpoint": {
                    "data_selector": "weapon",
                    "path": "/v1/rest/weapon",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
            # Pagination over weapons (V2)
            {
                "name": "v2_rest_weapon_search",
                "table_name": "weapon_v2_base",
                "endpoint": {
                    "data_selector": "weapons",
                    "path": "/v2/rest/weapon/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "pageNumber": "OPTIONAL_CONFIG",
                        # "pageSize": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            # Retrieval of a single weapon (V2)
            {
                "name": "v2_rest_weapon",
                "table_name": "weapon_v2_full",
                "endpoint": {
                    "data_selector": "weapon",
                    "path": "/v2/rest/weapon",
                    "params": {
                        "uid": "FILL_ME_IN",  # TODO: fill in required query parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
