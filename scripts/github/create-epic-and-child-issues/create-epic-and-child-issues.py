#!/usr/bin/env python3
# filepath: /workspaces/wclaytor.github.io/scripts/github/create-epic-and-child-issues.py
"""
BOFH Epic Issue Creator 🔥

This script parses the BOFH Epic markdown file and creates GitHub issues
using the gh CLI tool.

Usage:
    python create-epic-and-child-issues.py [--dry-run]

Options:
    --dry-run    Print commands without executing them
"""

import subprocess
import sys
import re
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Issue:
    """Represents a GitHub issue to be created."""
    title: str
    body: str
    labels: list[str] = field(default_factory=list)
    milestone: Optional[str] = None
    is_epic: bool = False


# Define the epic and child issues based on bofh-epic.md
EPIC_TITLE = "Epic: BOFH Site Improvements 🔥"
EPIC_LABELS = ["epic", "enhancement", "technical-debt"]
MILESTONE = "Site Refresh 2025"

CHILD_ISSUES = [
    Issue(
        title="fix: Add missing meta description, author, and SEO tags",
        labels=["seo", "quick-win", "priority-high"],
        body="""## Description

The site currently has empty meta description and author tags, which is SEO 101 failure.

## Current State

```html
<meta name="description" content="" />
<meta name="author" content="" />
```

## Required Changes

- Add meaningful meta description
- Add author meta tag
- Update page title to be more descriptive
- Add keywords meta tag (optional, but nice to have)

## Acceptance Criteria

- [ ] Meta description is filled with compelling, keyword-rich content
- [ ] Author meta tag is populated
- [ ] Page title includes name and role
- [ ] HTML validation passes

## References

- Part of Epic: BOFH Site Improvements 🔥
- [BOFH Site Review](/assets/docs/reviews/bofh-site-review.md)
"""
    ),
    Issue(
        title="feat: Add Open Graph and Twitter Card meta tags",
        labels=["seo", "enhancement", "priority-high"],
        body="""## Description

When the site is shared on LinkedIn, Twitter, or other social platforms, it displays poorly due to missing Open Graph tags.

## Required Changes

- Add Open Graph meta tags (og:type, og:title, og:description, og:url, og:image)
- Add Twitter Card meta tags
- Create or designate an og-image for social sharing

## Acceptance Criteria

- [ ] Open Graph tags are present and valid
- [ ] Twitter Card tags are present
- [ ] Social sharing preview looks professional (test with LinkedIn Post Inspector, Twitter Card Validator)
- [ ] og:image exists and is appropriately sized (1200x630px recommended)

## References

- Part of Epic: BOFH Site Improvements 🔥
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
"""
    ),
    Issue(
        title="fix: Correct email link href/display mismatch",
        labels=["bug", "quick-win", "priority-critical"],
        body="""## Description

The email link has a mismatched href and display text, potentially sending emails to the wrong address.

## Current State

```html
<a href="mailto:wclaytor@github.com">wclaytor@fastmail.com</a>
```

## Required Changes

- Ensure href and display text match the correct email address

## Acceptance Criteria

- [ ] Email href matches display text
- [ ] Email is the correct/preferred contact address
- [ ] Link is tested and functional

## References

- Part of Epic: BOFH Site Improvements 🔥
- **Priority: CRITICAL** - This is a bug that could cause missed communications
"""
    ),
    Issue(
        title="fix: Correct copyright date format in footer",
        labels=["bug", "quick-win", "priority-low"],
        body="""## Description

The copyright uses an unconventional pipe separator between years.

## Current State

```html
Copyright &copy; William Claytor 2023 | 2025
```

## Required Changes

- Use proper date range format with en-dash

## Expected Result

```html
Copyright &copy; 2023–2025 William Claytor
```

## Acceptance Criteria

- [ ] Copyright uses proper date range format (en-dash, not pipe)
- [ ] Year order is logical (start–end)
- [ ] Name placement is consistent with standards

## References

- Part of Epic: BOFH Site Improvements 🔥
"""
    ),
    Issue(
        title="feat: Add compelling tagline to masthead",
        labels=["enhancement", "content", "priority-medium"],
        body="""## Description

The masthead currently only displays the name in uppercase, missing an opportunity to immediately communicate value proposition.

## Current State

```html
<h1 class="mx-auto my-0 text-uppercase">william claytor</h1>
```

## Required Changes

- Add a subtitle/tagline beneath the name
- Consider adding a brief value proposition
- Ensure it's visually balanced and professional

## Suggested Taglines (pick one or similar)

- "Senior Software Engineer | QA Automation Expert"
- "25 Years Building Quality Software"
- "QA Automation Leader | Breaking Software So Users Don't Have To"

## Acceptance Criteria

- [ ] Tagline is present beneath the name
- [ ] Tagline communicates professional value
- [ ] Styling is consistent with site design
- [ ] Responsive on all screen sizes

## References

- Part of Epic: BOFH Site Improvements 🔥
"""
    ),
    Issue(
        title="chore: Remove unused sb-forms-latest.js script",
        labels=["performance", "technical-debt", "quick-win", "priority-medium"],
        body="""## Description

The site loads an external forms script that isn't being used, adding unnecessary page weight and an external dependency.

## Current State

```html
<script src="https://cdn.startbootstrap.com/sb-forms-latest.js"></script>
```

## Required Changes

- Remove the unused script tag
- Verify no functionality is broken

## Acceptance Criteria

- [ ] Script is removed
- [ ] No console errors after removal
- [ ] Page still functions correctly
- [ ] Page load time improves (measure before/after)

## References

- Part of Epic: BOFH Site Improvements 🔥
"""
    ),
    Issue(
        title="security: Add integrity attributes to external CDN scripts",
        labels=["security", "priority-medium"],
        body="""## Description

External CDN scripts lack integrity attributes, creating a security risk if those CDNs are compromised.

## Current State

```html
<script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
```

## Required Changes

- Add `integrity` and `crossorigin` attributes to all external scripts
- Consider adding fallback loading for critical scripts

## Acceptance Criteria

- [ ] All external scripts have integrity hashes
- [ ] crossorigin="anonymous" is present on all external resources
- [ ] Scripts still load and function correctly
- [ ] Security headers are appropriate

## References

- Part of Epic: BOFH Site Improvements 🔥
- [Subresource Integrity - MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
"""
    ),
    Issue(
        title="chore: Evaluate self-hosting vs CDN for critical assets",
        labels=["performance", "reliability", "priority-low"],
        body="""## Description

The site relies on three external CDNs (FontAwesome, jsDelivr, StartBootstrap). If any CDN has an outage, the site could be affected.

## Tasks

- [ ] Audit which external dependencies are critical
- [ ] Research pros/cons of self-hosting vs CDN
- [ ] Document decision and rationale
- [ ] Implement chosen approach

## Options to Evaluate

1. Keep CDNs with integrity attributes and fallbacks
2. Self-host all critical assets
3. Hybrid approach (CDN with local fallback)

## Acceptance Criteria

- [ ] Decision is documented
- [ ] Critical assets have fallback strategy
- [ ] Site works even if one CDN is unavailable
- [ ] Performance impact is measured

## References

- Part of Epic: BOFH Site Improvements 🔥
"""
    ),
    Issue(
        title="chore: Run comprehensive Lighthouse audit",
        labels=["quality", "testing", "priority-medium"],
        body="""## Description

After implementing the above fixes, run a full Lighthouse audit to measure improvements and identify any remaining issues.

## Tasks

- [ ] Run Lighthouse audit (Performance, Accessibility, Best Practices, SEO)
- [ ] Document baseline scores
- [ ] Address any new issues found
- [ ] Document final scores

## Acceptance Criteria

- [ ] Lighthouse Performance score >= 90
- [ ] Lighthouse Accessibility score >= 90
- [ ] Lighthouse Best Practices score >= 90
- [ ] Lighthouse SEO score >= 90
- [ ] Results are documented

## References

- Part of Epic: BOFH Site Improvements 🔥
- [Lighthouse Documentation](https://developers.google.com/web/tools/lighthouse)
"""
    ),
    Issue(
        title="feat: Create Open Graph image for social sharing",
        labels=["enhancement", "design", "priority-medium"],
        body="""## Description

Create a professional og-image that will display when the site is shared on social media.

## Requirements

- Size: 1200x630px (recommended for most platforms)
- Include: Name, title/role, professional visual
- Format: JPG or PNG (JPG preferred for file size)
- Location: `/assets/img/og-image.jpg`

## Acceptance Criteria

- [ ] Image is created and placed in correct location
- [ ] Image looks professional and on-brand
- [ ] Image displays correctly on LinkedIn, Twitter, Facebook
- [ ] File size is optimized (< 200KB if possible)

## References

- Part of Epic: BOFH Site Improvements 🔥
- Depends on: feat: Add Open Graph and Twitter Card meta tags
"""
    ),
]

EPIC_BODY = """## Overview

Address all issues identified in the BOFH site review to transform the main website from "competent" to "exceptional."

## Epic Summary

The Bastard Operator From Hell has reviewed our main website and found it... wanting. While the fundamentals are solid (it works, it's responsive, it has real projects), there are several issues that undermine the professional presentation expected from a Senior Software Engineer with 25 years of experience.

This epic tracks all improvements needed to address the BOFH's concerns and elevate the site to professional excellence.

## Child Issues

The following issues are part of this epic:

1. fix: Add missing meta description, author, and SEO tags
2. feat: Add Open Graph and Twitter Card meta tags
3. fix: Correct email link href/display mismatch
4. feat: Create Open Graph image for social sharing
5. fix: Correct copyright date format in footer
6. feat: Add compelling tagline to masthead
7. chore: Remove unused sb-forms-latest.js script
8. security: Add integrity attributes to external CDN scripts
9. chore: Evaluate self-hosting vs CDN for critical assets
10. chore: Run comprehensive Lighthouse audit

## Implementation Order (Recommended)

1. **Critical (Do First)**
   - Issue 3: Fix Email Link Mismatch

2. **Quick Wins (Easy, High Impact)**
   - Issue 1: Fix Empty Meta Tags
   - Issue 5: Fix Copyright Date Format
   - Issue 7: Remove Unused Script

3. **SEO Improvements**
   - Issue 2: Add Open Graph Tags
   - Issue 4: Create og-image

4. **Enhancements**
   - Issue 6: Enhance Masthead

5. **Security & Performance**
   - Issue 8: Add Subresource Integrity
   - Issue 9: Evaluate Self-Hosting

6. **Verification**
   - Issue 10: Lighthouse Audit

## Success Metrics

| Metric | Before | Target |
|--------|--------|--------|
| Lighthouse SEO | ~60 | 90+ |
| Lighthouse Best Practices | ~80 | 90+ |
| Meta tags filled | 0% | 100% |
| External scripts with integrity | 0 | All |
| BOFH Approval | 6.5/10 | 9+/10 |

## References

- [BOFH Site Review](/assets/docs/reviews/bofh-site-review.md)
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
- [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
- [Lighthouse Documentation](https://developers.google.com/web/tools/lighthouse)
"""


def run_command(cmd: list[str], dry_run: bool = False) -> tuple[int, str, str]:
    """Run a command and return exit code, stdout, stderr."""
    if dry_run:
        print(f"[DRY RUN] Would execute: {' '.join(cmd)}")
        return 0, "", ""
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def create_issue(issue: Issue, dry_run: bool = False) -> Optional[str]:
    """Create a GitHub issue using gh CLI. Returns issue URL on success."""
    cmd = [
        "gh", "issue", "create",
        "--title", issue.title,
        "--body", issue.body,
    ]
    
    # Add labels
    for label in issue.labels:
        cmd.extend(["--label", label])
    
    print(f"\n{'='*60}")
    print(f"Creating issue: {issue.title}")
    print(f"Labels: {', '.join(issue.labels)}")
    
    if dry_run:
        print(f"[DRY RUN] Command: gh issue create --title \"{issue.title}\" ...")
        print(f"[DRY RUN] Body preview (first 200 chars):")
        print(f"  {issue.body[:200]}...")
        return "https://github.com/wclaytor/wclaytor.github.io/issues/DRY-RUN"
    
    returncode, stdout, stderr = run_command(cmd, dry_run)
    
    if returncode != 0:
        print(f"❌ Error creating issue: {stderr}")
        return None
    
    issue_url = stdout.strip()
    print(f"✅ Created: {issue_url}")
    return issue_url


def ensure_labels_exist(labels: list[str], dry_run: bool = False) -> None:
    """Ensure all required labels exist in the repository."""
    print("\n" + "="*60)
    print("Checking/creating labels...")
    
    # Define label colors
    label_colors = {
        "epic": "7057ff",
        "enhancement": "a2eeef",
        "technical-debt": "d4c5f9",
        "seo": "0e8a16",
        "quick-win": "c5def5",
        "priority-high": "d93f0b",
        "priority-medium": "fbca04",
        "priority-low": "0e8a16",
        "priority-critical": "b60205",
        "bug": "d73a4a",
        "content": "bfdadc",
        "performance": "5319e7",
        "security": "ee0701",
        "reliability": "006b75",
        "quality": "1d76db",
        "testing": "bfd4f2",
        "design": "d4c5f9",
    }
    
    for label in labels:
        color = label_colors.get(label, "ededed")
        cmd = ["gh", "label", "create", label, "--color", color, "--force"]
        
        if dry_run:
            print(f"[DRY RUN] Would create label: {label} (color: #{color})")
        else:
            returncode, stdout, stderr = run_command(cmd)
            if returncode == 0:
                print(f"✅ Label '{label}' ready")
            else:
                # Label might already exist, that's OK
                print(f"ℹ️  Label '{label}': {stderr.strip() or 'exists'}")


def main():
    """Main function to create epic and child issues."""
    dry_run = "--dry-run" in sys.argv
    
    if dry_run:
        print("🔥 BOFH Epic Issue Creator - DRY RUN MODE 🔥")
        print("No issues will be created. Remove --dry-run to execute.")
    else:
        print("🔥 BOFH Epic Issue Creator 🔥")
    
    print("\n" + "="*60)
    print("This script will create:")
    print(f"  - 1 Epic issue")
    print(f"  - {len(CHILD_ISSUES)} child issues")
    print("="*60)
    
    if not dry_run:
        response = input("\nProceed? (y/N): ").strip().lower()
        if response != 'y':
            print("Aborted.")
            sys.exit(0)
    
    # Collect all unique labels
    all_labels = set(EPIC_LABELS)
    for issue in CHILD_ISSUES:
        all_labels.update(issue.labels)
    
    # Ensure labels exist
    ensure_labels_exist(list(all_labels), dry_run)
    
    # Create epic issue first
    epic_issue = Issue(
        title=EPIC_TITLE,
        body=EPIC_BODY,
        labels=EPIC_LABELS,
        is_epic=True
    )
    epic_url = create_issue(epic_issue, dry_run)
    
    # Create child issues
    created_issues = []
    failed_issues = []
    
    for issue in CHILD_ISSUES:
        url = create_issue(issue, dry_run)
        if url:
            created_issues.append((issue.title, url))
        else:
            failed_issues.append(issue.title)
    
    # Summary
    print("\n" + "="*60)
    print("📊 SUMMARY")
    print("="*60)
    
    if epic_url:
        print(f"\n✅ Epic created: {epic_url}")
    
    print(f"\n✅ Created {len(created_issues)} child issues:")
    for title, url in created_issues:
        print(f"   - {title}")
        print(f"     {url}")
    
    if failed_issues:
        print(f"\n❌ Failed to create {len(failed_issues)} issues:")
        for title in failed_issues:
            print(f"   - {title}")
    
    print("\n" + "="*60)
    if dry_run:
        print("🔥 DRY RUN COMPLETE - No issues were actually created 🔥")
        print("Run without --dry-run to create issues.")
    else:
        print("🔥 BOFH EPIC CREATION COMPLETE 🔥")
        print("Now go fix those issues before the BOFH notices...")


if __name__ == "__main__":
    main()