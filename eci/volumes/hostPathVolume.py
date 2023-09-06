# -*- coding: utf-8 -*-
# Copyright (c) 2023 Aliyun.com All right reserved. This software is the
# confidential and proprietary information of Aliyun.com ("Confidential
# Information"). You shall not disclose such Confidential Information and shall
# use it only in accordance with the terms of the license agreement you entered
# into with Aliyun.com .

# created by xiaohui at 2023/9/6 15:40

from eci.common.EciClient import *
from eci.common.model.VolumeType import VolumeType
from eci.common.model.ImagePullPolicy import ImagePullPolicy

from eci.common.Constant import REGION_ID


def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()

    # volumes
    volume1 = {
        'Name': 'test1',
        'Type': VolumeType.HostPathVolume.value,
        'HostPathVolume.Type': 'File',
        'HostPathVolume.Path': '/pod/data'
    }
    request.set_Volumes([volume1])

    volume_mount1 = {'Name': 'test1', 'MountPath': '/tmp', 'ReadOnly': False}
    container1 = {
        "Image": "registry-vpc.cn-hangzhou.aliyuncs.com/eci_open/nginx:alpine",
        "Name": "nginx",
        'VolumeMounts': [volume_mount1],
    }
    request.set_Containers([container1])
    response = client.do_action_with_exception(request)
    print(response)
