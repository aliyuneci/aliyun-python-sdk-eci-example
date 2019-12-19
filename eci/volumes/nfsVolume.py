#!/usr/bin/python

from eci.common.EciClient import *
from eci.common.model.VolumeType import VolumeType
from eci.common.model.ImagePullPolicy import ImagePullPolicy

from eci.common.Constant import REGION_ID


def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()

    # volumes
    volume2 = {
        'Name': 'default-volume2-nfs',
        'Type': VolumeType.NFSVolume.value,
        'NFSVolume.Path': '/',
        'NFSVolume.Server': '0a1bf4a604-rahxx.cn-hangzhou.nas.aliyuncs.com',
        'NFSVolume.ReadOnly': False,
    }
    request.set_Volumes([volume2])

    # volumeMounts
    volume_mount2 = {
        'Name': 'default-volume2-nfs',
        'MountPath': '/usr/share',
        'ReadOnly': False,
    }

    # containers
    container1 = {
        'Image': 'registry-vpc.' + REGION_ID + '.aliyuncs.com/eci_open/nginx:alpine',
        'Name': 'nginx-liu',
        'Cpu': 2,
        'Memory': 4,
        'ImagePullPolicy': ImagePullPolicy.Always.value,
        'VolumeMounts': [volume_mount2],
    }
    request.set_Containers([container1])

    response = client.do_action_with_exception(request)

    print response
