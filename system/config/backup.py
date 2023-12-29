import requests
import json


def establish_fortigate_session(ip, username, password):
    login_url = f"https://{ip}/logincheck"
    login_params = {"username": username, "secretkey": password}

    try:
        response = session.post(login_url, params=login_params, verify=False)
        response.raise_for_status()

        if response.status_code == 200:
            cookies = response.cookies
            csrf_token = cookies["ccsrftoken_443"].strip('"')
            aps_cookie = cookies["APSCOOKIE_443"]
            return session, csrf_token, aps_cookie
        else:
            return f"There was an issue connecting to {ip}. Status code: {response.status_code}"

    except (requests.exceptions.HTTPError, requests.RequestException) as err:
        return f"There was an error connecting to {ip}: {err}"


fg_ip = "10.1.1.110"
fg_username = "admin"
fg_password = "password"
session = requests.Session()


def backup_fortigate_config(ip, username, password):
    # Establish FortiGate session and obtain CSRF tokens
    session, csrf_token, aps_cookie = establish_fortigate_session(ip, username, password)

    # Construct backup request URL
    backup_url = f"https://{ip}/api/v2/monitor/system/config/backup"

    # Construct backup payload in JSON format
    payload = json.dumps({
        "destination": "file*",
        "scope": "global",
        "file_format": "fos*"
    })

    try:
        # Set headers with CSRF token for the backup request
        headers = {'x-csrftoken': csrf_token, 'Content-Type': 'application/json'}
    except Exception as e:
        print(e)

    # Send a POST request to initiate a configuration backup
    backup_config = session.request("POST", backup_url, headers=headers, data=payload, verify=False)

    # Write the backup configuration content to a local file
    with open("backup.conf", "w") as f:
        f.write(backup_config.text)
    print(f'Your file is saved into the local directory.')
    # Close the session


backup_fortigate_config(fg_ip, fg_username, fg_password)

session.close()
