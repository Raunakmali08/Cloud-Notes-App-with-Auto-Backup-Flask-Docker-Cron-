#!/bin/bash

# Create backups directory if it doesn't exist
mkdir -p /app/backups

# Define timestamp (make sure no extra spaces!)
timestamp=$(date +"%Y-%m-%d_%H-%M-%S")

# Copy the database file with timestamp
cp /app/notes.db /app/backups/notes_backup_"$timestamp".db

# Log output
echo "Backup created at /app/backups/notes_backup_$timestamp.db"

