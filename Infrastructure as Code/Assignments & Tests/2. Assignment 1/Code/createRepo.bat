::#######################################################################################
::# Name:     createRepo.bat
::# Purpose:  Creates directory Repository for storing Projects related documentation
::#              Directory can be reated eithe using standard template or customizable
::# Author:   PJ McMenamin
::# Revision: October 2023 - initial version
::#           October 2023 - added support for FooBar v2 switches
::#######################################################################################
@echo off
Setlocal EnableDelayedExpansion

call:mainMenu
goto:exitProgram

::#######################################################################################
::# Function: mainMenu
::#           Print Main Menu options for user selection
::#######################################################################################
:mainMenu
    cls
    echo.  **********************************************
    echo.              Repository Creation
    echo.  **********************************************
    echo.
    echo.      1 - Create Repository - Template based
    echo.      2 - Create Repository - Customizable
    echo.      3 - Exit
    echo. 
    set /p option1=Please select an Option, then press [return] :
    echo.  _ %option1% _

    if %option1%==1 goto:repo_standardDir
    if %option1%==2	goto:repo_newDirPt1
    if %option1%==3	goto:EOF
goto:mainMenu


::#######################################################################################
::# Function: repo_standardDir
::#           Created new Repository structure using predefined directory structure
::#######################################################################################
:repo_standardDir
    cls 
    echo.  **********************************************
    echo.            Create standard Repository
    echo.  **********************************************
    echo.
    set /p dirName=Enter Project Name:

    if exist %dirName% (
        echo.  %dirName% already exists... cannot overwrite.!
        echo.  Press any key to return to Main Menu...
        pause
    ) else (
        mkdir %dirName%
        cd %dirName%

        mkdir config
        mkdir docs
        mkdir images
        mkdir src
        
        cd src
        mkdir alert
        mkdir reporting
        mkdir server
        cd ..
        
        cd %dirName%

        goto:printDirDetails
    )
goto:mainMenu


::#######################################################################################
::# Function: repo_newDirPt1,
::#           Created New Repository structure - directories to be specified
::#######################################################################################
:repo_newDirPt1
    cls 
    echo.  **********************************************
    echo.            Create New Repository
    echo.  **********************************************
    echo.
    set /p dirName=Enter Project Name:

    if exist %dirName% (
        echo.  %dirName% already exists... cannot overwrite.!
        echo.  Press any key to return to Main Menu...
        pause
    ) else (
        mkdir %dirName%
        cd %dirName%
        
        goto:createSubDir
    )
goto:mainMenu

:createSubDir 
    set /p option2=Do you wish to create sub directory [Y/N]:

    if /I %option2%==Y (
        goto:createSubDir2
    )
    if /I %option2%==N (
        goto:printDirDetails
    )
goto:createSubDir

:createSubDir2
	set /p subDirName=Enter Project subfolder Name:
	mkdir %subDirName%
goto:createSubDir

:printDirDetails
    cd..

    cls
    echo.  *********************************************
    echo.              New Project Details  
    echo.  *********************************************
    echo.
	echo.  New Project: %dirName% has been created successfully...
	echo.
	tree %dirName% /F
	echo.
	pause
goto:mainMenu


::#######################################################################################
::# Function: exitProgram
::#           Exits program
::#######################################################################################
:exitProgram
    cls
    echo.  **********************************************
    echo.                Exit Program
    echo.  **********************************************
EXIT /b 0