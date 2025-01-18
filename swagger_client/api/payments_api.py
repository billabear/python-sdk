# coding: utf-8

"""
    BillaBear

    The REST API provided by BillaBear  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@billabear.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class PaymentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def charge_invoice(self, invoice_id, **kwargs):  # noqa: E501
        """Charge Invoice  # noqa: E501

        Attempts to charge a card that is on file for the invoice amount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.charge_invoice(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: The id of the invoice (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.charge_invoice_with_http_info(invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.charge_invoice_with_http_info(invoice_id, **kwargs)  # noqa: E501
            return data

    def charge_invoice_with_http_info(self, invoice_id, **kwargs):  # noqa: E501
        """Charge Invoice  # noqa: E501

        Attempts to charge a card that is on file for the invoice amount  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.charge_invoice_with_http_info(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: The id of the invoice (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method charge_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `charge_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_id' in params:
            path_params['invoiceId'] = params['invoice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/invoice/{invoiceId}/charge', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20014',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_invoice(self, invoice_id, **kwargs):  # noqa: E501
        """Download Invoice  # noqa: E501

        Returns the pdf blob for the invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_invoice(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: The id of the invoice (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_invoice_with_http_info(invoice_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_invoice_with_http_info(invoice_id, **kwargs)  # noqa: E501
            return data

    def download_invoice_with_http_info(self, invoice_id, **kwargs):  # noqa: E501
        """Download Invoice  # noqa: E501

        Returns the pdf blob for the invoice  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_invoice_with_http_info(invoice_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id: The id of the invoice (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'invoice_id' is set
        if ('invoice_id' not in params or
                params['invoice_id'] is None):
            raise ValueError("Missing the required parameter `invoice_id` when calling `download_invoice`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'invoice_id' in params:
            path_params['invoiceId'] = params['invoice_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/invoice/{invoiceId}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_receipt(self, receipt, **kwargs):  # noqa: E501
        """Download Receipt  # noqa: E501

        Returns the pdf blob for the Receipt  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_receipt(receipt, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str receipt: The id of the receipt (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_receipt_with_http_info(receipt, **kwargs)  # noqa: E501
        else:
            (data) = self.download_receipt_with_http_info(receipt, **kwargs)  # noqa: E501
            return data

    def download_receipt_with_http_info(self, receipt, **kwargs):  # noqa: E501
        """Download Receipt  # noqa: E501

        Returns the pdf blob for the Receipt  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_receipt_with_http_info(receipt, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str receipt: The id of the receipt (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['receipt']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_receipt" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'receipt' is set
        if ('receipt' not in params or
                params['receipt'] is None):
            raise ValueError("Missing the required parameter `receipt` when calling `download_receipt`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'receipt' in params:
            path_params['receipt'] = params['receipt']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/pdf'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/receipt/{receiptId}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_invoices_for_customer(self, customer_id, **kwargs):  # noqa: E501
        """List Customer Invoices  # noqa: E501

        List Customer Invoices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoices_for_customer(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: The id of the customer to retrieve (required)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_invoices_for_customer_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_invoices_for_customer_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def get_invoices_for_customer_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """List Customer Invoices  # noqa: E501

        List Customer Invoices  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_invoices_for_customer_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: The id of the customer to retrieve (required)
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_invoices_for_customer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_invoices_for_customer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/customer/{customerId}/invoices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payments_for_customer(self, customer_id, **kwargs):  # noqa: E501
        """List Customer Payments  # noqa: E501

        List Customer Payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_for_customer(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: The id of the customer to retrieve (required)
        :param int limit: How many items to return at one time (max 100)
        :param str last_key: The key to be used in pagination to say what the last key of the previous page was
        :param str name: The name to search for
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_payments_for_customer_with_http_info(customer_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_payments_for_customer_with_http_info(customer_id, **kwargs)  # noqa: E501
            return data

    def get_payments_for_customer_with_http_info(self, customer_id, **kwargs):  # noqa: E501
        """List Customer Payments  # noqa: E501

        List Customer Payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_for_customer_with_http_info(customer_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str customer_id: The id of the customer to retrieve (required)
        :param int limit: How many items to return at one time (max 100)
        :param str last_key: The key to be used in pagination to say what the last key of the previous page was
        :param str name: The name to search for
        :return: InlineResponse2004
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'limit', 'last_key', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments_for_customer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params or
                params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_payments_for_customer`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'customer_id' in params:
            path_params['customerId'] = params['customer_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'last_key' in params:
            query_params.append(('last_key', params['last_key']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/customer/{customerId}/payment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2004',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_payment(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        List all payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: How many items to return at one time (max 100)
        :param str last_key: The key to be used in pagination to say what the last key of the previous page was
        :param str name: The name to search for
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_payment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_payment_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_payment_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        List all payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: How many items to return at one time (max 100)
        :param str last_key: The key to be used in pagination to say what the last key of the previous page was
        :param str name: The name to search for
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'last_key', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_payment" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'last_key' in params:
            query_params.append(('last_key', params['last_key']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/payment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refund_payment(self, body, payment_id, **kwargs):  # noqa: E501
        """Refund Payment  # noqa: E501

        Issue a refund for payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_payment(body, payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IssueRefundPayment body: (required)
        :param str payment_id: The id of the payment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refund_payment_with_http_info(body, payment_id, **kwargs)  # noqa: E501
        else:
            (data) = self.refund_payment_with_http_info(body, payment_id, **kwargs)  # noqa: E501
            return data

    def refund_payment_with_http_info(self, body, payment_id, **kwargs):  # noqa: E501
        """Refund Payment  # noqa: E501

        Issue a refund for payment  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refund_payment_with_http_info(body, payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param IssueRefundPayment body: (required)
        :param str payment_id: The id of the payment (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'payment_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refund_payment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `refund_payment`")  # noqa: E501
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `refund_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/payment/{paymentId}/refund', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
