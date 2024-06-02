# Project Automation Testing

## Description

This project is a simple automation testing for website 'https://www.saucedemo.com' with selenium, it also includes API testing provided by 'https://dummyapi.io' and tested with Requests library. For creating and running the scenario, we use Behave library. The project is written in Python language.

## Prerequisites

- Allure
  - Download and install Allure from https://docs.qameta.io/allure/
- Conda or Miniconda
  - Download and install Miniconda from https://docs.conda.io/en/latest/miniconda.html
- Java 17
  - install java 17
  - Download and install Java 17 from https://www.oracle.com/java/technologies/javase-jdk17-downloads.html
  - Set the JAVA_HOME environment variable to the Java 17 installation path.
- Chrome Browser
  - Download and install Chrome Browser from https://www.google.com/chrome/
- Chrome WebDriver
  - Download the Chrome WebDriver from the following link and put it on the environment path:
    - https://chromedriver.chromium.org/downloads
    - Note : Make sure to download the version that matches your Chrome browser version.

### Installation

- Clone the following repository:
  - https://github.com/GitGudwl/AutomationTestingProject/tree/main
- Import the conda environment:
  - Open the terminal and navigate to the project folder
  - Run the following command:
    - `conda env create -f conda_env.yaml`
- Activate the conda environment on your terminal:
  - Run the following command:
    - `conda activate Softwar_Testing`
- You don't need to install the following libraries, they are already included in the conda environment:
  - `behave`
  - `requests`
  - `selenium`
  - `allure-behave`

## File Configuration

- To add new test cases, you can create a new feature file in the 'features' folder and add the steps in the 'steps' folder.
  - Note : Behave python not allowing multiple folders for steps, so you need to put all the steps in the 'steps' folder (I know it's hard to manage).
- To add new page objects, you can create a new python file in the 'pages' folder.
- To add new json data for API testing, you can create a new json file in the 'data' folder.
- To add new helper functions for API testing, you can create a new python file in the 'helpers' folder.

- The project structure should look like this:
  ```
  ├───features
  │   ├───data
  │   │
  │   └───steps
  │       └───helpers
  │
  ├───pages
  │
  └───reports
      └───features
  ```
  - Note : Delete the 'Reports' folder if you want to re-generate the test reports using Allure.

## Running the Test

- To run all the test scenarios, you can run the following command:
  - `behave`
- To run a specific test scenario, you can run the following command:
  - `behave features/<feature_file_name>.feature`
- To run the test with Allure report, you can run the following command:
  - `behave -f allure_behave formatter:AllureFormatter -o reports/features
`
  - Note : please delete the 'Reports' folder if you want to re-generate the test reports using Allure.
- To view the Allure report, you can run the following command:
  - `allure serve reports/features`

#### Software Under Test

- Website : https://www.saucedemo.com
- API : https://dummyapi.io

## Test Cases or Scenarios

The test cases or scenarios are written in the 'features' folder with the '.feature' extension.

## Author

- Zahri Al Adzani Hidayat
- Muhammad Fadhil
- Raihan Shidqi Pangestu
