# Survey Data Analyser

## Conception

- Lucidchart chart and planning

### Home Page

- Example point 1.
- Example point 2.
- Example point 3.
- Example point 4.

![#Image-Name](Relative-link.png)


## Setup of Gitpod Workspace and resources

I made use of Code Institutes "Love Sandwiches Walkthrough Project", "Getting Set Up" course videos for the following:
 - [Creating a Google Sheet](https://youtu.be/4MWpwuPpSCA).
 - [To activate API credentials](https://youtu.be/WTll5p4N7hE).
 - [Setup of Gitpod Workspace](https://youtu.be/3ikrLWM0QqU).
 - [Connecting to the API with Python](https://youtu.be/lPTKUiafTRY).

## Features

### Existing Features

- __Navigation Bar__

  - 
  - 

- __The Landing Page Image__

  - 
  - 

### Features Left to Implement


## Testing

- Found bug with navigation menu order, it is displaying in reverse order.
  - **Resolved** by researching information on [Web Developer Diary](http://nambiara.blogspot.com/2010/10/float-right-without-changing-order.html) and applying it to my design.
- Found that the Hero image did not cover entire screen width.
  - **Resolved** by using original image size instead of a re-sized image.
- Found that the tile display on the home page for the method introductions did not display as planned.
  - **Resolved** by adding additional div elements and floating their children as needed.

- Tested all internal links - All are functioning as intended.
- Tested all external links - All are functioning as intended.
- Tested all embedded videos - All are functioning as intended.
- Sourced most common media breakpoint widths on [www.freecodecamp.org](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/.) and made the site responsive down to minimum width of 320 pixels.
  - Mobile devices: 320px — 480px
  - iPads, Tablets: 481px — 768px
  - Small screens, laptops: 769px — 1024px
  - Desktops, large screens: 1025px — 1200px
  - Extra large screens, TV: 1201px and more
- Made use of Chrome developer tools for previewing and testing new designs for media queries as well as UX aspects.

### Validator Testing

- Made use of the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/) for the CSS file and the official [W3C validator](https://validator.w3.org/) for all HTML file testing. !!!![PEP8](https://)

#### Initial Validator Tests
- Initial validator test for index.html results:
  - 3 Bad Value errors for having spaces in image names.
    - **Resolved** by re-naming images accordingly.
  - 1 Warning for using an H1 tag incorrectly.
    - **Resolved** by replacing it with an unordered list for logical semantic structure.

- Initial validator test for balance.html results:
  - Found 4 errors referring to usage of height and width attributes in iframe tags with values of "100%".
    - **Resolved** by removing attributes and styling with CSS.
  - Found 2 warnings for the use of H1 tags.
    - **Resolved** by replacing with H2 tags for semantic structure.

- Initial validator test for minfulness.html results:
  - Found 4 errors referring to usage of height and width attributes in iframe tags with values of "100%".
    - **Resolved** by removing attributes and styling with CSS.
  - Found 2 warnings for the use of H1 tags.
    - **Resolved** by replacing with H2 tags for semantic.

- Initial validator test for sign-up.html results:
  - Found 1 warning for the use of H1 tags.
    - **Resolved** by replacing with H2 tags for semantic structure.

#### Final Validator tests

- Final validator test for index.html results:
  - 1 Warning for the introduction section not having a heading as it was wrapped in a nav element.
    - **Resolved** by removing the outer nav element as it served no other function.

- Final validator test for balance.html results:
  - No errors or warnings found.

- Final validator test for mindfulness.html results:
  - No errors or warnings found.

- Final validator test for sign-up.html results:
  - No errors or warnings found.

- Final validator test for style.css results:
  - file validates as CSS level 3 + SVG

- Final validator test for thank-you.html results:
  - No errors or warnings found.

- All the pages of  have passed their validator testing at the time of submission.

### Unfixed Bugs

- The only issues that I have found with Becentered is that I feel some containers (for example the technique page headings, detailed technique descriptions, sign up page heading, thank you page heading and footer) are not fully responsive in relation to their content and that a lot of manual adjustments had to be made to assist their responsiveness concerning appearance over the various media queries.
- I started doing some research and I was looking into the issue for this project and think that by using flex boxes I could possibly solve this issue but as I only discovered this possible solution barely 48 hours prior to the final submission date, I decided it unwise to try and restructure my code on that scale so close to the submission date.

## Deployment

- BeCentered was deployed to GitHub pages, the steps were as follows:
  - While in the GitHub repository, select the settings tab.
  - Then select the Pages tab from the new menu to the left of the viewport.
  - From the source section drop down menu, select Main branch.
  - Once the main branch has been selected, the page will automatically refresh with a detailed ribbon display to indicate the successful deployment.

Here is the live link [BeCentered](https://joao4569.github.io/be-centered/)

## Deployment Testing

- Tested all internal and external links, form validation as well as responsivenes of Becentered on deployed site and all are working as intended.

## Credits

- First and foremost I would like to thank my mentor Anthony for his valuable input.
- Code institutes Course material was essential for setting up and deployment.


### Content

- Commit comment conventions were taken from [Cheatography](https://cheatography.com/albelop/cheat-sheets/conventional-commits/), I do not totally understand all the vernacular but tried my best to implement it as best I could.


### Media

- All images sourced from [Pexels](https://www.pexels.com).
