# Shared via Compiler App https://g633x.app.goo.gl/TPlw
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())