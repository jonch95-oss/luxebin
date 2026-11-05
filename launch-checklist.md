# Luxebin launch checklist

Status key: [x] done and verified · [~] done, needs a check from you · [ ] not yet

## Catalogue
- [x] 26 products / 29 variants, all with price, vendor, product type and tags
- [x] Retail (compare-at) on 23 of 29 variants, set at 15% below retail with a 45% margin floor; 6 shown without a struck-through price because no retail price could be verified (both Drunk Elephant minis, Laneige set, Maybelline 315, Estée Lauder 7 ml); Olaplex set uses a $58 "stated value"
- [x] Descriptions rewritten; Key benefits on 26/26, How to use on 23/26, full ingredients on 16/26
- [ ] Images: 18 of 26 products have images; 8 need photos of your own stock (B-Hydra mini, Lala travel, r.e.m. gloss x2 shades, Estée Lauder, CoverGirl, Maybelline, Florence by Mills, Laneige set)
- [~] Check against the physical product: Maybelline 315 (gloss or lipstick?), Rare Beauty luminizer size, Protini mini size, Laneige set contents
- [x] SEO title and description on all 26 products and 25 collections

## Collections and navigation
- [x] Automated collections: Makeup 16 (Lips 10, Face 6), Skincare 6, Body & Hair 4 (Body Care 2, Hair Care 2), 16 brand collections
- [x] Curated: Best Sellers 8, New Arrivals 8 (hand-picked until sales data exists)
- [x] No empty collections
- [x] Menus: luxebin-main (mega menu), footer Shop / Help / Luxebin

## Theme ("Luxebin — Warm Luxury v3", unpublished, built on Dawn 16.0.0)
- [x] Direction B tokens, Cormorant Garamond + Jost, metallic wordmark
- [x] Homepage sections in brief order
- [x] Product page: brand link, title, price with retail struck through and Save X%, shade pills, accordions, authenticity badge, sticky add-to-bag on mobile, You may also like
- [x] Cart drawer with final-sale note
- [x] Theme check: 0 errors
- [x] Walkthrough screenshots in screens/: homepage desktop + mobile, Makeup collection desktop + mobile, 10 product pages, product page mobile, Authenticity page, 404. No Liquid errors, no sideways scroll at 390px, cream background and header on every page
- [x] Lighthouse (2026-11-05, live site). Home mobile: Performance 76, Accessibility 96, Best Practices 75, SEO 92. Home desktop: 94 / 96 / 74 / 92. Collection mobile: 86 / 96 / 75 / 100. Best Practices is held back by app third-party cookies and console errors (outside the theme)
- [ ] Homepage meta description (SEO 92 → 100): Online Store → Preferences → Meta description. Paste: "Prestige beauty, 100% authentic and guaranteed, for less than retail. Shop Olaplex, Rare Beauty, K18, Glow Recipe and more at Luxebin." (the theme fallback is in the repo, but the connector can't write to the live theme)
- [ ] Publish theme v3 (on your go-ahead). Old themes "Dawn 16 import", "Luxebin v1" and "Luxebin v2" can be deleted

## Pages and policies
- [x] Pages: About, Authenticity Guarantee, FAQ, Contact (existing)
- [ ] Policies: written (content/policies/*.html) but the API cannot save them; paste in Settings → Policies
- [~] Blog "Journal": 3 posts written and saved as hidden drafts (routine, layering serums, labels); publish after you've seen them in the theme

## Settings
- [x] Market: United States only, USD
- [x] Customer accounts: optional
- [x] Store name: Luxebin
- [ ] Free shipping threshold: currently $70 on Standard; change to $50 in Settings → Shipping and delivery → General profile → Domestic → Standard
- [ ] Store contact/sender email: currently a personal Gmail; set support@luxebin.co in Settings → General once the mailbox exists
- [ ] Payments: confirm Shop Pay, Apple Pay, Google Pay, PayPal, Klarna/Afterpay enabled (Settings → Payments)
- [ ] Taxes: NY nexus only (Settings → Taxes and duties)
- [ ] Order/shipping notification emails restyled
- [ ] Checkout branding: the API is locked on Basic, so set it in Settings → Checkout → Customize. Logo: brand/wordmark-dark.svg (export a PNG). Background #FAF6EF, order summary #F2EADF, text #2A2420, buttons #2A2420 with #FAF6EF text, accent #7C5A34, corners square, heading font Cormorant Garamond, body font Jost

## Apps and marketing
- [x] Discount WELCOME10: 10% off, once per customer, combines with free shipping
- [x] Klaviyo, Judge.me, Shopify Inbox, Search & Discovery installed
- [x] Judge.me star badge and review widget placed on product pages; star ratings switched on for product cards
- [ ] Theme editor → App embeds: turn on Judge.me Core, Klaviyo Onsite, Shopify Inbox (content/klaviyo/klaviyo-setup.md §5)
- [ ] Search & Discovery filters: Brand, Product type, Price, Availability (§6)
- [~] Klaviyo popup and flows: full copy and settings ready in content/klaviyo/klaviyo-setup.md; I'll build them as soon as the Klaviyo connector is authorised (claude.ai connector settings), or paste them in yourself
- [ ] Popup tested, code tested

## Final QA
- [ ] Test order placed and refunded (Bogus Gateway)
- [ ] All wallets visible at checkout
- [ ] Every nav link resolves
- [ ] 404 page styled
- [x] Password page OFF (done by you; site live, theme v3 published)

## Round 3 additions
- [x] Merged duplicates: Rare Beauty Soft Pinch Tinted Lip Oil (Wonder, Hope) and Truly Luxury Peptide Lip Oil (Glazed Donut, Cherry Baby Shimmer); old products archived with stock zeroed and old links redirected. Catalogue is now 24 active products / 29 variants
- [x] Shade colour dots on Rare Beauty, Truly and Dibs
- [x] "Deluxe mini" / "Gift set" labels on cards and product pages; quiet "Only a few left" line on product pages when real stock is 5 or fewer
- [x] Brands A–Z page (/pages/brands), linked from the Brands menu
- [x] About page redesigned with the full badge artwork
- [x] Google product category on all 24 active products (Google Shopping readiness)
- [ ] Sol de Janeiro body wash has no barcode: read it from the bottle and add it in the product's variant
- [x] Journal: 5 posts saved as hidden drafts
- [x] Weekly report scheduled every Monday 8:38am New York (push + email)
- [ ] Weekly report: attach the Shopify connector to the "Luxebin weekly report" routine in claude.ai so it can read the store
- [ ] Notification emails: logo and accent colour (content/notifications/README.md)

## Round 4: 11 new products (2026-10-30 batch)
- [x] Priced at 15% below verified MSRP with compare-at prices (Urban Decay De-Slick travel is $13 with no compare-at because the MSRP isn't verified)
- [x] Descriptions, benefits / how-to / ingredients metafields, SEO titles and descriptions
- [x] New collections: Eyes, Glow Recipe, Fekkai, K18, Makeup by Mario, Urban Decay; New Arrivals now shows these 8 new products
- [x] Menu: Makeup → Face / Eyes / Lips; Brands A–Z now lists 21 brands
- [x] Clean brand packshots set as the main image on 7 products, your own photos kept second with alt text; duplicate Fekkai image removed
- [x] Prices re-checked 2026-11-05: Olaplex No. 4 $28.50/$34, Lala Retro $18.50/$22, Protini $20/$24, Maybelline $11/$13, all correct. Olaplex No. 4 barcode (850056933575) is the new 4FINE series, so it was renamed "No. 4FINE Bond Maintenance Volumizing Shampoo" with matching description and SEO
- [x] Owner's rule: stock left at 0, and sold-out products come off the site. 10 products set to Draft and tagged auto-hidden-soldout (Kylie High Gloss, Kylie Lip Liner, Truly lip oil, RB Luminizer, Sol de Janeiro wash, Dibs, Laneige set, Laneige Lip Mask, Florence liner, Olaplex Endless Shine set). 24 products live. Six empty brands removed from the menu (A–Z page follows the menu)
- [x] Daily sold-out sweep at 6:17am New York (hides sold-out products, restores restocked ones) and weekly report Mondays 8:38am, both running in the Claude session that has the Shopify connection. The old weekly report, which had no store access, is disabled
- [x] Free shipping threshold now $50: Standard $8 under $50, Free Standard Shipping from $50, Express $15
- [ ] Remaining admin-screen items (policies, store email, homepage meta, hero text, app embeds, filters, checkout branding, old themes, Klaviyo): run content/admin-handoff-prompt.md in Claude Code with Chrome
