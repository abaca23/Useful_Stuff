#!/bin/sh
##Adelina Baca
##Finished July 10th
##general cleaning+update software cuz I cant be bothered to update, upgrade, adn autoremove multiple times a week. :P

sudo apt update
sudo apt upgrade -y
sudo apt autoremove -y

echo $(clear)'Updating, Upgrading, and Autoremoving is complete.'
echo 'It is' $(date +'%m/%d/%Y')
echo 'The time is' $(date +'%I:%M %p')
echo 'You are logged in as' $(whoami)
