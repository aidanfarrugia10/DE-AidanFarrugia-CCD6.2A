from main import app as fastapi_app
from mangum import Mangum

handler = Mangum(fastapi_app)

def handler(event, context):
    return handler(event, context)
