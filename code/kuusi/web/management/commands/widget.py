"""
kuusi
Copyright (C) 2014-2024  Christoph Müller  <mail@chmr.eu>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from typing import Dict, List, Callable, Type
from web.models import Category, Page, Widget, HTMLWidget, SessionVersionWidget, FacetteSelectionWidget, NavigationWidget, ResultShareWidget, ResultListWidget, FacetteRadioSelectionWidget
from logging import getLogger
logger = getLogger('command') 
def create_widgets(get_or_default: Callable[[str, Dict], any], haystack: Dict) -> List[Widget]:
    got = []

    key_map = {
        "html": HTMLWidget,
        "version": SessionVersionWidget,
        "selection": FacetteSelectionWidget,
        "radio": FacetteRadioSelectionWidget,
        "share": ResultShareWidget,
        "result": ResultListWidget,  
        "navigation": NavigationWidget
    }
    # FIXME: This currently doe
    prop_map: Dict[str, Dict[str, Type]]= {
        "html": {"template": str},
        "selection": {"topic":str},
        "radio": {"topic":str}
    }
    # check validity in terms of type definitions:
    for key in haystack.keys():
        if key not in key_map:
            raise Exception(f"Key of widget type not found: {key}")
    

    for key, widget_class in key_map.items():
        elements = haystack[key]
        # TODO: The Widget base class does not feature a real catalogue id. COnsider changing.
        for catalogue_id, properties in elements.items():
            logger.debug(f"Current widget: {catalogue_id}")
            new_widget: Widget = widget_class(
                row = get_or_default("row", properties),
                col = get_or_default("col", properties),
                width = get_or_default("width", properties)
            )
                
            new_widget.save()
            pages = properties["pages"]
            page_catalogue_id: str
            for page_catalogue_id in pages:
                new_widget.pages.add(Page.objects.get(catalogue_id=page_catalogue_id))

            if key in prop_map:
                for key, value in prop_map[key].items():
                    # TODO: Make this asisgnment more variable (especially for List[Type] szenarios)
                    if value in [str, int, float]:
                        new_widget.__setattr__(key, properties[key])
                    else:
                        raise NotImplementedError()

            new_widget.save()
            got.append(new_widget)



    return got
