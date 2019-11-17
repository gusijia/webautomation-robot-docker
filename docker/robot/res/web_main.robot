*** Settings ***
Library    SeleniumLibrary   timeout=60
Library    PageObjectLibrary

*** Keywords ***
Open Browser For Test Website
| | [Arguments] | ${testwebsite}
| | Close all browsers
| | Open Browser | ${testwebsite} | ${BROWSER} | ${ALIAS} | ${REMOTE_URL} | ${CAPABILITIES}
| | Maximize browser window

Login Using Provided Credential
| | [Arguments] | ${email} | ${password}
| | The Current Page Should Be | pages.LoginPage
| | Enter email address | ${email}
| | Enter password | ${password}
| | Click the login button

Register New User Account
| | The Current Page Should Be | pages.AccountCreationPage
| | Enter Personal Information | ${firstname} | ${lastname} | ${default_pw}
| | Enter Address | ${user_address} | ${city} | ${state_option} | ${zip_code} | ${country_option} | ${phone_number}
| | Click Register button
