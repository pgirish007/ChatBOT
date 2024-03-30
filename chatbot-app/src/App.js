import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSendMessage = () => {
    if (inputValue.trim() !== '') {
      // Add user message to the chat
      setMessages([...messages, { text: inputValue, sender: 'user' }]);
      
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
        <div className="messages">
          {messages.map((message, index) => (
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
        </div>
      </div>
    </div>
  );
}

export default App;