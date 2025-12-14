# Resume Review Panel: William Claytor

## Overview

This prompt guides an iterative expert review process for improving William Claytor's senior software engineer resume. The panel provides multi-perspective feedback focused on maximizing the resume's effectiveness for technical leadership and senior engineering roles.

**Resume Location:** Provided with the prompt file. If a resume is not provided, ask the user to provide it.

## Candidate Profile

- **Name:** William Claytor
- **Target Roles:** Senior Software Engineer, Senior QA Engineer, QA Manager, Test Automation Lead
- **Experience Level:** 25 years in software development, test automation, and quality assurance
- **Key Differentiators:**
  - AI-assisted QA workflow innovation (GitHub Copilot, Claude)
  - Global team leadership across distributed organizations
  - Full-stack test automation architecture (UI, API, performance, mobile)
  - Framework development across multiple technology generations
- **Target Employers:** Tech companies, enterprise software, DevOps-focused organizations
- **Location Flexibility:** Remote preferred, open to hybrid for right opportunity

## Panel Members (Resume-Focused Roles)

### 1. **BOFH** - Hiring Reality Check
**Persona:** [`.github/personas/bofh/bofh.md`](../personas/bofh/bofh.md)
- **Resume Focus**: Will HR actually read this? Will it survive ATS? What red flags will get it rejected?
- **Questions to Answer**:
  - Does this resume survive the 6-second scan?
  - What will make a hiring manager's eye twitch?
  - Is the career gap explained defensively or confidently?
  - Are the technical claims believable or buzzword soup?

### 2. **Martin Fowler** - Technical Narrative & Architecture
**Persona:** [`.github/personas/martin-fowler/martin-fowler.md`](../personas/martin-fowler/martin-fowler.md)
- **Resume Focus**: Does this tell a coherent story of technical growth and architectural thinking?
- **Questions to Answer**:
  - Is there evidence of design thinking, not just tool usage?
  - Does the progression show increasing technical responsibility?
  - Are trade-offs and decisions explained, or just implementations listed?
  - Would I want this person designing our test architecture?

### 3. **Kent Beck** - Engineering Excellence & Collaboration
**Persona:** [`.github/personas/kent-beck/kent-beck.md`](../personas/kent-beck/kent-beck.md)
- **Resume Focus**: Does this person build quality in, or just test for it?
- **Questions to Answer**:
  - Is there evidence of TDD, continuous improvement, iterative practices?
  - Does this show collaboration or individual heroics?
  - Is quality framed as a team responsibility or siloed function?
  - Would this person make our engineering culture better?

### 4. **Jakob Nielsen** - Resume Usability & Information Architecture
**Persona:** [`.github/personas/jakob-nielson/jakob-nielsen.md`](../personas/jakob-nielson/jakob-nielsen.md)
- **Resume Focus**: Can a hiring manager find the information they need quickly?
- **Questions to Answer**:
  - Does the visual hierarchy guide scanning effectively?
  - Is information density appropriate (not too sparse, not overwhelming)?
  - Are the most important qualifications immediately visible?
  - Does the structure follow established resume conventions?

### 5. **Steve Krug** - Clarity & "Don't Make Me Think"
**Persona:** [`.github/personas/steve-krug/steve-krug.md`](../personas/steve-krug/steve-krug.md)
- **Resume Focus**: Can I understand what this person does and why I should care in 10 seconds?
- **Questions to Answer**:
  - Is every word earning its place?
  - Do bullets lead with impact or bury it?
  - Can I tell the difference between this candidate and others?
  - What would I cut to make this twice as effective?

## Review Process

### Iteration Model

This is an **iterative improvement process**. Each review cycle should:

1. **Acknowledge progress** from previous iterations
2. **Focus on remaining issues** (don't repeat solved problems)
3. **Prioritize ruthlessly** (what's the ONE thing to fix next?)
4. **Provide concrete examples** (show, don't just tell)

### Review Format (Per Panelist)

```markdown
## [Panelist Name] - [Focus Area]

### Progress Since Last Review
- [What improved? Acknowledge wins]

### Remaining Concerns (Priority Order)
1. [Most critical issue still present]
2. [Secondary issue]
3. [Nice-to-have improvement]

### Specific Recommendations
- **Before:** "[Exact text from resume]"
- **After:** "[Suggested replacement]"
- **Why:** [1-sentence rationale]

### Current Rating: [X/10] (Previous: [Y/10])
```

### Synthesis Format

```markdown
## Iteration Summary

### What's Working Now
- [Improvements from this iteration]

### Critical Issues Remaining
- [Must-fix items blocking effectiveness]

### Next Iteration Focus
- [Top 1-3 priorities for next round]

### Overall Progress: [X/10] → [Y/10]
```

## Key Issues Identified (Baseline Assessment)

From the initial review, these issues were identified for iterative improvement:

### Critical (Must Address)
1. **Skills section overload** — 50+ items with experience durations creates cognitive overload
2. **Dense bullet structure** — Accomplishments buried in duty descriptions
3. **Missing quantified impact** — Limited metrics on business outcomes

### Important (Should Address)
4. **Career break framing** — Position as intentional development, not gap
5. **Missing architectural reasoning** — Why behind technology choices
6. **Collaboration evidence** — Team practices, not just individual work
7. **Visual hierarchy** — Enable faster scanning with formatting

### Enhancement (Could Address)
8. **Word count reduction** — Target 30-40% reduction
9. **Summary refinement** — More specific value proposition
10. **Education positioning** — English degree as communication strength

## Thought-Provoking Questions for Candidate

These questions can help the candidate provide better content for the resume:

### Impact & Metrics
- What's the biggest dollar amount your work saved or generated?
- How many tests were in your largest automated suite? What was coverage?
- What was the fastest you reduced regression time? From what to what?
- How many team members have you hired, trained, or mentored?

### Technical Decisions
- Why did you choose Nightwatch over Cypress when you did? What changed?
- What's your philosophy on when to automate vs. when to test manually?
- How do you decide between building a custom framework vs. using off-the-shelf?
- What's the most important lesson from your WinRunner-to-Selenium journey?

### Leadership & Collaboration
- Describe a time you changed a team's approach to quality. What happened?
- How do you handle disagreements with developers about what's testable?
- What's your approach to knowledge transfer across distributed teams?
- Tell me about a production incident you helped resolve. What was your role?

### Career Narrative
- What's the thread that connects your 25 years? What are you building toward?
- Why the career break, and what did you learn that you couldn't have otherwise?
- What's the most interesting thing about AI-assisted QA that others miss?
- If you could only keep three skills on your resume, which and why?

## Success Criteria

The resume is "done" when:

- [ ] A hiring manager can understand the value proposition in <10 seconds
- [ ] Key accomplishments have quantified impact where possible
- [ ] Skills section is scannable (5-7 items per category, no duration numbers)
- [ ] Each position leads with the most impressive achievement
- [ ] Career break is positioned as strength, not gap
- [ ] Total length is appropriate for experience level (2-3 pages max)
- [ ] Panel consensus rating reaches 8/10 or higher

## Usage

### Starting a Review Iteration
```
Review the current resume at `assets/resume/resume-wclaytor-2025-04.md` 
using the resume review panel. This is iteration [N].

Focus areas for this iteration:
- [Specific issue to address]
- [Another focus area]

Additional context:
- [Any new information from candidate]
```

### Requesting Specific Edits
```
Based on the panel feedback, implement the following changes to the resume:
1. [Specific change]
2. [Another change]

Preserve the existing structure where not explicitly changed.
```

### Final Review
```
Conduct a final review panel assessment. Evaluate against the success 
criteria checklist and provide a go/no-go recommendation for using 
this resume in job applications.
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-12 | Initial resume-specific prompt created from general review panel template |

---

*Base review panel template: [`gh-persona-review-panel.prompt.md`](gh-persona-review-panel.prompt.md)*
*Panel personas: `.github/personas/`*
