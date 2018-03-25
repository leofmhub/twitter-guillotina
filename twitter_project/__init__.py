from guillotina import configure


app_settings = {
    # provide custom application settings here...
}


def includeme(root):
    """
    custom application initialization here
    """
    configure.scan('twitter_project.api')
    configure.scan('twitter_project.install')
    configure.scan('twitter_project.content')
