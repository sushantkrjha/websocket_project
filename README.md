# Django Chat Project

This is a Django-based chat application with basic user authentication functionality. The application allows users to register, log in, log out, and access a chat room after logging in and that allows users to chat in real-time using WebSockets. It uses Django Channels for WebSocket support and Redis as the message broker.

## Features
- **User Registration**: Users can create a new account using the `UserCreationForm` from Django's built-in authentication system.
- **User Login**: Users can log in using their username and password through the `AuthenticationForm`.
- **User Logout**: Users can log out from their session, which redirects them to the login page.
- **Chat Room**: Once logged in, users are redirected to a chat room page where they can interact with other logged-in users.

## Usage

### 1. Registration
- Navigate to [http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/) to create a new account.
- Fill in the required fields (username and password), and click the "Register" button.
- If registration is successful, you will be redirected to the login page.

### 2. Login
- After registering, go to [http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/).
- Enter your username and password and click "Login."
- After a successful login, you will be redirected to the chat page.

### 3. Chat Room
- After logging in, you will be redirected to a chat room page where you can send and receive messages.
- Users have the option to join a different chat room during their session. To do this:
  - Enter the desired chat room name in the input field provided.
  - Click the "Join" button to enter the specified chat room.
  - The chat room will dynamically update with new messages from users in that room.

## How To Use
1. Create a virtual environment (venv)
  - python3 -m venv venv

2. Activate the virtual environment
  - source venv/bin/activate 

3. install Required Dependencies
  - Install the project dependencies using
  - pip install -r requirements.txt

4. Start the Django Development Server
  - Start the Django development server:
  - python manage.py runserver

5. create 2 user - user1, user2 using register api
  - http://127.0.0.1:8000/register/

6. login both the user in 2 seprate tab
  - http://127.0.0.1:8000/accounts/login/

7. Join Room:
  - User1 can join the room created by User2, or
  - User2 can join the room created by User1.

8. Send Messages:
  - Type the message from both tabs.
  - Send the message, and it will be visible to both users.
  - The sender’s name will be displayed alongside each message to show who sent it.