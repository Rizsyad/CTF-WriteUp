import requests

def init():
    r = requests
    return Request(r), r

class Request:
    def __init__(self, r: requests):
        self.r = r

    def redirect(self, url):
        r = self.r

        response = r.get(url).text
        return self.getFlag(response)

    def getFlag(self, response):
        r = self.r

    def exploit(self):
        r = self.r
        self.redirect()

if __name__ == "__main__":
    x, y = init()
    x.exploit()