

def bag_contents(request):
    """ Ensures that the bag contents are available when rendering every page """
    
    context = {
        'bag_contents': bag_contents(request),
    }
    
    return context