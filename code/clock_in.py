import time  
import random  
from datetime import datetime, timedelta  
from playwright.sync_api import sync_playwright  
from common import is_weekend, is_holiday, login_and_check_in, clock_in  
  
def run(playwright):  
    now = datetime.now()  
      
    if is_weekend(now) or is_holiday(now):  
        print("今天是週末或國定假日，不打卡")  
        return  
  
    # 設定上班時間範圍  
    start_time = now.replace(hour=9, minute=00, second=0, microsecond=0)  
    end_time = now.replace(hour=9, minute=30, second=0, microsecond=0)  
      
    if now > end_time:  
        print("已經過了上班打卡時間，不打卡")  
        return  
  
    random_seconds = random.randint(0, int((end_time - start_time).total_seconds()))  
    random_time = start_time + timedelta(seconds=random_seconds)  
    time_to_wait = (random_time - now).total_seconds()  
    print(f"等待 {time_to_wait} 秒後打上班卡")  
    time.sleep(time_to_wait)  
  
    browser = playwright.chromium.launch(headless=False)  
    page = browser.new_page()  
    page.goto("https://asiaauth.mayohr.com/HRM/Account/Login?original_target=https://apollo.mayohr.com/tube&lang=zh-tw&utm_source=google&utm_medium=cpc&utm_campaign=pmax%E6%89%93%E5%8D%A1%E7%B3%BB%E7%B5%B1%EF%BC%86utm_content=&utm_term=&gad_source=1&gclid=CjwKCAiAm-67BhBlEiwAEVftNmHCa7tTiFiOgcLJKk63cGj1O7vNZgwFzLMzSlaHGv720kuZrEEpMRoCuKoQAvD_BwE")  
  
    try:  
        login_and_check_in(page)  
        clock_in(page)  
        print("上班打卡成功")  
    except Exception as e:  
        print(f"上班打卡失敗: {e}")  
    finally:  
        browser.close()  
  
with sync_playwright() as playwright:  
    run(playwright)  
