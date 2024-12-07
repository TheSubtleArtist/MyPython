"""
Briefing L07 C05
Alien Email
Breakthrough! We've discovered that the aliens have an insider back on Earth, and they've been contacting each other by... email?!
We've managed to get hold of an email between the insider and Zultron, who we think might be the alien leader, with details about attack timings. 
We want to send another email with something different to try and confuse them.
Write a script that will connect to an SMTP server to send an email. 
Use the SMTP server at "127.0.0.1", port 1025, with a from address of bob-roswell-1947@gmail.com and a to address of zultron@thebigeye.com.
"""

import smtplib


from_address ='bob-roswell_1947@gmail.com'
to_address = 'zultron@thebigeye.com'
smtp_server = '127.0.0.1'
port = '1025'
message = """
From: Bob Roswell <bob-roswell_1947@gmail.com>
To: Zultron <zultron@thebigeye.com>
Subject: The Time

The Time is Now!
"""

try:
    s = smtplib.SMTP(smtp_server, port)
    s.sendmail(from_address, to_address, message)
    print("Success")

except SMTPException:
    print("Error")
flag = s.quit()
print(flag)
