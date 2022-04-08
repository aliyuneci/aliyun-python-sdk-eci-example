from aliyunsdkcore.client import AcsClient
from aliyunsdkeci.request.v20180808.CreateContainerGroupRequest import CreateContainerGroupRequest
from aliyunsdkeci.request.v20180808.DescribeContainerGroupsRequest import DescribeContainerGroupsRequest



def createContainerGroup():
    client = initClient()
    request = buildCreateContainerGroupRequest()

    # oss-volume
    volume1 = {
        'Name': 'oss-storage1',
        'Type': 'FlexVolume',
        "FlexVolume.Driver": "alicloud/oss",
        "FlexVolume.Options": {
            "url": "https://oss-" + REGION_ID + "-internal.aliyuncs.com",
            "bucket": bucket-name,
            "ramRole": ramRoleName
        },
    }

    volume2 = {
        'Name': 'oss-storage2',
        'Type': 'FlexVolume',
        "FlexVolume.Driver": "alicloud/oss",
        "FlexVolume.Options": {
             "url": "https://oss-" + REGION_ID + "-internal.aliyuncs.com",
            "bucket": bucket-name,
            "ramRole": ramRoleName
        },
    }

    request.set_Volumes([volume1, volume2])

    # mount volume
    volume_mount1 = {
        'Name': 'oss-storage1',
        'MountPath': '/oss1',
        'ReadOnly': False
    }

    volume_mount2 = {
        'Name': 'oss-storage2',
        'MountPath': '/oss2',
        'ReadOnly': False
    }

    # containers
    container1 = {
        'Image': 'registry-vpc.' + REGION_ID + '.aliyuncs.com/eci_open/nginx:alpine',
        'Name': 'nginx-liu',
        "Commands": ["/bin/sh", "-c", "sleep 999"],
        'VolumeMounts': [volume_mount1, volume_mount2],
    }
    request.set_Containers([container1])
    response = client.do_action_with_exception(request)
    print(response)

