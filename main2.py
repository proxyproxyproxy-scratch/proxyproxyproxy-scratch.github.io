import json
import requests

def download_file(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"Saved: {save_path}")
        else:
            print(f"Failed to download: {url}")
    except Exception as e:
        print(f"Error downloading file: {str(e)}")

def main(har_file_path):
    with open(har_file_path, "r", encoding="utf-8") as har_file:
        har_data = json.load(har_file)
    
    entries = har_data.get("log", {}).get("entries", [])
    
    for entry in entries:
        request_url = entry.get("request", {}).get("url")
        if request_url:
            save_path = request_url.split("/")[-1]  # ファイル名を取得
            download_file(request_url, save_path)

if __name__ == "__main__":
    har_file_path = "C:/Users/USER/Downloads/god2/god/godfield.net.har"  # Harファイルのパスを指定
    main(har_file_path)
