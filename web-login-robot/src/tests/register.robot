*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  Riku
    Set Password  Salasana2
    Set Password2  Salasana2
    Submit Credentials
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  Ri
    Set Password  Salasana2
    Set Password2  Salasana2
    Submit Credentials
    Page Should Contain  Username must be at least 3 characters long and contain only letters a-z

Register With Valid Username And Too Short Password
    Set Username  Rikua
    Set Password  Sala2
    Set Password2  Sala2
    Submit Credentials
    Page Should Contain  Password must be at least 8 characters long and contain special characters and numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  Rikub
    Set Password  Salasalasale2
    Set Password2  Salasalasala2
    Submit Credentials
    Page Should Contain  Password and password confirmation do not match

Login After Successful Registration
    Go To Login Page
    Set Username  Riku
    Set Password  Salasana2
    Click Button  Login
    Page Should Contain  Ohtu Application main page

Login After Failed Registration
    Go To Login Page
    Set Username  Rikub
    Set Password  Salasalasale2
    Click Button  Login
    Page Should Contain  Invalid username or password

*** Keywords ***
Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password2
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open