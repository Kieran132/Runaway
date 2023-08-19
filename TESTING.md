# Testing for Runaway Full Stack Development Project
---
### Manual Testing


---
### Validation

#### W3C HTML Validator

- 0 Errors
- 0 Warnings

#### W3C CSS Validator

- 0 Errors
- 5 Warnings
    - These warnings are in relation to a unknown vendor extentions that are added by CSS Autoprefixer for cross browser support.

#### Jshint and Javascript Validator

- Swal is an undefined variable as this is used for SweetAlert Pop up messages throughout the app
- The google map script gives 1 warning and has 1 undefined variable. However this comes from Google Maps Api Documentation
- Stripe Javacript is provided by the Stripe Documentation

#### Pep8

- All code written by myself adhired to Pep8 Validation

---
### Bugs/Issues and Resolutions