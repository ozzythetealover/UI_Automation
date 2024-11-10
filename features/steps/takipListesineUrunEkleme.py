import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'homepage e giriş yapılır')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://akakce.com")
    time.sleep(2)


@when(u'kullanıcı bir ürünü aratır')
def steps_impl(context):
    context.driver.find_element(By.ID, "q").send_keys("koltuk")
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//button[@title='Ara']").click()
    time.sleep(2)


@when(u'kullanıcı gelen ürün listesinden ürün seçimi yapar ve ürüne git seçeneğine tıklar')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//a//span[@class='bt_v8']").click()
    time.sleep(2)

@then(u'kullanıcı ürünü takip listesine ekler')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0, 300)")
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//*[text()='Takip Et']").click()
    time.sleep(3)

