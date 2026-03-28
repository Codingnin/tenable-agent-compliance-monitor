# tenable-agent-compliance-monitor

# Tenable Agent Compliance Monitor

A practical open-source project focused on improving visibility into missing, offline, or unhealthy Tenable/Nessus agent coverage in enterprise environments.

## Problem

In large enterprise environments, checking agent compliance is often manual and fragmented:
- Some systems do not have the agent installed
- Some agents are offline or stale
- Different data sources must be compared manually
- Security teams spend too much time preparing reports instead of fixing issues

## Goal

This project aims to simplify agent compliance monitoring by combining:
- Nessus / agent status exports
- CMDB or inventory data
- Basic comparison logic
- Report generation for remediation follow-up

## Planned Features

- Detect hosts missing Tenable agents
- Identify offline or stale agents
- Compare security data with CMDB inventory
- Export compliance gap reports
- Support prioritization by asset criticality
- Extend later with alerting and dashboards

## Why this project matters

This project is inspired by real-world vulnerability management and security operations workflows, where teams need a faster and more reliable way to track scanning readiness and agent health.

## Roadmap

- [x] Create repository and project scope
- [ ] Add sample input files
- [ ] Build first comparison script
- [ ] Add reporting output
- [ ] Add dashboard-friendly export
- [ ] Add documentation for enterprise adaptation

## Use cases

- Vulnerability management teams
- Security operations teams
- Compliance monitoring
- Enterprise asset coverage validation

## Status

Early project setup. Initial structure and documentation are being prepared.

## License

MIT