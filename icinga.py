# -*- coding: utf-8 -*-
"""
Display Icinga2 service status informations

Configuration Parameters:
    - cache_timeout: how often the data should be updated
    - base_url: the base url to the icinga-web2 services list
    - disable_acknowledge: enable or disable counting of acknowledged service problems
    - user: username to authenticate against the icinga-web2 interface
    - password: password to authenticate against the icinga-web2 interface

@author Ben Oswald <ben.oswald@root-space.de>
@license MIT License <https://opensource.org/licenses/MIT>
"""
from time import time
import requests
from requests.auth import HTTPBasicAuth
import json


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 60
    base_url = ''
    disable_acknowledge = False
    url_parameters = "?service_state={service_state}&format=json"
    user = ''
    password = ''
    ca = True

    def unknown(self, i3s_output_list, i3s_config):
        format = 'Unknown: {unknown}'
        service_state = 3
        if self.disable_acknowledge:
            self.url_parameters = self.url_parameters + "&service_handled=0"
        unknown = requests.get(
            self.base_url + self.url_parameters.format(service_state=service_state),
            auth=(self.user, self.password), verify=self.ca)
        response = {
            'color': '#cc77ff',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(unknown=len(unknown.json()))
        }
        return response

    def critical(self, i3s_output_list, i3s_config):
        format = 'Critical: {critical}'
        service_state = 2
        if self.disable_acknowledge:
            self.url_parameters = self.url_parameters + "&service_handled=0"
        critical = requests.get(
            self.base_url + self.url_parameters.format(service_state=service_state),
            auth=(self.user, self.password), verify=self.ca)
        response = {
            'color': '#ff5566',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(critical=len(critical.json()))
        }
        return response

    def warning(self, i3s_output_list, i3s_config):
        format = 'Warning: {warning}'
        service_state = 1
        if self.disable_acknowledge:
            self.url_parameters = self.url_parameters + "&service_handled=0"
        warning = requests.get(
            self.base_url + self.url_parameters.format(service_state=service_state),
            auth=(self.user, self.password), verify=self.ca)
        response = {
            'color': '#ffaa44',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(warning=len(warning.json()))
        }
        return response

    def ok(self, i3s_output_list, i3s_config):
        format = 'OK: {ok}'
        service_state = 0
        if self.disable_acknowledge:
            self.url_parameters = self.url_parameters + "&service_handled=0"
        ok = requests.get(
            self.base_url + self.url_parameters.format(service_state=service_state),
            auth=(self.user, self.password), verify=self.ca)
        response = {
            'color': '#44bb77',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(ok=len(ok.json()))
        }
        return response


if __name__ == "__main__":
	pass
