from coded_flows.types import Int, Iterable, Tuple, Any


coded_flows_metadata = {
    "display_name": "FOR EACH",
    "description": "FOR EACH loop",
    "type": "control",
    "icon": "arrow-iteration",
}


def for_each_loop(list: Iterable) -> Tuple[Any, Int]:
    index = 0
    element = ''
    return element, index