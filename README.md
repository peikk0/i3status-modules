# i3status Modules
This repository contains my py3status modules.

## Icinga.py
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
You also have to define the module directory within the py3status call with the -i parameter, so it looks for example like:
```
py3status -c ~/.i3status.conf -i /pat/to/modules/folder/i3status-modules
```

A screenshot of the plugin output:
![](http://files.benoswald.de/Screenshot2016-01-12_13-31-49.png)

### Older icinga web interface versions
Currently only icinga-web2 is supported by this module (you realy want to upgrade to icinga2 and icinga-web2!).
If you want support for older icinga interfaces like icinga-classic and icinga-web you have to wait or change the hard coded
URL parameter strings.

### Dependencies
- Python 3.4 (due to Enums)
- requests

If you want to run it with python < 3.4 you have to remove the enum and
if you run it under python 2 you may need pyopenssl, ndg-httpsclient and py-asn1
for a working TLS verification with SNI.

----

## icinga_simple.py
This module is a more flexible version of the icinga.py module.
With this module for example you are able to check only one status type.
You are able to reorder the status output, define the output format and you are able to define your own colors.
But this has some costs, you have to define all the config stuff redundant at your i3status.conf.
Additionaly you have to add the two config parameters status and format.

format is simply a format string like this: `format = "CRITICAL: %d`

status is one of this four values:

 - OK = 0
 - WARNING = 1
 - CRITICAL = 2
 - UNKNOWN = 3
