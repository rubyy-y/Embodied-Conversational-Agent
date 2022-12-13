class Chatbox {
    constructor() {
        this.args = {
            // correspond to class names in base.html;
            // gives whole div under this classname; access
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        // in the beginning chat window closed
        this.state = false;
        this.messages = [];
    }


    display() {
        const {openButton, chatBox, sendButton} = this.args;

        // click on open button toggles state
        openButton.addEventListener('click', () => this.toggleState(chatBox))

        // click on send sends message
        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        // also listen to keys: enter sends
        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }


    toggleState(chatbox) {
        // change state
        this.state = !this.state;

        // in css file - if yes: opacity 1, else: 0 (invisible)
        if (this.state) {
            chatbox.classList.add('chatbox--active')
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    
    onSendButton(chatbox) {
        // extract input text
        var textField = chatbox.querySelector('input');
        let text1 = textField.value

        // if text is empty
        if (text1 === "") {
            return;
        }

        // send text to bot as dict (object in js)
        // message key is same as in app.py
        let message1 = { name: "User", message: text1 };
        this.messages.push(message1);

        // hardcode: http://127.0.0.1:5000/predict
        // predict function with predict route in app.py

        fetch($SCRIPT_ROOT + '/predict', {
        //fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
        // extract json and display
        .then (r => r.json())
        .then (r => {
            // answer key as in python
            let message2 = { name: "Aria", message: r.answer };
            this.messages.push(message2);

            // updates chat text
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('oh no, an error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
        });
    }

    updateChatText(chatbox) {
        var html = '';

        // go over all messages and modify inner html code
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Aria")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }

}

userName = document.querySelector('.username')
const user = userName.querySelector('input');
        user.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                username = document.getElementById('username').value
                console.log(username)
                document.getElementById('username').value = ''
            }
        })

const chatbox = new Chatbox();
chatbox.display();