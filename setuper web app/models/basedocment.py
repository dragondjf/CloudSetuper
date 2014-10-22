#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mongokit import Document


class BaseDocment(Document):

    def loadFromDict(self, dictobj):
        for key in self.required_fields:
            print self.structure[key], dictobj[key]
            self[key] = self.structure[key](dictobj[key])
        for key in self.structure:
            if key not in self.required_fields and key in dictobj:
                self[key] = self.structure[key](dictobj[key])
        self.save()
        return self['_id']
