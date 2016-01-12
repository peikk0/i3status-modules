# i3status Modules
This repository contains my own py3status plugins.

## Icinga
This is a plugin showing a status overview for my services (Critical, Unknown, Warning and OK)

You have to configure it with the help of a config section in your i3status.conf.
```
icinga {
    disable_acknowledge = true
    base_url = "https://monitoring.example.com/icingaweb2/monitoring/list/services"
    user = "icingauser"
    password = "secretpassword"
	# If you use your own CA for the Icinga SSL Cert you can define it here to prevent errors
    ca = "/home/nazco/pki/ca.crt"
}
```
A screenshot of the plugin output:
![](http://files.benoswald.de/Screenshot2016-01-12_13-31-49.png)