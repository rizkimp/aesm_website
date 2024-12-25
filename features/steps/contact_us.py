import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'visit aesmwebsite')
def step_impl(context):
    context.page.goto(locator.dev_url)
    time.sleep(3)

@then(u'click button contact us')
def step_impl(context):
    context.page.click(locator.button_contact_us)
    time.sleep(3)
    context.page.click(f'#{locator.button_accept}')
    time.sleep(3)

@then(u'enter first name')
def step_impl(context):
    context.page.fill(f'#{locator.input_first_name}','test')

@then(u'enter last name')
def step_impl(context):
    context.page.fill(f'#{locator.input_last_name}','test')

@then(u'enter email')
def step_impl(context):
    context.page.fill(f'#{locator.input_email}','test@gmail.com')

@then(u'enter company name')
def step_impl(context):
    context.page.fill(f'#{locator.input_company_name}','test')

@then(u'enter job title')
def step_impl(context):
    context.page.fill(f'#{locator.input_job_title}','test')

@then(u'enter country')
def step_impl(context):
    context.page.fill(f'#{locator.input_country}','test')

@then(u'enter enquiry')
def step_impl(context):
    context.page.select_option(f'#{locator.input_nature_inquiry}',index=1)

@then(u'enter message')
def step_impl(context):
    context.page.fill(f'#{locator.input_message}','test')

@then(u'select checkbox')
def step_impl(context):
    context.page.click(f'#{locator.input_checkbox}')

@when(u'click button submit')
def step_impl(context):
    #button submit can not be clicked
    #context.page.click(locator.button_submit)
    pass

@then(u'success contact us')
def step_impl(context):
    pass   