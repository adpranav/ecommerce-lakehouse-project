# resources/config.py - Final Configuration File

def get_config(env: str):
    """
    Returns environment-specific configurations.
    
    Args:
        env (str): The target environment ('dev', 'prod').
        
    Returns:
        dict: A dictionary containing all configuration parameters.
    """
    
    # --- Base Configuration (using full data paths) ---
    # These values are the same for all environments but need to be defined once.
    config = {
        "SCHEMA_BRONZE": "bronze",
        "SCHEMA_SILVER": "silver",
        "SCHEMA_GOLD": "gold",
        
        # Base Path for ALL Raw Data Sources (Your Azure Blob location)
        "RAW_DATA_PATH_BASE": "abfss://adv@databrickspractice1.dfs.core.windows.net/",
        # Checkpoint path for streaming (must be unique and writeable)
        "CHECKPOINT_PATH_BASE": "abfss://managed@databrickspractice1.dfs.core.windows.net/checkpoints/",
        
        # Table-Specific Data Paths (The folder/file location in your Azure Blob)
        # NOTE: Adjust these paths if your file names or folders change!
        "PATH_CUSTOMERS": "abfss://adv@databrickspractice1.dfs.core.windows.net/customers",
        "PATH_PRODUCTS": "abfss://adv@databrickspractice1.dfs.core.windows.net/products",
        "PATH_ORDERS": "abfss://adv@databrickspractice1.dfs.core.windows.net/orders",
        "PATH_ORDER_ITEMS": "abfss://adv@databrickspractice1.dfs.core.windows.net/order_items",
        "PATH_REVIEWS": "abfss://adv@databrickspractice1.dfs.core.windows.net/product_reviews",
        
        # Processing Mode Overrides
        "MODE_ORDERS": "streaming", # Orders is high-velocity, so we use streaming
        "MODE_DEFAULT": "batch",    # All other tables use batch (overwrite mode)
    }

    # --- Environment Overrides (Changes the Target Catalog) ---
    if env == "prod":
        config["CATALOG_NAME"] = "ecommerce_prod"
    elif env == "staging":
        config["CATALOG_NAME"] = "ecommerce_staging"
    else: # Default is "dev"
        config["CATALOG_NAME"] = "ecommerce_dev"
        
    # --- Dynamic Path Construction ---
    # Creates FULL_SCHEMA_BRONZE, FULL_SCHEMA_SILVER, etc. (e.g., ecommerce_dev.bronze)
    for key in ["SCHEMA_BRONZE", "SCHEMA_SILVER", "SCHEMA_GOLD"]:
        config[f"FULL_{key}"] = f"{config['CATALOG_NAME']}.{config[key]}"
        
    return config