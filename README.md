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


### Validator Testing

- Made use of the [PEP8](http://pep8online.com/) online validation tool for systematic validator testing.


#### Initial Validator Tests

- Initial validator test for run.py results:
 - Found E402 error with position of Google-auth module level import - **Resolved** by changing position and eliminating unneccessary commenting.
 - Found 2 errors (W291 and W293) for "whitespace" in code - All **Resolved**
 - Found 6 E501 errors for length of line used - All **Resolved**
 - Found E302 error for only spacing with 1 blank line instead of 2 - **Resolved**

### Unfixed Bugs

- 

## Deployment

- 

Here is the live link [???](###)

## Deployment Testing

- 

## Credits

- First and foremost I would like to thank my mentor Anthony for his valuable input.
- Code institutes Course material was essential for setting up and deployment.


### Content

- Commit comment conventions were taken from [Cheatography](https://cheatography.com/albelop/cheat-sheets/conventional-commits/), I do not totally understand all the vernacular but tried my best to implement it as best I could.


### Media

- 
