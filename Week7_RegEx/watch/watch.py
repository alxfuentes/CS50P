import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Look for src="..." where the URL is a YouTube embed link
    # Supported:
    # http://youtube.com/embed/xvFZjo5PgG0
    # https://youtube.com/embed/xvFZjo5PgG0
    # https://www.youtube.com/embed/xvFZjo5PgG0
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)"'
    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()