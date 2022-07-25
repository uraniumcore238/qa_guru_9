import allure
from selene.core import command
from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss


class ChooseDatePage:

    date_of_birth_input_field = s('#dateOfBirth input')
    years = s(".react-datepicker__year-select").ss('option')
    months = s(".react-datepicker__month-select").ss('option')
    days = ss(".react-datepicker__day")

    def select_date_in_selector(self, el, year: str, month: str, day: str):
        allure.step(f'Select date {day}.{month}.{year} in selector')
        el.perform(command.js.scroll_into_view).click()
        ChooseDatePage.years.element_by(have.exact_text(f'{year}')).click()
        ChooseDatePage.months.element_by(have.exact_text(f'{month}')).click()
        ChooseDatePage.days.element_by(have.exact_text(day)).click()
