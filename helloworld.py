import gdata.docs.service

config = file.open('config.txt', 'r')

user = config.readline()
password = config.readline()

# Create a client class which will make HTTP request with Google Docs server
client = gdata.docs.service.DocsService()
# Authenticate using your email address and password
client.ClientLogin(user, password)

# Query the server for an Atom feed containing a  list of documents
documents_feed = client.GetDocumentListFeed()

# Loop through feed and extract each document entry
for document_entry in documents_feed.entry:
	print document_entry.title.text
