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

--

Nice! It seems to be working based on the input:

```
python scripts/personas/create-persona.py assets/personas/kent-beck.html
```

But we would like the default output location to be the same as the input file.

python scripts/personas/create-persona.py assets/personas/martin-fowler.html

-

Nice! We would like to have a team of five personas as our esteemed review panel. I have created persona files for you (The BOFH), Kent Beck, and Martin Fowler. You have the opportunity to suggest two additional personas to fill out the review panel. Please provide your suggestions with your reasoning and I will procure the persona files. Then we can assemble the panel and begin our full review process.

-

python scripts/personas/create-persona.py

python scripts/personas/create-persona.py assets/personas/jakob-nielsen.html

python scripts/personas/create-persona.py assets/personas/steve-krug.html

---

We are creating a review panel with five esteemed members to provide feedback on our work and help us create excellent solutions. Items for review may include:
- a code update on the fly
- a pull request
- a new design idea for our website
- a resume or cover letter
- project documentation
- an essay or blog post
- etc...

I have assembled the Persona files for our five esteemed members of the review panel. Please create a prompt file to assemble the review panel and guide them through the review process to each provide their own unique perspective, then synthesize a summary, and provide the complete review in Markdown format.

---

Nice! Let us focus on the immediate items first:

Immediate (Compliance & Discovery):

- Add descriptive meta tags (title, description, Open Graph)
- Implement skip-to-content navigation link for WCAG compliance
- Update Font Awesome to current stable version (6.7.x)

Let us take them one at a time. I will test each proposed change and we will work to resolve any issues. When we are satisfied I will commit the update and we will move on to the next item.

Let us start with the first item!

---

Nice! Let us move on to the next item.

---

Please elaborate on the "Implement consistent visual layout for project showcase" item.

-

We are going to be adding projects so moving to a card-based layout is appealing. We should have featured project cards for our featured projects, and regular cards for our other side projects. 

Let us start by implementing featured project cards with two cards per row, with the rows switching to stacked for mobile layouts.

---

Nice! We would like to include a link to the README.md file for each project. However, viewing the README.md in the browser will just show the raw text, which is not what we want. We want the README to be nicely formatted like they look on GitHub. So we would like to create a Python script to convert our README.md files into README.html files with that sweet formatting. We would also like to include a light / dark mode theme toggle like we use in the alpine-resume site which I have included as an example.

Please create the md2html.py script that will convert any Markdown file into a sweet HTML page that looks great in the browser.

--

scripts/utility/md2html/md2html.py

scripts/utility/md2html/md2html.py projects/alpine-resume/README.md

scripts/utility/md2html/md2html.py projects/alpine-markdown-presentation/README.md

Nice! These project repos are currently private, so instead of 'source' buttons let us replace those with 'view readme' buttons that link to our new README.html files.

