import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Look for src="..." only when inside an <iframe> element with a YouTube embed link
    # Supported embedded sources:
    # http://youtube.com/embed/xvFZjo5PgG0
    # https://youtube.com/embed/xvFZjo5PgG0
    # https://www.youtube.com/embed/xvFZjo5PgG0
    pattern = r'<iframe[^>]*\s+src="https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+)"[^>]*>'
    match = re.search(pattern, s)
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()
    