# Fuzzy: API Fuzzer

Fuzzy is a versatile Python tool designed for fuzzing (testing) API endpoints using a wordlist. With the help of the `argparse` library, this tool allows users to specify the API endpoint URL and the path to a wordlist file containing potential parameters for API requests. The script then iterates through the wordlist, sending multiple GET requests to the API endpoint with each word as a parameter in the URL. The tool outputs the response data, status code, and the word used in each request.

**Features:**
- Straightforward and efficient API fuzzer.
- Fuzzes an API endpoint with a customizable wordlist.
- Provides detailed output of response data and status codes for each request.

**Installation:**
1. Clone the repository to your local machine using the following command:
   ```shell
   git clone https://github.com/Toothless5143/Fuzzy.git && cd Fuzzy
   ```

2. Install the required dependencies by executing the following command:
   ```shell
   pip install -r requirements.txt
   ```

3. Run the tool by applying the following command, providing the API endpoint URL and the desired wordlist:
   ```shell
   python3 fuzzy.py -u <API URL> -w <Wordlist file>
   ```

**License:**
This tool is open source and available under the [MIT License](/LICENSE).
