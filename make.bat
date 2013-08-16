@echo off

:: Replacement for make on Windows.

set PYTHON=python
set TESTRUNNER=unittest
set RUNTEST=%PYTHON% -m %TESTRUNNER%

if "%1" == "" goto help

if "%1" == "help" (
    :help
    echo.Please use `make ^<target^>` where ^<target^> is one of
    echo.  run       to run the server.
    echo.  test      to run unit tests.

    goto end
)

if "%1" == "run" (
    %PYTHON% yaktak/app.py
    if errorlevel 1 exit /b 1
    goto end
)

if "%1" == "test" (
    %RUNTEST% yaktak.tests.test_suite
    if errorlevel 1 exit /b 1
    goto end
)

:end
