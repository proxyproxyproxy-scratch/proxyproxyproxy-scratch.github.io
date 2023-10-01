import json
import requests

def save_response(response_data, save_path, get_path):
    try:
        content_type = response_data.get("content", {}).get("mimeType")
        if content_type:
            response_body = response_data.get("content", {}).get("text")
            if response_body:
                with open(save_path, "wb") as file:
                    file.write(response_body.encode("utf-8"))
                #print(f"Saved: {save_path}")
            else:
                print("No response body to save.")
        else:
            print("No content type information available.")
    except Exception as e:
        print(f"Error saving response: {str(e)}")

def main(har_file_path):
    with open(har_file_path, "r", encoding="utf-8") as har_file:
        har_data = json.load(har_file)
    
    entries = har_data.get("log", {}).get("entries", [])
    
    for entry in entries:
        response = entry.get("response", {})
        get_path = entry.get("request", {}).get("url")
        save_path = get_path.split("/")[-1]  # ファイル名を取得
        print(get_path)
        save_response(response, save_path, get_path)

if __name__ == "__main__":
    har_file_path = "C:/Users/USER/Downloads/god2/god/godfield.net.har"  # Harファイルのパスを指定
    main(har_file_path)