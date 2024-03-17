See "Home/No-Breach/Yes-Breach.png" For a Working-Demo

Password Breach Checker

---

_Introduction_

The Password Breach Checker is a Python program that allows you to check if a password has been breached using the Pwned Passwords API. It helps you assess the security of your passwords and identify if they have been compromised in any known data breaches.

---

_Installation_

Before running the program, ensure you have the required dependencies installed. You can install them using pip:

    pip install requests
    pip install hashlib

---

_Usage_

1. Clone or download the project to your local machine.
2. Navigate to the project directory.
3. Run the program in your Python environment using the following command:

   python app.py

4. The program will start a local Flask server and display a message like "\* Running on http://127.0.0.1:5000/". This means the server is running.

5. Open your web browser and visit the following URL to access the Password Breach Checker web page:

   http://127.0.0.1:5000/

6. On the web page, enter the password you want to check and click the "Check Breach" button.

7. The program will query the Pwned Passwords API and display the breach status of the password on the same webpage.

---

_Functionality_

The program uses the Pwned Passwords API to check if the password has been breached. It performs a secure hash of the password using the SHA-1 algorithm and sends the first five characters of the hash to the Pwned Passwords API. The API returns a list of hashes that match those initial characters. The program then checks if the password hash suffix exists in the response, which indicates a breach.

---

_Disclaimer_

Please note that this program is intended for educational purposes and personal use. It does not store any passwords or breach data. However, it relies on third-party APIs for checking breach status, and there may be limitations or changes to these APIs over time. Use this program responsibly and at your own risk.

---

_Dependencies_

1. requests: This library is used for making HTTP requests to the Pwned Passwords API.
2. hashlib: This library is used for hashing passwords securely.

---

_Credits_

The Password Breach Checker program was created by Hadi Khamsi. The original concept and code for checking the breach status of passwords come from various sources, including the Pwned Passwords API.

For more information about the Pwned Passwords API and its usage terms, visit https://haveibeenpwned.com/API/v3#PwnedPasswords.

Thank you for using my Password Breach Checker!
