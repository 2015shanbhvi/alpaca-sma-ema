API_KEY = "PK3F7E6RMAG2KV22FSSN"
SECRET_KEY = "MpHWB/wSscmncHu0g5cjnhwz8K9M0UBlsSi199PK" 

BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = "{}/v2/account".format(BASE_URL)
ORDERS_URL = "{}/v2/orders".format(BASE_URL)
POSITIONS_URL = "{}/v2/positions".format(BASE_URL)

BARS_URL = "{}/v1/bars/day".format(BASE_URL)
HEADERS={"APCA-API-KEY-ID": API_KEY,"APCA-API-SECRET-KEY": SECRET_KEY}
