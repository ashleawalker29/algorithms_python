#!/bin/sh

# Decrypt the file
mkdir $HOME/secrets

# --batch to prevent interactive command
# --yes to assume 'yes' for questions
gpg --quiet --batch --yes --decrypt --passphrase='$SUPERUSER_SECRET' \
--output $HOME/spreadsheet_manipulation/superuser_secret.json superuser_scret.json.gpg
