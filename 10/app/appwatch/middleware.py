import json
from typing import Any


class LoggingMiddleware:

    def __init__(self, get_response) -> None:
        self._get_response = get_response

    def __call__(self, request) -> Any:
        response = self._get_response(request)

        data = {
            'path': request.path,
            'method': request.method,
            'API': request.META['HTTP_HOST']
        }

        with open('request.log', 'a') as f:
            f.write(json.dumps(data) + '\n')
        return response
