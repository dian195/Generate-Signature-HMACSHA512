import json
import hashlib
import hmac
import base64

# Given data
http_method = "POST"
relative_url = "/snap/v1.0/qr/qr-mpm-notify"
b2b_access_token = "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJleHAiOjE3MzM4OTgyMTAsImlzcyI6IkFTVFJBUEFZIn0."
secret_key = "AsLpH-yTjdJ-djFTd-VN98p-u6U75"
x_timestamp = "2024-12-11T13:08:29+07:00"

# Request body (minified version)
request_body = {
    "originalReferenceNo": "WBWD3VRCEN",
    "originalPartnerReferenceNo": "7b9081a0-8031-4dfe-aec1-ee4cbadfbecc",
    "latestTransactionStatus": "00",
    "transactionStatusDesc": "SUCCESS",
    "customerNumber": "9360082230001999492",
    "destinationNumber": "9360082232400047634",
    "destinationAccountName": "Bintang Motor UAT",
    "amount": {"value": "100000.00", "currency": "IDR"},
    "additionalInfo": {
        "tip": "0.00",
        "deviceId": "AstraPay",
        "channel": "POS",
        "userName": "AstraPay User",
        "merchantPan": "9360082232400047634",
        "customerPan": "9360082230001999492",
        "issuerName": "93600822",
        "transactionId": "INV/QRM/3YW4UZ/241211/2SY5Z0LV"
    }
}

# Minify the JSON request body (remove whitespaces)
minified_body = json.dumps(request_body, separators=(',', ':'))

# Hash the minified body using SHA-256
sha256_hash = hashlib.sha256(minified_body.encode('utf-8')).hexdigest().lower()

# Prepare the string to be signed
string_to_sign = f"{http_method}:{relative_url}:{b2b_access_token}:{sha256_hash}:{x_timestamp}"

# Generate the HMAC-SHA256 signature using the secret key
signature = hmac.new(secret_key.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha256).digest()

# Base64 encode the signature
signature_base64 = base64.b64encode(signature).decode('utf-8')

# Output the signature
print("Generated Signature:", signature_base64)
