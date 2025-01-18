# billabear.UsageApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_usage_limit**](UsageApi.md#create_customer_usage_limit) | **POST** /customer/{customerId}/uasge-limit | Create Usage Limit
[**create_event**](UsageApi.md#create_event) | **POST** /events | Create Event
[**customer_customer_id_uasge_limit_limit_id_delete**](UsageApi.md#customer_customer_id_uasge_limit_limit_id_delete) | **DELETE** /customer/{customerId}/uasge-limit/{limitId} | Delete Usage Limit
[**get_customer_costs**](UsageApi.md#get_customer_costs) | **GET** /customer/{customerId}/costs | Usage Cost Estimate
[**get_customer_usage_limits_by_id**](UsageApi.md#get_customer_usage_limits_by_id) | **GET** /customer/{customerId}/uasge-limit | Fetch Customer Usage Limits

# **create_customer_usage_limit**
> UsageLimit create_customer_usage_limit(body, customer_id)

Create Usage Limit

Create Usage Limit for the custoemr

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
api_instance = billabear.UsageApi(billabear.ApiClient(configuration))
body = billabear.CustomerIdUasgelimitBody() # CustomerIdUasgelimitBody | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Create Usage Limit
    api_response = api_instance.create_customer_usage_limit(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->create_customer_usage_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CustomerIdUasgelimitBody**](CustomerIdUasgelimitBody.md)|  | 
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**UsageLimit**](UsageLimit.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_event**
> create_event(body)

Create Event

Creates an event that is used for usage billing

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
api_instance = billabear.UsageApi(billabear.ApiClient(configuration))
body = billabear.Event() # Event | 

try:
    # Create Event
    api_instance.create_event(body)
except ApiException as e:
    print("Exception when calling UsageApi->create_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Event**](Event.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_id_uasge_limit_limit_id_delete**
> customer_customer_id_uasge_limit_limit_id_delete(customer_id, usage_limit_id)

Delete Usage Limit

Delete Usage Limit for the custoemr

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
api_instance = billabear.UsageApi(billabear.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
usage_limit_id = 'usage_limit_id_example' # str | The id of the usage limit

try:
    # Delete Usage Limit
    api_instance.customer_customer_id_uasge_limit_limit_id_delete(customer_id, usage_limit_id)
except ApiException as e:
    print("Exception when calling UsageApi->customer_customer_id_uasge_limit_limit_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 
 **usage_limit_id** | **str**| The id of the usage limit | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_costs**
> InlineResponse2001 get_customer_costs(customer_id)

Usage Cost Estimate

The estimated costs from usage based billing for a customer

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
api_instance = billabear.UsageApi(billabear.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Usage Cost Estimate
    api_response = api_instance.get_customer_costs(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_customer_costs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_usage_limits_by_id**
> InlineResponse2005 get_customer_usage_limits_by_id(customer_id)

Fetch Customer Usage Limits

Usage Limits for a specific customer

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
api_instance = billabear.UsageApi(billabear.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Fetch Customer Usage Limits
    api_response = api_instance.get_customer_usage_limits_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsageApi->get_customer_usage_limits_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

