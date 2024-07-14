from selene import browser, command, have
from demoqa_tests import resources


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def type_first_name(self, name):
        browser.element('#firstName').type(name)
        return self

    def type_last_name(self, lastname):
        browser.element('#lastName').type(lastname)
        return self

    def type_email(self, email):
        browser.element('#userEmail').type(email)
        return self

    def click_gender(self):
        browser.element('[for="gender-radio-2"]').click()
        return self

    def type_number(self, number):
        browser.element("#userNumber").type(number)
        return self

    def type_subject(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()
        return self

    def type_birthday(self, month, year, day):
        browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select').element(f'[value="{month}"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select').element(f'[value="{year}"]').click()
        browser.element(f'.react-datepicker__day--00{day}').click()
        return self

    def type_hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        return self

    def upload_photo(self, photo):
        browser.element('#uploadPicture').set_value(resources.resources_path(photo))
        return self

    def type_address(self, address):
        browser.element('#currentAddress').type(address).press_enter()
        return self

    def type_state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()
        return self

    def type_city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()
        return self

    def click_submit(self):
        browser.element('#submit').press_enter()
        return self

    def should_text(self, text):
        browser.element("#example-modal-sizes-title-lg").should(have.text(text))
        return self

    def should_exact_text(self, first_name, email, gender, phone, birthday, hobbies, hobbies2, photo, address, city):
        browser.element('.table').all('td').even.should(have.exact_texts(first_name, email, gender, phone, birthday,
                                                                         hobbies, hobbies2, photo, address, city))
        return self


registration = RegistrationPage()
