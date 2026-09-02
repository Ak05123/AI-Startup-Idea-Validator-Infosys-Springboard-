"""
Frontend configuration for the AI Startup Validator.

The Streamlit frontend runs the EXISTING validation pipeline directly
in-process — there is no FastAPI backend URL to configure anymore.
"""

# The validation pipeline runs many multi-agent LLM calls and can take
# several minutes; no network configuration is required here.
APP_TITLE = "AI Startup Validator"

# ------------------------------------------------------------------
# Country -> currency detection (pure lookup, no network / no IP).
# ------------------------------------------------------------------
_CURRENCIES = {
    "india": ("INR", "₹"), "in": ("INR", "₹"), "ind": ("INR", "₹"), "bharat": ("INR", "₹"),
    "united states": ("USD", "$"), "usa": ("USD", "$"), "us": ("USD", "$"),
    "united states of america": ("USD", "$"), "america": ("USD", "$"),
    "united kingdom": ("GBP", "£"), "uk": ("GBP", "£"), "britain": ("GBP", "£"),
    "great britain": ("GBP", "£"), "england": ("GBP", "£"),
    "united arab emirates": ("AED", "AED "), "uae": ("AED", "AED "), "emirates": ("AED", "AED "),
    "canada": ("CAD", "C$"), "ca": ("CAD", "C$"),
    "australia": ("AUD", "A$"), "au": ("AUD", "A$"),
    "japan": ("JPY", "¥"), "jp": ("JPY", "¥"),
    "china": ("CNY", "¥"), "cn": ("CNY", "¥"), "prc": ("CNY", "¥"),
    "singapore": ("SGD", "S$"), "sg": ("SGD", "S$"),
    "germany": ("EUR", "€"), "de": ("EUR", "€"), "deutschland": ("EUR", "€"),
    "france": ("EUR", "€"), "fr": ("EUR", "€"),
    "italy": ("EUR", "€"), "it": ("EUR", "€"), "italia": ("EUR", "€"),
    "spain": ("EUR", "€"), "es": ("EUR", "€"), "espana": ("EUR", "€"),
    "netherlands": ("EUR", "€"), "nl": ("EUR", "€"),
    "ireland": ("EUR", "€"), "ie": ("EUR", "€"),
    "portugal": ("EUR", "€"), "pt": ("EUR", "€"),
    "belgium": ("EUR", "€"), "be": ("EUR", "€"),
    "austria": ("EUR", "€"), "at": ("EUR", "€"),
    "switzerland": ("CHF", "CHF "), "ch": ("CHF", "CHF "),
    "south korea": ("KRW", "₩"), "korea": ("KRW", "₩"), "kr": ("KRW", "₩"),
    "brazil": ("BRL", "R$"), "br": ("BRL", "R$"), "brasil": ("BRL", "R$"),
    "mexico": ("MXN", "MX$"), "mx": ("MXN", "MX$"),
    "saudi arabia": ("SAR", "SAR "), "saudi": ("SAR", "SAR "), "ksa": ("SAR", "SAR "),
    "qatar": ("QAR", "QAR "), "qa": ("QAR", "QAR "),
    "new zealand": ("NZD", "NZ$"), "nz": ("NZD", "NZ$"),
    "south africa": ("ZAR", "R"), "za": ("ZAR", "R"),
    "thailand": ("THB", "฿"), "th": ("THB", "฿"),
    "malaysia": ("MYR", "RM"), "my": ("MYR", "RM"),
    "indonesia": ("IDR", "Rp"), "id": ("IDR", "Rp"),
    "philippines": ("PHP", "₱"), "ph": ("PHP", "₱"),
    "vietnam": ("VND", "₫"), "vn": ("VND", "₫"),
    "nigeria": ("NGN", "₦"), "ng": ("NGN", "₦"),
    "kenya": ("KES", "KSh"), "ke": ("KES", "KSh"),
    "egypt": ("EGP", "E£"), "eg": ("EGP", "E£"),
    "pakistan": ("PKR", "Rs"), "pk": ("PKR", "Rs"),
    "bangladesh": ("BDT", "৳"), "bd": ("BDT", "৳"),
    "sri lanka": ("LKR", "Rs"), "lk": ("LKR", "Rs"),
    "israel": ("ILS", "₪"), "il": ("ILS", "₪"),
    "turkey": ("TRY", "₺"), "turkiye": ("TRY", "₺"), "tr": ("TRY", "₺"),
    "poland": ("PLN", "zł"), "pl": ("PLN", "zł"),
    "sweden": ("SEK", "kr"), "se": ("SEK", "kr"),
    "norway": ("NOK", "kr"), "no": ("NOK", "kr"),
    "denmark": ("DKK", "kr"), "dk": ("DKK", "kr"),
    "argentina": ("ARS", "AR$"), "ar": ("ARS", "AR$"),
    "chile": ("CLP", "CL$"), "cl": ("CLP", "CL$"),
    "colombia": ("COP", "COL$"), "co": ("COP", "COL$"),
    "hong kong": ("HKD", "HK$"), "hk": ("HKD", "HK$"),
    "taiwan": ("TWD", "NT$"), "tw": ("TWD", "NT$"),
}


def detect_currency(country: str) -> tuple[str, str]:
    """
    Return (currency_code, symbol) for a free-text country field.
    Returns ("", "") for empty or unrecognized input — the UI must never
    silently assume USD. No network calls.
    """
    key = (country or "").strip().lower().rstrip(".")
    if key in _CURRENCIES:
        return _CURRENCIES[key]
    # Substring match, e.g. "Mumbai, India" or "India (IN)".
    for name, cur in _CURRENCIES.items():
        if len(name) > 3 and name in key:
            return cur
    return ("", "")
