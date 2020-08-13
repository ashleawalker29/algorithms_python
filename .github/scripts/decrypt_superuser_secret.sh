#!/bin/sh

# --batch to prevent interactive command
# --yes to assume 'yes' for questions
gpg2 --quiet --batch --yes --decrypt --passphrase='$SUPERUSER_SECRET' \
--pinentry loopback --output $HOME/spreadsheet_manipulation/superuser_secret.json .github/scripts/superuser_secret.json.gpg
