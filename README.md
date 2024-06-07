<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>IMAP Email Date Fixer</h1>

  <p>A Python script to correct the received date of emails downloaded from an IMAP server to match their original sent dates, and upload them to a different folder.</p>

  <h2>Usage</h2>

  <ol>
    <li>Clone or download the repository.</li>
    <li>Run the script using:</li>
  </ol>

  <pre><code>python fixdate.py [--list-folders] src_folder dst_folder imap_server username</code></pre>

  <p>Arguments:</p>

  <ul>
    <li><code>--list-folders</code>: List folders on the server.</li>
    <li><code>src_folder</code>: Source folder for downloading emails.</li>
    <li><code>dst_folder</code>: Destination folder for uploading modified emails.</li>
    <li><code>imap_server</code>: IMAP server address.</li>
    <li><code>username</code>: Username for IMAP server access.</li>
  </ul>

  <p>Enter the IMAP password when prompted.</p>

  <h2>Example</h2>

  <pre><code>python fixdate.py INBOX Processed imap.example.com user@example.com</code></pre>

  <h2>Requirements</h2>

  <ul>
    <li>Python 3.x</li>
    <li>IMAP server access with appropriate permissions.</li>
  </ul>

  <h2>License</h2>

  <p>This project is licensed under the MIT License.</p>
</body>
</html>
