class Movie:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration


class Theatre:
    def __init__(self, name, total_seats):
        self.name = name
        self.__ava_seats = total_seats 

    def book_seat(self, seats):
        if seats <= self.__ava_seats:
            self.__ava_seats -= seats
            return True
        return False

    def get_available_seats(self):
        return self.__ava_seats


class Customer:
    def __init__(self, name):
        self.name = name


class Ticket:
    def __init__(self, movie, theatre, seats):
        self.movie = movie
        self.theatre = theatre
        self.seats = seats
        self.price = 0

    def calculate_price(self):
        pass  # Polymorphism

    # Operator Overloading
    def __add__(self, other):
        return self.price + other.price

    @staticmethod
    def validate_seat_number(seats):
        return seats > 0


class Show2D(Ticket):
    def calculate_price(self):
        self.price = self.seats * 450
        return self.price


class Show3D(Ticket):
    def calculate_price(self):
        self.price = self.seats * 850
        return self.price


movie = Movie("KGF", "2h 30m")
theatre = Theatre("INOX", 47)
customer = Customer("Dip")

seats = int(input("ENter Number of Seats \n"))


if Ticket.validate_seat_number(seats):
    if theatre.book_seat(seats):
        ticket2d = Show2D(movie, theatre, seats)
        ticket3d = Show3D(movie, theatre, seats)

        print("---------------------------")
        print("Customer Name:", customer.name)
        print("Movie Name:", movie.name)
        print("---------------------------")
        print("Seats Available:", theatre.get_available_seats())
        print("---------------------------")
        print("2D Ticket Price:", ticket2d.calculate_price())
        print("3D Ticket Price:", ticket3d.calculate_price())

        total = ticket2d + ticket3d
        print("Total Amount:", total)
        print("---------------------------")
    else:
        print("Not enough seats available")
else:
    print("Invalid seat number")
