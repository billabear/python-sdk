# Customer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | 
**tax_number** | **str** | The tax number for the customer &lt;strong&gt;Since 1.1&lt;/strong&gt; | [optional] 
**standard_tax_rate** | **float** | The tax rate for the customer on for standard services a &lt;strong&gt;Since 1.1&lt;/strong&gt; | [optional] 
**digital_tax_rate** | **float** | The tax rate for the customer on digital services &lt;strong&gt;Since 1.1&lt;/strong&gt; | [optional] 
**billing_type** | **str** | Choice between card and invoice | [optional] 
**type** | **str** | Choice between &#x27;individual&#x27; and &#x27;business&#x27;. When not provided &#x27;individual&#x27; is used. &lt;strong&gt;Since 1.1&lt;/strong&gt; | [optional] 
**reference** | **str** |  | [optional] 
**external_reference** | **str** |  | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**locale** | **str** | Defaults to &#x27;en&#x27; if not sent. | [optional] 
**brand** | **str** | Defaults to &#x27;default&#x27; if not sent. | [optional] 
**invoice_format** | **str** | Choice between &#x27;pdf&#x27; and &#x27;xrechnung&#x27;. &lt;strong&gt;Since 2024.02.01&lt;/strong&gt; | [optional] 
**marketing_opt_in** | **bool** | If the customer has opted in for marketing | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

