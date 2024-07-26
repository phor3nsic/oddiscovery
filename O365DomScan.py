import requests
import sys

def get_domains(domain):
    url = "https://autodiscover-s.outlook.com:443/autodiscover/autodiscover.svc"
    headers = {
        "User-Agent": "AutodiscoverClient", 
        "Accept-Encoding": "gzip, deflate, br", 
        "Accept": "*/*", 
        "Connection": "keep-alive", 
        "Content-Type": "text/xml; charset=utf-8", 
        "Soapaction": "\"http://schemas.microsoft.com/exchange/2010/Autodiscover/Autodiscover/GetFederationInformation\""
        }
    data = f"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n    <soap:Envelope xmlns:exm=\"http://schemas.microsoft.com/exchange/services/2006/messages\" xmlns:ext=\"http://schemas.microsoft.com/exchange/services/2006/types\" xmlns:a=\"http://www.w3.org/2005/08/addressing\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\">\n        <soap:Header>\n            <a:Action soap:mustUnderstand=\"1\">http://schemas.microsoft.com/exchange/2010/Autodiscover/Autodiscover/GetFederationInformation</a:Action>\n            <a:To soap:mustUnderstand=\"1\">https://autodiscover-s.outlook.com/autodiscover/autodiscover.svc</a:To>\n            <a:ReplyTo>\n                <a:Address>http://www.w3.org/2005/08/addressing/anonymous</a:Address>\n            </a:ReplyTo>\n        </soap:Header>\n        <soap:Body>\n            <GetFederationInformationRequestMessage xmlns=\"http://schemas.microsoft.com/exchange/2010/Autodiscover\">\n                <Request>\n                    <Domain>{domain}</Domain>\n                </Request>\n            </GetFederationInformationRequestMessage>\n        </soap:Body>\n    </soap:Envelope>"
    r = requests.post(url, headers=headers, data=data)
    if "<Domains>" in r.text:
        domains = r.text.split("<Domains>")[1].split("</Domains>")[0].split("<Domain>")
        for domain in domains:
            domain = domain.replace("</Domain>","")
            if "onmicrosoft.com" not in domain:
                print(domain)
    else:
        print(domain)

if len(sys.argv) < 2:
    print("Try python3 "+sys.argv[0] + "domain.tdl")
    print("To get list domains related to a given domain within the Office 365 environment.")
    sys.exit()
else:
    get_domains(sys.argv[1])