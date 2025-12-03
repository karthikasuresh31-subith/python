#Create a Boolean variable has_account and assign it True.
has_account = True

#Create another Boolean variable email_verified and assign it False.
email_verified = False

#Use a logical operator to check if the user can log in. A user can log in only if they have an account and their email is verified. Store the result in can_login.
can_login = has_account and email_verified

#To validate an email address, check if it contains the @ symbol, which is required for a valid email.
email = "g@example.com"
is_email_valid = "@" in email

#The platform allows login only if the user’s age is greater than or equal to 18. Create a variable user_age and assign it 17. Use a comparison operator to check if the age is valid. Store the result in is_age_valid.
user_age = 17
is_age_valid = user_age >= 18

#Update the login logic to allow login only if has_account, email_verified, is_email_valid, and is_age_valid are all True. Store this final result in can_login_final
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

#Print the results of can_login, is_email_valid, is_age_valid, and can_login_final.
print("can_login :", can_login)
print("is_email_valid :", is_email_valid)
print("is_age_valid :", is_age_valid)
print("can_login_final :", can_login_final)

#Use an identity operator to confirm that has_account is True and print the result.
print("has_account :", has_account is True)
