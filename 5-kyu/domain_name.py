# Task: Extract the domain name from a URL
# Link: https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
# Level: 5 kyu

def domain_name(url):
    clean_url = url.replace("https://", "").replace("http://", "").replace("www.", "")

    return clean_url.split(".")[0]

domain = "http://google.com"
print(domain_name(domain))