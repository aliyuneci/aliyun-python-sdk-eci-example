# -*- coding: utf-8 -*-
# Copyright (c) 2024 Aliyun.com All right reserved. This software is the
# confidential and proprietary information of Aliyun.com ("Confidential
# Information"). You shall not disclose such Confidential Information and shall
# use it only in accordance with the terms of the license agreement you entered
# into with Aliyun.com .

# created by xiaohui at 2024/2/2 11:38
import json

from typing import List

from oslo_config import generator

from aliyunsdkcore.client import AcsClient

from aliyunsdkeci.request.v20180808.DescribeRegionsRequest import DescribeRegionsRequest
from aliyunsdkeci.request.v20180808.DescribeContainerGroupsRequest import DescribeContainerGroupsRequest
from aliyunsdkeci.request.v20180808.DeleteContainerGroupRequest import DeleteContainerGroupRequest

# 账号ak sk
AK_ID = ''
AK_SECRET = ''

# region_id='' 业务需要,请勿改动。
ali_eci_client = AcsClient(AK_ID, AK_SECRET, region_id='')


def describe_all_region():
    """查询ECI可以使用的阿里云地域"""
    req = DescribeRegionsRequest()
    req.set_endpoint('eci.aliyuncs.com')
    resp = ali_eci_client.do_action_with_exception(req)
    all_regions = [region_id.get('RegionId') for region_id in json.loads(resp).get('Regions')]
    print(f'当前 ECI 可以使用的阿里云地域: {all_regions}')
    return all_regions


def iter_pages_for_next_token(func):
    """
    NextToken翻页
    """
    def wrapper(*args, **kwargs):
        try:
            r = func(*args, **kwargs)
            yield r

            content = json.loads(r)
            next_token = content.get("NextToken")

            if next_token:
                kwargs["next_token"] = next_token

                for r in wrapper(*args, **kwargs):
                    yield r
        except Exception as e:
            print(f"Failed executing {func} with args {args}, kwargs {kwargs}: {e}.")
    return wrapper


@iter_pages_for_next_token
def _get_fill_container_groups(region, **kwargs) -> generator:
    req = DescribeContainerGroupsRequest()
    if kwargs.get("next_token"):
        req.set_NextToken(kwargs.get("next_token"))
    ali_eci_client.set_region_id(region)
    resp = ali_eci_client.do_action_with_exception(req)
    return resp


def get_fill_container_group_ids(region) -> List:
    """获取当前Region所有ECI实例id"""
    container_group_ids = []
    for page in _get_fill_container_groups(region):
        page_dict = json.loads(page)
        for eci in page_dict.get("ContainerGroups"):
            container_group_ids.append(eci.get("ContainerGroupId"))
    return container_group_ids


def clean_region_container_groups(region, container_group_id):
    """清理当前地域ECI"""
    req = DeleteContainerGroupRequest()
    req.set_ContainerGroupId(container_group_id)
    ali_eci_client.set_region_id(region)
    resp = ali_eci_client.do_action_with_exception(req)
    print(f"{resp} Clean {region} {container_group_id}")
    return resp


def delete_all_region_eci():
    for region in describe_all_region():
        for container_group_id in get_fill_container_group_ids(region):
            clean_region_container_groups(region, container_group_id)


if __name__ == '__main__':
    delete_all_region_eci()

