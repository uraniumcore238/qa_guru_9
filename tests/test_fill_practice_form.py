import allure
from selene import have
from selene.support.shared import browser
from controls.checkbox_actions import CheckboxActions
from controls.feel_value import FeelValue
from advertisement_helper import remove_advertisement
from controls.file_actions import FileActions
from controls.table_checking import TableChecking
from pages.choose_date_page import ChooseDatePage
from pages.practice_form_page import PracticeFormPage
from pages.result_page import ResultPage


class TestFillPracticeForm:

    @allure.severity('Blocker')
    @allure.story('Check the student registration form filling')
    @allure.label("owner", "uraniumcore238")
    @allure.story('Fill student registration form')
    def test_fill_practice_form(self):

        with allure.step('Open browser'):
            browser.open('/automation-practice-form')

            PracticeFormPage.main_header.should(have.exact_text('Practice Form'))
            PracticeFormPage.first_name.type('Vasya')
            PracticeFormPage.last_name.type('Terkin')
            PracticeFormPage.user_email.type('example@gmail.com')
            PracticeFormPage.user_number.type('9999999999')
            FileActions.attach_file(self, PracticeFormPage.file_upload_field, 'resources/image.png')
            FeelValue.type_data_in_input_field(self, PracticeFormPage.subject_input_field, 'Eng')
            ChooseDatePage.select_date_in_selector(self, PracticeFormPage.date_of_birth_input_field, '1988', 'March', '15')
            CheckboxActions.choose_checkbox_by_value(self, PracticeFormPage.checkboxes, 'Male')
            CheckboxActions.choose_checkbox_by_value(self, PracticeFormPage.checkboxes, 'Sports')
            CheckboxActions.choose_checkbox_by_value(self, PracticeFormPage.checkboxes, 'Reading')
            CheckboxActions.choose_checkbox_by_value(self, PracticeFormPage.checkboxes, 'Music')
            remove_advertisement.remove_advertisement()
            PracticeFormPage.current_address.type('Current address')
            FeelValue.type_data_in_input_field(self, PracticeFormPage.state_input_field, 'Rajasthan')
            FeelValue.choose_data_in_selector(self, PracticeFormPage.city_input_field, PracticeFormPage.city_names, 'Jaipur')
            PracticeFormPage.submit_button.press_enter()

            # // assertions
            TableChecking.asserts_exact_text(self, ResultPage.header, 'Thanks for submitting the form')
            TableChecking.asserts_texts_in_rows(self, ResultPage.table_rows, 'Student Name Vasya Terkin Student Email '
                                                                       'example@gmail.com Gender Male Mobile 9999999999 '
                                                                       'Date of Birth 15 March,1988 Subjects English '
                                                                       'Hobbies Sports, Reading, Music Picture image.png '
                                                                       'Address Current address State and City '
                                                                       'Rajasthan Jaipur')
