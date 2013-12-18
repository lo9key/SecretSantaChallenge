import random
santas = {}

class Person(object):
        def __init__(self,name,email,blacklist):
                self.name = name
                self.email = email
                # blacklist may contain multiple names seperated by spaces,
                # and should always include the santa's own name.
                if name not in blacklist:
                        self.blacklist = ' '.join([name,blacklist])
                else:
                        self.blacklist = blacklist
                self.giftee = None

        def display(self, name):
                return self.name, self.email, self.blacklist, self.giftee

def draw(name, giftees, redraw, swap = False):
        avail_santas = giftees[:]
        for canidate in avail_santas[:]:
                if canidate in santas[name].blacklist:
                        # canidate on blacklist, ineligible
                        avail_santas.remove(canidate)
                elif swap is True and name in santas[canidate].blacklist:
                        # canidate has name on blacklist, ineligible
                        avail_santas.remove(canidate)
        # all santas have been checked, now pick one.
        if len(avail_santas) > 0:
                # choose a random name from the avail_santas
                choice = random.choice(avail_santas)
                santas[name].giftee = choice
                if swap == False: # this is the first draw
                        giftees.remove(choice)
                else: # this is a redraw, choice redraws from remaining giftees
                        draw(choice,giftees,redraw)
        else: # no good choices left, name must redraw.
                redraw.append(name)
                choice = None
        return giftees

def shuffle(santas):
        # Set up variables for shuffling
        giftees = [x for x in santas]
        random.shuffle(giftees)
        redraw = [] # santas that could not draw
        # sort santas by the length of their blacklist
        # make a dictionary of name:length of blacklist
        picky = {n:len(santas[n].blacklist.split()) for n in santas}
        # easy_santas are sorted lowest blacklist length to highest
        easy_santas = sorted(picky.keys(), key=picky.get)
        # picky_santas are sorted highest blacklist length to lowest
        picky_santas = sorted(picky.keys(), key=picky.get, reverse=True)

        # for debugging
        # starting with the most picky santas, match santas to giftees
        for name in picky_santas:
                draw(name, giftees, redraw)
        # fix santas who need to redraw
        for name in redraw:
                # start with santas most likely to be able to trade
                draw(name, easy_santas, redraw, True)

        # display results
        print '*** Final Results ***'
        for s in santas:
                print santas[s].display(s)

def menu():
        print 'Welcome to the Secret Santa python app.'
        while True: # loop until they shuffle
                input = ''
                while len(input) < 2: # make sure they entered something
                        print 'Available commands are: ADD, DEL, DISPLAY, SHUFFLE, and HELP.'
                        print 'Example: >add ted ted@aol.com jane nancy sue'
                        # break input apart into a list
                        input = raw_input('> ').lower()

                if input.startswith('add'): # add
                        # prepare input for the function
                        # Split input into name, email, blacklist
                        input = input.split(None,3)[1:]
                        # assign variables even if input is < 3 pieces
                        # 3 vars = (~3-6 vars)[:3]
                        name, email, blacklist = (input + [None]*3)[:3]
                        # todo - This still needs work, potentially lets users have empty names
                        if not name:
                                name = raw_input("Please enter the Santa's name: ")
                        if not email:
                                email = raw_input("Please enter {}'s email: ".format(name))
                        if not blacklist:
                                print "Besides themselves, is there anyone {} should not draw?".format(name)
                                blacklist = raw_input("Seperate names by spaces, or leave blank: ")
                        # Capitalize names and blacklists
                        name = name.capitalize()
                        blacklist = blacklist.title()
                        # add to santas dict as name:object
                        santas[name] = Person(name,email,blacklist)

                elif input.startswith('del'): # delete
                        # todo - deleting needs work
                        print 'Deleting..'

                elif input.startswith('dis'): # display
                        # todo - Should be expanded
                        for s in santas:
                                print santas[s].display(s)

                elif input.startswith('shu'): # shuffle
                        print 'Shuffling..'
                        shuffle(santas)
                        break

                elif input.startswith('sam'): # sample data
                        data = [
                        ('Jo','j@','Jo Levi'),
                        ('Ted','t@','Ted Amy'),
                        ('Amy','a@','Amy'),
                        ('Bob','b@','Bob Amy')
                        ]
                        for name, email, blacklist in data:
                                santas[name] = Person(name,email,blacklist)

                else: # help
                        print 'Here are some tips on using this program:'
                        print ' 1 - To add names use the following syntax:'
                        print '   > add name email blacklist'
                        print '   > add ted ted@aol.com jane nancy sue'
                        print ' 2 - You can delete a santa using:'
                        print '   > delete ted'
                        print ' 3 - Or, shuffle the Santa list and assign everyone a giftee:'
                        print '   > shuffle'

if __name__ == '__main__':
        menu()
