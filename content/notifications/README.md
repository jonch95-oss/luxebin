# Order and shipping email branding

## 1. No code: Settings → Notifications → Customer notifications → Customize email templates
- Logo: upload `brand/luxebin-badge-900.jpg` (round badge). Logo width: 120 px.
- Accent colour: `#7C5A34`.
- Save. This restyles every Shopify notification (order confirmation, shipping confirmation, delivery, refund) at once.

## 2. Optional: add the Luxebin promise line under the order summary
In Settings → Notifications → **Order confirmation** → Edit code, find the line `{% if requires_shipping %}` near the end and paste this just above it. Repeat in **Shipping confirmation**.

```liquid
<table class="row" style="margin-top:24px;border-top:1px solid #E2D5C3;">
  <tr>
    <td style="padding-top:18px;font-family:Georgia,'Times New Roman',serif;color:#2A2420;font-size:15px;line-height:1.6;">
      <strong style="font-family:Helvetica,Arial,sans-serif;font-size:11px;letter-spacing:2px;color:#7C5A34;">100% AUTHENTIC — GUARANTEED</strong><br>
      Every piece is genuine and sold below retail. All sales are final; if anything arrives damaged,
      email a photo to <a href="mailto:support@luxebin.co" style="color:#7C5A34;">support@luxebin.co</a> within 7 days and we'll replace it.
    </td>
  </tr>
</table>
```

## 3. Subject lines (Settings → Notifications → each template → Subject)
- Order confirmation: `Your Luxebin order {{name}} is confirmed`
- Shipping confirmation: `Your Luxebin order {{name}} is on its way`
- Delivery: `Your Luxebin order has arrived`
