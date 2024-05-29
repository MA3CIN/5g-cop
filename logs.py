import os

# from /var/logs/pod or /containers get logs for given name (f5gc, o5gs)
# filter for Warning/Errors

def handle_single_log_file(fileName):
    pass


def check_logs(location = './test-logs/var/log/pods', core_type = 'open5gs'):
    selectedFiles =  os.listdir(location)
    for file in selectedFiles:
        if core_type in file:
            pass
    pass

check_logs()