import asyncio
import re
import time
import pymongo
import requests
from pyppeteer.launcher import launch, executablePath
from TaobaoCookies.login_func import mouse_slide, input_time_random
from TaobaoCookies.exe_js import js1, js3, js4, js5
from TaobaoCookies.config import MONGO_TABLE,MONGO_DB,MONGO_URL

async def main(username, pwd, url):
    browser = await launch({'executablePath':"C:\\Users\\Administrator\\AppData\\Local\\pyppeteer\\pyppeteer\\chrome-win\\chrome.exe",'headless': False, 'args': ['--no-sandbox'], })
    page = await browser.newPage()
    await page.setUserAgent(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

    await page.goto(url)
    await page.evaluate(js1)
    await page.evaluate(js3)
    await page.evaluate(js4)
    await page.evaluate(js5)

    await page.click('#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')
    page.mouse
    time.sleep(2)

    await page.type('.J_UserName', username, {'delay': input_time_random() - 50})
    await page.type('#J_StandardPwd input', pwd, {'delay': input_time_random()})
    await page.screenshot({'path': './headless-test-result.png'})
    time.sleep(2)

    slider = await page.Jeval('#nocaptcha', 'node => node.style')  # 是否有滑块

    if slider:
        print('出现滑块情况判定')
        await page.screenshot({'path': './headless-login-slide.png'})
        flag = await mouse_slide(page=page)
        if flag:
            await get_cookie(page)

    else:
        await page.keyboard.press('Enter')
        await page.waitFor(20)
        await page.waitForNavigation()
        try:
            global error
            error = await page.Jeval('.error', 'node => node.textContent')
        except Exception as e:
            error = None
        finally:
            if error:
                print('确保账户安全重新入输入')
                # 程序退出。
                loop.close()
            else:
                print(page.url)
                await get_cookie(page)

def save_to_mongo(content):
    client = pymongo.MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    db[MONGO_TABLE].insert_one(content)
    print('存储成功')
    return True

# 获取登录后cookie
async def get_cookie(page):
    cookies_list = await page.cookies()
    cookie = {}
    for item in cookies_list:
        cookie[item['name']] = item['value']
    save_to_mongo(cookie)
    return cookie


if __name__ == '__main__':
    username = '18801463693'
    pwd = 'lxh6338231'
    url = 'https://login.taobao.com/member/login.jhtml'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(username, pwd, url))