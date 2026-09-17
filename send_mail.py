
import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

CSV_FILE = "ndk_stock.csv"

MAIL_FROM = os.environ["MAIL_FROM"]
MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
MAIL_TO = os.environ["MAIL_TO"]

msg = MIMEMultipart()
msg["Subject"] = "NDK_STOCK_CSV_AUTO"
msg["From"] = MAIL_FROM
msg["To"] = MAIL_TO

# 本文
msg.attach(MIMEText("本日のNDK株価CSVを添付します。", "plain", "utf-8"))

# CSV添付
with open(CSV_FILE, "rb") as f:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(f.read())

encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename={CSV_FILE}"
)
msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(MAIL_FROM, MAIL_PASSWORD)
    smtp.send_message(msg)
