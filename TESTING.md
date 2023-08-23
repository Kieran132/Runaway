# Testing for Runaway Full Stack Development Project
---

## User Stories

#### Regular Site User Stories

- As a user, I am looking for their next place to visit as I enjoy new and exciting beers
    - Clear product images at top of the home page
    - Home page is informative but not overwhelming to read
    - The home page encourages the User to learn more

    <img src="static/images/README-images/index-top-images.png">

- As a user, I want the app to be easy and simple navigation through the app
    - The navigation bar is clear, and dropdown title links are representative of what the pages are informing the user about
    - All the buttons are bright, and bold and direct the user to the correct pages

    <img src="static/images/README-images/navbar.png">

- As a user, I want a simple understanding of what the app is about and its uses
    - How the app is laid out, it is clear where the user would need to go to get their desired outcome. Shop provides all the products and highlights 
      how the user can purchase. Contact Navigation button takes the user to a contact form page which is easy to input and submit.

#### Customer User Stories 

- As a customer, I want to be able to purchase products easily
    - Implementing a stripe with the checkout function enables an easy purchasing process. Starting from the shop the customer can view the 
      product in more detail. Then if desired, the customer can add to the shopping bag. From there, there is a button to direct the user to checkout with a form and input directions for the customer to complete their purchase. Finished off with purchase confirmation notification and email.#

- As a customer, I want a shop overview and a chance to view the product in more detail
    - Navigating to the shop page, each product card has a clear, bright button which will direct the customer to the product detail page. This is where 
      the customer can read more information on that product and choose to either add the product to the shopping bag or continue shopping.

      <img src="static/images/README-images/shop-about.png">

- As a customer, I want to be able to view my shopping bag and adjust accordingly
    - Once the customer has added product to their shoppinh bag, they will see a pop up message notifying them it has been done successfully. In the 
      navigation bar alongside the cart icon, the total of the shopping bag is shown to the customer. Clicking on either the icon or total amount, direct the customer to the shopping bag page. Here the customer can see their chosen products and update the quantity accordingly. This change is reflected in the grand total.

      <img src="static/images/README-images/shopping-bag.png">

#### Logged In Customer Stories

- As a logged-in user, I want the site to save my details
    - As a logged in user, within the account navigation bar heading, there is a dropdown link to the users profile. Here the user will be able to see 
      their saved details and update them is need be.

      <img src="static/images/README-images/profile-details.png">

- As a logged-in user, I want the ability to view previous order history
    - As mentioned in the point above, within the users profile page in addition to their details, the user will also be able to see their previous     
      order history. If the user clicks on the order number, it will direct them to that orders confirmation page with all the information.

      <img src="static/images/README-images/profile-order-history.png">

- As a logged-in user, I want email confirmation when booking a tour.
    - Once the user has selected the date and time of their tour and submitted, they will receive and email (from their saved details) and also an email 
      will be sent to Runaway confirming this tour.

      <img src="static/images/booking-confirmation.png">

### Manual Testing

#### Navigation Bar

- The navigation bar is fully responsive on all resolutions
- All tab headings redirect to the correct pages
- Aulauth verification is correctly working by showing sign-up/login before logging in and My profile/Log-out/Wishlist once signed in

#### Footer

- Font Awesome links correctly redirect to social media pages
- Links open in a new browser
- Fully responsive on all screen sizes

#### Shop

- The product cards all are even in size and spacing
- Sort drop-down correctly works depending on how the user sorts the page
- Data within the product cards is correct from cross-referencing with the database
- Age Verification pop-up shows for any user to authenticate age

#### Shop Details

- View details on shop.html correctly redirects to the view details page with the correct information
- All buttons showing if the User is logged in
- Only select buttons show when no user is logged in
- Plus/Minus for quantity selection correctly works 
- Size drop-down correctly works for t-shirt product

#### Wishlist

- Correct product is added to wishlist
- Pop-up messages correctly show depending on user task - add/delete/product already exists
- Only shows when the user has logged in

#### Shopping Bag

- Quantity plus/minus correctly works
- Product can be updated and deleted correctly
- Correct information is present (with size if chosen)
- Price/total price is correct
- Add an item to the bag with the correct information that appears
- The shopping cart in the navigation bar correctly redirects the user to the shopping bag page
- If no products are present, a button correctly redirects to shop.html

#### Checkout

- Checkout shows the correct product/quantity/price
- If the user has saved information this is present
- Update user information also correctly works
- Form responds to invalid inputs

---
### Validation

#### W3C HTML Validator

- 0 Errors
- 0 Warnings

#### W3C CSS Validator

- 0 Errors
- 5 Warnings
    - These warnings are about an unknown vendor extension that is added by CSS Autoprefixer for cross-browser support.

#### Jshint and Javascript Validator

- Swal is an undefined variable as this is used for SweetAlert Pop up messages throughout the app
- The Google map script gives 1 warning and has 1 undefined variable. However, this comes from Google Maps API Documentation
- Stripe Javascript is provided by the Stripe Documentation

#### Pep8

- All code written by myself adhered to Pep8 Validation

#### Color Contrast Validation

I put my project through color contrast validator to ensure that the colors used were accessible to everyone. However initially two errors came up, image below: 

<img src="static/images/README-images/color-contrast-validator issue.png">

To resolve this I amended the color accordingly which resulted in a pass, images below:

<img src="static/images/README-images/color-contrast-ammended.png">

<img src="static/images/README-images/color-contrast-ammended-2.png">

---
### Bugs/Issues and Resolutions

#### Gmail SMTP

When setting up email confirmation throughout the project, I came across an issue when submitting the contact form. The information inputted by the user (name, email address, and message) was not being sent to the terminal. 

Resolution:

Within my env.py file, I did not set the email password to one given by Google App Passwords. To obtain this password I did the following:
- Logged into Google account
- Turned off 2-step Verification
- Searched for App Passwords
- First Dropdown selected Gmail
- Second Dropdown inputted App Name
- App password is copied and added to the env.py file

#### Booked Tour Time Not Showing On Booking_Success.html

Initially set up the function to be able to book a tour by selecting a day and time so when the user clicked submit, this information carried on over to a confirmation page outlining what the user has booked. The type of booking (Tour) and the day the user selected showed, however the time the User selected was not showing.

Resolution:

The function was not retrieving the time the user submitted. To resolve this I added:

    time = request.POST.get('time')

This addition to the function was able to retrieve the missing information

#### Static File Root

All of my images initially were not showing after setting up AWS as the database for all media and static files.

Resolution:

    {% static '`file path name`' %}

#### Sweet Alert Script Source Tag

As a few of my HTML pages have pop-up messages showing to the user, it was best to create an include folder to store the HTML script files to keep the pages clean and not overcrowded. Initially, it was:

    {% include '/workspace/Runaway/shop/templates/includes/quantity_input_script.html' %}

However this was not finding the file as the file path was incorrect, it should be:

    {% include 'shop/templates/includes/quantity_input_script.html' %}

#### Shop Images

I had a could of bugs/issues with the images on the shop pages.

Firstly, the if statement to show images started with src="{{ product. image.url }}. However, this was not calling the image as the for loop was stated as {% for item in bag_items %}.

Resolution:

    src="{{ item.product.image.url }}

The second bug/issue I had was when the Admin User didn't select an image when adding a new product, no image was showing.

Resolution:

    src="{% static 'images/no-image-icon.png' %}

This followed on from the previous issue with adding static as the file path.

#### User Checkout

When the user checked out with a certain product that equated to less than the delivery cost the overall price was in the negatives giving this error:
 
    InvalidRequestError at /checkout/
    Request req_yIdnbCAG1kBEjq: This value must be greater than or equal to 1.

This was because within me bag/context.py file it had this: `if total < settings. FREE_DELIVERY_THRESHOLD:`

Resolution:

    if total < settings. FREE_DELIVERY_THRESHOLD:

And also added: 
    
    delivery = round(
            total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100), 2)

This meant that the total amount would be rounded up to the nearest two decimal places.