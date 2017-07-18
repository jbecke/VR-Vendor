# VR Vendor
Speak to virtual characters to make VR in-app purchases! This is the github page for my 2017 AWS Chatbot Competition <a href="https://devpost.com/software/vr-vendor">submission</a>. 

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

Here's how this project works: At "begin_play()" the user speaks into their microphone to the bot (it would be desirable to have an area trigger and this wouldn't be hard to implement). Because of the lack of threading support in UnrealEnginePython at the moment, the python script ("Lex.py") calls (via os.system) another python script ("talk.py") which sits in the voice_module directory of the python VM's execution path. For me this was in my win64 folder within Unreal Engine, but I suspect it will be different for you if you are on another OS or are using the embedded version of UE4Python. You will need to place voice_module/ at this execution path. This talk.py script inherantly runs in an external process because it is called from os.system. I was spawning another process via python but found this to be unneeded. Once UnrealEnginePython gets reliable threading support (which should be soon according to the author) this external script will be unnecessary. Or the code could be transfered into UE4's native C++ and the engine recompiled. I didn't want to get into all this for the Amazon Competition, so please forgive the mess. Next the talk.py records the user until there has been 6 chunks (chunk size 1024 bits) of audio below a loudness threshhold. I found this value experimentally. Then, the python scipt writes out to "demo.wav", closes it, and immediatly uses this file as the argument for a post_content to my Lex bot using the lex-runtime interface.
