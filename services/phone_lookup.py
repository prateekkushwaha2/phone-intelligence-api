import phonenumbers
from phonenumbers import (
    geocoder,
    carrier,
    timezone,
    number_type,
    PhoneNumberType
)


def get_type(parsed):

    t = number_type(parsed)

    mapping = {
        PhoneNumberType.MOBILE: "mobile",
        PhoneNumberType.FIXED_LINE: "fixed_line",
        PhoneNumberType.FIXED_LINE_OR_MOBILE: "fixed_or_mobile"
    }

    return mapping.get(t, "unknown")


def lookup_phone(number):

    try:

        parsed = phonenumbers.parse(number)

        return {
            "valid": phonenumbers.is_valid_number(parsed),

            "country":
            geocoder.description_for_number(
                parsed,
                "en"
            ),

            "carrier":
            carrier.name_for_number(
                parsed,
                "en"
            ),

            "timezone":
            timezone.time_zones_for_number(
                parsed
            ),

            "type":
            get_type(parsed),

            "international":
            phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.INTERNATIONAL
            ),

            "e164":
            phonenumbers.format_number(
                parsed,
                phonenumbers.PhoneNumberFormat.E164
            )
        }

    except Exception:

        return {
            "valid": False,
            "error": "invalid number"
        }
