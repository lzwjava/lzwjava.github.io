---
title: Debugging a Hetzner Cloud Server Snapshot Script
lang: en
layout: post
audio: false
translated: false
generated: true
---

# Debugging and Enhancing a Hetzner Cloud Server Snapshot Script

This article documents the process of troubleshooting and improving a Python script for managing Hetzner Cloud server snapshots and cloning servers.

## The Initial Problem

The script was encountering an error where a 'Server' object had no attribute 'create_snapshot'. The issue was in the `scripts/auto-ss-config/hetzner.py` file, which needed to be fixed to properly create snapshots.

## Step 1: Identifying the Bug

After examining the code, I identified that the error occurred because the script was trying to call `create_snapshot()` directly on a server object, but this method doesn't exist in the hcloud Python library's Server class.

The initial problematic code was:

```python
snapshot = server.create_snapshot(name=f"{server.name}-snapshot")
```

## Step 2: First Fix Attempt

The first fix was to use the client's servers API instead:

```python
snapshot = client.servers.create_snapshot(server, description=f"{server.name}-snapshot")
```

However, this led to a new error: `'ServersClient' object has no attribute 'create_snapshot'`

## Step 3: Investigating the Correct API

To understand the correct API method, I examined the hcloud Python library. This revealed that I needed to use `client.servers.create_image()` rather than trying to use a non-existent method.

The correct solution was:

```python
response = client.servers.create_image(server, description=f"{server.name}-snapshot", type="snapshot")
```

## Step 4: Enhancing the Script

After fixing the initial bug, I enhanced the script to add the ability to create new servers from snapshots. This involved:

1. Waiting for snapshots to be fully available before using them
2. Adding command-line arguments for flexibility
3. Improving error handling
4. Creating a more robust solution for checking snapshot status

## Final Implementation

The enhanced script now supports:

- Creating snapshots with: `python scripts/auto-ss-config/hetzner.py --create-snapshot [--server-name NAME]`
- Creating a server from an existing snapshot: `python scripts/auto-ss-config/hetzner.py --create-server --snapshot-id ID [--server-name NAME]`
- Doing both in one command: `python scripts/auto-ss-config/hetzner.py --create-snapshot --create-server [--server-name NAME]`

The script successfully creates snapshots and then uses them to create new server instances with the same specifications (server type, datacenter location) as the original server.

## Key Learnings

1. When working with cloud provider APIs, it's important to use the correct method calls as specified in their documentation
2. Resources like snapshots often have states (e.g., "creating", "available") that need to be properly handled
3. Adding command-line arguments improves script flexibility
4. Proper error handling and waiting mechanisms are essential for robust cloud automation scripts

This debugging process demonstrates how to systematically identify and fix issues in Python scripts that interact with cloud provider APIs.
