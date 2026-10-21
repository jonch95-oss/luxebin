# Luxebin homepage design research (Oct 2026)

## Sourcing note
- Web searches came back thin. No result documented the live design systems of Charlotte Tilbury, Augustinus Bader, Violet Grey, Space NK, Sturm, La Mer or Jomashop. WebFetch failed (DNS blocked by the proxy).
- **[V] = verified by search:** Jo Malone's typeface is the custom Malone Serif (Bold Decisions, 2019; Book to Semi-Bold, small caps for titling). Source: fontsinuse.com/uses/46125. Rhode is cited as the minimal benchmark (few hero products, lots of white space; $212M net sales in the 12 months to Mar 2025 from about 10 products). Strikethrough risks: an inflated "was" price erodes trust, reference prices carry legal duties, and the sale display must stay the same through checkout.
- **[K] = from my knowledge of these sites up to mid-2026.** Not checked live. Fonts named below are what the sites appear to use or match visually. Check them in DevTools before you quote them.

## Site-by-site patterns [K unless marked]

**Charlotte Tilbury.** Thin black or plum announcement bar with a rotating message (free shipping, gift with purchase). Full-bleed campaign hero with a serif headline and a pill CTA. Custom high-contrast serif for display, clean sans for UI. Palette is blush, nude, deep plum/black, with rose-gold accents. Product cards show the shade name, star rating, price and "Add to bag". A shade-swatch row sits under the image. Trust signals are reviews, the "Magic" claim-led copy and the virtual try-on. Product page has accordions for How to use, Ingredients, Benefits and Delivery.

**Jo Malone London.** Custom Malone Serif [V] with wide-tracked caps for navigation. Cream/ivory background, black text, signature cream-and-black box imagery. Lots of white space. Each product card is the bottle on a flat cream background, scent family in small caps, name, size and price. The site sells service as trust: complimentary gift wrap, samples, engraving. Mobile nav is a full-screen drawer with tracked-caps headings.

**Augustinus Bader.** White and very light grey with one strong accent (cobalt/"Bader blue"). Thin geometric sans in caps. Science-led hero: product on white with a clinical claim and a "Shop now" line link. Trust signals are TFC8 technology, clinical-study figures and press logos. Cards are minimal: name, size and price, with no badges.

**Dr. Barbara Sturm.** White with graphite type and a neutral sans, tracked caps for headers. Product photographed flat on white or grey. Trust comes from the founder as an MD and an ingredient-science story. Product page has accordions for Key ingredients, Usage and Full INCI.

**La Mer.** Pale sea-blue/grey and white, with silver and graphite. Light serif headlines over a light sans. Editorial, story-driven hero. Cards show the jar, name, size options and price. "Complimentary samples / gift wrap" appears in the announcement bar.

**Violet Grey.** Black and white with a violet accent and an editorial magazine feel ("The Violet Code" curation). Serif headlines, sans for UI. Curation itself is the trust signal: "every product vetted by experts".

**Cult Beauty and Space NK (multi-brand retailers, the closest model to Luxebin).** The card leads with the brand name in bold caps, then the product name, rating and price. On sale the price reads "£X (was £Y)" or shows the struck-through price in grey. The badge is small, rectangular, low-saturation and top-left ("Offer", "Save 20%"). Mobile header puts the logo centre, burger left, and search, account and bag right, with a persistent search bar under it. Cult Beauty uses black and white with a pink/red accent. Space NK uses black and white with very restrained badges.

**Jomashop (discount-luxury model).** Brand in caps above the product name. The "Retail $X" price is struck through in grey and labelled. The sale price is bold. "Save N%" sits in red text, not a heavy banner. Trust comes from authenticity and warranty copy. Pages tend to look cluttered, so copy the price anatomy and leave the density.

## Direction B, warm luxury
- **Borrow from:** Charlotte Tilbury (hero, rotating announcement bar), Jo Malone (cream space, tracked-caps nav, cards on flat cream), Space NK (multi-brand card anatomy, quiet badge).
- **Fonts:** Cormorant Garamond 500/600 for display, or Playfair Display 500 for more contrast. Jost 300/400/500 for UI and caps nav, letter-spacing 0.12em.
- **Palette:** bg #FAF6EF, surface #F2EADF, text #2A2420, muted #7A6E64, accent (bronze) #A27B4C, accent-deep #7C5A34, hairline #E4D9CA, sale #8C3B2E (brick, not red).

## Direction D, clinical luxury
- **Borrow from:** Augustinus Bader (single accent, claim-led hero), Sturm (product on grey, ingredient accordions), La Mer (silver/graphite and editorial calm).
- **Fonts:** Manrope 300/400/500 for everything, or Inter Tight 300/500 for display with Inter 400 for body. Caps tracked at 0.14em.
- **Palette:** bg #FFFFFF, surface #F4F5F6, text #1E2124, muted #6B7178, accent (graphite) #3A3F45, silver #B8BDC3, hairline #E3E5E8, sale #2F5D8A (steel blue) or #9A2E2E if it has to be red.

## Prestige discount rules
1. The retail price is the anchor. Label it "Retail $48" and strike it through in the muted colour at the same size or smaller. The Luxebin price sits to its right in the text colour, a little heavier.
2. "Save 15%" goes in a small hairline-outlined tag or plain text in the sale colour. Avoid filled red bursts, and keep it to one badge per card.
3. Say it once, at site level. Use "Prestige beauty, 15% below retail. Always." in the announcement bar or hero, rather than shouting "SALE" on every card. It reads as the business model, not clearance.
4. Lead every card with the brand name in tracked caps. The brand carries the prestige and the price supports it. Pair the price with "100% Authentic" near the add-to-bag button, not inside the price block.
5. Stay honest and consistent. Use real current MSRPs only, keep the same treatment through PDP, cart and checkout, and show "Final sale" calmly on the PDP and cart in an accordion or note line, not hidden away.

## Shared mobile patterns
- 36px announcement bar.
- Header: burger left, wordmark centre, search and bag right.
- Hero at about 70vh with one CTA, then a brand logo strip as a trust signal.
- Two-column product grid with 4:5 images on the surface colour.
- PDP accordions: Details, How to use, Ingredients, Authenticity, Shipping & final sale.
