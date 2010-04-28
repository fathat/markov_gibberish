#!/usr/bin/env python
import random


class Chain(object):
    def __init__(self, input, window_size):
        self.root = Link(None)
        self.window_size = window_size
        self.root.process(input, window_size)
        
    def generate(self, max, start_word=None):
        if not start_word:
            start_word = self.root.select_random_link().data
        return [x.data for x in
                self.root.generate(start_word, self.window_size, max)
                if x.data]
        

class Link(object):
    def __init__(self, data):
        self.data = data
        self.links = {}
        self.count = 0
    
    @property
    def times_seen(self):
        return self.count
    
    @property
    def times_links_seen(self):
        return sum((x.times_seen for x in self.links.values()))
    
    def seen(self):
        self.count += 1

    def process(self, input, window_size):
        current_window = []
        for x in input:
            if len(current_window) == window_size:
                del current_window[0]
            current_window.append(x)
            self.process_window(current_window)
    
    def process_window(self, window):
        link = self
        for x in window:
            link = link.process_word(x)
    
    def process_word(self, part):
        link = self.links.get(part)
        if not link:
            link = Link(part)
            self.links[part] = link
        link.seen()
        return link
    
    def select_random_link(self):
        universe = self.times_links_seen
        rnd = random.randint(1, universe+1)
        total = 0
        for child in self.links.values():
            total += child.times_seen
            if total >= rnd:
                return child
        return None
    
    def follow(self, w):
        return self.links.get(w)
    
    def follow_window(self, window):
        link = self
        for w in window:
            link = link.follow(w)
            if not link: return None
        return link
    
    def generate(self, start, window_size, max):
        rval = []
        window = [start]
        link = self.follow_window(window)
        
        while link != None and max != 0:
            next = link.select_random_link()
            if len(window) == window_size-1:
                del window[0]
            if next:
                rval.append(link)
                window.append(next.data)
            link = self.follow_window(window)
            max -= 1
        return rval
                
    def __repr__(self):
        return "<%s, %d>" % (self.data, self.count)


