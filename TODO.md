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

## Next Steps (Implementation Plan)
1. Create new project-level scaffolding for scalable ecommerce:
   - add production-ready settings baseline (static/media, env vars, security defaults)
   - add custom user model (`accounts`) and vendor-ready permissions structure
2. Upgrade database schema to match required entities (incremental, migration-safe):
   - ✅ extend `store` models: Category+Subcategory, Variant (separate size/color), ProductImage, SEO fields
   - ✅ extend `orders` models: Address + Order(status) + OrderItem
   - ✅ add wishlist models (DB-backed)
   - ⏳ next: Inventory, Review+Rating+ReviewImage, Coupon, Featured/Best/Flash sections
3. Add PostgreSQL + Redis + Celery configuration (production-ready) using env vars.
4. Add Docker + Docker Compose for Django + Postgres + Redis + Celery.
5. Add Tailwind + Alpine.js or HTMX integration skeleton (choose best for project).
6. Update `requirements.txt` with secure, latest-compatible packages.
7. Add `.env.example` optimized for Pakistani hosting.
8. Add production logging + Sentry integration.


## Notes
- Current project uses SQLite and Django default `User`; migration to custom user + postgres/redis/celery will require generating migrations.
- Current `orders.Order` contains some Razorpay fields; we will keep backward compatibility short-term, but can clean later.

