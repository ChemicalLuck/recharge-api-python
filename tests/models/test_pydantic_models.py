import pytest

from recharge.model.v1.charge import Charge as ChargeV1
from recharge.model.v1.order import Order as OrderV1
from recharge.model.v1.subscription import Subscription as SubV1
from recharge.model.v1.discount import Discount as DiscountV1, DiscountChannelSettingsValue
from recharge.model.v2.charge import Charge as ChargeV2
from recharge.model.v2.customer import Customer as CustomerV2, CustomerDeliverySchedule
from recharge.model.v2.subscription import Subscription as SubV2
from recharge.model.v2.plan import Plan


# ── Extra field tolerance ──────────────────────────────────────────────────

def test_extra_fields_are_tolerated():
    c = ChargeV1.model_validate({"id": 1, "completely_new_api_field": "future"})
    assert c.model_extra == {"completely_new_api_field": "future"}


def test_v2_extra_fields_tolerated():
    c = ChargeV2.model_validate({"id": 1, "new_v3_field": True})
    assert c.model_extra["new_v3_field"] is True


# ── Type field (previously __annotations__ hack) ───────────────────────────

def test_v1_charge_type_field():
    c = ChargeV1.model_validate({"id": 1, "type": "SUBSCRIPTION"})
    assert c.type == "SUBSCRIPTION"


def test_v1_order_type_field():
    o = OrderV1.model_validate({"id": 1, "type": "CHECKOUT"})
    assert o.type == "CHECKOUT"


def test_v2_charge_type_field():
    c = ChargeV2.model_validate({"id": 1, "type": "CHECKOUT"})
    assert c.type == "CHECKOUT"


def test_v2_plan_type_field():
    p = Plan.model_validate({"id": 1, "type": "subscription"})
    assert p.type == "subscription"


# ── Optional fields default to None ────────────────────────────────────────

def test_optional_fields_are_none_by_default():
    c = ChargeV1.model_validate({"id": 1})
    assert c.email is None
    assert c.processed_at is None
    assert c.retry_date is None


def test_list_fields_default_to_empty():
    c = ChargeV1.model_validate({"id": 1})
    assert c.line_items == []
    assert c.note_attributes == []
    assert c.tags == []


# ── Bug 5: CustomerDeliverySchedule.deliveries (not delvieries) ───────────

def test_deliveries_field_spelled_correctly():
    cds = CustomerDeliverySchedule.model_validate({
        "customer": {"id": 1, "email": "a@b.com", "first_name": "A", "last_name": "B"},
        "deliveries": [],
    })
    assert cds.deliveries == []
    assert not hasattr(cds, "delvieries")


# ── Nested model validation ─────────────────────────────────────────────────

def test_nested_billing_address():
    c = ChargeV1.model_validate({
        "id": 1,
        "billing_address": {"address1": "123 Main St", "city": "London", "zip": "SW1A 1AA"},
    })
    assert c.billing_address is not None
    assert c.billing_address.city == "London"


def test_v1_discount_channel_settings_nested():
    d = DiscountV1.model_validate({
        "id": 1,
        "channel_settings": {
            "api": {"can_apply": True},
            "checkout_page": {"can_apply": False},
        },
    })
    assert d.channel_settings is not None
    assert d.channel_settings.api is not None
    assert d.channel_settings.api.can_apply is True
    assert d.channel_settings.checkout_page.can_apply is False


# ── V2 Customer required fields ─────────────────────────────────────────────

def test_v2_customer_requires_core_fields():
    with pytest.raises(Exception):
        CustomerV2.model_validate({"id": 1})  # missing required fields


def test_v2_customer_valid():
    c = CustomerV2.model_validate({
        "id": 1,
        "apply_credit_to_next_recurring_charge": False,
        "created_at": "2024-01-01T00:00:00",
        "email": "t@test.com",
        "first_name": "Joe",
        "has_payment_method_in_dunning": False,
        "has_valid_payment_method": True,
        "hash": "abc",
        "last_name": "Smith",
        "subscriptions_active_count": 0,
        "subscriptions_total_count": 1,
        "tax_exempt": False,
        "updated_at": "2024-01-01T00:00:00",
    })
    assert c.id == 1
    assert c.first_name == "Joe"
