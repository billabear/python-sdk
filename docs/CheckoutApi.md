# swagger_client.CheckoutApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout**](CheckoutApi.md#create_checkout) | **POST** /checkout | Create Checkout

# **create_checkout**
> InlineResponse201 create_checkout(body)

Create Checkout

Create checkout<br><br><strong>Since 2024.01</strong>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CheckoutApi(swagger_client.ApiClient(configuration))
body = swagger_client.CheckoutBody() # CheckoutBody | 

try:
    # Create Checkout
    api_response = api_instance.create_checkout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutApi->create_checkout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CheckoutBody**](CheckoutBody.md)|  | 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

