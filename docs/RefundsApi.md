# swagger_client.RefundsApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_refunds_for_customer**](RefundsApi.md#get_refunds_for_customer) | **GET** /customer/{customerId}/refund | List Customer Refunds
[**list_refund**](RefundsApi.md#list_refund) | **GET** /refund | List
[**show_refund_by_id**](RefundsApi.md#show_refund_by_id) | **GET** /refund/{refundId} | Detail

# **get_refunds_for_customer**
> InlineResponse2003 get_refunds_for_customer(customer_id, limit=limit, last_key=last_key, name=name)

List Customer Refunds

List Customer Refund

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
api_instance = swagger_client.RefundsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List Customer Refunds
    api_response = api_instance.get_refunds_for_customer(customer_id, limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->get_refunds_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 
 **name** | **str**| The name to search for | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refund**
> InlineResponse2003 list_refund(limit=limit, last_key=last_key, name=name)

List

List all refund

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
api_instance = swagger_client.RefundsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List
    api_response = api_instance.list_refund(limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->list_refund: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 
 **name** | **str**| The name to search for | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_refund_by_id**
> Refund show_refund_by_id(refund_id)

Detail

Info for a specific Refund

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
api_instance = swagger_client.RefundsApi(swagger_client.ApiClient(configuration))
refund_id = 'refund_id_example' # str | The id of the refund

try:
    # Detail
    api_response = api_instance.show_refund_by_id(refund_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefundsApi->show_refund_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| The id of the refund | 

### Return type

[**Refund**](Refund.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

