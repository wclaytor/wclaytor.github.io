# 2025 resume update notes

We are working on an update to the client resume! We have added their two most recent engagements to their existing markdown file by copy/pasting them from LinkedIn but they don't quite fit the template and will likely break our display system. Please review the two most recent entries and update the formatting to be consistent with the template and how it is used in the rest of the resume.

---

Nice! The client would like our Senior HR Advisor to view the resume through their Lens and provide their feedback. We don't want to bias them so we just want to give them the resume and ask for their feedback as the Senior HR Advisor.

---

Nice! The client would like the Bastard Operator From Hell to view the resume through their Lens and provide their feedback. We don't want to bias them so we just want to give them the resume and ask for their feedback as the Senior HR Advisor.

Please capture the following Wikipedia page of this person to create a `$person.md` file that we can reference when referring to them in our prompts.

https://en.wikipedia.org/wiki/Bastard_Operator_From_Hell

--

Nice! We love this feature! Here is a test person to create a persona:

https://en.wikipedia.org/wiki/Lando_Norris

python scripts/personas/create-persona.py https://en.wikipedia.org/wiki/Lando_Norris

@wclaytor ➜ /workspaces/wclaytor.github.io (13-bug-fixes-and-enhancements) $ python scripts/personas/create-persona.py https://en.wikipedia.org/wiki/Lando_Norris


---

We are getting:

```
Connection Error: Failed to fetch Wikipedia page: HTTP Error 403: Forbidden
```

So now we have a way to save the whole HTML page and just give that to the script.

---

Nice! The client would like the Bastard Operator From Hell to view the resume through their Lens and provide their feedback.
