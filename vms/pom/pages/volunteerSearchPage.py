# Django
from pom.pages.basePage import BasePage

# local Django
from pom.locators.volunteerSearchPageLocators import VolunteerSearchPageLocators
from pom.pages.authenticationPage import AuthenticationPage
from pom.pageUrls import PageUrls


class VolunteerSearchPage(BasePage):

    volunteer_search_page = PageUrls.volunteer_search_page
    live_server_url = ''

    def __init__(self, driver):
        self.driver = driver
        self.authentication_page = AuthenticationPage(self.driver)
        self.elements = VolunteerSearchPageLocators()
        super(VolunteerSearchPage, self).__init__(driver)

    def navigate_to_volunteer_search_page(self):
        self.get_page(self.live_server_url, self.volunteer_search_page)

    def submit_form(self):
        self.element_by_class_name(self.elements.SUBMIT_PATH).click()

    def send_to_field(self, field, value):
        text_box = self.find_element_by_css_selector(field)
        text_box.clear()
        text_box.send_keys(value)

    def search_first_name_field(self, search_text):
        self.send_to_field(self.elements.FIRST_NAME_FIELD, search_text)

    def search_last_name_field(self, search_text):
        self.send_to_field(self.elements.LAST_NAME_FIELD, search_text)

    def search_city_field(self, search_text):
        self.send_to_field(self.elements.CITY_FIELD, search_text)

    def search_state_field(self, search_text):
        self.send_to_field(self.elements.STATE_FIELD, search_text)

    def search_country_field(self, search_text):
        self.send_to_field(self.elements.COUNTRY_FIELD, search_text)

    def search_organization_field(self, search_text):
        self.element_by_id('select').send_keys(search_text)

    def search_event_field(self, search_text):
         self.send_to_field(self.elements.EVENT_FIELD, search_text)

    def search_job_field(self, search_text):
         self.send_to_field(self.elements.JOB_FIELD, search_text)

    def get_help_block(self):
        return self.element_by_class_name(self.elements.HELP_BLOCK)

    def get_search_results(self):
        search_results = self.element_by_xpath(self.elements.RESULT_BODY)
        return search_results

    @staticmethod
    def get_results_list(search_results):

        result = []
        for tr in search_results.find_elements_by_tag_name('tr'):
            row = tr.text.split()
            result.append(row)

        return result

    def get_shift_summary(self):
        return self.element_by_xpath(self.elements.TOTAL_SHIFTS).text
