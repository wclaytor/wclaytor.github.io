# wclaytor

projects/alpine-markdown-presentation

We have an issue with the alpine-markdown-presentation not correctly loading the sample file when we view it live in GitHub pages. It seems to work when we preview it in a Codespace which is why we didn't catch it sooner.

---

The UI / UX design team submitted their proposal for an update to the resume page. This is the page that viewers will see when they click the resume link on the main site. Please check it out!


This version is much closer. 

There are a few more issues: 
In the navigation section, 'Home' is a separate button. Insetead, it should be the first option in the list of sections, like: - Home - Links - etc... 

Speaking of the section navigation, we do not need a label to tell us what the section contains ('text'). Please remove these. 

The 'Short' button is not explanatory. In the same way that we have 'Theme: Dark' we should have 'Content: Short'. 

The links should be removed from the William Claytor header as they are also in the Links section. The Links section should just be one of the sections, not a heading section with a surround like William Claytor. There is already a leftover Links section heading and this is where the links should go. And when we do display the links, we should have a label and then the URL of the link as the link. This way when it is printed the URLs are displayed rather than just the text 'Personal website', etc... And this way users can see the URL they are about to visit to ensure it is valid and safe. 

And lastly, please also tweak the header to include that “US citizen willing to relocate…” line (right now it isn’t captured by the minimal parser, since it’s a pre-section bullet). That’s easy to support by adding a headerBullets field in the parsed model.

---

python projects/dynamic-resume/releases/v2.2/build_resume.py projects/dynamic-resume/releases/v2.2/william-claytor-resume.md projects/dynamic-resume/releases/v2.2/test.html

We are debugging the script. I can see the template is there. Please see what this issue is and fix it.