# swagger_client.PaymentsApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charge_invoice**](PaymentsApi.md#charge_invoice) | **POST** /invoice/{invoiceId}/charge | Charge Invoice
[**download_invoice**](PaymentsApi.md#download_invoice) | **GET** /invoice/{invoiceId}/download | Download Invoice
[**download_receipt**](PaymentsApi.md#download_receipt) | **GET** /receipt/{receiptId}/download | Download Receipt
[**get_invoices_for_customer**](PaymentsApi.md#get_invoices_for_customer) | **GET** /customer/{customerId}/invoices | List Customer Invoices
[**get_payments_for_customer**](PaymentsApi.md#get_payments_for_customer) | **GET** /customer/{customerId}/payment | List Customer Payments
[**list_payment**](PaymentsApi.md#list_payment) | **GET** /payment | List
[**refund_payment**](PaymentsApi.md#refund_payment) | **POST** /payment/{paymentId}/refund | Refund Payment

# **charge_invoice**
> InlineResponse20014 charge_invoice(invoice_id)

Charge Invoice

Attempts to charge a card that is on file for the invoice amount

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | The id of the invoice

try:
    # Charge Invoice
    api_response = api_instance.charge_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->charge_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The id of the invoice | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_invoice**
> str download_invoice(invoice_id)

Download Invoice

Returns the pdf blob for the invoice

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | The id of the invoice

try:
    # Download Invoice
    api_response = api_instance.download_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->download_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The id of the invoice | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_receipt**
> str download_receipt(receipt)

Download Receipt

Returns the pdf blob for the Receipt

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
receipt = 'receipt_example' # str | The id of the receipt

try:
    # Download Receipt
    api_response = api_instance.download_receipt(receipt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->download_receipt: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **receipt** | **str**| The id of the receipt | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Invoices
    api_response = api_instance.get_invoices_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_invoices_for_customer: %s\n" % e)
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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List Customer Payments
    api_response = api_instance.get_payments_for_customer(customer_id, limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->get_payments_for_customer: %s\n" % e)
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

# **list_payment**
> InlineResponse2009 list_payment(limit=limit, last_key=last_key, name=name)

List

List all payment

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | How many items to return at one time (max 100) (optional)
last_key = 'last_key_example' # str | The key to be used in pagination to say what the last key of the previous page was (optional)
name = 'name_example' # str | The name to search for (optional)

try:
    # List
    api_response = api_instance.list_payment(limit=limit, last_key=last_key, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentsApi->list_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **last_key** | **str**| The key to be used in pagination to say what the last key of the previous page was | [optional] 
 **name** | **str**| The name to search for | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_payment**
> refund_payment(body, payment_id)

Refund Payment

Issue a refund for payment

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
api_instance = swagger_client.PaymentsApi(swagger_client.ApiClient(configuration))
body = swagger_client.IssueRefundPayment() # IssueRefundPayment | 
payment_id = 'payment_id_example' # str | The id of the payment

try:
    # Refund Payment
    api_instance.refund_payment(body, payment_id)
except ApiException as e:
    print("Exception when calling PaymentsApi->refund_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IssueRefundPayment**](IssueRefundPayment.md)|  | 
 **payment_id** | **str**| The id of the payment | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

