import cx_Oracle
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Connect to Oracle database
connection = cx_Oracle.connect("username", "password", "hostname:port/service_name")

# Retrieve data from the employee table
query = "SELECT salary, date_of_birth FROM employee"
data = pd.read_sql(query, con=connection)

# Close the connection
connection.close()

# Preprocess the data
# Feature scaling for salary
scaler_salary = MinMaxScaler()
data['scaled_salary'] = scaler_salary.fit_transform(data[['salary']])

# Convert date_of_birth to age and scale
current_year = 2024  # Update with the current year
data['date_of_birth'] = pd.to_datetime(data['date_of_birth'])
data['age'] = current_year - data['date_of_birth'].dt.year
scaler_age = MinMaxScaler()
data['scaled_age'] = scaler_age.fit_transform(data[['age']])

# Calculate bonus based on age gap
bonus_percent_increment = 0.05
bonus_age_gap = 5
data['bonus_percent'] = (data['age'] // bonus_age_gap) * bonus_percent_increment

# Create sequences for LSTM input
def create_sequences(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i+seq_length])
        y.append(data[i+seq_length])
    return np.array(X), np.array(y)

sequence_length = 10  # Adjust according to your data and problem
X, y = create_sequences(data[['scaled_salary', 'scaled_age', 'bonus_percent']].values, sequence_length)

# Split data into train and test sets
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Reshape input to be 3D [samples, timesteps, features]
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 3))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 3))

# Build LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(sequence_length, 3)))
model.add(Dense(3))  # Output dimension adjusted to match features
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

# Predictions
predictions = model.predict(X_test)

# Inverse transform predictions to get actual values
predictions_actual = np.concatenate((predictions, X_test[:, :, 2].reshape(-1, 1)), axis=1)
predictions_actual = np.concatenate((predictions_actual[:, :, :2], scaler_salary.inverse_transform(predictions_actual[:, :, :1]), predictions_actual[:, :, 2:]), axis=1)

# Plotting
plt.figure(figsize=(14, 7))

plt.plot(predictions_actual[:, :, 0], label='Predicted Salary', linestyle='--')
plt.plot(predictions_actual[:, :, 1], label='Predicted Age', linestyle='--')
plt.plot(predictions_actual[:, :, 2], label='Bonus Percentage', linestyle='--')

plt.xlabel('Time Step')
plt.ylabel('Value')
plt.title('Predicted Salary, Age, and Bonus Percentage over Time')
plt.legend()
plt.grid(True)
plt.show()
