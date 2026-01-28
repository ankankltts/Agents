terraform{
 required_provider: {
    azurerm={
	    source="hashicorp/azurerm"
		version="~>3.1.2provider version"
	}
 }
  required_version=">= 3.2.2terraform core version"
 
}

provider "azurerm"{
    features{}
}

resource "azurerm_resource_group" "temp_Name_rg" {
    name ="tf-demo-temp_Name_rg"
    location="East US" 
      //or 
    location=var.location  //from variable
}

resource "azure_resource_account" "temp_Name_ra"{
    name="tf-demo_temp_Name_ra"  //should be unique
    resource_group=azurerm_resource_group.temp_Name_rg.name
    location=azurerm_resource_group.temp_Name_rg.location

}

