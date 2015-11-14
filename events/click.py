import pygame

class ClickHandler():
    children = []

    def click(self, event):
        return delegate(self.children, event)

def delegate(children, event):
    for child in children:
        br = get_bounding_rect_for_obj(child)

        did_collide = False
        try:
            did_collide = br.collidepoint(event.pos)
        except AttributeError as e:
            print "Unable to delegate click because we cannot find the bounding box of children."
            print event
            continue

        if did_collide:
            try:
                return child.click(event)
            except AttributeError as e:
                print "Unable to pass click event to child because it doesn't handle clicks."
                print child
                print event
                return

def get_bounding_rect_for_obj(child):
    if isinstance(child, pygame.sprite.Sprite):
        return child.image.get_bounding_rect()

    try:
        return child._editor_rect
    except AttributeError as e:
        pass

    try:
        return child.world.get_bounding_rect()
    except AttributeError as e:
        pass
