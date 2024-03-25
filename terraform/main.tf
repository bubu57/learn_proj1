terraform {
  required_providers {
    proxmox = {
      source = "bpg/proxmox"
      version = "0.50.0"
    }
  }
}

provider "proxmox" {
    endpoint = "http://192.168.0.18:8006"
    username = "root"
    password = var.password
    insecure = true
}




