# Price

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**amount** | **int** |  | 
**currency** | **str** | Three-letter ISO currency code. Must be upper-case | 
**external_reference** | **str** |  | [optional] 
**recurring** | **bool** |  | 
**schedule** | **str** | Required if recurring is true | [optional] 
**including_tax** | **bool** | If the price is including tax. If false tax will be added on top of the price. | [optional] 
**public** | **bool** |  | [optional] 
**metric** | [**Metric**](Metric.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

