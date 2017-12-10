import json

from astexport import parse as parse_text, export_json

def parse(event, context = None):
    code = event["body"]
    ast = parse_text(code)
    serialized = export_json(ast, False)

    response = {
        "statusCode": 200,
        "body": serialized
    }

    return response
