# -*- coding: utf-8 -*-
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'warprobot'


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class AuthForm(Component):
    LOGIN = '#id_Login'
    PASSWORD = '#id_Password'
    DOMAIN = '#id_Domain'
    SUBMIT = '#gogogo>input'

    def set_login(self, login):
        self.driver.find_element_by_css_selector(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_css_selector(self.PASSWORD).send_keys(pwd)

    def set_domain(self, domain):
        select = self.driver.find_element_by_css_selector(self.DOMAIN)
        Select(select).select_by_visible_text(domain)

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT).click()


class TopMenu(Component):
    EMAIL = '#PH_user-email'

    def get_email(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EMAIL).text
        )


class BaseSettings(Component):
    CAMPAIGN_NAME = '.base-setting__campaign-name__input'
    PRODUCT_TYPE = '#product-type-6043'
    PADS_TARGET = '#pad-mobile_site_feed_interface'

    def set_campaign_name(self, campaign_name):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.CAMPAIGN_NAME)
        )
        element.clear()
        element.send_keys(campaign_name)

    def set_product_type(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PRODUCT_TYPE)
        )
        element.click()

    def set_pads_targeting(self):
        element = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_element_by_css_selector(self.PADS_TARGET)
        )
        element.click()


class CreateAdd(Component):
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    URL = 'input[data-name="url"]'
    IMAGE = 'input[data-name="image"]'
    SAVE_BUTTON = '.banner-form__save-button'
    RESET_BUTTON = '.banner-form__reset'
    SUBMIT_BUTTON = ".main-button-new"

    def set_title(self, title):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TITLE)
        )
        element.send_keys(title)

    def set_text(self, text):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        )
        element.send_keys(text)

    def set_url(self, url):
        self.url.send_keys(url)

    @property
    def url(self):
        elements = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_elements_by_css_selector(self.URL)
        )
        for element in elements:
            if element.is_displayed():
                return element

    def set_image(self, image_path):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        )
        element.send_keys(image_path)

    def loading_image(self, driver):
        images = driver.find_elements_by_css_selector('.banner-preview .banner-preview__img')
        for image in images:
            if image.value_of_css_property("width") == '90px':
                return WebDriverWait(image, 30, 0.1).until(
                    lambda d: d.value_of_css_property("background-image") is not None
                )

    def wait_picture(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: self.loading_image(d)
        )

    def save(self):
        self.driver.find_element_by_css_selector(self.SAVE_BUTTON).click()

    def reset(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RESET_BUTTON)
        )
        element.click()

    def submit(self):
        self.driver.find_element_by_css_selector(self.SUBMIT_BUTTON).click()


class Navigation(Component):
    BUTTON = '.control__link_edit'

    def go_to_edit(self):
        element = WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_css_selector(self.BUTTON)
        )
        element.click()


class EditAdd(Component):
    TITLE = '.banner-preview__title'
    TEXT = '.banner-preview__text'
    BLOCK = '.added-banner__banners-wrapper'
    AGE = '.campaign-setting__value[data-node-id="restrict"]'
    WHERE = '.campaign-setting__chosen-box__item__name'

    def get_title(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BLOCK)
        )
        return block.find_element_by_css_selector(self.TITLE).text

    def get_text(self):
        block = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.BLOCK)
        )
        return block.find_element_by_css_selector(self.TEXT).text

    def get_age(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AGE).text
        )

    def get_where(self):
        where = []
        places = WebDriverWait(self.driver, 30, 0.5).until(
            lambda d: d.find_elements_by_css_selector(self.WHERE)
        )
        for place in places:
            where.append(place.text)
        return where


class CampaignData(Component):
    CAMPAIGN_NAME = '.campaign-title__name'

    def get_campaign_name(self):
        return WebDriverWait(self.driver, 30, 0.2).until(
            lambda d: d.find_element_by_css_selector(self.CAMPAIGN_NAME).text
        )


class SetTarget(Component):
    AGE_MULTIPLE_CHOICE = '.campaign-setting__value[data-node-id="restrict"]'
    AGE_6 = 'input[data-value="6+"]'
    AGE_18 = 'input[data-value="18+"]'
    RUSSIA_CHECKBOX = '#regions188 > .tree__node__input'
    USSR_CHECKBOX = '#regions100001 > .tree__node__input'
    USSR = '[data-node-id="БывшийСССР"]'
    ABHAZ_CHECKBOX = '#regions398 > .tree__node__input'
    GRUZ_CHECKBOX = '#regions29 > .tree__node__input'

    def set_age(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AGE_MULTIPLE_CHOICE)
        )
        element.click()

    def set_age_6(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AGE_6)
        )
        element.click()

    def set_age_18(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.AGE_18)
        )
        element.click()

    def click_russia_checkbox(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RUSSIA_CHECKBOX)
        )
        element.click()

    def click_ussr_checkbox(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.USSR_CHECKBOX)
        )
        element.click()

    def click_ussr(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.USSR)
        )
        element.click()

    def click_abhaz_checkbox(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ABHAZ_CHECKBOX)
        )
        element.click()

    def click_gruz_checkbox(self):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.GRUZ_CHECKBOX)
        )
        element.click()

