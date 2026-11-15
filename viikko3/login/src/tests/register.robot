*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Numbers In Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click  button >> text=Register
    Register Should Succeed

Register With Valid Username And Special Character In Password
    Set Username  pekka
    Set Password  pekka#abc
    Set Password Confirmation  pekka#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Different Password Confirmation
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka124
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register With Valid Username And Password With Only Lowercase Letters
    Set Username  pekka
    Set Password  pekkapekka
    Set Password Confirmation  pekkapekka
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or special character

Register With Valid Username And Password With Only Letters
    Set Username  pekka
    Set Password  PekkaPekka
    Set Password Confirmation  PekkaPekka
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or special character

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click  button >> text=Register
    Register Should Fail With Message  Username is too short (at least 3 characters)

Register With Valid Username And Too Short Password
    Set Username  pekka
    Set Password  pekka
    Set Password Confirmation  pekka
    Click  button >> text=Register
    Register Should Fail With Message  Password is too short (at least 8 characters)

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password Confirmation
    [Arguments]  ${password_confirm}
    Fill Secret  id=password_confirmation  $password_confirm

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page