from aliyunsdkcore.client import AcsClient
from aliyunsdkeci.request.v20180808.DeleteContainerGroupRequest import DeleteContainerGroupRequest
from aliyunsdkeci.request.v20180808.RestartContainerGroupRequest import RestartContainerGroupRequest



# Required parameters: ak, secret, region_id
client = AcsClient(ak="", secret="", region_id="")


def restart_container_group(container_group_id):
    request = RestartContainerGroupRequest()
    request.set_ContainerGroupId(container_group_id)
    response = client.do_action_with_exception(request)
        
    # python2:  print(response) 
    print(str(response, encoding='utf-8'))



if __name__ == '__main__':
    # restart Eci
    restart_container_group("eci-xx")




