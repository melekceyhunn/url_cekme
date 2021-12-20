import requests
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33"}
response = requests.get("https://www.usom.gov.tr/url-list.txt", headers=header)

with open("usom.txt", "w") as dosya:
    dosya.write(str(response.content))
