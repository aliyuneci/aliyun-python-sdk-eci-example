#!/usr/bin/python

from eci.common.EciClient import *
from eci.common.model.VolumeType import VolumeType
from eci.common.model.ImagePullPolicy import ImagePullPolicy
from eci.common.Constant import REGION_ID

import base64


def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()

    # volumes
    configFileToPath1 = {
        'Path': 'nginx-proxy.conf',
        'Content': base64.b64encode("content1"),

    }

    configFileToPath2 = {
        'Path': 'access.lua',
        'Content': base64.b64encode("content2"),
    }

    volume3 = {
        'Name': 'default-volume3-config',
        'Type': VolumeType.ConfigFileVolume.value,
        'ConfigFileVolume.ConfigFileToPaths': [configFileToPath1, configFileToPath2],
    }
    request.set_Volumes([volume3])

    # volumeMounts
    volume_mount3 = {
        'Name': 'default-volume3-config',
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
        'VolumeMounts': [volume_mount3],
    }
    request.set_Containers([container1])

    response = client.do_action_with_exception(request)

    print(response)
