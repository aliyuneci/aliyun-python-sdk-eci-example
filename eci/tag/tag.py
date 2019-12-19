#!/usr/bin/python

from eci.common.EciClient import *
from eci.common.model.ImagePullPolicy import ImagePullPolicy

from eci.common.Constant import REGION_ID


def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()

    # tags
    tag1 = {
        'Key': 'test',
        'Value': 'sdk-python',
    }
    tag2 = {
        'Key': 'app',
        'Value': 'nginx',
    }

    request.set_Tags([tag1, tag2])

    # containers
    container1 = {
        'Image': 'registry-vpc.' + REGION_ID + '.aliyuncs.com/eci_open/nginx:alpine',
        'Name': 'nginx-liu',
        'Cpu': 2,
        'Memory': 4,
        'ImagePullPolicy': ImagePullPolicy.Always.value,
    }
    request.set_Containers([container1])

    response = client.do_action_with_exception(request)

    print response
