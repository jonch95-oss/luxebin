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

## Theme ("Luxebin — Warm Luxury", unpublished, built on Dawn 16.0.0)
- [x] Direction B tokens, Cormorant Garamond + Jost, metallic wordmark
- [x] Homepage sections in brief order
- [x] Product page: brand link, title, price with retail struck through and Save X%, shade pills, accordions, authenticity badge, sticky add-to-bag on mobile, You may also like
- [x] Cart drawer with final-sale note
- [x] Theme check: 0 errors
- [ ] Walkthrough screenshots (blocked: storefront password needed)
- [ ] Lighthouse mobile/desktop scores (blocked: storefront password needed)
- [ ] Publish theme (only on your go-ahead)

## Pages and policies
- [x] Pages: About, Authenticity Guarantee, FAQ, Contact (existing)
- [ ] Policies: written (content/policies/*.html) but the API cannot save them; paste in Settings → Policies
- [ ] Blog: not started (decide after seeing the theme)

## Settings
- [x] Market: United States only, USD
- [x] Customer accounts: optional
- [x] Store name: Luxebin
- [ ] Free shipping threshold: currently $70 on Standard; change to $50 in Settings → Shipping and delivery → General profile → Domestic → Standard
- [ ] Store contact/sender email: currently a personal Gmail; set support@luxebin.co in Settings → General once the mailbox exists
- [ ] Payments: confirm Shop Pay, Apple Pay, Google Pay, PayPal, Klarna/Afterpay enabled (Settings → Payments)
- [ ] Taxes: NY nexus only (Settings → Taxes and duties)
- [ ] Order/shipping notification emails restyled
- [ ] Checkout branding (logo, colours, fonts)

## Apps and marketing
- [x] Discount WELCOME10: 10% off, once per customer, combines with free shipping
- [ ] Install Klaviyo, Judge.me, Shopify Inbox, Search & Discovery (all free tiers)
- [ ] Klaviyo: popup (fires once per visitor), welcome flow with 10% code, abandoned cart x2, post-purchase review request
- [ ] Popup tested, code tested

## Final QA
- [ ] Test order placed and refunded (Bogus Gateway)
- [ ] All wallets visible at checkout
- [ ] Every nav link resolves
- [ ] 404 page styled
- [ ] Password page OFF — only when you say so
