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

## Theme ("Luxebin — Warm Luxury v2", unpublished, built on Dawn 16.0.0)
- [x] Direction B tokens, Cormorant Garamond + Jost, metallic wordmark
- [x] Homepage sections in brief order
- [x] Product page: brand link, title, price with retail struck through and Save X%, shade pills, accordions, authenticity badge, sticky add-to-bag on mobile, You may also like
- [x] Cart drawer with final-sale note
- [x] Theme check: 0 errors
- [x] Walkthrough screenshots in screens/: homepage desktop + mobile, Makeup collection desktop + mobile, 10 product pages, product page mobile, Authenticity page, 404. No Liquid errors, no sideways scroll at 390px, cream background and header on every page
- [ ] Lighthouse mobile/desktop scores: run once the password page is off (the password page blocks automated testing). Fonts now load from Shopify's own CDN, nothing render-blocking from apps on the homepage
- [ ] Publish theme v2 (on your go-ahead). Old themes "Dawn 16 import" and "Luxebin v1" can be deleted

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
- [ ] Password page OFF — only when you say so
