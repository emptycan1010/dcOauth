import requests

# Dcinside Oauth using gallog
class dcauth:
    def __init__(self, id: str, pw: str):
        # Login
        self.id = id
        self.pw = pw
        self.s = requests.Session()
        self.s.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": "https://sign.dcinside.com/login?s_url=https://gallog.dcinside.com/"
                + id,
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://gallog.dcinside.com",
                "Connection": "keep-alive",
                "Sec-Fetch-Mode": "naviagate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "DNT": "1",
                "HOST": "sign.dcinside.com",
            }
        )
        self.s.get("https://sign.dcinside.com/login?s_url=https://www.dcinside.com/")
        res = self.s.post(
            "https://sign.dcinside.com/login/member_check",
            {
                "user_id": self.id,
                "pw": self.pw,
                "s_url": "//www.dcinside.com/",
                "ssl": "Y",
            },
        )

    def sendM(self, id: str, code: str):
        self.s.get("https://gallog.dcinside.com/" + id + "/guestbook")
        self.s.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
                "Accept": "*/*",
                "Referer": f"https://gallog.dcinside.com/{id}/guestbook",
                "Origin": "https://gallog.dcinside.com",
                "Host": "gallog.dcinside.com",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3",
                "Connection": "keep-alive",
                "sec-gpc": "1",
                "sec-ch-ua-mobile": "?0",
                "Sec-Fetch-Mode": "cors",
                "Content-Length": "0",
                # "Accept": "application/json, text/javascript, */*; q=0.01",
                "DNT": "1",
            }
        )
        res = self.s.post(
            f"https://gallog.dcinside.com/{id}/ajax/guestbook_ajax/write",
            data={
                "is_secret": "1",
                "memo": code,
            },
        )
        print(res.text)
        if res.json()["result"] == "success":
            return True
        else:
            return False
