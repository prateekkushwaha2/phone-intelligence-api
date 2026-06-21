
import phonenumbers
from phonenumbers import (
    geocoder,
    carrier,
    timezone,
    number_type,
    PhoneNumberType
)


def get_type(parsed):

    mapping = {
        PhoneNumberType.MOBILE: "mobile",
        PhoneNumberType.FIXED_LINE: "fixed_line",
        PhoneNumberType.FIXED_LINE_OR_MOBILE:
        "fixed_or_mobile"
    }

    return mapping.get(
        number_type(parsed),
        "unknown"
    )


def lookup_phone(number):

    try:

        parsed = phonenumbers.parse(
            number
        )

        valid = (
            phonenumbers
            .is_valid_number(parsed)
        )

        return {

            "valid": valid,

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
            list(
                timezone
                .time_zones_for_number(
                    parsed
                )
            ),

            "type":
            get_type(parsed),

            "international":
            phonenumbers.format_number(
                parsed,
                phonenumbers
                .PhoneNumberFormat
                .INTERNATIONAL
            ),

            "national":
            phonenumbers.format_number(
                parsed,
                phonenumbers
                .PhoneNumberFormat
                .NATIONAL
            ),

            "e164":
            phonenumbers.format_number(
                parsed,
                phonenumbers
                .PhoneNumberFormat
                .E164
            ),

            "possible":
            phonenumbers
            .is_possible_number(
                parsed
            )

        }

    except Exception:

        return {

            "valid": False,
            "error": "invalid number"

        }
