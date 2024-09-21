import argparse
# other imports go here
import urllib.request
import datetime
import csv
import io

def downloadData(url):
    """
    Reads data from a URL and returns the data as a string

    :param url:
    :return: the content of the URL
    """
    # read the URL
    with urllib.request.urlopen(url) as response:
        response = response.read().decode('utf-8')

    # return the data
    return response


def processData(file_content):
    csv_data = csv.reader(io.StringIO(file_content))
    image_counter = 0
    line_counter = 0

    chrome_counter = 0
    safari_counter = 0
    msie_counter = 0
    ffox_counter = 0
    for row in csv_data:
        line_counter += 1
        # process your data
        path_to_file = row[0]
        datetime_accessed = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
        browser = row[2]
        print(f"Path = {path_to_file} | Hour accessed = {datetime_accessed.hour} | Browser = {browser}")
        # Count images if path ends in .jpg, .gif or .png
        if path_to_file.endswith("jpg"):
            image_counter += 1

        # For browser count, you will need to inspect the browser field
        # Chrome, Firefox, Safari, MSIE
        if browser.find("Chrome") != -1:
            chrome_counter += 1
        

    percent_images = image_counter / line_counter * 100
    print(f"“Image requests account for {percent_images}% of all requests")

    # Print the most popular browser (compare all the browser counts)



def main(url):
    print("*********************************")
    print(f"Running main with URL = {url}...")
    print("*********************************")
    url_data = downloadData(url)
    processData(url_data)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
