Messaging Integration using Django and Twilio

Source code: https://www.twilio.com/en-us/blog/bulk-sms-service-django-twilio

## It is recommended to run Django in a virtual environment

1. Create virtual environment
    ```
    py -m venv message_integration
    ```
 
2. Activate the virtual environment

    ```
    C:\path\to\your\message_integration>Scripts\activate
    ```

3. Install Django, Twilio, Django-environ

    ```
    (message_integration)C:\path\to\your\message_integration>pip install django twilio django-environ
    ```

    or install all dependecies from requirments.txt

    ```
    pip install -r 'requirements.txt'
    ```

4. Run the server
    ```
    (message_integration)C:\path\to\your\message_integration>py manage.py runserver
    ```

5. Contact me for the .env file in message_integration folder