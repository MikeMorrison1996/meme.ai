import asyncio
import websockets
import json
import requests
import base64
import os
import hashlib

from solders.pubkey import Pubkey

SOLANA_WS = "wss://api.mainnet-beta.solana.com/"
SOLANA_RPC = "https://api.mainnet-beta.solana.com/"
METADATA_PROGRAM_ID = "metaqbxxUerdq28cj1RbAWkYQm3ybzjb6a8bt518x1s"
DATA_PATH = "clean_token_data.json"
HEADERS = { "Content-Type": "application/json" }

def find_metadata_pda(mint):
    seeds = [
        b"metadata",
        bytes(Pubkey.from_string(METADATA_PROGRAM_ID)),
        bytes(Pubkey.from_string(mint))
    ]
    for nonce in range(255, 0, -1):
        try:
            seeds_with_nonce = seeds + [bytes([nonce])]
            hash_bytes = hashlib.sha256(b''.join(seeds_with_nonce)).digest()
            pda = Pubkey.from_bytes(hash_bytes[:32])
            return pda, nonce
        except:
            continue
    raise Exception("Could not find PDA")

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

def fetch_token_metadata(mint_address):
    metadata_pda, _ = find_metadata_pda(mint_address)
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getAccountInfo",
        "params": [str(metadata_pda), {"encoding": "base64"}]
    }
    res = requests.post(SOLANA_RPC, headers=HEADERS, json=payload)
    if res.ok:
        try:
            data = res.json()['result']['value']['data'][0]
            raw_bytes = base64.b64decode(data)
            name = raw_bytes[1:33].decode('utf-8').strip('\x00')
            symbol = raw_bytes[33:43].decode('utf-8').strip('\x00')
            uri = raw_bytes[115:247].decode('utf-8').strip('\x00')
            meta = requests.get(uri).json()
            image_url = meta.get("image", "")
            return {
                "mint": mint_address,
                "name": name,
                "symbol": symbol,
                "uri": uri,
                "image": image_url
            }
        except Exception as e:
            print(f"❌ Failed to parse metadata for {mint_address}: {e}")
    return None

def extract_mint_from_log(logs):
    for log in logs:
        if "Program log: Mint:" in log:
            return log.split("Program log: Mint:")[-1].strip()
    return None

async def listen_new_tokens():
    print("📡 Connecting to Solana WebSocket...")
    async with websockets.connect(SOLANA_WS) as websocket:
        print("✅ Connected. Listening for token creation events...")

        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "logsSubscribe",
            "params": [
                {"mentions": ["TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA"]},
                {"commitment": "confirmed"}
            ]
        }

        await websocket.send(json.dumps(payload))

        while True:
            response = await websocket.recv()
            data = json.loads(response)

            if 'method' in data and data['method'] == 'logsNotification':
                logs = data['params']['result']['value']['logs']
                sig = data['params']['result']['value']['signature']
                for log in logs:
                    if "initializeMint" in log:
                        print(f"🧠 New Mint Detected! Signature: {sig}")
                        mint_address = extract_mint_from_log(logs)
                        if mint_address:
                            meta = fetch_token_metadata(mint_address)
                            if meta:
                                print("🎉 Token Metadata:")
                                for k, v in meta.items():
                                    print(f"  {k}: {v}")
                                save_token(meta)
                                print("📥 Token saved to clean_token_data.json ✅\n")

if __name__ == "__main__":
    try:
        asyncio.run(listen_new_tokens())
    except KeyboardInterrupt:
        print("👋 Exiting Solana token listener.")
