import requests, time

def send_webhook(url, payload, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, timeout=5)
            if response.status_code == 200:
                print("✅ Success")
                return True
            else:
                print(f"❌ Failed with {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

        wait = 2 ** attempt  # exponential backoff: 1,2,4,8...
        print(f"Retrying in {wait} seconds...")
        time.sleep(wait)

    print("🚨 Max retries reached, giving up.")
    return False

# Example usage
send_webhook("https://webhook.site/036e3066-b18a-49f5-9927-3e1a61825e88", {"message": "hello from Yinka"})
