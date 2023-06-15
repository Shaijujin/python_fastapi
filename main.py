# main.py
from fastapi import *
from function_api.route import *
import uvicorn



app = FastAPI()
for route in routes:
    app.add_api_route(route.path, route.endpoint, methods=route.methods)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)