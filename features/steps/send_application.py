import os
import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@then(u'click button careers')
def step_impl(context):
    context.page.click(locator.button_carrer)
    time.sleep(1)

@then(u'enter first name cv')
def step_impl(context):
    context.page.fill(f'#{locator.input_first_name_cv}','test')
    time.sleep(3)
    #context.page.click(f'#{locator.button_accept}')
    time.sleep(3)

@then(u'enter last name cv')
def step_impl(context):
    context.page.fill(f'#{locator.input_last_name_cv}','test')

@then(u'enter email cv')
def step_impl(context):
    context.page.fill(f'#{locator.input_email_cv}','test@gmail.com')

@then(u'upload cv')
def step_impl(context):
    context.page.set_input_files(f'#{locator.upload_cv}','../features/steps/assets/test.pdf')

@then(u'select job type')
def step_impl(context):
    context.page.select_option(f'#{locator.select_job}',index=1)

@then(u'enter job position')
def step_impl(context):
    context.page.fill(f'#{locator.input_job_position}','test')

@then(u'enter remarks')
def step_impl(context):
    context.page.fill(f'#{locator.input_remarks}','test')

@when(u'click button send application')
def step_impl(context):
    context.page.click(locator.button_send_application)

@then(u'success send appication')
def step_impl(context):
    pass
