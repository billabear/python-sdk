# billabear.ProductsApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_product**](ProductsApi.md#create_product) | **POST** /product | Create
[**list_product**](ProductsApi.md#list_product) | **GET** /product | List
[**show_product_by_id**](ProductsApi.md#show_product_by_id) | **GET** /product/{productId} | Detail
[**update_product**](ProductsApi.md#update_product) | **PUT** /product/{productId} | Update

# **create_product**
> create_product(body)

Create

Create a product

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
api_instance = billabear.ProductsApi(billabear.ApiClient(configuration))
body = billabear.Product() # Product | 

try:
    # Create
    api_instance.create_product(body)
except ApiException as e:
    print("Exception when calling ProductsApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](Product.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_product**
> InlineResponse20010 list_product(limit=limit, last_key=last_key, name=name)

List

List all products

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
api_instance = billabear.ProductsApi(billabear.ApiClient(configuration))
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List
    api_response = api_instance.list_product(limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->list_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 
 **name** | **str**| The name to search for | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_product_by_id**
> Product show_product_by_id(product_id)

Detail

Info for a specific product

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
api_instance = billabear.ProductsApi(billabear.ApiClient(configuration))
product_id = 'product_id_example' # str | The id of the product to retrieve

try:
    # Detail
    api_response = api_instance.show_product_by_id(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->show_product_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The id of the product to retrieve | 

### Return type

[**Product**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_product**
> Product update_product(product_id)

Update

Update a product

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
api_instance = billabear.ProductsApi(billabear.ApiClient(configuration))
product_id = 'product_id_example' # str | The id of the product to retrieve

try:
    # Update
    api_response = api_instance.update_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The id of the product to retrieve | 

### Return type

[**Product**](Product.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

