# Authentication with python...
import http.server
import cgi

form = cgi.FieldStorage

# This is basically useless at the moment....
if form.getvalue('username') == "Jesse" & form.getvalue('password') == "123456":
    print("<h1>Authorized!</h1>")
else:
    print("<h1>FAILED</h1>")
