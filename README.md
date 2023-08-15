# Runaway Brewery - Portfolio Project 5 - Full Stack Software Development (E-commerce Applications)

<img src="static/images/README-images/app-resonsiveness.png">

## Live Site

<https://runawaybrewery-d81d6b05c59f.herokuapp.com/>

## Repository

<https://github.com/Kieran132/Runaway>

## Contents

- Project Goals
- UXD - User Experience Design
- Existing Features
 - Home Page
 - Shop
 - About
  - Taproom & Bottle Shop
  - Plan Your Visit
  - Book A Tour
  - Delivery and Collection
  - Trade
 - Contact
 - My Account
  - Log In/ Log Out
  - Sign uUp
  - My Profile
  - Wishlist
 - Shopping bag
 - Checkout
- Technologies Used
- Testing
- Deployment
- Credits

---

## Project Goals

Runaway Brewery is my fifth project as part of the Code Institute Full Stack Web Developer Course.

Runaway Brewery is an already existing company that has been trading for over 6 years now and has currently moved into a bigger premises, so expanding in both customer facing trade and also cask/keg selling trade. They came to me and asked if I could revap their current website as they used spotify templating and was not to their like or design.
With this app the user get a brief intro in the style of beer runaway make and a brief introduction to their ethos and what they do. Further into the app, the user is able to purchase the beer through a working checkout, the user can find more information about the brewery and where to find them, they are able to book tours with which the email is sent to both the logged in user and Runaway itself. In addition to this, the user has a profile which shows previous purchase history and enables the user to add products to their wishlist for future reference.

---

## UXD - User Experience Design

When designing and creating this project it was important to keep the user experience at the forefront of everything. This was achieved by breaking the project down into 5 planes;

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

---

## Strategy Plane

In this design phase, I had discussion with the people at Runaway Brewery to outline what sort of app they were looking for. We discussed colours, ease of use and what type on information should be accessible.

<u> Prodject Objectives </u>

- Take their existing website as reference
- Apply clean, more personal design to their website
- Allows for CRUD functionality for admin users

<u> Users and User Needs </u>

- Beer lovers looking for their next place to visit
- Easy and simple navigation through the app
- Simple understanding of what the app is about and its uses

---

## Scope Plane

For the Scope Plane, I outlined the features I think would best suit the project and the design. With this I relayed this back to Runaway for feedback and any changes they wanted to make.

<u> Features </u>

- Homepage
- Shop - allowed for filtering and searching
- Abouts page - covered all information about Runaway and ability to Book a Tour
- Contact Page
- Accounts tab - allowed for user profile, wishlist
- Authentication levels throughout the website depending on the user

---

## Structure Plane

Here at the Structure Plane, this is where I outlined the design colours, fonts and the building blocks of the project

<u> Colors </u>

<img src="static/images/README-images/colour-palette.png">

The main color that wanted to be used was Keppel, as this was the main color used within the logo of Runaway. This color is used for the logo, the nav bar heading tabs and the information in the footer.
To contrast this blue-ish color, I went for a yellow/mustard as main button color and also the background for the banner on the hompage. This color is very bold and eyecatching. 
For button hover color the red orange I thought contrasted very well with the yellow as it is inline with eachother
For the main background color of body, header and footer the Eggshell was used. This was because its slight off white which helps make all the other colors stand out and not clash.

<u> Fonts </u>

For H1, H2 tags I decided to use Oswald. I feel it is very clean, crisp looking font

For the body of the project I decided to use Roboto. It is very similar to Oswald but I felt that it was better suited for body of the app.

<u> Key Models </u>

-  User Authentication

- Allauth creates user profile and determins the depth of authentication within the app

- Appointment
    
    - Allows only signed in user to be able to book a tour around the brewery
    - Upon submission, time is saved and removed from any other users selecting that time
    - Email is sent to both the users email and Runaway

- Checkout

    - Allows any user to process payment of their chosen purchased items
    - Shows item added to bag within the shopping cart

- Contact

    - Shows user contact form which submits the form and information is sent to Runaway

- Wishlist

    - Allows for users to add products to their own wishlist page for future reference
    - These can be deleted by the user

- Profile

    - Profile is created with the users information which is used around the app
    - The user can update and amend their profile

- Shop

    - Shows all the products that Runaway has to offer
    - Authorised admin are able to add, edit and delete products without using the admin panel
    - User can sort items within the shop 
    - Ability to select only certain products, instead of viewing all of them

---

## Skeleton Plane

#### Home Page

From the beginning, I wanted the home page to be a certain way and have similarities to the home page Runaway already has as I felt this is something they liked and wanted. I wanted to add some images of the products they have recently created at the top of the page to showcase to people visiting the app. Then following down the page add brief and informative text about Runaway. Keeping the page vibrant, engaging and also to the point.

<img src="static/images/wireframes/home-wire.png">

#### Shop Page 

I wanted this page to be simple, clear and easy for the user. I felt there is nothing more annoying than having a page that is difficult to navigate and use for a simple task. Therefore, I went for a 3 row layout for the products within a card tag with image, title of the product, a button to take the user a detail page and the price.

<img src="static/images/wireframes/shop-wire.png">

#### Contact Page

For the contact page, I wanted to create a simple form that was easy to understand for the user and one which allowed the user to submit only the neccessary field - name, email address and message. In addition, I wanted to add google maps function so the user could physically see the location of Runaway

<img src="static/images/wireframes/contact-wire.png">

#### About Page

For this page, I decided to keep all the information about Runaway all in one easily accessible tab, that broke down into different areas. Most of this information would come from the already existing website as this is what they wanted.

<img src="static/images/wireframes/about-wire.png">

#### Booking Page

Runaway offer tours around their brewery to the public, however this is done via an external company using their product and api, which mean added costs. I felt it would be easier and more efficient to keep this all in house and for the app to do the work for them without them having to out-source this. I wanted very simple and easy way of booking that sent out relevant information to both parties.

<img src="static/images/wireframes/booking-wire.png">

