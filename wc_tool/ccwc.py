#!/usr/bin/env python3
import sys
import argparse

def count_stats(stream):
    """Reads the input stream once and computes all required metrics."""
    # Read the full raw bytes to accurately measure byte size
    raw_data = stream.read()
    
    # Calculate bytes
    num_bytes = len(raw_data)
    
    # Decode to string to calculate lines, words, and characters
    try:
        text = raw_data.decode('utf-8')
    except UnicodeDecodeError:
        # Fallback to loose decoding if it's a binary file
        text = raw_data.decode('utf-8', errors='ignore')

    num_chars = len(text)
    num_lines = text.count('\n')
    num_words = len(text.split())

    return num_lines, num_words, num_chars, num_bytes

def main():
    # Setup argparse to closely match standard Unix options
    parser = argparse.ArgumentParser(
        description="A custom clone of the Unix 'wc' command line utility.",
        add_help=True
    )
    parser.add_argument('file', nargs='?', type=argparse.FileType('rb'), default=sys.stdin.buffer,
                        help="The file to count. If omitted, reads from standard input.")
    parser.add_argument('-c', '--bytes', action='store_true', help="Print the byte counts")
    parser.add_argument('-l', '--lines', action='store_true', help="Print the newline counts")
    parser.add_argument('-w', '--words', action='store_true', help="Print the word counts")
    parser.add_argument('-m', '--chars', action='store_true', help="Print the character counts")
    
    args = parser.parse_args()

    # Fetch stats
    try:
        lines, words, chars, bytes_count = count_stats(args.file)
    except Exception as e:
        print(f"ccwc: error reading input: {e}", file=sys.stderr)
        sys.exit(1)

    # Determine what to print based on flags
    # If no flags are provided, the default behavior prints lines, words, and bytes
    no_flags = not (args.bytes or args.lines or args.words or args.chars)
    
    output = []
    if args.lines or no_flags:
        output.append(f"{lines:>7}")
    if args.words or no_flags:
        output.append(f"{words:>7}")
    if args.chars:
        output.append(f"{chars:>7}")
    if args.bytes or (no_flags and not args.chars):
        output.append(f"{bytes_count:>7}")

    # Append the filename if we read from an actual file instead of stdin
    file_name = args.file.name if args.file.name != '<stdin>' else ''
    if file_name:
        output.append(f" {file_name}")

    print("".join(output))

if __name__ == "__main__":
    main()
