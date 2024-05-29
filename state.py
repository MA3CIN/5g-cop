def state_fun():
    return ("ret from state")

#using k8s API, get all pods state. Fire a flag when any # is not in Ready state (except for finished, idk)