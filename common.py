import time  
import random  
from datetime import datetime, timedelta  
from playwright.sync_api import sync_playwright  
  
# 定義國定假日  
HOLIDAYS = [  
    "2025-01-01",  # 元旦  
    "2025-01-27",  # 春節假期  
    "2025-01-28",  # 春節假期  
    "2025-01-29",  # 春節假期  
    "2025-01-30",  # 春節假期  
    "2025-01-31",  # 春節假期  
    "2025-02-28",  # 和平紀念日  
    "2025-04-03",  # 兒童節  
    "2025-04-04",  # 清明節  
    "2025-05-01",  # 勞動節  
    "2025-05-30",  # 端午節  
    "2025-10-06",  # 中秋節  
    "2025-10-10",  # 國慶日  
]  
  
def is_holiday(date):  
    return date.strftime("%Y-%m-%d") in HOLIDAYS  
  
def is_weekend(date):  
    return date.weekday() >= 5  # 週六是5，週日是6  
  
def login_and_check_in(page):  
    page.fill('input[placeholder="公司代碼"]', '<您的公司代碼>')  
    page.fill('input[placeholder="工號"]', '<您的工號>')  
    page.fill('input[placeholder="請輸入您的密碼"]', '<您的密碼>')  
    page.click('button:has-text("登入")')  
    page.wait_for_load_state('networkidle')  
  
def clock_in(page):  
    page.click('a[href="/ta?id=webpunch"]')  
    page.wait_for_load_state('networkidle')  
    page.click('button:has-text("上班")')  
    page.wait_for_timeout(5000)  # 5秒  
  
def clock_out(page):  
    page.click('a[href="/ta?id=webpunch"]')  
    page.wait_for_load_state('networkidle')  
    page.click('button:has-text("下班")')  
    page.wait_for_timeout(5000)  # 5秒  
