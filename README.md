# pyusers
Experiments with user registration and authentication in python.

Pyusers is a simple backend implemented in python that allows a user to register with their email and password of choice, after which they receive a confirmation email. Registered users can authenticate with the application by entering their username and password. If they enter a wrong password a certain number of times consecutively, their account will be locked. After a certain configurable amount of time, they will be free to authenticate again.

### Notes and assumptions:
- the project was developed with python 3.7
- in its current form, the project is not so much a backend as a database api, since sessions are not implemented 
- user data is stored in an sqlite database for simplicity
- passwords are encrypted using the PBKDF2 key-derivation function, which has a sliding computational cost. The chosen hashing algorithm is SHA256. With 100000 iterations, the encryption takes ~100ms, which is perfectly acceptable for user authentication and registration, and helps prevent against brute force attacks.
- currently the app only controls for failed logins with invalid passwords

### To do:
- attach a web server to the application
- implement sessions (with cookies for example)
- add an activation link to the confirmation email and route the request back to the application when the link is clicked
- add a check for invalid usernames and increment the failed attempts counter. Only checking wrong passwords exposes which usernames are valid.

### Set up:
Clone the repo
```console
$ git clone https://github.com/lseab/pyusers
$ cd pyusers
```
Create a new virtual environment
```console
$ virtualenv --python=python3.7 pyusers
```
Activate it
```console
$ source pyusers/bin/activate
```
Install the packages
```console
(pyusers) $ make install-test
```
Run the tests with pytest
```console
(pyusers) $ make tests
```
