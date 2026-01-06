---
assignees: []
author: wclaytor
closed_at: null
comment_count: 0
created_at: '2026-01-05T21:37:16Z'
issue_number: 50
labels:
- enhancement
milestone: null
state: OPEN
title: 'Accessibility: Fix color contrast and heading hierarchy issues'
updated_at: '2026-01-05T21:37:16Z'
---

# Issue #50: Accessibility: Fix color contrast and heading hierarchy issues

## Description

## Summary

Automated accessibility testing with axe-core has identified the following WCAG violations:

### Color Contrast Issues (WCAG 2 AA Violations)

| Element | Current | Required | Details |
|---------|---------|----------|---------|
| `text-primary` (#64a19d) on white | 2.94:1 | 3:1 (large) / 4.5:1 (normal) | Card titles, headings |
| `text-black-50` (#808080) on white | 3.94:1 | 4.5:1 | Card descriptions |
| `btn-primary` (white on #64a19d) | 2.94:1 | 4.5:1 | View Project buttons |
| Footer `text-white-50` on black | 5.31:1 | 7:1 (AAA) | Copyright text |

### Heading Hierarchy Issues

- `h3.expertise-title` appears after `h1` (skips h2)
- Card titles use `h4`/`h5` without proper `h2`/`h3` parent sections
- Heading order is invalid according to WCAG best practices

### Recommended Fixes

1. **Color Contrast**
   - Change `--bs-primary` from #64a19d to a darker shade like #4a8179 (ratio ~4.5:1)
   - Change `text-black-50` usages to `text-secondary` or custom darker class
   - Or use `text-body-secondary` for better contrast

2. **Heading Hierarchy**
   - Add proper `h2` sections before `h3` content
   - Consider restructuring card headings or using `aria-level`

### Impact

- **Users affected**: Screen reader users, low vision users
- **WCAG Level**: AA (some AAA issues)
- **Priority**: High (color contrast is a common accessibility audit failure)

### References

- [WCAG 2.1 Contrast Requirements](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [axe-core color-contrast rule](https://dequeuniversity.com/rules/axe/4.8/color-contrast)

---

Discovered by automated testing in PR #49

## Notes

_Add your implementation notes, decisions, and documentation here._
