# Question 1.1
class Student:
    students = 0
    def __init__(self, name, staff):
        self.name = name
        self.understanding = 0
        Student.students += 1
        print("There are now", Student.students, "students")
        staff.add_student(self)

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class Professor:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student

    def assist(self, student):
        student.understanding += 1

def __main__():
    """
    >>> callahan = Professor("Callahan")
    >>> elle = Student("Elle", callahan)
    There are now 1 students
    >>> elle.visit_office_hours(callahan)
    Thanks, Callahan
    >>> elle.visit_office_hours(Professor("Paulette"))
    Thanks, Paulette
    >>> elle.understanding
    2
    >>> [name for name in callahan.students]
    ['Elle']
    >>> x = Student("Vivian", Professor("Stromwell")).name
    There are now 2 students
    >>> x
    'Vivian'
    >>> [name for name in callahan.students]
    ['Elle']
    """

# Question 1.2
class MinList:
    """A list that can only pop the smallest element."""
    def __init__(self):
        self.item = []
        # self.size = 0

    def append(self, item):
        """Appends an item to the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(2)
        >>> m.size
        2
        """
        self.item.append(item)

    def pop(self):
        """Removes and returns the smallest item from the MinList
        >>> m = MinList()
        >>> m.append(4)
        >>> m.append(1)
        >>> m.append(5)
        >>> m.pop()
        1
        >>> m.size
        2
        """
        smallest_item = min(self.item)
        self.item.remove(smallest_item)
        return smallest_item

    @property
    def size(self):
        return len(self.item)
    
# Question 1.3
class Email():
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """Each Server has an istance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client

class Client:
    """Every Client has instance attributes name (which is 
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and 
    inbox (a list of all emails the client has received).
    """
    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = None

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient cient.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)

# Question 2.1
class Pet():
    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Dog(Pet):
    def talk(self):
        print(self.name + ' says woof!')

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        Pet.__init__(self, name, owner)
        self.lives = lives

    def talk(self):
        """Print out a cat's greeting.

        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive' 
        becomes False. If this is called after lives has reached zero, print out 
        that the cat has no more lives to lose."""
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False
            print(self.name + ' has no more lives to lose.')

# Question 2.2
class NoisyCat(Cat):
    """A Cat that repeats things twice."""
    def __init__(self, name, owner, lives=9):
        Cat.__init__(self, name, owner, lives=9)

    def talk(self):
        """Talks twice as much as a regular cat.

        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        for _ in range(2):
            Cat.talk(self)

    def __repr__(self):
        """The interpreter-readable representation of a NoisyCay

        >>> muffin = NoisyCat('Muffin', 'Catherine')
        >>> repr(muffin)
        "NoisyCat('Muffin', 'Catherine')"
        >>> muffin
        NoisyCat('Muffin', 'Catherine')
        """
        return "NoisyCat('{}', '{}')".format(self.name, self.owner)

        






