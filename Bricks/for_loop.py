from coded_flows.types import Int


coded_flows_metadata = {
    "display_name": "FOR",
    "description": "FOR loop",
    "type": "control",
    "icon": "repeat",
    "options": [
        {
            "name": "start",
            "type": "integer",
            "step": 1,
            "max": 10000000000,
            "min": -10000000000,
            "default": 0,
        },
        {
            "name": "end",
            "type": "integer",
            "step": 1,
            "max": 10000000000,
            "min": -10000000000,
            "default": 10,
        },
    ],
}


def for_loop(start: Int, end:Int, options) -> Int:
    index = 0
    return index