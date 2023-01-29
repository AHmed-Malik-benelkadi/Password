# Password <hr>
This code is written in Python and uses the tkinter, hashlib and json modules. It was created by Ahmed Malik Ben elkadi.


Its purpose is to check the validity of a password by verifying that it contains at least :

1 number <br>
1 lower case letter<br>
1 capital letter<br>
1 special character<br>
a length of at least 8 characters<br><br>
If the password is valid, it is then hashed using the SHA-256 algorithm and stored in a user dictionary as a hexadecimal string.

The script also uses a function to add passwords to a specific user by checking that they do not already exist for that user.

It also uses dialogs to display error or confirmation messages in case of success.

The user dictionary is stored in a json file named "users.json".




