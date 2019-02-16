# Placements_webscrapper_notify
This python script scraps the notifications from the placements website and sends mail if the mail is new notifications

This Can be directly deployed on heroku for getting self notifications to your mail-id.

1. Provide the mail-id and password from which the mail has to be sent.
2. Provide the mail-id to which the mails have to be sent.
3. Provide the username and password of the http://aitplacements.com/wp-login.php website.

## How to Deploy on Heroku platform?

1. Create a heroku app in the heroku webiste.
2. Download the heroku CLI for ubuntu.
3. Type <b>$heroku login</b> in the terminal.
4. Go to the project folder using cd.
5. clone the git location for commiting ur app by command <b>$heroku git:clone -a appname</b>
6. <b>$git add .</b>
7. <b>$git commit -am "Inital commits"</b>
8. <b>$git push heroku master </b>
9. <b>$heroku ps:scale worker=1 </b>
10. <b>$heroku logs --tails <b> to see the logs of the running script.
  
