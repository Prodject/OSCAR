#This file contains the defaults for various config files that Oscar uses.
#All are generated using JSON, which was chosen as a convenient half-way point between English readable text and code.
#   - Responses
#       - The responses file is responsible for Oscar's responses to various inputs.
#   - Inputs
#       - The inputs file is in charge of mapping inputs to Oscar's various functions.
#       - While it is a bit more complicated than the response system, the input system has a format that is easy to follow, and is described above its code below.

#0: Daytime greetings
#1: Nighttime greetings
#2: Response if search query blank
#3: Response if can't give summary for search query
#4: Response to ask user if they'd like to see the search result source
#5: Response for the time
#6: Response to say "You're welcome" to the user.
#7: Response to say that OSCAR can't open the URL in their browser.
#8: Response to confirm scheduled time
#9: Response to say that the scheduled task has been cancelled.
#10: Response to ask user if it was a yes or a no -- unclear.
#11: Response to ask user to rephrase their scheduled task
#12: Response to tell the user that the shutdown has been scheduled.
#13: Response to tell the user that the shutdown has been cancelled.
#14: Response to decide which option in the should method should be used.
#15: Response to say goodbye to the user before closing
#16: Response to ambiguous request
#17: Response if the user should do something
#18: Response if the user shouldn't do something
#19: Response to tell user that Oscar won't open a link in their browser
#20: Response to tell the user that Oscar won't open a link in their browser (No summary)
#21: Response to tell the user that their command has been scheduled.
#22: Response to ask the user to enter the command to be scheduled.
#23: Response to tell user that Oscar is opening a link in their browser
#24: Response to ask the user for their name
#25: Response to ask the user if they prefer 24-hour or 12-hour clocks
#26: Response to tell the user that they've selected a 24-hour clock
#27: Response to tell the user that they've selected a 12-hour clock
responses_array = [
    #0: Daytime greetings
    [
        "Hey there, <user>. How can I help you today?",
        "Nice to see you again, <user>. What can I do for you?",
        "Oscar here. I'm assuming that you're <user>, what can I help you with today?",
        "What's new, pussyca- err, I mean, <user>."
    ],
    #1: Nighttime greetings
    [
        "Nice to see you again, <user>. What can I do for you tonight?",
        "Back so quickly, <user>? Let's hear it.",
        "Burning the midnight oil again? What can I help you with?",
        "What's new, pussyca- err, I mean, <user>."
    ],
    #2: Response if search query blank
    [
        "It's hard to look up something that doesn't exist.",
        "Look man, I'm just a computer program - I can't answer a question if you don't ask it.",
        "Garbage in, garbage out."
    ],
    #3: Response if can't give summary for search query
    [
        "I'm having a bit of trouble making a summary on that. Care to have a look yourself?\n",
        "This is a bit too complicated for me to understand, maybe you'd like to see it?\n",
        "Maybe it's better that you look at this yourself. Want to?\n",
        "I can't find a summary for you, sorry, but I can open it in your browser if you'd like.\n"
    ],
    #4: Response to ask user if they'd like to see the search result source.
    [
        "That's an answer and a half if I dare say. Tell me if you want to read more on your own.\n",
        "That's all I've got. Want to see more for yourself?\n",
        "Want my sources?\n",
        "If you think that was too abstract of an abstract, I can open it for you so you can see yourself.\n"
    ],
	#5: Response for the time
    [
        "It's currently <time>.",
        "Right now? It's <time>.",
        "Do I look like a clock to you? Don't answer that. It's <time>.",
        "It's <time>, and don't ask for me to make an analog clock.",
        "Here? It's <time>. In china? I have no idea. Unless we're in china. Actually, I have no idea where we're at."
    ],
	#6: Response to say "You're welcome" to the user.
	[
		"You're welcome! I love to help.",
		"Of course. It's my job, after all.",
		"I'm programmed to help - I'm glad that I'm doing it well.",
		"Helpful? Me? Impossible.",
		"You're welcome! Although, if you really want to thank me, you can contribute to the github repos."
	],
	#7: Response to say that OSCAR can't open the URL in their browser.
	[
		"Weird, I can't open your browser. Here's the URL: <url>\n",
		"Huh, that's strange. I can't open your browser. Have a URL: <url>\n",
		"Well, this is awkward. Normally I'd open your browser now, but I can't for some reason or another. Enjoy your URL: <url>\n",
		"A URL a day keeps the doctor away, especially when your assistant isn't able to open your browser. URL: <url>\n",
		"You seem independent, have a URL. I can't open it, anyways. URL: <url>\n"
	],
	#8: Response to confirm scheduled time
	[
		"Alrighty then. I'll do that for you in <time_string>, yes?\n",
		"Just to clarify, you want that done in <time_string>?\n",
		"In <time_string>? Sure, my schedule's clear. That is the time, correct?\n",
		"I'd love to! I'll mark you down for <time_string> from now, then?\n",
		"Yeah, I can do that for you. You said <time_string> didn't you?\n"
	],
	#9: Response to say that the scheduled task has been cancelled.
	[
		"Task cancelled.",
		"Okay. I'll mark that with a red X. Very large, very red, just for you.",
		"Operation aborted.",
		"You're really decisive, aren't you? Okay, okay, cancelling it...",
		"I'll forget you even asked."
	],
	#10: Response to ask user if it was a yes or a no -- unclear.
	[
		"Was that a yes or a no?\n",
		"I'm sorry, I didn't quite get that - is that a yes or an no?\n",
		"Imagine that I'm a slightly handsomer magic eight ball. Yes, or no?\n",
		"You'll have to excuse me, I'm not quite sure what you mean. Would you like me to schedule it, or cancel it?\n",
		"I may be digital, but I'm not omnipotent. Would you mind rephrasing your response?\n"
	],
	#11: Response to ask user to rephrase their scheduled task
	[
		"Sometimes the English language eludes me. This is one of those moments. Can you rephrase that?",
		"Can you rephrase that for me?",
		"I'm sorry, but I have no idea what you want me to do right now. Can you say that again?",
		"I didn't quite get that. English is my second language, after binary, of course.",
		"Would you rephrase that, please? I'm afraid I don't understand."
	],
	#12: Response to tell the user that the shutdown has been scheduled.
	[
		"Powerdown imminent. Well, not imminent, really, but it's scheduled.",
		"I'll perform the shutdown when you asked.",
		"Shutdown scheduled.",
		"I'll turn your PC off at the aforementioned time.",
		"You're a busy person, so I'll make sure to shut it down for you when you asked."
	],
	#13: Response to tell the user that the shutdown has been cancelled.
	[
		"Shutdown cancelled.",
		"Powerdown aborted.",
		"Changed your mind? I'll take it off the to-do list.",
		"Sounds like a pla - oh, changed your mind already? I'll cancel that, then.",
		"Okay, I'll forget that you ever asked me."
	],
	#14: Response to decide which option in the should method should be used.
	[
		"Clearly, <option> is the superior choice.",
        "I would go with <option>.",
        "You know what? Today, I'm feeling like <option>.",
        "You'd have to be a fool to not go with <option>.",
        "In situations like this, you should ask yourself: what would OSCAR do? Obviously, he would go with <option>.",
        "What kind of a question is that? Of course it's <option>!",
		"Normally, I wouldn't do it, but since you asked nicely, I'd go with <option>."
	],
    #15: Response to say goodbye to the user before closing
    [
        "Have a lovely time.",
        "Leaving so soon? I was just getting warmed up.",
        "Alrighty then, I'll see you around.",
        "Until next time.",
        "You'll be back, we both know it."
    ],
    #16: Response to ambiguous request
    [
        "I'm sorry, I have no idea what that means.",
        "Sometimes the English language eludes me. This is one of those moments. Can you rephrase that?",
		"Can you rephrase that for me?",
		"I'm sorry, but I have no idea what you want me to do right now. Can you say that again?",
		"I didn't quite get that. English is my second language, after binary, of course.",
		"Would you rephrase that, please? I'm afraid I don't understand."
    ],
    #17: Response if the user should do something
    [
        "That's a great idea! Do it.",
        "I don't see why not.",
        "What could go wrong?",
        "Yeah, sure, go for it.",
        "I wouldn't be against it."
    ],
    #18: Response if the user shouldn't do something
    [
        "That doesn't sound like a good idea to me.",
        "Are you sure? I'm not sure it's such a good idea.",
        "Personally, I wouldn't, but it's not my choice.",
        "That sounds dreadful, don't do it.",
        "Would you be angry if I said no? I'm saying no."
    ],
    #19: Response to tell user that Oscar won't open a link in their browser (Summary)
    [
        "My summary was good enough? Excellent!",
        "That's okay, I'll just read it alone.",
        "Alrighty then. I'll keep the link to myself.",
        "You're a busy person. If a summary works, it works. If it doesn't, the link's still there.",
        "I'm glad that I was able to summarize it well for you."
    ],
    #20: Response to tell the user that Oscar won't open a link in their browser (No summary)
    [
        "I won't open it in your browser, then.",
        "If you change your mind, just ask again.",
        "The link's not going anywhere, in case you change your mind.",
        "That's fine. I'll leave it closed, in that case.",
        "Sounds good to me. If you change your mind, just ask again."
    ],
    #21: Response to tell the user that their command has been scheduled.
    [
        "Command scheduled.",
        "I'll do that.",
        "I'll take care of it for you when the time arrives, don't worry.",
        "I can do that.",
        "Okay, I'll do that for you."
    ],
    #22: Reponse to ask the user to enter the command to be scheduled.
    [
        "Okay. What do you want me to do at that time, exactly?",
        "Well, I've got the time down, but I'm not exactly sure of what you want me to do. Can you clarify?",
        "My schedule's clear for that time. What would you like me to do then?",
        "I don't have any plans for that time. What do you need me to do?",
        "Sure, that time works for me. What's your command?"
    ],
    #23: Response to tell user that Oscar is opening a link in their browser
    [
        "Let's open that in your browser, then.",
        "Opening link now...",
        "I'll open that link for you quickly.",
        "Your browser is asking for your attention - I believe it's the link you asked for.",
        "The page is opened in your browser, whenever you're ready for it."
    ],
    #24: Response to ask the user for their name
    [
        "What do you like to be called?\n",
        "What's your name, stranger?\n",
        "I'm Oscar, lovely to meet you. You would be..?\n",
        "A fresh face! What do I call you?\n",
        "I'm always terrible at introductions. Let's start with names - I'm Oscar, and you are?\n"
    ],
    #25: Response to ask the user if they prefer 24-hour or 12-hour clocks
    [
        "Next question: Your clock type. 24-hour or 12-hour?\n",
        "What type of clock do you prefer: 12-hour or 24-hour?\n"
        "<user>. Got it. So what kind of clock do you like, <user>? 24-hour or 12-hour?\n",
        "It's nice to meet you, <user>. Do you prefer the 24-hour or 12-hour clock?\n",
        "Okay <user>, do you prefer your times to be in 24-hour or 12-hour format?\n"
    ],
    #26: Response to tell the user that they've selected a 24-hour clock
    [
        "24-hour, huh? Finally, someone sensible.",
        "At last, someone rational. 24-hour clock it is.",
        "I'll serve your times in a 24-hour format, then.",
        "24-hour? sounds good to me.",
        "I'm glad you chose 24-hour. I don't think I'd see you in the same light if you had said 12."
    ],
    #27: Response to tell the user that they've selected a 12-hour clock
    [
        "12-hour? Weird, but okay.",
        "12-hour it is.",
        "Strange choice, but it's yours. 12-hour clock, then.",
        "Alright, I'll give you the time in the 12-hour format whenever you ask.",
        "12-hour? Aww. Come to the dark side - we have cookies, and twice the hours on our clock."
    ]
]

#This array is a bit complicated. The layers are described below
#The first layer consists of each function. Take for example, the search function
#The second layer is made up of arrays of the keywords or antikeywords. 0 = keywords, 1 = anti-words.
#The third and final layer is where the keywords/anti-words are stored.

#0: Time/date command
#1: Search command
#2: Should command
#3: Launch program command
#4: Thank you command
#5: Schedule shutdown command
#6: Schedule command command
#7: Close command
#8: A response that means no
#9: A response that means yes
#10: A response that means the user wants to walk through settings configuration.
#11: A response that means the user wants to use the default settings.
#12: A response that means the user prefers the 24-hour clock
#13: A response that means the user prefers the 12-hour clock
#14: Introductions to the user's name
inputs_array = [
    #0: Time/date command
    [
        [
            "\\btime\\b",
            "\\bday\\b",
            "\\bdate\\b"
        ],
        [
            "\\blook up\\b",
            "\\bsearch\\b",
            "\\blooking up\\b",
            "\\bsearching up\\b",
            "\\btell me about",
            "\\bwho is\\b",
            "\\bwho's\\b",
            "\\bdefine\\b",
            "\\bwhat are\\b",
            "\\bwhat was\\b",
            "\\bwhat were\\b",
            "\\bwho was\\b",
            "\\bwho were\\b",
        ]
    ],
    #1: Search command
    [
        [
            "\\bsearch\\b",
            "\\blook up\\b",
            "\\blooking up\\b",
            "\\bsearching up\\b",
            "\\btell me\\b",
            "\\btell me the\\b",
            "\\btell me about\\b",
            "\\bwhat is\\b",
            "\\bwhat's\\b",
            "\\bwhats\\b",
            "\\bwho is\\b",
            "\\bwho's\\b",
            "\\bdefine\\b",
            "\\bwhat are\\b",
            "\\bwhat was\\b",
            "\\bwhat were\\b",
            "\\bwho was\\b",
            "\\bwho were\\b"
        ],
        [

        ]
    ],
    #2: Should command
    [
        [
            "\\bshould\\b"
        ],
        [

        ]
    ],
    #3: Launch program command
    [
        [
            "\\blaunch\\b",
            "\\bstart\\b",
            "\\bopen\\b"
        ],
        [

        ]
    ],
    #4: Thank you command
    [
        [
            "\\bthanks\\b",
            "\\bthank you\\b",
            "\\bappreciate\\b",
            "\\bgrateful\\b",
            "\\bglad\\b",
            "\\bty\\b"
        ],
        [

        ]
    ],
    #5: Schedule shutdown command
    [
        [
            "\\bshut down\\b",
            "\\bshutdown\\b",
            "\\bpower off\\b",
            "\\bpoweroff\\b",
            "\\bpower down\\b",
            "\\bpowerdown\\b",
            "\\bturn off\\b"
        ],
        [

        ]
    ],
    #6: Schedule command command
    [
        [
            "\\bschedule\\b",
            "\\bseco?n?d?s?\\b",
            "\\bminu?t?e?s?\\b",
            "\\bhour\\b",
            "\\bday\\b"
        ],
        [

        ]
    ],
    #7: Close command
    [
        [
            "\\bexit\\b",
            "\\bfuck off\\b",
            "\\b:q\\b",
            "\\bquit\\b",
            "\\bclose\\b",
            "\\bbye\\b",
            "\\btalk to you later\\b",
            "\\blater\\b",
            "\\bsee you later\\b",
            "\\bcya\\b",
            "\\bsee you\\b"
        ],
        [
            "\\bdon't\\b",
            "\\bdo not\\b",
            "\\bno\\b",
            "\\bnevermind\\b"
        ]
    ],
    #8: A response that means no
    [
        [
            "\\bno\\b",
            "\\bnah\\b",
            "\\bnevermind\\b",
            "\\bnope\\b",
            "\\bforget about it\\b",
            "\\bforget it\\b",
            "\\bchanged my mind\\b",
            "\\bnegative\\b",
            "\\bnegatory \\b",
            "\\bcancel\\b"
        ],
        [

        ]
    ],
    #9: A response that means yes
    [
        [
            "\\byes\\b",
            "\\bof course\\b",
            "\\bplease\\b",
            "\\bnaturally\\b",
            "\\blove\\b",
            "\\byeah\\b",
            "\\byep\\b",
            "\\byea\\b",
            "\\bi do\\b",
            "\\bsure\\b",
            "\\balright\\b",
            "\\bokay\\b",
            "\\bsummary\\b",
            "\\bok\\b"
        ],
        [
            "\\bno\\b",
            "\\bnot\\b",
            "\\bdon't\\b",
            "\\bdo not\\b",
            "\\bnevermind\\b"
        ]
    ],
    #10: A response that means the user wants to walk through settings configuration.
    [
        [
            "\\bhelp\\b",
            "\\bhelpful\\b",
            "\\byes\\b",
            "\\bof course\\b",
            "\\bplease\\b",
            "\\bnaturally\\b",
            "\\blove\\b",
            "\\byeah\\b",
            "\\byep\\b",
            "\\byea\\b",
            "\\bi do\\b",
            "\\bsure\\b",
            "\\balright\\b",
            "\\bokay\\b",
            "\\bok\\b",
            "\\bwalkthrough\\b",
            "\\bwalk me through\\b",
            "\\bwalk through\\b"
        ],
        [
            "\\bno\\b",
            "\\bnot\\b",
            "\\bdon't\\b",
            "\\bdo not\\b"
        ]
    ],
    #11: A response that means the user wants to use the default settings.
    [
        [
            "\\bdefaults?\\b",
            "\\bthanks anyways\\b",
            "\\bno thanks\\b"
        ],
        [

        ]
    ],
    #12: A response that means the user prefers the 24-hour clock
    [
        [
            "\\b24-hour\\b",
            "\\b24 hour\\b",
            "\\b24hour\\b",
            "\\b24\\b",
            "\\btwenty four\\b"
        ],
        [

        ],
    ],
    #13: A response that means the user prefers the 12-hour clock
    [
        [
            "\\b12-hour\\b",
            "\\b12 hour\\b",
            "\\b12hour\\b",
            "\\b12\\b",
            "\\btwelve\\b"
        ],
        [

        ]
    ],
    #14: Introductions to the user's name
    [
        [
            "\\byou can call me\\b",
            "\\bmy name is\\b",
            "\\bsome people call me\\b",
            "\\bsome call me\\b",
            "\\bthe name's\\b",
            "\\bthe name is\\b",
            "\\bcall me\\b",
            "\\bi go by\\b"
        ],
        [

        ]
    ]
]
#The settings array is responsible for managing the user's various settings and preferences.
#0: The name that the user wishes to be called
#1: 24-hour or 12-hour clock. 0 = 24-hour, 1 = twelve-hour
settings_array = [
    #0: The name that the user wishes to be called
    "nameless",
    #1: 24-hour or 12-hour clock. 0 = 24-hour, 1 = twelve-hour
    1
]
