#!/bin/sh
# Default acpi script that takes an entry for all actions

set $*

group=${1/\/*/}
action=${1/*\//}

case "$group" in
	button)
		case "$action" in
			#power)	/sbin/init 0
			#	;;
			*)
				logger "ACPI action $action is not defined"
				;;
		esac
		;;

	*)
		logger "ACPI group $group / action $action is not defined"
		;;
esac
