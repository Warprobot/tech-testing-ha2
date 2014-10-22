# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from tests.helpers.constants import *
from tests.helpers.pages import *


class Test(unittest.TestCase):

    def setUp(self):
        """
        Install required constants and env vars. Preparing for testing
        """

        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def login(self):
        """
        helper login function
        """
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_domain(DOMAIN)
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

    def pre_creating(self, create_page):
        """
        helper. before creating
        """
        create_page.base_settings.set_product_type()
        create_page.base_settings.set_campaign_name(CAMPAIGN_NAME)
        create_page.base_settings.set_pads_targeting()
        create_page.create_advert.set_title(TITLE)
        create_page.create_advert.set_text(TEXT)
        create_page.create_advert.set_url(URL)
        create_page.create_advert.set_image(os.path.abspath(IMAGE_NAME))
        create_page.create_advert.wait_picture()
        create_page.create_advert.save()

    def test_login(self):
        """
        Testing login
        """
        self.login()
        create_page = CreateAdsPage(self.driver)
        create_page.open()
        email = create_page.top_menu.get_email()

        self.assertEqual(USERNAME, email)

    def test_simple_ads(self):
        """
        Testing creating simple ads
        """
        self.login()
        create_page = CreateAdsPage(self.driver)
        create_page.open()

        self.pre_creating(create_page)
        create_page.create_advert.submit()

        campaign_page = CampaignsPage(self.driver)
        name = campaign_page.campaign_data.get_campaign_name()
        campaign_page.navigation.go_to_edit()

        edit_page = EditPage(self.driver)
        title = edit_page.edit_advert.get_title()
        text = edit_page.edit_advert.get_text()

        self.assertEqual(CAMPAIGN_NAME, name)
        self.assertEqual(TEXT, text)
        self.assertEqual(TITLE, title)

    def test_age_targeting(self):
        """
        Testing age targeting according my variant
        """
        DESIRED_AGE = '18+'
        self.login()
        create_page = CreateAdsPage(self.driver)
        create_page.open()

        self.pre_creating(create_page)
        create_page.set_target.set_age()
        # choose some age
        create_page.set_target.set_age_6()
        # choose another age
        create_page.set_target.set_age_18()
        create_page.create_advert.submit()

        campaign_page = CampaignsPage(self.driver)
        campaign_page.navigation.go_to_edit()

        edit_page = EditPage(self.driver)
        age = edit_page.edit_advert.get_age()
        self.assertEqual(DESIRED_AGE, age)

    def test_where_targeting(self):
        DESIRED_WHERE = u'Бывший СССР'

        self.login()
        create_page = CreateAdsPage(self.driver)
        create_page.open()

        self.pre_creating(create_page)
        create_page.set_target.click_russia_checkbox()
        create_page.set_target.click_ussr_checkbox()
        create_page.create_advert.submit()

        campaign_page = CampaignsPage(self.driver)
        campaign_page.navigation.go_to_edit()

        edit_page = EditPage(self.driver)
        where = edit_page.edit_advert.get_where()

        self.assertEqual(DESIRED_WHERE, where[0])

    def test_two_where_conditions(self):
        DESIRED_WHERE_1 = u'Абхазия'
        DESIRED_WHERE_2 = u'Грузия'

        self.login()
        create_page = CreateAdsPage(self.driver)
        create_page.open()

        self.pre_creating(create_page)
        create_page.set_target.click_russia_checkbox()
        create_page.set_target.click_ussr()
        create_page.set_target.click_gruz_checkbox()
        create_page.set_target.click_abhaz_checkbox()
        create_page.create_advert.submit()

        campaign_page = CampaignsPage(self.driver)
        campaign_page.navigation.go_to_edit()

        edit_page = EditPage(self.driver)
        where = edit_page.edit_advert.get_where()

        self.assertEqual(DESIRED_WHERE_1, where[0])
        self.assertEqual(DESIRED_WHERE_2, where[1])

    def test_both_targetings(self):
        DESIRED_WHERE = u'Бывший СССР'
        DESIRED_AGE = '18+'

        self.login()
        create_page = CreateAdsPage(self.driver)
        create_page.open()

        self.pre_creating(create_page)
        create_page.set_target.set_age()
        create_page.set_target.set_age_18()
        create_page.set_target.click_russia_checkbox()
        create_page.set_target.click_ussr_checkbox()
        create_page.create_advert.submit()

        campaign_page = CampaignsPage(self.driver)
        campaign_page.navigation.go_to_edit()

        edit_page = EditPage(self.driver)
        where = edit_page.edit_advert.get_where()
        age = edit_page.edit_advert.get_age()

        self.assertEqual(DESIRED_AGE, age)
        self.assertEqual(DESIRED_WHERE, where[0])



