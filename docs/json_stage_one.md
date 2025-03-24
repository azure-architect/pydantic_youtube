{
  "video_id": "AgN3RHSZGwI",
  "transcript": [
    {
      "text": "complex problems always yield better",
      "start": 0.16,
      "duration": 4.48
    },
    {
      "text": "results when tackled by a team of people",
      "start": 2.28,
      "duration": 4.44
    },
    {
      "text": "with different specializations and with",
      "start": 4.64,
      "duration": 5.52
    },
    {
      "text": "AI agents it works exactly the same way",
      "start": 6.72,
      "duration": 6.2
    },
    {
      "text": "individual expertise combined creates",
      "start": 10.16,
      "duration": 5.04
    },
    {
      "text": "exponentially better Solutions because",
      "start": 12.92,
      "duration": 4.68
    },
    {
      "text": "just like with humans AI agents work",
      "start": 15.2,
      "duration": 4.72
    },
    {
      "text": "better the more narrow their role and",
      "start": 17.6,
      "duration": 5.64
    },
    {
      "text": "goals are it is all about Focus I know",
      "start": 19.92,
      "duration": 4.8
    },
    {
      "text": "you have seen it before where you're",
      "start": 23.24,
      "duration": 3.16
    },
    {
      "text": "building your AI agent and it works",
      "start": 24.72,
      "duration": 3.28
    },
    {
      "text": "really well at first but then as you",
      "start": 26.4,
      "duration": 3.32
    },
    {
      "text": "continue to add more instructions and",
      "start": 28.0,
      "duration": 4.36
    },
    {
      "text": "tools it starts to hallucinate even with",
      "start": 29.72,
      "duration": 4.24
    },
    {
      "text": "the things that it was doing well with",
      "start": 32.36,
      "duration": 3.96
    },
    {
      "text": "at first and it's so frustrating cuz",
      "start": 33.96,
      "duration": 4.32
    },
    {
      "text": "llms they just get overwhelmed so",
      "start": 36.32,
      "duration": 5.0
    },
    {
      "text": "quickly and fragmenting your AI agent",
      "start": 38.28,
      "duration": 5.04
    },
    {
      "text": "into different sub agents to handle",
      "start": 41.32,
      "duration": 4.12
    },
    {
      "text": "different components is one of the best",
      "start": 43.32,
      "duration": 4.12
    },
    {
      "text": "ways to solve for this and take your AI",
      "start": 45.44,
      "duration": 4.92
    },
    {
      "text": "agents to that next level and that is",
      "start": 47.44,
      "duration": 4.08
    },
    {
      "text": "exactly what I'm going to show you how",
      "start": 50.36,
      "duration": 3.16
    },
    {
      "text": "to do right now because here's the thing",
      "start": 51.52,
      "duration": 4.12
    },
    {
      "text": "creating an army of specialized agents",
      "start": 53.52,
      "duration": 4.719
    },
    {
      "text": "takes a lot of consideration how do you",
      "start": 55.64,
      "duration": 4.64
    },
    {
      "text": "split up the problem what tools do your",
      "start": 58.239,
      "duration": 4.041
    },
    {
      "text": "agents need how do you combine the work",
      "start": 60.28,
      "duration": 4.239
    },
    {
      "text": "done by all the agents at the end and",
      "start": 62.28,
      "duration": 4.76
    },
    {
      "text": "most importantly one llm by itself",
      "start": 64.519,
      "duration": 4.321
    },
    {
      "text": "already takes a while to get a response",
      "start": 67.04,
      "duration": 3.119
    },
    {
      "text": "and so if you have to have many",
      "start": 68.84,
      "duration": 3.56
    },
    {
      "text": "specialized agents running together how",
      "start": 70.159,
      "duration": 3.761
    },
    {
      "text": "do you make it so that your system",
      "start": 72.4,
      "duration": 3.48
    },
    {
      "text": "doesn't take ages to run but it's all",
      "start": 73.92,
      "duration": 3.64
    },
    {
      "text": "right take a deep breath cuz I'm going",
      "start": 75.88,
      "duration": 3.72
    },
    {
      "text": "to cover this all with you in this video",
      "start": 77.56,
      "duration": 4.12
    },
    {
      "text": "so that by the end these kind of agentic",
      "start": 79.6,
      "duration": 4.519
    },
    {
      "text": "systems are as clear as day to you both",
      "start": 81.68,
      "duration": 5.479
    },
    {
      "text": "the how and equally important the why",
      "start": 84.119,
      "duration": 4.921
    },
    {
      "text": "we'll build a parallel agent",
      "start": 87.159,
      "duration": 3.92
    },
    {
      "text": "architecture using my two favorite",
      "start": 89.04,
      "duration": 4.52
    },
    {
      "text": "Frameworks pantic Ai and Lang graph so",
      "start": 91.079,
      "duration": 4.561
    },
    {
      "text": "we have a group of specialized agents",
      "start": 93.56,
      "duration": 4.199
    },
    {
      "text": "that are running simultaneously all",
      "start": 95.64,
      "duration": 4.4
    },
    {
      "text": "working to accomplish the same goal this",
      "start": 97.759,
      "duration": 4.441
    },
    {
      "text": "is hands down one of the most important",
      "start": 100.04,
      "duration": 4.16
    },
    {
      "text": "agent architectures and throughout this",
      "start": 102.2,
      "duration": 4.0
    },
    {
      "text": "video I have a lot of tips and trick",
      "start": 104.2,
      "duration": 4.36
    },
    {
      "text": "sprinkled in for both pantic Ai and Lane",
      "start": 106.2,
      "duration": 4.36
    },
    {
      "text": "graph a lot that I'm sharing with you",
      "start": 108.56,
      "duration": 3.519
    },
    {
      "text": "here so let's go ahead and dive right",
      "start": 110.56,
      "duration": 3.96
    },
    {
      "text": "into it so let's start with the basics",
      "start": 112.079,
      "duration": 4.64
    },
    {
      "text": "what is the parallel agent architecture",
      "start": 114.52,
      "duration": 4.32
    },
    {
      "text": "at its core and I think that this",
      "start": 116.719,
      "duration": 4.08
    },
    {
      "text": "article from anthrop IC on building",
      "start": 118.84,
      "duration": 4.36
    },
    {
      "text": "effective agents explains it the best at",
      "start": 120.799,
      "duration": 4.24
    },
    {
      "text": "a high level and it was published a",
      "start": 123.2,
      "duration": 3.919
    },
    {
      "text": "while ago but I still refer to this",
      "start": 125.039,
      "duration": 3.56
    },
    {
      "text": "constantly because it's just a great",
      "start": 127.119,
      "duration": 3.36
    },
    {
      "text": "resource covering all the different",
      "start": 128.599,
      "duration": 3.72
    },
    {
      "text": "agent architectures that you and I",
      "start": 130.479,
      "duration": 4.04
    },
    {
      "text": "should be paying attention to and they",
      "start": 132.319,
      "duration": 4.2
    },
    {
      "text": "even mentioned Lang graph in this",
      "start": 134.519,
      "duration": 3.44
    },
    {
      "text": "article which is super neat and they do",
      "start": 136.519,
      "duration": 2.961
    },
    {
      "text": "give a warning about Frameworks it's a",
      "start": 137.959,
      "duration": 3.161
    },
    {
      "text": "level of abstraction that can sometimes",
      "start": 139.48,
      "duration": 3.479
    },
    {
      "text": "be dangerous so you have to understand",
      "start": 141.12,
      "duration": 3.479
    },
    {
      "text": "how these Frameworks work under the hood",
      "start": 142.959,
      "duration": 3.601
    },
    {
      "text": "but that's why I'm showing you how to do",
      "start": 144.599,
      "duration": 4.36
    },
    {
      "text": "things with Lang graph and pantic AI in",
      "start": 146.56,
      "duration": 4.64
    },
    {
      "text": "this video and then scrolling down they",
      "start": 148.959,
      "duration": 3.64
    },
    {
      "text": "have these diagrams for all these",
      "start": 151.2,
      "duration": 2.64
    },
    {
      "text": "different architectures the one that",
      "start": 152.599,
      "duration": 3.401
    },
    {
      "text": "we're going to be focusing on is this",
      "start": 153.84,
      "duration": 4.96
    },
    {
      "text": "one right here parallelization and so we",
      "start": 156.0,
      "duration": 4.36
    },
    {
      "text": "have the input com in from a user and",
      "start": 158.8,
      "duration": 3.6
    },
    {
      "text": "then that's fed into these different",
      "start": 160.36,
      "duration": 4.12
    },
    {
      "text": "green boxes each of these represent an",
      "start": 162.4,
      "duration": 4.6
    },
    {
      "text": "AI agent with its own instructions and",
      "start": 164.48,
      "duration": 4.8
    },
    {
      "text": "tools to tackle a certain part of the",
      "start": 167.0,
      "duration": 3.92
    },
    {
      "text": "problem and then you have an aggregator",
      "start": 169.28,
      "duration": 3.72
    },
    {
      "text": "at the end in this case this is not a",
      "start": 170.92,
      "duration": 3.44
    },
    {
      "text": "large language model that's what the",
      "start": 173.0,
      "duration": 3.8
    },
    {
      "text": "purple box signifies that just takes the",
      "start": 174.36,
      "duration": 4.08
    },
    {
      "text": "output from each of the agents in",
      "start": 176.8,
      "duration": 4.159
    },
    {
      "text": "parallel and prod produces some sort of",
      "start": 178.44,
      "duration": 4.6
    },
    {
      "text": "nicely formatted output combining all",
      "start": 180.959,
      "duration": 4.441
    },
    {
      "text": "the results for the end user like you or",
      "start": 183.04,
      "duration": 4.559
    },
    {
      "text": "I and then in my case I even want to",
      "start": 185.4,
      "duration": 4.52
    },
    {
      "text": "take this a little bit further and so we",
      "start": 187.599,
      "duration": 4.841
    },
    {
      "text": "have a similar flow here but instead of",
      "start": 189.92,
      "duration": 4.48
    },
    {
      "text": "there just being a non llm that",
      "start": 192.44,
      "duration": 3.64
    },
    {
      "text": "Aggregates the results we use yet",
      "start": 194.4,
      "duration": 4.36
    },
    {
      "text": "another AI agent as a synthesizer to",
      "start": 196.08,
      "duration": 4.64
    },
    {
      "text": "take the output from each of our",
      "start": 198.76,
      "duration": 4.759
    },
    {
      "text": "parallel agents and figure out a way to",
      "start": 200.72,
      "duration": 5.72
    },
    {
      "text": "summarize it format it whatever for that",
      "start": 203.519,
      "duration": 4.521
    },
    {
      "text": "final output for the user I'm just",
      "start": 206.44,
      "duration": 3.4
    },
    {
      "text": "calling it a parallel agent architecture",
      "start": 208.04,
      "duration": 4.24
    },
    {
      "text": "in our case instead of a work quo for",
      "start": 209.84,
      "duration": 4.72
    },
    {
      "text": "orchestrator workers just because this",
      "start": 212.28,
      "duration": 4.84
    },
    {
      "text": "is just a better name parallel agents",
      "start": 214.56,
      "duration": 4.679
    },
    {
      "text": "and so the architexture that we have for",
      "start": 217.12,
      "duration": 4.479
    },
    {
      "text": "our agent today is this so what you're",
      "start": 219.239,
      "duration": 3.881
    },
    {
      "text": "looking at here is a visual",
      "start": 221.599,
      "duration": 3.84
    },
    {
      "text": "representation of the L graph workflow",
      "start": 223.12,
      "duration": 4.56
    },
    {
      "text": "for the agent that we are building we're",
      "start": 225.439,
      "duration": 4.841
    },
    {
      "text": "making a travel planner assistant agent",
      "start": 227.68,
      "duration": 5.119
    },
    {
      "text": "today it's a very good example of an AI",
      "start": 230.28,
      "duration": 4.519
    },
    {
      "text": "agent that could operate just as a",
      "start": 232.799,
      "duration": 3.64
    },
    {
      "text": "single agent but there's a lot that goes",
      "start": 234.799,
      "duration": 3.16
    },
    {
      "text": "into planning a trip and so we have",
      "start": 236.439,
      "duration": 3.88
    },
    {
      "text": "these specialized sub agents to handle",
      "start": 237.959,
      "duration": 4.36
    },
    {
      "text": "different components like the flight",
      "start": 240.319,
      "duration": 5.12
    },
    {
      "text": "hotel and recommending activities and so",
      "start": 242.319,
      "duration": 4.681
    },
    {
      "text": "at the start of this conversation we",
      "start": 245.439,
      "duration": 3.52
    },
    {
      "text": "gather information from the user where",
      "start": 247.0,
      "duration": 3.68
    },
    {
      "text": "are they flying to where are they flying",
      "start": 248.959,
      "duration": 3.801
    },
    {
      "text": "from how many days is their trip going",
      "start": 250.68,
      "duration": 4.16
    },
    {
      "text": "to be for and so we have this initial",
      "start": 252.76,
      "duration": 3.439
    },
    {
      "text": "Loop making sure we get all the",
      "start": 254.84,
      "duration": 3.519
    },
    {
      "text": "information and then once we have all of",
      "start": 256.199,
      "duration": 4.521
    },
    {
      "text": "that then we move on to the parallel",
      "start": 258.359,
      "duration": 4.361
    },
    {
      "text": "part of our workflow having these",
      "start": 260.72,
      "duration": 4.0
    },
    {
      "text": "different agents plan everything for the",
      "start": 262.72,
      "duration": 5.199
    },
    {
      "text": "trip in parallel and then the results",
      "start": 264.72,
      "duration": 4.6
    },
    {
      "text": "for all of these agents they're",
      "start": 267.919,
      "duration": 3.321
    },
    {
      "text": "recommended commendations are fed into",
      "start": 269.32,
      "duration": 4.319
    },
    {
      "text": "this final synthesizer agent that just",
      "start": 271.24,
      "duration": 4.44
    },
    {
      "text": "summarizes all of it in a neat package",
      "start": 273.639,
      "duration": 3.801
    },
    {
      "text": "to present to you for its final",
      "start": 275.68,
      "duration": 4.56
    },
    {
      "text": "recommendation for everything and we",
      "start": 277.44,
      "duration": 4.88
    },
    {
      "text": "even have a streamlet user interface",
      "start": 280.24,
      "duration": 4.2
    },
    {
      "text": "built out for this travel planner",
      "start": 282.32,
      "duration": 4.319
    },
    {
      "text": "assistant you can give your preferences",
      "start": 284.44,
      "duration": 3.72
    },
    {
      "text": "for things like your Airlines and the",
      "start": 286.639,
      "duration": 4.4
    },
    {
      "text": "amenities that you want in your hotel a",
      "start": 288.16,
      "duration": 4.759
    },
    {
      "text": "budget level and then you can save these",
      "start": 291.039,
      "duration": 3.961
    },
    {
      "text": "preferences and then I can ask it to",
      "start": 292.919,
      "duration": 3.801
    },
    {
      "text": "plan a trip for me so for example I can",
      "start": 295.0,
      "duration": 4.039
    },
    {
      "text": "say I want to plan a trip frying from",
      "start": 296.72,
      "duration": 4.759
    },
    {
      "text": "Minneapolis to Paris uh in June and then",
      "start": 299.039,
      "duration": 4.681
    },
    {
      "text": "my Max budget for a hotel is $200 per",
      "start": 301.479,
      "duration": 3.841
    },
    {
      "text": "night and look at this I don't know if",
      "start": 303.72,
      "duration": 3.96
    },
    {
      "text": "you caught that there but each of these",
      "start": 305.32,
      "duration": 4.64
    },
    {
      "text": "lines were printed out at exactly the",
      "start": 307.68,
      "duration": 4.44
    },
    {
      "text": "same time and that is the beginning of",
      "start": 309.96,
      "duration": 4.12
    },
    {
      "text": "the execution of each of those sub",
      "start": 312.12,
      "duration": 4.6
    },
    {
      "text": "agents in this parallel workflow and it",
      "start": 314.08,
      "duration": 4.679
    },
    {
      "text": "happens so fast like it's already",
      "start": 316.72,
      "duration": 4.16
    },
    {
      "text": "printing out the final results from the",
      "start": 318.759,
      "duration": 4.16
    },
    {
      "text": "synthesizer streaming it out to my",
      "start": 320.88,
      "duration": 4.36
    },
    {
      "text": "interface here but it was doing all of",
      "start": 322.919,
      "duration": 4.041
    },
    {
      "text": "that in parallel it got the flight",
      "start": 325.24,
      "duration": 3.72
    },
    {
      "text": "recommendations Hotel recommendations",
      "start": 326.96,
      "duration": 4.72
    },
    {
      "text": "and activity recommendations at exactly",
      "start": 328.96,
      "duration": 4.92
    },
    {
      "text": "the same time using different agents",
      "start": 331.68,
      "duration": 3.799
    },
    {
      "text": "that were given different tools and",
      "start": 333.88,
      "duration": 4.319
    },
    {
      "text": "instructions for that specific task and",
      "start": 335.479,
      "duration": 4.28
    },
    {
      "text": "then giving me the final output at the",
      "start": 338.199,
      "duration": 3.681
    },
    {
      "text": "end it is super neat so with our travel",
      "start": 339.759,
      "duration": 3.72
    },
    {
      "text": "planner assistant we're not going to be",
      "start": 341.88,
      "duration": 4.4
    },
    {
      "text": "using real flight hotel or weather data",
      "start": 343.479,
      "duration": 4.84
    },
    {
      "text": "it's all mocked just because we want a",
      "start": 346.28,
      "duration": 4.32
    },
    {
      "text": "simple example and focusing on the",
      "start": 348.319,
      "duration": 5.041
    },
    {
      "text": "architecture itself versus the tooling",
      "start": 350.6,
      "duration": 5.039
    },
    {
      "text": "but as usual I go above and beyond",
      "start": 353.36,
      "duration": 4.16
    },
    {
      "text": "providing a lot of value so if you want",
      "start": 355.639,
      "duration": 3.761
    },
    {
      "text": "to see the parallel agent architecture",
      "start": 357.52,
      "duration": 4.88
    },
    {
      "text": "in in a full-fledged use case check out",
      "start": 359.4,
      "duration": 5.6
    },
    {
      "text": "archon this is an AI agent that builds",
      "start": 362.4,
      "duration": 4.919
    },
    {
      "text": "other AI agents completely free and open",
      "start": 365.0,
      "duration": 4.12
    },
    {
      "text": "source this project that I'm pouring",
      "start": 367.319,
      "duration": 4.521
    },
    {
      "text": "myself into right now and I recently",
      "start": 369.12,
      "duration": 4.72
    },
    {
      "text": "implemented the parallel agent",
      "start": 371.84,
      "duration": 3.88
    },
    {
      "text": "architecture and so I'll have a link to",
      "start": 373.84,
      "duration": 3.6
    },
    {
      "text": "this GitHub repo in the description but",
      "start": 375.72,
      "duration": 4.0
    },
    {
      "text": "take a look at this you can ask archon",
      "start": 377.44,
      "duration": 5.199
    },
    {
      "text": "to autonomously refine the AI agent that",
      "start": 379.72,
      "duration": 5.08
    },
    {
      "text": "it produces the code for and then it'll",
      "start": 382.639,
      "duration": 3.68
    },
    {
      "text": "kick off this parallel workflow with",
      "start": 384.8,
      "duration": 3.88
    },
    {
      "text": "these agents to refine The Prompt tools",
      "start": 386.319,
      "duration": 5.361
    },
    {
      "text": "and agent and archon is an mCP server so",
      "start": 388.68,
      "duration": 4.639
    },
    {
      "text": "you can literally hook it into your AI",
      "start": 391.68,
      "duration": 3.76
    },
    {
      "text": "IDE like I'm doing with wind surf here",
      "start": 393.319,
      "duration": 4.481
    },
    {
      "text": "and so first I ask it to build an agent",
      "start": 395.44,
      "duration": 4.159
    },
    {
      "text": "using archon that searches the web with",
      "start": 397.8,
      "duration": 4.679
    },
    {
      "text": "brave it produces this pantic AI agent",
      "start": 399.599,
      "duration": 5.04
    },
    {
      "text": "for me so I've got all the code for it",
      "start": 402.479,
      "duration": 4.881
    },
    {
      "text": "here but then I can ask it to refine the",
      "start": 404.639,
      "duration": 4.801
    },
    {
      "text": "agent and so after that initial creation",
      "start": 407.36,
      "duration": 3.92
    },
    {
      "text": "you can see that I just ask it to refine",
      "start": 409.44,
      "duration": 4.44
    },
    {
      "text": "it and then this kicks off that parallel",
      "start": 411.28,
      "duration": 4.759
    },
    {
      "text": "workflow to make all those revisions and",
      "start": 413.88,
      "duration": 4.039
    },
    {
      "text": "then wind surf comes back and adds in",
      "start": 416.039,
      "duration": 3.681
    },
    {
      "text": "all these code changes so we have",
      "start": 417.919,
      "duration": 3.72
    },
    {
      "text": "parallel agents we've got wind surf",
      "start": 419.72,
      "duration": 3.96
    },
    {
      "text": "working with an mCP sub agent there's so",
      "start": 421.639,
      "duration": 4.721
    },
    {
      "text": "much cool stuff going on here so dive in",
      "start": 423.68,
      "duration": 4.079
    },
    {
      "text": "this if you wanted to go into something",
      "start": 426.36,
      "duration": 4.279
    },
    {
      "text": "insane but to start simple and really",
      "start": 427.759,
      "duration": 4.081
    },
    {
      "text": "make sure we understand this",
      "start": 430.639,
      "duration": 3.361
    },
    {
      "text": "architecture let's get into the code for",
      "start": 431.84,
      "duration": 4.44
    },
    {
      "text": "the travel planner assistant here is the",
      "start": 434.0,
      "duration": 4.36
    },
    {
      "text": "GitHub repository for the travel",
      "start": 436.28,
      "duration": 3.88
    },
    {
      "text": "planning assistant all the code that",
      "start": 438.36,
      "duration": 3.6
    },
    {
      "text": "we're going to create together right now",
      "start": 440.16,
      "duration": 3.4
    },
    {
      "text": "I'll have a link in the description to",
      "start": 441.96,
      "duration": 3.32
    },
    {
      "text": "this repo if you go there on the",
      "start": 443.56,
      "duration": 3.44
    },
    {
      "text": "homepage you have this read me where I",
      "start": 445.28,
      "duration": 4.08
    },
    {
      "text": "cover the architecture and also how you",
      "start": 447.0,
      "duration": 4.08
    },
    {
      "text": "can can get up and running yourself if",
      "start": 449.36,
      "duration": 4.239
    },
    {
      "text": "you want to follow along or take what",
      "start": 451.08,
      "duration": 4.679
    },
    {
      "text": "I've built here and tweak it for your",
      "start": 453.599,
      "duration": 4.361
    },
    {
      "text": "own use cases so I cover setting up your",
      "start": 455.759,
      "duration": 4.801
    },
    {
      "text": "environment um your variables running",
      "start": 457.96,
      "duration": 4.12
    },
    {
      "text": "the streamlet interface that I showed",
      "start": 460.56,
      "duration": 3.84
    },
    {
      "text": "earlier all that good stuff and so the",
      "start": 462.08,
      "duration": 4.48
    },
    {
      "text": "plan right now is I'm going to walk you",
      "start": 464.4,
      "duration": 5.0
    },
    {
      "text": "through building the pantic AI agents",
      "start": 466.56,
      "duration": 4.479
    },
    {
      "text": "that make up all the individual",
      "start": 469.4,
      "duration": 4.56
    },
    {
      "text": "components for our workflow so all of",
      "start": 471.039,
      "duration": 4.72
    },
    {
      "text": "the agents that you see in the agents",
      "start": 473.96,
      "duration": 4.079
    },
    {
      "text": "folder those correspond to the different",
      "start": 475.759,
      "duration": 4.56
    },
    {
      "text": "nodes that we have in our ra we have the",
      "start": 478.039,
      "duration": 4.401
    },
    {
      "text": "infog Gathering agent the specialized",
      "start": 480.319,
      "duration": 4.041
    },
    {
      "text": "agents who are planning the trip and",
      "start": 482.44,
      "duration": 3.96
    },
    {
      "text": "then that final synthesizer all those",
      "start": 484.36,
      "duration": 4.119
    },
    {
      "text": "are individual Python scripts that you",
      "start": 486.4,
      "duration": 4.56
    },
    {
      "text": "can see right here and so I'll walk you",
      "start": 488.479,
      "duration": 4.601
    },
    {
      "text": "through creating one of the agents from",
      "start": 490.96,
      "duration": 3.76
    },
    {
      "text": "scratch we'll create the flight agent",
      "start": 493.08,
      "duration": 3.72
    },
    {
      "text": "from scratch and then I'll briefly show",
      "start": 494.72,
      "duration": 3.96
    },
    {
      "text": "you each of the other agents that are",
      "start": 496.8,
      "duration": 3.44
    },
    {
      "text": "going to be created in a very similar",
      "start": 498.68,
      "duration": 4.359
    },
    {
      "text": "way with pantic AI and then with that we",
      "start": 500.24,
      "duration": 5.639
    },
    {
      "text": "can dive into building our Lang graph",
      "start": 503.039,
      "duration": 4.88
    },
    {
      "text": "graph combining all these agents",
      "start": 505.879,
      "duration": 4.801
    },
    {
      "text": "together to create the full process and",
      "start": 507.919,
      "duration": 4.761
    },
    {
      "text": "so with that let's get into building our",
      "start": 510.68,
      "duration": 4.88
    },
    {
      "text": "first agent so to make this as simple as",
      "start": 512.68,
      "duration": 4.32
    },
    {
      "text": "possible for you you can think of",
      "start": 515.56,
      "duration": 3.88
    },
    {
      "text": "building pantic AI agents as building",
      "start": 517.0,
      "duration": 4.719
    },
    {
      "text": "three distinct parts so let me show you",
      "start": 519.44,
      "duration": 4.0
    },
    {
      "text": "the documentation with a really nice",
      "start": 521.719,
      "duration": 3.441
    },
    {
      "text": "example to demonstrate this so this is",
      "start": 523.44,
      "duration": 4.04
    },
    {
      "text": "the weather agent just very simple",
      "start": 525.16,
      "duration": 4.88
    },
    {
      "text": "implementation that I cover a lot it",
      "start": 527.48,
      "duration": 4.24
    },
    {
      "text": "just shows these different components",
      "start": 530.04,
      "duration": 3.6
    },
    {
      "text": "very well when you're building an agent",
      "start": 531.72,
      "duration": 4.08
    },
    {
      "text": "the first component is defining the",
      "start": 533.64,
      "duration": 4.12
    },
    {
      "text": "dependencies these are things like the",
      "start": 535.8,
      "duration": 4.44
    },
    {
      "text": "API keys and database connections that",
      "start": 537.76,
      "duration": 4.88
    },
    {
      "text": "your agent tools need for the agent to",
      "start": 540.24,
      "duration": 5.12
    },
    {
      "text": "do things on your behalf then the second",
      "start": 542.64,
      "duration": 5.56
    },
    {
      "text": "component is the definition of the agent",
      "start": 545.36,
      "duration": 4.76
    },
    {
      "text": "itself and so this is where you specify",
      "start": 548.2,
      "duration": 3.56
    },
    {
      "text": "things like the large language model you",
      "start": 550.12,
      "duration": 4.56
    },
    {
      "text": "want to use the system prompt the exact",
      "start": 551.76,
      "duration": 4.72
    },
    {
      "text": "dependencies and a lot of other",
      "start": 554.68,
      "duration": 3.44
    },
    {
      "text": "different parameters that pantic AI",
      "start": 556.48,
      "duration": 3.039
    },
    {
      "text": "offers for things like defining",
      "start": 558.12,
      "duration": 4.92
    },
    {
      "text": "automatic retries for your agent as well",
      "start": 559.519,
      "duration": 5.481
    },
    {
      "text": "and then the last component which",
      "start": 563.04,
      "duration": 4.479
    },
    {
      "text": "usually takes most of your code for an",
      "start": 565.0,
      "duration": 5.56
    },
    {
      "text": "agent is defining the tools itself and",
      "start": 567.519,
      "duration": 4.481
    },
    {
      "text": "so you have all the functionality",
      "start": 570.56,
      "duration": 3.68
    },
    {
      "text": "wrapped up in a function that the agent",
      "start": 572.0,
      "duration": 3.92
    },
    {
      "text": "can call upon when it wants to do",
      "start": 574.24,
      "duration": 3.76
    },
    {
      "text": "something specific and in this dock",
      "start": 575.92,
      "duration": 4.68
    },
    {
      "text": "string this larger comment that you have",
      "start": 578.0,
      "duration": 4.2
    },
    {
      "text": "at the top of the function this is where",
      "start": 580.6,
      "duration": 4.4
    },
    {
      "text": "you specify to the agent when and how to",
      "start": 582.2,
      "duration": 4.68
    },
    {
      "text": "use each of these tools so you give it",
      "start": 585.0,
      "duration": 3.959
    },
    {
      "text": "the purpose and the arguments so I can",
      "start": 586.88,
      "duration": 4.28
    },
    {
      "text": "reason about when it would invoke this",
      "start": 588.959,
      "duration": 4.241
    },
    {
      "text": "tool specifically and what arguments",
      "start": 591.16,
      "duration": 3.64
    },
    {
      "text": "that you would pass in for something",
      "start": 593.2,
      "duration": 3.84
    },
    {
      "text": "like the location in this example and",
      "start": 594.8,
      "duration": 4.719
    },
    {
      "text": "you just Define all the individual tools",
      "start": 597.04,
      "duration": 4.84
    },
    {
      "text": "in the same way so that's a good",
      "start": 599.519,
      "duration": 4.721
    },
    {
      "text": "overview of how we build an agent with",
      "start": 601.88,
      "duration": 4.36
    },
    {
      "text": "pantic AI we're going to follow a very",
      "start": 604.24,
      "duration": 3.599
    },
    {
      "text": "similar structure here building our",
      "start": 606.24,
      "duration": 3.8
    },
    {
      "text": "flight agent so first we'll start by",
      "start": 607.839,
      "duration": 3.841
    },
    {
      "text": "importing all of the libraries that we",
      "start": 610.04,
      "duration": 3.52
    },
    {
      "text": "need and defining some of our",
      "start": 611.68,
      "duration": 3.68
    },
    {
      "text": "configuration like getting the exact",
      "start": 613.56,
      "duration": 3.399
    },
    {
      "text": "large language model that we want which",
      "start": 615.36,
      "duration": 4.08
    },
    {
      "text": "in this utils.py I just have this simple",
      "start": 616.959,
      "duration": 4.12
    },
    {
      "text": "function to get that based on our",
      "start": 619.44,
      "duration": 4.28
    },
    {
      "text": "environment variables that we set next",
      "start": 621.079,
      "duration": 5.241
    },
    {
      "text": "up I want to Define my dependencies for",
      "start": 623.72,
      "duration": 4.52
    },
    {
      "text": "the flight agent in this case we're",
      "start": 626.32,
      "duration": 3.68
    },
    {
      "text": "keeping it very simple again this is",
      "start": 628.24,
      "duration": 3.52
    },
    {
      "text": "just more of a demonstration focusing on",
      "start": 630.0,
      "duration": 4.079
    },
    {
      "text": "the architecture versus making really",
      "start": 631.76,
      "duration": 4.24
    },
    {
      "text": "robust agents and so in this case our",
      "start": 634.079,
      "duration": 4.401
    },
    {
      "text": "dependencies we just have the preferred",
      "start": 636.0,
      "duration": 4.0
    },
    {
      "text": "Airlines for the user so they're going",
      "start": 638.48,
      "duration": 3.32
    },
    {
      "text": "to set that in the streamlet UI like we",
      "start": 640.0,
      "duration": 3.639
    },
    {
      "text": "saw in the demo earlier and then that's",
      "start": 641.8,
      "duration": 4.24
    },
    {
      "text": "given as a piece of information to our",
      "start": 643.639,
      "duration": 4.681
    },
    {
      "text": "flight agent then we can Define our",
      "start": 646.04,
      "duration": 3.64
    },
    {
      "text": "system prompt just giving the",
      "start": 648.32,
      "duration": 3.92
    },
    {
      "text": "instructions to the flight agent for its",
      "start": 649.68,
      "duration": 5.04
    },
    {
      "text": "role and goals and how to use the tools",
      "start": 652.24,
      "duration": 5.24
    },
    {
      "text": "that we give it as well and then that",
      "start": 654.72,
      "duration": 4.799
    },
    {
      "text": "brings us to our second component for",
      "start": 657.48,
      "duration": 3.84
    },
    {
      "text": "building agents which is the definition",
      "start": 659.519,
      "duration": 3.961
    },
    {
      "text": "for the agent itself so we give it just",
      "start": 661.32,
      "duration": 4.199
    },
    {
      "text": "like we saw in the documentation the",
      "start": 663.48,
      "duration": 4.799
    },
    {
      "text": "model system prompt dependencies and",
      "start": 665.519,
      "duration": 5.32
    },
    {
      "text": "giving it some automatic retries and",
      "start": 668.279,
      "duration": 3.721
    },
    {
      "text": "then with that out of the way we can get",
      "start": 670.839,
      "duration": 2.921
    },
    {
      "text": "on to the very last part I mean it's",
      "start": 672.0,
      "duration": 3.839
    },
    {
      "text": "it's pretty simple overall because now",
      "start": 673.76,
      "duration": 3.48
    },
    {
      "text": "we're just defining the tools for the",
      "start": 675.839,
      "duration": 3.641
    },
    {
      "text": "agent and so we use this python",
      "start": 677.24,
      "duration": 4.76
    },
    {
      "text": "decorator above the function definition",
      "start": 679.48,
      "duration": 4.919
    },
    {
      "text": "itself to tell pantic AI that this is a",
      "start": 682.0,
      "duration": 4.959
    },
    {
      "text": "tool for our flight agent that we just",
      "start": 684.399,
      "duration": 5.041
    },
    {
      "text": "defined above and then the parameters",
      "start": 686.959,
      "duration": 5.721
    },
    {
      "text": "here the large language model decides",
      "start": 689.44,
      "duration": 5.399
    },
    {
      "text": "what we're going to use for the origin",
      "start": 692.68,
      "duration": 5.08
    },
    {
      "text": "destination and date for searching",
      "start": 694.839,
      "duration": 5.56
    },
    {
      "text": "flights and then this run context this",
      "start": 697.76,
      "duration": 5.4
    },
    {
      "text": "is how pantic AI injects the",
      "start": 700.399,
      "duration": 5.68
    },
    {
      "text": "dependencies like the preferred flights",
      "start": 703.16,
      "duration": 5.919
    },
    {
      "text": "into this function and so at the very",
      "start": 706.079,
      "duration": 4.521
    },
    {
      "text": "beginning just like we saw in the docs",
      "start": 709.079,
      "duration": 3.56
    },
    {
      "text": "we're going to have a comment here this",
      "start": 710.6,
      "duration": 4.76
    },
    {
      "text": "doc string that tells the agent when and",
      "start": 712.639,
      "duration": 5.241
    },
    {
      "text": "how to use this function and then we can",
      "start": 715.36,
      "duration": 4.44
    },
    {
      "text": "get straight into the implement ation",
      "start": 717.88,
      "duration": 4.519
    },
    {
      "text": "cuz really tools for agents are just",
      "start": 719.8,
      "duration": 4.96
    },
    {
      "text": "functions that you wrap up and send as a",
      "start": 722.399,
      "duration": 4.321
    },
    {
      "text": "part of the prompt to the llm and so in",
      "start": 724.76,
      "duration": 3.72
    },
    {
      "text": "this case we're using mock data so we",
      "start": 726.72,
      "duration": 4.04
    },
    {
      "text": "have this dictionary that simulates",
      "start": 728.48,
      "duration": 3.84
    },
    {
      "text": "something you might get back if you used",
      "start": 730.76,
      "duration": 3.96
    },
    {
      "text": "a real flight API and so we return a few",
      "start": 732.32,
      "duration": 5.079
    },
    {
      "text": "flight options and then if there are any",
      "start": 734.72,
      "duration": 4.479
    },
    {
      "text": "preferred airlines that the user",
      "start": 737.399,
      "duration": 3.921
    },
    {
      "text": "specified we're going to change the",
      "start": 739.199,
      "duration": 4.561
    },
    {
      "text": "order of the flights based on their",
      "start": 741.32,
      "duration": 4.8
    },
    {
      "text": "preferences and then just add a note",
      "start": 743.76,
      "duration": 4.319
    },
    {
      "text": "that this flight was preferred or maybe",
      "start": 746.12,
      "duration": 3.399
    },
    {
      "text": "multiple flights were prefer referred",
      "start": 748.079,
      "duration": 3.921
    },
    {
      "text": "and so the result of all of this is then",
      "start": 749.519,
      "duration": 3.921
    },
    {
      "text": "just going to be returned for this",
      "start": 752.0,
      "duration": 3.16
    },
    {
      "text": "function and so whatever is returned",
      "start": 753.44,
      "duration": 5.0
    },
    {
      "text": "here this Json string is going back to",
      "start": 755.16,
      "duration": 5.52
    },
    {
      "text": "the llm so the agent the flight agent",
      "start": 758.44,
      "duration": 4.6
    },
    {
      "text": "invokes this tool to search for flights",
      "start": 760.68,
      "duration": 4.159
    },
    {
      "text": "and then that list of sorted flights",
      "start": 763.04,
      "duration": 4.359
    },
    {
      "text": "based on preferences is given back so I",
      "start": 764.839,
      "duration": 5.041
    },
    {
      "text": "can then reason about that and give the",
      "start": 767.399,
      "duration": 5.12
    },
    {
      "text": "final answer to the user for what flight",
      "start": 769.88,
      "duration": 4.399
    },
    {
      "text": "it recommends and even though we're",
      "start": 772.519,
      "duration": 3.56
    },
    {
      "text": "building this agent to be a part of a",
      "start": 774.279,
      "duration": 3.841
    },
    {
      "text": "larger architecture we can use this",
      "start": 776.079,
      "duration": 4.12
    },
    {
      "text": "flight agent in olation and have a",
      "start": 778.12,
      "duration": 4.8
    },
    {
      "text": "conversation with just it and so in this",
      "start": 780.199,
      "duration": 5.801
    },
    {
      "text": "extras folder I created this flight C.P",
      "start": 782.92,
      "duration": 5.2
    },
    {
      "text": "script and so this is a way for us to in",
      "start": 786.0,
      "duration": 4.519
    },
    {
      "text": "the terminal have a conversation with",
      "start": 788.12,
      "duration": 4.519
    },
    {
      "text": "the flight agent and there's a bit more",
      "start": 790.519,
      "duration": 4.32
    },
    {
      "text": "of a complex implementation that I have",
      "start": 792.639,
      "duration": 4.241
    },
    {
      "text": "here for streaming the output from the",
      "start": 794.839,
      "duration": 4.601
    },
    {
      "text": "pantic AI agent I won't go in the weeds",
      "start": 796.88,
      "duration": 4.72
    },
    {
      "text": "for this but I spent a good amount of",
      "start": 799.44,
      "duration": 3.759
    },
    {
      "text": "time figuring this out so take this and",
      "start": 801.6,
      "duration": 3.2
    },
    {
      "text": "use it for yourself it'll definitely",
      "start": 803.199,
      "duration": 3.041
    },
    {
      "text": "save you a headache if you want to",
      "start": 804.8,
      "duration": 3.56
    },
    {
      "text": "stream the output from your pantic AI",
      "start": 806.24,
      "duration": 3.959
    },
    {
      "text": "agents so that not only do you get the",
      "start": 808.36,
      "duration": 4.52
    },
    {
      "text": "response from the agent but you get the",
      "start": 810.199,
      "duration": 4.64
    },
    {
      "text": "tokens out in real time as it is",
      "start": 812.88,
      "duration": 4.28
    },
    {
      "text": "producing the response and so back over",
      "start": 814.839,
      "duration": 4.36
    },
    {
      "text": "in the terminal I can run this command",
      "start": 817.16,
      "duration": 4.56
    },
    {
      "text": "to run the flight CLI and then I can say",
      "start": 819.199,
      "duration": 4.681
    },
    {
      "text": "something basic like Hello this won't",
      "start": 821.72,
      "duration": 4.119
    },
    {
      "text": "cause it to search for flights but then",
      "start": 823.88,
      "duration": 4.36
    },
    {
      "text": "I can say something like I want to go",
      "start": 825.839,
      "duration": 7.641
    },
    {
      "text": "from Minneapolis to Tokyo on June 1st",
      "start": 828.24,
      "duration": 7.56
    },
    {
      "text": "and based on what I sent here it's going",
      "start": 833.48,
      "duration": 4.359
    },
    {
      "text": "to pick out the origin destination and",
      "start": 835.8,
      "duration": 4.399
    },
    {
      "text": "date use that tool to search for flights",
      "start": 837.839,
      "duration": 4.36
    },
    {
      "text": "and then stream out its recommendations",
      "start": 840.199,
      "duration": 4.481
    },
    {
      "text": "to me obviously it's going to give me",
      "start": 842.199,
      "duration": 4.08
    },
    {
      "text": "the same recommendations no matter what",
      "start": 844.68,
      "duration": 4.0
    },
    {
      "text": "I say because it's not really searching",
      "start": 846.279,
      "duration": 4.521
    },
    {
      "text": "for flights but yeah this is working",
      "start": 848.68,
      "duration": 4.159
    },
    {
      "text": "beautifully and then for the rest of our",
      "start": 850.8,
      "duration": 4.64
    },
    {
      "text": "agents they're built in the same way the",
      "start": 852.839,
      "duration": 4.961
    },
    {
      "text": "sponsor of today's video is lutra a",
      "start": 855.44,
      "duration": 4.759
    },
    {
      "text": "userfriendly solution for creating",
      "start": 857.8,
      "duration": 4.279
    },
    {
      "text": "automated workflows with natural",
      "start": 860.199,
      "duration": 4.161
    },
    {
      "text": "language ever wish your AI assistant",
      "start": 862.079,
      "duration": 4.081
    },
    {
      "text": "could actually do things and not just",
      "start": 864.36,
      "duration": 4.159
    },
    {
      "text": "chat I mean sure most platforms have web",
      "start": 866.16,
      "duration": 4.28
    },
    {
      "text": "search and canvas at this point but that",
      "start": 868.519,
      "duration": 5.0
    },
    {
      "text": "is not enough lutra is a full-fledged AI",
      "start": 870.44,
      "duration": 4.88
    },
    {
      "text": "agent that connects seamlessly with your",
      "start": 873.519,
      "duration": 4.401
    },
    {
      "text": "favorite services like slack and Gmail",
      "start": 875.32,
      "duration": 4.24
    },
    {
      "text": "and then it can do things within those",
      "start": 877.92,
      "duration": 3.919
    },
    {
      "text": "Services based on your conversation so",
      "start": 879.56,
      "duration": 4.519
    },
    {
      "text": "it's very similar to a custom agent that",
      "start": 881.839,
      "duration": 4.12
    },
    {
      "text": "you or I would make but the really cool",
      "start": 884.079,
      "duration": 4.161
    },
    {
      "text": "part is that it creates code to take",
      "start": 885.959,
      "duration": 4.041
    },
    {
      "text": "these actions on your behalf and then",
      "start": 888.24,
      "duration": 3.959
    },
    {
      "text": "you can save that code as an automated",
      "start": 890.0,
      "duration": 4.959
    },
    {
      "text": "workflow to reuse later or set up as a",
      "start": 892.199,
      "duration": 4.921
    },
    {
      "text": "scheduled task called A playbook they're",
      "start": 894.959,
      "duration": 4.361
    },
    {
      "text": "also launching this brand new plugin",
      "start": 897.12,
      "duration": 4.0
    },
    {
      "text": "platform which is going to allow lutra",
      "start": 899.32,
      "duration": 4.28
    },
    {
      "text": "to connect to literally any API you just",
      "start": 901.12,
      "duration": 4.56
    },
    {
      "text": "give it the documentation and then it'll",
      "start": 903.6,
      "duration": 4.12
    },
    {
      "text": "be able to write code to connect to that",
      "start": 905.68,
      "duration": 3.56
    },
    {
      "text": "service just like the native",
      "start": 907.72,
      "duration": 4.119
    },
    {
      "text": "Integrations it is super neat and so",
      "start": 909.24,
      "duration": 4.599
    },
    {
      "text": "what does lutra actually look like well",
      "start": 911.839,
      "duration": 3.56
    },
    {
      "text": "I'll show you a quick demo of it right",
      "start": 913.839,
      "duration": 3.761
    },
    {
      "text": "now so to show you the power of lutra",
      "start": 915.399,
      "duration": 3.921
    },
    {
      "text": "I'm obviously going to give it a request",
      "start": 917.6,
      "duration": 3.679
    },
    {
      "text": "that something like Claude or GPT would",
      "start": 919.32,
      "duration": 4.439
    },
    {
      "text": "not be able to do so I'm going to ask it",
      "start": 921.279,
      "duration": 4.36
    },
    {
      "text": "to get a list of poll requests from",
      "start": 923.759,
      "duration": 5.241
    },
    {
      "text": "archon my AI agent Builder from GitHub",
      "start": 925.639,
      "duration": 5.44
    },
    {
      "text": "and then add them to a Google sheet and",
      "start": 929.0,
      "duration": 3.92
    },
    {
      "text": "it's going to start right off the bat by",
      "start": 931.079,
      "duration": 3.401
    },
    {
      "text": "reasoning to itself and you can watch",
      "start": 932.92,
      "duration": 3.52
    },
    {
      "text": "this reasoning which is really cool and",
      "start": 934.48,
      "duration": 3.919
    },
    {
      "text": "then it'll ask me a couple of follow-up",
      "start": 936.44,
      "duration": 3.879
    },
    {
      "text": "questions so I'll go ahead and answer",
      "start": 938.399,
      "duration": 3.92
    },
    {
      "text": "those and then what it's going to do is",
      "start": 940.319,
      "duration": 4.801
    },
    {
      "text": "ask me to connect the necessary accounts",
      "start": 942.319,
      "duration": 5.08
    },
    {
      "text": "for it to have that authorization for",
      "start": 945.12,
      "duration": 4.399
    },
    {
      "text": "both Google Drive and GitHub and in this",
      "start": 947.399,
      "duration": 4.321
    },
    {
      "text": "case I already connected GitHub so I'm",
      "start": 949.519,
      "duration": 3.24
    },
    {
      "text": "showing you that I don't have to",
      "start": 951.72,
      "duration": 3.359
    },
    {
      "text": "reconnect it but it is going to ask me",
      "start": 952.759,
      "duration": 4.161
    },
    {
      "text": "to connect my Google Drive so first",
      "start": 955.079,
      "duration": 3.961
    },
    {
      "text": "it'll create that code for this custom",
      "start": 956.92,
      "duration": 4.0
    },
    {
      "text": "integration and then it'll ask me to",
      "start": 959.04,
      "duration": 4.0
    },
    {
      "text": "connect my Google API all right so I'm",
      "start": 960.92,
      "duration": 4.2
    },
    {
      "text": "all connected and now it just continues",
      "start": 963.04,
      "duration": 4.039
    },
    {
      "text": "right away so I don't even have to go",
      "start": 965.12,
      "duration": 2.959
    },
    {
      "text": "somewhere else to configure my",
      "start": 967.079,
      "duration": 2.401
    },
    {
      "text": "credentials I just do it right here in",
      "start": 968.079,
      "duration": 2.801
    },
    {
      "text": "the chat when it's required for the",
      "start": 969.48,
      "duration": 4.0
    },
    {
      "text": "first time and now it's doing everything",
      "start": 970.88,
      "duration": 4.439
    },
    {
      "text": "that I asked it to do and boom look at",
      "start": 973.48,
      "duration": 3.719
    },
    {
      "text": "that it even opens up the Google sheet",
      "start": 975.319,
      "duration": 4.88
    },
    {
      "text": "within the lutra UI on the right hand",
      "start": 977.199,
      "duration": 5.0
    },
    {
      "text": "side it looks absolutely perfect pulled",
      "start": 980.199,
      "duration": 4.88
    },
    {
      "text": "all my active PRS tells me my sheet ID",
      "start": 982.199,
      "duration": 4.44
    },
    {
      "text": "asks me what I want to do next we can",
      "start": 985.079,
      "duration": 3.24
    },
    {
      "text": "see all the actions that it did within",
      "start": 986.639,
      "duration": 4.081
    },
    {
      "text": "GitHub and Google sheet this is just",
      "start": 988.319,
      "duration": 4.76
    },
    {
      "text": "incredible to me pretty slick right luch",
      "start": 990.72,
      "duration": 4.28
    },
    {
      "text": "is like having an AI agent that can",
      "start": 993.079,
      "duration": 4.721
    },
    {
      "text": "reason think and build Integrations for",
      "start": 995.0,
      "duration": 4.759
    },
    {
      "text": "you so you're not just chatting with it",
      "start": 997.8,
      "duration": 4.2
    },
    {
      "text": "it's doing stuff for you and building",
      "start": 999.759,
      "duration": 4.721
    },
    {
      "text": "automations at the exact same time and",
      "start": 1002.0,
      "duration": 4.0
    },
    {
      "text": "it's totally free to get started so you",
      "start": 1004.48,
      "duration": 3.76
    },
    {
      "text": "can head on over to lutra doai I'll have",
      "start": 1006.0,
      "duration": 3.92
    },
    {
      "text": "a link in the description definitely",
      "start": 1008.24,
      "duration": 3.48
    },
    {
      "text": "worth checking them out so that is the",
      "start": 1009.92,
      "duration": 3.56
    },
    {
      "text": "flight agent now we can dive really",
      "start": 1011.72,
      "duration": 3.64
    },
    {
      "text": "quickly into the other specialized",
      "start": 1013.48,
      "duration": 4.0
    },
    {
      "text": "agents I'm going to go fast because this",
      "start": 1015.36,
      "duration": 4.52
    },
    {
      "text": "setup is very similar take a look at",
      "start": 1017.48,
      "duration": 4.76
    },
    {
      "text": "this this is our hotel agent so we've",
      "start": 1019.88,
      "duration": 4.6
    },
    {
      "text": "got our dependencies again and this time",
      "start": 1022.24,
      "duration": 3.719
    },
    {
      "text": "it is going to be the amenities that",
      "start": 1024.48,
      "duration": 3.439
    },
    {
      "text": "we're looking for and our budget level",
      "start": 1025.959,
      "duration": 3.84
    },
    {
      "text": "then we have a system prompt structured",
      "start": 1027.919,
      "duration": 4.201
    },
    {
      "text": "in a very similar way we Define our",
      "start": 1029.799,
      "duration": 4.801
    },
    {
      "text": "agent and then we have a tool to look up",
      "start": 1032.12,
      "duration": 3.919
    },
    {
      "text": "hotels so that it can make a",
      "start": 1034.6,
      "duration": 3.439
    },
    {
      "text": "recommendation so we have again this",
      "start": 1036.039,
      "duration": 4.0
    },
    {
      "text": "mock dictionary this is what a real",
      "start": 1038.039,
      "duration": 4.961
    },
    {
      "text": "hotel API would give something like this",
      "start": 1040.039,
      "duration": 4.76
    },
    {
      "text": "and then we filter and sort based on the",
      "start": 1043.0,
      "duration": 3.839
    },
    {
      "text": "max price preferred amenities and the",
      "start": 1044.799,
      "duration": 3.561
    },
    {
      "text": "budget level and then return the final",
      "start": 1046.839,
      "duration": 3.84
    },
    {
      "text": "list of TS so the agent can reason about",
      "start": 1048.36,
      "duration": 3.88
    },
    {
      "text": "that to make its",
      "start": 1050.679,
      "duration": 3.681
    },
    {
      "text": "recommendation and then for the activity",
      "start": 1052.24,
      "duration": 4.28
    },
    {
      "text": "agent we don't even have dependencies in",
      "start": 1054.36,
      "duration": 4.36
    },
    {
      "text": "this case so it is even simpler we just",
      "start": 1056.52,
      "duration": 3.56
    },
    {
      "text": "have our agent definition with the",
      "start": 1058.72,
      "duration": 3.16
    },
    {
      "text": "system prompt and then because the",
      "start": 1060.08,
      "duration": 3.56
    },
    {
      "text": "weather oftentimes dictates what",
      "start": 1061.88,
      "duration": 3.72
    },
    {
      "text": "activities you can do on a trip we give",
      "start": 1063.64,
      "duration": 3.88
    },
    {
      "text": "it a tool to look up the weather so",
      "start": 1065.6,
      "duration": 4.48
    },
    {
      "text": "based on the date and a city we have",
      "start": 1067.52,
      "duration": 4.96
    },
    {
      "text": "this mock data so for a few cities it",
      "start": 1070.08,
      "duration": 4.719
    },
    {
      "text": "can look at the temperature and then use",
      "start": 1072.48,
      "duration": 4.079
    },
    {
      "text": "that to reason about if it's going to",
      "start": 1074.799,
      "duration": 3.601
    },
    {
      "text": "recommend more indoor activities or more",
      "start": 1076.559,
      "duration": 4.041
    },
    {
      "text": "outdoor activities whatever it might",
      "start": 1078.4,
      "duration": 4.279
    },
    {
      "text": "dictate based on the weather so those",
      "start": 1080.6,
      "duration": 4.28
    },
    {
      "text": "are all of our specialized agents we've",
      "start": 1082.679,
      "duration": 4.961
    },
    {
      "text": "covered everything for these three right",
      "start": 1084.88,
      "duration": 4.84
    },
    {
      "text": "here now we just have two left we have",
      "start": 1087.64,
      "duration": 4.08
    },
    {
      "text": "our final synthesizer agent and then our",
      "start": 1089.72,
      "duration": 4.64
    },
    {
      "text": "info Gathering agent and so starting",
      "start": 1091.72,
      "duration": 5.88
    },
    {
      "text": "with the simpler one we have our final",
      "start": 1094.36,
      "duration": 5.679
    },
    {
      "text": "planner and take a look at this there's",
      "start": 1097.6,
      "duration": 5.0
    },
    {
      "text": "not even a tool for this agent because",
      "start": 1100.039,
      "duration": 6.041
    },
    {
      "text": "it's main job its only job is to take",
      "start": 1102.6,
      "duration": 5.199
    },
    {
      "text": "the recommended hotels flights and",
      "start": 1106.08,
      "duration": 3.8
    },
    {
      "text": "activities and combine it together in a",
      "start": 1107.799,
      "duration": 4.0
    },
    {
      "text": "nice summary this is also a good",
      "start": 1109.88,
      "duration": 3.679
    },
    {
      "text": "opportunity to have an agent that could",
      "start": 1111.799,
      "duration": 3.481
    },
    {
      "text": "validate the different outputs from the",
      "start": 1113.559,
      "duration": 4.24
    },
    {
      "text": "other agents you can use a synthesizer",
      "start": 1115.28,
      "duration": 4.92
    },
    {
      "text": "as a validator as well and add different",
      "start": 1117.799,
      "duration": 4.601
    },
    {
      "text": "tools to do that but in our case to keep",
      "start": 1120.2,
      "duration": 4.359
    },
    {
      "text": "it very simple it is just an agent with",
      "start": 1122.4,
      "duration": 4.92
    },
    {
      "text": "a system prompt nice and easy and then",
      "start": 1124.559,
      "duration": 5.36
    },
    {
      "text": "the last agent that we have is our info",
      "start": 1127.32,
      "duration": 4.359
    },
    {
      "text": "Gathering agent and what makes this",
      "start": 1129.919,
      "duration": 3.681
    },
    {
      "text": "agent Special is that we are using",
      "start": 1131.679,
      "duration": 4.36
    },
    {
      "text": "structured outputs to guarantee that",
      "start": 1133.6,
      "duration": 4.48
    },
    {
      "text": "every single response from this agent",
      "start": 1136.039,
      "duration": 4.721
    },
    {
      "text": "has these key pieces of information and",
      "start": 1138.08,
      "duration": 4.8
    },
    {
      "text": "the reason I'm doing this besides it",
      "start": 1140.76,
      "duration": 4.039
    },
    {
      "text": "just being a good opportunity for me to",
      "start": 1142.88,
      "duration": 4.84
    },
    {
      "text": "show you pantic AI structured outputs is",
      "start": 1144.799,
      "duration": 5.24
    },
    {
      "text": "because we want to guarantee that we",
      "start": 1147.72,
      "duration": 4.64
    },
    {
      "text": "have the necessary information for our",
      "start": 1150.039,
      "duration": 4.801
    },
    {
      "text": "specialized sub agents to invoke the",
      "start": 1152.36,
      "duration": 4.36
    },
    {
      "text": "tools that they need to invoke to search",
      "start": 1154.84,
      "duration": 4.92
    },
    {
      "text": "for flights hotels and weather data and",
      "start": 1156.72,
      "duration": 5.6
    },
    {
      "text": "so we get the destination origin Max",
      "start": 1159.76,
      "duration": 4.2
    },
    {
      "text": "hotel price the dates that they're",
      "start": 1162.32,
      "duration": 3.64
    },
    {
      "text": "leaving and returning everything that",
      "start": 1163.96,
      "duration": 4.44
    },
    {
      "text": "our sub agents need and then we have the",
      "start": 1165.96,
      "duration": 4.04
    },
    {
      "text": "resp response this is what we give back",
      "start": 1168.4,
      "duration": 3.8
    },
    {
      "text": "to the user as they're conversating with",
      "start": 1170.0,
      "duration": 4.52
    },
    {
      "text": "this infog Gathering agent and then",
      "start": 1172.2,
      "duration": 4.479
    },
    {
      "text": "finally we have this all important",
      "start": 1174.52,
      "duration": 4.399
    },
    {
      "text": "Boolean value that determines if the",
      "start": 1176.679,
      "duration": 4.401
    },
    {
      "text": "user has given all of the necessary",
      "start": 1178.919,
      "duration": 4.801
    },
    {
      "text": "values and this is what we key off of to",
      "start": 1181.08,
      "duration": 4.719
    },
    {
      "text": "determine in our graph if we can",
      "start": 1183.72,
      "duration": 4.76
    },
    {
      "text": "continue to the rest of this flow",
      "start": 1185.799,
      "duration": 5.921
    },
    {
      "text": "invoking our parallel agents and so at",
      "start": 1188.48,
      "duration": 4.72
    },
    {
      "text": "the beginning the user might say",
      "start": 1191.72,
      "duration": 4.12
    },
    {
      "text": "something like I want to take a trip to",
      "start": 1193.2,
      "duration": 4.88
    },
    {
      "text": "Germany and then the G infog Gathering",
      "start": 1195.84,
      "duration": 4.68
    },
    {
      "text": "agent will be okay cool but I don't have",
      "start": 1198.08,
      "duration": 4.44
    },
    {
      "text": "enough information to call upon the rest",
      "start": 1200.52,
      "duration": 3.56
    },
    {
      "text": "of these agents here I need to know",
      "start": 1202.52,
      "duration": 3.639
    },
    {
      "text": "where you flying from what dates are",
      "start": 1204.08,
      "duration": 4.44
    },
    {
      "text": "your trip going to be and so the user",
      "start": 1206.159,
      "duration": 4.961
    },
    {
      "text": "will give all that information and then",
      "start": 1208.52,
      "duration": 4.24
    },
    {
      "text": "we can continue to the rest of the",
      "start": 1211.12,
      "duration": 3.16
    },
    {
      "text": "process but if they don't give what's",
      "start": 1212.76,
      "duration": 4.2
    },
    {
      "text": "required we continue in this Loop until",
      "start": 1214.28,
      "duration": 4.72
    },
    {
      "text": "they do that's the important job of this",
      "start": 1216.96,
      "duration": 4.48
    },
    {
      "text": "infog Gathering agent is to gatekeep the",
      "start": 1219.0,
      "duration": 4.6
    },
    {
      "text": "rest of the process to make sure that",
      "start": 1221.44,
      "duration": 4.32
    },
    {
      "text": "the agents don't hallucinate Because by",
      "start": 1223.6,
      "duration": 4.0
    },
    {
      "text": "the time it gets to them they will have",
      "start": 1225.76,
      "duration": 4.52
    },
    {
      "text": "all of the necessary information and so",
      "start": 1227.6,
      "duration": 4.079
    },
    {
      "text": "the rest of the agent is defined in a",
      "start": 1230.28,
      "duration": 2.639
    },
    {
      "text": "very similar way where we just have a",
      "start": 1231.679,
      "duration": 2.961
    },
    {
      "text": "system prompt and then the definition",
      "start": 1232.919,
      "duration": 3.321
    },
    {
      "text": "for the agent itself and then the way",
      "start": 1234.64,
      "duration": 4.279
    },
    {
      "text": "that we can enforce that it produces a",
      "start": 1236.24,
      "duration": 5.16
    },
    {
      "text": "Json output that matches this structure",
      "start": 1238.919,
      "duration": 4.521
    },
    {
      "text": "is we just add this single line to our",
      "start": 1241.4,
      "duration": 4.519
    },
    {
      "text": "pantic AI agent the result type is and",
      "start": 1243.44,
      "duration": 4.28
    },
    {
      "text": "then we pass in our class that we",
      "start": 1245.919,
      "duration": 4.521
    },
    {
      "text": "defined right here for travel details",
      "start": 1247.72,
      "duration": 5.76
    },
    {
      "text": "and that is it we have now defined all",
      "start": 1250.44,
      "duration": 5.359
    },
    {
      "text": "of our agents in this graph and so now",
      "start": 1253.48,
      "duration": 4.4
    },
    {
      "text": "we can take each of them and piece them",
      "start": 1255.799,
      "duration": 3.801
    },
    {
      "text": "together in in our Lang graph",
      "start": 1257.88,
      "duration": 4.24
    },
    {
      "text": "implementation and just like with pantic",
      "start": 1259.6,
      "duration": 4.36
    },
    {
      "text": "AI you can think of Lang graph",
      "start": 1262.12,
      "duration": 4.48
    },
    {
      "text": "implementations as being three distinct",
      "start": 1263.96,
      "duration": 4.64
    },
    {
      "text": "parts and I just love breaking down",
      "start": 1266.6,
      "duration": 3.48
    },
    {
      "text": "complex things like this if you can",
      "start": 1268.6,
      "duration": 3.8
    },
    {
      "text": "compartmentalize the different parts of",
      "start": 1270.08,
      "duration": 4.079
    },
    {
      "text": "what goes into a process it just makes",
      "start": 1272.4,
      "duration": 3.92
    },
    {
      "text": "it a lot easier to understand and so for",
      "start": 1274.159,
      "duration": 4.801
    },
    {
      "text": "Lang graph our first part is the state",
      "start": 1276.32,
      "duration": 4.4
    },
    {
      "text": "for the graph these are the key pieces",
      "start": 1278.96,
      "duration": 3.64
    },
    {
      "text": "of information that you want to keep",
      "start": 1280.72,
      "duration": 3.64
    },
    {
      "text": "track of throughout the execution that",
      "start": 1282.6,
      "duration": 3.92
    },
    {
      "text": "your agents will use you'll give back to",
      "start": 1284.36,
      "duration": 4.28
    },
    {
      "text": "the user things like the conversation",
      "start": 1286.52,
      "duration": 4.039
    },
    {
      "text": "history and the results from the",
      "start": 1288.64,
      "duration": 4.2
    },
    {
      "text": "different agent executions then the",
      "start": 1290.559,
      "duration": 4.521
    },
    {
      "text": "second part is defining all of the nodes",
      "start": 1292.84,
      "duration": 4.12
    },
    {
      "text": "for the graph and So within each node",
      "start": 1295.08,
      "duration": 3.8
    },
    {
      "text": "you have all the logic to do something",
      "start": 1296.96,
      "duration": 4.4
    },
    {
      "text": "like invoke an AI agent or in Lane graph",
      "start": 1298.88,
      "duration": 4.2
    },
    {
      "text": "each node doesn't even have to call upon",
      "start": 1301.36,
      "duration": 3.919
    },
    {
      "text": "an llm you can just have deterministic",
      "start": 1303.08,
      "duration": 3.959
    },
    {
      "text": "code if you want and sometimes that's",
      "start": 1305.279,
      "duration": 3.721
    },
    {
      "text": "even better than using large language",
      "start": 1307.039,
      "duration": 3.841
    },
    {
      "text": "models that can be all over the place",
      "start": 1309.0,
      "duration": 3.76
    },
    {
      "text": "sometimes so that's the second thing and",
      "start": 1310.88,
      "duration": 3.6
    },
    {
      "text": "then the very last component the third",
      "start": 1312.76,
      "duration": 4.159
    },
    {
      "text": "component to Lang graph is setting up",
      "start": 1314.48,
      "duration": 4.76
    },
    {
      "text": "the graph itself so you take the State",
      "start": 1316.919,
      "duration": 4.64
    },
    {
      "text": "you take your nodes you define all of",
      "start": 1319.24,
      "duration": 4.6
    },
    {
      "text": "them within a graph instance and then",
      "start": 1321.559,
      "duration": 4.881
    },
    {
      "text": "you connect them all together with edges",
      "start": 1323.84,
      "duration": 4.319
    },
    {
      "text": "and that's it that's all that goes into",
      "start": 1326.44,
      "duration": 3.68
    },
    {
      "text": "building a graph but what I'm going to",
      "start": 1328.159,
      "duration": 4.12
    },
    {
      "text": "do with you right here to walk you",
      "start": 1330.12,
      "duration": 4.72
    },
    {
      "text": "through it step by step is I am going to",
      "start": 1332.279,
      "duration": 4.041
    },
    {
      "text": "delete everything take a look at this",
      "start": 1334.84,
      "duration": 3.24
    },
    {
      "text": "all right boom it is gone we have a",
      "start": 1336.32,
      "duration": 3.2
    },
    {
      "text": "blank slate so I'm going to walk you",
      "start": 1338.08,
      "duration": 3.4
    },
    {
      "text": "through this step by step to really make",
      "start": 1339.52,
      "duration": 3.519
    },
    {
      "text": "sure you understand how we are",
      "start": 1341.48,
      "duration": 3.48
    },
    {
      "text": "connecting all these agents together and",
      "start": 1343.039,
      "duration": 3.801
    },
    {
      "text": "managing the state for everything in L",
      "start": 1344.96,
      "duration": 3.079
    },
    {
      "text": "graph so the first thing we're going to",
      "start": 1346.84,
      "duration": 3.36
    },
    {
      "text": "do is support all of our libraries that",
      "start": 1348.039,
      "duration": 3.961
    },
    {
      "text": "we need and the different agents that",
      "start": 1350.2,
      "duration": 2.92
    },
    {
      "text": "we're going to be running through our",
      "start": 1352.0,
      "duration": 3.559
    },
    {
      "text": "nodes then we can knock out right away",
      "start": 1353.12,
      "duration": 4.559
    },
    {
      "text": "the first part of our graph which is the",
      "start": 1355.559,
      "duration": 3.921
    },
    {
      "text": "state and so this is everything that we",
      "start": 1357.679,
      "duration": 3.441
    },
    {
      "text": "have to keep track of throughout the",
      "start": 1359.48,
      "duration": 4.48
    },
    {
      "text": "execution of our workflow and so we have",
      "start": 1361.12,
      "duration": 5.08
    },
    {
      "text": "the latest user message we are building",
      "start": 1363.96,
      "duration": 4.36
    },
    {
      "text": "up conversation history specifically for",
      "start": 1366.2,
      "duration": 3.8
    },
    {
      "text": "the infog Gathering agent the rest of",
      "start": 1368.32,
      "duration": 2.719
    },
    {
      "text": "the agents don't really need",
      "start": 1370.0,
      "duration": 3.159
    },
    {
      "text": "conversation history then we have the",
      "start": 1371.039,
      "duration": 4.12
    },
    {
      "text": "travel details that's that structured",
      "start": 1373.159,
      "duration": 4.161
    },
    {
      "text": "output from our info Gathering agent",
      "start": 1375.159,
      "duration": 3.76
    },
    {
      "text": "we'll store that because we need to use",
      "start": 1377.32,
      "duration": 3.359
    },
    {
      "text": "it for the rest of our agents and then",
      "start": 1378.919,
      "duration": 3.88
    },
    {
      "text": "we have user preferences the result from",
      "start": 1380.679,
      "duration": 4.48
    },
    {
      "text": "each of the parallel agents and then",
      "start": 1382.799,
      "duration": 4.921
    },
    {
      "text": "finally what is aggregated together into",
      "start": 1385.159,
      "duration": 4.801
    },
    {
      "text": "that final plan from our synthesizer",
      "start": 1387.72,
      "duration": 5.36
    },
    {
      "text": "agent is stored here so that's the state",
      "start": 1389.96,
      "duration": 5.199
    },
    {
      "text": "now we can get on to building the graph",
      "start": 1393.08,
      "duration": 4.24
    },
    {
      "text": "itself so I'll show you setting up the",
      "start": 1395.159,
      "duration": 3.76
    },
    {
      "text": "structure for the graph and then we'll",
      "start": 1397.32,
      "duration": 3.959
    },
    {
      "text": "get into building each individual node",
      "start": 1398.919,
      "duration": 3.721
    },
    {
      "text": "and so the first thing is you want to",
      "start": 1401.279,
      "duration": 3.961
    },
    {
      "text": "create an instance of the graph and then",
      "start": 1402.64,
      "duration": 4.6
    },
    {
      "text": "you pass in the travel state so now we",
      "start": 1405.24,
      "duration": 3.6
    },
    {
      "text": "know what the state is going to look",
      "start": 1407.24,
      "duration": 3.559
    },
    {
      "text": "like for this graph and then we can",
      "start": 1408.84,
      "duration": 3.719
    },
    {
      "text": "Define all of our nodes and again",
      "start": 1410.799,
      "duration": 3.76
    },
    {
      "text": "there'll be a separate python function",
      "start": 1412.559,
      "duration": 4.081
    },
    {
      "text": "for each of these nodes right now I'm",
      "start": 1414.559,
      "duration": 3.961
    },
    {
      "text": "just adding them into the graph one at a",
      "start": 1416.64,
      "duration": 3.36
    },
    {
      "text": "time all the nodes that you see here",
      "start": 1418.52,
      "duration": 3.32
    },
    {
      "text": "like Gathering info getting the next",
      "start": 1420.0,
      "duration": 3.159
    },
    {
      "text": "user message getting flight",
      "start": 1421.84,
      "duration": 3.88
    },
    {
      "text": "recommendations these names correspond",
      "start": 1423.159,
      "duration": 5.12
    },
    {
      "text": "exactly with the nodes that we see in",
      "start": 1425.72,
      "duration": 5.199
    },
    {
      "text": "this graph because the lane graph Studio",
      "start": 1428.279,
      "duration": 4.64
    },
    {
      "text": "that we're looking at right here it",
      "start": 1430.919,
      "duration": 4.521
    },
    {
      "text": "looks at this python script it builds",
      "start": 1432.919,
      "duration": 5.161
    },
    {
      "text": "the graph and then it displays exactly",
      "start": 1435.44,
      "duration": 4.88
    },
    {
      "text": "how we set it up with our nodes and then",
      "start": 1438.08,
      "duration": 4.24
    },
    {
      "text": "also the edges which we're defining here",
      "start": 1440.32,
      "duration": 3.92
    },
    {
      "text": "so we start with the infog Gathering",
      "start": 1442.32,
      "duration": 4.2
    },
    {
      "text": "agent and then we have this conditional",
      "start": 1444.24,
      "duration": 4.72
    },
    {
      "text": "Edge and so this is that decision right",
      "start": 1446.52,
      "duration": 4.72
    },
    {
      "text": "here do we get the next user message to",
      "start": 1448.96,
      "duration": 4.4
    },
    {
      "text": "continue the conversation to gather the",
      "start": 1451.24,
      "duration": 6.28
    },
    {
      "text": "info or do we pass on to our specialized",
      "start": 1453.36,
      "duration": 7.559
    },
    {
      "text": "parallel agents to finish the workflow",
      "start": 1457.52,
      "duration": 6.0
    },
    {
      "text": "recommend the travel details so we make",
      "start": 1460.919,
      "duration": 4.721
    },
    {
      "text": "that decision based on this function",
      "start": 1463.52,
      "duration": 4.12
    },
    {
      "text": "that we'll Define later as well and then",
      "start": 1465.64,
      "duration": 4.399
    },
    {
      "text": "we add an edge from getting next user",
      "start": 1467.64,
      "duration": 4.56
    },
    {
      "text": "message to Gathering info because once",
      "start": 1470.039,
      "duration": 4.24
    },
    {
      "text": "we get more details from the user we",
      "start": 1472.2,
      "duration": 4.199
    },
    {
      "text": "want to pass back to the info Gathering",
      "start": 1474.279,
      "duration": 4.361
    },
    {
      "text": "agent to determine if it has everything",
      "start": 1476.399,
      "duration": 4.921
    },
    {
      "text": "it needs now and then finally we add",
      "start": 1478.64,
      "duration": 4.8
    },
    {
      "text": "edges from all the specialized agents",
      "start": 1481.32,
      "duration": 4.719
    },
    {
      "text": "going all three into the same create",
      "start": 1483.44,
      "duration": 4.52
    },
    {
      "text": "final plan node because that's how we",
      "start": 1486.039,
      "duration": 4.801
    },
    {
      "text": "can take the outputs from all three and",
      "start": 1487.96,
      "duration": 5.0
    },
    {
      "text": "bring them together into the synthesizer",
      "start": 1490.84,
      "duration": 4.24
    },
    {
      "text": "all at the same time and then finally",
      "start": 1492.96,
      "duration": 4.92
    },
    {
      "text": "our synthesizer agent just goes to the",
      "start": 1495.08,
      "duration": 4.959
    },
    {
      "text": "end of of the graph now we can move on",
      "start": 1497.88,
      "duration": 4.6
    },
    {
      "text": "to building out the nodes for our graph",
      "start": 1500.039,
      "duration": 4.561
    },
    {
      "text": "and so starting with our first one the",
      "start": 1502.48,
      "duration": 4.64
    },
    {
      "text": "Gathering info agent and so we take two",
      "start": 1504.6,
      "duration": 4.52
    },
    {
      "text": "pieces of information for this function",
      "start": 1507.12,
      "duration": 4.12
    },
    {
      "text": "we have our state so it can access",
      "start": 1509.12,
      "duration": 4.08
    },
    {
      "text": "things like the message history and user",
      "start": 1511.24,
      "duration": 4.36
    },
    {
      "text": "input and then we also give it a writer",
      "start": 1513.2,
      "duration": 3.76
    },
    {
      "text": "I'm not going to go into the Weeds on",
      "start": 1515.6,
      "duration": 3.04
    },
    {
      "text": "this but this is a custom object that",
      "start": 1516.96,
      "duration": 3.64
    },
    {
      "text": "you can pass in in Lan graph which",
      "start": 1518.64,
      "duration": 4.08
    },
    {
      "text": "allows us to stream the output from our",
      "start": 1520.6,
      "duration": 4.4
    },
    {
      "text": "pantic AI agents so we watch The Tokens",
      "start": 1522.72,
      "duration": 5.6
    },
    {
      "text": "come out in real time and so first we'll",
      "start": 1525.0,
      "duration": 5.36
    },
    {
      "text": "will get the user input from the state",
      "start": 1528.32,
      "duration": 3.599
    },
    {
      "text": "and then we'll build up the message",
      "start": 1530.36,
      "duration": 3.12
    },
    {
      "text": "history over time because we want our",
      "start": 1531.919,
      "duration": 3.041
    },
    {
      "text": "info Gathering agent to be",
      "start": 1533.48,
      "duration": 3.439
    },
    {
      "text": "conversational because different parts",
      "start": 1534.96,
      "duration": 3.8
    },
    {
      "text": "of the trip are going to be given by the",
      "start": 1536.919,
      "duration": 4.12
    },
    {
      "text": "user throughout a couple of messages",
      "start": 1538.76,
      "duration": 4.56
    },
    {
      "text": "potentially and the reason we're using a",
      "start": 1541.039,
      "duration": 4.64
    },
    {
      "text": "model messages type adapter here this is",
      "start": 1543.32,
      "duration": 4.479
    },
    {
      "text": "a special object that we have from",
      "start": 1545.679,
      "duration": 4.6
    },
    {
      "text": "pantic AI is because when we get our",
      "start": 1547.799,
      "duration": 5.12
    },
    {
      "text": "messages from a pantic AI agent we need",
      "start": 1550.279,
      "duration": 5.041
    },
    {
      "text": "to convert it into a format that we can",
      "start": 1552.919,
      "duration": 4.721
    },
    {
      "text": "store in a database and to make it very",
      "start": 1555.32,
      "duration": 4.68
    },
    {
      "text": "compatible with databases like postgress",
      "start": 1557.64,
      "duration": 6.159
    },
    {
      "text": "we choose Json B binary Json that's the",
      "start": 1560.0,
      "duration": 5.88
    },
    {
      "text": "format that we store our conversation",
      "start": 1563.799,
      "duration": 4.561
    },
    {
      "text": "history in the database and in the state",
      "start": 1565.88,
      "duration": 4.88
    },
    {
      "text": "here but then when we retrieve that",
      "start": 1568.36,
      "duration": 4.84
    },
    {
      "text": "conversation history to use a again in a",
      "start": 1570.76,
      "duration": 4.84
    },
    {
      "text": "pantic agent we have to convert it back",
      "start": 1573.2,
      "duration": 4.64
    },
    {
      "text": "into the format for pantic AI so that",
      "start": 1575.6,
      "duration": 5.36
    },
    {
      "text": "it's an object in Python not just Json",
      "start": 1577.84,
      "duration": 5.0
    },
    {
      "text": "being that's what we're doing here so",
      "start": 1580.96,
      "duration": 3.48
    },
    {
      "text": "one of the more complicated parts of",
      "start": 1582.84,
      "duration": 4.28
    },
    {
      "text": "pantic AI I hope that makes sense though",
      "start": 1584.44,
      "duration": 4.76
    },
    {
      "text": "and so now with the conversation history",
      "start": 1587.12,
      "duration": 4.6
    },
    {
      "text": "we can invoke our agent using run Stream",
      "start": 1589.2,
      "duration": 4.4
    },
    {
      "text": "So that we get the tokens outputed in",
      "start": 1591.72,
      "duration": 3.64
    },
    {
      "text": "real time and we just have to pass in",
      "start": 1593.6,
      "duration": 4.24
    },
    {
      "text": "the user input and then the conversation",
      "start": 1595.36,
      "duration": 4.88
    },
    {
      "text": "history and also if you want to run",
      "start": 1597.84,
      "duration": 3.92
    },
    {
      "text": "synchronously like you don't want to",
      "start": 1600.24,
      "duration": 2.76
    },
    {
      "text": "stream the output you just want to get",
      "start": 1601.76,
      "duration": 3.68
    },
    {
      "text": "it all at once I have this comment right",
      "start": 1603.0,
      "duration": 4.08
    },
    {
      "text": "here which you could use instead it",
      "start": 1605.44,
      "duration": 4.16
    },
    {
      "text": "simplifies things a lot but I think a",
      "start": 1607.08,
      "duration": 4.88
    },
    {
      "text": "lot of you appreciate having streamed",
      "start": 1609.6,
      "duration": 3.88
    },
    {
      "text": "output it just makes the agent feel",
      "start": 1611.96,
      "duration": 3.48
    },
    {
      "text": "snappier and more responsive so I wanted",
      "start": 1613.48,
      "duration": 4.28
    },
    {
      "text": "to show you how to do that and so the",
      "start": 1615.44,
      "duration": 4.92
    },
    {
      "text": "way that we do that it's kind of unique",
      "start": 1617.76,
      "duration": 3.96
    },
    {
      "text": "here because remember this infog",
      "start": 1620.36,
      "duration": 3.679
    },
    {
      "text": "Gathering agent it streams out a",
      "start": 1621.72,
      "duration": 4.88
    },
    {
      "text": "structured response we have that Json",
      "start": 1624.039,
      "duration": 4.281
    },
    {
      "text": "object I can even go back to the agent",
      "start": 1626.6,
      "duration": 3.76
    },
    {
      "text": "and show you that definition again we",
      "start": 1628.32,
      "duration": 3.64
    },
    {
      "text": "have this Json object that we're",
      "start": 1630.36,
      "duration": 3.88
    },
    {
      "text": "outputting and so it's not as simple as",
      "start": 1631.96,
      "duration": 5.36
    },
    {
      "text": "just streaming out a string because it's",
      "start": 1634.24,
      "duration": 5.12
    },
    {
      "text": "a dictionary that has these different",
      "start": 1637.32,
      "duration": 4.4
    },
    {
      "text": "values and so there's a very specific",
      "start": 1639.36,
      "duration": 4.72
    },
    {
      "text": "way to do this in pantic AI that I I",
      "start": 1641.72,
      "duration": 4.88
    },
    {
      "text": "don't want to dive into a ton but if you",
      "start": 1644.08,
      "duration": 4.88
    },
    {
      "text": "go to their documentation they do show",
      "start": 1646.6,
      "duration": 4.24
    },
    {
      "text": "you how to do this so I just poked",
      "start": 1648.96,
      "duration": 3.48
    },
    {
      "text": "around for a couple of hours with this",
      "start": 1650.84,
      "duration": 3.319
    },
    {
      "text": "documentation figuring out how to best",
      "start": 1652.44,
      "duration": 3.76
    },
    {
      "text": "do it using this example right here",
      "start": 1654.159,
      "duration": 4.361
    },
    {
      "text": "streaming structured responses and so",
      "start": 1656.2,
      "duration": 4.44
    },
    {
      "text": "you can see that when you run an agent",
      "start": 1658.52,
      "duration": 4.44
    },
    {
      "text": "in stream mode and it outputs a",
      "start": 1660.64,
      "duration": 4.639
    },
    {
      "text": "structured response the output that you",
      "start": 1662.96,
      "duration": 4.559
    },
    {
      "text": "get over time as it streams out the",
      "start": 1665.279,
      "duration": 4.321
    },
    {
      "text": "tokens is going to look something like",
      "start": 1667.519,
      "duration": 3.801
    },
    {
      "text": "this where it slowly builds up the",
      "start": 1669.6,
      "duration": 4.24
    },
    {
      "text": "values in the dictionary and even within",
      "start": 1671.32,
      "duration": 5.199
    },
    {
      "text": "a single key it can build up that string",
      "start": 1673.84,
      "duration": 3.92
    },
    {
      "text": "over time and that's what we're going to",
      "start": 1676.519,
      "duration": 4.4
    },
    {
      "text": "do with our response and so over time",
      "start": 1677.76,
      "duration": 5.48
    },
    {
      "text": "we're building up the travel details.",
      "start": 1680.919,
      "duration": 4.64
    },
    {
      "text": "response because this piece of",
      "start": 1683.24,
      "duration": 4.76
    },
    {
      "text": "information is what we want to give to",
      "start": 1685.559,
      "duration": 4.681
    },
    {
      "text": "the user as the output and then the rest",
      "start": 1688.0,
      "duration": 4.44
    },
    {
      "text": "of the items we're just keeping track of",
      "start": 1690.24,
      "duration": 3.48
    },
    {
      "text": "these behind the scenes because that'll",
      "start": 1692.44,
      "duration": 3.479
    },
    {
      "text": "get past into our other agents later",
      "start": 1693.72,
      "duration": 4.16
    },
    {
      "text": "this is the most complicated part of the",
      "start": 1695.919,
      "duration": 3.88
    },
    {
      "text": "entire graph so I hope that makes sense",
      "start": 1697.88,
      "duration": 3.799
    },
    {
      "text": "to you and then we're just validating",
      "start": 1699.799,
      "duration": 5.24
    },
    {
      "text": "the Json at each iteration and we are",
      "start": 1701.679,
      "duration": 5.561
    },
    {
      "text": "using this debounce bu so that we're not",
      "start": 1705.039,
      "duration": 4.161
    },
    {
      "text": "every single split second validating the",
      "start": 1707.24,
      "duration": 4.559
    },
    {
      "text": "Json structure we're just doing it every",
      "start": 1709.2,
      "duration": 4.92
    },
    {
      "text": "you know .01 seconds here validating",
      "start": 1711.799,
      "duration": 5.841
    },
    {
      "text": "that the Json is good Json and then",
      "start": 1714.12,
      "duration": 5.6
    },
    {
      "text": "finally at the very end if we have a",
      "start": 1717.64,
      "duration": 4.879
    },
    {
      "text": "valid travel details. response then",
      "start": 1719.72,
      "duration": 4.079
    },
    {
      "text": "we're going to write that out to the",
      "start": 1722.519,
      "duration": 4.361
    },
    {
      "text": "user and we're going to save this to our",
      "start": 1723.799,
      "duration": 6.161
    },
    {
      "text": "graph state so we get the results from",
      "start": 1726.88,
      "duration": 6.48
    },
    {
      "text": "invoking our agent and we append that",
      "start": 1729.96,
      "duration": 5.199
    },
    {
      "text": "conversation history so we're adding on",
      "start": 1733.36,
      "duration": 3.72
    },
    {
      "text": "to the conversation history and then",
      "start": 1735.159,
      "duration": 5.24
    },
    {
      "text": "also setting the travel details to that",
      "start": 1737.08,
      "duration": 5.76
    },
    {
      "text": "structured output that we just got and",
      "start": 1740.399,
      "duration": 4.88
    },
    {
      "text": "so now travel details is going to be an",
      "start": 1742.84,
      "duration": 4.6
    },
    {
      "text": "object that contains all of these pieces",
      "start": 1745.279,
      "duration": 3.681
    },
    {
      "text": "of information that we can reference",
      "start": 1747.44,
      "duration": 4.2
    },
    {
      "text": "later from our other specialized agents",
      "start": 1748.96,
      "duration": 4.36
    },
    {
      "text": "and then luckily the rest of our nodes",
      "start": 1751.64,
      "duration": 4.32
    },
    {
      "text": "are definitely simpler so starting with",
      "start": 1753.32,
      "duration": 5.239
    },
    {
      "text": "our flight recommendations node and so",
      "start": 1755.96,
      "duration": 4.839
    },
    {
      "text": "same arguments that we're passing in",
      "start": 1758.559,
      "duration": 4.24
    },
    {
      "text": "we're going to get the travel details",
      "start": 1760.799,
      "duration": 4.36
    },
    {
      "text": "and preferred Airlines from our state so",
      "start": 1762.799,
      "duration": 4.201
    },
    {
      "text": "this is set by the user in the front end",
      "start": 1765.159,
      "duration": 3.76
    },
    {
      "text": "and then this is what was just set by",
      "start": 1767.0,
      "duration": 4.159
    },
    {
      "text": "our info Gathering agent and then we",
      "start": 1768.919,
      "duration": 5.0
    },
    {
      "text": "also write out to the screen that we are",
      "start": 1771.159,
      "duration": 4.64
    },
    {
      "text": "getting flight recommendations so",
      "start": 1773.919,
      "duration": 4.161
    },
    {
      "text": "remember we saw in the demo earlier that",
      "start": 1775.799,
      "duration": 4.041
    },
    {
      "text": "it wrote out to the screen getting",
      "start": 1778.08,
      "duration": 3.68
    },
    {
      "text": "flight recommendations getting Hotel",
      "start": 1779.84,
      "duration": 3.4
    },
    {
      "text": "recommendations getting activity",
      "start": 1781.76,
      "duration": 3.32
    },
    {
      "text": "recommendations all at the exact same",
      "start": 1783.24,
      "duration": 3.799
    },
    {
      "text": "time so I'm just putting this in here so",
      "start": 1785.08,
      "duration": 3.88
    },
    {
      "text": "that we can see that this is truly",
      "start": 1787.039,
      "duration": 4.24
    },
    {
      "text": "simultaneous execution CU sometimes",
      "start": 1788.96,
      "duration": 4.199
    },
    {
      "text": "people will say it's parallel when",
      "start": 1791.279,
      "duration": 4.201
    },
    {
      "text": "really it's just running one after the",
      "start": 1793.159,
      "duration": 4.601
    },
    {
      "text": "other sequentially just combining the",
      "start": 1795.48,
      "duration": 4.559
    },
    {
      "text": "output put at the end but this is truly",
      "start": 1797.76,
      "duration": 3.68
    },
    {
      "text": "parallel and that's really important",
      "start": 1800.039,
      "duration": 2.721
    },
    {
      "text": "because otherwise this workflow would",
      "start": 1801.44,
      "duration": 4.0
    },
    {
      "text": "take a long time if it wasn't",
      "start": 1802.76,
      "duration": 5.0
    },
    {
      "text": "simultaneous and so then we're going to",
      "start": 1805.44,
      "duration": 3.92
    },
    {
      "text": "set up our dependencies for the flight",
      "start": 1807.76,
      "duration": 3.0
    },
    {
      "text": "just with the preferred airlines that we",
      "start": 1809.36,
      "duration": 3.96
    },
    {
      "text": "get from the state and we can create our",
      "start": 1810.76,
      "duration": 5.159
    },
    {
      "text": "prompt and invoke our flight agent so",
      "start": 1813.32,
      "duration": 4.44
    },
    {
      "text": "we're injecting the key pieces of",
      "start": 1815.919,
      "duration": 3.961
    },
    {
      "text": "information from the travel details into",
      "start": 1817.76,
      "duration": 4.039
    },
    {
      "text": "this prompt here so that our flight",
      "start": 1819.88,
      "duration": 4.48
    },
    {
      "text": "agent has the information that it needs",
      "start": 1821.799,
      "duration": 4.72
    },
    {
      "text": "to invoke that tool and then we just",
      "start": 1824.36,
      "duration": 4.12
    },
    {
      "text": "call it and we do it synchron ly this",
      "start": 1826.519,
      "duration": 3.721
    },
    {
      "text": "time so I'm not doing any fancy",
      "start": 1828.48,
      "duration": 3.96
    },
    {
      "text": "streaming stuff here because there's",
      "start": 1830.24,
      "duration": 3.48
    },
    {
      "text": "nothing that we want to write to the",
      "start": 1832.44,
      "duration": 4.28
    },
    {
      "text": "screen yet we want to wait until we have",
      "start": 1833.72,
      "duration": 4.799
    },
    {
      "text": "everything synthesized together and then",
      "start": 1836.72,
      "duration": 3.92
    },
    {
      "text": "stream that out to the user and then in",
      "start": 1838.519,
      "duration": 3.681
    },
    {
      "text": "the meantime we'll just say that we're",
      "start": 1840.64,
      "duration": 3.08
    },
    {
      "text": "loading that we're getting the flight",
      "start": 1842.2,
      "duration": 4.12
    },
    {
      "text": "recommendations so pretty simple and",
      "start": 1843.72,
      "duration": 3.88
    },
    {
      "text": "then the only thing that we want to",
      "start": 1846.32,
      "duration": 3.68
    },
    {
      "text": "update in the state for the graph is the",
      "start": 1847.6,
      "duration": 4.12
    },
    {
      "text": "flight results so we just take the",
      "start": 1850.0,
      "duration": 3.799
    },
    {
      "text": "results from invoking the agent get the",
      "start": 1851.72,
      "duration": 3.839
    },
    {
      "text": "data and then that's just a string that",
      "start": 1853.799,
      "duration": 4.641
    },
    {
      "text": "we store in Flight results and then for",
      "start": 1855.559,
      "duration": 5.041
    },
    {
      "text": "our other parallel agents it's going to",
      "start": 1858.44,
      "duration": 4.0
    },
    {
      "text": "look very similar so getting Hotel",
      "start": 1860.6,
      "duration": 3.679
    },
    {
      "text": "recommendations again we just get the",
      "start": 1862.44,
      "duration": 4.16
    },
    {
      "text": "necessary pieces of State build up the",
      "start": 1864.279,
      "duration": 4.12
    },
    {
      "text": "hotel dependencies and then we create",
      "start": 1866.6,
      "duration": 3.88
    },
    {
      "text": "that prompt again passing in the key",
      "start": 1868.399,
      "duration": 4.441
    },
    {
      "text": "information from the travel details and",
      "start": 1870.48,
      "duration": 4.48
    },
    {
      "text": "then running that agent and then we just",
      "start": 1872.84,
      "duration": 4.92
    },
    {
      "text": "set the hotel results to that string the",
      "start": 1874.96,
      "duration": 5.319
    },
    {
      "text": "results. data and then finally for the",
      "start": 1877.76,
      "duration": 5.2
    },
    {
      "text": "activity recommendations it is exactly",
      "start": 1880.279,
      "duration": 4.12
    },
    {
      "text": "the same so I'm just glossing over this",
      "start": 1882.96,
      "duration": 3.48
    },
    {
      "text": "really quick there's nothing new to go",
      "start": 1884.399,
      "duration": 3.76
    },
    {
      "text": "over in this node we just have to to get",
      "start": 1886.44,
      "duration": 4.16
    },
    {
      "text": "it set up and then we have our",
      "start": 1888.159,
      "duration": 5.36
    },
    {
      "text": "synthesizer agent and so this time what",
      "start": 1890.6,
      "duration": 5.679
    },
    {
      "text": "we're going to do is take the state that",
      "start": 1893.519,
      "duration": 5.16
    },
    {
      "text": "we have for each of our parallel agents",
      "start": 1896.279,
      "duration": 4.64
    },
    {
      "text": "because at this point because you set it",
      "start": 1898.679,
      "duration": 5.201
    },
    {
      "text": "up this way in the graph we have all of",
      "start": 1900.919,
      "duration": 4.6
    },
    {
      "text": "that defined it's guaranteed to be",
      "start": 1903.88,
      "duration": 3.72
    },
    {
      "text": "defined for each of those specialized",
      "start": 1905.519,
      "duration": 4.081
    },
    {
      "text": "agents so we get those different pieces",
      "start": 1907.6,
      "duration": 4.72
    },
    {
      "text": "of information and then we build up this",
      "start": 1909.6,
      "duration": 5.0
    },
    {
      "text": "prompt where we are asking it to",
      "start": 1912.32,
      "duration": 4.64
    },
    {
      "text": "summarize all of these recommendations",
      "start": 1914.6,
      "duration": 5.28
    },
    {
      "text": "and then we give it the flight hotel and",
      "start": 1916.96,
      "duration": 4.679
    },
    {
      "text": "activity recommendations and we ask it",
      "start": 1919.88,
      "duration": 4.48
    },
    {
      "text": "to create a comprehensive travel plan",
      "start": 1921.639,
      "duration": 5.201
    },
    {
      "text": "based on these recommendations and then",
      "start": 1924.36,
      "duration": 4.559
    },
    {
      "text": "we just run a stream so we call the Run",
      "start": 1926.84,
      "duration": 4.04
    },
    {
      "text": "stream again and then we're going to",
      "start": 1928.919,
      "duration": 3.401
    },
    {
      "text": "stream a little bit differently it's",
      "start": 1930.88,
      "duration": 3.24
    },
    {
      "text": "simpler this time because it's not a",
      "start": 1932.32,
      "duration": 3.52
    },
    {
      "text": "structured output it's just a regular",
      "start": 1934.12,
      "duration": 3.679
    },
    {
      "text": "string and so we can call the stream",
      "start": 1935.84,
      "duration": 4.52
    },
    {
      "text": "text function instead and it's going to",
      "start": 1937.799,
      "duration": 4.641
    },
    {
      "text": "give us a bunch of different chunks",
      "start": 1940.36,
      "duration": 4.319
    },
    {
      "text": "basically portions of the response that",
      "start": 1942.44,
      "duration": 4.44
    },
    {
      "text": "we can use that custom writer object",
      "start": 1944.679,
      "duration": 4.641
    },
    {
      "text": "that we have here to stream the response",
      "start": 1946.88,
      "duration": 4.56
    },
    {
      "text": "out to the front end like we saw earlier",
      "start": 1949.32,
      "duration": 4.319
    },
    {
      "text": "in streamlet when I gave you that demo",
      "start": 1951.44,
      "duration": 3.959
    },
    {
      "text": "and then finally we can get the response",
      "start": 1953.639,
      "duration": 3.28
    },
    {
      "text": "just like we did with our other agents",
      "start": 1955.399,
      "duration": 4.081
    },
    {
      "text": "and then set the final plan to that",
      "start": 1956.919,
      "duration": 5.36
    },
    {
      "text": "value and that is it we have defined",
      "start": 1959.48,
      "duration": 5.24
    },
    {
      "text": "everything for our agent nodes and so",
      "start": 1962.279,
      "duration": 4.161
    },
    {
      "text": "now we can just Define a couple of the",
      "start": 1964.72,
      "duration": 3.24
    },
    {
      "text": "other pieces that we need like for",
      "start": 1966.44,
      "duration": 4.56
    },
    {
      "text": "example when we make that decision do we",
      "start": 1967.96,
      "duration": 4.8
    },
    {
      "text": "have all the information we need to",
      "start": 1971.0,
      "duration": 3.84
    },
    {
      "text": "continue or do we have to keep asking",
      "start": 1972.76,
      "duration": 3.96
    },
    {
      "text": "the user for more travel details we're",
      "start": 1974.84,
      "duration": 4.719
    },
    {
      "text": "doing this with this routing function",
      "start": 1976.72,
      "duration": 5.559
    },
    {
      "text": "here so first we get the travel details",
      "start": 1979.559,
      "duration": 4.761
    },
    {
      "text": "cuz remember going back to the graph",
      "start": 1982.279,
      "duration": 5.52
    },
    {
      "text": "here this message get next user message",
      "start": 1984.32,
      "duration": 6.52
    },
    {
      "text": "it goes back to gather info and then we",
      "start": 1987.799,
      "duration": 4.84
    },
    {
      "text": "make the decision which one do we route",
      "start": 1990.84,
      "duration": 3.199
    },
    {
      "text": "to and so when we're making that",
      "start": 1992.639,
      "duration": 3.441
    },
    {
      "text": "decision we have the travel details",
      "start": 1994.039,
      "duration": 4.36
    },
    {
      "text": "defined because that happens after the",
      "start": 1996.08,
      "duration": 5.079
    },
    {
      "text": "Gathering info agent so we get the",
      "start": 1998.399,
      "duration": 5.201
    },
    {
      "text": "details and then we just see is all",
      "start": 2001.159,
      "duration": 4.88
    },
    {
      "text": "details given that Boolean value that it",
      "start": 2003.6,
      "duration": 4.72
    },
    {
      "text": "defines right here is this true true or",
      "start": 2006.039,
      "duration": 5.081
    },
    {
      "text": "false and if it's true if they have",
      "start": 2008.32,
      "duration": 5.44
    },
    {
      "text": "given all of the necessary details then",
      "start": 2011.12,
      "duration": 5.279
    },
    {
      "text": "we can move on but if it's false like we",
      "start": 2013.76,
      "duration": 5.24
    },
    {
      "text": "see right here then we have to move on",
      "start": 2016.399,
      "duration": 5.601
    },
    {
      "text": "to that node to get the next user",
      "start": 2019.0,
      "duration": 5.12
    },
    {
      "text": "message and then we'll display in that",
      "start": 2022.0,
      "duration": 3.96
    },
    {
      "text": "response variable to the user like hey I",
      "start": 2024.12,
      "duration": 3.96
    },
    {
      "text": "need the destination or I need the dates",
      "start": 2025.96,
      "duration": 3.92
    },
    {
      "text": "you're going on your trip then we get",
      "start": 2028.08,
      "duration": 4.0
    },
    {
      "text": "that from the user then it comes back",
      "start": 2029.88,
      "duration": 4.159
    },
    {
      "text": "and we would make this decision a second",
      "start": 2032.08,
      "duration": 4.719
    },
    {
      "text": "time after we get a response and so if",
      "start": 2034.039,
      "duration": 5.161
    },
    {
      "text": "we are good to continue if all details",
      "start": 2036.799,
      "duration": 6.12
    },
    {
      "text": "given is true then we can just return a",
      "start": 2039.2,
      "duration": 5.959
    },
    {
      "text": "list of the nodes that we want to move",
      "start": 2042.919,
      "duration": 4.561
    },
    {
      "text": "on to and so when we return a list in a",
      "start": 2045.159,
      "duration": 4.48
    },
    {
      "text": "router function like this in L graph",
      "start": 2047.48,
      "duration": 3.399
    },
    {
      "text": "that means that we're going to execute",
      "start": 2049.639,
      "duration": 3.401
    },
    {
      "text": "all of these nodes in parallel so it is",
      "start": 2050.879,
      "duration": 4.76
    },
    {
      "text": "that easy to get simultaneous execution",
      "start": 2053.04,
      "duration": 5.76
    },
    {
      "text": "of nodes and laning graph just like this",
      "start": 2055.639,
      "duration": 5.801
    },
    {
      "text": "and within our Edge the dictionary or",
      "start": 2058.8,
      "duration": 4.279
    },
    {
      "text": "the array I should say right here this",
      "start": 2061.44,
      "duration": 3.479
    },
    {
      "text": "just defines all the different nodes",
      "start": 2063.079,
      "duration": 4.161
    },
    {
      "text": "that we could route to and so just like",
      "start": 2064.919,
      "duration": 4.2
    },
    {
      "text": "we have a list here we have a subset",
      "start": 2067.24,
      "duration": 3.639
    },
    {
      "text": "that we return these are the ones that",
      "start": 2069.119,
      "duration": 3.28
    },
    {
      "text": "we want to execute which is basically",
      "start": 2070.879,
      "duration": 3.401
    },
    {
      "text": "everything except the get next user",
      "start": 2072.399,
      "duration": 4.921
    },
    {
      "text": "message node and then finally for the",
      "start": 2074.28,
      "duration": 5.76
    },
    {
      "text": "node itself to get the next user message",
      "start": 2077.32,
      "duration": 4.96
    },
    {
      "text": "we're using this concept in Lan graph",
      "start": 2080.04,
      "duration": 4.4
    },
    {
      "text": "called an interrupt this is how you add",
      "start": 2082.28,
      "duration": 4.52
    },
    {
      "text": "human in the loop to L graph which is a",
      "start": 2084.44,
      "duration": 4.479
    },
    {
      "text": "very powerful way to no matter where",
      "start": 2086.8,
      "duration": 4.2
    },
    {
      "text": "you're at in the execution of a l graph",
      "start": 2088.919,
      "duration": 4.96
    },
    {
      "text": "workflow you can stop and wait for the",
      "start": 2091.0,
      "duration": 5.079
    },
    {
      "text": "user to input something so in this case",
      "start": 2093.879,
      "duration": 4.321
    },
    {
      "text": "we're waiting for them to provide a",
      "start": 2096.079,
      "duration": 3.721
    },
    {
      "text": "value and I'll show you later how this",
      "start": 2098.2,
      "duration": 3.6
    },
    {
      "text": "is set up in the streamlet UI we're",
      "start": 2099.8,
      "duration": 3.96
    },
    {
      "text": "waiting for the user to provide a value",
      "start": 2101.8,
      "duration": 5.12
    },
    {
      "text": "which we then set as the user input so",
      "start": 2103.76,
      "duration": 5.24
    },
    {
      "text": "we stop the graph here we're not running",
      "start": 2106.92,
      "duration": 4.28
    },
    {
      "text": "it anymore we wait for them to input a",
      "start": 2109.0,
      "duration": 4.52
    },
    {
      "text": "message and then we set user input to",
      "start": 2111.2,
      "duration": 4.8
    },
    {
      "text": "whatever their message is and because we",
      "start": 2113.52,
      "duration": 4.839
    },
    {
      "text": "have the edge that takes get user",
      "start": 2116.0,
      "duration": 5.4
    },
    {
      "text": "message back to gather info that's how",
      "start": 2118.359,
      "duration": 5.441
    },
    {
      "text": "we then repeat the process of calling",
      "start": 2121.4,
      "duration": 5.48
    },
    {
      "text": "our info Gathering agent and so with",
      "start": 2123.8,
      "duration": 4.64
    },
    {
      "text": "that out of the way we now have",
      "start": 2126.88,
      "duration": 4.12
    },
    {
      "text": "everything we need for our nodes and so",
      "start": 2128.44,
      "duration": 4.0
    },
    {
      "text": "the last thing that I want to add here",
      "start": 2131.0,
      "duration": 3.8
    },
    {
      "text": "is memory for our agent so that it can",
      "start": 2132.44,
      "duration": 4.2
    },
    {
      "text": "remember the state of the graph when we",
      "start": 2134.8,
      "duration": 4.08
    },
    {
      "text": "have that human in the loop interrupt",
      "start": 2136.64,
      "duration": 3.959
    },
    {
      "text": "we're just using a simple memory saver",
      "start": 2138.88,
      "duration": 3.28
    },
    {
      "text": "so it's going to save it on the RAM on",
      "start": 2140.599,
      "duration": 4.281
    },
    {
      "text": "my machine you can set up a SQL light or",
      "start": 2142.16,
      "duration": 4.28
    },
    {
      "text": "a postgress memory saver if you want to",
      "start": 2144.88,
      "duration": 3.199
    },
    {
      "text": "use superbase or something to store all",
      "start": 2146.44,
      "duration": 3.28
    },
    {
      "text": "this state so you can make it very",
      "start": 2148.079,
      "duration": 3.401
    },
    {
      "text": "persistent in production ready as well",
      "start": 2149.72,
      "duration": 3.76
    },
    {
      "text": "if you want I'm just keeping it simple",
      "start": 2151.48,
      "duration": 4.2
    },
    {
      "text": "and then finally we'll just call our",
      "start": 2153.48,
      "duration": 4.839
    },
    {
      "text": "build travel agent graph so that we have",
      "start": 2155.68,
      "duration": 5.52
    },
    {
      "text": "this travel agent graph instance that we",
      "start": 2158.319,
      "duration": 5.04
    },
    {
      "text": "can now reference somewhere else to call",
      "start": 2161.2,
      "duration": 4.159
    },
    {
      "text": "into this graph and that's what we do in",
      "start": 2163.359,
      "duration": 4.121
    },
    {
      "text": "our streamlet UI so for the streamlet",
      "start": 2165.359,
      "duration": 3.76
    },
    {
      "text": "interface let me show you really quickly",
      "start": 2167.48,
      "duration": 4.639
    },
    {
      "text": "how we interact with our agent and so",
      "start": 2169.119,
      "duration": 5.2
    },
    {
      "text": "first we import the travel agent graph",
      "start": 2172.119,
      "duration": 3.96
    },
    {
      "text": "that we just defined right here so we",
      "start": 2174.319,
      "duration": 3.601
    },
    {
      "text": "have an instance of the graph that we",
      "start": 2176.079,
      "duration": 4.52
    },
    {
      "text": "can then use within our UI anywhere and",
      "start": 2177.92,
      "duration": 4.439
    },
    {
      "text": "so in our function specifically to",
      "start": 2180.599,
      "duration": 4.161
    },
    {
      "text": "interact with the agent invoke agent",
      "start": 2182.359,
      "duration": 5.201
    },
    {
      "text": "graph we take in the user input as a par",
      "start": 2184.76,
      "duration": 4.8
    },
    {
      "text": "parameter and then we first Define our",
      "start": 2187.56,
      "duration": 4.36
    },
    {
      "text": "configuration including a thread ID this",
      "start": 2189.56,
      "duration": 4.799
    },
    {
      "text": "is how we can have a unique identifier",
      "start": 2191.92,
      "duration": 5.679
    },
    {
      "text": "for this specific execution of our Lan",
      "start": 2194.359,
      "duration": 5.841
    },
    {
      "text": "graph graph and then if it is the first",
      "start": 2197.599,
      "duration": 5.0
    },
    {
      "text": "message from the user as in the current",
      "start": 2200.2,
      "duration": 4.639
    },
    {
      "text": "chat history just has a length of one",
      "start": 2202.599,
      "duration": 3.801
    },
    {
      "text": "that means we're invoking the graph for",
      "start": 2204.839,
      "duration": 3.161
    },
    {
      "text": "the first time so we build up our",
      "start": 2206.4,
      "duration": 3.6
    },
    {
      "text": "initial state where we have the first",
      "start": 2208.0,
      "duration": 3.8
    },
    {
      "text": "user message and then we have all the",
      "start": 2210.0,
      "duration": 4.599
    },
    {
      "text": "preferences that they set in the UI and",
      "start": 2211.8,
      "duration": 4.72
    },
    {
      "text": "then with all of that we just use the",
      "start": 2214.599,
      "duration": 4.641
    },
    {
      "text": "aam function call for our travel agent",
      "start": 2216.52,
      "duration": 4.68
    },
    {
      "text": "graph giving the initial State the",
      "start": 2219.24,
      "duration": 4.359
    },
    {
      "text": "config that has the thread ID and then",
      "start": 2221.2,
      "duration": 4.6
    },
    {
      "text": "stream mode equals custom is how we have",
      "start": 2223.599,
      "duration": 4.921
    },
    {
      "text": "that writer object passed into our nodes",
      "start": 2225.8,
      "duration": 5.279
    },
    {
      "text": "so that our pantic AI agents can stream",
      "start": 2228.52,
      "duration": 5.839
    },
    {
      "text": "the output in real time to our front end",
      "start": 2231.079,
      "duration": 5.881
    },
    {
      "text": "because we just use this async 4 so that",
      "start": 2234.359,
      "duration": 4.081
    },
    {
      "text": "as we're getting those chunks we're able",
      "start": 2236.96,
      "duration": 4.92
    },
    {
      "text": "to yield those and display them in real",
      "start": 2238.44,
      "duration": 6.12
    },
    {
      "text": "time and then if we have more than just",
      "start": 2241.88,
      "duration": 4.68
    },
    {
      "text": "a single message in the chat history",
      "start": 2244.56,
      "duration": 3.48
    },
    {
      "text": "that means that the convers ation has",
      "start": 2246.56,
      "duration": 3.559
    },
    {
      "text": "already began with our info Gathering",
      "start": 2248.04,
      "duration": 4.72
    },
    {
      "text": "agent and we want to continue it and so",
      "start": 2250.119,
      "duration": 4.761
    },
    {
      "text": "in our graph that's where we have this",
      "start": 2252.76,
      "duration": 4.599
    },
    {
      "text": "interrupt here where we are waiting for",
      "start": 2254.88,
      "duration": 5.239
    },
    {
      "text": "that next value from the user and so to",
      "start": 2257.359,
      "duration": 5.841
    },
    {
      "text": "send in that value we call the agent in",
      "start": 2260.119,
      "duration": 4.881
    },
    {
      "text": "a very similar way as when it's the",
      "start": 2263.2,
      "duration": 4.32
    },
    {
      "text": "first message except instead of passing",
      "start": 2265.0,
      "duration": 4.96
    },
    {
      "text": "in our initial State we're using this",
      "start": 2267.52,
      "duration": 4.64
    },
    {
      "text": "command directive in Lang graph where we",
      "start": 2269.96,
      "duration": 4.68
    },
    {
      "text": "say resume is equal to user input so",
      "start": 2272.16,
      "duration": 4.919
    },
    {
      "text": "whatever you set resume to here that is",
      "start": 2274.64,
      "duration": 5.52
    },
    {
      "text": "what that value gets defined as for that",
      "start": 2277.079,
      "duration": 4.961
    },
    {
      "text": "human in the loop interrupt and so value",
      "start": 2280.16,
      "duration": 4.199
    },
    {
      "text": "is now whatever user message and that's",
      "start": 2282.04,
      "duration": 5.76
    },
    {
      "text": "what's set for the user input State and",
      "start": 2284.359,
      "duration": 5.121
    },
    {
      "text": "so we're just passing in user input for",
      "start": 2287.8,
      "duration": 3.2
    },
    {
      "text": "the resume here and then the rest of it",
      "start": 2289.48,
      "duration": 3.04
    },
    {
      "text": "the same we just give the config and",
      "start": 2291.0,
      "duration": 3.48
    },
    {
      "text": "then the stream mode of custom yield",
      "start": 2292.52,
      "duration": 3.68
    },
    {
      "text": "each message so we're streaming out that",
      "start": 2294.48,
      "duration": 3.44
    },
    {
      "text": "response it's it that's it and I'm not",
      "start": 2296.2,
      "duration": 4.0
    },
    {
      "text": "going to dive into the exact setup for",
      "start": 2297.92,
      "duration": 3.56
    },
    {
      "text": "the streamly interface and everything",
      "start": 2300.2,
      "duration": 2.639
    },
    {
      "text": "like that because that's not the focus",
      "start": 2301.48,
      "duration": 4.2
    },
    {
      "text": "of this video but with that we can now",
      "start": 2302.839,
      "duration": 4.721
    },
    {
      "text": "just I'll show you the command here you",
      "start": 2305.68,
      "duration": 3.639
    },
    {
      "text": "can just run streamlit run and then the",
      "start": 2307.56,
      "duration": 4.24
    },
    {
      "text": "name of the UI I forgot to save which is",
      "start": 2309.319,
      "duration": 3.841
    },
    {
      "text": "why I got that error but yeah you just",
      "start": 2311.8,
      "duration": 3.0
    },
    {
      "text": "run this command and then that'll spin",
      "start": 2313.16,
      "duration": 3.48
    },
    {
      "text": "up the UI in the browser for you so we",
      "start": 2314.8,
      "duration": 3.559
    },
    {
      "text": "can go ahead and chat with our agent and",
      "start": 2316.64,
      "duration": 3.84
    },
    {
      "text": "so I can say my name is Cole my",
      "start": 2318.359,
      "duration": 4.801
    },
    {
      "text": "preferences are I like Ocean Air for my",
      "start": 2320.48,
      "duration": 5.16
    },
    {
      "text": "Airline I really want to have a",
      "start": 2323.16,
      "duration": 4.76
    },
    {
      "text": "restaurant and free breakfast because",
      "start": 2325.64,
      "duration": 4.32
    },
    {
      "text": "I'm just a foodie I guess um and then a",
      "start": 2327.92,
      "duration": 4.199
    },
    {
      "text": "budget level of mid-range I'll sa my",
      "start": 2329.96,
      "duration": 4.24
    },
    {
      "text": "preferences and then just like with our",
      "start": 2332.119,
      "duration": 3.561
    },
    {
      "text": "initial demo let's just have a fun",
      "start": 2334.2,
      "duration": 3.399
    },
    {
      "text": "conversation with it so I'll say I'm",
      "start": 2335.68,
      "duration": 5.88
    },
    {
      "text": "want to go to Spain all right and so",
      "start": 2337.599,
      "duration": 5.76
    },
    {
      "text": "obviously this isn't enough information",
      "start": 2341.56,
      "duration": 4.36
    },
    {
      "text": "at first and so now the agent the info",
      "start": 2343.359,
      "duration": 5.041
    },
    {
      "text": "Gathering agent is going to ask for more",
      "start": 2345.92,
      "duration": 5.04
    },
    {
      "text": "details and it's not the nicest response",
      "start": 2348.4,
      "duration": 4.28
    },
    {
      "text": "it's just very blunt like boom give me",
      "start": 2350.96,
      "duration": 3.6
    },
    {
      "text": "more you could obviously change that in",
      "start": 2352.68,
      "duration": 3.28
    },
    {
      "text": "the system prompt if you want I just",
      "start": 2354.56,
      "duration": 4.0
    },
    {
      "text": "kept it very basic but I'll say I'm",
      "start": 2355.96,
      "duration": 5.76
    },
    {
      "text": "flying from Minneapolis just keep that",
      "start": 2358.56,
      "duration": 7.559
    },
    {
      "text": "same thing going um going June 1st",
      "start": 2361.72,
      "duration": 10.56
    },
    {
      "text": "through the 6th um and I don't want to",
      "start": 2366.119,
      "duration": 10.0
    },
    {
      "text": "spend more than let's just say $250 per",
      "start": 2372.28,
      "duration": 6.36
    },
    {
      "text": "night for a hotel all right so we give",
      "start": 2376.119,
      "duration": 4.401
    },
    {
      "text": "it all the information that it needs and",
      "start": 2378.64,
      "duration": 3.479
    },
    {
      "text": "now yep there we go we have everything",
      "start": 2380.52,
      "duration": 3.599
    },
    {
      "text": "that we need and look at that it invokes",
      "start": 2382.119,
      "duration": 3.561
    },
    {
      "text": "all three of our specialized agents at",
      "start": 2384.119,
      "duration": 3.2
    },
    {
      "text": "the exact same time so we're just",
      "start": 2385.68,
      "duration": 3.88
    },
    {
      "text": "waiting for all three of them to finish",
      "start": 2387.319,
      "duration": 3.921
    },
    {
      "text": "and then it's going to get fed into our",
      "start": 2389.56,
      "duration": 3.84
    },
    {
      "text": "synthesizer agent that streams the",
      "start": 2391.24,
      "duration": 4.28
    },
    {
      "text": "output look at this your comprehensive",
      "start": 2393.4,
      "duration": 4.959
    },
    {
      "text": "travel plans for Spain and and Bam this",
      "start": 2395.52,
      "duration": 5.319
    },
    {
      "text": "is really fast this is using GPT 40 mini",
      "start": 2398.359,
      "duration": 4.601
    },
    {
      "text": "under the hood for the llm for all of",
      "start": 2400.839,
      "duration": 4.76
    },
    {
      "text": "these agents by the way and yeah this is",
      "start": 2402.96,
      "duration": 4.639
    },
    {
      "text": "just awesome again just using all mock",
      "start": 2405.599,
      "duration": 4.24
    },
    {
      "text": "data so it's not like the most amazing",
      "start": 2407.599,
      "duration": 4.0
    },
    {
      "text": "thing but yeah here we go we got our",
      "start": 2409.839,
      "duration": 3.52
    },
    {
      "text": "restaurant this one doesn't have free",
      "start": 2411.599,
      "duration": 4.601
    },
    {
      "text": "Wi-Fi or or free breakfast rather so it",
      "start": 2413.359,
      "duration": 4.201
    },
    {
      "text": "didn't accommodate all of our",
      "start": 2416.2,
      "duration": 2.96
    },
    {
      "text": "preferences but it did for the flight it",
      "start": 2417.56,
      "duration": 3.44
    },
    {
      "text": "said Ocean Air so it did its best based",
      "start": 2419.16,
      "duration": 3.64
    },
    {
      "text": "on the mock data that we gave it yeah",
      "start": 2421.0,
      "duration": 4.52
    },
    {
      "text": "this is working so well and you can take",
      "start": 2422.8,
      "duration": 4.76
    },
    {
      "text": "this kind of architecture and and all",
      "start": 2425.52,
      "duration": 3.36
    },
    {
      "text": "the things that I taught you here with",
      "start": 2427.56,
      "duration": 4.32
    },
    {
      "text": "pantic AI and Lang graph and use this",
      "start": 2428.88,
      "duration": 5.12
    },
    {
      "text": "for your own use case and get really",
      "start": 2431.88,
      "duration": 3.64
    },
    {
      "text": "complex with it you can turn your",
      "start": 2434.0,
      "duration": 3.839
    },
    {
      "text": "synthesizer agent into a validator as",
      "start": 2435.52,
      "duration": 4.28
    },
    {
      "text": "well you can give a ton of powerful",
      "start": 2437.839,
      "duration": 4.0
    },
    {
      "text": "tools to your different specialized",
      "start": 2439.8,
      "duration": 3.72
    },
    {
      "text": "agents to really take advantage of the",
      "start": 2441.839,
      "duration": 3.601
    },
    {
      "text": "fact that you can split up the different",
      "start": 2443.52,
      "duration": 4.04
    },
    {
      "text": "tasks in that way there's so many ways",
      "start": 2445.44,
      "duration": 3.72
    },
    {
      "text": "that you can take this further a lot of",
      "start": 2447.56,
      "duration": 2.799
    },
    {
      "text": "things I want to do with that with my",
      "start": 2449.16,
      "duration": 3.24
    },
    {
      "text": "content going forward as well so there",
      "start": 2450.359,
      "duration": 3.921
    },
    {
      "text": "you have it you now have what it takes",
      "start": 2452.4,
      "duration": 4.24
    },
    {
      "text": "to build specialized AI agents that run",
      "start": 2454.28,
      "duration": 3.48
    },
    {
      "text": "in parallel",
      "start": 2456.64,
      "duration": 3.16
    },
    {
      "text": "and that just unlocks that next level of",
      "start": 2457.76,
      "duration": 4.24
    },
    {
      "text": "building agentic systems that are far",
      "start": 2459.8,
      "duration": 3.519
    },
    {
      "text": "more powerful than what you could do",
      "start": 2462.0,
      "duration": 3.599
    },
    {
      "text": "with just a single AI agent so this",
      "start": 2463.319,
      "duration": 4.641
    },
    {
      "text": "architecture it's not just efficient it",
      "start": 2465.599,
      "duration": 4.681
    },
    {
      "text": "is transformative for the way that",
      "start": 2467.96,
      "duration": 4.359
    },
    {
      "text": "allows you to solve complex problems for",
      "start": 2470.28,
      "duration": 4.039
    },
    {
      "text": "really any use case also I'm planning on",
      "start": 2472.319,
      "duration": 3.76
    },
    {
      "text": "putting out a lot more content in the",
      "start": 2474.319,
      "duration": 3.8
    },
    {
      "text": "near future for different AI agent",
      "start": 2476.079,
      "duration": 4.081
    },
    {
      "text": "architectures and continuing to build",
      "start": 2478.119,
      "duration": 4.601
    },
    {
      "text": "powerful agents with pantic AI and L",
      "start": 2480.16,
      "duration": 5.0
    },
    {
      "text": "graph so if you appreciated this video",
      "start": 2482.72,
      "duration": 3.639
    },
    {
      "text": "and you're looking forward to more",
      "start": 2485.16,
      "duration": 4.64
    },
    {
      "text": "things AI AG pantic Ai and L graph I",
      "start": 2486.359,
      "duration": 5.0
    },
    {
      "text": "would really appreciate a like and a",
      "start": 2489.8,
      "duration": 3.68
    },
    {
      "text": "subscribe and with that I will see you",
      "start": 2491.359,
      "duration": 5.041
    },
    {
      "text": "in the next video",
      "start": 2493.48,
      "duration": 2.92
    }
  ],
  "available_transcripts": {},
  "video_info": {
    "video": {
      "id": "AgN3RHSZGwI",
      "title": "10x Your AI Agents with this ONE Agent Architecture",
      "description": "Complex problems always yield better results when tackled by teams of people with different specializations. The same principle applies to AI agents - individual expertise combined creates exponentially more powerful solutions. Just like people, AI agents perform better the more narrow their role and goals are - it\u2019s all about focus. Taking what could be a single AI agent and fragmenting it into an army of specialized experts.\n\nIn this video, we\u2019ll build a parallel agent architecture using my two favorite frameworks - Pydantic AI and LangGraph, so we can have a group of specialized agents running simultaneously all working to accomplish the same goal.\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nIntegrate anything and automate anything with AI agents using Lutra, check it out here and get started for free!\n\nhttps://lutra.ai/\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nAll the code created in this video can be found here:\n\nhttps://github.com/coleam00/ottomator-agents/tree/main/pydantic-ai-langgraph-parallelization\n\nIf you want to see these AI agent principles used in a full fledged use case (the real deal and it's open source), check out Archon - the AI agent that builds other AI agents using Pydantic AI and LangGraph:\n\nhttps://github.com/coleam00/Archon\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n00:00 - 10x Your Agents with Agent Specialization\n01:52 - Parallel Agent Architecture Explained Simply\n03:37 - Architecture for Our Travel Planner Assistant\n04:40 - Parallel Specialized Agents Demo\n05:41 - Parallel Agents in Archon\n07:15 - Travel Planner Assistant Overview\n08:33 - Building Our First Specialized Agent\n12:53 - Chatting with Our Specialized Agent\n14:15 - Lutra.ai\n16:51 - The Other Specialized Agents\n18:02 - Synthesizer/Aggregator Agent\n18:50 - Info Gathering Agent\n21:00 - Diving into Our LangGraph Implementation\n22:27 - Defining the State for Our Graph\n23:13 - Creating the Graph Structure\n24:59 - Info Gathering Agent Node\n29:11 - Parallel Specialized Agent Nodes\n31:29 - Synthesizer Agent Node\n32:44 - Finishing Our Graph\n36:06 - Using Our Agent with a Frontend\n38:38 - Final Demo\n40:51 - Outro\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nJoin me as I push the limits of what is possible with AI. I'll be uploading videos at least two times a week - Sundays and Wednesdays at 7:00 PM CDT!",
      "publishedAt": "2025-03-24T00:00:07",
      "views": 10190,
      "likes": 456,
      "tags": [
        "ai",
        "artificial intelligence",
        "ai agents",
        "software engineering",
        "software development",
        "coding",
        "automation",
        "saas",
        "development",
        "langgraph",
        "pydantic ai",
        "anthropic agent architecture",
        "ai agent architecture",
        "langgraph + pydantic ai",
        "pydantic ai agents",
        "langgraph agents",
        "ai agent army",
        "pydantic ai guide",
        "langgraph guide",
        "elite ai agents",
        "parallel ai agents",
        "ai agent design",
        "specialized agents",
        "streamlit",
        "streamlit ai agent",
        "langgraph tutorial",
        "pydantic ai tutorial",
        "lutra"
      ],
      "topicDetails": {
        "topicCategories": [
          "https://en.wikipedia.org/wiki/Knowledge",
          "https://en.wikipedia.org/wiki/Technology"
        ]
      },
      "thumbnail": "https://i.ytimg.com/vi/AgN3RHSZGwI/sddefault.jpg",
      "comments": {
        "commentCount": 47,
        "sampleComments": []
      }
    },
    "channel": {
      "id": "UCMwVTLZIRRUyyVrkjDpn4pA",
      "title": "Cole Medin",
      "description": "Artificial Intelligence is no doubt the future of not just software development but the whole world. And I'm on a mission to master it - focusing first on mastering AI Agents.\n\nJoin me as I push the limits of what is possible with AI. \n\nI'll be uploading videos at least two times a week - Sundays and Wednesdays at 7:00 PM CDT! Sundays and Wednesdays are for everything AI, focusing on providing insane and practical educational value. I will also post sometimes on Fridays at 7:00 PM CDT - specifically for platform showcases - sometimes sponsored, always creative in approach!\n",
      "subscriberCount": 100000,
      "videoCount": 111,
      "channelAge": "12.6 years (4604 days)",
      "isVerified": false
    }
  }
}
(youtube_v2_env) ➜  youtube_v2 git:(main) ✗ 