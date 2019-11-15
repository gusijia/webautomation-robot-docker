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
| | The Current Page Should Be | pages.HomePage
| | Click Sign In
| | The current page should be | pages.LoginPage
| | Enter username | ${email}
| | Enter password | ${password}
| | Click the login button
