# CriticalMassApplication
Requested materials for the Internship Application


//===========================
// WORK AND PROJECT EXAMPLES 
//=========================== 

1. NIGHT OF THE LIVING HOWLS (Unity Game)

Description/Context
- Instead of paying 60 dollars per person for the Global Game Jam, I organized a game jam of our 
own with my brother Armin (artist), and my friend Carlos(writer/designer) over the last 3 day weekend
(BC Family Day and actually my Birthday too! :D ).
- This is an isometric/2d game designed to have an arcade experience. You are a Vampire that roams
a creepy scottish castle pub that is dimly lit as werewolves spawn and attack you.
- The core game mechanic is that the werewolves can only be seen in light. So make sure to grab a torch!

My Role/Contributions
- As the main programmer of the team, I designed the code structure and implemented most of the functionality.
A non-exhaustive list of features I created:
    - Start/End screen with UI and buttons
    - An inheritance structure for all the interactables of the game by creating in IInteractable interface, and having
    enemies, torches, etc... all implement it.
    - Player/Enemy animations using blend-trees and state machines
    - Basic Wolf AI that tracks and follwos the player
    - Camera script that allows the camera to follow the player, while never exceeding the boundaries of the map (background).
    - UI interface to show player health, and have it decrease accordinly as you get damaged.

Additional Notes
- You can actually go play our game! I've included both a Windows Executable and a Mac dmg. I've also included the Unity project files.
- The game is a work in progress that we're very proud of! We actually intend to showcase an improved version with a scoring system
(and generally polished up) to the local "Full Indie" event this month in Vancouver!
k

2. COPYRIGHT TOOL

Description/Context
- This is a copyright python tool that takes a given directory, hunts for all cs files within, and tacks on a Copyright text at the
top of the file. You also have the option to submit changes to perforce!
- At my current job, my supervisor noted that we need to start copyrighting our project sripts (there are hundreds of them). So I decided
to make a python tool in my spare time.
- It started out as a simple program to run through command prompt/terminal, but I decided to make it user friendly by making a GUI!
This was a great experience for me as I had never used PyQT. I'm quite proud of it. Feel free to try it out!

My Role/Contributions
- I created this tool entirely by myself, so all the code/gui was done by me.
- I had to design a simple python script to first be able to recursively walk through a directory, open cs files, write, and close.
- Once I had this functionality (tested through CMD), I began the GUI.
- I used PyQT to create the GUI all by code (I didnt use the QT Designer at all!).
- I also later decided to implement some code to allow the changes to be commited to perforce changelists.

Additional Notes
- I've removed company-sensitive comments/code from the project and made a version which you can try out yourself!
- While I havent quite finished it, when I get some more time I'm extending the functionality by allowing the user to select
multiple filetypes they wish to copyright (.cs, .txt, cpp, .py etc...). Its as simple as passing in a list of these filetypes and having
to make some of my codes in to iterative for loops. I just havent finished it up yet.


3. ARDUINO ENVIRONMENT SENSITIVE / CAPTURE-THE-FLAG ROBOT

Description/Context
- One my recent facinations has been with robotics. I only recently (maybe a year and half?) started to play around with Arduinos.
It's really interesting to me because it really challenges me to flip my way of thinking as a programmer. With mechanics, and real-life physics coming into play, I love the challenge of trying to make code harmonize with machinery/design (in this case Arduinos, simple motors, and Lego structures).
- I got introduced to arduinos/lego robots in one of my classes. So after that class finished, I took my materials, scavenged some code, and starting working on some new and improved robots >:)

My Role/Contributions
- I've written a basic script in Arduino's IDE (C-esque). This includes functionalities for communicating with:
    - motor controllers
    - ultrasonic sensors
    - touch sensors
- I also completely redesigned the robot lego/motor layout.
- I soldered wires, and connected the aforementioned componenents.

Additional Notes
- I've attached one of my scripts that I've worked on since my project course. This script allows the robot to navigate a maze
and avoid walls by using it's ultrasonic sensor.
- I've also attached a picture of my favourite build :) (because its so clean and compact!).


//===========================
//       INSPIRATION
//===========================

1. LINK: http://www.codingwithunity.com/2016/09/sprite-depth-for-top-down-2d.html

- For the recent "Night of the Living Howls" game I worked on, I found an article/tutorial on 2d perspectives. The problem I was having
was that I was basing the game in 2d, but I wanted a tilted depth perspective (isometric) so that the player could be infront of a tree, but also walk behind it (so the tree renders in front of it). This article shows an ingenious, simple method to get around this by applying a dynamic rendering script so that objects higher up on the screen or rendered lower down (and so as the player moves, it's render layer changes as well!)

This was so cool to me because its such a simple solution (when compared to having a 3d project requiring actual z - axis motion). One of the reasons I'm so fascinated by programming is because of its creativity. I love that there are so many ways to accomplish a solution to a problem. This is a perfect example of one.

2. 








- Instead of paying 60 dollars per person for the Global Game Jam, I organized a game jam of our own over the last 3 day weekend
mMy Brother Armin (artist), and my friend Carlos(writer/designer).
- This is an isometric/2d game IAs the core prog


2.


3.




// INSPIRATION

1.

2.

3.


// FOCUS


1.

2.

3




//===========================
//      CODE CHALLENGE
//===========================
Link:
https://codepen.io/alimortazavi/live/VQyazp
