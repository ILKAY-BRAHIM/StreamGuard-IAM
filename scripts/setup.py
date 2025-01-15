from LogFusion import LogFusion

def main():
    log_fusion = LogFusion()
    setup_workflow = [
        "curl -s https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash", # Install K3d
        "k3d cluster create streamguard-cluster --servers 1 --agents 2 --kubeconfig-update-default --wait", # Create a cluster
        "curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash", # Install Helm
        "kubectl apply -f https://openebs.github.io/charts/openebs-operator.yaml", # Deploy OpenEBS
        # "kubectl wait --for=condition=Ready pod -l app=openebs -n openebs --timeout=300s", # Wait for OpenEBS pods to be ready
        "kubectl apply -f https://github.com/cert-manager/cert-manager/releases/download/v1.13.0/cert-manager.yaml", # Install Cert-Manager
        # "kubectl wait --for=condition=Available deployment -n cert-manager --timeout=300s", # Wait for Cert-Manager pods to be ready
        "kubectl get nodes", # Verify Kubernetes Nodes
        "helm version", # Verify Helm Version
        "kubectl get pods -n openebs", # Verify OpenEBS Pods
        "kubectl get pods -n cert-manager", # Verify Cert-Manager Pods
        # "k3d cluster delete streamguard-cluster", # Delete the cluster
    ]

    log_fusion.start(setup_workflow)

if __name__ == "__main__":
    main()
