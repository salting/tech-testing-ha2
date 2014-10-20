# -*- coding: utf-8 -*-

import os
import unittest
import urlparse
from selenium import webdriver
from selenium.webdriver import ActionChains, DesiredCapabilities, Remote
from helper.helper_page import AuthForm, AuthPage, CreatePage, CreateAds, ThatAdvertise, CreateCompany, \
    Platform, Edit, Campaigns, Where, GetResult, AgeRestrictions
from selenium.webdriver.support.ui import WebDriverWait

class TargetTests(unittest.TestCase):

    def setUp(self):

        self.USERNAME = 'tech-testing-ha2-10@bk.ru'
        self.PASSWORD = os.environ.get('TTHA2PASSWORD', 'Pa$$w0rD-10')
        self.DOMAIN = '@bk.ru'
        self.IMAGE = os.path.abspath('img.jpg')
        self.IMAGE_SMALL = os.path.abspath('test_image_1.png')
        self.IMAGE_BIG = os.path.abspath('test_image_2.jpg')

        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(self.USERNAME)
        auth_form.set_domain(self.DOMAIN)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        create_page = CreatePage(self.driver)
        create_page.open()

    def tearDown(self):
        campaign = Campaigns(self.driver)
        campaign.open()
        delete = campaign.get_delete
        delete.click_delete()

        self.driver.quit()

    def test_platform(self):
        advertise = ThatAdvertise(self.driver)
        advertise.set_product()
    
        platform = Platform(self.driver)
        platform.set_platform()
    
        create_ads = CreateAds(self.driver)
        create_ads.set_title('test')
        create_ads.set_text('test')
        create_ads.set_image_small(self.IMAGE_SMALL)
        create_ads.set_image_big(self.IMAGE_BIG)
        create_ads.set_link('http://www.odnoklassniki.ru/event/ID')
        create_ads.add()
    
        create = CreateCompany(self.driver)
        create.click()
    
        edit = Edit(self.driver)
        edit.click_edit()
    
        platform_result = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector('.base-setting__pads-item__label').text
        )
    
        self.assertEquals('Одноклассники: мобильная версия', platform_result.encode('utf-8'))

    def test_where(self):
    
        where = Where(self.driver)
        where.click_asia()
    
        create_ads = CreateAds(self.driver)
        create_ads.set_title('test')
        create_ads.set_text('test')
        create_ads.set_image(self.IMAGE)
        create_ads.set_link('www.target.mail.ru')
        create_ads.add()
    
        create = CreateCompany(self.driver)
        create.click()
    
        edit = Edit(self.driver)
        edit.click_edit()
    
        getter_result = GetResult(self.driver)
    
        self.assertEquals(True, getter_result.get_checked_asia())

    def test_age_restrictions(self):
        test_age = '0+'

        create_ads = CreateAds(self.driver)
        create_ads.set_title('test')
        create_ads.set_text('test')
        create_ads.set_image(self.IMAGE)
        create_ads.set_link('www.target.mail.ru')
        create_ads.add()

        age_res = AgeRestrictions(self.driver)
        age_res.click_restrict()
        age_res.click_age()

        create = CreateCompany(self.driver)
        create.click()

        edit = Edit(self.driver)
        edit.click_edit()

        getter_result = GetResult(self.driver)

        self.assertEquals(test_age, getter_result.get_text_age().encode('utf-8'))