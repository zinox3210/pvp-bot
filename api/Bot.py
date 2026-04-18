from http.server import BaseHTTPRequestHandler
import requests
from bs4 import BeautifulSoup
import json

# --- ضع بياناتك هنا ---
TOKEN = "8751273971:AAFPINj ru7qt7F9B0Cuq6Pid
D4 c9wMFqEA8"
CHAT_ID = "8665814266"

def get_exchange_rates():
    # دالة بسيطة لسحب البيانات من الموقع
    try:
        url = "https://www.masrfi.net/"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # هنا البوت سيسحب عنوان الموقع كبداية للتجربة
        title = soup.title.string if soup.title else "موقع مصرفي"
        return f"تم فحص الموقع بنجاح: {title}\nلا توجد تحديثات جديدة حالياً."
    except Exception as e:
        return f"حدث خطأ أثناء السحب: {str(e)}"

def send_telegram_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text})

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # هذه الدالة ستعمل عندما يزور Vercel الرابط
        data = get_exchange_rates()
        send_telegram_msg(data)
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write("Bot is running... Message sent to Telegram!".encode())


