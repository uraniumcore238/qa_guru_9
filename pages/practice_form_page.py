from selene.support.shared.jquery_style import s, ss


class PracticeFormPage:

    main_header = s('.main-header')
    first_name = s('#firstName')
    last_name = s('#lastName')
    user_email = s('#userEmail')
    checkboxes = ss('.custom-control')
    user_number = s('#userNumber')
    date_of_birth_input_field = s('#dateOfBirth input')
    file_upload_field = s('#uploadPicture')
    current_address = s('#currentAddress')
    state_input_field = s('#state input')
    city_input_field = s('#city')
    city_names = s("//div[contains(@class, '-menu')]").ss("//div[contains(@id, 'react-select')]")
    subject_input_field = s('#subjectsContainer input')
    male_checkbox = s('#subjectsContainer input')
    submit_button = s('#submit')

