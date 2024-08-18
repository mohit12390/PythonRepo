import smtplib

hostname = 'smtp.gmail.com'
email = 'mohit.gangil2012@gmail.com'
password = 'fztdvofpwkuorzef'

with smtplib.SMTP(host=hostname) as connection:
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs=email,
        msg=f"Subject: Test Python Email\n\n  This is test email"


    )