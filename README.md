# DjangoAuthVerifyWithEmail

DjangoAuthVerifyWithEmail is a web application with Django that allows users to createAccount and Login as User. It provides a simple and user-friendly interface to create account and Login.


## Getting Started

1. Clone the repository:

   ```
   git clone https://github.com/RajaulAnsari/DjangoAuthVerifyWithEmail.git
   
2. Navigate to the project directory:

   ```
   cd DjangoAuthVerifyWithEmail

3. Create a virtual environment (optional but recommended):

   ```
   python -m venv venv

4. Activate the virtual environment:
    * On Windows:
      ```
      venv\Scripts\activate

     * On macOs/Linux
       ```
       source venv/bin/activate

5. Install dependencies:

   ```
   pip install django
   pip install mysqlclient
6. Appply changes in setting.py
* For Database
   ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabasename',   #use your database name
        'USER':'root',
        'PASSWORD':'mydatabasepassword', #use your database password
        'HOST':'localhost',
        'PORT':'3306'
       }
   }

* For Email
   ```
   EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
   EMAIL_HOST = 'smtp.gmail.com'  # Set your email host
   EMAIL_PORT = 587
   EMAIL_USE_TLS = True
   EMAIL_HOST_USER = 'example@gmail.com'  # Set your email address
   EMAIL_HOST_PASSWORD = 'generated app password here'  # Set your email app password

6. Apply database migrations:

   ```
      python manage.py makemigrations
      python manage.py migrate

7. Run the development server:

   ```
   python manage.py runserver

  The application will be accessible at http://127.0.0.1:8000/.
 

## Contact

If you have any questions or need further assistance, you can contact the repository owner [here](mailto:ansarimdrajaul2@gmail.com).

*Note: You can modify your code as needed...*

## Thanks For Your Interest
