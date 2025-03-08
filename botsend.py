import requests
import time

# Telegram Bot Token & Chat ID
BOT_TOKEN = "7369624909:AAHvl9GQG8I2ImVnI-fvCX4483zxCpc72xI"
CHAT_ID = "-1001513208230"
MESSAGE = "<a href='https://t.me/blueskybd'>আমাদের চ্যানেল</a>"  # HTML ফরম্যাটে লিংক

# কয়বার মেসেজ পাঠাবে
REPEAT_COUNT = 100
DELAY = 1  # প্রতিটি মেসেজের মধ্যে কত সেকেন্ড বিরতি থাকবে

def send_message():
    """টেলিগ্রামে বার্তা পাঠানোর ফাংশন"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    for i in range(REPEAT_COUNT):
        payload = {
            "chat_id": CHAT_ID,
            "text": MESSAGE,
            "parse_mode": "HTML"  # HTML ফরম্যাট সাপোর্টের জন্য
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            print(f"✅ মেসেজ সফলভাবে পাঠানো হয়েছে ({i+1}/{REPEAT_COUNT})")
        else:
            print(f"❌ মেসেজ পাঠানো ব্যর্থ! ({i+1}/{REPEAT_COUNT}) Error:", response.json())

        time.sleep(DELAY)  # প্রতিটি মেসেজের মধ্যে বিরতি

# ফাংশন কল করা হবে
send_message()
