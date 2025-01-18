# swagger_client.PaymentDetailsApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_frontend_payment_details**](PaymentDetailsApi.md#complete_frontend_payment_details) | **POST** /customer/{customerId}/payment-methods/frontend-payment-token | Complete Frontend Detail Collection
[**delete_payment_details**](PaymentDetailsApi.md#delete_payment_details) | **DELETE** /payment-methods/{paymentDetailsId} | Delete
[**delete_payment_details_customer**](PaymentDetailsApi.md#delete_payment_details_customer) | **DELETE** /customer/{customerId}/payment-methods/{paymentDetailsId} | Delete With Customer
[**get_payment_details**](PaymentDetailsApi.md#get_payment_details) | **GET** /payment-methods/{paymentDetailsId} | Fetch
[**list_payment_details**](PaymentDetailsApi.md#list_payment_details) | **GET** /customer/{customerId}/payment-methods | List Customer&#x27;s Payment Details
[**make_default_payment_details**](PaymentDetailsApi.md#make_default_payment_details) | **POST** /payment-methods/{paymentDetailsId}/default | Make Default
[**make_default_payment_details_customer**](PaymentDetailsApi.md#make_default_payment_details_customer) | **POST** /customer/{customerId}/payment-methods/{paymentDetailsId}/default | Make Default With Customer
[**start_frontend_payment_details**](PaymentDetailsApi.md#start_frontend_payment_details) | **GET** /customer/{customerId}/payment-methods/frontend-payment-token | Start Frontend Detail Collection

# **complete_frontend_payment_details**
> PaymentDetails complete_frontend_payment_details(body, customer_id)

Complete Frontend Detail Collection

Complete frontend payment details

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
body = swagger_client.FrontendToken() # FrontendToken | 
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Complete Frontend Detail Collection
    api_response = api_instance.complete_frontend_payment_details(body, customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->complete_frontend_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FrontendToken**](FrontendToken.md)|  | 
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**PaymentDetails**](PaymentDetails.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_details**
> delete_payment_details(payment_details_id)

Delete

Delete Payment Details

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
payment_details_id = 'payment_details_id_example' # str | The id of the payment details

try:
    # Delete
    api_instance.delete_payment_details(payment_details_id)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->delete_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_details_id** | **str**| The id of the payment details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_details_customer**
> delete_payment_details_customer(customer_id, payment_details_id)

Delete With Customer

Delete Payment Details

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
payment_details_id = 'payment_details_id_example' # str | The id of the payment details

try:
    # Delete With Customer
    api_instance.delete_payment_details_customer(customer_id, payment_details_id)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->delete_payment_details_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 
 **payment_details_id** | **str**| The id of the payment details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_details**
> PaymentDetails get_payment_details(payment_details_id)

Fetch

Fetch the payment cards

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
payment_details_id = 'payment_details_id_example' # str | The id of the payment details

try:
    # Fetch
    api_response = api_instance.get_payment_details(payment_details_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->get_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_details_id** | **str**| The id of the payment details | 

### Return type

[**PaymentDetails**](PaymentDetails.md)

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer's Payment Details
    api_response = api_instance.list_payment_details(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->list_payment_details: %s\n" % e)
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

# **make_default_payment_details**
> make_default_payment_details(customer_id, payment_details_id)

Make Default

Delete Payment Details

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
payment_details_id = 'payment_details_id_example' # str | The id of the payment details

try:
    # Make Default
    api_instance.make_default_payment_details(customer_id, payment_details_id)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->make_default_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 
 **payment_details_id** | **str**| The id of the payment details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_default_payment_details_customer**
> make_default_payment_details_customer(customer_id, payment_details_id)

Make Default With Customer

Delete Payment Details

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
payment_details_id = 'payment_details_id_example' # str | The id of the payment details

try:
    # Make Default With Customer
    api_instance.make_default_payment_details_customer(customer_id, payment_details_id)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->make_default_payment_details_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 
 **payment_details_id** | **str**| The id of the payment details | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_frontend_payment_details**
> FrontendToken start_frontend_payment_details(customer_id)

Start Frontend Detail Collection

Start frontend payment details

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
api_instance = swagger_client.PaymentDetailsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # Start Frontend Detail Collection
    api_response = api_instance.start_frontend_payment_details(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentDetailsApi->start_frontend_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| The id of the customer to retrieve | 

### Return type

[**FrontendToken**](FrontendToken.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

