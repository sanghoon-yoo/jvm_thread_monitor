#!/usr/bin/env python3
# -*-Encoding:UTF-8 -*- #
# -*-coding:utf-8 -*-


class JvmException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class MailException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
