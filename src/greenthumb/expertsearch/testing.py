# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import greenthumb.expertsearch


class GreenthumbExpertsearchLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=greenthumb.expertsearch)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'greenthumb.expertsearch:default')


GREENTHUMB_EXPERTSEARCH_FIXTURE = GreenthumbExpertsearchLayer()


GREENTHUMB_EXPERTSEARCH_INTEGRATION_TESTING = IntegrationTesting(
    bases=(GREENTHUMB_EXPERTSEARCH_FIXTURE,),
    name='GreenthumbExpertsearchLayer:IntegrationTesting',
)


GREENTHUMB_EXPERTSEARCH_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(GREENTHUMB_EXPERTSEARCH_FIXTURE,),
    name='GreenthumbExpertsearchLayer:FunctionalTesting',
)


GREENTHUMB_EXPERTSEARCH_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        GREENTHUMB_EXPERTSEARCH_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='GreenthumbExpertsearchLayer:AcceptanceTesting',
)
