"""

Calculating the negative acceleration of a vehicle with a known initial velocity and the distance it will cover.

References:
    1)Science | Physics Library | Unit 1 | Kinematic formulas and projectile motion | Lesson 4 (https://www.khanacademy.org/science/physics/one-dimensional-motion/kinematic-formulas/a/what-are-the-kinematic-formulas)

"""

initial_velocity = 20                                                                             # Initial velocity of the object (m/s)
final_velocity = 0                                                                                # Final velocity of the object (m/s) 

distance = 5                                                                                      #The range of distances for which we want to calculate acceleration (m)
                                                                                                 
def calculate_acceleration(initial_velocity, final_velocity, distance):                    
    acceleration = (final_velocity**2 - initial_velocity**2) / (2 * distance)                     #Calculate the acceleration using the formula [ref:1 eq:4] (v^2)=(v0^2)+(2a*Δx) (m/s^2)
    return acceleration



for distance in range (distance,95,5):                                                             # The range of distances for which we want to calculate acceleration (from 5 to 95, in increments of 5)  
    acceleration = calculate_acceleration(initial_velocity, final_velocity, distance)              # Calculate acceleration for the current distance
    formatted_acceleration = f"{acceleration:.4f}"                                                 # Format the acceleration to four decimal places                               
    print("Mesafe =" , distance , "\tNegative Acceleration =" , formatted_acceleration , "m/s^2" ) # Print the distance and the formatted acceleration
