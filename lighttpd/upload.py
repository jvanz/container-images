#!/usr/bin/python3

import cgi
import cgitb

cgitb.enable(display=0, logdir="/var/log/lighttpd")

form = cgi.FieldStorage()
filefield = form["file"]
msg = "Failed to upload file!"
if filefield.filename:
    with open(f"/tmp/{filefield.filename}", "w+b") as f:
        f.write(filefield.file.read())
        msg = "File uploaded!"
else:
    msg = f"Cannot find file field. {filefield.name} = {filefield.filename}"

print("Content-Type: text/html")
print()
print("<html>")
print("<body>")
print(f"<H1>{msg}</H1>")
print("</body>")
print("</html>")

