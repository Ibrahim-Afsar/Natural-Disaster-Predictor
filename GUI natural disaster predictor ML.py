import tkinter as tk
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Provide the Data
data = {
    "disaster": ["flood", "hurricane", "earthquake", "drought", "wildfire", "tornado", "tsunami", "thunderstorm"],
    "rainfall": [5, 10, 0, 0.1, 0, 0, 10, 2],
    "temperature": [20, 25, 15, 30, 35, 20, 15, 25],
    "humidity": [85, 80, 50, 10, 25, 70, 65, 88],
    "wind_speed": [15, 20, 0, 5, 15, 30, 0, 20],
    "atmospheric_pressure": [1010, 1005, 0, 1020, 1015, 1000, 0, 1012],
    "sea_level": [1, 2, 0, 0, 0, 0, 3, 0],
    "richter_scale_magnitude": [0, 0, 5, 0, 0, 0, 8, 0],
    "depth": [0, 0, 10, 0, 0, 0, 50, 0],
    "precipitation": [5, 10, 0, 0.1, 0, 1, 0, 3],
    "lightning_strikes": [0, 0, 0, 0, 2, 5, 0, 8]
}

# Load the dataset
df = pd.DataFrame(data)

# Prepare the training data.
X_train = df.drop("disaster", axis=1)
y_train = df["disaster"]

# Create a logistic regression model.
model = LogisticRegression()

# Train the model using the training data.
model.fit(X_train, y_train)

# Create the main window
window = tk.Tk()
window.title("Natural Disaster Predictor")

# Frame for the title
frame_1 = tk.Frame(window)
frame_1.grid(row=0, column=0)

# Title label
label_1 = tk.Label(frame_1, text="Natural Disaster Predictor", fg="black", font=("Sitka small", 30))
label_1.grid(row=0, column=0)

# Frame for instructions
frame_2 = tk.Frame(window)
frame_2.grid(row=1, column=0)

# Instruction label
label_2 = tk.Label(frame_2, text="Please enter the following correctly to get an accurate result:-",font=("Sitka small", 15))
label_2.grid(row=1, column=0)

# Frame for input fields
frame_3 = tk.Frame(window)
frame_3.grid(row=2, column=0, sticky="W")

# Create input labels and entry fields
tk.Label(frame_3, text="").grid(row=0, column=0)  # Empty space
input_variables = ("rainfall:", "temperature:", "humidity:", "wind speed:", "atmospheric pressure:", "sea level:", "richter scale magnitude:", "depth:", "precipitation:", "lightning strikes:")
entries = []

for i, variable in enumerate(input_variables, start=1):
    tk.Label(frame_3, text=variable, font=("Sitka Small", 12)).grid(row=i, column=0, sticky="W")
    entry = tk.Entry(frame_3, width=10, font=('Sitka Subheading', 12))
    entry.grid(row=i, column=1, sticky="W")
    entries.append(entry)

tk.Label(frame_3, text="").grid(row=len(input_variables) + 1, column=0)  # Empty space

# Function to predict natural disaster based on input
def predict():
    variables = []
    for entry in entries:
        value = entry.get()
        if value.isdigit():
            variables.append(int(value))
        else:
            variables.append(0)  # Default to 0 if input is not valid
    # Make prediction using the model
    prediction = model.predict([variables])
    # Display prediction
    tk.Label(text=f"{prediction} is the most likely natural disaster to happen", font=("Sitka Small", 15)).grid(row=3, column=0, sticky="W")

# Submit button
submit_button = tk.Button(frame_3, text="Submit", width="11", height="2", fg="White", bg="Blue", command=predict)
submit_button.grid(row=len(input_variables) + 2, column=1)

# Run the main loop
window.mainloop()