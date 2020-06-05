#!/usr/bin/python

from eci.common.EciClient import *
from eci.common.model.ImagePullPolicy import ImagePullPolicy


def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()
    request.set_InstanceType("ecs.gn6v-c8g1.2xlarge")




    # containers
    container1 = {
        'Image': 'registry-vpc.cn-beijing.aliyuncs.com/eci_open/nginx:1.15.10',
        'Name': 'nginx',
        'Gpu': 1,
        'ImagePullPolicy': ImagePullPolicy.Always.value,
    }
    request.set_Containers([container1])

    response = client.do_action_with_exception(request)

    print response