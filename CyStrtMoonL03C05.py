

import re

dString ="""
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>"""

dPattern = "class='(.*)'"
ddata = re.findall(dPattern, dString)

for i in range(len(ddata)):
    print(ddata[i])


