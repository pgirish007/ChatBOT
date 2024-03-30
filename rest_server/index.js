const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors'); // Import cors middleware
const cron = require('node-cron');
const NodeCache = require('node-cache');
const Message = require('./models/Message');


const app = express();
const port = 3001;

app.use(cors()); // Enable CORS for all routes
app.use(bodyParser.json());

// Create a new cache instance with a default TTL of 24 hours (in seconds)
const cache = new NodeCache({ stdTTL: 24 * 60 * 60 });

// Schedule task to run every 6 hours
cron.schedule('0 */6 * * *', async () => {
  try {
    // Implement your task here
    console.log('Task executed successfully');
  } catch (error) {
    console.error('Error executing task:', error);
  }
});


// REST API endpoint to get all messages
app.get('/api/messages', async (req, res) => {
  try {
    let messages = cache.get('messages'); // Try to retrieve messages from cache
    if (!messages) {
      // If messages are not in cache, fetch from the database
      messages = await Message.find().sort({ createdAt: 'asc' });
      // Store messages in cache with a TTL of 24 hours
      cache.set('messages', messages);
    }
    res.json({ messages });
  } catch (error) {
    console.error('Error fetching messages:', error);
    res.status(500).json({ error: 'An error occurred while fetching messages' });
  }
});


// Example POST endpoint to save message
app.post('/api/messages', async (req, res) => {
  const { text, sender } = req.body;
  const message = new Message({ text, sender });
  try {
    await message.save();
    // Clear cache after saving new message
    cache.del('messages');
    res.status(201).json({ message: 'Message saved successfully' });
  } catch (error) {
    console.error('Error saving message:', error);
    res.status(500).json({ error: 'An error occurred while saving the message' });
  }
});

app.post('/msg', (req, res) => {
  const { message } = req.body;
  const responseMessage = 'Hello';
  res.json({ message: responseMessage });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});

/*
this is in case we call Oracle database
const express = require('express');
const bodyParser = require('body-parser');
const oracledb = require('oracledb');

const app = express();
const port = 3001;

// Database connection configuration
const dbConfig = {
  user: 'your_username',
  password: 'your_password',
  connectString: 'oracle://localhost:1521/orcl'
};

// Middleware
app.use(bodyParser.json());

// API endpoint to handle user messages
app.post('/messages', async (req, res) => {
  const { message } = req.body;

  // Establish a database connection
  let connection;
  try {
    connection = await oracledb.getConnection(dbConfig);

    // Execute a query (replace 'your_query' with your actual SQL query)
    const result = await connection.execute('your_query', [message]);

    // Assuming your query returns a single row with a 'response' column
    const responseMessage = result.rows[0][0];

    res.json({ message: responseMessage });
  } catch (error) {
    console.error('Error executing query:', error);
    res.status(500).json({ error: 'An error occurred while processing your request' });
  } finally {
    // Close the database connection
    if (connection) {
      try {
        await connection.close();
      } catch (error) {
        console.error('Error closing connection:', error);
      }
    }
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});


*/