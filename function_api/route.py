#route.py
from starlette.routing import Route
from function_api.services import *

item_view = ItemView()

routes = [
    Route("/items/{item_id}", item_view.get, methods=["GET"]),
    Route("/items", item_view.post, methods=["POST"]),
    Route("/items/{item_id}", item_view.put, methods=["PUT"]),
    Route("/items/{item_id}", item_view.delete, methods=["DELETE"]),
]
