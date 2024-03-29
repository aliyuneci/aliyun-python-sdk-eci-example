#!/usr/bin/python

from aliyunsdkcore.client import AcsClient
from aliyunsdkeci.request.v20180808.CreateContainerGroupRequest import CreateContainerGroupRequest
from aliyunsdkeci.request.v20180808.DescribeContainerGroupsRequest import DescribeContainerGroupsRequest
from aliyunsdkeci.request.v20180808.DeleteContainerGroupRequest import DeleteContainerGroupRequest

from eci.common.Constant import *

def initClient():
    client = AcsClient(
        AK_ID,
        AK_SECRET,
        REGION_ID,
    )

    return client


def buildCreateContainerGroupRequest():
    request = CreateContainerGroupRequest()
    request.set_ContainerGroupName('liu-test-python-sdk')
    request.set_RestartPolicy('Never')
    request.set_SecurityGroupId(SECURITY_GROUP_ID)
    request.set_VSwitchId(VSWITCH_ID)

    return request





