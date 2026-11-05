# Prompt: finish the Luxebin admin settings

Paste everything below the line into **Claude Code with Chrome**. Use the Claude desktop app, or run `claude --chrome` inside a clone of github.com/jonch95-oss/luxebin. Be logged in to the Luxebin Shopify admin (luxebin.co) in that Chrome window first.

These steps need the Shopify admin screens. The Shopify connector can't do them: it can't write policies, the live theme or checkout branding, can't delete themes, and has no access to Search & Discovery.

---

You're finishing the store settings for Luxebin (luxebin.co), a Shopify store selling genuine prestige beauty at about 15% below retail. You're working in this repository (jonch95-oss/luxebin) and in the Shopify admin, which is open and logged in in Chrome. The owner has approved every step below; don't ask for confirmation, just do it and report at the end.

House rules:
- Never use the words "authorized retailer" or "official stockist".
- Don't install or pay for any app.
- Don't touch any store other than Luxebin. If the admin shows "LuxeSupply" / herbiemissry, switch stores first.
- The live theme is **"Luxebin — Warm Luxury v3"** (theme ID 187347730617). Never delete or unpublish it.

Do these in order. After each one, check it took effect, then move on:

1. **Policies.** Go to Settings → Policies. Paste the HTML from these files into the matching policy, using the editor's `<>` source view so the formatting is kept, then save:
   - `content/policies/refund.html` → Refund policy
   - `content/policies/shipping.html` → Shipping policy
   - `content/policies/privacy.html` → Privacy policy (if Shopify manages it automatically, switch to a custom policy first)
   - `content/policies/terms.html` → Terms of service
2. **Store email.** Go to Settings → General (Store details). Set the store contact email and the sender email to `support@luxebin.co`. If Shopify asks to verify the domain, follow the DNS instructions it shows and tell the owner exactly what is still pending.
3. **Homepage meta description.** Go to Online Store → Preferences. Set the title to "Luxebin | Prestige Beauty, 100% Authentic, Below Retail" and the meta description to: "Prestige beauty, 100% authentic and guaranteed, for less than retail. Shop Olaplex, Rare Beauty, K18, Glow Recipe and more at Luxebin." Leave the password protection off.
4. **Hero text.** Go to Online Store → Themes → Warm Luxury v3 → Customize → Home page → the hero section. Change the line "Rare Beauty, Laura Mercier, Laneige and the names you already love…" to "Rare Beauty, Laura Mercier, Glow Recipe and the names you already love. 100% authentic, and always below retail." Laneige is sold out and hidden. Save.
5. **App embeds.** In the same editor, open App embeds (the puzzle-piece icon). Turn on Judge.me Reviews (core), Klaviyo Onsite Javascript and Shopify Inbox. For Inbox, use button colour #2A2420 and the greeting "Questions about a product or your order? We're here." Save.
6. **Search & Discovery filters.** Go to Apps → Search & Discovery → Filters. Make sure there are filters for Availability, Price, Brand (vendor) and Product type, in that order. Save, then check that /collections/makeup shows them.
7. **Checkout branding.** Go to Settings → Checkout → Customize. Settings:
   - Logo: export `brand/wordmark-dark.svg` to a PNG about 600px wide (any converter, e.g. `rsvg-convert` or a browser screenshot) and upload it.
   - Colours: background #FAF6EF, order summary #F2EADF, text #2A2420, buttons #2A2420 with text #FAF6EF, accent #7C5A34.
   - Corner radius: none.
   - Fonts: headings Cormorant Garamond, body Jost (or the closest fonts available).

   Save.
8. **Old themes.** Go to Online Store → Themes. Delete every theme in the library except the live "Luxebin — Warm Luxury v3". Read each name before deleting, and never delete the published theme.
9. **Klaviyo (only if the Klaviyo tab is logged in).** Build items 1–4 of `content/klaviyo/klaviyo-setup.md`: the sign-up popup with code WELCOME10, the welcome flow, the abandoned checkout flow and the review request. Set them live.
10. **Final check.** In a private window, open luxebin.co:
    - The homepage hero has the new text.
    - The reviews widget shows on a product page.
    - The Inbox chat bubble appears.
    - A cart over $50 shows free shipping at checkout, and a cart under $50 shows $8.

Finish by updating `launch-checklist.md`: tick what you completed, add a note for anything blocked and why, then commit and push to main. Report a short table of each step: done, or blocked and why.
