alias:
	alias k8s='microk8s kubectl'
getpass:
	kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
update:
	docker rmi ssimedockerhub/ml-pipeline:latest
	docker build -t ssimedockerhub/ml-pipeline:latest .
	docker push ssimedockerhub/ml-pipeline:latest

sync:
	argocd app sync ml-pipeline-2

monitor:
	kubectl logs -n argocd -l workflows.argoproj.io/workflow=ml-pipeline-workflow --follow