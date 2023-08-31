from contextlib import contextmanager

import requests


# response = requests.get("https://pokeapi.co/api/v2/pokemon/11")
# data = response.json()
# print (f" pockemon is {data['name']}")
class ApiClientContext:
    def __init__(self, base_url: str) -> None:
        self._client: ApiClient | None = None
        self._base_url: str = base_url

    def __enter__(self):
        self._client = ApiClient(base_url=self._base_url)
        return self._client

    def __exit__(self, exc_type, exc_value, tb):
        print(f"⚠️⚠️⚠️ Unexpected client's response: {exc_value}")
        self.close()

    def close(self):
        print("Closing the client")
        self._client.close()


class ApiClient:
    allowed_methods: list[str] = ["get"]

    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url

    def get_response(self, method: str, endpoint: str) -> dict:
        if method not in self.allowed_methods:
            raise NotImplementedError(f"Method {method} is not found ")

        callback = getattr(requests, method)
        # url = self.base_url + endpoint
        url = "".join([self.base_url, endpoint])
        response = callback(url)

        #    response.raise_for_status()

        try:
            response.raise_for_status()
            return response.json()
        except Exception:
            raise Exception("HTTP request Error")

        #    response = requests.get()


@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    print("inside init")
    try:
        yield "As value"
    finally:
        # Code to release resource, e.g.:
        print("Exiting")


with managed_resource() as value:
    print(value)


with ApiClientContext(base_url="https://pokeapi.co/api/v2/") as client:
    ditto_data = client.get_response(method="get", endpoint="/pokemon/11")
    print(f"Fetched pokemon: {ditto_data['name']}")
