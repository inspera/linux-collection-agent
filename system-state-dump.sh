#!/usr/bin/bash


echo "System dump for $(whoami)@$(hostname) at $(date)"

echo "Hardware:"
inxi -Fxz

echo
echo
echo "Packages:"
apt list --installed 2>/dev/null

echo
echo
echo "Applications:"
for app in /usr/share/applications/*.desktop; do app="${app##/*/}"; echo "${app::-8}"; done
