import os
import json
import requests

PATH = "./data/"

def read_json():
    all_json_list = []
    for filename in os.listdir(PATH):
        # every file in this dir has a different path
        full_path = f"{PATH}{filename}"
        try:
            with open(full_path, "r") as file:
                json_data = json.load(file)
                all_json_list.append(json_data)
        except json.JSONDecodeError as e:
            print(f"Error: Failed to decode json file {e}")

    # making the data one big list[dict] (every json file is a list[dict])
    simplefied_json = simplefy_multiple_json(all_json_list)
    return simplefied_json

def simplefy_multiple_json(json_files: list[list]):
    result = []
    for json_file in json_files:
        for event in json_file:
            result.append(event)
    return result



def detect_format(content_type: str) -> str:
    content_type = content_type.lower()

    if "application/json" in content_type:
        return "json"
    if "text/csv" in content_type:
        return "csv"
    if "text/plain" in content_type:
        return "text"
    return "binary"


def safe_get_request(session, url, *, params=None, timeout=10):
    try:
        response = session.get(
            url=url,
            params=params,
            timeout=timeout
        )

        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        data_format = detect_format(content_type)

        if data_format == "json":
            data = response.json()
        elif data_format in ("csv", "text"):
            data = response.text
        else:
            data = response.content

        return {
            "ok": True,
            "status_code": response.status_code,
            "format": data_format,
            "data": data
        }

    except requests.exceptions.RequestException as e:
        return {
            "ok": False,
            "error": str(e)
        }
