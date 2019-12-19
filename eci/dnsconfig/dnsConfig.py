#!/usr/bin/python

from eci.common.EciClient import *
from eci.common.model.DnsPolicy import DnsPolicy
from eci.common.model.ImagePullPolicy import ImagePullPolicy

from eci.common.Constant import REGION_ID


def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()

    # dns options
    option1 = {
        'Name': 'ndots',
        'Value': '5',
    }
    # DNS config
    request.set_DnsConfigOptions([option1])
    request.set_DnsConfigNameServers(['100.100.2.138', '100.100.2.136'])
    request.set_DnsConfigSearchs(['default.svc.cluster.local.c79f7ab6360f346348fb79dd00e719cc0',
                                  'svc.cluster.local.c79f7ab6360f346348fb79dd00e719cc0',
                                  'cluster.local.c79f7ab6360f346348fb79dd00e719cc0',
                                  'local.c79f7ab6360f346348fb79dd00e719cc0',
                                  'c79f7ab6360f346348fb79dd00e719cc0',
                                  ])
    request.set_DnsPolicy(DnsPolicy.Policy_ClusterFirst.value)

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
