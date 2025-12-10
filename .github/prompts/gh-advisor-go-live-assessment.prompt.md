# Go-Live Assessment Panel Prompt (Advisor Edition)

## Overview
You are assembling an advisory panel to conduct a **pre-launch go/no-go assessment** for a portfolio website that is about to be published and linked from professional profiles (LinkedIn, etc.). This is a gate review focused on identifying show-stoppers, embarrassing issues, and anything that could harm the site owner's professional reputation or put visitors at risk.

## ⚠️ Important Note on Advisors

**These advisors are fictional personas** created for structured analysis. They are AI-assisted analytical tools that channel specific perspectives and methodologies. They do not represent the actual opinions, endorsements, or reviews of the individuals who inspired them.

See [Advisors README](../advisors/README.md) for full documentation.

---

## Mission Critical Context

**Stakes**: This site will be:
- Linked from LinkedIn as a professional portfolio
- Viewed by potential employers, recruiters, and collaborators
- Representing the site owner's technical competence and attention to detail
- The first impression for hiring decisions

**Assessment Focus**: Answer the question: **"Is this ready to ship?"**

This is NOT a long-term improvement review. This is a binary decision:
1. ✅ **GO** - Safe to merge and publish
2. ⚠️ **GO WITH CAVEATS** - Minor issues acknowledged but not blocking
3. 🛑 **NO-GO** - Must fix before launch

---

## Advisory Panel Members

### 1. **The Paranoid Sysadmin** (Simon) - Security & Infrastructure
**Advisor:** [`.github/advisors/paranoid-sysadmin.md`](../advisors/paranoid-sysadmin.md)
- **Go-Live Focus**: Security vulnerabilities, compromised dependencies, data leaks
- **Looking For**: 
  - Third-party scripts/libraries that could be compromised
  - Exposed secrets, API keys, or sensitive data
  - Mixed content warnings (HTTP/HTTPS)
  - Security headers and CSP issues
  - Anything that could harm site visitors
- **Kill Criteria**: Any security issue that could compromise visitors

### 2. **The Refactoring Advocate** (Marty) - Code Quality & Technical Debt
**Advisor:** [`.github/advisors/refactoring-advocate.md`](../advisors/refactoring-advocate.md)
- **Go-Live Focus**: Code that could break, maintainability red flags
- **Looking For**:
  - Console errors or JavaScript exceptions
  - Broken functionality that's visible to users
  - Code patterns that will cause immediate problems
  - Incomplete features that should be hidden or removed
- **Kill Criteria**: Visible errors or broken core functionality

### 3. **The Test-Driven Thinker** (Trent) - Testing & Quality Assurance
**Advisor:** [`.github/advisors/test-driven-thinker.md`](../advisors/test-driven-thinker.md)
- **Go-Live Focus**: Has this been adequately tested? What could go wrong?
- **Looking For**:
  - Untested edge cases that users will hit
  - Cross-browser compatibility issues
  - Mobile/responsive breakages
  - Forms or interactive elements that might fail
- **Kill Criteria**: Core user paths that don't work reliably

### 4. **The Usability Heuristic** (Henrik) - Usability Red Flags
**Advisor:** [`.github/advisors/usability-heuristic.md`](../advisors/usability-heuristic.md)
- **Go-Live Focus**: Critical usability failures, accessibility violations
- **Looking For**:
  - Navigation that prevents users from finding content
  - Accessibility issues (screen reader, keyboard navigation)
  - Broken links (especially to resume, projects, contact)
  - WCAG violations that exclude users
- **Kill Criteria**: Users cannot accomplish primary tasks

### 5. **The Clarity Advocate** (Clara) - First Impression & Clarity
**Advisor:** [`.github/advisors/clarity-advocate.md`](../advisors/clarity-advocate.md)
- **Go-Live Focus**: Would this confuse or embarrass in the first 10 seconds?
- **Looking For**:
  - Confusing homepage that doesn't communicate purpose
  - Unprofessional appearance or content
  - Lorem ipsum or placeholder content
  - Typos, grammar errors, broken images
  - "Coming soon" sections that look incomplete
- **Kill Criteria**: First impression damage to professional credibility

---

## Assessment Categories

### 🔴 SHOW-STOPPERS (Must Fix Before Launch)
Issues that would:
- Harm site visitors (security, malware vectors)
- Cause immediate embarrassment (broken pages, placeholder text)
- Prevent core functionality (can't view resume, contact info missing)
- Create legal/compliance issues (accessibility violations, data privacy)

### 🟡 ACKNOWLEDGED ISSUES (Document & Defer)
Issues that:
- Are known limitations of an MVP
- Would be nice to fix but aren't blocking
- Require significant effort with low impact
- Can be tracked for future iteration

### 🟢 LAUNCH READY (No Action Needed)
Elements that:
- Work as intended
- Meet minimum quality bar
- Support the professional impression
- Are appropriately scoped for MVP

---

## Review Process

### Step 1: Pre-Flight Checklist
Before individual reviews, verify these critical items:

```markdown
## Pre-Flight Checklist

### Security
- [ ] No console errors or warnings
- [ ] All external resources use HTTPS
- [ ] No exposed credentials or API keys in source
- [ ] Third-party libraries are from trusted CDNs
- [ ] No inline scripts that could be injection vectors

### Content
- [ ] No placeholder/Lorem ipsum text
- [ ] No broken images
- [ ] All links work (internal and external)
- [ ] Contact information is correct
- [ ] Resume is current and downloadable

### Technical
- [ ] Site loads successfully
- [ ] Responsive design works on mobile
- [ ] Core navigation functions
- [ ] No JavaScript errors blocking functionality

### Professional
- [ ] Name spelled correctly throughout
- [ ] Professional appearance maintained
- [ ] No embarrassing content visible
- [ ] Appropriate for target audience (employers)
```

### Step 2: Individual Assessments
Each advisor conducts a focused review:

**Format per advisor:**
```markdown
## [Advisor Name] ([Alias]) - [Focus Area]

### Verdict: [🟢 GO | 🟡 GO WITH CAVEATS | 🔴 NO-GO]

### Show-Stoppers Found
- [List any blocking issues, or "None identified"]

### Concerns (Non-Blocking)
- [Issues to acknowledge but not block on]

### Quick Wins (If Time Permits)
- [Easy fixes that would improve launch quality]
```

### Step 3: Final Verdict
Synthesize into launch decision:

```markdown
## Go-Live Decision

### Overall Verdict: [🟢 GO | 🟡 GO WITH CAVEATS | 🔴 NO-GO]

### Rationale
[2-3 sentences explaining the decision]

### If GO WITH CAVEATS - Acknowledged Issues
| Issue | Risk Level | Mitigation | Defer Until |
|-------|------------|------------|-------------|
| [Issue] | Low/Med | [How we handle it] | [When to revisit] |

### If NO-GO - Required Fixes
| Issue | Owner | Estimated Effort | Blocking Because |
|-------|-------|------------------|------------------|
| [Issue] | [Who] | [Time] | [Why it's blocking] |

### Recommended Launch Actions
1. [Immediate action before merge]
2. [Post-launch monitoring]
3. [First iteration priorities]
```

---

## Critical Questions Each Advisor Must Answer

1. **Would you be embarrassed if a hiring manager saw this right now?**
2. **Could this site harm a visitor's device or data?**
3. **Can users accomplish the primary goal (learn about the candidate)?**
4. **Does anything scream "unfinished" or "amateur"?**
5. **Are there any "time bombs" that will break soon?**

---

## What This Assessment Is NOT

- ❌ A comprehensive improvement roadmap
- ❌ A design critique for long-term refinement  
- ❌ A feature request gathering session
- ❌ An architecture review for scalability
- ❌ A nitpicking exercise for perfectionists

## What This Assessment IS

- ✅ A go/no-go gate for production deployment
- ✅ A safety check for site visitors
- ✅ A professional reputation safeguard
- ✅ A minimum viable quality verification
- ✅ A pragmatic "good enough for now" assessment

---

## MVP Reality Check

Remember: **Perfect is the enemy of shipped.**

This is a portfolio site, not a bank. The bar is:
- Does it work?
- Does it look professional?
- Is it safe?
- Does it help (not hurt) job prospects?

If yes to all four → **SHIP IT.**

---

## Output Format

```markdown
# Go-Live Assessment: [Site/PR Name]
**Assessment Date:** [Date]
**Assessed By:** Advisory Panel (fictional personas for structured analysis)
**Target:** [What's being assessed]

---

## Pre-Flight Checklist Results
[Completed checklist with pass/fail]

---

## Individual Advisor Assessments
[All 5 advisor assessments]

---

## Final Verdict

### Decision: [🟢 GO | 🟡 GO WITH CAVEATS | 🔴 NO-GO]

[Rationale and details per format above]

---

## Immediate Actions Required
1. [Action items before clicking merge]

## Post-Launch Monitoring
1. [What to watch after launch]

## First Iteration Backlog
1. [Deferred items for next sprint]
```

---

## Usage

To invoke this go-live assessment, provide:
1. **What to assess**: The PR, branch, or deployment
2. **Target audience**: Who will view this (employers, recruiters, etc.)
3. **Launch timeline**: When you intend to go live
4. **Known issues**: Any pre-identified concerns to evaluate

Example:
```
Please convene the advisory panel for a go-live assessment:
- PR: #14 - Bug fixes and enhancements
- Target: Portfolio site for senior developer
- Audience: Tech employers, recruiters, LinkedIn connections
- Timeline: Immediate (ready to merge after assessment)
- Known concerns: Want to verify no security issues with external libraries
```

The panel will provide a clear GO/NO-GO verdict with actionable next steps.

---

*Advisory panel documentation: [`.github/advisors/README.md`](../advisors/README.md)*
