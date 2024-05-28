example_1 = """
{
	"Description": "Add two numbers",
	"GrasshopperScriptModel":
	{
		"ChainOfThought": "To add two numbers we need to Add. There is an Addition component that performs this function. We need to create two numbers the user can edit, we can use the Number Slider for both numbers. And then we can Connections all of the components together",
		"Advice": "Make sure to set the number sliders to the correct value",
		"Additions": [
			{
				"Name": "Number Slider",
				"Id": 1,
				"value": "0..25..100"
			},
			{
				"Name": "Number Slider",
				"Id": 2,
				"value": "-50..25..100"
			},
			{
				"Name": "Addition",
				"Id": 3
			}
		],
		"Connections": [
			{
				"From": {
					"Id": 1,
					"ParameterName": "Value"
				},
				"To": {
					"Id": 3,
					"ParameterName": "A"
				}
			},
			{
				"From": {
					"Id": 2,
					"ParameterName": "Value"
				},
				"To": {
					"Id": 3,
					"ParameterName": "B"
				}
			}
		]
	}
}
"""


example_2 = """
{
	"Description": "Creates a cup shape in grasshopper",
	"GrasshopperScriptModel":
	{
		"ChainOfThought": "To create a cup shape in Grasshopper, we'll first create a circle using a 'Circle CNR' component, which will act as the base of the cup. Then, we will use a 'Move' component to move the base circle vertically to create the upper rim of the cup. To create the body of the cup, we'll loft these two circles using a 'Loft' component.",
		"Advice": "Remember, to properly define the cups dimensions using the number slider",
		"Additions": [
			{
				"Name": "Circle CNR",
				"Id": 1
			},
			{
				"Name": "Move",
				"Id": 2
			},
			{
				"Name": "Loft",
				"Id": 3
			}
		],
		"Connections": [
			{
				"From": {
					"Id": 1,
					"ParameterName": "Circle"
				},
				"To": {
					"Id": 2,
					"ParameterName": "Geometry"
				}
			},
			{
				"From": {
					"Id": 1,
					"ParameterName": "Circle"
				},
				"To": {
					"Id": 3,
					"ParameterName": "Curves"
				}
			},
			{
				"From": {
					"Id": 2,
					"ParameterName": "Geometry"
				},
				"To": {
					"Id": 3,
					"ParameterName": "Curves"
				}
			}
		]
	}
}
"""


example_3 = """
{
	"Description": "creates a twisty skyscraper",
	"GrasshopperScriptModel":
	{
		"ChainOfThought": "We can create the 'twist' using the twist component, so let's extrude a rectangle and twist it!",
		"Advice": "Make sure to use reasonable inputs or the skyscraper will look weird",
		"Additions": [
			{
				"Name": "Rectangle",
				"Id": 1
			},
			{
				"Name": "Number Slider",
				"Id": 2,
				"Value": "0..50..100"
			},
			{
				"Name": "Unit Z",
				"Id": 3
			},
			{
				"Name": "Extrude",
				"Id": 4
			},
			{
				"Name": "Number Slider",
				"Id": 5,
				"Value": "0..90..360"
			},
			{
				"Name": "Line",
				"Id": 6
			},
			{
				"Name": "Point",
				"Id": 7,
				"value": "{0,0,0}"
			},
			{
				"Name": "Point",
				"Id": 8,
				"value": "{0,0,250}"
			},
			{
				"Name": "Twist",
				"Id": 9
			},
			{
				"Name": "Solid Union",
				"Id": 10
			},
			{
				"Name": "Brep Join",
				"Id": 11
			}
		],
		"Connections": [
			{
				"From": {
					"Id": 1,
					"ParameterName": "Rectangle"
				},
				"To": {
					"Id": 4,
					"ParameterName": "Base"
				}
			},
			{
				"From": {
					"Id": 2,
					"ParameterName": "Value"
				},
				"To": {
					"Id": 3,
					"ParameterName": "Factor"
				}
			},
			{
				"From": {
					"Id": 5,
					"ParameterName": "Value"
				},
				"To": {
					"Id": 9,
					"ParameterName": "Angle"
				}
			},
			{
				"From": {
					"Id": 3,
					"ParameterName": "Unit vector"
				},
				"To": {
					"Id": 4,
					"ParameterName": "Direction"
				}
			},
			{
				"From": {
					"Id": 4,
					"ParameterName": "Extrusion"
				},
				"To": {
					"Id": 9,
					"ParameterName": "Geometry"
				}
			},
			{
				"From": {
					"Id": 7,
					"ParameterName": "Point"
				},
				"To": {
					"Id": 6,
					"ParameterName": "Start Point"
				}
			},
			{
				"From": {
					"Id": 8,
					"ParameterName": "Point"
				},
				"To": {
					"Id": 6,
					"ParameterName": "End Point"
				}
			},
			{
				"From": {
					"Id": 9,
					"ParameterName": "Geometry"
				},
				"To": {
					"Id": 10,
					"ParameterName": "Breps"
				}
			},
			{
				"From": {
					"Id": 10,
					"ParameterName": "Result"
				},
				"To": {
					"Id": 11,
					"ParameterName": "Breps"
				}
			},
			{
				"From": {
					"Id": 6,
					"ParameterName": "Line"
					},
				"To": {
					"Id": 9,
					"ParameterName": "Axis"
				}
			}
		]
	}
}
"""
