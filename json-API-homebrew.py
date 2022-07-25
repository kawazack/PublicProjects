import json
import time
import requests

header={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

r = requests.get('https://formulae.brew.sh/api/formula.json', headers=header)

packages_json = r.json()
#print the total packages to further inspect
#print(packages_json[:2]) as test, slice the data returned

""" first element of the packages_json: commented because was only test to valadiate and to not use so much resources. """
#package_name = packages_json[0]['name']
#package_desc = packages_json[0]['desc']

#general URL using f format and variable

#p = json.dumps(packages_json[:10], indent=2)
#print(p)

results = []
t1 = time.perf_counter()


for package in packages_json[:10]:
    package_name = package['name'] #individual package name
    package_desc = package['desc'] #individual package desc

    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json' 

    r = requests.get(package_url)
    package_json = r.json()

    installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
    installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
    installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

    data = {
        'name': package_name,
        'desc': package_desc,
        'analytics': {
            '30d': installs_30,
            '90d': installs_90,
            '365d': installs_365,        
        }
    }
    #print(package_name)
    results.append(data)
    time.sleep(r.elapsed.total_seconds())
    print(f'Got {package_name} in {r.elapsed.total_seconds()} seconds')

t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')

with open('homebrew_package_info.json', 'w+') as f:
    json.dump(results, f, indent=2)




# total packages with better json indent
# packages_str = json.dumps(packages_json[0], indent=2)
# print(packages_str)

# package_str = json.dumps(package_json, indent=2)
# print(package_str[:1])

# installs_30 = package_json['analytics']['install_on_request']['30d'][package_name]
# installs_90 = package_json['analytics']['install_on_request']['90d'][package_name]
# installs_365 = package_json['analytics']['install_on_request']['365d'][package_name]

# print(package_name, package_desc, installs_30, installs_90, installs_365)

#print("The total length of the packages_json from homebrew API is: "+ str(len(packages_json)))


#print(results)




