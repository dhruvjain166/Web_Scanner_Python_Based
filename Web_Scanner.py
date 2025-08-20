import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def detect_sql_injection(url):
    """Test for SQL Injection vulnerability."""
    payload = "' OR '1'='1"  # Common SQL Injection payload
    test_url = f"{url}?id={payload}"
    response = requests.get(test_url)
    if "error in your SQL syntax" in response.text.lower():
        print(f"[VULNERABLE] SQL Injection detected at {test_url}")
    else:
        print(f"[SECURE] No SQL Injection vulnerability detected at {url}")

def detect_xss(url):
    """Test for Cross-Site Scripting (XSS) vulnerability."""
    payload = "<script>alert('XSS')</script>"
    test_url = f"{url}?q={payload}"
    response = requests.get(test_url)
    if payload in response.text:
        print(f"[VULNERABLE] XSS detected at {test_url}")
    else:
        print(f"[SECURE] No XSS vulnerability detected at {url}")

def find_forms(url):
    """Extract all forms from a webpage."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("form")

def scan_website(url):
    """Scan a website for SQL Injection and XSS vulnerabilities."""
    print(f"Scanning {url} for vulnerabilities...")
    detect_sql_injection(url)
    detect_xss(url)
    
    forms = find_forms(url)
    print(f"Found {len(forms)} forms on {url}.")
    
    if forms:
        print("Manual testing recommended for form-based vulnerabilities.")

def main():
    url = input("Enter the URL to scan: ")
    scan_website(url)

if __name__ == "__main__":
    main()
