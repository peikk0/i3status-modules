# -*- coding: utf-8 -*-


from time import time
import requests
from requests.auth import HTTPBasicAuth
import json


class Py3status:
    """
    """
    # available configuration parameters
    cache_timeout = 60
    format = 'Unknown: {unknown} | Critical: {critical} | Warning: {warning} | OK: {ok}'
    cred = ('user', 'password')

    def unknown(self, i3s_output_list, i3s_config):
        format = 'Unknown: {unknown}'
        unknown = requests.get(
            "https://monitoring.benoswald.de/icingaweb2/monitoring/list/services?service_state=3&format=json",
            auth=self.cred, verify="/home/nazco/pki/ca.crt")
        response = {
            'color': '#cc77ff',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(unknown=len(unknown.json()))
        }
        return response

    def critical(self, i3s_output_list, i3s_config):
        format = 'Critical: {critical}'
        critical = requests.get(
            "https://monitoring.benoswald.de/icingaweb2/monitoring/list/services?service_state=2&format=json",
            auth=self.cred, verify="/home/nazco/pki/ca.crt")
        response = {
            'color': '#ff5566',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(critical=len(critical.json()))
        }
        return response

    def warning(self, i3s_output_list, i3s_config):
        format = 'Warning: {warning}'
        warning = requests.get(
            "https://monitoring.benoswald.de/icingaweb2/monitoring/list/services?service_state=1&format=json",
            auth=self.cred, verify="/home/nazco/pki/ca.crt")
        response = {
            'color': '#ffaa44',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(warning=len(warning.json()))
        }
        return response

    def ok(self, i3s_output_list, i3s_config):
        format = 'OK: {ok}'
        ok = requests.get(
            "https://monitoring.benoswald.de/icingaweb2/monitoring/list/services?service_state=0&format=json",
            auth=self.cred, verify="/home/nazco/pki/ca.crt")
        response = {
            'color': '#44bb77',
            'cached_until': time() + self.cache_timeout,
            'full_text': format.format(ok=len(ok.json()))
        }
        return response


if __name__ == "__main__":
    x = Py3status()
    config = {
        'color_bad': '#FF0000',
        'color_degraded': '#FFFF00',
        'color_good': '#00FF00'
    }
    print(x.unknown("bar", "baz"))
