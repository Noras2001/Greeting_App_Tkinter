# Simple Greeting Application with Tkinter

This repository contains a Python script that creates a simple graphical user interface (GUI) using `tkinter`. The application asks the user to input their name and then displays a personalized greeting.

## Project Overview

The application creates a small window using the `tkinter` library, where the user can enter their name and click a button to receive a greeting.

### Features

- **Text Input**: The user can enter their name in an input field.
- **Button Interaction**: Upon clicking the button, the program reads the entered name and displays a personalized greeting.
- **Dynamic Label Update**: The greeting message is updated dynamically in the same window.

## How to Run

1. Install the required dependencies (if you don't have Tkinter installed already):
   ```bash
   pip install tk
   ```

2. Run the script:
   ```bash
   python greeting_app.py
   ```

This will open the application window where you can interact with the greeting feature.

## Example Output

When the user enters their name and clicks the "Pоприветствовать" button, the window will display a greeting like:

```
Привет, [Name]!
```

Where `[Name]` is the name entered by the user.

## How It Works

1. The script creates the main window using `tk.Tk()`.
2. It defines a function `greet()` that retrieves the name entered in the text field and updates a label with the greeting.
3. Widgets for the label, entry field, and button are created and arranged in the window using the `.pack()` method.
4. The main loop (`root.mainloop()`) starts the application, keeping the window open for interaction.

## License

This project is licensed under the MIT License.


