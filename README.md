# key-protected-server
A simple project to protect a website with key access only

key must be provided in a post form data as 'key'

## tldr
```
docker run --name key-protected-server -v ~/Projects/key-protected-server/config.json:/app/config.json -v  ~/Projects/key-protected-server/content/:/app/content/ -p 8080:8080 -d lerignoux/key-protected-server
curl -X POST 'http://localhost:8080/' --data 'key=00000000-0000-1111-0000-000000000000' -o myFile.tar.gz
```

key and the content path have to be added to the config.json file (see config.tpl.json).
content files need to be added in the content folder
