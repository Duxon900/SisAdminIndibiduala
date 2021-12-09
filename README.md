# SisAdminIndibiduala
Docker
'''
$ docker-compose up
'''

kubernetes: k8s-en klase asko daude, baina funtzionatzeko:
- Datu basea kanpoalderako funtzionatzeko:
'''
$ kubectl apply -f k8s/service.yml
$ kubectl apply -f k8s/pvc.yml
$ kubectl apply -f k8s/pod-blob.yml
'''
