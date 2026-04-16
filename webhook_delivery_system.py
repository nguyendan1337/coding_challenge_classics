# webhooks_challenge.py
"""
STRIPE HACKERRANK OA - WEBHOOKS EVENT PROCESSING (MaaS / MMS Team)
====================================================================

Stripe sends real-time webhook events for all money movement activities (payouts, payments, disputes, etc.).
Your service must process these events reliably with strict idempotency and maintain accurate object state.

Input:
- events: List[Dict]                → webhook events in the exact order they arrive

Each event has:
{
    "id": str,                      # unique event ID — critical for idempotency
    "type": str,                    # e.g. "payout.created", "payout.paid", "payout.failed", "payment_intent.succeeded"
    "data": {"object": { ... }}     # the actual resource (payout or payment_intent)
}

=== PROGRESSIVE PARTS (Implement ONE function that solves all parts) ===

Part 1: Basic Event Processing
- Process events in arrival order.
- Extract the object from event["data"]["object"].
- Store the object in state using its "id" as the key.
- For payout events, set initial status = "created" if not present.

Part 2: Status Update Logic
- Support the following exact status mappings:
    - "payout.created"           → status = "created"
    - "payout.paid"              → status = "paid"
    - "payout.failed"            → status = "failed"
    - "payment_intent.succeeded" → status = "succeeded"
- Later events for the same object should overwrite the previous state (latest status wins).
- Ignore unknown event types silently.

Part 3: Idempotency
- Skip any event whose "id" has already been processed (use a set to track seen event IDs).
- Never process the same event twice, even if it appears multiple times.

Part 4: Production Requirements & Edge Cases
- Support multiple object types (payouts and payment_intents).
- Handle events that arrive out of order (latest event always wins for that object).
- Do NOT mutate any input data.
- Always return a deep copy of the final state.
- If an event is missing "data.object.id", ignore it silently.

Return Value:
    Dict[str, Dict[str, Any]]
    → final_state: object_id → latest object dictionary (with status added/updated)

This is production webhook logic used in Stripe’s Money Movement systems. Duplicates or incorrect state can cause major customer issues.
"""

from typing import Dict, List, Any
from copy import deepcopy

def process_webhooks(events: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    # TODO: Implement full logic for Parts 1–4 here
    pass


# ========================= RUNNABLE TEST CASES =========================
if __name__ == "__main__":
    print("Running Stripe Webhooks OA tests...\n")

    # Parts 1–3
    events1 = [
        {"id": "evt_1", "type": "payout.created", "data": {"object": {"id": "po_1", "amount": 10000, "currency": "USD"}}},
        {"id": "evt_2", "type": "payment_intent.succeeded", "data": {"object": {"id": "pi_1", "amount": 2500, "currency": "USD"}}},
        {"id": "evt_3", "type": "payout.paid", "data": {"object": {"id": "po_1", "amount": 10000, "currency": "USD"}}},
    ]
    result1 = process_webhooks(events1)
    assert result1["po_1"]["status"] == "paid"
    assert result1["pi_1"]["status"] == "succeeded"
    print("✓ Parts 1–3 passed")

    # Part 4 - Idempotency + latest wins + unknown
    events2 = events1 + [
        {"id": "evt_1", "type": "payout.created", "data": {"object": {"id": "po_1"}}},   # duplicate → ignore
        {"id": "evt_4", "type": "payout.failed", "data": {"object": {"id": "po_1"}}},    # latest wins
        {"id": "evt_5", "type": "random.unknown", "data": {"object": {"id": "ignore_me"}}},
    ]
    result2 = process_webhooks(events2)
    assert result2["po_1"]["status"] == "failed"
    assert len(result2) == 2
    print("✓ Part 4 passed (idempotency + latest wins + unknown events)")

    print("\n🎉 All 4 parts passed! This matches the exact style of recent MaaS webhooks OAs.")