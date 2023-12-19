## Calculate the user holiday cost including the plane cost, hotel cost, car rental cost.
## user input for city_flight,number_of_night and rental_days.
c = "coimbatore"
b = "Bangalore"
d = "delhi"
city_flight = input( "Enter any one city as (\"b\",\"c\",\"d\": ")
number_of_nights = int(input("Enter the number of nights in hotel:"))
rental_days = int(input("Enter number of days rental for car :"))
## Define the function for hotel_cost,plane_cost,car_rental,holiday_cost
## first function is hotel_cost and arguments as number_of_nights
def hotel_cost(number_of_nights):
    return(220 * (number_of_nights))
## Second function is plane_cost and argument as city_flight
## using if elif statement to select the city
def plane_cost(city_flight):
    if city_flight == "c":
        return 1000
    elif city_flight == "b":
        return 900
    elif city_flight == "d":
        return 800
    else:
        return 0
## Third function is car_rental and argument as rental_days
def car_rental(rental_days):
    return(60 * (rental_days))
## Fourth function is holiday_cost and arguments are hotel_cost,plane_cost,car_rental
def holiday_cost(hotel_cost,plane_cost,car_rental):
    return(hotel_cost(number_of_nights) + plane_cost(city_flight) + car_rental(rental_days))
print("Holiday cost {} for the city {} in the hotel {} and the car rental {} ".format(holiday_cost(hotel_cost,plane_cost,car_rental),plane_cost(city_flight),hotel_cost(number_of_nights),car_rental(rental_days)))

