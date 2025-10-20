import argparse
from config import DEFAULT_PAGES, SAVE_FILE
from page import generate_pages
from game_engine import play

def main():
    parser = argparse.ArgumentParser(description='MaxPages Adventure')
    parser.add_argument('--pages', type=int, default=DEFAULT_PAGES, help='number of pages to generate')
    args = parser.parse_args()

    pages = generate_pages(max(5, args.pages))
    play(pages, SAVE_FILE)

if __name__ == '__main__':
    main()
