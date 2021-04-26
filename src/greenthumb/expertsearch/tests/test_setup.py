# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from greenthumb.expertsearch.testing import (
    GREENTHUMB_EXPERTSEARCH_INTEGRATION_TESTING  # noqa: E501,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that greenthumb.expertsearch is properly installed."""

    layer = GREENTHUMB_EXPERTSEARCH_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if greenthumb.expertsearch is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'greenthumb.expertsearch'))

    def test_browserlayer(self):
        """Test that IGreenthumbExpertsearchLayer is registered."""
        from greenthumb.expertsearch.interfaces import (
            IGreenthumbExpertsearchLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IGreenthumbExpertsearchLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = GREENTHUMB_EXPERTSEARCH_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['greenthumb.expertsearch'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if greenthumb.expertsearch is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'greenthumb.expertsearch'))

    def test_browserlayer_removed(self):
        """Test that IGreenthumbExpertsearchLayer is removed."""
        from greenthumb.expertsearch.interfaces import \
            IGreenthumbExpertsearchLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IGreenthumbExpertsearchLayer,
            utils.registered_layers())
