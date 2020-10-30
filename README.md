# SI Gathering Challenge: 

# PleaseDress
PleaseDress is an application that will radically change your daily commuting experience to/from work. By utilizing Deep Learning and cloud technology together with open weather APIs "PleaseDress" will give you optimal advice for proper dressing both for walking, biking or using car.

The application runs in your browser and can be accessed from the following link:  
https://gathering-eris.app.playground.radix.equinor.com/

The main purposes are:
  - Safe commuting to/from work by using correct clothing for the weather and best method (car/walk/bike). Also advice for tires for car and bike.
    This is part of the 'I am safety' culture with the expectation "I understand and manage my risks".
  - Comfort during travelling
    This is very important for the mental health. ref #mentalhealth campaign. 
  - More employees to walk or bike to/from work
  - Recommendation for walking or biking possiblby helps the employees' physical health. Also part of the #mentalhealth campaign and support Equinors goal of lower the lower CO2
 emissions
  - Time efficiency
    Time saved ecpecially in the morning When getting the advice for communting and dressing right away when waking up.
  
 Current features:
 Display precipitation for selected office locations
- Rule based hypo/hyperthermia prevention algorithm
 
Planned features:
- Link to Calendars
  If many meeting the current day and the are bad weather the advice will be homeoffice
 - Link to 'Insight' information if the office is 'Green/yelow/red' due to Covid. 
 This will give instruction of home office and dressing in hoodies/sweatpants (also dependent on Calendar meetings)
- Collect user feedback of reccomendations
- Use deep learning to improve reccomendations
- Integrate with more weather APIs
- Reccomendations based on current location

Contributions, bug reports and feature requests are welcome! Create an issue or pull request in this repository.

### Running the project
The repository consists of a frontend and backend component. To run the whole project you can use docker-compose:

```
docker compose up
```

Each component can also be run individually with docker

Frontend:
```
docker build -t pleasedress-frontend ./frontend
docker run -p 8000:8000 pleasedress-frontend
```

Backend:
```
docker build -t pleasedress-backend ./backend
docker run -p 8001:80 pleasedress-backend
```
