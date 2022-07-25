import allure
from selene.support.conditions import have


class CheckboxActions:

    @allure.title('Choose checkbox by name')
    def choose_checkbox_by_value(self, els: all, checkbox_name: str):
        allure.step(f'Choose checkbox "{checkbox_name}"')
        els.element_by(have.text(f'{checkbox_name}')).click()
