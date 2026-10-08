from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import urlsplit
from datetime import datetime, timezone
import json, time, os, threading, webbrowser

BASE=Path(__file__).resolve().parent
CACHE=BASE/"nav_cache"
CACHE.mkdir(exist_ok=True)
PORT=8505
UPSTREAM="https://api.mfapi.in/mf"
TTL=12*3600

class Handler(BaseHTTPRequestHandler):
    def send_bytes(self, content, mime="application/json", status=200, freshness=None):
        self.send_response(status)
        self.send_header("Content-Type",mime+"; charset=utf-8")
        self.send_header("Cache-Control","no-store")
        if freshness:self.send_header("X-KOTE-Data-Status",freshness)
        self.end_headers()
        self.wfile.write(content)
    def do_GET(self):
        route=urlsplit(self.path)
        if route.path in ("/","/dashboard.html"):
            return self.send_bytes((BASE/"dashboard.html").read_bytes(),"text/html")
        if route.path=="/api/health":
            return self.send_bytes(json.dumps({"status":"running","cache_files":len(list(CACHE.glob("*.json")))}).encode())
        if not route.path.startswith("/api/mf/"):
            return self.send_bytes(b'{"error":"Not found"}',status=404)
        # Accept only fixed API paths, no arbitrary proxy URLs
        tail=route.path[len("/api/mf/"):]
        if tail=="search":
            key="search_"+str(__import__("hashlib").sha256(route.query.encode()).hexdigest()[:24])
            url=UPSTREAM+"/search?"+route.query
        elif tail.isdigit() and len(tail)<12:
            key="fund_"+tail
            url=UPSTREAM+"/"+tail
        else:
            return self.send_bytes(b'{"error":"Invalid route"}',status=400)
        file=CACHE/(key+".json")
        fresh=file.exists() and time.time()-file.stat().st_mtime<TTL
        if fresh:
            return self.send_bytes(file.read_bytes(),freshness="cached")
        try:
            req=Request(url,headers={"User-Agent":"KOTE-Multi-Asset/1.0","Accept":"application/json"})
            with urlopen(req,timeout=15) as r: data=r.read()
            json.loads(data)
            tmp=file.with_suffix(".tmp")
            tmp.write_bytes(data)
            tmp.replace(file)
            return self.send_bytes(data,freshness="updated")
        except Exception as e:
            if file.exists():
                return self.send_bytes(file.read_bytes(),freshness="stale-offline")
            return self.send_bytes(json.dumps({"error":"No cached NAV available. Connect to internet and retry.","detail":str(e)}).encode(),status=503)
    def log_message(self,fmt,*args): print("%s - %s"%(self.address_string(),fmt%args))

if __name__=="__main__":
    print("KOTE Multi Asset local dashboard")
    print("Open http://localhost:%d/"%PORT)
    print("NAV data is cached in",CACHE)
    server=ThreadingHTTPServer(("127.0.0.1",PORT),Handler)
    threading.Timer(1.2,lambda:webbrowser.open("http://localhost:%d/"%PORT)).start()
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
