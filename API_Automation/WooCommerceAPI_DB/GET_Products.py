from woocommerce import API

wcapi = API(
    url="http://mystore.local",
    consumer_key="ck_014699ef04695e1d5974c49e808428f7ae2693aa",
    consumer_secret="cs_8b9a93440960682db1601c50a9d165e8b3bc23e2",
    version="wc/v3",
    timeout=15
)

r = wcapi.get("products")
import pprint

pprint.pprint(r.json())
