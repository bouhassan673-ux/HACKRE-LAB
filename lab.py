
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs
import html

class Lab(BaseHTTPRequestHandler):
    def page(self, content):
        body = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>HACKRE LAB</title>
<style>
body {{
  background: #050505;
  color: #00ff66;
  font-family: monospace;
  text-align: center;
  padding: 30px 12px;
}}
.panel {{
  max-width: 500px;
  margin: 30px auto;
  padding: 24px;
  border: 1px solid #00ff66;
  border-radius: 12px;
  box-shadow: 0 0 15px #003b19;
}}
input, button, .back {{
  padding: 12px;
  margin: 8px;
  border-radius: 6px;
}}
input {{
  background: #111;
  color: white;
  border: 1px solid #00ff66;
}}
button, .back {{
  background: #00ff66;
  color: black;
  border: 0;
  cursor: pointer;
  text-decoration: none;
  display: inline-block;
}}

/* HACKRE CYBER THEME */
:root {{
  color-scheme: dark;
}}
body {{
  background:
    radial-gradient(ellipse at top, #082417 0%, #050807 48%, #020303 100%);
  color: #00ff88;
  font-family: monospace;
  min-height: 100vh;
  position: relative;
}}
body::before {{
  content: "";
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 0;
  background: repeating-linear-gradient(
    to bottom,
    transparent 0px,
    transparent 3px,
    rgba(0, 255, 100, 0.035) 4px
  );
}}
.panel {{
  position: relative;
  z-index: 1;
  max-width: 540px;
  margin: 30px auto;
  padding: 26px 20px;
  background: rgba(3, 12, 8, 0.94);
  border: 1px solid #00ff66;
  border-radius: 12px;
  box-shadow: 0 0 12px #00ff6640, inset 0 0 22px #00ff660b;
}}
h1 {{
  color: #00ff88;
  letter-spacing: 3px;
  text-shadow: 0 0 8px #00ff66, 0 0 22px #00aa55;
}}
h2 {{
  color: #8affbd;
  text-shadow: 0 0 8px #00ff6640;
}}
input, button, .back {{
  font-family: inherit;
  border-radius: 6px;
}}
input {{
  background: #07110b;
  color: #fff;
  border: 1px solid #00aa55;
}}
button, .back {{
  background: #00ff66;
  color: #001b0a;
  font-weight: bold;
  box-shadow: 0 0 10px #00ff6630;
}}
button:hover, .back:hover {{
  background: #aaffcc;
  box-shadow: 0 0 16px #00ff66a0;
}}
a {{
  color: #75ffad;
}}


.home-form, .home-actions {{
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 100%;
  max-width: 360px;
  margin: 18px auto;
}}
.home-form input, .home-form button, .home-actions .back {{
  box-sizing: border-box;
  width: 100%;
  min-height: 48px;
  margin: 0;
  font-size: 16px;
}}
.home-actions .back {{
  display: flex;
  align-items: center;
  justify-content: center;
}}
.note {{
  font-size: 13px;
  line-height: 1.8;
  color: #8affbd;
}}
@media (max-width: 480px) {{
  body {{ padding: 12px 10px; }}
  .panel {{
    width: auto;
    margin: 16px auto;
    padding: 22px 16px;
  }}
  h1 {{ font-size: 26px; letter-spacing: 2px; }}
}}

</style>
</head>
<body>
<div class="panel">
<h1>HACKRE LAB</h1>
<p>مختبر الأمن السيبراني المحلي</p>
{content}
</div>
</body>
</html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        url = urlparse(self.path)

        if url.path == "/":
            self.page("""
<h2>مرحبًا بك في المختبر</h2>
<p>بيئة محلية للتعلّم وتجربة أساسيات الأمن السيبراني.</p>
<form action="/greet" class="home-form">
<input name="name" placeholder="اكتب اسمًا تجريبيًا" required>
<button type="submit">عرض الترحيب</button>
</form>
<div class="home-actions">
<a class="back" href="/security">فحص الحماية</a>
<a class="back" href="/about">معلومات المختبر</a>
<a class="back" href="/tools">الأدوات السيبرانية</a>
</div>
<p class="note">استخدم الأدوات على أنظمتك أو بإذن صريح فقط.</p>
""")
        elif url.path == "/network":
            import socket
            ip = "غير متاح"
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                sock.connect(("192.0.2.1", 80))
                ip = sock.getsockname()[0]
            except OSError:
                pass
            finally:
                sock.close()
            self.page(f"""
<h2>معلومات الشبكة المحلية</h2>
<p>عنوان IP المحلي: {html.escape(ip)}</p>
<p class="note">هذه معلومة عن مسار الشبكة في الهاتف، وليست فحصًا للأجهزة الأخرى.</p>
<a class="back" href="/tools">رجوع للأدوات</a>
<a class="back" href="/">الرئيسية</a>
""")
        elif url.path == "/tools":
            self.page("""
<h2>الأدوات السيبرانية</h2>
<p>مرحبًا بك في قسم الأدوات التعليمية.</p>
<div class="home-actions">
<a class="back" href="/security">فحص رؤوس الحماية</a>
<a class="back" href="/about">معلومات المختبر</a>

<a class="back" href="/network">معلومات الشبكة المحلية</a>
</div>
<p class="note">استخدم هذه الأدوات على أجهزتك أو بإذن صريح فقط.</p>
<a class="back" href="/">رجوع للرئيسية</a>
""")
        elif url.path == "/about":
            self.page("""
<h2>معلومات المختبر</h2>
<p>HACKRE LAB — مختبر محلي للتعلّم.</p>
<p>يعرض هذا المشروع واجهة تعليمية وفحصًا لبعض رؤوس الحماية HTTP.</p>
<p>عنوان التشغيل المحلي: 127.0.0.1:8080</p>
<a class="back" href="/">رجوع للرئيسية</a>
""")
        elif url.path == "/greet":
            name = html.escape(parse_qs(url.query).get("name", ["زائر"])[0])
            self.page(f"""
<h2>أهلًا {name}</h2>
<a class="back" href="/">رجوع للرئيسية</a>
""")
        elif url.path == "/security":
            import http.client
            expected = {
                "x-content-type-options": "nosniff",
                "x-frame-options": "DENY",
                "referrer-policy": "no-referrer",
                "cache-control": "no-store",
            }
            results = []
            try:
                conn = http.client.HTTPConnection("127.0.0.1", PORT, timeout=3)
                conn.request("GET", "/")
                response = conn.getresponse()
                headers = {k.lower(): v for k, v in response.getheaders()}
                response.read()
                conn.close()
                for key, value in expected.items():
                    actual = headers.get(key, "غير موجود")
                    status = "PASS" if actual.lower() == value.lower() else "FAIL"
                    results.append(
                        f"<p><b>{status}</b> — {key}: {actual}</p>"
                    )
            except Exception as e:
                results.append(f"<p><b>FAIL</b> — {e}</p>")

            self.page("""
<h2>لوحة فحص الحماية</h2>
<p>نتائج فحص استجابة الخادم الفعلية:</p>
<div style="text-align:right;overflow-wrap:anywhere">
""" + "".join(results) + """
</div>
<form action="/security" method="get">
<button type="submit">▶ أعد فحص الحماية</button>
</form>
<a class="back" href="/">رجوع للرئيسية</a>
""")
        else:
            self.send_error(404)

import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8080"))
print(f"HACKRE LAB listening on {HOST}:{PORT}")
ThreadingHTTPServer((HOST, PORT), Lab).serve_forever()

