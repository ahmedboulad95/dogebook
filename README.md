# Getting Started

## Install prerequisite software

1. Node.js - https://nodejs.org/en/download/
2. Python - https://www.python.org/downloads/
    - Be sure to check the box at the bottom of the prompt to include Python in your PATH
3. Yarn
    Open git bash or other terminal application
    ```
    npm install --global yarn
    ```

## Clone the repo

1. Copy the repo url by clicking on the green "Code" button above and clicking the clipboard icon
2. Open git bash or other terminal application
3. Run the following commands to navigate to the desired location and clone the repo. This example uses the Documents folder, but any directory can be used
    ```
    cd ~/Documents
    git clone https://github.com/ahmedboulad95/dogebook.git
    ```
4. You should now have a folder named "dogebook". Run the following commands to confirm that the folder exists and to navigate inside the directory
    ```
    ls -l
    cd dogebook
    ```

## Install dependencies

1. In the project directory, install the frontend dependencies with npm
    ```
    npm install
    ```
2. Create and activate a Python virtual environment
    ```
    cd api
    python -m venv venv
    cd venv/Scripts/
    . activate
    ```
2. Navigate back to the api folder and install the python dependencies with pip
    ```
    cd ../..
    pip install -r requirements.txt
    ```
3. Navigate back to the root project folder
    ```
    cd ..
    ```

## Run the api server

1. On Windows
    ```
    yarn start-api-win
    ```
2. On Mac
    ```
    yarn start-api-mac
    ```

## Start the react app
1. Run the start script
    ```
    yarn start
    ```

A browser tab should open showing the react app. If it doesn't, navigate to https://localhost:3000

## Create a branch to work on a new feature

1. In git bash, navigate to the project folder
    ```
    cd ~/Documents/dogebook
    ```
2. Checkout the main branch and then create a new feature branch. Be sure to replace FEATURE_BRANCH_NAME with a descriptive feature name
    ```
    git checkout main
    git checkout -b FEATURE_BRANCH_NAME
    ```
3. Push your new branch up to the repository. Be sure to replace FEATURE_BRANCH_NAME with the name of your branch
    ``
    git add .
    git commit -m "Pushing new feature branch"
    git push -u origin FEATURE_BRANCH_NAME
    ```