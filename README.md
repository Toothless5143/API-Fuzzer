# Fuzzy:
It is a simple API fuzzer that fuzzes (tests) an API endpoint with a wordlist. It uses the `argparse` library to parse command-line arguments for the API endpoint URL and the path to the wordlist file containing words to be used as parameters in the API request. The script then sends multiple GET requests to the API endpoint, using each word from the wordlist as a parameter in the URL, and prints the response data and status code for each request.

### Installation:
Download all the required files and libraries you need to run the tool: <br>
```shell 
git clone https://github.com/Toothless5143/Fuzzy.git && cd Fuzzy
pip install -r requirements.txt
```

In order to run the tool apply this command:
```shell
python3 fuzzy.py -u <API URL> -w <Desired wordlist>
```

### License:
This tool is open source and available under the [MIT License.](/LICENSE)
