# Klaviyo setup for Luxebin

Everything below is ready to paste. Brand: background #FAF6EF, panel #F2EADF, text #2A2420, accent #7C5A34, buttons #2A2420 with #FAF6EF text, square corners. Heading font: Cormorant Garamond (fallback Georgia). Body font: Jost (fallback Helvetica/Arial). Header image: brand/logo-full.webp (the round badge); footer: support@luxebin.co.

Discount: use Klaviyo's **Shopify unique coupon** block in the welcome email (10% off, single use, expires 30 days, once per customer). The shared code **WELCOME10** already exists in Shopify as a fallback.

## 1. Sign-up popup (Sign-up forms → Create → Popup)
- Targeting: show to visitors not in the "Newsletter" list; **show once per visitor** (don't show again for 30 days after close; never after submit).
- Timing: after 8 seconds or 40% scroll, whichever first; desktop and mobile (mobile as a bottom sheet).
- Exclude: /checkout, /cart.
- Copy:
  - Eyebrow: THE LUXEBIN LIST
  - Heading: Take 10% off your first order
  - Body: Join for first word on new arrivals, restocks and private offers.
  - Field: Email address
  - Button: Unlock 10% off
  - Small print: By subscribing you agree to receive marketing emails. Unsubscribe anytime.
  - Success step: Welcome to Luxebin. Your code is on its way to your inbox.
- Submit adds to list "Newsletter" (this triggers flow 2).

## 2. Welcome flow (trigger: added to list "Newsletter")
**Email 1, immediately**
- Subject: Your 10% is inside
- Preview: Prestige beauty, always below retail.
- Body:
  > Welcome to Luxebin.
  >
  > We bring together the beauty you already love, from Rare Beauty, Laura Mercier, Laneige, NARS and more, and offer it below retail. Every piece is 100% authentic, guaranteed.
  >
  > Here is 10% off your first order: **[unique coupon]**
  >
  > [Shop the Edit] → /collections/best-sellers
- Below: 4-product grid (Best Sellers collection).

**Email 2, 2 days later (only if no order placed)**
- Subject: How we keep prices below retail
- Preview: The short version of our authenticity promise.
- Body: 3 short paragraphs from the Authenticity Guarantee page (how we source, why prices are lower, what we guarantee), button "Read our promise" → /pages/authenticity-guarantee, reminder of the code.

**Email 3, 4 days after email 2 (only if no order placed)**
- Subject: Your 10% expires soon
- Preview: A gentle reminder, then we'll leave you be.
- Body: one line reminder + New Arrivals grid + code.

## 3. Abandoned checkout flow (trigger: Started Checkout; filter: placed order zero times since starting this flow)
**Email 1, 4 hours later**
- Subject: You left something beautiful behind
- Preview: Your bag is saved, below retail as always.
- Body: dynamic checkout items block, button "Return to your bag", trust line: 100% Authentic — Guaranteed · Free US shipping over $50.

**Email 2, 24 hours after email 1**
- Subject: Still thinking it over?
- Preview: A quick note on our final-sale policy.
- Body: items block + short honest note: "Every piece is sold below retail, so all sales are final. If anything arrives damaged, send us a photo within 7 days and we'll replace it." Button "Complete your order". (No extra discount, so the margin floor holds.)

## 4. Post-purchase review request
Use **Judge.me** (not Klaviyo) to send the review request, so reviews land on the product pages:
- Judge.me → Settings → Review request: send 14 days after fulfilment; one reminder after 7 days.
- Subject: How are you finding your {{product_name}}?
- Style: background #FAF6EF, button #2A2420, logo = wordmark.
- Optional: connect Judge.me to Klaviyo (Judge.me → Integrations → Klaviyo) so the request is sent from Klaviyo in the same template style.

## 5. Theme switches (Online Store → Themes → Luxebin — Warm Luxury v2 → Customize → App embeds)
- Turn on **Judge.me Core** (stars and review widget are already placed on product pages and product cards).
- Turn on **Klaviyo Onsite Javascript** (needed for the popup).
- Shopify Inbox chat: turn on **Shopify Inbox** embed; set colour #2A2420, greeting "Questions about a shade or size? We're here."

## 6. Search & Discovery filters (Apps → Search & Discovery → Filters)
Add in this order: Brand (vendor), Product type, Price, Availability. Optional: tag filter for Finish.
