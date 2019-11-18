*** Settings ***
| Library    | SeleniumLibrary | timeout=60
| Library    | PageObjectLibrary
| Resource   | web_main.robot
|
| Suite Setup    | Run Keywords | Set Selenium Speed   | 0.2 | AND | Open Browser For Test Website | ${TEST_WEBSITE}
| Suite Teardown | Close all browsers

*** Test Cases ***
| Create Account If Not Exists And Login
| | The Current Page Should Be | pages.HomePage
| | Click Sign In
| | The current page should be | pages.LoginPage
| | Create Account With | ${default_email}
| | Sleep | 5
| | ${result} | Verify Account Exist Or not
| | Run Keyword Unless | ${result} | Register New User Account
| | Run Keyword If | ${result} | Login Using Provided Credential | ${default_email} | ${default_pw}
| | The Current Page Should Be | pages.AccountPage
| | Click The Home Button
| | The Current Page Should Be | pages.HomePage

| Add A Product In Shopping Cart
| | Add To Shopping Cart
| | Go To Shopping Cart
| | Verify Product In Cart
