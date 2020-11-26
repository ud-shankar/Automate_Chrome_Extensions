##
# **Chrome Extension (Saka) Automated Testing**

The Test Automation Framework is created for automating the google chrome extensions Saka by using the CRX file of the extension, "keyboard" library of python to invoke the extension using hotkeys in the browser and verify the functionality.

### Scripting Language

Python is used as the scripting language. Pytest Framework is selected for Test Framework creation. Pytest-bdd solution has been used for creation of Automation Framework to use Cucumber+Gherkin feature files and to use full functionality of pytest. Cucumber files will help in improving the readability of test cases for users without coding background.

Selenium Webdriver is used to perform browser automation. The front end automation is achieved by implementing pytest test cases using webdriver based automation.

### Folder Structure

The Test Automation Suite is having below folders.

- **Features** : Feature files have been created based on each feature which is under test. The different scenarios and corresponding steps in each test case that is linked to the particular feature have been listed in the same feature file.
- **Source** : Source folder has been used to list the modules used to implement the source files for corresponding feature files steps. Emphasis has been kept to reuse the codes wherever possible using file level methods.
- **Drivers** : Folder used to save driver details used to link selenium to the corresponding browser driver and adding multiple arguments and extensions as options


### Saka_extension.crx file

The dictionary.crx file is used to add extension to the chrome driver using chrome options. This file is generated by using pack extension in your chrome browser in developer mode. This is important in automating chrome extensions.

### Creation of a test case

The following steps briefly describe how a new test case can be added to the framework.

1. Create a feature file, if required. Add the scenario and steps in the .feature file in Gherkin format.
2. Add the test cases scripts in the corresponding file in the Source folder. Do create a new script file if required. The steps and classes which are already implemented may be reused to reduce duplicate scripting.

### Test Execution

1. First clone the repo to your local. 
2. Open your terminal and point to the location.
3. Execute the command "pip install -r requirements.txt"
4. Tests can be executed by pointing the location of your terminal to where the project is saved and with a simple command 'pytest'.
