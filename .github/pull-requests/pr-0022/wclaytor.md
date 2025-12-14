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

```
@wclaytor ➜ /workspaces/wclaytor.github.io (21-more-tweaks) $ python projects/dynamic-resume/releases/v2.2/build_resume.py projects/dynamic-resume/releases/v2.2/william-claytor-resume.md projects/dynamic-resume/releases/v2.2/test.html
Traceback (most recent call last):
  File "/workspaces/wclaytor.github.io/projects/dynamic-resume/releases/v2.2/build_resume.py", line 306, in <module>
    main()
  File "/workspaces/wclaytor.github.io/projects/dynamic-resume/releases/v2.2/build_resume.py", line 294, in main
    template = args.template.read_text(encoding="utf-8")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python/3.12.1/lib/python3.12/pathlib.py", line 1027, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors) as f:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/python/3.12.1/lib/python3.12/pathlib.py", line 1013, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'resume_template_configurable.html'
```

---

```
@wclaytor ➜ /workspaces/wclaytor.github.io (21-more-tweaks) $ python projects/dynamic-resume/releases/v2.2/build_resume.py projects/dynamic-resume/releases/v2.2/william-claytor-resume.md projects/dynamic-resume/releases/v2.2/test.html
Wrote projects/dynamic-resume/releases/v2.2/test.html
```

Well it created a file, but the file doesn't include the resume data. They gave us a "generated" version that we found quite impressive. So of course the first thing we want to do is test the python script and reproduce the results. You can see the results in test.html

As a baseline, before we even think about improvements we might want to make, we should try to figure out why the current script output doesn't match the "generated" version. It is possible that they didn't even use the script to generate that version at all. We hope that is not the case. Maybe it is just a small issue. Let us proceed.

-

python projects/dynamic-resume/releases/v2.3/build_resume.py projects/dynamic-resume/releases/v2.3/william-claytor-resume.md projects/dynamic-resume/releases/v2.3/test1.html

---

There are a few more issues. We will work through them one at a time and I will test each update before we move on to the next.

Please keep in mind that we want to update the script so that it creates the correct result and verify the generated test.htm l file. We do not want to update the test.html file directly.

First: In the navigation section, 'Home' is a separate button. Insetead, it should be the first option in the list of sections, like: - Home - Links - etc... 

Speaking of the section navigation, we do not need a label to tell us what the section contains ('text'). Please remove these. 

The 'Short' button is not explanatory. In the same way that we have 'Theme: Dark' we should have 'Content: Short'. 

The links should be removed from the William Claytor header as they are also in the Links section. The Links section should just be one of the sections, not a heading section with a surround like William Claytor. There is already a leftover Links section heading and this is where the links should go. And when we do display the links, we should have a label and then the URL of the link as the link. This way when it is printed the URLs are displayed rather than just the text 'Personal website', etc... And this way users can see the URL they are about to visit to ensure it is valid and safe. 

And lastly, please also tweak the header to include that “US citizen willing to relocate…” line (right now it isn’t captured by the minimal parser, since it’s a pre-section bullet). That’s easy to support by adding a headerBullets field in the parsed model.

python projects/dynamic-resume/releases/v2.3/build_resume.py projects/dynamic-resume/releases/v2.3/william-claytor-resume.md projects/dynamic-resume/releases/v2.3/test2.html

The structure of the page looks good but the links section is empty.