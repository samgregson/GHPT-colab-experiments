from jsonschema import ValidationError
from models.models import GrasshopperScriptModel
import pytest


def test_gh_model_pass():
    example_json = {
        "ChainOfThought": "Use the sphere component with a number slider as"
        "input to set the radius",
        "Advice": "Adjust the radius of the sphere using a number slider for"
        "desired size",
        "Additions": [
            {
                "Name": "Sphere",
                "Id": 1
            },
            {
                "Name": "Number Slider",
                "Id": 2,
                "Value": "5..50..100"
            }
        ],
        "Connections": [
            {
                "To": {
                    "Id": 1,
                    "ParameterName": "Radius"
                },
                "From": {
                    "Id": 2,
                    "ParameterName": "Number"
                }
            }
        ]
    }

    try:
        GrasshopperScriptModel(**example_json)
    except ValidationError as e:
        assert False, f"Failed parsing json: {str(e)}"


def test_gh_model_component_fail():
    example_json = {
        "ChainOfThought": "Use the sphere component with a number slider as"
        "input to set the radius",
        "Advice": "Adjust the radius of the sphere using a number slider for"
        "desired size",
        "Additions": [
            {
                "Name": "Sphere",
                "Id": 1
            },
            {
                "Name": "Slider",
                "Id": 2,
                "Value": "5..50..100"
            }
        ],
        "Connections": [
            {
                "To": {
                    "Id": 1,
                    "ParameterName": "Radius"
                },
                "From": {
                    "Id": 2,
                    "ParameterName": "Number"
                }
            }
        ]
    }

    with pytest.raises(ValueError) as e:
        GrasshopperScriptModel(**example_json)
    assert e.typename == "ValidationError"