import allure
from selene.core import command
from selene.core.entity import Element
from selene.support.conditions import have
# from selene.support.shared.jquery_style import ss, s


class FeelValue:

    def type_data_in_input_field(self, el: Element, text: str):
        allure.step(f'Type data {text} in input field')
        el.perform(command.js.scroll_into_view).type(text).press_tab()

    def choose_data_in_selector(self, container: Element, els: all, text: str):
        allure.step(f'Choose {text} in selector')
        container.perform(command.js.scroll_into_view).click()
        els.element_by(have.text(f'{text}')).click()
