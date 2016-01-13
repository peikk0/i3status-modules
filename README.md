# i3status Modules
This repository contains my py3status modules.

## Icinga
This is a module showing a status overview for your services (Critical, Unknown, Warning and OK)

You have to configure it with the help of a config section in your i3status.conf.
```
icinga {
    disable_acknowledge = true
    base_url = "https://monitoring.example.com/icingaweb2/monitoring/list/services"
    user = "icingauser"
    password = "secretpassword"
	# If you use your own CA for the Icinga SSL Cert you can define it here to prevent errors
    ca = "/path/to/pki/ca.crt"
}
```
A screenshot of the plugin output:
![](http://files.benoswald.de/Screenshot2016-01-12_13-31-49.png)

### Older icinga web interface versions
Currently only icinga-web2 is supported by this module (you realy want to upgrade to icinga2 and icinga-web2!).
If you want support for older icinga interfaces like icinga-classic and icinga-web you have to wait or change the hard coded
URL parameter strings.
