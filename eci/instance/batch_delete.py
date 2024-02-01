import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkeci.request.v20180808.DescribeContainerGroupsRequest import DescribeContainerGroupsRequest
from aliyunsdkeci.request.v20180808.DeleteContainerGroupRequest import DeleteContainerGroupRequest


class BatchAction:
    def __init__(self, ak, sk, region_id):
        self.ak = ak
        self.sk = sk
        self.region_id = region_id
        self.client = AcsClient(ak=self.ak, secret=self.sk, region_id=self.region_id)

    def all(self, status=None):
        next_token = ""
        container_group_ids = []
        while True:
            describe = DescribeContainerGroupsRequest()
            describe.set_NextToken(next_token)
            if status:
                describe.set_Status(status)
            resp = self.client.do_action_with_exception(describe)
            result = json.loads(str(resp, 'utf-8'))
            if result.get('NextToken') != '':
                next_token = result.get("NextToken")
                for container_group in result.get("ContainerGroups"):
                    container_group_ids.append(container_group.get("ContainerGroupId"))
            if not result.get('NextToken'):
                for container_group in result.get("ContainerGroups"):
                    container_group_ids.append(container_group.get("ContainerGroupId"))
                break
        print(f"查询当前地域 {self.region_id} 总实例数: {len(container_group_ids)}")
        return container_group_ids

    def batch_delete(self, container_group_ids: list):
        if container_group_ids != []:
            for container_group_id in container_group_ids:
                delete = DeleteContainerGroupRequest()
                delete.set_ContainerGroupId(container_group_id)
                resp = self.client.do_action_with_exception(delete)
                print(f"Delete Resp: {resp} ---- {container_group_id}")


if __name__ == '__main__':
    demo = BatchAction("access_key_id", "access_key_secret", "cn-hangzhou")
    ecis = demo.all()
    print(ecis)
    demo.batch_delete(ecis)
