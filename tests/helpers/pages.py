import urlparse

from tests.helpers.components import AuthForm, TopMenu, BaseSettings, CreateAdd, Navigation, EditAdd, CampaignData, SetTarget


__author__ = 'warprobot'


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = "/login"

    @property
    def form(self):
        return AuthForm(self.driver)


class CampaignsPage(Page):
    PATH = '/ads/campaigns/'

    @property
    def navigation(self):
        return Navigation(self.driver)

    @property
    def campaign_data(self):
        return CampaignData(self.driver)


class CreateAdsPage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def base_settings(self):
        return BaseSettings(self.driver)

    @property
    def create_advert(self):
        return CreateAdd(self.driver)

    @property
    def set_target(self):
        return SetTarget(self.driver)


class EditPage(Page):

    @property
    def edit_advert(self):
        return EditAdd(self.driver)
