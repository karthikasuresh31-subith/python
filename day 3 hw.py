#Declare two Boolean variables: is_logged_in = True and is_subscribed = False.
is_logged_in = True 
is_subscribed = False

#Initialize user_credits = 100, max_credits = 200, and min_credits = 50.
user_credits = 100
max_credits = 200
min_credits = 50

#Check if user_credits is within the valid range and not equal to min_credits. Store the result in credits_valid.
credits_valid = (user_credits >= min_credits and user_credits <= max_credits and user_credits != min_credits)

#Check if the user is eligible for bonus credits: the user is eligible if they are either subscribed or have credits greater than min_credits. Use the or and not operators. Store the result in bonus_eligible.
bonus_eligible = (is_subscribed or user_credits > min_credits)

#Modify user_credits using the following operators: += (add 50), -= (subtract 20), *= (multiply by 2), and %= (modulo 150). Store the final value in user_credits.
user_credits += 50
user_credits -= 20
user_credits *=2
user_credits %= 150

#Compute the square of the final user_credits and store it in power_result.
power_result = user_credits ** 2

#Use a logical operator to check if the user is both logged in and subscribed. Store the result in full_access.
full_access = is_logged_in and is_subscribed

#Use an identity operator to check if is_logged_in is exactly True. Store the result in is_true_login.
is_true_login = (is_logged_in is True)

#Demonstrate operator precedence with the expression: access_result = is_logged_in or is_subscribed and False.
access_result = is_logged_in or is_subscribed and False

#Print the following results: is_logged_in, is_subscribed, credits_valid, bonus_eligible, user_credits, power_result, full_access, is_true_login, and access_result
print("is_logged_in :",is_logged_in)
print("is_subscribed :",is_subscribed)
print("credits_valid :",credits_valid)
print("bonus_eligible :",bonus_eligible)
print("user_credits :",user_credits)
print("power_result :",power_result)
print("full_access :",full_access)
print("is_true_login :",is_true_login)
print("access_result :",access_result)