# Azure Virtual Machines (VMs) Setup and Hosting Guide

This guide explains how to create **Windows** and **Linux VMs** on the Azure portal, manage **Network Security Groups (NSGs)**, and host a **Node.js project** on a Linux VM using **NGINX**. It also covers the use of **custom/user data** for automated configuration.

---

## 1. Create Windows VM on Azure Portal

### Steps:
1. **Log in to Azure Portal:**  
   - Visit [https://portal.azure.com](https://portal.azure.com)

2. **Create a Resource:**  
   - Click **Create a resource** → **Compute** → **Windows Virtual Machine**

3. **Configure Basic Settings:**
   - **Subscription:** Free trial  
   - **Resource Group:** `rg-vm-shreya`  
   - **Virtual Machine Name:** `vm-windows`  
   - **Region:** North Europe  
   - **Image:** Windows Server 2019 Datacenter  
   - **Size:** Standard_B2s  
   - **Administrator Account:** Set username and password  

4. **Inbound Port Rules:**  
   - Open **RDP (3389)** for remote desktop access.

5. **Review and Deploy:**  
   - Click **Review + Create** → **Create** to deploy the VM.

6. **Access Your VM:**  
   - Go to the **VM Overview** and copy the **public IP address**.  
   - Use **Remote Desktop (RDP)** to connect by entering the public IP, username, and password.

---

## 2. Create Linux VM on Azure Portal

### Steps:
1. **Log in to Azure Portal:**  
   - Visit [https://portal.azure.com](https://portal.azure.com)

2. **Create a Resource:**  
   - Click **Create a resource** → **Compute** → **Linux Virtual Machine**

3. **Configure Basic Settings:**
   - **Subscription:** Free trial  
   - **Resource Group:** `rg-vm-shreya`  
   - **Virtual Machine Name:** `vm-linux`  
   - **Region:** North Europe  
   - **Image:** Ubuntu Server 20.04 LTS  
   - **Size:** Standard_B2s  

4. **Administrator Account:**  
   - **Password Authentication:** Set a username and password.  
   - **SSH Authentication:** Provide your **public SSH key**.

5. **Inbound Port Rules:**  
   - Open **SSH (22)** to allow remote login.

6. **Review and Deploy:**  
   - Click **Review + Create** → **Create** to deploy the VM.

7. **Access Your VM:**  
   - Copy the **public IP address** from the **VM Overview**.  
   - Use an SSH client to connect:
     ```bash
     ssh -i <path to downloaded ssh public key> <username>@<public-ip>
     ```

---

## 3. Network Security Groups (NSGs) in Azure for VMs

### Overview:
A **Network Security Group (NSG)** is a virtual firewall that controls inbound and outbound network traffic to resources like VMs.

### Key Features:
- **Inbound and Outbound Rules:** Control traffic based on protocols, IPs, and ports.
- **Example Use Case:**  
  - Allow **RDP (3389)** to a Windows VM.  
  - Allow **SSH (22)** to a Linux VM.  
  - Block all other inbound traffic for security.

### Rule Components:
- **Source and Destination:** IP ranges or services.
- **Port:** Example: Port 80 for HTTP traffic.
- **Protocol:** TCP, UDP, or Any.
- **Priority:** Lower priority rules take precedence.

---

## 4. Host a Website on Linux VM Using NGINX

### Steps:
1. **Create a Linux VM:**  
   - Follow the steps from **Create Linux VM on Azure Portal**.

2. **Create a Node.js Project Locally.**

3. **Transfer Files to VM:**  
   Use `scp` to copy the Node.js project to the VM:
   ```bash
   scp -i ~/Downloads/myKey.pem -r my-node-app <your-username>@<VM-IP-Address>:/home/<your-username>/

 4. Connect to the VM Using SSH

Log in to the Linux VM using the following SSH command:

```bash
ssh -i <path to public key .pem file> <username>@<public-ip>



