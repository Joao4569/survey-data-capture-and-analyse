# Survey Data Analyser

## Conception

- Lucidchart chart and planning


## Setup of Gitpod Workspace and resources

I made use of Code Institutes "Love Sandwiches Walkthrough Project", "Getting Set Up" course videos for the following:
 - [Creating a Google Sheet](https://youtu.be/4MWpwuPpSCA).
 - [To activate API credentials](https://youtu.be/WTll5p4N7hE).
 - [Setup of Gitpod Workspace](https://youtu.be/3ikrLWM0QqU).
 - [Connecting to the API with Python](https://youtu.be/lPTKUiafTRY).

## Features

### Existing Features

## Testing

- Made use of the terminal window and print function on multiple occasions in order to view data and check if functions work as expected.

- Tested data_validator function with various data types and amounts of data provided:

 - If less than 4 values provided - ValueError raised as intended.
 - If more than 4 values provided  - ValueError raised as intended.
 - If a non numerical string is provided by the user - ValueError raised as intended.
 - If each supplied result by user is between 0 and 10 - ValueError raised as intended.

- Tested if program is updating the Google worksheet correctly - Working as intended.
- 


### Validator Testing

- Made use of the [PEP8](http://pep8online.com/) online validation tool for systematic validator testing.


#### Initial Validator Tests

- Initial validator test for run.py results:
 - Found **E402** error with position of Google-auth module level import - **Resolved** by changing position and eliminating unneccessary commenting.
 - Found 2 errors **(W291 and W293)** for "whitespace" in code - All **Resolved**
 - Found 6 **E501** errors for length of line used - All **Resolved**
 - Found **E302** error for only spacing with 1 blank line instead of 2 - **Resolved**

### Unfixed Bugs

- 

## Deployment

- This application is deployed on [Heroku](https://id.heroku.com/login) as described by Code Institute in the Love Sandwiches walkthrough project [deployment video Part 1](https://youtu.be/BhW26FryaYI) and [deployment video Part 2](https://youtu.be/ONx3iEqAOM4) and these were the neccessary steps in the order that they need to be done:

 1. Firstly I added a new line character (\n) to the end of the text of any input methods due to a software issue as describe in the tutorial, in order to display the input method's text in the terminal as intended.
 2. I create a list of requirements as described in the tutorial in order for the program to run as intended, Heroku will need these dependencies in order to run the application on the deployed site.
 3. I opened Heroku and on the dashboard page click on the "NEW" button and select the "Create a new app" option.
 4. On the new page that opens, I named my app, selected my region and then clicked on the "Create app" button.
 5. On the new page select the settings tab.
 6. On the new page, in the config vars section, I selected the "Reveal Config Vars" button.
 7. Next I selected the "Key" input field and typed in "CREDS" as the key.
 8. I then copied my creds.json file content and pasted that into the "Value" input area, and clicked the "Add" button.
 9. Next I added the word "PORT" as another "Key" with "8000" as the "Value" and again clicked on the "Add" button.
 10. I then selected the "Add buildpack" button, then first selected the "Python" option and saved the changes.
 11. I repeated the previous step but this time selected the node.js option and saved this buildpack change.
 12. I then selected the "Deploy" tab on the top of the page.
 13. I then selected "Github" as my deployment method and clicked on the "Connect to Github" button.
 14. Next I searched for this app's repository in the "Connect to Github" section of the page and clicked on connect on order to connect the repository to this application.
 15. Next I clicked on the "Deploy Branch" button in the "manual Deploy" section of the page.
 16. Once the app was built, I selected the "View" button under the now visible "Your app was successfully deployed" message in order to view the page of the now running application.
 17. After previewing the running application I went back to the previous page and toggled the "Enable Automatic Deploys" button so that the app would automatically update when a change is pushed to Github.

Here is the live link [Survey Data Capture and Extraction Application](https://survey-data-capture-extract.herokuapp.com/)

## Deployment Testing

- Found bug with how print statements are displayed on deployed site in relation with how they are inputted into workspace to avoid line being too long as described by PEP8 validator - **Resolved** by correct use of quotation marks, indentation and new line characters (\n), I managed to resolve all my display issues on the deployed site.

## Credits

- First and foremost I would like to thank my mentor Anthony for his valuable input.
- Code institutes Course material was essential for setting up a workspace and deployment of the program on [Heroku](https://id.heroku.com/login).
- I sourced the code for printing coloured text to the terminal from [lycaeum.dev](https://lycaeum.dev/en/questions/287871).
- I researched and made use of basic Markdown syntax sourced on [markdownguide.org](https://www.markdownguide.org/basic-syntax/).


### Content

- Commit comment conventions were taken from [Cheatography](https://cheatography.com/albelop/cheat-sheets/conventional-commits/), I do not totally understand all the vernacular but tried my best to implement it as best I could.


### Media

- 
