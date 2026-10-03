"""Extract all email addresses from a .txt file and save them to another file.

CodeAlpha Python Programming Internship.
"""

import argparse
import re

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def extract_emails(text):
    """Return a sorted list of unique email addresses found in text."""
    return sorted(set(re.findall(EMAIL_PATTERN, text)))


def extract_from_file(input_path, output_path):
    """Read input_path, save unique emails to output_path, return the list."""
    with open(input_path, encoding="utf-8") as f:
        text = f.read()
    emails = extract_emails(text)
    if emails:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(emails) + "\n")
    return emails


def main():
    parser = argparse.ArgumentParser(description="Extract email addresses from a text file.")
    parser.add_argument("input", help="Path to the input .txt file")
    parser.add_argument("-o", "--output", default="emails.txt", help="Output file (default: emails.txt)")
    args = parser.parse_args()

    try:
        emails = extract_from_file(args.input, args.output)
    except FileNotFoundError:
        print("Error: file '" + args.input + "' not found.")
        return

    if emails:
        print("Found " + str(len(emails)) + " unique email(s). Saved to " + args.output)
    else:
        print("No email addresses found.")


if __name__ == "__main__":
    main()
