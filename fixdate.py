import imaplib
import email
import getpass
import argparse
from email.utils import parsedate_to_datetime

def list_folders(imap):
    result, folders = imap.list()
    if result == 'OK':
        print("Available folders:")
        for folder in folders:
            print(folder.decode())
    else:
        print("Failed to list folders")

def fetch_and_modify_messages(imap, src_folder, dst_folder):
    imap.select(src_folder)
    typ, msgnums = imap.search(None, 'ALL')

    for num in msgnums[0].split():
        typ, data = imap.fetch(num, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])

        # Get the sent date from the Date header
        sent_date_str = msg['Date']
        
        # Parse the date string to a datetime object with timezone information
        sent_date = parsedate_to_datetime(sent_date_str)
        
        # Check if sent_date is None
        if sent_date is None:
            print(f"Failed to parse sent date for message {num}")
            continue

        # Prepare the message for uploading
        raw_msg = data[0][1]

        # Append the message to the destination folder with the original sent date as INTERNALDATE
        try:
            imap.append(dst_folder, None, imaplib.Time2Internaldate(sent_date), raw_msg)
            print(f"Message {num} processed and uploaded to {dst_folder}")
        except Exception as e:
            print(f"Failed to append message {num}: {e}")

        # Mark the message for deletion in the source folder
        imap.store(num, '+FLAGS', '\\Deleted')
    
    # Expunge the source folder to permanently delete marked messages
    imap.expunge()

def main():
    parser = argparse.ArgumentParser(description="IMAP Email Processor")
    parser.add_argument('--list-folders', action='store_true', help='List folders on the server')
    parser.add_argument('src_folder', nargs='?', help='Source folder')
    parser.add_argument('dst_folder', nargs='?', help='Destination folder')
    parser.add_argument('imap_server', help='IMAP server address')
    parser.add_argument('username', help='Username for IMAP server')
    args = parser.parse_args()

    password = getpass.getpass("Enter your IMAP password: ")

    # Connect to the IMAP server
    imap = imaplib.IMAP4_SSL(args.imap_server)
    imap.login(args.username, password)

    if args.list_folders:
        list_folders(imap)
    else:
        if args.src_folder and args.dst_folder:
            fetch_and_modify_messages(imap, args.src_folder, args.dst_folder)
        else:
            print("Source and destination folders must be specified unless listing folders")

    imap.logout()

if __name__ == "__main__":
    main()
