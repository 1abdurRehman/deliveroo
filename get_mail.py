import imaplib
import email
import re

def get_magic_link_from_body(body):
    # Compile a regular expression to match the magic link
    pattern = re.compile(r"https://deliveroo\.co\.uk/login/magic-link\?[^\s]*")

    # Search for the magic link in the body text
    match = pattern.search(body)

    # If a match is found, extract the magic link
    if match:
        magic_link = match.group()
        print("Magic link:", magic_link)
        return magic_link
    print("Magic link not found.")

def get_mail_out():
    # Connect to the Outlook IMAP server
    imap_server = imaplib.IMAP4_SSL("outlook.office365.com")

    # Log in to your account
    imap_server.login("abd.reh980@outlook.com", "Database56$$")

    # Select the Inbox folder
    imap_server.select("Inbox")

    # Search for messages with a specific subject line, sorted in reverse order
    subject = "Log in to Deliveroo with your magic link"
    # subject = imaplib.encode_utf7(subject)
    _ , messages = imap_server.search(None, 'SUBJECT', f'"{subject}"')

    # Get the first message in the list (which will be the latest message)
    message_id = messages[0].split()[-1]
    _ , data = imap_server.fetch(message_id, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    body = ""
    if message.is_multipart():
        # If the message is multipart, get the first text/plain part
        for part in message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                break
    else:
        # If the message is not multipart, the body is the message payload
        body = message.get_payload(decode=True)

    # Decode the body from bytes to a string
    body = body.decode("utf-8", errors="ignore")


    # Print the body of the message
    magic_link = get_magic_link_from_body(body)
    return magic_link