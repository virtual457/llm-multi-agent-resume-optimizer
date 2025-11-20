"""
Test SSE streaming endpoint
"""
import requests
import json

url = "http://localhost:8000/api/generate/stream"

payload = {
    "username": "chandan",
    "jd_text": "We are looking for a Software Engineer with Python experience",
    "company": "TestCompany",
    "role": "Software Engineer",
    "optimize": True
}

print("Starting SSE stream test...")
print("=" * 60)

response = requests.post(url, json=payload, stream=True)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    print(response.text)
    exit(1)

# Read SSE events
for line in response.iter_lines():
    if line:
        line = line.decode('utf-8')
        if line.startswith('data: '):
            data = json.loads(line[6:])
            
            stage = data.get('stage', 'unknown')
            message = data.get('message', '')
            progress = data.get('progress', 0)
            
            print(f"[{progress:3d}%] {stage:20s} | {message}")
            
            if stage == 'complete':
                print("\n" + "=" * 60)
                print("✓ Stream completed successfully!")
                print(f"  Evaluation Score: {data['data']['scores']['evaluation']['total_score']}")
                print(f"  Factuality Score: {data['data']['scores']['factuality']['factuality_score']}")
                break
            
            if stage == 'error':
                print("\n" + "=" * 60)
                print(f"✗ Error: {data.get('error')}")
                break

print("\nTest complete!")
