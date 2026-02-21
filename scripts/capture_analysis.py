"""
Comprehensive visual and mobile rendering analysis for mygnathia.com.
Captures desktop + mobile screenshots for all key pages and extracts
layout, accessibility, and visual hierarchy data.
"""
from playwright.sync_api import sync_playwright
import json
import os

SCREENSHOT_DIR = r"C:\personal projects\claude-seo\screenshots"
os.makedirs(os.path.join(SCREENSHOT_DIR, "desktop"), exist_ok=True)
os.makedirs(os.path.join(SCREENSHOT_DIR, "mobile"), exist_ok=True)

PAGES = [
    {"url": "https://mygnathia.com", "name": "homepage"},
    {"url": "https://mygnathia.com/accommodations", "name": "accommodations"},
    {"url": "https://mygnathia.com/gallery", "name": "gallery"},
    {"url": "https://mygnathia.com/construction", "name": "construction"},
    {"url": "https://mygnathia.com/about", "name": "about"},
    {"url": "https://mygnathia.com/contact", "name": "contact"},
]

VIEWPORTS = [
    {"name": "desktop", "width": 1920, "height": 1080},
    {"name": "mobile", "width": 375, "height": 812, "is_mobile": True, "device_scale_factor": 3},
]


def analyze_page(page, page_name, viewport_name):
    """Extract layout, accessibility, and visual data from a page."""
    data = page.evaluate("""() => {
        const results = {};

        // Viewport meta tag
        const vpMeta = document.querySelector('meta[name="viewport"]');
        results.viewportMeta = vpMeta ? vpMeta.getAttribute('content') : 'MISSING';

        // Page title
        results.title = document.title;

        // Meta description
        const metaDesc = document.querySelector('meta[name="description"]');
        results.metaDescription = metaDesc ? metaDesc.content : null;

        // H1 elements
        const h1s = document.querySelectorAll('h1');
        results.h1Elements = Array.from(h1s).map(h => ({
            text: h.textContent.trim().substring(0, 200),
            rect: h.getBoundingClientRect(),
            fontSize: getComputedStyle(h).fontSize,
            fontWeight: getComputedStyle(h).fontWeight,
            color: getComputedStyle(h).color,
            isAboveFold: h.getBoundingClientRect().top < window.innerHeight,
        }));

        // All headings hierarchy
        const headings = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
        results.headingHierarchy = Array.from(headings).slice(0, 40).map(h => ({
            tag: h.tagName,
            text: h.textContent.trim().substring(0, 100),
            visible: h.getBoundingClientRect().height > 0,
        }));

        // CTA buttons / links
        const buttons = document.querySelectorAll('button, a[class*="btn"], a[class*="button"], a[class*="cta"], [role="button"], a[href*="contact"], a[href*="book"], a[href*="enquir"], a[href*="whatsapp"]');
        results.ctaElements = Array.from(buttons).slice(0, 25).map(b => {
            const rect = b.getBoundingClientRect();
            const style = getComputedStyle(b);
            return {
                tag: b.tagName,
                text: b.textContent.trim().substring(0, 100),
                href: b.href || '',
                rect: { top: rect.top, left: rect.left, width: rect.width, height: rect.height },
                fontSize: style.fontSize,
                backgroundColor: style.backgroundColor,
                color: style.color,
                isAboveFold: rect.top < window.innerHeight && rect.bottom > 0,
                touchTargetOk: rect.width >= 48 && rect.height >= 48,
            };
        });

        // All above-fold links (for CTA detection)
        const allLinks = document.querySelectorAll('a');
        results.aboveFoldLinks = Array.from(allLinks).filter(a => {
            const r = a.getBoundingClientRect();
            return r.top < window.innerHeight && r.bottom > 0 && r.width > 0;
        }).slice(0, 30).map(a => ({
            text: a.textContent.trim().substring(0, 80),
            href: a.href,
            rect: a.getBoundingClientRect(),
            classes: a.className.substring(0, 100),
        }));

        // Navigation
        const nav = document.querySelector('nav, [role="navigation"]');
        const header = document.querySelector('header');
        const navEl = nav || header;
        results.navigation = navEl ? {
            exists: true,
            tag: navEl.tagName,
            rect: navEl.getBoundingClientRect(),
            links: Array.from(navEl.querySelectorAll('a')).slice(0, 20).map(a => ({
                text: a.textContent.trim().substring(0, 50),
                href: a.href,
                visible: a.getBoundingClientRect().width > 0 && a.getBoundingClientRect().height > 0,
                rect: { width: a.getBoundingClientRect().width, height: a.getBoundingClientRect().height },
            })),
        } : { exists: false };

        // Hamburger / mobile menu
        const hamburger = document.querySelector(
            '[class*="hamburger"], [class*="menu-toggle"], [class*="mobile-menu"], ' +
            '[aria-label*="menu"], [aria-label*="Menu"], button[class*="nav"], ' +
            '.navbar-toggler, [class*="toggle"], [data-toggle="collapse"]'
        );
        results.hamburgerMenu = hamburger ? {
            exists: true,
            visible: hamburger.getBoundingClientRect().width > 0 && hamburger.getBoundingClientRect().height > 0,
            rect: hamburger.getBoundingClientRect(),
            ariaLabel: hamburger.getAttribute('aria-label'),
            ariaExpanded: hamburger.getAttribute('aria-expanded'),
            tagName: hamburger.tagName,
            classes: hamburger.className.substring(0, 150),
        } : { exists: false };

        // Images analysis
        const images = document.querySelectorAll('img');
        results.images = Array.from(images).slice(0, 30).map(img => ({
            src: img.src ? img.src.substring(0, 200) : '',
            alt: img.alt,
            hasAlt: img.hasAttribute('alt'),
            altEmpty: img.alt === '',
            isAboveFold: img.getBoundingClientRect().top < window.innerHeight,
            naturalWidth: img.naturalWidth,
            naturalHeight: img.naturalHeight,
            loading: img.getAttribute('loading'),
        }));

        // Body font size
        results.bodyFontSize = getComputedStyle(document.body).fontSize;

        // Check paragraph font size too
        const firstP = document.querySelector('p');
        results.paragraphFontSize = firstP ? getComputedStyle(firstP).fontSize : null;

        // Check horizontal overflow
        results.horizontalOverflow = document.documentElement.scrollWidth > document.documentElement.clientWidth;
        results.pageWidth = document.documentElement.scrollWidth;
        results.viewportWidth = document.documentElement.clientWidth;

        // Touch target analysis
        const allClickable = document.querySelectorAll('a, button, input, select, textarea, [role="button"]');
        let smallTargets = [];
        let totalVisible = 0;
        Array.from(allClickable).forEach(el => {
            const rect = el.getBoundingClientRect();
            if (rect.width > 0 && rect.height > 0) {
                totalVisible++;
                if (rect.width < 44 || rect.height < 44) {
                    smallTargets.push({
                        tag: el.tagName,
                        text: el.textContent.trim().substring(0, 50),
                        width: Math.round(rect.width),
                        height: Math.round(rect.height),
                    });
                }
            }
        });
        results.touchTargets = {
            totalVisible: totalVisible,
            smallCount: smallTargets.length,
            smallTargets: smallTargets.slice(0, 15),
        };

        // Skip navigation links
        const skipLinks = document.querySelectorAll('a[href="#main"], a[href="#content"], a[class*="skip"], [class*="skip-nav"]');
        results.skipNavigation = skipLinks.length > 0;

        // Focus indicators - check if outline is removed globally
        const allFocusable = document.querySelectorAll('a, button, input, select, textarea');
        let focusOutlineRemoved = 0;
        Array.from(allFocusable).slice(0, 20).forEach(el => {
            const style = getComputedStyle(el);
            if (style.outlineStyle === 'none' || style.outline === 'none' ||
                style.outlineWidth === '0px') {
                focusOutlineRemoved++;
            }
        });
        results.focusIndicators = {
            totalChecked: Math.min(allFocusable.length, 20),
            outlineRemovedCount: focusOutlineRemoved,
        };

        // Hero section detection
        const heroSelectors = [
            '[class*="hero"]', '[class*="Hero"]', '[class*="banner"]',
            '[class*="Banner"]', '[class*="slider"]', '[class*="Slider"]',
            '[class*="carousel"]'
        ];
        let hero = null;
        for (const sel of heroSelectors) {
            hero = document.querySelector(sel);
            if (hero) break;
        }
        if (!hero) {
            hero = document.querySelector('section:first-of-type, main > div:first-child');
        }
        if (hero) {
            const heroRect = hero.getBoundingClientRect();
            const heroBg = getComputedStyle(hero).backgroundImage;
            results.heroSection = {
                exists: true,
                selector: hero.className.substring(0, 100),
                rect: { top: heroRect.top, left: heroRect.left, width: heroRect.width, height: heroRect.height },
                hasBackgroundImage: heroBg !== 'none',
                backgroundImage: heroBg.substring(0, 300),
            };
        } else {
            results.heroSection = { exists: false };
        }

        // Color contrast sampling
        const textElements = document.querySelectorAll('p, span, a, h1, h2, h3, li');
        results.colorSamples = Array.from(textElements).slice(0, 15).map(el => {
            const style = getComputedStyle(el);
            return {
                tag: el.tagName,
                text: el.textContent.trim().substring(0, 50),
                color: style.color,
                backgroundColor: style.backgroundColor,
                fontSize: style.fontSize,
            };
        });

        // Lang attribute
        results.htmlLang = document.documentElement.getAttribute('lang');

        // Schema.org markup
        const schemas = document.querySelectorAll('script[type="application/ld+json"]');
        results.schemaCount = schemas.length;
        results.schemas = Array.from(schemas).map(s => {
            try {
                const parsed = JSON.parse(s.textContent);
                return parsed['@type'] || (parsed['@graph'] ? 'Graph' : 'Unknown');
            } catch(e) { return 'ParseError'; }
        });

        // Open Graph tags
        const ogTags = document.querySelectorAll('meta[property^="og:"]');
        results.ogTags = Array.from(ogTags).map(t => ({
            property: t.getAttribute('property'),
            content: t.content ? t.content.substring(0, 150) : null,
        }));

        // Performance hints
        results.preloadLinks = document.querySelectorAll('link[rel="preload"]').length;
        results.prefetchLinks = document.querySelectorAll('link[rel="prefetch"]').length;
        results.lazyImages = document.querySelectorAll('img[loading="lazy"]').length;
        results.totalImages = document.querySelectorAll('img').length;

        return results;
    }""")
    return data


def run():
    all_results = {}

    with sync_playwright() as p:
        for vp in VIEWPORTS:
            browser = p.chromium.launch()
            context_opts = {
                "viewport": {"width": vp["width"], "height": vp["height"]},
            }
            if vp.get("is_mobile"):
                context_opts["is_mobile"] = True
                context_opts["device_scale_factor"] = vp.get("device_scale_factor", 2)
                context_opts["user_agent"] = (
                    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) "
                    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 "
                    "Mobile/15E148 Safari/604.1"
                )

            context = browser.new_context(**context_opts)
            page = context.new_page()

            for pg in PAGES:
                key = f"{pg['name']}_{vp['name']}"
                vp_dir = os.path.join(SCREENSHOT_DIR, vp["name"])
                print(f"\n--- Capturing: {key} ---")

                try:
                    page.goto(pg["url"], wait_until="networkidle", timeout=45000)
                    page.wait_for_timeout(2500)  # Extra settle time for animations

                    # Above-the-fold screenshot
                    atf_path = os.path.join(vp_dir, f"{pg['name']}_atf.png")
                    page.screenshot(path=atf_path, full_page=False)
                    print(f"  Saved above-fold: {atf_path}")

                    # Full page screenshot
                    full_path = os.path.join(vp_dir, f"{pg['name']}_full.png")
                    page.screenshot(path=full_path, full_page=True)
                    print(f"  Saved full page: {full_path}")

                    # Analyze page data
                    data = analyze_page(page, pg["name"], vp["name"])
                    all_results[key] = data
                    print(f"  Analysis complete. H1s: {len(data.get('h1Elements', []))}, "
                          f"Images: {data.get('totalImages', 0)}")

                except Exception as e:
                    print(f"  ERROR: {e}")
                    all_results[key] = {"error": str(e)}

            # Mobile-specific: test hamburger menu interaction
            if vp.get("is_mobile"):
                print(f"\n--- Testing mobile menu interaction ---")
                try:
                    page.goto("https://mygnathia.com", wait_until="networkidle", timeout=30000)
                    page.wait_for_timeout(1500)

                    # Try various hamburger selectors
                    hamburger_selectors = [
                        '[class*="hamburger"]',
                        '[class*="menu-toggle"]',
                        '[class*="mobile-menu"]',
                        'button[aria-label*="menu"]',
                        'button[aria-label*="Menu"]',
                        '.navbar-toggler',
                        '[class*="toggle"]',
                        'nav button',
                        'header button',
                        '[data-toggle]',
                    ]
                    clicked = False
                    for sel in hamburger_selectors:
                        el = page.query_selector(sel)
                        if el and el.is_visible():
                            el.click()
                            page.wait_for_timeout(1000)
                            menu_path = os.path.join(SCREENSHOT_DIR, "mobile", "menu_open.png")
                            page.screenshot(path=menu_path, full_page=False)
                            print(f"  Clicked hamburger ({sel}), saved: {menu_path}")
                            all_results["mobile_menu_test"] = {
                                "found": True,
                                "selector": sel,
                                "clicked": True,
                            }
                            clicked = True
                            break
                    if not clicked:
                        print("  No visible hamburger menu button found")
                        all_results["mobile_menu_test"] = {"found": False}

                except Exception as e:
                    print(f"  Menu test error: {e}")
                    all_results["mobile_menu_test"] = {"error": str(e)}

            context.close()
            browser.close()

    # Save analysis data
    json_path = os.path.join(SCREENSHOT_DIR, "analysis_data.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nAll analysis data saved to: {json_path}")


if __name__ == "__main__":
    run()
