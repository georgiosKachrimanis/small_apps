# Flash Cards Application (WordCard)

A simple flashcards application built using `tkinter` for GUI and `pandas` for data handling. The application displays flashcards with words from one language on one side and their translations on the other. I created this app, because I am really bad at learning languages. I hope it will help you as much as it helped me!

## Features:

1. **Randomized Flashcards:** Flashcards are selected at random each time.
2. **Flipping Effect:** Flashcards automatically flip after 3 seconds to display the answer.
3. **Learning Progress:** Known words can be marked and will be removed from future sessions.

## Prerequisites

- Python 3
- tkinter
- pandas

## How to Run

1. Clone the repository.
2. Navigate to the directory where the script is located.
3. Run the script:
    ```bash
    python3 wordcard.py
    ```

## How it Works

1. On starting the application, the program tries to load a file `words_need_to_learn.csv` which contains words that the user hasn't learned yet.
2. If the above file is not found, it loads `Nederalnds_English_5k.csv` which contains 5,000 Dutch to English word pairs.
3. The user is presented with a word in Dutch on the front side of the flashcard.
4. After 3 seconds, the card flips to show the English translation.
5. The user can then indicate if they already know the word or not.
6. If the word is marked as known, it gets removed from the learning list and the updated list is saved back to `words_need_to_learn.csv`.

## Note

Always ensure that the images and CSV files are located in the correct path as mentioned in the code for the application to run smoothly.

## Future Enhancements

1. Add support for multiple languages.
2. Include audio support for pronunciation.
3. User account and progress tracking across sessions.
