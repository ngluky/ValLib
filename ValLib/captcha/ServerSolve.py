import asyncio
import json
import os
import webbrowser
from importlib_resources import files
f = files("ValLib.captcha.assets")


class ServerCaptcha:
    def __init__(self, rqdata: str, site_key: str):
        self.rqdata = rqdata
        self.site_key = site_key
        self.server = None
        self.token = None
        self.stop_ = False

    @staticmethod
    async def read_all(r: asyncio.StreamReader):
        output = ''

        while recv := await r.read(1024):
            output += recv.decode("utf8")

            if len(recv) < 1024:
                break

        return output

    @staticmethod
    def parse_req(req: str):
        line_iter = iter(req.rstrip().splitlines())

        # 1st line is head, all other can just be put into dict
        method, dir_, http_ver = next(line_iter).split()

        req_dict = {
            'Method': method,
            'Directory': "" if dir_ == "/" else dir_,
            'HTTP': http_ver
        }

        for line in line_iter:
            if ':' in line:
                key, val = line.split(": ")
            else:
                key = "Body"
                val = line
            req_dict[key] = val

        return req_dict

    def resp_html_file(self, req_dict, path):
        file = f / "captcha.html"
        text = file.read_text()
        text = text.replace('SITE_KEY', self.site_key)

        resp = f"{req_dict['HTTP']} 200 OK\r\n" \
               f"Content-Type: text/html\r\n" \
               f"Content-Length: {len(text.encode('utf8'))}\r\n" \
               f"Connection: close\r\n\r\n" \
               f"{text}"

        return resp

    @staticmethod
    def resp_send_data(req_dict, data):
        text = ''
        if isinstance(data, str):
            text = data
        elif isinstance(data, dict) or isinstance(data, list) or isinstance(data, tuple):
            text = json.dumps(data)
        else:
            text = str(data)

        resp = f"{req_dict['HTTP']} 200 OK\r\n" \
               f"Content-Type: text/html\r\n" \
               f"Content-Length: {len(text.encode('utf8'))}\r\n" \
               f"Connection: close\r\n\r\n" \
               f"{text}"

        return resp

    def create_resp(self, req_dict: dict):
        dir_ = req_dict["Directory"]
        method = req_dict['Method']
        if method == "GET":
            if dir_ == "":
                return self.resp_html_file(req_dict, r"captcha.html")

            elif dir_ == "/v1/hcaptcha/rqdata":
                return self.resp_send_data(req_dict, self.rqdata)

        elif method == "POST":
            if dir_ == "/v1/hcaptcha/response":
                if req_dict.get('Body', None):
                    self.token = req_dict["Body"]
                    self.stop_ = True
                return f"{req_dict['HTTP']} 200 OK\r\nConnection: close\r\n\r\n"
        return f"{req_dict['HTTP']} 405 Method Not Allowed\r\nConnection: close\r\n\r\n"

    async def tcp_handler(self, r: asyncio.StreamReader, w: asyncio.StreamWriter):

        parsed = self.parse_req(await self.read_all(r))

        resp = self.create_resp(parsed)

        w.write(resp.encode("utf8"))
        await w.drain()
        w.close()
        if self.stop_:
            self.server.close()

    async def server_start(self):
        self.server = await asyncio.start_server(self.tcp_handler, '127.0.0.1', 80)

        print("captcha server stated at http://localhost:80")
        webbrowser.open("http://localhost:80", new=2)
        async with self.server:
            try:
                await self.server.serve_forever()
            except asyncio.CancelledError:
                pass

            print("ok")
            await self.server.wait_closed()
            print('ok')

    def stop(self):
        self.server.close()


if __name__ == "__main__":
    server = ServerCaptcha('', '')
    asyncio.run(server.server_start())
