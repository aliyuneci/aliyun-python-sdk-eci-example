# -*- coding: utf-8 -*-
# Copyright (c) 2023 Aliyun.com All right reserved. This software is the
# confidential and proprietary information of Aliyun.com ("Confidential
# Information"). You shall not disclose such Confidential Information and shall
# use it only in accordance with the terms of the license agreement you entered
# into with Aliyun.com .

# created by xiaohui at 2023/9/6 15:44
from aliyunsdkcore.client import AcsClient
from aliyunsdkeci.request.v20180808.DescribeDataCachesRequest import DescribeDataCachesRequest


AK = ''
SK = ''
Region = ''

client = AcsClient(ak=AK, secret=SK, region_id=Region)


def describe_data_cache(data_cache_id: list):
    """
    查询数据缓存
    @refer_doc: https://help.aliyun.com/document_detail/2412302.html?spm=a2c4g.2412236.0.0.37fc55c1Zveu5Q
    :param data_cache_id: ['edc-xxx', 'edc-xxx']
    :return:
    """
    req = DescribeDataCachesRequest()
    req.set_DataCacheId(data_cache_id)
    resp = client.do_action_with_exception(req)
    return resp


if __name__ == '__main__':
    print(describe_data_cache(['edc-xxx']))
