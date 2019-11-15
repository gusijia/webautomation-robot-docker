*** Settings ***
| Library    | SeleniumLibrary | timeout=60
| Library    | PageObjectLibrary
| Resource   | web_main.robot
|
| Suite Setup    | Set Selenium Speed   | 0.2
| Test Setup    | Open Browser For Test Website | ${TEST_WEBSITE}
| Suite Teardown | Close all browsers

*** Test Cases ***
| Login Using Correct Account
| | [Documentation] | Verify that we can login successfully.
| | Login Using Provided Credential | ${default_email} | ${default_pw}
