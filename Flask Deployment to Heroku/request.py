import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'brand': 'trek',
                            'model': 'crossgrip',
                            'speed': 24,
                            'timetilend': 1,
                            'current bid count': 100,
                            'stand over height': 31,
                            'gear shifter brand': 'shimano',
                            'front derailleur brand': 'shimano',
                            'rear derailleur brand': 'shimano',
                            'brake lever brand': 'shimano',
                            'crank set brand': 'fsa',
                            'brake type': 'disc'})

print(r.json())