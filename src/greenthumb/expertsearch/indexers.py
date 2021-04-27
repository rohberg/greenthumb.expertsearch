from collective import dexteritytextindexer
from dexterity.membrane.content.member import IMember
from zope.component import adapts
from zope.interface import implementer

@implementer(dexteritytextindexer.IDynamicTextIndexExtender)
class MembraneSearchableTextExtender(object):
    adapts(IMember)    

    def __init__(self, context):
        self.context = context

    def __call__(self):
        """Extend the searchable text with a custom string"""
        return "{} {}".format(self.context.last_name, self.context.first_name)
