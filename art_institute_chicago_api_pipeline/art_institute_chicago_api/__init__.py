from typing import List

import dlt
from dlt.extract.source import DltResource
from rest_api import rest_api_source
from rest_api.typing import RESTAPIConfig


@dlt.source(name="art_institute_chicago_api_source", max_table_nesting=2)
def art_institute_chicago_api_source(
    base_url: str = dlt.config.value,
) -> List[DltResource]:

    # source configuration
    source_config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
        },
        "resources": [
            {
                "name": "get_agents",
                "table_name": "agent",
                "endpoint": {
                    "path": "/agents",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_agentsid",
                "table_name": "agent",
                "endpoint": {
                    "path": "/agents/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_agent_roles",
                "table_name": "agent_role",
                "endpoint": {
                    "path": "/agent-roles",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_agent_rolesid",
                "table_name": "agent_role",
                "endpoint": {
                    "path": "/agent-roles/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_agent_types",
                "table_name": "agent_type",
                "endpoint": {
                    "path": "/agent-types",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_agent_typesid",
                "table_name": "agent_type",
                "endpoint": {
                    "path": "/agent-types/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_articles",
                "table_name": "article",
                "endpoint": {
                    "path": "/articles",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_articlesid",
                "table_name": "article",
                "endpoint": {
                    "path": "/articles/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artists",
                "table_name": "artist",
                "endpoint": {
                    "path": "/artists",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artistsid",
                "table_name": "artist",
                "endpoint": {
                    "path": "/artists/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artworks",
                "table_name": "artwork",
                "endpoint": {
                    "path": "/artworks",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artworksid",
                "table_name": "artwork",
                "endpoint": {
                    "path": "/artworks/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artwork_date_qualifiers",
                "table_name": "artwork_date_qualifier",
                "endpoint": {
                    "path": "/artwork-date-qualifiers",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artwork_date_qualifiersid",
                "table_name": "artwork_date_qualifier",
                "endpoint": {
                    "path": "/artwork-date-qualifiers/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artwork_place_qualifiers",
                "table_name": "artwork_place_qualifier",
                "endpoint": {
                    "path": "/artwork-place-qualifiers",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artwork_place_qualifiersid",
                "table_name": "artwork_place_qualifier",
                "endpoint": {
                    "path": "/artwork-place-qualifiers/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artwork_types",
                "table_name": "artwork_type",
                "endpoint": {
                    "path": "/artwork-types",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artwork_typesid",
                "table_name": "artwork_type",
                "endpoint": {
                    "path": "/artwork-types/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_category_terms",
                "table_name": "category_term",
                "endpoint": {
                    "path": "/category-terms",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_category_termsid",
                "table_name": "category_term",
                "endpoint": {
                    "path": "/category-terms/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_digital_catalogs",
                "table_name": "digital_catalog",
                "endpoint": {
                    "path": "/digital-catalogs",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_digital_catalogsid",
                "table_name": "digital_catalog",
                "endpoint": {
                    "path": "/digital-catalogs/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_digital_publication_sections",
                "table_name": "digital_publication_section",
                "endpoint": {
                    "path": "/digital-publication-sections",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_digital_publication_sectionsid",
                "table_name": "digital_publication_section",
                "endpoint": {
                    "path": "/digital-publication-sections/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_educator_resources",
                "table_name": "educator_resource",
                "endpoint": {
                    "path": "/educator-resources",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_educator_resourcesid",
                "table_name": "educator_resource",
                "endpoint": {
                    "path": "/educator-resources/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_events",
                "table_name": "event",
                "endpoint": {
                    "path": "/events",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_eventsid",
                "table_name": "event",
                "endpoint": {
                    "path": "/events/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_event_occurrences",
                "table_name": "event_occurrence",
                "endpoint": {
                    "path": "/event-occurrences",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_event_occurrencesid",
                "table_name": "event_occurrence",
                "endpoint": {
                    "path": "/event-occurrences/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_event_programs",
                "table_name": "event_program",
                "endpoint": {
                    "path": "/event-programs",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_event_programsid",
                "table_name": "event_program",
                "endpoint": {
                    "path": "/event-programs/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_exhibitions",
                "table_name": "exhibition",
                "endpoint": {
                    "path": "/exhibitions",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_exhibitionsid",
                "table_name": "exhibition",
                "endpoint": {
                    "path": "/exhibitions/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_galleries",
                "table_name": "gallery",
                "endpoint": {
                    "path": "/galleries",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_galleriesid",
                "table_name": "gallery",
                "endpoint": {
                    "path": "/galleries/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_generic_pages",
                "table_name": "generic_page",
                "endpoint": {
                    "path": "/generic-pages",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_generic_pagesid",
                "table_name": "generic_page",
                "endpoint": {
                    "path": "/generic-pages/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_highlights",
                "table_name": "highlight",
                "endpoint": {
                    "path": "/highlights",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_highlightsid",
                "table_name": "highlight",
                "endpoint": {
                    "path": "/highlights/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_images",
                "table_name": "image",
                "endpoint": {
                    "path": "/images",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_imagesid",
                "table_name": "image",
                "endpoint": {
                    "path": "/images/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_mobile_sounds",
                "table_name": "mobile_sound",
                "endpoint": {
                    "path": "/mobile-sounds",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_mobile_soundsid",
                "table_name": "mobile_sound",
                "endpoint": {
                    "path": "/mobile-sounds/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_places",
                "table_name": "place",
                "endpoint": {
                    "path": "/places",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_placesid",
                "table_name": "place",
                "endpoint": {
                    "path": "/places/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_press_releases",
                "table_name": "press_release",
                "endpoint": {
                    "path": "/press-releases",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_press_releasesid",
                "table_name": "press_release",
                "endpoint": {
                    "path": "/press-releases/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_printed_catalogs",
                "table_name": "printed_catalog",
                "endpoint": {
                    "path": "/printed-catalogs",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_printed_catalogsid",
                "table_name": "printed_catalog",
                "endpoint": {
                    "path": "/printed-catalogs/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_products",
                "table_name": "product",
                "endpoint": {
                    "path": "/products",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_productsid",
                "table_name": "product",
                "endpoint": {
                    "path": "/products/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_publications",
                "table_name": "publication",
                "endpoint": {
                    "path": "/publications",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_publicationsid",
                "table_name": "publication",
                "endpoint": {
                    "path": "/publications/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_artworkssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/artworks/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_agentssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/agents/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_placessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/places/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_galleriessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/galleries/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_exhibitionssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/exhibitions/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_category_termssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/category-terms/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_imagessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/images/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_videossearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/videos/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_soundssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/sounds/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_textssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/texts/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_productssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/products/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_tourssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/tours/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_mobile_soundssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/mobile-sounds/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_publicationssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/publications/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sectionssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/sections/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sitessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/sites/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_eventssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/events/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_event_occurrencessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/event-occurrences/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_event_programssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/event-programs/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_articlessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/articles/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_highlightssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/highlights/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_static_pagessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/static-pages/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_generic_pagessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/generic-pages/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_press_releasessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/press-releases/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_educator_resourcessearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/educator-resources/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_digital_catalogssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/digital-catalogs/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_digital_publication_sectionssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/digital-publication-sections/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_printed_catalogssearch",
                "table_name": "search",
                "endpoint": {
                    "path": "/printed-catalogs/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_search",
                "table_name": "search",
                "endpoint": {
                    "path": "/search",
                    "params": {
                        # the parameters below can optionally be configured
                        # "q": "OPTIONAL_CONFIG",
                        # "query": "OPTIONAL_CONFIG",
                        # "sort": "OPTIONAL_CONFIG",
                        # "from": "OPTIONAL_CONFIG",
                        # "size": "OPTIONAL_CONFIG",
                        # "facets": "OPTIONAL_CONFIG",
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sections",
                "table_name": "section",
                "endpoint": {
                    "path": "/sections",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sectionsid",
                "table_name": "section",
                "endpoint": {
                    "path": "/sections/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sites",
                "table_name": "site",
                "endpoint": {
                    "path": "/sites",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sitesid",
                "table_name": "site",
                "endpoint": {
                    "path": "/sites/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_sounds",
                "table_name": "sound",
                "endpoint": {
                    "path": "/sounds",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_soundsid",
                "table_name": "sound",
                "endpoint": {
                    "path": "/sounds/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_static_pages",
                "table_name": "static_page",
                "endpoint": {
                    "path": "/static-pages",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_static_pagesid",
                "table_name": "static_page",
                "endpoint": {
                    "path": "/static-pages/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_texts",
                "table_name": "text",
                "endpoint": {
                    "path": "/texts",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_textsid",
                "table_name": "text",
                "endpoint": {
                    "path": "/texts/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_tours",
                "table_name": "tour",
                "endpoint": {
                    "path": "/tours",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_toursid",
                "table_name": "tour",
                "endpoint": {
                    "path": "/tours/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
            {
                "name": "get_videos",
                "table_name": "video",
                "endpoint": {
                    "path": "/videos",
                    "paginator": "auto",
                },
            },
            {
                "name": "get_videosid",
                "table_name": "video",
                "endpoint": {
                    "path": "/videos/{id}",
                    "params": {
                        "id": "FILL_ME_IN",  # TODO: fill in required path parameter
                    },
                    "paginator": "auto",
                },
            },
        ],
    }

    return rest_api_source(source_config)
