# -*- coding: utf-8 -*-
from greenthumb.expertsearch.behaviors.expert import IExpertMarker
from greenthumb.expertsearch.testing import GREENTHUMB_EXPERTSEARCH_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class ExpertIntegrationTest(unittest.TestCase):

    layer = GREENTHUMB_EXPERTSEARCH_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_expert(self):
        behavior = getUtility(IBehavior, 'greenthumb.expertsearch.expert')
        self.assertEqual(
            behavior.marker,
            IExpertMarker,
        )
