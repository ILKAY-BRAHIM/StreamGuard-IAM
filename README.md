# Keycloak and RabbitMQ for Streaming-Driven IAM

## Project Overview
This project implements a scalable, secure, and multi-tenant identity and access management (IAM) solution using Keycloak, enhanced by RabbitMQ for targeted streaming and asynchronous messaging. It integrates multiple applications to handle real-time event streaming, automates deployments, and demonstrates system resilience.

## Key Features
- **High-Availability Keycloak and RabbitMQ Clusters**: Deployed on Kubernetes for scalability and fault tolerance.
- **Multi-Tenancy**: Separate Keycloak realms for Corporate, Partner, and Customer use cases.
- **Advanced Authentication**: Multi-Factor Authentication (MFA) using OTP and WebAuthn, with real-time notifications.
- **Streaming Integration**: RabbitMQ configured for targeted, real-time event streaming per tenant.
- **DevOps Automation**: Deployment scripts and CI/CD pipelines for dynamic provisioning and updates.
- **Monitoring and Resilience**: Real-time dashboards and failure simulation tests.

## Folder Structure
```
project-keycloak-rabbitmq/
├── README.md                       # Overview and setup instructions
├── docs/                           # Detailed documentation
├── scripts/                        # Deployment and CI/CD scripts
├── helm/                           # Helm charts for Kubernetes deployments
├── kubernetes/                     # Kubernetes manifests
├── config/                         # Configuration files for Keycloak and RabbitMQ
├── monitoring/                     # Monitoring setup for Grafana and Prometheus
├── tests/                          # Unit, integration, and resilience tests
├── ci-cd/                          # CI/CD pipelines
└── logs/                           # Logs for debugging and monitoring
```

## Prerequisites
- Kubernetes Cluster (e.g., K3s or K3d)
- Helm 3+
- Docker
- Terraform or Ansible (for provisioning)
- Prometheus and Grafana (for monitoring)
- Python 3.8+ (for testing)

## Deployment Steps

### 1. Provision Infrastructure
Use the provided Terraform/Ansible scripts to provision infrastructure:
```bash
cd scripts
./provision-infra.sh
```

### 2. Deploy Keycloak and RabbitMQ
Use Helm or Kubernetes manifests:
```bash
# Deploy Keycloak
helm install keycloak ./helm/keycloak

# Deploy RabbitMQ
helm install rabbitmq ./helm/rabbitmq
```

### 3. Configure Multi-Tenancy
- Add realms for Corporate, Partner, and Customer users using the JSON configuration files in `config/keycloak/realms`.
- Apply customized login themes located in `config/keycloak/login-themes`.

### 4. Set Up Streaming
- Configure RabbitMQ topics and queues using the files in `config/rabbitmq/`.
- Enable targeted streaming for realm-specific event notifications.

### 5. Enable Monitoring and Logging
- Set up Prometheus and Grafana using configurations in `monitoring/`.
- Aggregate logs using ELK Stack or Loki.

### 6. Validate the Deployment
Run tests to ensure functionality and resilience:
```bash
cd tests
pytest
```

## Monitoring and Resilience
- **Monitoring**: Use Grafana dashboards to monitor RabbitMQ streaming and Keycloak activity.
- **Resilience Tests**: Simulate message delivery delays, queue saturation, and node failures using the resilience test scripts.

## Contributing
Contributions are welcome! Please fork the repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

For detailed documentation, refer to the `docs/` folder.