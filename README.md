# Possible Bug? Feature? Undocumented Behavior?
## Preamble
I’m facing an issue with generated resources and Python.

I already discussed this on Slack: [Slack thread here](https://app.slack.com/client/T046T6T8L/C046T6T9U).  
However, as I’ve learned: **always create a minimal working project to showcase the issue.** So, here we are.

## What’s Working
1. **The generated file is included in the loose layout of the PEX**  
   - Command: `pants package ::`  
   - You can inspect the output at `dist/src.python.example/loose.pex/example`, the `generated.txt` is right there.
2. **It works in the loose layout of the PEX**  
   - Command: `pants run src/python/example:loose`  
   - Output: `found_generated_txt=True`
3. **It works in the zipapp layout of the PEX**  
   - Command: `pants run src/python/example:zipapp`  
   - Output: `found_generated_txt=True`


## What’s Not Working
1. **The generated file is missing when running the `python_sources` target directly.**  
   This would be a huge speed boost for Django projects since it avoids waiting for a regenerated PEX file.  
   - Command: `pants run src/python/example/main.py`  
   - Output: `found_generated_txt=False`


## Questions
1. Is this behavior intended?
2. Is there a workaround?


## Thanks
Thanks to everyone on the team for your hard work on such a massive tool. It gets better with every release. Keep up the great work! 🎉
