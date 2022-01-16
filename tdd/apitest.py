import requests
import json


url = "https://gorest.co.in/public/v1/users"

data = requests.get(url)

to_test = data.text
#print(data.json())

text = """{"meta":{"pagination":{"total":1311,"pages":66,"page":1,"limit":20,"links":{"previous":null,"current":"https://gorest.co.in/public/v1/users?page=1","next":"https://gorest.co.in/public/v1/users?page=2"}}},"data":[{"id":7,"name":"Kashyapi Chattopadhyay","email":"kashyapi_chattopadhyay@wolff.info","gender":"female","status":"active"},{"id":8,"name":"Chakor Kocchar","email":"chakor_kocchar@sporer-lakin.io","gender":"male","status":"active"},{"id":9,"name":"Vaijayanthi Gupta MD","email":"vaijayanthi_md_gupta@bode.org","gender":"female","status":"inactive"},{"id":11,"name":"Anagh Panicker","email":"panicker_anagh@heathcote.net","gender":"female","status":"inactive"},{"id":12,"name":"Ashlesh Varrier","email":"varrier_ashlesh@dickens.info","gender":"female","status":"active"},{"id":13,"name":"Anjushri Kaur","email":"anjushri_kaur@schneider.biz","gender":"female","status":"active"},{"id":14,"name":"Bhagavaan Desai","email":"desai_bhagavaan@bogan.io","gender":"female","status":"active"},{"id":15,"name":"Jay Iyer","email":"iyer_jay@wolf-shanahan.co","gender":"female","status":"inactive"},{"id":16,"name":"Sarisha Nambeesan","email":"sarisha_nambeesan@buckridge.name","gender":"male","status":"active"},{"id":17,"name":"Amb. Jitendra Asan","email":"amb_jitendra_asan@weissnat-schroeder.net","gender":"male","status":"inactive"},{"id":18,"name":"Sujata Kocchar","email":"kocchar_sujata@beahan.com","gender":"male","status":"inactive"},{"id":21,"name":"Gorakhanatha Tandon","email":"tandon_gorakhanatha@herzog.info","gender":"female","status":"inactive"},{"id":22,"name":"Shobhana Khanna","email":"shobhana_khanna@wilderman.biz","gender":"male","status":"inactive"},{"id":23,"name":"Adityanandana Patel LLD","email":"lld_patel_adityanandana@emard.io","gender":"male","status":"inactive"},{"id":24,"name":"Tapan Chattopadhyay","email":"chattopadhyay_tapan@robel.io","gender":"female","status":"inactive"},{"id":25,"name":"Rev. Tanushree Nambeesan","email":"nambeesan_tanushree_rev@effertz-altenwerth.name","gender":"male","status":"active"},{"id":26,"name":"Gautam Bhattacharya","email":"bhattacharya_gautam@oconnell.net","gender":"female","status":"active"},{"id":27,"name":"Harita Reddy","email":"reddy_harita@paucek.info","gender":"male","status":"inactive"},{"id":28,"name":"Dr. Ekalavya Mehra","email":"ekalavya_mehra_dr@ziemann.net","gender":"male","status":"active"},{"id":29,"name":"Avantika Sharma","email":"avantika_sharma@pfannerstill-koch.net","gender":"female","status":"inactive"}]}"""


text = json.loads(text)


print(type(text))
print(type(data.json()))

if sorted(text.items()) == sorted(data.json().items()):
    print("OK")

else:
    print("No")


f = open('dumptest.txt','a+')
f.write(str(text))
f.write(str(data.json()))
f.close()
