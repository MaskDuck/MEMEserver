# MEMEserver
this MEMEserver serve all types of MEMEs!

# How to deploy

1. Fork this repo.
2. `pip install -r requirements.txt`
3. `python3 memeserver`

# How to contribute a meme
**This require Python knowledge.**
1. Contribute your meme in `memeserver/memes` folder.
2. Write an handler for the meme. Here's an example:
   ```
   async def wikipedia(scope):
       return FileResponse('memeserver/memes/wikipedia.png')
   ```
3. Add the handler to the global list of scope.
4. Submit a PR.
