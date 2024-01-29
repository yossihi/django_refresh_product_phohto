# Django Product Management Web Application

This is a simple web application built with Django and Bootstrap for managing products. Users can register, log in, add products with descriptions, prices, and images, view their own products, and delete products.

## Features

- **User Authentication:** Users can register and log in securely using JWT (JSON Web Token) for authentication.

- **Product Management:** Users can add products with descriptions, prices, and images. They can also view a list of their own products and delete products.

- **Responsive UI:** The user interface is designed using Bootstrap, making it responsive and user-friendly.

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/django-product-management.git
   cd django-product-management

2. **Create Virtual Environment:**

    ```bash
    python -m venv venv

3. **Activate Virtual Environment:**

    ### On Windows:
        venv\Scripts\activate

    ### On macOS/Linux:
        source venv/bin/activate

4. **Install Dependencies:**

        pip install -r requirements.txt

5. **Apply Database Migrations:**

        python manage.py migrate

6. **Run the Development Server:**

        python manage.py runserver

The application will be accessible at http://127.0.0.1:8000/.

# Usage
## Register:

 - Open the application in your web browser.
- Click on the "Log In" button to go to the login page.
- If you don't have an account, click on the "Register" link to create a new account.
- Fill in the registration form with your username, email, and password.
- After registration, you will be redirected to the login page.

## Log In:

 - Use your registered username and password to log in.

## Add Products:

 - On the protected page, you can add products using the provided form.
 - Enter the product description, price, and choose an image file.
 - Click the "Add Product" button to submit the form.

## View Products:

 - The added products will be displayed on the page with their details.
 - You can see the product ID, description, price, and the time it was created.
 - Each product card also includes a "Del" button to delete the respective product.
## Delete Products:

 - Click the "Del" button on a product card to delete that product.
 - The product will be removed from the list.

## Technologies Used
 - Django
 - Bootstrap
 - JavaScript (Axios for API requests)

### Notes
 - This application uses JWT for authentication, and the tokens are stored in the browser's local storage.
The user interface is responsive, making it suitable for various screen sizes.
 - Feel free to explore, modify, and enhance the application according to your requirements. If you encounter any issues or have suggestions, please let us know!
