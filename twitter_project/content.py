from guillotina import configure
from guillotina import schema
from guillotina import Interface
from guillotina import interfaces
from guillotina import content


class ITwitterData(interfaces.IItem):
    text = schema.Text()


@configure.contenttype(
    type_name="TwitterData",
    schema=ITwitterData)
class TwitterData(content.Item):
    """
    Our ToDo type
    """