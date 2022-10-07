import requests
import pandas as pd

url = "https://data.hkp.com.hk/search/v1/properties"

hkp_data = pd.DataFrame(columns =['price','floor_level','bedroom_amount','net_area',
                                      'district','address','misc','facility','url_desc'])
for x in range(1, 100):
    querystring = {"hash":"true","lang":"en","currency":"HKD","unit":"feet","search_behavior":"normal","tx_type":"S","score":"false","page":f"{x}","limit":"100"}

    payload = ""
    headers = {
        "authority": "data.hkp.com.hk",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJndWlkIjoibXItMjAyMi0wOC0yOS0zbktTWUN5b1hBOWFqS2JlSFF2QnJHTkk2OU5mTjRDTzBVSW5felpwX1g0Y0RUb2NYNTZaQUtqWVJONl9QY2hrc0U5ZkdvNS1JSSIsImlhdCI6MTY2MTc0MTE4MSwiaXNzIjoid3d3LmhrcC5jb20uaGsifQ.PkRkCxOM4RgxFff7TV-MuYaUoucG6kmz8ef0BXIjPdbulwDV2d1d4Z4TnVFgcLOUsPWrwEWvTTE0LWmqonxDmEc8lWB-VoVtuQmb8KZFnj0_mF9AROyISABLpAgQJUZC0FgclQpqJKFcZ-45OvJoW4l-DYlHP55-_YW_9bgweuZGKeTVUGceaauD66C4_QzHQK6uTARShl22xbT0Esn2by5xq3IJAjymXh6bCCFHI5iWhVzc94BYSYjCeH8fGH1FwbkOb2TUyexN7N3_pn0rKoxLibOHliIX2Q2hU_3QzRYcF6kGfKUszGkWOd-l_zvNxay-yv2rtmuLjnPEDBgg3cuJtpXmhb-Q2PIabQ2jdHbWH6i3NPPiFzWRonPWNAT424MefqEUIQpRraDUyv8vaNZk42CaGJ3pxy_IIpPF5EZ3uBHvp7CrN5E1eME-yC16zZ5mNXfTjwr59R3572Qzd1Z5ayleMSKkudq6iXgEZ_Bt1fgk6dwY2KtqwN_BPJnlk8_JgfEIU8s_Hb7X9pezmmcaCl8HBlwVtXm5pzrfVbKNDjFjJ8NsELAviwFR-5AUBBKY0FEk-4vfwSLKd53c0K9AxSGKrbAt-Vfn3TdfiqBoKPmM59bpUgiiqwutTeuuISYGptKMu-qt7aOf2CXFlvhyjSERPl14ofGF0GqMSCo",
        "cache-control": "no-cache",
        "dnt": "1",
        "origin": "https://www.hkp.com.hk",
        "pragma": "no-cache",
        "referer": "https://www.hkp.com.hk/",
        "sec-ch-ua": "'Chromium';v='104', 'Not A;Brand';v='99', 'Google Chrome';v='104'",
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": "'Android'",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36"
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
        hkp_data = hkp_data.append(helper, ignore_index=True)
        print(len(hkp_data))

hkp_data.to_csv('hkp.csv',encoding='utf-8')