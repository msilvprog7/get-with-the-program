import pygame

class ClickHandler():
    children = []

    def click(self, event):
        return delegate(self.children, event)

def delegate(children, event):
    print event.pos
    
    for child in children:
        print "Trying", child
        br = get_bounding_rect_for_obj(child)
        print br

        did_collide = False
        try:
            did_collide = br.collidepoint(event.pos)
        except AttributeError as e:
            print "Cannot find the bounding box of", child
            continue

        if did_collide:
            print "Collided!"
            try:
                return child.click(event)
            except AttributeError as e:
                print "Unable to pass click event to child because it doesn't handle clicks."
                print child
                print event
                return
                

def get_bounding_rect_for_obj(child):
    try:
        return child.image.get_bounding_rect()
    except AttributeError as e:
        pass

    try:
        return child._editor_rect
    except AttributeError as e:
        pass

    try:
        return child.world.get_bounding_rect()
    except AttributeError as e:
        pass

    try:
        if len(child.sprites()) == 1:
            print "Get the first bounding box in the group"
            return child.sprites()[0].image.get_bounding_rect()
    except Exception as e:
        pass
