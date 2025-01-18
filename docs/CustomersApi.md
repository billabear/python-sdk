# swagger_client.CustomersApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_seats_subscriptions**](CustomersApi.md#add_seats_subscriptions) | **POST** /subscription/{subscriptionId}/seats/add | Add Seats
[**apply_voucher_to_customer**](CustomersApi.md#apply_voucher_to_customer) | **POST** /customer/{customerId}/voucher | Apply voucher
[**create_customer**](CustomersApi.md#create_customer) | **POST** /customer | Create
[**create_customer_usage_limit**](CustomersApi.md#create_customer_usage_limit) | **POST** /customer/{customerId}/uasge-limit | Create Usage Limit
[**customer_customer_id_uasge_limit_limit_id_delete**](CustomersApi.md#customer_customer_id_uasge_limit_limit_id_delete) | **DELETE** /customer/{customerId}/uasge-limit/{limitId} | Delete Usage Limit
[**disable_customer**](CustomersApi.md#disable_customer) | **POST** /customer/{customerId}/disable | Disable Customer
[**enable_customer**](CustomersApi.md#enable_customer) | **POST** /customer/{customerId}/enable | Enable Customer
[**get_active_for_customer**](CustomersApi.md#get_active_for_customer) | **GET** /customer/{customerId}/subscription/active | List Customer Active Subscriptions
[**get_all_customers**](CustomersApi.md#get_all_customers) | **GET** /customer | List
[**get_customer_by_id**](CustomersApi.md#get_customer_by_id) | **GET** /customer/{customerId} | Detail
[**get_customer_costs**](CustomersApi.md#get_customer_costs) | **GET** /customer/{customerId}/costs | Usage Cost Estimate
[**get_customer_limits_by_id**](CustomersApi.md#get_customer_limits_by_id) | **GET** /customer/{customerId}/limits | Fetch Customer Limits
[**get_customer_usage_limits_by_id**](CustomersApi.md#get_customer_usage_limits_by_id) | **GET** /customer/{customerId}/uasge-limit | Fetch Customer Usage Limits
[**get_for_customer**](CustomersApi.md#get_for_customer) | **GET** /customer/{customerId}/subscription | List Customer Subscriptions
[**get_invoices_for_customer**](CustomersApi.md#get_invoices_for_customer) | **GET** /customer/{customerId}/invoices | List Customer Invoices
[**get_payments_for_customer**](CustomersApi.md#get_payments_for_customer) | **GET** /customer/{customerId}/payment | List Customer Payments
[**get_refunds_for_customer**](CustomersApi.md#get_refunds_for_customer) | **GET** /customer/{customerId}/refund | List Customer Refunds
[**list_payment_details**](CustomersApi.md#list_payment_details) | **GET** /customer/{customerId}/payment-methods | List Customer&#x27;s Payment Details
[**remove_seats_subscriptions**](CustomersApi.md#remove_seats_subscriptions) | **POST** /subscription/{subscriptionId}/seats/remove | Remove Seats
[**update_customer**](CustomersApi.md#update_customer) | **PUT** /customer/{customerId} | Update

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SeatsAddBody() # SeatsAddBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Add Seats
    api_response = api_instance.add_seats_subscriptions(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->add_seats_subscriptions: %s\n" % e)
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

# **apply_voucher_to_customer**
> apply_voucher_to_customer(body, customer_id)

Apply voucher

Apply Voucher to Customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.VoucherCode() # VoucherCode | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Apply voucher
    api_instance.apply_voucher_to_customer(body, customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->apply_voucher_to_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoucherCode**](VoucherCode.md)|  | 
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer**
> Customer create_customer(body)

Create

Create a customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Customer() # Customer | 

try:
    # Create
    api_response = api_instance.create_customer(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_usage_limit**
> UsageLimit create_customer_usage_limit(body, customer_id)

Create Usage Limit

Create Usage Limit for the custoemr

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.CustomerIdUasgelimitBody() # CustomerIdUasgelimitBody | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Create Usage Limit
    api_response = api_instance.create_customer_usage_limit(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->create_customer_usage_limit: %s\n" % e)
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

# **customer_customer_id_uasge_limit_limit_id_delete**
> customer_customer_id_uasge_limit_limit_id_delete(customer_id, usage_limit_id)

Delete Usage Limit

Delete Usage Limit for the custoemr

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
usage_limit_id = 'usage_limit_id_example' # str | The id of the usage limit

try:
    # Delete Usage Limit
    api_instance.customer_customer_id_uasge_limit_limit_id_delete(customer_id, usage_limit_id)
except ApiException as e:
    print("Exception when calling CustomersApi->customer_customer_id_uasge_limit_limit_id_delete: %s\n" % e)
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

# **disable_customer**
> disable_customer(customer_id)

Disable Customer

Disable customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Disable Customer
    api_instance.disable_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->disable_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_customer**
> enable_customer(customer_id)

Enable Customer

Enable a customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Enable Customer
    api_instance.enable_customer(customer_id)
except ApiException as e:
    print("Exception when calling CustomersApi->enable_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Active Subscriptions
    api_response = api_instance.get_active_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_active_for_customer: %s\n" % e)
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

# **get_all_customers**
> InlineResponse200 get_all_customers(limit=limit, last_key=last_key, email=email, country=country, reference=reference, external_reference=external_reference, company_name=company_name)

List

List all customers

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
email = 'email_example' # str | The email to search for (optional)
country = 'country_example' # str | The country code to search for (optional)
reference = 'reference_example' # str | The reference to search for (optional)
external_reference = 'external_reference_example' # str | The external reference to search for (optional)
company_name = 'company_name_example' # str | The company name to search for (optional)

try:
    # List
    api_response = api_instance.get_all_customers(limit=limit, last_key=last_key, email=email, country=country, reference=reference, external_reference=external_reference, company_name=company_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_all_customers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 
 **email** | **str**| The email to search for | [optional] 
 **country** | **str**| The country code to search for | [optional] 
 **reference** | **str**| The reference to search for | [optional] 
 **external_reference** | **str**| The external reference to search for | [optional] 
 **company_name** | **str**| The company name to search for | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_by_id**
> Customer get_customer_by_id(customer_id)

Detail

Info for a specific customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Detail
    api_response = api_instance.get_customer_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**Customer**](Customer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_costs**
> InlineResponse2001 get_customer_costs(customer_id)

Usage Cost Estimate

The estimated costs from usage based billing for a customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Usage Cost Estimate
    api_response = api_instance.get_customer_costs(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_costs: %s\n" % e)
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

# **get_customer_limits_by_id**
> InlineResponse2002 get_customer_limits_by_id(customer_id)

Fetch Customer Limits

Limits for a specific customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Fetch Customer Limits
    api_response = api_instance.get_customer_limits_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_limits_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Fetch Customer Usage Limits
    api_response = api_instance.get_customer_usage_limits_by_id(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_customer_usage_limits_by_id: %s\n" % e)
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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Subscriptions
    api_response = api_instance.get_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_for_customer: %s\n" % e)
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

# **get_invoices_for_customer**
> InlineResponse2006 get_invoices_for_customer(customer_id)

List Customer Invoices

List Customer Invoices

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Invoices
    api_response = api_instance.get_invoices_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_invoices_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_for_customer**
> InlineResponse2004 get_payments_for_customer(customer_id, limit=limit, last_key=last_key, name=name)

List Customer Payments

List Customer Payment

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List Customer Payments
    api_response = api_instance.get_payments_for_customer(customer_id, limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_payments_for_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 
 **name** | **str**| The name to search for | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List Customer Refunds
    api_response = api_instance.get_refunds_for_customer(customer_id, limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->get_refunds_for_customer: %s\n" % e)
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

# **list_payment_details**
> InlineResponse2007 list_payment_details(customer_id)

List Customer's Payment Details

List all customers <br><br>Added in version 1.1

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer's Payment Details
    api_response = api_instance.list_payment_details(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->list_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.SeatsRemoveBody() # SeatsRemoveBody | 
subscription_id = 'subscription_id_example' # str | The id of the subscription to retrieve

try:
    # Remove Seats
    api_response = api_instance.remove_seats_subscriptions(body, subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->remove_seats_subscriptions: %s\n" % e)
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

# **update_customer**
> Customer update_customer(body, customer_id)

Update

Update a customer

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
api_instance = swagger_client.CustomersApi(swagger_client.ApiClient(configuration))
body = swagger_client.Customer() # Customer | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Update
    api_response = api_instance.update_customer(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomersApi->update_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Customer**](Customer.md)|  | 
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**Customer**](Customer.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

