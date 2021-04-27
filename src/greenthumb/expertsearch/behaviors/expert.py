# -*- coding: utf-8 -*-

from greenthumb.expertsearch import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IExpertMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IExpert(model.Schema):
    """
    """

    competence = schema.TextLine(
        title=_(u'Competence'),
        required=True,
    )
    region = schema.TextLine(
        title=_(u'Region'),
        required=True
    )
    organisation = schema.TextLine(
        title=_(u'Organisation'),
        required=True,
    )


@implementer(IExpert)
@adapter(IExpertMarker)
class Expert(object):
    def __init__(self, context):
        self.context = context

    @property
    def competence(self):
        if safe_hasattr(self.context, 'competence'):
            return self.context.competence
        return None

    @competence.setter
    def competence(self, value):
        self.context.competence = value


    @property
    def region(self):
        if safe_hasattr(self.context, 'region'):
            return self.context.region
        return None

    @region.setter
    def region(self, value):
        self.context.region = value


    @property
    def organisation(self):
        if safe_hasattr(self.context, 'organisation'):
            return self.context.organisation
        return None

    @organisation.setter
    def organisation(self, value):
        self.context.organisation = value
