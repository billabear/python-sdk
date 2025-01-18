# Invoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**currency** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**tax_total** | **int** |  | [optional] 
**sub_total** | **int** |  | [optional] 
**amount_due** | **int** |  | [optional] 
**paid** | **bool** |  | [optional] 
**pay_link** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**paid_at** | **str** |  | [optional] 
**due_date** | **str** |  | [optional] 
**biller_address** | [**Address**](Address.md) |  | [optional] 
**payeeaddress** | [**Address**](Address.md) |  | [optional] 
**lines** | [**list[InvoiceLines]**](InvoiceLines.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

