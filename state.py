from kubernetes import client, config

#using k8s API, get all pods state. Fire a flag when any # is not in Ready state (except for finished, idk)


# Configs can be set in Configuration class directly or using helper utility
def check_pod_state():
    config.load_kube_config()

    v1 = client.CoreV1Api()
    print("Listing pods with their statuses:")
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for i in ret.items:
        print("%s\t%s\t%s" % (i.status.phase, i.metadata.namespace, i.metadata.name))
        # print(ret)
        # print(ret.items)
    unhealthy = len(list(filter(
        lambda obj: obj.status.phase != 'Running',
        ret.items
    )))
    print(str(unhealthy) + " unhealthy out of " + str(len(ret.items))  + " Pods.")
        # TODO consider i.container_statuses for pods that haven't started yet