*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click  button >> text=Register
    Register Should Succeed

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