# CodeAlpha_TaskAutomation

Two small scripts that automate repetitive tasks: extracting email addresses from a text file, and moving `.jpg` images into a new folder.

> Built for the **CodeAlpha Python Programming Internship**.

## Features
- **Email extractor:** finds every email in a `.txt` file, removes duplicates and saves them to another file
- **JPG mover:** moves all `.jpg` / `.jpeg` files (any letter case) into a new folder without overwriting
- Command-line interface with `argparse`
- Friendly error messages
- Unit tests for both scripts

## Concepts used
- `re` (regular expressions)
- `shutil` and `pathlib`
- File reading and writing
- `argparse`
- Exception handling
- `unittest` with temporary folders

## Project structure
```
CodeAlpha_TaskAutomation/
+-- email_extractor.py
+-- jpg_mover.py
+-- sample.txt             # test input
+-- test_email_extractor.py
+-- test_jpg_mover.py
+-- TaskAutomation.ipynb
+-- README.md
+-- requirements.txt
+-- .gitignore
```

## How to run
Requires Python 3.8+ (no external libraries).

```bash
# Email extractor
python email_extractor.py sample.txt -o emails.txt

# JPG mover
python jpg_mover.py ./photos ./photos/images
```

Run the unit tests:
```bash
python -m unittest -v
```

Open the step-by-step notebook:
```bash
pip install jupyter
jupyter notebook
```

## Sample run
```
$ python email_extractor.py sample.txt -o emails.txt
Found 3 unique email(s). Saved to emails.txt

$ cat emails.txt
john.doe99@mail.co.in
sales@example.com
support@example.com
```

## Future improvements
- Scrape the title of a webpage with `requests` and `BeautifulSoup`
- Sort images by file type or date
- Add logging
- Support folders of many text files

## Author
Your Name - [LinkedIn](https://linkedin.com/in/your-profile) - [GitHub](https://github.com/your-username)
