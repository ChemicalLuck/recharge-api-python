"""
Verify that live Recharge API responses parse cleanly into the v2 Pydantic models.

Usage:
    RECHARGE_API_TOKEN=sk_xxx python scripts/verify_models.py

Or put RECHARGE_API_TOKEN in a .env file in the project root.
"""

import os
import sys
import traceback

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("RECHARGE_API_TOKEN")
if not TOKEN:
    print("ERROR: RECHARGE_API_TOKEN not set", file=sys.stderr)
    sys.exit(1)

from recharge import RechargeAPI  # noqa: E402

# ── colour helpers ────────────────────────────────────────────────────────────
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

results: list[tuple[str, str, str]] = []  # (resource, status, detail)


def _pass(resource: str, detail: str = "") -> None:
    results.append((resource, "PASS", detail))
    print(f"  {GREEN}✓ PASS{RESET}  {resource}" + (f"  {detail}" if detail else ""))


def _fail(resource: str, detail: str) -> None:
    results.append((resource, "FAIL", detail))
    print(f"  {RED}✗ FAIL{RESET}  {resource}  {detail}")


def _skip(resource: str, reason: str) -> None:
    results.append((resource, "SKIP", reason))
    print(f"  {YELLOW}– SKIP{RESET}  {resource}  ({reason})")


def _section(name: str) -> None:
    print(f"\n{BOLD}{CYAN}{name}{RESET}")


def _run(label: str, fn):
    """Call fn(), report PASS/FAIL. Returns the result or None on failure."""
    try:
        result = fn()
        count = len(result) if isinstance(result, list) else 1
        _pass(label, f"({count} item{'s' if count != 1 else ''})")
        return result
    except Exception as exc:
        _fail(label, str(exc))
        if "--verbose" in sys.argv or "-v" in sys.argv:
            traceback.print_exc()
        return None


# ── initialise ────────────────────────────────────────────────────────────────
print(f"\n{BOLD}Connecting to Recharge API…{RESET}")
try:
    api = RechargeAPI(TOKEN)
    print(f"  {GREEN}✓{RESET} Connected — scopes: {', '.join(api.scopes[:5])}{'…' if len(api.scopes) > 5 else ''}")
except Exception as exc:
    print(f"  {RED}✗ Failed to initialise RechargeAPI: {exc}{RESET}")
    sys.exit(1)

v2 = api.v2

# ── Store ─────────────────────────────────────────────────────────────────────
_section("Store")
_run("Store.get()", v2.Store.get)

# ── Token ─────────────────────────────────────────────────────────────────────
_section("Token")
_run("Token.get()", v2.Token.get)

# ── Accounts ──────────────────────────────────────────────────────────────────
_section("Accounts")
accounts = _run("Account.list_()", v2.Account.list_)
if accounts:
    _run(f"Account.get({accounts[0].id})", lambda: v2.Account.get(str(accounts[0].id)))

# ── Customers ─────────────────────────────────────────────────────────────────
_section("Customers")
customers = _run("Customer.list_(limit=5)", lambda: v2.Customer.list_({"limit": "5"}))
first_customer = customers[0] if customers else None
if first_customer:
    _run(f"Customer.get({first_customer.id})", lambda: v2.Customer.get(str(first_customer.id)))
    _run(
        f"Customer.get_delivery_schedule({first_customer.id})",
        lambda: v2.Customer.get_delivery_schedule(str(first_customer.id), {"delivery_count_future": 2}),
    )
    if "read_credit_summary" in api.scopes:
        _run(
            f"Customer.get_credit_summary({first_customer.id})",
            lambda: v2.Customer.get_credit_summary(str(first_customer.id)),
        )
    else:
        _skip("Customer.get_credit_summary()", "missing scope: read_credit_summary")

# ── Addresses ─────────────────────────────────────────────────────────────────
_section("Addresses")
addr_query = {"limit": "5"}
if first_customer:
    addr_query["customer_id"] = str(first_customer.id)
addresses = _run("Address.list_(limit=5)", lambda: v2.Address.list_(addr_query))
if addresses:
    _run(f"Address.get({addresses[0].id})", lambda: v2.Address.get(str(addresses[0].id)))

# ── Subscriptions ─────────────────────────────────────────────────────────────
_section("Subscriptions")
subscriptions = _run("Subscription.list_(limit=5)", lambda: v2.Subscription.list_({"limit": "5"}))
if subscriptions:
    _run(
        f"Subscription.get({subscriptions[0].id})",
        lambda: v2.Subscription.get(str(subscriptions[0].id)),
    )

# ── Onetimes ──────────────────────────────────────────────────────────────────
_section("Onetimes")
onetimes = _run("Onetime.list_(limit=5)", lambda: v2.Onetime.list_({"limit": "5"}))
if onetimes:
    _run(f"Onetime.get({onetimes[0].id})", lambda: v2.Onetime.get(str(onetimes[0].id)))

# ── Charges ───────────────────────────────────────────────────────────────────
_section("Charges")
charges = _run("Charge.list_(limit=5)", lambda: v2.Charge.list_({"limit": "5"}))
if charges:
    _run(f"Charge.get({charges[0].id})", lambda: v2.Charge.get(str(charges[0].id)))

# ── Orders ────────────────────────────────────────────────────────────────────
_section("Orders")
orders = _run("Order.list_(limit=5)", lambda: v2.Order.list_({"limit": "5"}))
if orders:
    _run(f"Order.get({orders[0].id})", lambda: v2.Order.get(str(orders[0].id)))

# ── Payment Methods ───────────────────────────────────────────────────────────
_section("Payment Methods")
if "read_payment_methods" in api.scopes:
    pm_query = {"customer_id": first_customer.id} if first_customer else None
    payment_methods = _run(
        "PaymentMethod.list_()",
        lambda: v2.PaymentMethod.list_(pm_query),
    )
    if payment_methods:
        _run(
            f"PaymentMethod.get({payment_methods[0].id})",
            lambda: v2.PaymentMethod.get(payment_methods[0].id),
        )
else:
    _skip("PaymentMethod.list_()", "missing scope: read_payment_methods")

# ── Plans ─────────────────────────────────────────────────────────────────────
_section("Plans")
if "read_products" in api.scopes:
    _run("Plan.list_(limit=5)", lambda: v2.Plan.list_({"limit": "5"}))
else:
    _skip("Plan.list_()", "missing scope: read_products")

# ── Products ──────────────────────────────────────────────────────────────────
_section("Products")
if "read_products" in api.scopes:
    _skip("Product.list_()", "requires external_product_ids filter — no list-all endpoint")
else:
    _skip("Product.list_()", "missing scope: read_products")

# ── Collections ───────────────────────────────────────────────────────────────
_section("Collections")
if "read_products" in api.scopes:
    collections = _run("Collection.list_(limit=5)", lambda: v2.Collection.list_({"limit": "5"}))
    if collections:
        _run(
            f"Collection.get({collections[0].id})",
            lambda: v2.Collection.get(str(collections[0].id)),
        )
else:
    _skip("Collection.list_()", "missing scope: read_products")

# ── Discounts ─────────────────────────────────────────────────────────────────
_section("Discounts")
if "read_discounts" in api.scopes:
    discounts = _run("Discount.list_(limit=5)", lambda: v2.Discount.list_({"limit": "5"}))
    if discounts:
        _run(
            f"Discount.get({discounts[0].id})",
            lambda: v2.Discount.get(str(discounts[0].id)),
        )
else:
    _skip("Discount.list_()", "missing scope: read_discounts")

# ── Webhooks ──────────────────────────────────────────────────────────────────
_section("Webhooks")
webhooks = _run("Webhook.list_()", v2.Webhook.list_)
if webhooks:
    _run(f"Webhook.get({webhooks[0].id})", lambda: v2.Webhook.get(str(webhooks[0].id)))

# ── Events ────────────────────────────────────────────────────────────────────
_section("Events")
if "read_events" in api.scopes:
    _run("Event.list_(limit=5)", lambda: v2.Event.list_({"limit": "5"}))
else:
    _skip("Event.list_()", "missing scope: read_events")

# ── Metafields ────────────────────────────────────────────────────────────────
_section("Metafields")
_mf_found = False
for _owner in ("customer", "subscription", "address", "order", "charge"):
    try:
        mfs = v2.Metafield.list_({"owner_resource": _owner, "limit": "5"})  # type: ignore[arg-type]
        _pass(f"Metafield.list_(owner_resource={_owner!r})", f"({len(mfs)} items)")
        if mfs and not _mf_found:
            _mf_found = True
            _mf = mfs[0]
            _run(
                f"Metafield.get({_mf.id}, {_owner!r})",
                lambda: v2.Metafield.get(str(_mf.id), _owner),  # type: ignore[arg-type]
            )
        break
    except Exception as exc:
        if "scope" in str(exc).lower() or "permission" in str(exc).lower():
            _skip(f"Metafield.list_(owner_resource={_owner!r})", str(exc))
            break
        _fail(f"Metafield.list_(owner_resource={_owner!r})", str(exc))

# ── Retention Strategies ──────────────────────────────────────────────────────
_section("Retention Strategies")
if "read_subscriptions" in api.scopes:
    rs = _run("RetentionStrategy.list_()", v2.RetentionStrategy.list_)
    if rs:
        _run(
            f"RetentionStrategy.get({rs[0].id})",
            lambda: v2.RetentionStrategy.get(rs[0].id),
        )
else:
    _skip("RetentionStrategy.list_()", "missing scope: read_subscriptions")

# ── Async Batches ─────────────────────────────────────────────────────────────
_section("Async Batches")
if "read_batches" in api.scopes:
    batches = _run("AsyncBatch.list_()", v2.AsyncBatch.list_)
    if batches:
        _run(
            f"AsyncBatch.get({batches[0].id})",
            lambda: v2.AsyncBatch.get(str(batches[0].id)),
        )
else:
    _skip("AsyncBatch.list_()", "missing scope: read_batches")

# ── Bundle Selections ─────────────────────────────────────────────────────────
_section("Bundle Selections")
if "read_subscriptions" in api.scopes:
    bs = _run("BundleSelection.list_()", lambda: v2.BundleSelection.list_())
    if bs:
        _run(
            f"BundleSelection.get({bs[0].id})",
            lambda: v2.BundleSelection.get(str(bs[0].id)),
        )
else:
    _skip("BundleSelection.list_()", "missing scope: read_subscriptions")

# ── Summary ───────────────────────────────────────────────────────────────────
passed = sum(1 for _, s, _ in results if s == "PASS")
failed = sum(1 for _, s, _ in results if s == "FAIL")
skipped = sum(1 for _, s, _ in results if s == "SKIP")

print(f"\n{BOLD}{'─' * 50}{RESET}")
print(f"{BOLD}Results:{RESET}  {GREEN}{passed} passed{RESET}  {RED}{failed} failed{RESET}  {YELLOW}{skipped} skipped{RESET}")

if failed:
    print(f"\n{RED}Failed checks:{RESET}")
    for resource, status, detail in results:
        if status == "FAIL":
            print(f"  • {resource}: {detail}")
    sys.exit(1)
