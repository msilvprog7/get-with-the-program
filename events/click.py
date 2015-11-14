import pygame

class ClickHandler():
    children = []

    def click(self, event):
        br = get_bounding_rect_for_obj(self)
        # print self, br
        event.pos = (event.pos[0] - br.x, event.pos[1] - br.y)
        return delegate(self.children, event)

def delegate(children, event):
    for child in children:
        # print "Trying", child
        br = get_bounding_rect_for_obj(child)

        did_collide = False
        try:
            did_collide = br.collidepoint(event.pos)
        except AttributeError as e:
            print "Cannot find the bounding box of", child
            continue

        if did_collide:
            try:
                return click_attempt(child, event)
            except AttributeError as e:
                print "Unable to pass click event to child because it doesn't handle clicks.", child
                print e
                return

def click_attempt(child, event):
    return child.click(event)

def get_bounding_rect_for_obj(child):
    try:
        return child.rect
    except AttributeError as e:
        pass
    
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
            return child.sprites()[0].rect
    except Exception as e:
        pass

    try:
        if len(child.sprites()) == 1:
            return child.sprites()[0].image.get_bounding_rect()
    except Exception as e:
        pass
