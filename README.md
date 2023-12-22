# the Worst Bad Usb Blocker

Este projeto oferece uma solução prática para monitorar e gerenciar dispositivos USB em um sistema operacional. Utilizando Python e o módulo `pyudev`, este projeto identifica dispositivos USB conectados, verifica se estão na lista de autorizados e desabilita os não autorizados para aumentar a segurança do sistema.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Para rodar este projeto, você precisará de Python 3 e o módulo `pyudev`. É recomendável também ter um ambiente virtual Python para isolar as dependências.

```
python3 -m venv myenv
source myenv/bin/activate
pip install pyudev
```

### 🔧 Instalação

Siga estes passos para configurar o ambiente de desenvolvimento:

1. Clone o repositório:

```
git clone https://github.com/AugustoSavi/theWorstBadUsbBlocker.git
```

2. Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

3. Execute o script `save_devices_to_env.py` para gerar o arquivo `.usb_devices` com os dispositivos USB autorizados:

```bash
python save_devices_to_env.py
```

4. Inicie o script principal para monitorar os dispositivos com super usuário:

```bash
sudo python main.py
```

## ⚙️ Executando os testes

Atualmente, não há testes automatizados implementados para este sistema.

## 📦 Implantação

Para implantar este projeto em um sistema ativo, siga as mesmas instruções de instalação, garantindo que as dependências necessárias estejam presentes no sistema de destino.

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem de programação usada
* [pyudev](https://pyudev.readthedocs.io/en/latest/) - Usado para interagir com o sistema de arquivos do dispositivo
