# coding: utf-8

"""
 Copyright 2023 TikTok Pte. Ltd.

 This source code is licensed under the MIT license found in
 the LICENSE file in the root directory of this source tree.
"""
from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from business_api_client.api_client import ApiClient


class ReportingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def report_integrated_get(self, advertiser_id, report_type, dimensions, access_token, **kwargs):  # noqa: E501
        """Create a synchronous report task.  This endpoint can currently return the reporting data of up to 10,000 advertisements. If your number of advertisements exceeds 10,000, please use campaign_ids / adgroup_ids / ad_ids as a filter to obtain the reporting data of all advertisements in batches. Additionally, with CHUNK mode on, up to 20,000 advertisements can be returned. If you use campaign_ids / adgroup_ids / ad_ids as a filter, you can pass in up to 100 IDs at a time. [Reporting Get](https://ads.tiktok.com/marketing_api/docs?id=1740302848100353)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.report_integrated_get(advertiser_id, report_type, dimensions, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str advertiser_id: Advertiser ID (required)
        :param str report_type: Report type. Enum values- `BASIC` (basic report), `AUDIENCE` (audience report), `PLAYABLE_MATERIAL`  (playable ads report), `CATALOG` (DSA report). When `service_type` is `RESERVATION`, only `BASIC` report is supported. When `service_type` is `AUCTION`, `BASIC`, `AUDIENCE`, `PLAYABLE_MATERIAL`, and `CATALOG` reports are all supported. (required)
        :param list[str] dimensions: Grouping conditions. For example- `［\"campaign_id\", \"stat_time_day\"］` indicates that both `campaign_id` and `stat_time_day` (days) are grouped. For supported dimensions for each report type, see the corresponding articles under [Report types](https://ads.tiktok.com/marketing_api/docs?id=1738864835805186). (required)
        :param str access_token: Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162). (required)
        :param str service_type: Ad service type. Enum values:`AUCTION`(Auction Ads), `RESERVATION`(Reservation Ads). Default value `AUCTION`.
        :param str data_level: The data level that you'd like to query in reports. Required when `report_type` is `BASIC`,`AUDIENCE` or `CATALOG`. Enum values `AUCTION_AD` Auction Ads, Ad level. `AUCTION_ADGROUP` Auction Ads, Ad Group level. `AUCTION_CAMPAIGN` Auction Ads, Campaign level. `AUCTION_ADVERTISER` Auction Ads, Advertiser level. `RESERVATION_AD` Reservation Ads, Ad level. `RESERVATION_ADGROUP` Reservation Ads, Ad Group level. RESERVATION_CAMPAIGN` Reservation Ads, Campaign level. `RESERVATION_ADVERTISER` Reservation Ads, Advertiser level.
        :param list[str] metrics: Metrics to query. Different report types support different metrics.  For supported metrics for each report type, see the corresponding articles under [Report types](https://ads.tiktok.com/marketing_api/docs?id=1738864835805186).
        :param str order_field: Sorting field. All supported metrics (excluding attribute metrics) support sorting. Not sorting by default.
        :param str order_type: Sorting order. Enum values- `ASC`, `DESC`. Default value- `DESC`.
        :param str start_date: Query start date (closed interval) in the format of `YYYY-MM-DD`. The date is based on the ad account time zone. This field is required when `query_lifetime` is `False`.
        :param str end_date: Query end date (closed interval) in the format of `YYYY-MM-DD`. The date is based on the ad account time zone. This field is required when `query_lifetime` is `False`.
        :param list[FilteringReportIntegratedGet] filtering: Filtering conditions. Supported filtering conditions vary based on `service_type` and `data_level`. For filters supported in different report types, refer to the articles under [Report types](https://ads.tiktok.com/marketing_api/docs?id=1738864835805186).
        :param bool query_lifetime: Whether to request the lifetime metrics.  Default value- `False`. If `query_lifetime` = `True`, the `start_date` and `end_date` parameters will be ignored. The lifetime metric name is the same as the normal one.
        :param int page: Current page number. Default value- `1`
        :param int page_size: Pagination size. Value range- 1-1000. Default value- `10`.
        :param str query_mode: The way data is queried. Enum values- `REGULAR`, `CHUNK`. Default value- `REGULAR`.  With `CHUNK` mode on, data can be returned much faster in a more stable way. Meanwhile, pagination will not be working with `CHUNK`.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.report_integrated_get_with_http_info(advertiser_id, report_type, dimensions, access_token, **kwargs)  # noqa: E501
        else:
            (data) = self.report_integrated_get_with_http_info(advertiser_id, report_type, dimensions, access_token, **kwargs)  # noqa: E501
            return data

    def report_integrated_get_with_http_info(self, advertiser_id, report_type, dimensions, access_token, **kwargs):  # noqa: E501
        """Create a synchronous report task.  This endpoint can currently return the reporting data of up to 10,000 advertisements. If your number of advertisements exceeds 10,000, please use campaign_ids / adgroup_ids / ad_ids as a filter to obtain the reporting data of all advertisements in batches. Additionally, with CHUNK mode on, up to 20,000 advertisements can be returned. If you use campaign_ids / adgroup_ids / ad_ids as a filter, you can pass in up to 100 IDs at a time. [Reporting Get](https://ads.tiktok.com/marketing_api/docs?id=1740302848100353)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.report_integrated_get_with_http_info(advertiser_id, report_type, dimensions, access_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str advertiser_id: Advertiser ID (required)
        :param str report_type: Report type. Enum values- `BASIC` (basic report), `AUDIENCE` (audience report), `PLAYABLE_MATERIAL`  (playable ads report), `CATALOG` (DSA report). When `service_type` is `RESERVATION`, only `BASIC` report is supported. When `service_type` is `AUCTION`, `BASIC`, `AUDIENCE`, `PLAYABLE_MATERIAL`, and `CATALOG` reports are all supported. (required)
        :param list[str] dimensions: Grouping conditions. For example- `［\"campaign_id\", \"stat_time_day\"］` indicates that both `campaign_id` and `stat_time_day` (days) are grouped. For supported dimensions for each report type, see the corresponding articles under [Report types](https://ads.tiktok.com/marketing_api/docs?id=1738864835805186). (required)
        :param str access_token: Authorized access token. For details, see [Authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162). (required)
        :param str service_type: Ad service type. Enum values:`AUCTION`(Auction Ads), `RESERVATION`(Reservation Ads). Default value `AUCTION`.
        :param str data_level: The data level that you'd like to query in reports. Required when `report_type` is `BASIC`,`AUDIENCE` or `CATALOG`. Enum values `AUCTION_AD` Auction Ads, Ad level. `AUCTION_ADGROUP` Auction Ads, Ad Group level. `AUCTION_CAMPAIGN` Auction Ads, Campaign level. `AUCTION_ADVERTISER` Auction Ads, Advertiser level. `RESERVATION_AD` Reservation Ads, Ad level. `RESERVATION_ADGROUP` Reservation Ads, Ad Group level. RESERVATION_CAMPAIGN` Reservation Ads, Campaign level. `RESERVATION_ADVERTISER` Reservation Ads, Advertiser level.
        :param list[str] metrics: Metrics to query. Different report types support different metrics.  For supported metrics for each report type, see the corresponding articles under [Report types](https://ads.tiktok.com/marketing_api/docs?id=1738864835805186).
        :param str order_field: Sorting field. All supported metrics (excluding attribute metrics) support sorting. Not sorting by default.
        :param str order_type: Sorting order. Enum values- `ASC`, `DESC`. Default value- `DESC`.
        :param str start_date: Query start date (closed interval) in the format of `YYYY-MM-DD`. The date is based on the ad account time zone. This field is required when `query_lifetime` is `False`.
        :param str end_date: Query end date (closed interval) in the format of `YYYY-MM-DD`. The date is based on the ad account time zone. This field is required when `query_lifetime` is `False`.
        :param list[FilteringReportIntegratedGet] filtering: Filtering conditions. Supported filtering conditions vary based on `service_type` and `data_level`. For filters supported in different report types, refer to the articles under [Report types](https://ads.tiktok.com/marketing_api/docs?id=1738864835805186).
        :param bool query_lifetime: Whether to request the lifetime metrics.  Default value- `False`. If `query_lifetime` = `True`, the `start_date` and `end_date` parameters will be ignored. The lifetime metric name is the same as the normal one.
        :param int page: Current page number. Default value- `1`
        :param int page_size: Pagination size. Value range- 1-1000. Default value- `10`.
        :param str query_mode: The way data is queried. Enum values- `REGULAR`, `CHUNK`. Default value- `REGULAR`.  With `CHUNK` mode on, data can be returned much faster in a more stable way. Meanwhile, pagination will not be working with `CHUNK`.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['advertiser_id', 'report_type', 'dimensions', 'access_token', 'service_type', 'data_level', 'metrics', 'order_field', 'order_type', 'start_date', 'end_date', 'filtering', 'query_lifetime', 'page', 'page_size', 'query_mode']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method report_integrated_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'advertiser_id' is set
        if ('advertiser_id' not in params or
                params['advertiser_id'] is None):
            raise ValueError("Missing the required parameter `advertiser_id` when calling `report_integrated_get`")  # noqa: E501
        # verify the required parameter 'report_type' is set
        if ('report_type' not in params or
                params['report_type'] is None):
            raise ValueError("Missing the required parameter `report_type` when calling `report_integrated_get`")  # noqa: E501
        # verify the required parameter 'dimensions' is set
        if ('dimensions' not in params or
                params['dimensions'] is None):
            raise ValueError("Missing the required parameter `dimensions` when calling `report_integrated_get`")  # noqa: E501
        # verify the required parameter 'access_token' is set
        if ('access_token' not in params or
                params['access_token'] is None):
            raise ValueError("Missing the required parameter `access_token` when calling `report_integrated_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'advertiser_id' in params:
            query_params.append(('advertiser_id', params['advertiser_id']))  # noqa: E501
        if 'service_type' in params:
            query_params.append(('service_type', params['service_type']))  # noqa: E501
        if 'data_level' in params:
            query_params.append(('data_level', params['data_level']))  # noqa: E501
        if 'report_type' in params:
            query_params.append(('report_type', params['report_type']))  # noqa: E501
        if 'dimensions' in params:
            query_params.append(('dimensions', params['dimensions']))  # noqa: E501
            collection_formats['dimensions'] = 'multi'  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
            collection_formats['metrics'] = 'multi'  # noqa: E501
        if 'order_field' in params:
            query_params.append(('order_field', params['order_field']))  # noqa: E501
        if 'order_type' in params:
            query_params.append(('order_type', params['order_type']))  # noqa: E501
        if 'start_date' in params:
            query_params.append(('start_date', params['start_date']))  # noqa: E501
        if 'end_date' in params:
            query_params.append(('end_date', params['end_date']))  # noqa: E501
        if 'filtering' in params:
            query_params.append(('filtering', params['filtering']))  # noqa: E501
            collection_formats['filtering'] = 'multi'  # noqa: E501
        if 'query_lifetime' in params:
            query_params.append(('query_lifetime', params['query_lifetime']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page_size', params['page_size']))  # noqa: E501
        if 'query_mode' in params:
            query_params.append(('query_mode', params['query_mode']))  # noqa: E501

        header_params = {}
        if 'access_token' in params:
            header_params['Access-Token'] = params['access_token']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/open_api/v1.3/report/integrated/get/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse200',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
