# billabear.PricesApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_price**](PricesApi.md#create_price) | **POST** /product/{productId}/price | Create
[**list_price**](PricesApi.md#list_price) | **GET** /product/{productId}/price | List

# **create_price**
> create_price(body, product_id)

Create

Create a price

### Example
```python
from __future__ import print_function
import time
import billabear
from billabear.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = billabear.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = billabear.PricesApi(billabear.ApiClient(configuration))
body = billabear.Price() # Price | 
product_id = 'product_id_example' # str | The id of the product to retrieve

try:
    # Create
    api_instance.create_price(body, product_id)
except ApiException as e:
    print("Exception when calling PricesApi->create_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Price**](Price.md)|  | 
 **product_id** | **str**| The id of the product to retrieve | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price**
> InlineResponse20011 list_price(product_id, limit=limit, last_key=last_key)

List

List all prices

### Example
```python
from __future__ import print_function
import time
import billabear
from billabear.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = billabear.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = billabear.PricesApi(billabear.ApiClient(configuration))
product_id = 'product_id_example' # str | The id of the product to retrieve
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)

try:
    # List
    api_response = api_instance.list_price(product_id, limit=limit, last_key=last_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PricesApi->list_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The id of the product to retrieve | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

