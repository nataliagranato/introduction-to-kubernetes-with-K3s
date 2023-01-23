# Implante o seu ambiente de laboratório

k3d é um pequeno programa feito para executar um cluster K3s  no Docker. O K3s é um projeto Sandbox e distribuição Kubernetes leve e certificado pela CNCF. Projetado para ambientes de poucos recursos, o K3s é distribuído como um único binário que usa menos de 512 MB de RAM.

O k3d facilita muito a criação de clusters k3s de um ou vários nós no docker, por exemplo, para desenvolvimento local no Kubernetes.

*Requisitos*
Tenha o docker instalado para poder utilizar o k3d.
O kubectl para interagir com o cluster Kubernetes.

## Instalação via script
```
wget -q -O - https://raw.githubusercontent.com/k3d-io/k3d/main/install.sh | bash
```

## Criando um cluster k3s de alta disponibilidade com o k3d
Como as práticas recomendadas de alta disponibilidade do Kubernetes, devemos criar um cluster de alta disponibilidade com pelo menos três nós control plane.

Podemos conseguir isso no k3d em um comando:
```
k3d cluster create --servers 3 --image rancher/k3s:v1.23.15-k3s1-amd64
```

### Aprendendo o comando:
Comando base: k3d cluster create
Opções:
– server 3: solicita que três nós sejam criados.

– image rancher/k3s:v1.19.3-k3s2: especifica a imagem K3S a ser usada.

Agora podemos verificar o que foi criado a partir dos diferentes pontos de vista:
```
kubectl get nodes --output wide
```
