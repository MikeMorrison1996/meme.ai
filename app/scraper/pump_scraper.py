import requests
import json
import os

# Output file path
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'output')
DATA_PATH = os.path.join(OUTPUT_DIR, "clean_token_data.json")

# Updated to use Solana and the specific pairId provided
CHAIN_ID = "solana"
PAIR_ID = "GiqkyXUkexS2WNMadEKq1JRPELcF97nU7zHz1DH4zyvM"
DEX_PROFILES_API = f"https://api.dexscreener.com/latest/dex/pairs/{CHAIN_ID}/{PAIR_ID}"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_token(meta):
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as f:
            json.dump([], f)

    with open(DATA_PATH, "r+") as f:
        try:
            existing = json.load(f)
        except json.JSONDecodeError:
            existing = []

        existing.append(meta)
        f.seek(0)
        json.dump(existing, f, indent=2)
        f.truncate()

def fetch_and_save_tokens():
    print("📥 Fetching Solana token data from DEX Screener...")
    try:
        res = requests.get(DEX_PROFILES_API)
        if res.ok:
            token = res.json().get("pair", {})
            token_data = {
                "name": token.get("baseToken", {}).get("name", ""),
                "ticker": token.get("baseToken", {}).get("symbol", ""),
                "marketcap": float(token.get("fdv", 0)),
                "volume": float(token.get("volume", {}).get("h24", 0)),
                "num_holders": 0,  # DEX Screener doesn't provide holders
                "dev_wallet": token.get("pairCreatedBy", ""),
                "image": token.get("baseToken", {}).get("logoUrl", ""),
                "progress": 0.0
            }
            save_token(token_data)
            print(f"✅ Saved token: {token_data['name']} ({token_data['ticker']})")
        else:
            print(f"❌ Failed to fetch token data. Status code: {res.status_code}")
    except Exception as e:
        print(f"⚠️ Error during API call: {e}")

if __name__ == "__main__":
    fetch_and_save_tokens()
