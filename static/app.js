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
        .then (response => response.json())
        .then (response => {
            // answer key as in python
            let message2 = { name: "Aria", message: response.answer };
            this.messages.push(message2);

            // updates chat text
            this.updateChatText(chatbox)
            textField.value = ''

            // highlight corresponding widget
            let tag = response.tag;
            const plot_options = ["wins", "minutesPlayed", "performance"]
            if (plot_options.includes(tag)) {

                // console.log(tag)
                const plot = document.getElementById("plot");
                plot.innerHTML = "<img src='../static/plots/" + tag + ".png' height='300'></img>"
            }

            tag += '_wid'
            const wid = document.getElementById(tag);
            
            // console.log(tag)
            wid.style.background = "#5B5D6B";
            setTimeout(() => { wid.style.background = "#F3F4F8"; }, 1500);
        })
        .catch((error) => {
            // console.error('oh no, an error:', error);
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

const exists_notification = document.getElementById("username_display");
const matches = document.getElementById("matches");
const minutesPlayed = document.getElementById("minutesPlayed");
const wins = document.getElementById("wins");
const winRate = document.getElementById("winRate");
const kills = document.getElementById("kills");
const kd = document.getElementById("kd");

userName = document.querySelector('.username')
const user = userName.querySelector('input');
        user.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                username = document.getElementById('username').value
                // console.log(username)

                fetch($SCRIPT_ROOT + '/username', {
                        method: 'POST',
                        body: JSON.stringify({ username: username }),
                        mode: 'cors',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                    })

                    // extract json and display
                    .then(response => response.json())
                    .then (response => {
                        exists_notification.innerHTML = response.status;
                        matches.innerHTML = response.matches;
                        minutesPlayed.innerHTML = response.minutesPlayed;
                        wins.innerHTML = response.wins;
                        winRate.innerHTML = response.winRate;
                        kills.innerHTML = response.kills;
                        kd.innerHTML = response.kd;

                        const plot = document.getElementById("plot");
                        plot.innerHTML = "<img src='../static/plots/empty_plot.png' height='300'></img>"
                    })
                

                document.getElementById('username').value = ''
            }
        })


const chatbox = new Chatbox();
chatbox.display();