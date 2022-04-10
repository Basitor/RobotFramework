*** Settings ***
Library  TestCase.py
Library  Helpers.py

Test Setup  test_setup


*** Variables ***
@{str_cases}  string  123  $@!%&*  string\n


*** Test Cases ***

7000 test for loop
    FOR  ${CASE}  IN  @{str_cases}
        test_add_string_no_return  ${CASE}        ${CASE}test
    END

7001 test2
    TRY
        test_add_string_no_return  ${1}        ${1}test
    EXCEPT
        Pass  "Function should raise exception with int parameter"
    ELSE
        Fail  "Function shouldn't pass with int parameter"
    END

7002 test return
    FOR  ${CASE}  IN  @{str_cases}
        ${returned_value}  test_add_string_return  ${CASE}
        Should Be Equal  ${returned_value}  ${CASE}test
    END