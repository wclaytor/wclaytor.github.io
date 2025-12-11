# 2025 resume update notes

## 2025.12.10
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

---

Nice, thanks! Having read the entire review, the first thing we should tackle is the icon issue. The recommendation to use SVG icons sounds great and will allow us to eliminate dependencies. Please create a plan to replace all of our icons with SVG icons.

-

Nice! Let's go!

---

What should we do about the copyright issue mentioned in the review. We currently have:
```
Copyright &copy; William Claytor 2023 | 2025
```

What should we use instead?

---

Ok! On to next steps:

1. **Enhance the masthead** — Add a compelling tagline below the name (e.g., "Senior Software Engineer | Building Reliable Systems for 25 Years") to immediately communicate value

We really like the minimal landing page. We are hoping that folks will be intrigued and want to learn more by scrolling down or clicking / tapping the about link.

We are willing to try adding the tagline "Senior Software Engineer" and if it fits with the current design and looks great we will consider keeping it. Please implement the tagline and make us love it!

---

Very nice! We are definitely keeping that! The art director and the UX designer were brainstorming after reviewing this update and thought a subtle call to action indicator could enhance engagement. The most subtle thing they could think of is a down-facing arrow button that fades in and causes the page to scroll to the About section when clicked.

---

Nice! We would like each of the sections to feel like a page, but with the ability to scroll between them. However, the Contact section is only about a half page tall, so the illusion is somewhat broken when you click the contact link and see half of the projects section sticking out.

What can we do to subtly and tastefully give the Contacts section enough vertical space to seem like a full page when we navigate to that section?

---

Another nice one, thanks! Users are very interested in our background image theming system and how it is used on each page. 

This makes me think it is time to update our README.md file with some juicy info on everything about how our site is designed and our layout process, including our background image filtering system.

---



As we are testing the site we get the feeling that the use of the background in the about section feels too similar to the main section. We see this called out in the README as visual consistency, but it is a bit too consistent. 

Since the about page will likely be most user's first experience with how we transform the background image, we need to do enough to call out that we are using the same image but changing it in multiple ways, while not being cheezy about it. 

With that in mind, please give it a shot, and we can keep working on it until we get it just right! Go for it!

---

Yes!!! That is so awesome!

Since we are on a roll, let us try an experiment and just create a small project in the projects folder right in the middle of our session to capture what we are doing, and add it to the larger site for later use elsewhere.

I created a README for my idea and will quote it here:

```
A demonstration of our background theming system that displays the background image and shows all of the various filters that can be applied to it, with presets and interactive controls so that the user can experiment by tweaking the filters in real-time and then capture the result as a preset they can use for a section on the site.
```

Go ahead and one-shot that! I know you can do it!

---

Holy freaking wow!!! That is so cool, after testing it for a few minutes I can see really digging in and spending lots of time making cool presets! 

I think we should go ahead and ship it with the current PR. But in that case we do need a way to differentiate it from our projects that we have put tons of effort and testing into. This is a SUPER cool experiment...

We need an experiments section for our projects section! And this can be the first one to go there. And as an experiment, you get to design it and integrate it into the current site. There will be many more experiments to come so it should be easy for us to integrate them as we create them.

-

scripts/utility/md2html/md2html.py projects/alpine-background-transformer/README.md

-

Fantastic! I have created the HTML version of the README. Please link to it from the card.

---

Hello esteemed reviewers! I have worked through several rounds of your reviews.

---

All right! It looks like we have some next steps:

## Next Steps

1. **Immediate Fixes** (This PR): Remove unused SB Forms script, verify asset references, strengthen the masthead headline to lead with "25 Years" value proposition

2. **Content Enhancement**: Refactor the About section copy to be scannable - bullet points, shorter phrases, impact-first language

3. **Architecture Improvement**: Extract project data into `projects.json` and implement dynamic rendering with Alpine.js, establishing the maintainability pattern for future growth

Let us start with the Immediate Fixes!

---

Well that is pretty freaking awesome! Thanks! We are going to run with that. In fact, we have already pushed the commit.

One thing that has been nagging at us through this process is that the professional work experience starts in 1998, and it is 2025, so that is not 25 years of experience. That is over 25 years of experience. How should we pitch this?

--

Yes, let us go with "over 25 years" and we will (hopefully) update it when it needs to be "over 30 years". ;?

---

Ok! I think we are at the point where we can merge this PR and go live with these updates. Before we do that

---

All right! We have our review panel prompt and we would like to create a variant of it that will be a go-live assesment prompt. While the review prompt has a long term focus, the go-live assesment should focus on any show-stopping UI / UX issues, embarrasing issues with any of the content, security issues, performance issues, etc...

Basically, if there is any reason that we should not merge the current PR and go live with it, this is the time to call it our and either fix it or acknowledge it and defer it. We can't fix everything and this is an MVP, so we need to be realistic.

But we are also about to present this site to the world as a demonstration of our experience, skill, abilities, focus on quality, and good judgement. Before we update the URL in the LinkedIn profile to point to this site, we need to be absolutely sure that it is up to standards and will get us hired rather than round-filed over some issue we should have caught and fixed. Heaven forbid we are using any third-party libraries that could become compromised and then harm viewers of our site. We absolutely can not have that happen.

So we need a promt file to assemble the panel with that mission.

---

All right! The PR looks good, all the comments are there... we are just about set... but...

When we present these reviews in the PR, we need to be ABSOULUTELY CLEAR that we are not getting actual reviews from these actual living people. These are "inspired-by" personas informed by Markdown files with some basic limited information we have gathered about these folks. We use them because we think they help to inform our work and the context of our discussions about it. 

We know they are not real people actually thinking about the questions we are asking them. Rather, we hypothesize that adding the context of their Persona profiles to the context helps to guide the model into the "contextual spaces" that we want to explore. It seems to work, we have gotten lots of great feedback, and implemented it, and seen the acknowledgement in subsequent reviews performed with a fresh context. 

Maybe this is a good time to create five Personas with their own unique identity that is inspired by their original namesake / profile doc but that can be a living document that can grow and expand to include other ideas and perspectives beyond these static characterizations.

In our other projects we have implemented this as Roles which you can read about in the README files of the projects in the projects folder. For example, see `projects/alpine-resume/README.md` where it talks about the seven roles.

We want to explore that same approach with this public-facing project, but in a more fluid and less regimented way.

After working through the epics to get the current featured projects to their present state, we have encountered some friction that is perfectly fine and good for those projects but not for this one where we need to work in the timeframe of hours and not seasons. We need to get important things done now, and less important things can wait but should not be forgotten.

Let us ponder how to proceed, and if there is anything else we should do before going live.

---

A simple first step would be to create an alias for each of our advisors so it doesn't look like we are claiming to be them. In the alias file it can reference the persona doc of the mentor.

Please create an alias persona for our first advisor and we will refine it, approve it, and then use that process for the others.

I have provided an example of an advisor file. But in our case the advisor should be informed by the persona, so let's do that for steve-krug.md and create a corresponding advisor file that is inspired by Steve but is not claiming to be Steve.

-

Yes, I can dig it! I do like the name - well done! Let us do the same for each of the others, one at a time, so that we can review each before proceeding to the next.

---

Yes, that is great! Please continue with the next.

---

So we have the persona-based versions of our review and go-live prompts. Let us create alternate versions of these that refernece the advisors rather than referening the personas.

---

## 2025.12.11

We are working on some final tweaks and polish to the website before we go live.

Please review the README.md file to get familiar with the layout and background theming system.

First, we would like to adjust the background filter for the about section to use more of an indigo blue.

-

Nice, that looks perfect! Now, we would like to flex a bit for the contacts section as it now looks very similar to the about section. In addition to the gradient and transparency, we would like to add grain and blur effects.

---

Nice! We previously created the alpine-background-transformer project to demonstrate the background theming system. We would like to update that project to reflect the recent updates to the site:
- new midnight theme for the about section
- new effects and purple theme for the content section

So we will need to update the theme examples for the sections to reflect the current site. And we will need to add the blur and grain effects controls to the controls panel.