# -*- coding: utf-8 -*-
# Copyright (c) 2023 Aliyun.com All right reserved. This software is the
# confidential and proprietary information of Aliyun.com ("Confidential
# Information"). You shall not disclose such Confidential Information and shall
# use it only in accordance with the terms of the license agreement you entered
# into with Aliyun.com .

# created by xiaohui at 2023/9/6


from aliyunsdkcore.client import AcsClient

from aliyunsdkeci.request.v20180808.CreateDataCacheRequest import CreateDataCacheRequest

AK = ''
SK = ''
Region = ''
SecurityGroupId = ''
VSwitchId = ''

client = AcsClient(ak=AK, secret=SK, region_id=Region)


def create_data_cache():
    """
    创建一个数据缓存资源
    @refer_doc: https://help.aliyun.com/document_detail/2412301.html?spm=a2c4g.2412236.0.0.69491542loE7Bl
    :return: {'RequestId': '', 'DataCacheId': ''}
    """
    req = CreateDataCacheRequest()
    # 数据缓存名称
    req.set_Name('test-data-cache')
    req.set_SecurityGroupId(SecurityGroupId)
    req.set_VSwitchId(VSwitchId)
    req.set_Path('/test/data-cache-resource/')

    """
    DataSource类型
    具体使用配置 @refer_doc: https://help.aliyun.com/document_detail/2391456.html?spm=a2c4g.2391452.0.0.68083200MG6KpP#3c9228a032ffp

    URL = {
        "Type": "URL",
        "Options": {"repoId": '', "repoSource": '', 'revision': '', 'accessToken': ''}
    }

    NAS = {
        'Type': 'NAS',
        'Options': {'server': '', 'path': '', 'vers': '', 'options': ''}
    }

    OSS = {
        'Type': 'OSS',
        'Options': {'bucket': '', 'url': '', 'path': '', 'otherOpts': '', 'ramRole': '', 'akId': '', 'akSecret': ''}
    }

    SNAPSHOT = {
        'Type': 'SNAPSHOT',
        'Options': {'snapshotId': ''}
    }

    CPFS = {
        'Type': 'CPFS',
        'Options': {'server': '', 'path': '', 'mountProtocol': '', 'volumeAs': ''}
    }

    """

    url = {
        "Type": "URL",
        "Options": {
            "repoId": 'qwen/Qwen-7B-Chat',
            "repoSource": 'ModelScope/Model'
        }
    }
    req.set_DataSource(url)

    # 数据缓存大小。单位为GiB，默认为20 GiB。请根据实际数据量评估所需大小.
    # req.set_Size(50)

    # 若vpc或者交换机未开通公网能力则无法下载model。可以通过绑定nat网关 或者 可以使用随实例创建eip的方式实现外网能力。
    # req.set_EipCreateParam({'Bandwidth': 50})

    resp = client.do_action_with_exception(req)
    return resp


if __name__ == '__main__':
    create_data_cache()
