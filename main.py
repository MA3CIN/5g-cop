import logs
import state 

# structure this around 5 modules: state, logs, metrics, traces...? + something from Service Mesh, not sure what (comm with their API)

print(logs.logs_fun())
print(state.check_pod_state())