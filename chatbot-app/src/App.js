import React, { useState, useEffect } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  let [messages, setMessages] = useState(JSON.parse(localStorage.getItem('chatMessages')) || []);
  let [inputValue, setInputValue] = useState('');

  useEffect(() => {
    // Load chat history from local storage when component mounts
    const storedMessages = localStorage.getItem('chatMessages');
    if (storedMessages) {
      setMessages(JSON.parse(storedMessages));
    }
  }, []); // Empty dependency array ensures the effect runs only once

  // Update local storage whenever messages state changes
  useEffect(() => {
    localStorage.setItem('chatMessages', JSON.stringify(messages));
  }, [messages]);

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleClearStorage = () => {
    while (messages.length <=0) {
      messages.pop();
    }
    localStorage.removeItem("chatMessages")
    console.log(localStorage.length);
    const divElement = document.getElementById('messagesContainer');
    divElement.innerHTML='';
  };

  const handleSendMessage = () => {
    if (inputValue.trim() !== '') {
      // Add user message to the chat
      //setMessages([...messages, { text: inputValue, sender: 'user' }]);
      
      // Make an API call to send user input to the server
      axios.post('http://localhost:3001/msg', {
        message: inputValue
      })
      .then(response => {
        // Handle successful response from the server
        const botResponse = response.data.message;
        setMessages([...messages, { text: botResponse, sender: 'bot' }]);
      })
      .catch(error => {
        // Handle error from the server
        console.error('Error sending message to server:', error);
      });

      // Clear input field
      setInputValue('');
    }
  };

  return (
    <div className="App">
      <div className="chat-container">
        <div id="messagesContainer" className="messages">
          {messages.length > 0 && messages.map((message, index) => (
              <div key={index} className={`message ${message.sender}`}>
                {message.text}
              </div>
          ))}
        </div>
        <div className="input-container">
          <input
            type="text"
            placeholder="Type a message..."
            value={inputValue}
            onChange={handleInputChange}
            onKeyPress={(event) => {
              if (event.key === 'Enter') {
                handleSendMessage();
              }
            }}
          />
          <button onClick={handleSendMessage}>Send</button>
          <button onClick={handleClearStorage}>Clear</button>
        </div>
      </div>
    </div>
  );
}

export default App;