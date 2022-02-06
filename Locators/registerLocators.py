class RegisterLocators:

    # Registration page elements
    username_textbox_css = 'fieldset:nth-of-type(1) > .form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid'
    email_textbox_css = '.form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid.ng-valid-email'
    password_textbox_css = '.form-control.form-control-lg.ng-empty.ng-pristine.ng-untouched.ng-valid'
    sign_up_button_xpath = "//button[@type='submit']"

    error_message_classname = 'error-messages'