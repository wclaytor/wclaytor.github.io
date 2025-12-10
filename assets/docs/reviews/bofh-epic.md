# Epic: BOFH Site Improvements 🔥

## Overview

Address all issues identified in the BOFH site review to transform the main website from "competent" to "exceptional."

**Priority:** High  
**Labels:** `enhancement`, `technical-debt`, `seo`, `accessibility`  
**Milestone:** Site Refresh 2025  

---

## Epic Summary

The Bastard Operator From Hell has reviewed our main website and found it... wanting. While the fundamentals are solid (it works, it's responsive, it has real projects), there are several issues that undermine the professional presentation expected from a Senior Software Engineer with 25 years of experience.

This epic tracks all improvements needed to address the BOFH's concerns and elevate the site to professional excellence.

---

## Child Issues

### Issue 1: Fix Empty Meta Tags and Add SEO Metadata

**Title:** `fix: Add missing meta description, author, and SEO tags`

**Description:**
The site currently has empty meta description and author tags, which is SEO 101 failure.

**Current State:**
```html
<meta name="description" content="" />
<meta name="author" content="" />
```

**Required Changes:**
- Add meaningful meta description
- Add author meta tag
- Update page title to be more descriptive
- Add keywords meta tag (optional, but nice to have)

**Acceptance Criteria:**
- [ ] Meta description is filled with compelling, keyword-rich content
- [ ] Author meta tag is populated
- [ ] Page title includes name and role
- [ ] HTML validation passes

**Labels:** `seo`, `quick-win`, `priority-high`

---

### Issue 2: Add Open Graph and Social Media Meta Tags

**Title:** `feat: Add Open Graph and Twitter Card meta tags`

**Description:**
When the site is shared on LinkedIn, Twitter, or other social platforms, it displays poorly due to missing Open Graph tags.

**Required Changes:**
- Add Open Graph meta tags (og:type, og:title, og:description, og:url, og:image)
- Add Twitter Card meta tags
- Create or designate an og-image for social sharing

**Acceptance Criteria:**
- [ ] Open Graph tags are present and valid
- [ ] Twitter Card tags are present
- [ ] Social sharing preview looks professional (test with LinkedIn Post Inspector, Twitter Card Validator)
- [ ] og:image exists and is appropriately sized (1200x630px recommended)

**Labels:** `seo`, `enhancement`, `priority-high`

---

### Issue 3: Fix Email Link Mismatch

**Title:** `fix: Correct email link href/display mismatch`

**Description:**
The email link has a mismatched href and display text, potentially sending emails to the wrong address.

**Current State:**
```html
<a href="mailto:wclaytor@github.com">wclaytor@fastmail.com</a>
```

**Required Changes:**
- Ensure href and display text match the correct email address

**Acceptance Criteria:**
- [ ] Email href matches display text
- [ ] Email is the correct/preferred contact address
- [ ] Link is tested and functional

**Labels:** `bug`, `quick-win`, `priority-critical`

---

### Issue 4: Fix Copyright Date Format

**Title:** `fix: Correct copyright date format in footer`

**Description:**
The copyright uses an unconventional pipe separator between years.

**Current State:**
```html
Copyright &copy; William Claytor 2023 | 2025
```

**Required Changes:**
- Use proper date range format with en-dash

**Expected Result:**
```html
Copyright &copy; 2023–2025 William Claytor
```

**Acceptance Criteria:**
- [ ] Copyright uses proper date range format (en-dash, not pipe)
- [ ] Year order is logical (start–end)
- [ ] Name placement is consistent with standards

**Labels:** `bug`, `quick-win`, `priority-low`

---

### Issue 5: Enhance Masthead with Tagline

**Title:** `feat: Add compelling tagline to masthead`

**Description:**
The masthead currently only displays the name in uppercase, missing an opportunity to immediately communicate value proposition.

**Current State:**
```html
<h1 class="mx-auto my-0 text-uppercase">william claytor</h1>
```

**Required Changes:**
- Add a subtitle/tagline beneath the name
- Consider adding a brief value proposition
- Ensure it's visually balanced and professional

**Suggested Taglines (pick one or similar):**
- "Senior Software Engineer | QA Automation Expert"
- "25 Years Building Quality Software"
- "QA Automation Leader | Breaking Software So Users Don't Have To"

**Acceptance Criteria:**
- [ ] Tagline is present beneath the name
- [ ] Tagline communicates professional value
- [ ] Styling is consistent with site design
- [ ] Responsive on all screen sizes

**Labels:** `enhancement`, `content`, `priority-medium`

---

### Issue 6: Remove Unused External Script

**Title:** `chore: Remove unused sb-forms-latest.js script`

**Description:**
The site loads an external forms script that isn't being used, adding unnecessary page weight and an external dependency.

**Current State:**
```html
<script src="https://cdn.startbootstrap.com/sb-forms-latest.js"></script>
```

**Required Changes:**
- Remove the unused script tag
- Verify no functionality is broken

**Acceptance Criteria:**
- [ ] Script is removed
- [ ] No console errors after removal
- [ ] Page still functions correctly
- [ ] Page load time improves (measure before/after)

**Labels:** `performance`, `technical-debt`, `quick-win`, `priority-medium`

---

### Issue 7: Add Subresource Integrity to External CDN Scripts

**Title:** `security: Add integrity attributes to external CDN scripts`

**Description:**
External CDN scripts lack integrity attributes, creating a security risk if those CDNs are compromised.

**Current State:**
```html
<script src="https://use.fontawesome.com/releases/v6.1.0/js/all.js" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
```

**Required Changes:**
- Add `integrity` and `crossorigin` attributes to all external scripts
- Consider adding fallback loading for critical scripts

**Acceptance Criteria:**
- [ ] All external scripts have integrity hashes
- [ ] crossorigin="anonymous" is present on all external resources
- [ ] Scripts still load and function correctly
- [ ] Security headers are appropriate

**Labels:** `security`, `priority-medium`

---

### Issue 8: Evaluate Self-Hosting Critical Assets

**Title:** `chore: Evaluate self-hosting vs CDN for critical assets`

**Description:**
The site relies on three external CDNs (FontAwesome, jsDelivr, StartBootstrap). If any CDN has an outage, the site could be affected.

**Tasks:**
- Audit which external dependencies are critical
- Research pros/cons of self-hosting vs CDN
- Document decision and rationale
- Implement chosen approach

**Options to Evaluate:**
1. Keep CDNs with integrity attributes and fallbacks
2. Self-host all critical assets
3. Hybrid approach (CDN with local fallback)

**Acceptance Criteria:**
- [ ] Decision is documented
- [ ] Critical assets have fallback strategy
- [ ] Site works even if one CDN is unavailable
- [ ] Performance impact is measured

**Labels:** `performance`, `reliability`, `priority-low`

---

### Issue 9: Run Lighthouse Audit and Address Findings

**Title:** `chore: Run comprehensive Lighthouse audit`

**Description:**
After implementing the above fixes, run a full Lighthouse audit to measure improvements and identify any remaining issues.

**Tasks:**
- Run Lighthouse audit (Performance, Accessibility, Best Practices, SEO)
- Document baseline scores
- Address any new issues found
- Document final scores

**Acceptance Criteria:**
- [ ] Lighthouse Performance score >= 90
- [ ] Lighthouse Accessibility score >= 90
- [ ] Lighthouse Best Practices score >= 90
- [ ] Lighthouse SEO score >= 90
- [ ] Results are documented

**Labels:** `quality`, `testing`, `priority-medium`

---

### Issue 10: Create og-image for Social Sharing

**Title:** `feat: Create Open Graph image for social sharing`

**Description:**
Create a professional og-image that will display when the site is shared on social media.

**Requirements:**
- Size: 1200x630px (recommended for most platforms)
- Include: Name, title/role, professional visual
- Format: JPG or PNG (JPG preferred for file size)
- Location: `/assets/img/og-image.jpg`

**Acceptance Criteria:**
- [ ] Image is created and placed in correct location
- [ ] Image looks professional and on-brand
- [ ] Image displays correctly on LinkedIn, Twitter, Facebook
- [ ] File size is optimized (< 200KB if possible)

**Labels:** `enhancement`, `design`, `priority-medium`

---

## Implementation Order (Recommended)

1. **Critical (Do First)**
   - Issue 3: Fix Email Link Mismatch

2. **Quick Wins (Easy, High Impact)**
   - Issue 1: Fix Empty Meta Tags
   - Issue 4: Fix Copyright Date Format
   - Issue 6: Remove Unused Script

3. **SEO Improvements**
   - Issue 2: Add Open Graph Tags
   - Issue 10: Create og-image

4. **Enhancements**
   - Issue 5: Enhance Masthead

5. **Security & Performance**
   - Issue 7: Add Subresource Integrity
   - Issue 8: Evaluate Self-Hosting

6. **Verification**
   - Issue 9: Lighthouse Audit

---

## Success Metrics

| Metric | Before | Target |
|--------|--------|--------|
| Lighthouse SEO | ~60 | 90+ |
| Lighthouse Best Practices | ~80 | 90+ |
| Meta tags filled | 0% | 100% |
| External scripts with integrity | 0 | All |
| BOFH Approval | 6.5/10 | 9+/10 |

---

## References

- [BOFH Site Review](/assets/docs/reviews/bofh-site-review.md)
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
- [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
- [Lighthouse Documentation](https://developers.google.com/web/tools/lighthouse)