from pprint import pprint

import openapi_client
from openapi_client.rest import ApiException

# Defining the host is optional and defaults to http://localhost

# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(host="http://localhost:8000")


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    item_id = 56  # int |
    q = "q_example"  # str |  (optional)

    try:
        # Read Item
        api_response = api_instance.read_item_items_item_id_get(item_id, q=q)
        print("The response of DefaultApi->read_item_items_item_id_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->read_item_items_item_id_get: %s\n" % e)
