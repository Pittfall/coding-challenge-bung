# Coding Challenge

A coding challenge presented by Bungalow which is to be completed in a few hours.

## Running CSV Import Script
python manage.py import_csv --path {path_of_csv_file}

## Comments/Assumptions

Best practice would be to gradually make code commits.  As it was a smaller
task, I just sort of got into it and completed it but I do understand the 
importance of small commits and how they help the entire team as well.

To restrict work to only a few hours I made some "cuts" so that I could
produce results:
- Database normalization was not done to keep it simple but even that is a 
  design choice more than a must.
- From a quick scan of the data, I noticed that the number and date fields are
  sometimes missing data so I allowed nulls and empties for those fields to
  test functionality and then left it there since there aren't specs on what 
  should and shouldn't be mandatory.
- Writing tests is an important part of a project but since I wanted to follow
  the instructions and limit my time spent, I did not write any.
- The generated docs need more work to be "production ready" but again,
  I did the minimum to be able to present some documentation in a timely
  fashion. ({url}/api/docs).
- Since the django command seems to be an internal task, I left out any error
  checking and left with the assumption that the person running it knows what
  they are doing but normally I'd check if the arugments needed were passed, I'd
  check if the file exists, check if the data is valid etc...
- I know that prices of things are typically handled by decimal numbers but since
  we are talking house prices, I thought whole numbers would be ok.
- Typically I left 255 characters for my char characters since I didn't really
  have specs as to what the maximum amount of characters should be.  However,
  I do understand that 255 might be a lot for something like a city.
- I assumned that the price field should have a number representation so that
  it can be formated as desired depending on the UI being presented.
- Part of the excercise was to be able to insert new records.  I assume this
  meant the post action in my viewset which is there, of course.

## Challenges

My biggest challenge for this project was the deserialization proccess.  To
reduce noise in my code, I wanted to rely on the framework as much as I could
in terms of handling my data.  My initial thoughts were around processing each
column one by one manually and doing what I needed to clean it up but that felt 
"hacky" so I investigated what the framework can do for me a little more.  
This sort of ties in to my strenghts too.  Even though Python and Django may be 
newer to me I think I have a decent sense as to when I am writing code that 
could be improved. I have a good sense as to what common problems are, when the 
framework "should" handle certain things and I typically know when I need to 
ask/look something up.