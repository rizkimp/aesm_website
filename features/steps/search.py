import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@then(u'click icon search')
def step_impl(context):
    context.page.click(locator.icon_search)
    time.sleep(3)
    context.page.click(f'#{locator.button_accept}')
    time.sleep(3)
    context.page.click(locator.icon_search)
    time.sleep(3)

@then(u'enter keyword')
def step_impl(context):
    context.page.fill(locator.input_search,'anglo')
    time.sleep(3)

@when(u'click button search')
def step_impl(context):
    context.page.click(locator.button_search)
    time.sleep(3)

@then(u'there is search result')
def step_impl(context):
    context.page.locator(f'#{locator.search_result}')