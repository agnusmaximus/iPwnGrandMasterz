from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

def mouse_event(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(None, type, (posx,posy), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mouse_move(posx,posy):
        mouse_event(kCGEventMouseMoved, posx, posy);

def mouse_click(posx,posy):
        mouse_event(kCGEventMouseMoved, posx,posy);
        mouse_event(kCGEventLeftMouseDown, posx, posy);
        mouse_event(kCGEventLeftMouseUp, posx, posy);
