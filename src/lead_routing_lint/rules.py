from __future__ import annotations

from lead_routing_lint.models import Rule

PROJECT_NAME = 'lead-routing-lint'
SUMMARY = 'Audit lead routing rules for owner gaps, region mismatch, and fallback behavior.'
SAMPLE_RISK = 'region EMEA owner none fallback missing territory mismatch'
SAMPLE_CLEAN = 'region EMEA owner sales-emea fallback inbound-queue'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='missing-owner',
        severity='high',
        pattern='owner\\s+(none|missing|unknown)',
        message='lead owner missing',
        recommendation='assign route owner',
    ),
    Rule(
        code='missing-fallback',
        severity='medium',
        pattern='fallback\\s+(missing|none|unknown)',
        message='fallback route missing',
        recommendation='add fallback queue',
    ),
    Rule(
        code='territory-mismatch',
        severity='low',
        pattern='territory\\s+mismatch',
        message='territory mismatch detected',
        recommendation='verify territory mapping',
    ),
)
