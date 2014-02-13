#!/usr/bin/env python
#-*- coding:utf-8 -*-

#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>
#
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

import logging
import xmlrpclib

class XMLRPCClient(object):
    """
    Python client to interact with GLPI webservices plugin
    """
    def __init__(self, baseurl="http://localhost/glpi"):
        self.baseurl = baseurl
        self.serviceurl = self.baseurl + '/plugins/webservices/xmlrpc.php'
        self.session = None
        self.server = xmlrpclib.ServerProxy(self.serviceurl)
        self.logger = logging.getLogger()

    def connect(self, login_name=None, login_password=None):
        if not None in [login_name, login_password]:
            params = {
                'login_name':login_name,
                'login_password':login_password,
            }
            response = self.server.glpi.doLogin(params)

            if 'session' in response:
                self.session = response['session']
            else:
                raise Exception("Login incorrect or server down")
        else:
            self.logger.warn("Connected anonymously, will only be able to use non-authenticated methods")
        return True

    def __getattr__(self, attr):
        def call(module='glpi', *args, **kwargs):
            params = {}
            if self.session:
                params['session'] = self.session

            params = dict(params.items() + kwargs.items())

            called_module = getattr(self.server, module)
            return getattr(called_module, attr)(params)

        call.__name__ = attr
        call.__doc__ = call(help=True)
        return call
