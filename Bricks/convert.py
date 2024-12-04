from coded_flows.types import Any, Str
from coded_flows.utils import convert_type

coded_flows_metadata = {
    "display_name": "Convert",
    "description": "Converts a value from one type to another",
    "type": "converter",
    "icon": "transform-filled",
}


def convert(input: Any, input_type: Str = "Any", output_type: Str = "Any") -> Any:
    output = convert_type(input, input_type, output_type)
    return output
