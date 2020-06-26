# Instruction
1. Clone repository 
    - `$ git clone https://github.com/victormura/ChatAPI.git`
    - `$ cd ChatAPI`
2. Create and activate a virtual environment 
    - `$ python3 -m venv venv`
    - *Mac/Linux* `$ source venv/bin/activate` 
    or `$ source venv/Scripts/activate` *Bash on Windows*
3. Install packages `$ pip install -r requirements.txt`
4. Migrate database `$ python manage.py migrate`
5. Run app `$ python manage.py runserver`
6. Open app *http://127.0.0.1:8000/*

## API interface

- *GET* **/v1/messages/** - return all messages
- *GET* **/v1/messages/?chat={chat_id}** - return chat messages
- *POST* **/v1/messages/** - send message in chat

- *POST* **/v1/group_chat/** - create a new group chat
- *POST* **/v1/group_chat/{chat_id}/participants/** - Add a new participant to the group chat
- *DELETE* **/v1/group_chat/{chat_id}/participants/{user_id}/** - Remove user from group chat



    