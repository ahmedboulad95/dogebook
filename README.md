# Getting Started

## Install prerequisite software

1. Node.js - https://nodejs.org/en/download/
2. Python - https://www.python.org/downloads/
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
2. Navigate to the api folder and install the backend dependencies with pip
    ```
    cd api
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

    ```
    yarn start
    ```

A browser tab should open showing the react app. If it doesn't, navigate to https://localhost:3000