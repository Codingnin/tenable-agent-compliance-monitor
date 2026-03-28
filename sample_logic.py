def compare_assets(cmdb_assets, agent_assets):
    """
    Simple placeholder logic for future implementation.
    Returns assets that are present in CMDB but not reporting through agent data.
    """
    cmdb_set = set(cmdb_assets)
    agent_set = set(agent_assets)
    return sorted(list(cmdb_set - agent_set))


if __name__ == "__main__":
    cmdb_assets = ["server01", "server02", "server03"]
    agent_assets = ["server01"]
    missing = compare_assets(cmdb_assets, agent_assets)
    print("Missing agent coverage:", missing)