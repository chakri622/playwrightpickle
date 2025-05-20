import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect
import os
from dotenv import load_dotenv
import datetime
import time

load_dotenv()

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    ccname = os.getenv("CCNAME")
    ccid = os.getenv("CCID")
    expiry_mon = os.getenv("EXPIRY_MON")
    expiry_year = os.getenv("EXPIRY_YEAR")
    cvv = os.getenv("CVV")
    page = await context.new_page()
    await page.goto("https://www.alpharetta.ga.us/307/Tennis-Pickleball")
    await page.get_by_role("link", name="Reservations page").click()
    await page.get_by_text("NP Pickleball Court 1", exact=True).click()
    await page.get_by_role("link", name="Sign In", exact=True).click()
    await page.get_by_role("textbox", name="Email address Required").dblclick()
    await page.get_by_role("textbox", name="Email address Required").click()
    await page.get_by_role("textbox", name="Email address Required").fill(username)
    await page.get_by_role("textbox", name="Password Required").click()
    await page.get_by_role("textbox", name="Password Required").fill(password)
    await page.get_by_role("button", name="Sign in").click()
    await page.get_by_role("link", name="Reservations").click()
    await page.get_by_text("NP Pickleball Court 1", exact=True).click()
    await page.get_by_role("textbox", name="Number of attendees").click()
    await page.get_by_role("textbox", name="Number of attendees").press("ArrowRight")
    await page.get_by_role("textbox", name="Number of attendees").fill("4")
    await page.get_by_role("link", name="When?").click()
    today = datetime.date.today()
    one_week = datetime.timedelta(weeks=1)
    future_date = today + one_week

    print(future_date.strftime("%d"))
    print(future_date.strftime("%B %d %Y"))
    await page.get_by_role("gridcell", name=f"{future_date.strftime("%d")}", exact=True).locator("div").click()
    #await page.get_by_label(f"calendar {future_date.strftime("%B %d %Y")} is").get_by_text(future_date.strftime("%d")).click()
  
   
    await page.get_by_role("combobox", name="Time range start time").click()
    await page.get_by_role("combobox", name="Time range start time").fill("7:00 PM")
    time.sleep(5)
    await page.get_by_role("combobox", name="Time range end time").click()
    await page.get_by_role("combobox", name="Time range end time").dblclick()
    time.sleep(5)
    await page.get_by_role("combobox", name="Time range end time").fill("9:00 PM")
    time.sleep(5)
    #await page.get_by_label(f"calendar {future_date.strftime("%B %d %Y")} is").get_by_text(future_date.strftime("%d")).click()
    #await page.get_by_label(f"calendar {future_date.strftime("%B %d %Y")} is").get_by_text(future_date.strftime("%d")).click()
    await page.get_by_role("gridcell", name=f"{future_date.strftime("%d")}", exact=True).locator("div").click()
    await page.get_by_role("gridcell", name=f"{future_date.strftime("%d")}", exact=True).locator("div").click()
  
    await page.get_by_role("button", name="Apply").click()
    await page.get_by_role("button", name="Proceed").click()
    await page.get_by_role("textbox", name="Input Event name").click()
    await page.get_by_role("textbox", name="Input Event name").fill("pickle ball tournament")
    await page.get_by_label("Event type*").get_by_text("Please select an event type").click()
    await page.get_by_role("option", name="Pickleball Court Rental").click()
    await page.get_by_role("button", name="Add to cart").click()
    await page.get_by_role("button", name="Check out").click()
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="Name on card").click()
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="Name on card").fill(ccname)
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="Card number").click()
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="Card number").fill(ccid)
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_test_id("form-label").nth(2).click()
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_label("expiration date month").select_option(expiry_mon)
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_label("expiration date year").select_option(expiry_year)
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="CVV/CVC You can find your 3").click()
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="CVV/CVC You can find your 3").click()
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_role("textbox", name="CVV/CVC You can find your 3").fill(cvv)
    await page.locator(".an-grid").first.click()
    time.sleep(5)
    await page.locator("iframe[name=\"primaryPCIPaymentIframe\"]").content_frame.get_by_text("Name on card*Card number*").click()
    await page.get_by_role("button", name="Pay", exact=True).click()
    time.sleep(5)

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
