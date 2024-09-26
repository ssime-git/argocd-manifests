alias:
	alias k8s='microk8s kubectl'
getpass:
	kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d