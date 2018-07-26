# VR Vendor
<img src="https://raw.githubusercontent.com/jbecke/VR-Vendor/ae473fd5e0cdaabf7e5912e944139aea77212e9f/vr_vendor.jpg">
Speak to virtual characters to make VR in-app purchases! This is the github page for my 2017 AWS Chatbot Competition <a href="https://devpost.com/software/vr-vendor">submission</a>. This project integrates Lex with game engines Unreal Engine 4 and Amazon Lumberyard so that players can speak to in-game characters.

<h3>Why Lex?</h3>

Text-to-speech is rapidly improving but still doesn't sound like a human. The point of this project is allowing immersion while making payments, so I wanted to use pre-recorded human voice. Lex allows me to have powerful speech-understanding but still standardize outputs (as opposed to an end-to-end ANN model). For example, all inputs to the effect of "how are you?" could produce an output "good.wav" to play the sound file.

<h3> Setup Instructions</h3>

This project has several dependencies. I've only tested it on Windows. 


<ul>
<li>Unreal Engine 4.16 with <a href="https://github.com/20tab/UnrealEnginePython">Unreal Engine Python</a> installed</li>
<li>Python 3 (added to PATH)</li>
<li>An AWS account</li>
<li>AWS Boto3 library with credentials</li>
<li>A twitch.tv account</li>
<li>An oauth key from twitch.tv</li>
<li>An identical copy of my Amazon Lex bot</li>
<li>A powerful computer to run UE4</li>
</ul>

Here's how this project works: At "begin_play()" the user speaks into their microphone to the bot (it would be desirable to have an area trigger and this wouldn't be hard to implement). Because of the lack of threading support in UnrealEnginePython at the moment, the python script ("Lex.py") calls (via os.system) another python script ("talk.py") which sits in the voice_module directory of the python VM's execution path. For me this was in my win64 folder within Unreal Engine, but I suspect it will be different for you if you are on another OS or are using the embedded version of UE4Python. You will need to place voice_module/ at this execution path. This talk.py script inherantly runs in an external process because it is called from os.system. Once UnrealEnginePython gets reliable threading support (which should be soon according to the author) this external script will be unnecessary. Or the code could be transfered into UE4's native C++ and the engine recompiled. Next the talk.py records the user until there has been 6 chunks (chunk size 1024 bits) of audio below a loudness threshhold. Then, the python scipt writes out to "demo.wav", closes it, and immediatly uses this file as the argument for a post_content to my Lex bot using the lex-runtime interface.

<h3>Using Amazon Lumberyard</h3>

Lumberyard is in beta and lacks an audio input library. It doesn't seem to like having external processes spawned from its Lua scripting interface, as it freezes up and locks the mouse even after the game has ended. Thus, I have only implemented text-based support for Lumberyard. I.e. you type into a textbox at the bottom right of the screen to talk to the bot. To test this, download the Lumberyard directory and place the level inside the Starter Project (as it uses Starter Project assets). Play the game and walk forward a bit and the tirigger arena will fire, allowing you to chat with the character.

<img src="https://raw.githubusercontent.com/jbecke/VR-Vendor/master/media/lumberyard.png">

<h3>Future Direction</h3>

This is a quick hack solution. I estimate it would take a lot of effort for another person to get it all up and running on their computer. UE4Python Plugin is very buggy at the moment, so the next step is to transfer this to C++ and reate my own plugin. This could be impleented using the IVoiceCapture class provided by Epic Games. 
