import json


path = "data/evalset.jsonl"


with open(path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        try:
            json.loads(line)
            print(f"line {i}: OK")
        except Exception as e:
            print(f"line {i}: ERROR")
            print(e)
