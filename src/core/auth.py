import os

from dotenv import load_dotenv


load_dotenv()


CAS_SECURE_KEY = os.getenv("CAS_SECURE_KEY", default="access_token_cookie")

TEST_PUBLIC_KEY = """"
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDIzi1aV7xG1BGjwf1ZsCxiMO5j
dYEPVfdPDLbBQtMD4VZlNb4ps2B6bExyLisOUxnlhEqdVn424EHIFRwNAV3eo0Gc
RrEGT4u57+Esqy9QQmvknJaA+oBFlzCpMLV3clQIm6ropbVtgqQtnLH19WJMfal3
nwB/v8Nle2XNQ7DJKwIDAQAB
-----END PUBLIC KEY-----
"""

JWT_SECRET = os.getenv("JWT_SECRET", default=TEST_PUBLIC_KEY)

JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", default="RS256")
