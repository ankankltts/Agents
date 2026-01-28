# Initialize Terraform
- terraform init
# Preview changes
- terraform plan
# Create resource
- terraform apply
# Destroy everything
- Destroy everything
# Variables
- used in main
# Outputs (for pipelines & dashboards)
- output "rg_name" {
  value = azurerm_resource_group.rg.name
}

apply: terraform output

# Terraform Workflow
- terraform init
- terraform plan
- terraform apply
- terraform destroy

# how to fit terraform in ci/cd pipeline
 Code (Git) 
   ↓
Azure DevOps Pipeline
   ↓
Terraform Init
Terraform Plan
Terraform Apply
   ↓
Azure Infrastructure

- Terraform becomes the infrastructure stage of your pipeline.
-  App code pipeline = builds & deploys code
- Terraform pipeline = creates/updates infra


# Required Setup (One-Time)
- A. Azure Service Connection (VERY IMPORTANT)
- Terraform should not use your personal login in pipelines.
- Steps:
  1. Azure DevOps → Project Settings
  2. Service connections
  3. New → Azure Resource Manager
  4. Choose
     - Authentication: Service principal (automatic)
     - Scope: Subscription


     
PR Created
   ↓
Terraform Plan (Review)
   ↓
PR Approved
   ↓
Terraform Apply (Manual Approval)