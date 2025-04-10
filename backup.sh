#!/bin/bash
mkdir -p /app/backups
cp /app/data/notes.db /app/backups/notes_backup_$(date +%F_%H-%M-%S).db
echo "Backup created at /app/backups/notes_backup_$(date +%F_%H-%M-%S).db"

