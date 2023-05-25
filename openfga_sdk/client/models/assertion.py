# coding: utf-8
"""
   Python SDK for OpenFGA

   API version: 0.1
   Website: https://openfga.dev
   Documentation: https://openfga.dev/docs
   Support: https://discord.gg/8naAwJfWN6
   License: [Apache-2.0](https://github.com/openfga/python-sdk/blob/main/LICENSE)

   NOTE: This file was auto generated by OpenAPI Generator (https://openapi-generator.tech). DO NOT EDIT.
"""


class ClientAssertion():
    """
    ClientAssertion flattens the input necessary for an Assertion
    """

    def __init__(self, user: str, relation: str, object: str, expectation: bool):
        self._user = user
        self._relation = relation
        self._object = object
        self._expectation = expectation

    @property
    def user(self):
        """
        Return user
        """
        return self._user

    @property
    def relation(self):
        """
        Return relation
        """
        return self._relation

    @property
    def object(self):
        """
        Return object
        """
        return self._object

    @property
    def expectation(self):
        """
        Return expectation
        """
        return self._expectation
