import urlparse
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait


class Page(object):
    BASE_URL = 'https://target.mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)


class AuthPage(Page):
    PATH = '/login'

    @property
    def form(self):
        return AuthForm(self.driver)


class CreatePage(Page):
    PATH = '/ads/create'

    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def slider(self):
        return Slider(self.driver)


class Component(object):
    def __init__(self, driver):
        self.driver = driver


class Campaigns(Page):
    PATH = '/ads/campaigns'

    @property
    def get_delete(self):
        return DeleteCompany(self.driver)


class DeleteCompany(Component):
    DELETE = '.control__preset_delete'

    def click_delete(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.DELETE)
        ).click()


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


class Slider(Component):
    SLIDER = '.price-slider__begunok'

    def move(self, offset):
        element = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.SLIDER)
        )
        ac = ActionChains(self.driver)
        ac.click_and_hold(element).move_by_offset(offset, 0).perform()


class ThatAdvertise(Component):
    PRODUCT = '#product-type-5212'

    def set_product(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PRODUCT)
        ).click()


class Platform(Component):
    PLATFORM = '#pad-mobile_odkl_feed_abstract'

    def set_platform(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.PLATFORM)
        ).click()


class CreateCompany(Component):
    CREATE = '.main-button-new'

    def click(self):
        self.driver.find_element_by_css_selector(self.CREATE).click()


class CreateAds(Component):
    TITLE = 'input[data-name="title"]'
    TEXT = 'textarea[data-name="text"]'
    LINK = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[3]/div/div[1]/ul/li[4]/span[2]/input'
    IMAGE = 'input[data-name="image"]'
    IMAGE_SMALL = 'input[data-name="image"]'
    IMAGE_BIG = 'input[data-name="promo_image"]'
    ADD = '.banner-form__save-button'

    def set_title(self, title):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TITLE)
        ).send_keys(title)

    def set_text(self, text):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.TEXT)
        ).send_keys(text)

    def set_link(self, link):
        link_ = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LINK)
        )
        link_.send_keys(link)

    def set_image(self, url):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE)
        ).send_keys(url)

    def set_image_small(self, url):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE_SMALL)
        ).send_keys(url)

    def set_image_big(self, url):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.IMAGE_BIG)
        ).send_keys(url)

    def add(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.ADD)
        ).click()


class AgeRestrictions(Component):
    RESTRICT = 'span[data-node-id="restrict"]'
    AGE = '//*[@id="restrict-0+"]'

    def click_restrict(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.RESTRICT)
        ).click()

    def click_age(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.AGE)
        ).click()


class Where(Component):
    ASIA = '//*[@id="regions100003"]/input'
    ARROW_ASIA = '//*[@id="regions100003"]/span[1]'
    INNER_TAG_1 = '//*[@id="regions204"]/label'
    INNER_TAG_2 = '//*[@id="regions222"]/label'

    def click_asia(self):
        WebDriverWait(self.driver, 40, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ASIA)
        ).click()

    def click_arrow_asia(self):
        WebDriverWait(self.driver, 40, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ARROW_ASIA)
        ).click()

    def click_inner_tag(self):
        WebDriverWait(self.driver, 40, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INNER_TAG_1)
        ).click()
        WebDriverWait(self.driver, 40, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INNER_TAG_2)
        ).click()


class Edit(Component):
    EDIT = '.control__link_edit'

    def click_edit(self):
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_css_selector(self.EDIT)
        ).click()


class GetResult(Component):
    ASIA = '//*[@id="regions100003"]/input'
    RESTRICT = '/html/body/div[1]/div[5]/div/div[2]/div/div[1]/div[7]/div/div[2]/ul/li[3]/div/div[2]/span'
    INNER_TAG_1 = '//*[@id="regions204"]/input'
    INNER_TAG_2 = '//*[@id="regions222"]/input'

    def get_checked_asia(self):
        asia = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.ASIA)
        )
        return asia.is_selected()

    def get_checked_inner_asia_1(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INNER_TAG_1)
        ).is_selected()

    def get_checked_inner_asia_2(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.INNER_TAG_2)
        ).is_selected()

    def get_text_age(self):
        text = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.RESTRICT).text
        )
        return text
