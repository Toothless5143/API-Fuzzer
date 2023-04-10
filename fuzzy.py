import argparse
import requests
import sys

parser = argparse.ArgumentParser(description='Fuzz an API endpoint with a wordlist')
parser.add_argument('-u', '--url', help='API endpoint URL', required=True)
parser.add_argument('-w', '--wordlist', help='Path to wordlist file', required=True)
args = parser.parse_args()

def loop():
    with open(args.wordlist, 'r') as f:
        for word in f:
            word = word.strip()
            res = requests.get(url=f"{args.url}/{word}")
            if res.status_code == 404:
                continue
            else:
                data = res.json()
                print(data)
                print(res.status_code)
                print(word)

if __name__ == '__main__':
    loop()
