## ML-Model-Flask-Deployment
This project deploys a bike price predictor using 1-month of collected data from Police Auctions Canada to Heroku

### Prerequisites
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has three main parts :
1. app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the precited value based on our model and returns it.
2. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
3. templates - This folder contains the HTML template to allow user to enter employee detail and displays the predicted bike price.

Test out the api here:
https://bike-price-predictor.herokuapp.com/


-- Test add to readme
