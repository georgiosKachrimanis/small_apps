<h1> small_apps </h1>

This is going to be a repo with some small fun apps that I will be creating to improve my skills on Python

# Pomodoro Timer

TODO: Add alarm sounds :) 

A user-friendly Pomodoro Timer built with tkinter in Python to help you manage your time effectively. Utilizing the Pomodoro technique, this application encourages you to work for set periods and then take short or long breaks, increasing productivity.

## Features:

1. **Preset Timers:** The app uses the classic Pomodoro timing: 
   - 25 minutes of focused work.
   - 5-minute short break.
   - 20-minute long break after four work sessions.
  
2. **Visual Feedback:** The timer displays a countdown, and the app provides visual feedback indicating the number of completed work sessions.
  
3. **Customizable Appearance:** Utilizing pleasing colors and a straightforward interface, the app is designed to provide a motivating environment for users.

4. **Intuitive Controls:** Start, pause, or reset the timer with one click.

## Setup:

### Prerequisites:

- Python
- tkinter

### Installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/georgiosKachrimanis/small_apps/tree/main/pomodoro
    ```

2. Navigate to the project directory:
    ```bash
    cd [Directory Name]
    ```

3. Run the application:
    ```bash
    python pomodoro.py
    ```

## Usage:

1. **Starting a Session:** Click the "Start" button to begin a work session.
2. **Taking a Break:** After completing a work session, the app will automatically start a short break timer. After four work sessions, a long break timer will start.
3. **Resetting the Timer:** To reset the timer and session count, click the "Reset" button.

# -----------------------------------------------------

## Password Manager (panager)

TODO: Create an encryption mechanism for the stored passwords!

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
    git clone https://github.com/georgiosKachrimanis/small_apps/tree/main/panager
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


