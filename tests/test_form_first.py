from pages.registration_page import registration


def test_registration_demoqa():
    registration.open()
    registration.type_first_name('Kam')
    registration.type_last_name('Mar')
    registration.type_email('m81321184@gmail.com')
    registration.click_gender()
    registration.type_number('1234567890')
    registration.type_subject('computer')
    registration.type_birthday(3, 2000, 2)
    registration.type_hobbies()
    registration.upload_photo('img.png.png')
    registration.type_address('ЦАО')
    registration.type_state("Rajasthan")
    registration.type_city("Jaiselmer")
    registration.click_submit()
    registration.should_text('Thanks for submitting the form')
    registration.should_exact_text('Kam Mar', 'm81321184@gmail.com', 'Female', '1234567890', '02 April,2000',
                                   'Computer Science', 'Sports', 'img.png.png', 'ЦАО', 'Rajasthan Jaiselmer')

