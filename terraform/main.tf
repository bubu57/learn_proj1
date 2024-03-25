variable password {}

terraform {
  required_providers {
    proxmox = {
      source = "bpg/proxmox"
      version = "0.50.0"
    }
  }
}

provider "proxmox" {
  endpoint = "https://192.168.0.18:8006"
  username = "root@pam"
  password = "${var.password}"
  insecure = true
}

resource "proxmox_virtual_environment_vm" "ubuntu_vm" {
  name = "LEARN-1"
  node_name = "pve"
  vm_id = 707

  agent {
    enabled = false
  }

  memory {
    dedicated = "4096"
  }

  cpu {
    cores = 4
    numa = true
    type = "host"
  }

  network_device {
    model = "rtl8139"
  }

  started = true

  operating_system {
    type = "l26"
  }

  disk {
    datastore_id = "NVME_PNY"
    file_id      = "local:iso/focal-server-cloudimg-amd64.img"
    interface    = "scsi0"
    size         = "80"
  }

  initialization  {
    ip_config {
      ipv4 {
        address = "192.168.0.123/24"
        gateway = "192.168.0.1"
      }
    }
    user_account {
      keys     = ["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIGbHxu/JPLjmHpQ4JsT1aakiCyzysNnVzC6yArMmD8P4 bubu@gmail.com"]
      password = "azerty"
      username = "bubu"
    }
  }

}




