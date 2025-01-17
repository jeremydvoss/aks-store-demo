resource "azurerm_key_vault" "example" {
    name                        = "kv-${local.name}"
    location                    = azurerm_resource_group.example.location
    resource_group_name         = azurerm_resource_group.example.name
    enabled_for_disk_encryption = true
    tenant_id                   = data.azurerm_client_config.current.tenant_id
    sku_name                    = "standard"
}

resource "azurerm_key_vault_access_policy" "example" {
  key_vault_id = azurerm_key_vault.example.id
  tenant_id    = data.azurerm_client_config.current.tenant_id
  object_id    = data.azurerm_client_config.current.object_id
  secret_permissions = [
    "Get",
    "Set",
    "List",
    "Delete",
    "Purge"
  ]
}

resource "azurerm_key_vault_secret" "openai_key" {
    name         = "AZURE-OPENAI-KEY"
    value        = azurerm_cognitive_account.example.primary_access_key
    key_vault_id = azurerm_key_vault.example.id
    depends_on = [ azurerm_key_vault_access_policy.example ]
}

resource "azurerm_key_vault_secret" "cosmosdb_key" {
    name         = "AZURE-COSMOS-KEY"
    value        = azurerm_cosmosdb_account.example.primary_key
    key_vault_id = azurerm_key_vault.example.id
    depends_on = [ azurerm_key_vault_access_policy.example ]
}

resource "azurerm_key_vault_secret" "listener_key" {
    name         = "AZURE-SERVICE-BUS-LISTENER-KEY"
    value        = azurerm_servicebus_namespace_authorization_rule.example.primary_key
    key_vault_id = azurerm_key_vault.example.id
    depends_on = [ azurerm_key_vault_access_policy.example ]
}

resource "azurerm_key_vault_secret" "sender_key" {
    name         = "AZURE-SERVICE-BUS-SENDER-KEY"
    value        = azurerm_servicebus_queue_authorization_rule.example.primary_key
    key_vault_id = azurerm_key_vault.example.id
    depends_on = [ azurerm_key_vault_access_policy.example ]
}