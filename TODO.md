# TODO

## Completed / Applied Fixes
- Fixed product “View” page crash
  - **File:** `store/views.py`
  - **Change:** corrected template name from `store/product_detail.html` → `store/product_details.html`.

- Changed currency symbols from INR/₹ to USD/$
  - **Files:**
    - `templates/store/home.html`
    - `templates/store/product_list.html`
    - `templates/store/product_details.html`
    - `templates/cart/cart_details.html`

- Fixed missing template error on product details
  - **Change:** ensured product detail view renders the existing template `store/product_details.html`.

- Made product images bigger
  - **File:** `static/css/style.css`
  - **Change:** increased `.product-card img` and `.card-img-top` to 260px.

- Removed Razorpay UI flow (offline payments only)
  - **File:** `templates/orders/payments.html`
  - **Change:** removed Razorpay JS and replaced button with direct POST to `{% url 'orders:paymenthandler' %}`.

## Notes / Known Issues
- Backend `Order` model still contains `razorpay_*` fields (no UI usage after change).
- To fully remove Razorpay from DB/model requires a migration.

## Next Steps (Optional)
- Add a migration to remove `razorpay_*` fields from `orders/models.py` + `orders/migrations`.
- Verify checkout/payment templates match the offline-only flow.

