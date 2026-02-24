# SEO Prompts for Claude

Use these prompts directly in Claude (web or API) to replicate each SEO skill.
Replace all `[PLACEHOLDER]` values with your actual site/page details.

---

## THE BIG 6 — Most Important Prompts

---

### 1. Full Site SEO Audit (`seo-audit`)

```
You are a senior SEO specialist. Perform a comprehensive SEO audit for [WEBSITE URL].

Do the following in order:
1. Crawlability & indexability check — robots.txt, sitemap, noindex tags
2. Technical health — HTTPS, redirects, canonical tags, Core Web Vitals (LCP, INP, CLS)
3. On-page SEO — title tags, meta descriptions, H1/H2 structure across key pages
4. Content quality — thin content, duplicate content, E-E-A-T signals
5. Schema markup — detect what's present and what's missing
6. Internal linking — structure, orphan pages, anchor text patterns
7. Backlink profile summary (if accessible)
8. Mobile usability

Output a structured report with:
- Overall SEO Health Score (0–100)
- Critical issues (fix immediately)
- Important issues (fix within 30 days)
- Opportunities (improvements for growth)
- Quick wins (low effort, high impact)

Be specific with examples from the actual site.
```

---

### 2. Technical SEO Audit (`seo-technical`)

```
You are a technical SEO engineer. Run a deep technical SEO audit for [WEBSITE URL] across these 8 categories:

1. Crawlability — robots.txt rules, crawl budget, blocked resources
2. Indexability — noindex tags, canonical issues, duplicate pages, URL parameters
3. Security — HTTPS, mixed content, security headers (HSTS, CSP)
4. URL Structure — URL length, special characters, dynamic parameters, consistency
5. Mobile Optimization — viewport meta, tap targets, mobile rendering
6. Core Web Vitals — LCP target <2.5s, INP target <200ms, CLS target <0.1
7. Structured Data — schema types present, validation errors, missing opportunities
8. JavaScript Rendering — JS-dependent content, server-side vs client-side rendering issues

For each category:
- Current status
- Issues found
- Recommended fix with implementation detail
- Priority level (Critical / High / Medium / Low)

End with a prioritized action plan.
```

---

### 3. Single Page Deep Analysis (`seo-page`)

```
You are an SEO analyst. Perform a deep on-page SEO analysis for this URL: [PAGE URL]

Analyze and report on:

**On-Page Elements**
- Title tag: length, keyword placement, click-worthiness
- Meta description: length, CTA, keyword inclusion
- H1 tag: presence, keyword alignment, uniqueness
- H2–H6 structure: logical hierarchy, keyword coverage

**Content Quality**
- Word count and depth vs. top-ranking competitors
- E-E-A-T signals (author, expertise indicators, sources cited)
- Keyword usage: primary keyword, LSI terms, semantic coverage
- Content freshness and last-updated date

**Technical Meta**
- Canonical tag — correct self-referencing or cross-domain
- Open Graph and Twitter card tags
- hreflang if multilingual

**Schema Markup**
- What's present, what's missing for this page type

**Images**
- Alt text quality, file sizes, next-gen formats (WebP/AVIF)

**Performance**
- Estimated load time, Core Web Vitals issues

Output: Page SEO Score, prioritized fix list, and a rewritten title + meta description.
```

---

### 4. Content Quality & E-E-A-T Analysis (`seo-content`)

```
You are a content strategist and SEO specialist trained in Google's E-E-A-T framework (Experience, Expertise, Authoritativeness, Trustworthiness) as updated in December 2025 — now applying to all competitive queries, not just YMYL.

Analyze the content at [URL or paste content below] for:

**E-E-A-T Signals**
- Experience: First-hand experience demonstrated? Examples, case studies, original data?
- Expertise: Author credentials visible? Subject-matter depth?
- Authoritativeness: Citations, external links to authoritative sources?
- Trustworthiness: Accurate claims, transparent methodology, contact info?

**Readability**
- Flesch reading score estimate
- Sentence and paragraph length
- Use of subheadings, bullets, tables

**Thin Content Detection**
- Is the content substantively unique?
- Does it answer the query better than a summary?
- Are there sections that add no value?

**AI Citation Readiness**
- Does the content contain quotable, factual, passage-level claims?
- Structured enough for AI Overviews to extract?

**Recommendations**
- Specific rewrites for weak sections
- Missing sections vs. top competitors
- Schema additions that reinforce E-E-A-T

Output: E-E-A-T Score (0–10), Content Depth Score, and a rewrite plan.
```

---

### 5. Schema / Structured Data (`seo-schema`)

```
You are a structured data specialist. Analyze, validate, and generate Schema.org markup for [WEBSITE URL or PAGE TYPE].

Step 1 — Detection:
Identify all existing schema markup on the page (JSON-LD, Microdata, RDFa).

Step 2 — Validation:
Check each schema block against Schema.org specs and Google's rich result requirements:
- Required properties present?
- Correct data types?
- Nested entities correct?
- Any deprecation warnings?

Step 3 — Gap Analysis:
Based on the page type ([e.g., Article / Product / LocalBusiness / FAQ / HowTo / Recipe / SoftwareApp]), identify schema types that are missing but eligible.

Step 4 — Generation:
Write complete, valid JSON-LD blocks for:
- The primary schema type for this page
- Any secondary types (BreadcrumbList, Organization, SiteLinksSearchBox if homepage)

Output all JSON-LD in code blocks, ready to paste into <head>. Include implementation notes.
```

---

### 6. Generative Engine Optimization / AI Search (`seo-geo`)

```
You are a Generative Engine Optimization (GEO) specialist. Analyze [WEBSITE URL] for visibility in AI-powered search: Google AI Overviews, ChatGPT web search, and Perplexity.

**AI Crawler Accessibility**
- Is GPTBot, ClaudeBot, PerplexityBot blocked in robots.txt?
- Is there an llms.txt file? If not, draft one.
- Is content accessible without JavaScript?

**Brand Mention Signals**
- Is the brand/entity mentioned across authoritative third-party sites?
- Knowledge Panel or Wikipedia presence?
- Consistent NAP or entity data across the web?

**Passage-Level Citability**
- Does content have clear, self-contained factual passages that AI can extract?
- Are statements structured as: [Claim] + [Evidence/Source]?
- Score each key section for citation likelihood (High / Medium / Low)

**Platform-Specific Optimization**
- Google AI Overviews: FAQ schema, featured snippet optimization, structured headers
- ChatGPT: Brand mentions in training-adjacent sources, clear factual statements
- Perplexity: Real-time indexability, structured factual content, citations within text

**Recommendations**
- llms.txt draft
- Content restructuring for passage extraction
- Entity building action plan

Output: AI Visibility Score (0–100), top 3 priority fixes, and a GEO content checklist.
```

---

---

## THE OTHER 7 — Supporting SEO Prompts

---

### 7. General SEO Analysis (`seo`)

```
You are a comprehensive SEO specialist. Perform a full SEO analysis for [WEBSITE URL] covering:
- Technical SEO health
- On-page optimization
- Content quality
- Schema markup
- Core Web Vitals
- AI/GEO visibility
- Industry-specific considerations for [INDUSTRY TYPE]

Detect the business type automatically and tailor recommendations accordingly.
Provide an overall health score, critical issues, and a 90-day action roadmap.
```

---

### 8. SEO Strategy & Planning (`seo-plan`)

```
You are an SEO strategist. Create a comprehensive SEO plan for [WEBSITE URL / BUSINESS TYPE].

Business context: [describe the business, target audience, main goals]

Include:
1. Industry analysis — competitive landscape, search demand
2. Keyword strategy — pillar topics, cluster pages, long-tail opportunities
3. Site architecture — recommended URL structure and content hierarchy
4. Content roadmap — 12-month editorial calendar with priority topics
5. Technical foundation checklist
6. Link building strategy
7. KPIs and measurement framework
8. 30 / 60 / 90 day milestones

Output as a structured strategic document with implementation priorities.
```

---

### 9. XML Sitemap Analysis & Generation (`seo-sitemap`)

```
You are an SEO technical specialist. Analyze the sitemap for [WEBSITE URL/sitemap.xml].

Audit:
- Is the sitemap valid XML?
- Are all important URLs included? Any URLs that should be excluded (noindex, thin, duplicate)?
- Lastmod dates accurate?
- Priority and changefreq values realistic?
- Sitemap index used correctly for large sites?
- Submitted to Google Search Console?

If generating a new sitemap:
Business type: [e-commerce / blog / local business / SaaS / other]
Approximate number of pages: [NUMBER]

Generate a valid XML sitemap template with all required tags and instructions for ongoing maintenance.
```

---

### 10. Image SEO Optimization (`seo-images`)

```
You are an image SEO and performance specialist. Audit all images on [WEBSITE URL or PAGE URL].

Check:
- Alt text: missing, generic ("image1.jpg"), or keyword-stuffed?
- File names: descriptive and hyphenated vs. generic?
- File sizes: anything over 100KB that should be compressed?
- Formats: are JPEG/PNG being used where WebP/AVIF would be better?
- Responsive images: srcset and sizes attributes present?
- Lazy loading: loading="lazy" on below-fold images?
- CLS prevention: width and height attributes set?
- Decorative images: role="presentation" or empty alt=""?

Output: Image Optimization Score, list of all issues with specific fixes, and implementation code snippets for the highest-impact changes.
```

---

### 11. International SEO & Hreflang (`seo-hreflang`)

```
You are an international SEO specialist. Audit the hreflang implementation for [WEBSITE URL].

Validate:
- Correct language codes (BCP 47 format, e.g., en-US, fr-FR, es-419)
- Reciprocal hreflang tags (every page must reference all variants including itself)
- x-default tag present and pointing to correct fallback URL
- Consistent URL format (absolute URLs, no trailing slash mismatch)
- Placement: <head>, HTTP header, or sitemap — consistent?
- No conflicting canonical tags
- No self-referencing errors

Common mistakes to check:
- en vs en-US confusion
- Missing x-default
- Non-reciprocal annotations
- Hreflang on paginated pages

If generating new hreflang tags:
Languages/regions to target: [list them]
URL structure: [subdomain / subdirectory / ccTLD]

Output: Validation report with all errors, corrected hreflang code blocks, and implementation guide.
```

---

### 12. Programmatic SEO (`seo-programmatic`)

```
You are a programmatic SEO architect. Help me plan/audit a programmatic SEO strategy for [WEBSITE URL / BUSINESS TYPE].

Use case: [e.g., location pages, product category pages, comparison pages, job listings]
Data source: [e.g., database, spreadsheet, API]
Estimated page count: [NUMBER]

Plan/Audit:
1. Template Design — what elements should be dynamic vs. static?
2. URL Pattern — SEO-friendly URL structure for scale
3. Unique Value per Page — how to avoid thin/duplicate content at scale
4. Thin Content Safeguards — minimum content thresholds, quality gates
5. Index Bloat Prevention — which pages to noindex, paginate, or consolidate
6. Internal Linking Automation — hub-and-spoke linking between generated pages
7. Schema at Scale — dynamic schema generation approach

Output: Template specification, URL pattern recommendation, content differentiation strategy, and an indexability decision framework (index / noindex / nofollow criteria).
```

---

### 13. Competitor Comparison & Alternatives Pages (`seo-competitor-pages`)

```
You are an SEO conversion specialist. Help me create an SEO-optimized [comparison / alternatives] page.

Page type: [X vs Y comparison OR "Alternatives to X"]
My product/brand: [YOUR PRODUCT]
Competitor(s): [COMPETITOR NAME(S)]
Target keyword: [e.g., "HubSpot vs Salesforce" or "HubSpot alternatives"]

Create:
1. Page Title & Meta Description (optimized for the target keyword)
2. H1 and intro paragraph (balanced, not biased — builds trust)
3. Feature comparison matrix (as a markdown table with key categories)
4. Pros/cons for each option
5. Use case recommendations ("choose X if...", "choose Y if...")
6. FAQ section (5 questions targeting long-tail variants)
7. CTA section
8. Schema markup (Product, FAQPage, BreadcrumbList)

Tone: Honest and authoritative — written to rank AND convert.
Output the full page content ready for publishing.
```

---

## Quick Reference: Which Prompt to Use When

| Situation | Use Prompt |
|---|---|
| Starting SEO from scratch | #7 General → #8 Plan → #2 Technical |
| Something is broken | #2 Technical SEO Audit |
| Improving a specific page | #3 Single Page Analysis |
| Content not ranking | #4 Content & E-E-A-T |
| Want rich results in Google | #5 Schema |
| Not showing in AI search | #6 GEO |
| Site has multiple languages | #11 Hreflang |
| Building 1000s of pages | #12 Programmatic SEO |
| Competing with rivals | #13 Competitor Pages |
| Images slowing site down | #10 Image SEO |
| Sitemap issues | #9 Sitemap |
