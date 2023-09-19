import os

from selene import browser, command
from selene.support.conditions import have, be

def test_practice_form():
    browser.open('/')
    browser.element('#firstName').type('John')
    browser.element('#lastName').type('Dou')
    browser.element('#userEmail').type('JohnDou@gmail.com')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type(8999374567)
    browser.element('#dateOfBirthInput').click()
    browser.element('#dateOfBirthInput').perform(command.js.scroll_into_view).click()
    browser.element('.react-datepicker__month-select').send_keys("March")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').send_keys("1989")
    browser.element('#dateOfBirthInput').click()
    browser.element(f'.react-datepicker__day--005').click()
    browser.element('#subjectsInput').send_keys('Computer Science').press_tab()
    browser.all('#hobbiesWrapper .custom-control-label').element_by(have.exact_text('Sports')).click()
    browser.all('#hobbiesWrapper .custom-control-label').element_by(have.exact_text('Reading')).click()
    browser.all('#hobbiesWrapper .custom-control-label').element_by(have.exact_text('Music')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('resources/photo.jpg'))
    browser.element('#currentAddress').type('street test 12')
    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()

    browser.element('#submit').press_enter()


    browser.all('.table-responsive .table td:nth-child(2)').should(have.exact_texts(
        'John Dou',
        'JohnDou@gmail.com',
        'Male',
        '8999374567',
        '05 March,1989',
        'Computer Science',
        'Sports, Reading, Music',
        'photo.jpg',
        'street test 12',
        'Haryana Karnal'

    ))