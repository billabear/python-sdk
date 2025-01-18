# swagger_client.SubscriptionsApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_seats_subscriptions**](SubscriptionsApi.md#add_seats_subscriptions) | **POST** /subscription/{subscriptionId}/seats/add | Add Seats
[**cancel_subscription**](SubscriptionsApi.md#cancel_subscription) | **POST** /subscription/{subscriptionId}/cancel | Cancel Subscription
[**change_subscription_price**](SubscriptionsApi.md#change_subscription_price) | **POST** /subscription/{subscriptionId}/price | Change Price
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /customer/{customerId}/subscription/start | Create Subscription
[**customer_change_subscription_plan**](SubscriptionsApi.md#customer_change_subscription_plan) | **POST** /subscription/{subscriptionId}/plan | Change Subscription Plan
[**extend_trial**](SubscriptionsApi.md#extend_trial) | **POST** /subscription/{subscriptionId}/extend | Extend Trial Subscription
[**get_active_for_customer**](SubscriptionsApi.md#get_active_for_customer) | **GET** /customer/{customerId}/subscription/active | List Customer Active Subscriptions
[**get_for_customer**](SubscriptionsApi.md#get_for_customer) | **GET** /customer/{customerId}/subscription | List Customer Subscriptions
[**list_subscription_plans**](SubscriptionsApi.md#list_subscription_plans) | **GET** /subscription/plans | List Subscription Plans
[**list_subscriptions**](SubscriptionsApi.md#list_subscriptions) | **GET** /subscription | List
[**remove_seats_subscriptions**](SubscriptionsApi.md#remove_seats_subscriptions) | **POST** /subscription/{subscriptionId}/seats/remove | Remove Seats
[**show_subscription_by_id**](SubscriptionsApi.md#show_subscription_by_id) | **GET** /subscription/{subscriptionId} | Detail
[**start_trial**](SubscriptionsApi.md#start_trial) | **POST** /customer/{customerId}/subscription/trial | Start Trial Subscription For Customer

# **add_seats_subscriptions**
> InlineResponse20013 add_seats_subscriptions(body, subscription_id)

Add Seats

Adds seats to a per seat subscription<br><br><strong>Since 1.1.4</strong>

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SeatsAddBody() # SeatsAddBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Add Seats
    api_response = api_instance.add_seats_subscriptions(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_seats_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SeatsAddBody**](SeatsAddBody.md)|  | 
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription**
> cancel_subscription(body, subscription_id)

Cancel Subscription

Info for a specific subscription

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionIdCancelBody() # SubscriptionIdCancelBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Cancel Subscription
    api_instance.cancel_subscription(body, subscription_id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->cancel_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionIdCancelBody**](SubscriptionIdCancelBody.md)|  | 
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_subscription_price**
> InlineResponse20013 change_subscription_price(body, subscription_id)

Change Price

Changes the price being used for a price. Useful for changing pricing schedule or just price.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionIdPriceBody() # SubscriptionIdPriceBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Change Price
    api_response = api_instance.change_subscription_price(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->change_subscription_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionIdPriceBody**](SubscriptionIdPriceBody.md)|  | 
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subscription**
> Subscription create_subscription(body, customer_id)

Create Subscription

Create subscription for a customer

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionStartBody() # SubscriptionStartBody | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Create Subscription
    api_response = api_instance.create_subscription(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionStartBody**](SubscriptionStartBody.md)|  | 
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_change_subscription_plan**
> Subscription customer_change_subscription_plan(body, subscription_id)

Change Subscription Plan

Change the subscription plan for a customer

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionIdPlanBody() # SubscriptionIdPlanBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Change Subscription Plan
    api_response = api_instance.customer_change_subscription_plan(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->customer_change_subscription_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionIdPlanBody**](SubscriptionIdPlanBody.md)|  | 
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extend_trial**
> Subscription extend_trial(body, subscription_id)

Extend Trial Subscription

Extend a trial subscription so it's converted from a trial to a normal subscription.

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionIdExtendBody() # SubscriptionIdExtendBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Extend Trial Subscription
    api_response = api_instance.extend_trial(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->extend_trial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionIdExtendBody**](SubscriptionIdExtendBody.md)|  | 
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_for_customer**
> InlineResponse2008 get_active_for_customer(customer_id)

List Customer Active Subscriptions

List all Active customer subscriptions

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Active Subscriptions
    api_response = api_instance.get_active_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_active_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_for_customer**
> InlineResponse2008 get_for_customer(customer_id)

List Customer Subscriptions

List all customer subscriptions<br><br><strong>Since 1.1</strong>

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Subscriptions
    api_response = api_instance.get_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscription_plans**
> InlineResponse20012 list_subscription_plans(limit=limit, last_key=last_key)

List Subscription Plans

List all subscriptions plans

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)

try:
    # List Subscription Plans
    api_response = api_instance.list_subscription_plans(limit=limit, last_key=last_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_subscription_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscriptions**
> InlineResponse2008 list_subscriptions(limit=limit, last_key=last_key)

List

List all subscriptions

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)

try:
    # List
    api_response = api_instance.list_subscriptions(limit=limit, last_key=last_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_seats_subscriptions**
> InlineResponse20013 remove_seats_subscriptions(body, subscription_id)

Remove Seats

Remove seats to a per seat subscription<br><br><strong>Since 1.1.4</strong>

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SeatsRemoveBody() # SeatsRemoveBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Remove Seats
    api_response = api_instance.remove_seats_subscriptions(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->remove_seats_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SeatsRemoveBody**](SeatsRemoveBody.md)|  | 
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_subscription_by_id**
> Subscription show_subscription_by_id(subscription_id)

Detail

Info for a specific subscription

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Detail
    api_response = api_instance.show_subscription_by_id(subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->show_subscription_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The id of the subscription to retrieve | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_trial**
> Subscription start_trial(body, customer_id)

Start Trial Subscription For Customer

Start subscription for a customer

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
api_instance = swagger_client.SubscriptionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.SubscriptionTrialBody() # SubscriptionTrialBody | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Start Trial Subscription For Customer
    api_response = api_instance.start_trial(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->start_trial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionTrialBody**](SubscriptionTrialBody.md)|  | 
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

