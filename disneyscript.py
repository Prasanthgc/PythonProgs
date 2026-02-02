import subprocess
import json
from datetime import datetime, timedelta


# Replace these values with your actual credentials and URLs

baseURL = "https://iics-icinq1.informaticacloud.com"
serverURL = "https://na1.iics-icinq1.informaticacloud.com"
USERNAME = "username"
PASSWORD = "Password"



def login():
    login_command = f'curl --location --request POST "{baseURL}/ma/api/v2/user/login" --header "Content-Type: application/json" --header "Accept: application/json" --data-raw "{{\\"username\\": \\"{USERNAME}\\", \\"password\\": \\"{PASSWORD}\\"}}"'
    response = subprocess.check_output(login_command, shell=True, universal_newlines=True)
    response = response.strip()
    response = response[1:-1]  # Remove surrounding double quotes
    icSessionId = ""
    for item in response.split(','):
        if '"icSessionId"' in item:
            icSessionId = item.strip()
            break
    return icSessionId

def get_task_list(icSessionId):
    task_list_command = f'curl --location --request GET "{serverURL}/saas/api/v2/activity/activityMonitor?details=true" --header "{icSessionId}" --header "Connection: keep-alive"'
    task_list_response = subprocess.check_output(task_list_command, shell=True, universal_newlines=True)
    return task_list_response.strip()




# Function to filter data from the last 24 hours
def filter_last_24_hours(data):
    # Get current time and subtract 24 hours to get the cutoff time
    current_time = datetime.utcnow()
    cutoff_time = current_time - timedelta(days=1)

    # Filter data based on startTime being within the last 24 hours
    filtered_data = []
    for entry in data:
        start_time = datetime.strptime(entry["startTime"], "%Y-%m-%dT%H:%M:%S.000Z")

        if start_time >= cutoff_time:
            filtered_data.append(entry)

    return filtered_data


def filter_by_time_range(data, start_time, end_time):

    start_time  = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S.000Z")
    end_time    = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S.000Z")

    # print("start_time: ",start_time)
    # print("end_time: ", end_time)

    # Filter data based on startTime being within the specified time range
    filtered_data = []
    for entry in data:
        entry_time = datetime.strptime(entry["startTime"], "%Y-%m-%dT%H:%M:%S.000Z")

        if start_time <= entry_time <= end_time:
            filtered_data.append(entry)

    return filtered_data

def get_all_task_list(icSessionId,start_time,end_time):
    task_list_command = f'curl --location --request GET "{serverURL}/saas/api/v2/activity/activityLog" --header "{icSessionId}" --header "Connection: keep-alive"'
    task_list_response = subprocess.check_output(task_list_command, shell=True, universal_newlines=True)

    json_data = json.loads(task_list_response)
#to get report for last 24hrs

    #json_data = filter_last_24_hours(json_data)

#to get report between specified start & end time

    json_data = filter_by_time_range(json_data, start_time, end_time)
    return json_data


def print_activity_log_table(data):
    import json

    # Map UIState to session status
    ui_state_mapping = {
        1: "Succeeded",
        2: "Warning",
        3: "Failed",
        6: "Stopped",

    }

    # Prepare headers
    headers = ["startTime","Workflow Name", "Session Name", "Transformation Name", "Success Rows", "Rejected Rows", "Session Status"]
    max_lengths = [len(header) for header in headers]
    rows = []

    # Extract data
    for entry in data:
        entries = entry.get("entries", [])
        for sub_entry in entries:
            # Parse taskRuntimeInfo for asset
            task_runtime_info = sub_entry.get("taskRuntimeInfo", None)
            asset = "N/A"
            if task_runtime_info:
                try:
                    task_runtime_info_json = json.loads(task_runtime_info)
                    payload = task_runtime_info_json.get("payload", {})
                    invoke_context = payload.get("invokeContext", {})
                    call_stack = invoke_context.get("callStack", [])
                    if call_stack:
                        asset = call_stack[0].get("asset", "N/A")
                except (json.JSONDecodeError, TypeError):
                    pass

            # Extract transformations
            transformations = sub_entry.get("transformationEntries", [])
            session_status = ui_state_mapping.get(sub_entry.get("UIState"), "Unknown")
            for transformation in transformations:
                row = [
                    entry.get("startTime", "N/A"),
                    asset,
                    entry.get("objectName", "N/A"),
                    transformation.get("txName", "N/A"),
                    transformation.get("successRows", 0),
                    transformation.get("failedRows", 0),
                    session_status,
                ]
                rows.append(row)
                # Update max_lengths for dynamic table width
                for i, cell in enumerate(row):
                    max_lengths[i] = max(max_lengths[i], len(str(cell)))

    # Helper functions for table formatting
    def print_row(row):
        formatted = " | ".join(str(cell).ljust(max_lengths[i]) for i, cell in enumerate(row))
        print(f"| {formatted} |")

    def print_separator():
        print("+-" + "-+-".join("-" * length for length in max_lengths) + "-+")

    # Print the table
    print_separator()
    print_row(headers)
    print_separator()
    for row in rows:
        print_row(row)
    print_separator()



# Sample start time - "2024-11-24T10:30:00.000Z"

start_time = "2024-11-19T10:30:00.000Z"
end_time   = "2024-11-22T00:32:30.000Z"


icSessionId = login()
task_list_response = get_all_task_list(icSessionId,start_time,end_time)
print_activity_log_table(task_list_response)

