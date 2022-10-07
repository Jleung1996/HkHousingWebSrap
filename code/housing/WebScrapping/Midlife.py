import requests
import pandas as pd
url = "https://data.midland.com.hk/search/v2/properties"

Midlife_data = pd.DataFrame(columns =['price','floor_level','bedroom_amount','net_area',
                                      'district','address','misc','facility','url_desc'])
for x in range(1, 100):
    querystring = {"hash": "true", "lang": "en", "currency": "HKD", "unit": "feet", "search_behavior": "normal",
                   "tx_type": "S", "limit": "100", "page": f"{x}", }

    payload = ""

    headers = {
        "authority": "data.midland.com.hk",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9"
                         ".eyJndWlkIjoibXItMjAyMi0wOC0yNy1oc2s4dGxlaVVaNkNOUGc4QmJPd2V3WnNOazZnR3o5Zlg1dmV4aTlPUjJEZVRfVDRjZV8zdFhjQ2pQbGJYNzNHRlRmWWJaTy1JSSIsImlhdCI6MTY2MTU2MTQ1MywiaXNzIjoiZGF0YS5taWRsYW5kLmNvbS5oayJ9.vVPdXz5rxNKdqbTEmKQ0OYQQK3LXrJgSo7_vkWfphl-eR1eimKjHbxusbKlh4seetMnwPLwrmPjEeLOc0LY5WURkcbhhVR2wRGLT1Rc3kgP3Y1ViUrGu_hZ6l7CE9qnRn0d4YWDHQwryLBA1oQ7FpR_8rrjppMIYbc081zmnzBB4xpiOOR90xB6nk7iBHcWF15Qz8BJjsDQ4Hel7XMSB3JlrFG6VgNTPSUDLxSyYfzWT7V_XccI9cngQioPLdLckKX-QWJ-4ZoZBiKVLVTM-pOmjC-AIQjD8hQ_nIfpFVx8pJJnJa-blyKexW0BsB4kKo5EypNh6gbz3K3zFLT4diZJFCxsob_ZXCF0bGMJIJ_NumTQF-pAv_ClKWuY2tYo51jw5Elf6XzTmmZAkiq4dlTxStwSaV8UZQZDTF6zDEQPzpPNNb3HcB2zW-NK0HwUhFSS8g9mbY1UgtWpuwnWwlr6O1oTDInQaEO0jp-krCeV4JXgFKGs-9nLGhtu9cmESaw18QdFAW05bqoQhYFaxxOyx3OlU_pFDSb7XEq3aLCw7EQLoPIwArIhjLGIkYRNiylnaCswX-Ir0PiCnid87MnLFrE-o4QesbYVWk06P7B0OCFIQhzYVXu_CxT7ePiT_aj4p1jemPq4VkEd3hECCSiJFGB6OK09FzJG-XlExxzY",
        "cache-control": "no-cache",
        "dnt": "1",
        "origin": "https://www.midland.com.hk",
        "pragma": "no-cache",
        "referer": "https://www.midland.com.hk/",
        "sec-ch-ua": "'Chromium';v='104', 'Not A;Brand';v='99', 'Google Chrome';v='104'",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "'Android'",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/104.0.0.0 Mobile Safari/537.36 "
    }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = response.json()
    for results in data['result']:
        helper = pd.DataFrame(columns=['price', 'floor_level', 'bedroom_amount', 'net_area',
                                       'district', 'address', 'misc', 'facility', 'url_desc'])
        price = []
        floor_level = []
        bedroom_amount = []
        net_area = []
        district = []
        address = []
        misc = []
        facility = []
        url_desc = []
        try:
            price.append(results['price'])
            helper['price'] = price
        except:
            pass
        try:
            floor_level.append(results['floor_level']['id'])
            helper['floor_level'] = floor_level
        except:
            pass
        try:
            bedroom_amount.append(results['bedroom'])
            helper['bedroom_amount'] = bedroom_amount
        except:
            pass
        try:
            net_area.append(results['net_area'])
            helper['net_area'] = net_area
        except:
            pass
        try:
            district.append(results['district']['name'])
            helper['district'] = district
        except:
            pass
        try:
            address.append(results['building']['address'])
            helper['address'] = address
        except:
            pass
        try:
            misc.append(results['misc']['sell'])
            helper['misc'] = misc
        except:
            pass
        try:
            facility.append(results['facilityGroup'])
            helper['facility'] = facility
        except:
            pass
        try:
            url_desc.append(results['url_desc'])
            helper['url_desc'] = url_desc
        except:
            pass
        Midlife_data = Midlife_data.append(helper, ignore_index=True)
        print(len(Midlife_data))

Midlife_data.to_csv('Mid_lifeV2.csv',encoding='utf-8')