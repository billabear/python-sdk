# billabear.ReceiptApi

All URIs are relative to *https://{customerId}.billabear.cloud/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_receipt**](ReceiptApi.md#download_receipt) | **GET** /receipt/{receiptId}/download | Download Receipt

# **download_receipt**
> str download_receipt(receipt)

Download Receipt

Returns the pdf blob for the Receipt

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
api_instance = billabear.ReceiptApi(billabear.ApiClient(configuration))
receipt = 'receipt_example' # str | The id of the receipt

try:
    # Download Receipt
    api_response = api_instance.download_receipt(receipt)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReceiptApi->download_receipt: %s\n" % e)
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

