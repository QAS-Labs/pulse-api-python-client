# coding: utf-8

"""
    Pulse API

    Integrate all of your testing apps with Pulse API

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class LoginLogoutApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def login(self, domain, username, password, **kwargs):
        """
        login
        Get Pulse user token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.login(domain, username, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain: Domain name of user (required)
        :param str username: Username of user (required)
        :param str password: Password of user (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.login_with_http_info(domain, username, password, **kwargs)
        else:
            (data) = self.login_with_http_info(domain, username, password, **kwargs)
            return data

    def login_with_http_info(self, domain, username, password, **kwargs):
        """
        login
        Get Pulse user token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.login_with_http_info(domain, username, password, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str domain: Domain name of user (required)
        :param str username: Username of user (required)
        :param str password: Password of user (required)
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['domain', 'username', 'password']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method login" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'domain' is set
        if ('domain' not in params) or (params['domain'] is None):
            raise ValueError("Missing the required parameter `domain` when calling `login`")
        # verify the required parameter 'username' is set
        if ('username' not in params) or (params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `login`")
        # verify the required parameter 'password' is set
        if ('password' not in params) or (params['password'] is None):
            raise ValueError("Missing the required parameter `password` when calling `login`")


        collection_formats = {}

        resource_path = '/login'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'domain' in params:
            form_params.append(('domain', params['domain']))
        if 'username' in params:
            form_params.append(('username', params['username']))
        if 'password' in params:
            form_params.append(('password', params['password']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse200',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def logout(self, api_token, **kwargs):
        """
        logout
        Logout user from Pulse
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.logout(api_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_token: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.logout_with_http_info(api_token, **kwargs)
        else:
            (data) = self.logout_with_http_info(api_token, **kwargs)
            return data

    def logout_with_http_info(self, api_token, **kwargs):
        """
        logout
        Logout user from Pulse
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.logout_with_http_info(api_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str api_token: (required)
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method logout" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_token' is set
        if ('api_token' not in params) or (params['api_token'] is None):
            raise ValueError("Missing the required parameter `api_token` when calling `logout`")


        collection_formats = {}

        resource_path = '/logout'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}
        if 'api_token' in params:
            header_params['api-token'] = params['api_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2001',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
