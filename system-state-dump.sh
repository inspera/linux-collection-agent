#!/usr/bin/env bash


echo "System dump for $(whoami)@$(hostname) at $(date)"
echo

echo "Hardware:"
inxi -Fxz

echo
echo
echo "Packages:"
if [ -f "/etc/arch-release" ]; then
	pacman -Q 2>/dev/null
else
	apt list --installed 2>/dev/null
fi

echo
echo
echo "Applications:"
for app in /usr/share/applications/*.desktop; do app="${app##/*/}"; echo "${app::-8}"; done

echo
echo
echo "Services:"
systemctl --type=service --all
