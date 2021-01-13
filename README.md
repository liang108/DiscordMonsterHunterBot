This is a Discord bot to be used to look up information on monsters in the game Monster Hunter World. For reference,
The Handler is the main character's partner who helps organize their missions. She also has a huge appetite.

The bot scrapes HTML from the website:

https://monsterhunter.fandom.com/wiki

and returns relevant information. 

Currently, there are four commands that send information to the Discord channel:
(Replace `<monster-name>` with desired monster)

* `!weak <monster-name>`: Returns the elements the monster is weak to.
* `!type <monster-name>`: Returns the monster's elemental types.
* `!ailments <monster-name>`: Returns the ailments that the monster may inflict on the player.
* `!all <monster-name>`: Returns all of the above.

If the monster's name contains a space, it must be replaced with an underscore. The bot also tends to work better with capitalized names.

Here is a demo of the `!weak` command:

![alt text](https://github.com/liang108/Monster-Hunter-Bot/blob/main/Screenshots/bot2.PNG)

which correctly scraped the appropriate HTML from the column on the right from the wiki (the "weakest to" section).

![alt text](https://github.com/liang108/Monster-Hunter-Bot/blob/main/Screenshots/bot3.PNG)
