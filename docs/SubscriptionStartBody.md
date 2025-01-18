# SubscriptionStartBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_plan** | **str** | The ID for the subscription plan to be used (Can also be the code name) | 
**payment_details** | **str** | The Id for the customer&#x27;s payment details to be used | [optional] 
**card_token** | **str** | A stripe card token that&#x27;s been created using Stripe&#x27;s js sdk. It&#x27;ll create the payment details for the customer. | [optional] 
**price** | **str** | The ID for the price to be used | [optional] 
**schedule** | **str** | The schedule of the plan that is to be started. Only used if price isn&#x27;t given. Requires currency as well. | [optional] 
**currency** | **str** | The currency of the plan that is to be started. Only used if price isn&#x27;t given. Requires schedule as well. | [optional] 
**seat_numbrers** | **int** |  | [optional] 
**deny_trial** | [**Bool**](Bool.md) |  | [optional] 
**metadata** | **object** | Any metadata you want to add to a subscription | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

