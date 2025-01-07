import time  
import random  
import json
from datetime import datetime, timedelta  
from playwright.sync_api import sync_playwright  

# read config.json
with open("./config.json", "r") as jsonfile:
    configs = json.load(jsonfile)

def is_holiday(date):  
    return date.strftime("%Y-%m-%d") in configs['HOLIDAYS']

def is_weekend(date):  
    return date.weekday() >= 5  # 週六是5，週日是6  
  
def login_and_check_in(page):  
    page.fill('input[placeholder="公司代碼"]', configs['company_code'])  
    page.fill('input[placeholder="工號"]', configs['staff_id'])  
    page.fill('input[placeholder="請輸入您的密碼"]', configs['password'])  
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
