# swagger_client.InvoicesApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**charge_invoice**](InvoicesApi.md#charge_invoice) | **POST** /invoice/{invoiceId}/charge | Charge Invoice
[**download_invoice**](InvoicesApi.md#download_invoice) | **GET** /invoice/{invoiceId}/download | Download Invoice
[**get_invoices_for_customer**](InvoicesApi.md#get_invoices_for_customer) | **GET** /customer/{customerId}/invoices | List Customer Invoices

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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | The id of the invoice

try:
    # Charge Invoice
    api_response = api_instance.charge_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->charge_invoice: %s\n" % e)
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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | The id of the invoice

try:
    # Download Invoice
    api_response = api_instance.download_invoice(invoice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->download_invoice: %s\n" % e)
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
api_instance = swagger_client.InvoicesApi(swagger_client.ApiClient(configuration))
customer_id = 'customer_id_example' # str | The id of the customer to retrieve

try:
    # List Customer Invoices
    api_response = api_instance.get_invoices_for_customer(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->get_invoices_for_customer: %s\n" % e)
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

