*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  rikku  rikkutikku99
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  riku  riku1231232232123
    Output Should Contain  User with username riku already exists

Register With Too Short Username And Valid Password
    Input Credentials  r  kankaanravintola99
    Output Should Contain  Username must be at least 3 characters long and contain only characters a-z.

Register With Valid Username And Too Short Password
    Input Credentials  olut  i
    Output Should Contain  Password must be at least 8 characters long and must contain numbers or special characters.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kaljavanukas  panpaanpaanklkasdf
    Output Should Contain  Password must be at least 8 characters long and must contain numbers or special characters.

*** Keywords ***
Input New Command And Create User
    Create user  riku  riku1231232232123
    Input New Command