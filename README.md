# small_apps

This is going to be a repo with some small fun apps that I will be creating to improve my skills on Python

## Pomodoro

A simple pomodoro technic clock. Currently is set up to 4 x 25 mins work sessions followed by 5 minutes breaks.

After finishing the forth session your break is 20 min.

TODO: Add sound for the alarm. 

TODO: Adjust the timer based on the user input.


## Password Manager (panager)

A simple password manager built with tkinter in Python. The application allows users to generate strong passwords and store them along with the associated website and username details.

### Features:

1. **Generate Strong Passwords:** The app generates passwords with a mix of letters (both uppercase and lowercase), numbers, and special symbols, ensuring strong password security.
2. **Clipboard Support:** The generated password is automatically copied to the clipboard for easy use.
3. **Save Credentials:** Users can save their website, username, and password details in a text file for easy reference.

### Setup:

#### Prerequisites:

- Python
- tkinter
- pyperclip

#### Installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/georgiosKachrimanis/small_apps
    ```

2. Navigate to the project directory:
    ```bash
    cd [Directory Name]
    ```

3. Install the required modules:
    ```bash
    pip install pyperclip
    ```

4. Run the application:
    ```bash
    python panager.py
    ```

### Usage:

1. **Generating Password:** Click on the "Generate Password" button. A strong password will be generated and displayed in the "Password" field. This password is also copied to your clipboard.
2. **Saving Credentials:** Enter the website and username. Use the generated password or type your own. Click "Add" to save these details to the text file `p422_w0r6.txt`.


